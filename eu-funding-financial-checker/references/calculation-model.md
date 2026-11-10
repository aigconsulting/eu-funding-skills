# Modello di calcolo — esempio, non autorizzazione finanziaria

Il calcolatore in `scripts/estimate_grant.py` effettua **soltanto** una simulazione per **una singola aliquota** in un grant calcolato sui costi ammissibili. Non valida voci, tassi, cap, tipologia di grant, cofinanziamento esterno, ammortamenti, cumulo, IVA o normativa; serve per controllare l'aritmetica di dati già qualificati.

## Input JSON

```json
{
  "scenario": "Esempio IA Horizon — ipotesi didattiche, NON topic reale",
  "direct_eligible": {
    "personnel": "100000.00",
    "purchases": "30000.00",
    "subcontracting": "20000.00",
    "third_party_support": "0.00"
  },
  "other_eligible": "0.00",
  "indirect_rate": "0.25",
  "indirect_base_categories": ["personnel", "purchases"],
  "funding_rate": "0.70",
  "non_eligible": "10000.00",
  "grant_cap": null
}
```

Ogni importo è una stringa decimale non negativa in euro. `funding_rate` e `indirect_rate` vanno da 0 a 1. `grant_cap` è **il massimale vincolante del grant per quel perimetro**, se confermato; non passarvi il budget della call/topic. `indirect_base_categories` deve essere un sottoinsieme di `direct_eligible`; l'utilizzatore è responsabile dell'esclusione di categorie non ammesse alla base. `other_eligible` serve solo per categorie dirette **aggiuntive non già incluse** e non entra nella base indiretti: non usarla per duplicare costi.

Il calcolatore richiede **tutti** i campi e distingue `null` da zero per il cap. Se un importo o tasso non è verificato, non inserirvi un numero fittizio a meno che lo scenario sia marcato *illustrativo*; l'output è sempre qualificato come **simulazione aritmetica non vincolante**.

## Formule

- `direct = sum(direct_eligible) + other_eligible`
- `indirect_base = sum(direct_eligible[category] for category in indirect_base_categories)`
- `indirect = indirect_base × indirect_rate`
- `eligible_total = direct + indirect`
- `theoretical_grant = eligible_total × funding_rate`
- `estimated_grant = min(theoretical_grant, grant_cap)` se cap presente
- `estimated_funding_gap = eligible_total + non_eligible − estimated_grant`
- `eligible_cofinancing = eligible_total − estimated_grant`

L'eventuale `grant_cap` deve essere compatibile con l'azione e con il perimetro in analisi; il calcolatore non riconcilia massimali combinati fra partner o intensità differenziate. Il fabbisogno non coperto è **diverso** dal fabbisogno di cassa a breve, che richiede un calendario di flussi reali. Non applicare questa formula a grants lump sum, unit cost o finanziamenti misti senza un modello ad hoc.

## Esempio numerico (NON un grant approvato)

- Diretti: 100.000 + 30.000 + 20.000 = 150.000 €.
- Base indiretti **solo** personale + acquisti: 130.000 €.
- Indiretti flat 25%: 32.500 €.
- Totale eleggibile: 182.500 €.
- Con tasso ipotetico 70%: 127.750 €.
- Quota non coperta dei costi eleggibili: 54.750 €.
- Aggiungendo 10.000 € di costi non eleggibili: fabbisogno non coperto totale = 64.750 €.

Un tasso «70%» NON equivale necessariamente a «30% del budget totale da mettere di tasca propria»: bisogna considerare costi esclusi, cap, ruolo nel consorzio e fonti finanziarie compatibili.

### Comando

`python3 eu-funding-financial-checker/scripts/estimate_grant.py /percorso/input.json`

Output JSON con tutti i risultati in EUR e avvertenza esplicita. Nessun dato viene trasmesso a servizi esterni.
