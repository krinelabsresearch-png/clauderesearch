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

## Candidati in ricerca (ondata 1 e 2)
| ID | Candidato | Stato |
|---|---|---|
| 091 | Voce amica: telefonata AI quotidiana agli anziani soli, riassunto ai figli | in ricerca |
| 092 | Allenatore AI dell'esame orale | in ricerca |
| 093 | Tutor di matematica AI a voce per bambini 6–13, pensato per i minori | in ricerca |
| 094 | Coach AI di lettura ad alta voce per bambini 6–10 | in ricerca |
| 095 | Orientamento AI basato sui dati (università e lavoro) | in ricerca |
| 096 | Tutor AI per gli esami di matematica e fisica del primo anno | in ricerca |
| 098 | Coach AI per ADHD e funzioni esecutive (adulti) | in ricerca |
| 099 | Storie audio AI personalizzate su Toniebox/Yoto | in ricerca |
| 100 | Libro della vita dei nonni con interviste telefoniche AI | in ricerca |
| 101 | Palestra sociale AI per giovani adulti | in ricerca |
| 102 | Tracker AI dei capelli | in ricerca |
| 103 | Assistente AI per i caregiver familiari | in ricerca |
| 104 | Coach AI di forza ed equilibrio per over 60 | in ricerca |
| 105 | Assistente di viaggio per l'Europa delle nuove regole | in ricerca |
| 106 | Coach AI per perimenopausa e menopausa | in ricerca |
| 107 | Assistente AI per la tesi con dati | in ricerca |
| 108 | Preparazione AI ai concorsi pubblici | in ricerca |
| 109 | Matematica per lavorare con l'AI (adulti) | in ricerca |
| 110 | Laboratorio AI per ragazzi 9–14, sicuro per i minori | in ricerca |
| 111 | Preparazione atletica e prevenzione infortuni per il padel | in ricerca |

(La 097 è stata assorbita dalla 093 e dalla 096.)

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
