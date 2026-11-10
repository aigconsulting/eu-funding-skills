#!/usr/bin/env python3
"""Calcola un esempio grant a singola aliquota; NON verifica regole del finanziamento."""
import json
import sys
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
from pathlib import Path

CENTS = Decimal("0.01")
REQUIRED = {
    "scenario", "direct_eligible", "other_eligible", "indirect_rate",
    "indirect_base_categories", "funding_rate", "non_eligible", "grant_cap",
}


class InvalidScenario(ValueError):
    pass


def decimal_value(value, name, is_rate=False):
    if isinstance(value, bool) or not isinstance(value, str):
        raise InvalidScenario(f"{name}: usare stringa decimale, non {type(value).__name__}")
    try:
        d = Decimal(value)
    except InvalidOperation as exc:
        raise InvalidScenario(f"{name}: numero invalido") from exc
    if not d.is_finite() or d < 0 or (is_rate and d > 1):
        raise InvalidScenario(f"{name}: usare valore finito e {'fra 0 e 1' if is_rate else 'non negativo'}")
    return d


def eur(x):
    return str(x.quantize(CENTS, rounding=ROUND_HALF_UP))


def estimate(data):
    if not isinstance(data, dict) or set(data) != REQUIRED:
        raise InvalidScenario(f"Campi richiesti esatti: {', '.join(sorted(REQUIRED))}")
    if not isinstance(data["scenario"], str) or not data["scenario"].strip():
        raise InvalidScenario("scenario: descrizione obbligatoria")
    categories = data["direct_eligible"]
    if not isinstance(categories, dict) or not categories:
        raise InvalidScenario("direct_eligible: oggetto non vuoto")
    for name in categories:
        if not isinstance(name, str) or not name or name.startswith("_"):
            raise InvalidScenario("direct_eligible: nomi categoria invalidi")
    direct_values = {key: decimal_value(val, f"direct_eligible.{key}") for key, val in categories.items()}
    base_keys = data["indirect_base_categories"]
    if (not isinstance(base_keys, list) or len(set(map(str, base_keys))) != len(base_keys)
            or any(not isinstance(x, str) or x not in direct_values for x in base_keys)):
        raise InvalidScenario("indirect_base_categories: lista distinta di categorie dirette esistenti")
    indirect_rate = decimal_value(data["indirect_rate"], "indirect_rate", is_rate=True)
    funding_rate = decimal_value(data["funding_rate"], "funding_rate", is_rate=True)
    other = decimal_value(data["other_eligible"], "other_eligible")
    non_eligible = decimal_value(data["non_eligible"], "non_eligible")
    cap = data["grant_cap"]
    if cap is not None:
        cap = decimal_value(cap, "grant_cap")
    direct = sum(direct_values.values(), Decimal(0)) + other
    base = sum((direct_values[k] for k in base_keys), Decimal(0))
    indirect = base * indirect_rate
    eligible = direct + indirect
    theoretical = eligible * funding_rate
    estimated = min(theoretical, cap) if cap is not None else theoretical
    return {
        "scenario": data["scenario"],
        "currency": "EUR",
        "direct_eligible": eur(direct),
        "indirect_base": eur(base),
        "indirect_estimate": eur(indirect),
        "eligible_total": eur(eligible),
        "funding_rate": str(funding_rate),
        "theoretical_grant": eur(theoretical),
        "grant_cap": None if cap is None else eur(cap),
        "estimated_grant": eur(estimated),
        "eligible_cofinancing": eur(eligible - estimated),
        "non_eligible": eur(non_eligible),
        "estimated_funding_gap": eur(eligible + non_eligible - estimated),
        "status": "SIMULAZIONE_ARITMETICA_NON_VINCOLANTE",
        "warning": "Nessuna verifica di costi, tassi, cap, cronologia pagamenti, eventuale cumulo o condizioni del bando. Non è una concessione.",
    }


def main():
    if len(sys.argv) != 2:
        print("Uso: estimate_grant.py /percorso/scenario.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(json.dumps(estimate(data), ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError) as exc:
        print(f"SCENARIO_INVALIDO: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
