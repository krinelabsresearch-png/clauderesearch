# OTIUM at Vivido: animazione da 12 secondi

L'animazione del flyer OTIUM (Vivido, Firenze, domenica 15/11). Il video è costruito a partire dalla grafica originale: il flyer viene scomposto in livelli separati, poi animati e riassemblati. Le scritte vengono **vettorializzate** e ridisegnate nitide alla risoluzione d'uscita.

Ci sono due grafiche di partenza, con la stessa identica animazione:

| Variante | Sorgente | Livelli | Video |
|---|---|---|---|
| `feed` | `source/flyer.png` (4:5, 1122×1402) | `layers/` | `OTIUM_4x5_*`, `OTIUM_9x16_*` |
| `reel` | `source/flyer_reel.png` (9:16, 941×1672) | `layers_reel/` | `OTIUM_reel_9x16_*` |

Le coordinate di ogni grafica (riquadri dei testi, disco ball, fari, palme, folla) stanno in `scripts/layouts.py`. Si sceglie la variante con la variabile d'ambiente `OTIUM_VARIANT`.

## File finali (`out/`)

| File | Formato | Uso |
|---|---|---|
| `OTIUM_4x5_60fps.mp4` | 1080×1350, 60 fps, audio AAC 320k | feed Instagram e Facebook, versione principale |
| `OTIUM_4x5_30fps.mp4` | 1080×1350, 30 fps | feed, se la piattaforma converte comunque a 30 fps |
| `OTIUM_9x16_60fps.mp4` | 1080×1920, 60 fps | Reel, Storie e TikTok |
| `OTIUM_9x16_30fps.mp4` | 1080×1920, 30 fps | Reel, Storie e TikTok (versione compatibile) |
| `OTIUM_reel_9x16_60fps.mp4` | 1080×1920, 60 fps | **Reel dalla grafica 9:16 dedicata** |
| `OTIUM_reel_9x16_30fps.mp4` | 1080×1920, 30 fps | Reel dalla grafica 9:16 dedicata (versione compatibile) |
| `otium_audio.wav` | stereo, 44,1 kHz | traccia audio a sé, in loop continuo |

La codifica privilegia la qualità sul peso: x264 con CRF 10, preset slower e `tune grain`. Ogni versione viene codificata direttamente dai fotogrammi originali, senza una seconda compressione. I file `.mp4` non sono nel repository perché superano il limite di 100 MB per file di GitHub. Si rigenerano con `bash scripts/build.sh`.

Tutti i video durano **12,0 s** e girano in **loop perfetto**: l'ultimo fotogramma si richiude sulla stella su fondo bordeaux da cui parte il primo.

## Qualità dell'immagine

- **Scritte vettoriali.** Ogni lettera ed elemento grafico ha un contorno ricalcato con precisione sub-pixel (in `layers/vector/`, anche come SVG). Ogni fotogramma lo ridisegna alla risoluzione d'uscita, con antialiasing 4×4 e inchiostro pieno: niente ricampionamento, niente grana sulle lettere.
- **Legature senza giunture.** I pezzi che si toccano (O–T, U–M, le cifre dell'orario) sono composti in un unico strato di copertura, quindi non compare la sottile linea chiara tra un pezzo e l'altro.
- **Grana solo dove serve.** La texture della carta è statica. La grana animata vive solo nel fondo bordeaux dell'apertura e della chiusura.
- **Composizione in due stadi.** La foto (2.5D, disco ball, luci) è composta sulla griglia originale del flyer e ricampionata una sola volta: ridotta con filtro ad area nel feed, ingrandita con Lanczos nel Reel (941 → 1080 px). Le scritte sono disegnate direttamente sul fotogramma finale, quindi restano nitide anche nel Reel ingrandito.

## Timeline (100 BPM: 5 battute = 12 s esatti)

| Battuta | Tempo | Cosa succede |
|---|---|---|
| 1 | 0,0 – 2,4 s | La stella pulsa sul fondo bordeaux con un'onda d'urto a punti e vola nella **O** mentre si apre l'iride di carta. La O atterra a 0,9 s, dopo 1,5 tempi invece di 2: è la riduzione del 25% dell'intro. Poi T, I, U e M si stampano sui colpi del dembow. |
| 2 | 2,4 – 4,8 s | La camera scende sul layout completo e la foto **si stampa a retino**. Entrano "AT VIVIDO", la linea, la stellina e "FIRENZE"; si accendono le teste mobili. |
| 3 | 4,8 – 7,2 s | Entrano "DOMENICA" e poi il timbro **15/11**. La stella grande gira e l'orario **rulla come una slot machine**. |
| 4 | 7,2 – 9,6 s | Entrano i generi. "FREE ENTRY SU PRENOTAZIONE" si scrive in rosso, poi il riquadro si riempie fino al primo tempo della battuta 5. |
| 5 | 9,6 – 12 s | **Drop**: flash sul primo tempo, poi circa 1,9 s con il layout completo fermo. Infine l'iride bordeaux si richiude sulla stella e riparte il loop. |

**Nessuna vibrazione dopo OTIUM.** Il fuori registro risograph e la piccola scossa a tempo ci sono solo mentre si stampano le lettere del logo. Dalla M in poi scritte e foto restano ferme. Si muovono soltanto in modo fluido e continuo:
- la disco ball 3D che ruota;
- i fasci delle teste mobili, i punti di luce sulle pareti e i riflessi stellati;
- le palme che ondeggiano piano;
- la lenta spinta della camera in 2.5D.

## Livelli separati (`layers/` e `layers_reel/`)

- `text/`: 44 sprite RGBA, uno per lettera o elemento, ritagliati dal flyer. Il logo OTIUM è una legatura, quindi è stato diviso a mano: O, stella, T, I, U, M.
- `vector/`: gli stessi elementi in SVG vettoriale. `_all_typography.svg` contiene tutta la tipografia del flyer.
- `photo/`:
  - finestra della foto;
  - piatto con la sfera rimossa (inpainting);
  - le due disco ball;
  - palme e folla;
  - mappa di profondità.
- `00_paper_plate.png`: la carta pulita, senza testi.
- `_overview.png`: foglio di controllo con tutti i livelli.
- `_reconstruction.png`: tutti i livelli rimessi in posizione.

## Audio

L'audio è sintetizzato da zero con numpy e scipy, senza campioni, quindi non ci sono problemi di licenza. È un reggaeton dembow a 100 BPM in La minore (Am, F, C, G, Am):
- cassa 808, rullante e clap sul ritmo dembow, hi-hat e sub bass sul tresillo;
- marimba e pad, con un filtro che si apre durante l'intro.

Gli effetti sonori sono sincronizzati agli eventi visivi: whoosh della stella, timbri tipografici, rumore della pressa durante la stampa, tic delle lettere, cricchetto della slot machine, riser verso il drop, digitazione, impatto sul flash e reverse finale che rilancia il loop.

## Rigenerare tutto

```bash
pip install opencv-python-headless scipy numpy
bash scripts/build.sh
```

Per vedere un fotogramma singolo senza fare il render completo:

```bash
OTIUM_VARIANT=feed python3 scripts/render.py --fmt 4x5 --preview 1.3,5.0,10.5
```

```bash
OTIUM_VARIANT=reel python3 scripts/render.py --fmt 9x16 --preview 1.3,5.0,10.5
```

La timeline (tutti i tempi sono agganciati alla griglia dei 100 BPM) è in cima a `scripts/render.py`. `scripts/audio.py` la importa, quindi suono e immagine restano sincronizzati se si sposta un evento.
