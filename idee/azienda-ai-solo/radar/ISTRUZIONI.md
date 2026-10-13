# Radar B6: come farlo girare

Da questo ambiente cloud non posso raggiungere Meta né Apple: la rete li blocca (`graph.facebook.com`, `itunes.apple.com`). Hai due strade:
- **A. Lo lanci tu sul Mac** (consigliato: 10 minuti, nessuna installazione, basta Python 3).
- **B. Apri la rete dell'ambiente cloud** e lo lancio io: menu dell'ambiente cloud nel titolo della sessione → Edit → Network access → aggiungi `graph.facebook.com`, `itunes.apple.com` e `rss.applemarketingtools.com` agli Allowed domains (lasciando spuntato "Allow package managers"). Guida: https://code.claude.com/docs/en/cloud-environments#network-access

---

## 1. Radar App Store: subito, senza chiavi

```bash
git clone <il repository> && cd clauderesearch/idee/azienda-ai-solo/radar
python3 radar_appstore.py                     # USA contro IT, ES, DE, FR (~5–10 minuti)
python3 radar_appstore.py --paesi it          # solo Italia
```
Produce `radar_b6.csv`: le app AI tra le più redditizie negli USA, con un **gap** per Paese che è alto quando l'app:
- non c'è nello store locale, o
- non supporta la lingua, o
- non entra nelle classifiche locali e ha poche recensioni.

**Mandami il CSV** (oppure lancialo con `--paesi it` e incolla le prime 25 righe): lo analizzo e faccio la verifica qualitativa (recensioni negative, prezzi, concorrenti locali).

Limite da sapere: il feed delle classifiche per incassi è il vecchio feed RSS di Apple. Se un giorno smettesse di rispondere, lo script lo segnala e lo sostituisco.

---

## 2. Radar Meta: serve un token (la parte che solo tu puoi fare)

L'accesso a Facebook su Chrome non basta: Meta chiede passaggi legati alla tua identità che non posso fare al posto tuo (caricare un documento, accettare i termini per sviluppatori a tuo nome).

1. **Conferma dell'identità:** vai su https://www.facebook.com/ID e segui la procedura "Conferma la tua identità e la tua posizione" (documento + eventualmente un codice). L'approvazione può richiedere da qualche ora a qualche giorno.
2. **Account sviluppatore:** https://developers.facebook.com → "Inizia" → registrati come sviluppatore (verifica con telefono o carta).
3. **Crea un'app:** "Le mie app" → "Crea app" → tipo "Altro" → "Business" (nessuna revisione necessaria per la libreria pubblicitaria).
4. **Token:** apri https://developers.facebook.com/tools/explorer → scegli la tua app → "Generate Access Token". Poi su https://developers.facebook.com/tools/debug/accesstoken premi "Extend Access Token" per un token da ~60 giorni.
5. **Prova:**
   ```bash
   export META_TOKEN='incolla-qui-il-token'
   python3 radar_meta.py --paesi IT --termini "AI" --max-pagine 2
   ```
   Se risponde con un errore su identità o permessi, il passo 1 non è ancora approvato.
6. **Uso normale** (una volta a settimana; dalla seconda esecuzione calcola la crescita):
   ```bash
   python3 radar_meta.py --paesi IT,ES,DE,FR --termini "AI,intelligenza artificiale,app"
   ```

**Il token è una password:** non incollarlo in chat e non metterlo nel repository. Se vuoi che il radar giri da solo nell'ambiente cloud, va salvato tra i secret dell'ambiente.
