# OTIUM at Vivido: animazione da 10 secondi

L'animazione del flyer OTIUM (Vivido, Firenze, domenica 15/11). Il video è costruito a partire dalla grafica originale: il flyer viene scomposto in livelli separati, che vengono animati uno per uno e poi riassemblati.

## File finali (`out/`)

| File | Formato | Uso |
|---|---|---|
| `OTIUM_4x5_60fps.mp4` | 1080×1350, 60 fps, audio AAC | feed Instagram e Facebook, versione principale |
| `OTIUM_4x5_30fps.mp4` | 1080×1350, 30 fps | feed, se la piattaforma converte comunque a 30 fps |
| `OTIUM_9x16_60fps.mp4` | 1080×1920, 60 fps | Reel, Storie e TikTok |
| `OTIUM_9x16_30fps.mp4` | 1080×1920, 30 fps | Reel, Storie e TikTok (versione compatibile) |
| `otium_audio.wav` | stereo, 44,1 kHz | traccia audio a sé, in loop continuo |

I video sono codificati per la massima qualità: x264 con CRF 12, preset slower e `tune grain`, così il retino e la grana restano intatti. Ogni versione viene codificata direttamente dai fotogrammi originali, senza una seconda compressione. I file `.mp4` non sono nel repository perché il 9:16 a 60 fps supera il limite di 100 MB per file di GitHub. Si rigenerano con `bash scripts/build.sh`, in circa 6 minuti.

Tutti i video durano 10,0 s e girano in **loop perfetto**: l'ultimo fotogramma si richiude sulla stella su fondo bordeaux da cui parte il primo.

## Timeline (96 BPM: 4 battute = 10 s esatti)

| Battuta | Tempo | Cosa succede |
|---|---|---|
| 1 | 0,0 – 2,5 s | Fondo bordeaux stampato a retino. La stella a 8 punte pulsa sulla cassa e manda un'onda d'urto a punti. Poi vola nella **O**, mentre un'iride di carta si apre con il bordo a retino. Il logo è al centro dello schermo: O, T, I, U e M si stampano una per colpo, a tempo con il dembow. |
| 2 | 2,5 – 5,0 s | Sul primo tempo la camera scende sul layout completo e la foto **si stampa a retino**, prima i punti scuri. "AT VIVIDO" sale lettera per lettera, la linea si disegna, la stellina si apre ed entra "FIRENZE". Si accendono le teste mobili. |
| 3 | 5,0 – 7,5 s | Entra "DOMENICA", poi **15/11** si imprime come un timbro (tremolio della carta e fuori registro del rosso). La stella grande gira, l'orario **rulla come una slot machine** con sfocatura di movimento reale, i generi entrano a tempo. |
| 4 | 7,5 – 10 s | "FREE ENTRY SU PRENOTAZIONE" si scrive in rosso, poi il riquadro rosso si riempie e il testo diventa negativo. Flash stroboscopico, quindi circa 1,4 s con il layout completo fermo, buono per uno screenshot. Infine un'iride di bordeaux si richiude sulla stella e riparte il loop. |

Effetti sempre attivi:
- **Disco ball 3D procedurale** che ruota davvero. Ogni tassello riflette la mappa di luce della foto originale, quindi il disegno della sfera resta quello del flyer.
- Riflessi stellati sulla sfera, punti di luce che scorrono sulle pareti e fasci delle teste mobili stampati a retino.
- Spinta lenta della camera in **2.5D** su una mappa di profondità: la folla è più vicina della struttura.
- La folla **salta sulla cassa** a 12 fps (passo uno) con fasi diverse per ogni persona. Le palme ondeggiano.
- Look da stampa risograph:
  - grana e tremolio della carta a 12 fps;
  - **fuori registro della lastra rossa** a ogni colpo, calcolato separando davvero gli inchiostri rosso e prugna.

## Livelli separati (`layers/`)

- `text/`: 44 sprite RGBA, uno per lettera o elemento, ritagliati dal flyer. Il logo OTIUM è una legatura, quindi è stato diviso a mano: O, stella, T, I, U, M.
- `photo/`:
  - finestra della foto;
  - piatto con la sfera rimossa (inpainting);
  - le due disco ball;
  - palme e folla;
  - mappa di profondità.
- `00_paper_plate.png`: la carta pulita, senza testi.
- `_overview.png`: foglio di controllo con tutti i livelli.
- `_reconstruction.png`: tutti i livelli rimessi in posizione. È identico al flyer (PSNR circa 41 dB).

## Audio

L'audio è sintetizzato da zero con numpy e scipy, senza campioni, quindi non ci sono problemi di licenza. È un reggaeton dembow a 96 BPM in La minore:
- cassa 808, rullante e clap sul ritmo dembow, hi-hat e sub bass sul tresillo;
- marimba e pad, con un filtro che si apre durante l'intro.

Gli effetti sonori sono sincronizzati agli eventi visivi: whoosh della stella, timbri tipografici, rumore della pressa durante la stampa, tic delle lettere, cricchetto della slot machine, riser, digitazione, impatto sul flash e reverse finale che rilancia il loop.

## Rigenerare tutto

```bash
pip install opencv-python-headless scipy numpy
bash scripts/build.sh
```

Per vedere un fotogramma singolo senza fare il render completo:

```bash
python3 scripts/render.py --fmt 4x5 --preview 1.3,5.0,9.0
```

La timeline (tutti i tempi sono agganciati alla griglia dei 96 BPM) è in cima a `scripts/render.py`. `scripts/audio.py` la importa, quindi suono e immagine restano sincronizzati se si sposta un evento.
