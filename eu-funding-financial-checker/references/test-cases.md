# Casi di comportamento da provare con un agente (NON eseguiti)

1. **Budget call 150 milioni, 10 topic:** non affermare che il singolo progetto riceve 150 milioni o 15 milioni.
2. **Topic indica “expected EU contribution 2–3 milioni”**: descrivere come importo indicativo, non massimale vincolante se non espressamente previsto.
3. **Grant Horizon RIA 100%**: specificare che copre al massimo costi ammissibili; i costi esclusi restano fuori.
4. **Grant Horizon IA impresa**: verificare rate 70% nelle condizioni del topic, non attribuirlo a ogni programma.
5. **Horizon IA ente non profit**: verificare effettivo diritto all'eccezione e regole del topic, non inferire 100% dalla sola dichiarazione “associazione”.
6. **Digital Europe SIMPLE**: non applicare un generico 100% Horizon; leggere tipo di azione e call document.
7. **Subappalto e indiretti HE**: escludere il subappalto dalla base del 25%, se la regola è quella applicabile.
8. **Costo computer 100.000 €**: verificare se è eleggibile solo ammortamento e quota d'uso, non assumere acquisto integralmente ammissibile.
9. **IVA recuperabile**: non classificarla come costo eleggibile senza la regola specifica.
10. **Lump sum 500.000 €**: non simulare rimborso percentuale di ogni fattura; distinguere deliverable/work packages e condizioni di pagamento.
11. **Prestito 1 milione**: non presentarlo come contributo a fondo perduto.
12. **EIC blended grant + equity**: distinguere sovvenzione e investimento, inclusa possibile diluizione; non inventare cap table.
13. **Contributo per progetto vs partner:** ripartizione solo se nota/approvata; non dividere in parti uguali.
14. **Anticipo 80%**: non sommarlo al grant massimo; controllare data sheet e trattenute.
15. **MIM Horizon 2026–2027**: non utilizzare 5% in modo automatico; Annexes menzionano 5–8%, contratto determina il tasso del caso.
16. **Costi ammissibili 100.000 €, grant 70%, non ammissibili 40.000 €**: quota non coperta totale 70.000 €, non 30.000 €.
17. **Tasso non riportato nel topic, niente documenti:** `NON_VERIFICATO`, nessun tasso supposto.
18. **Topic regionale PR FESR**: usare avviso regionale e regime aiuti, non il 25% HE.
19. **Quota beneficiario non ammissibile al finanziamento ma partecipa:** grant per lui zero solo se esclusione accertata; non derivare automaticamente una quota dei fondi del consorzio.
20. **Stesso costo imputato a due grant:** segnalare possibile doppio finanziamento salvo sinergia formalmente prevista e documentata.
21. **Finanziamento 100% con anticipo solo 20%**: evidenziare possibile fabbisogno temporaneo di cassa, non equipararlo al cofinanziamento finale.
22. **Scenario con percentuale 70% e massimale vincolante 50.000 €**: calcolatore applica `min` e segnala la riduzione del contributo teorico.

I casi sopra sono **specifiche di test agentico**, non prove eseguite. Le prove numeriche automatizzate sono solo in `scripts/test_calculations.py`.
