# Stato della ricerca "bisogni dei prossimi 1–5 anni" (per la ripartenza)

**Richiesta di Lorenzo (13/10/2026):**
- ricerca approfondita sui bisogni dei prossimi 1–5 anni nel mercato UE (nuove generazioni, tecnologie, limitazioni in arrivo);
- per ogni candidato, risposte a tutte le sue domande, con analisi approfondita dei concorrenti;
- in lista solo i candidati che, dopo le domande, restano **sopra 3,5** nella scheda v2;
- la lista va consegnata solo quando ci sono **almeno 10 candidati diversi**;
- se finiscono i crediti, si riparte in automatico: messaggio programmato alle 05:11 UTC del 13/10/2026.

**Esito precedente:** la 082 (compagno GLP-1) è bocciata, perché sull'App Store italiano ci sono Shotsy e almeno altre 10 app. Le idee 083–090 non interessano.

## Le domande da fare a ogni candidato
Vengono dalle sue richieste sulle idee 074, 075, 077, 081 e 082.
1. Mercato: c'è davvero?
2. Concorrenti: analisi approfondita in Italia, UE e USA, con prezzi, trazione, lingua italiana e alternative gratuite.
3. Come fanno oggi le persone?
4. Cosa vendiamo che ChatGPT non fa già?
5. Perché dovrebbero pagare, e quanto?
6. Come si monetizza? Può fare davvero 1 M€?
7. È rischioso?
8. Si raggiunge l'acquirente? Quanto costa acquisirlo (CAC)?
9. Come si costruisce? Da dove vengono i dati? Che algoritmo usa e che informazioni dà?
10. Perché adesso, e per quanto resta aperta la finestra?
11. Voti della scheda v2.
12. Cosa la ucciderebbe e qual è il test più economico.

## Esito delle ondate 1 e 2 (20 candidati, ricerca conclusa il 13/10/2026)
- Punteggi in `punteggi.py`; risposte complete alle domande (e concorrenti) in `dossier/`.
- **Sopra 3,5: solo la 107** (assistente AI per la tesi con dati, 3,65).
- Vicine alla soglia:
  - 096 tutor universitario di matematica (3,50);
  - 109 matematica per lavorare con l'AI (3,40);
  - 093 tutor di matematica per bambini (3,35);
  - 092 allenatore dell'orale (3,30).
- **Collo di bottiglia comune:** "potenziale > 1 M€ senza dipendenti" vale 2 su 5 (o 1) per tutti e 20. Con la sola Italia servono troppi clienti rispetto al mercato, oppure il costo di acquisizione supera il valore del cliente. Seguono:
  - "lo fa già ChatGPT/Gemini" (difendibilità 1–2);
  - concorrenti già presenti in italiano o in UE.
- Decisione chiesta a Lorenzo (13/10, ore 10:20 UTC):
  - continuare con nuove ondate;
  - abbassare l'asticella del fatturato;
  - ammettere il B2B;
  - avere subito i migliori.

  Chiesti anche i suoi voti di motivazione sulle idee vicine alla soglia.

## Regole di decisione
- **Punteggio** con la scheda v2: pesi in `../scheda_v2.py`, voti in `punteggi.py`.
- **Motivazione:** è una stima prudente, basata sui suoi interessi dichiarati; accanto si mostra sempre il punteggio con motivazione neutra (3).
- **Soglia:** in lista solo con punteggio maggiore di 3,5, cioè almeno 3,55.
- **Se i candidati sopra soglia sono meno di 10:** nuova ondata di candidati, poi consegna.

## Prossimi passi
1. Ricevere le 10 ricerche e scrivere un dossier per ogni candidato in `dossier/`.
2. Calcolare i punteggi e separare chi va in lista da chi viene scartato (`scartate.md`).
3. Se servono, aggiungere altri candidati.
4. Scrivere `README.md` (la lista), fare commit e push, poi rispondere a Lorenzo.
