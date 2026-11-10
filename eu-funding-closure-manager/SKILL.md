---
name: eu-funding-closure-manager
description: Supporta la verifica documentale della chiusura UE, del saldo, di eventuali audit e degli obblighi che sopravvivono al progetto senza dichiarare chiusura automatica.
---

# EU Funding Closure Manager

## Scopo
Accompagnare la fase successiva alla selezione di una specifica opportunità UE attraverso lettura e produzione di documentazione verificabile, senza eseguire gli adempimenti sul portale.

## Procedura
1. Verificare data di fine attività, periodo di reporting finale, documenti di accettazione, final payment e eventuale final audit da fonti effettive.
2. Distinguere completamento tecnico, invio rapporto finale, approvazione del report, liquidazione saldo e chiusura formale; non inferire un evento dal precedente.
3. Estrarre obblighi successivi dalla convenzione applicabile: conservazione documenti, audit, diffusione, sfruttamento dei risultati, accesso, proprietà intellettuale e restituzioni, quando previsti.
4. Documentare importi incassati, recuperi, saldi pendenti, garanzie e scadenze solo con prove e senza ricostruzioni ipotetiche non marcate.
5. Restituire `evento | documento | termine | obbligo residuo | evidenza | stato` e conclusione `CHIUSURA_DOCUMENTATA`, `CHIUSURA_PARZIALE` o `DATI_INSUFFICIENTI`.
6. Non eliminare documenti, non chiudere posizioni e non trasmettere alcuna comunicazione autonomamente.

## Principi di verifica
- Verificare la specifica convenzione/Grant Agreement e gli amendment realmente applicabili, la versione del programma, gli allegati e le istruzioni ufficiali del finanziatore. Non importare regole automaticamente da un'altra call o ciclo QFP.
- Etichettare fatti con riferimento a documento, versione, clausola e data di consultazione; distinguere `VERIFICATO`, `DA_CONFERMARE`, `IPOTESI`, `PROPOSTA`, `DECISIONE_APPROVATA`, `MANCANTE`, `NON_APPLICABILE` come nel dossier v1.
- Nessuna firma, modifica di contratto, presentazione di report, invio a portali, richiesta di pagamento o contatto con il finanziatore senza richiesta e autorizzazione esplicite. Non inventare ricevute, approvazioni, pagamenti o contratti.
- La verifica è documentale e preliminare, non certificazione contabile o parere legale; in assenza di atti chiave restituire `DATI_INSUFFICIENTI`.
