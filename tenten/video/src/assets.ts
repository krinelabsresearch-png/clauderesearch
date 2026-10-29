// Immagini e font del reel: caricati una volta prima del primo fotogramma.
import {continueRender, delayRender, staticFile} from 'remotion';

const PHOTOS = ['folla', 'pista', 'ragazze', 'brindisi', 'gioco', 'dj', 'mc', 'boy'];
const FILES: Record<string, string> = {
  ...Object.fromEntries(PHOTOS.flatMap((k) => [[k, `img/${k}.jpg`], [`${k}_depth`, `img/${k}_depth.png`]])),
  coin: 'img/coin.png',
  buzzer: 'img/buzzer.png',
  bottle: 'img/bottle.png',
  xo: 'img/xo-logo.png',
};

export const IMG: Record<string, HTMLImageElement> = {};

let loading: Promise<void> | null = null;
const loadAll = () =>
  (loading ??= Promise.all([
    ...Object.entries(FILES).map(
      ([k, f]) =>
        new Promise<void>((res, rej) => {
          const img = new Image();
          img.onload = () => {
            IMG[k] = img;
            res();
          };
          img.onerror = () => rej(new Error(`immagine mancante: ${f}`));
          img.src = staticFile(f);
        }),
    ),
    new FontFace('Anton', `url(${staticFile('fonts/anton.woff2')})`).load().then((f) => {
      document.fonts.add(f);
    }),
  ]).then(() => undefined));

// avvia il caricamento appena il modulo viene letto e trattiene il render finché non è finito
if (typeof document !== 'undefined') {
  const handle = delayRender('immagini e font');
  loadAll().then(
    () => continueRender(handle),
    (e) => {
      throw e;
    },
  );
}
