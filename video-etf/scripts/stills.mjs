// Fotogrammi singoli per la revisione, con un solo bundle e un solo browser.
// Uso: node scripts/stills.mjs <composizione> <cartella> <frame,frame,...|every:N> [qualità]
import path from 'node:path';
import {mkdirSync} from 'node:fs';
import {bundle} from '@remotion/bundler';
import {openBrowser, renderStill, selectComposition} from '@remotion/renderer';

const [id = 'ETFLiquid', outDir = 'out/stills', spec = 'every:60', quality = '1'] = process.argv.slice(2);
const browserExecutable = '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell';
const chromiumOptions = {gl: 'swangle'};
const inputProps = {quality: Number(quality)};

mkdirSync(outDir, {recursive: true});
const serveUrl = await bundle({entryPoint: path.resolve('src/index.ts')});
const browser = await openBrowser('chrome', {browserExecutable, chromiumOptions});
const composition = await selectComposition({serveUrl, id, inputProps, puppeteerInstance: browser, browserExecutable, chromiumOptions});
const frames = spec.startsWith('every:')
  ? Array.from({length: Math.ceil(composition.durationInFrames / Number(spec.slice(6)))}, (_, i) => i * Number(spec.slice(6)))
  : spec.split(',').map(Number);
for (const frame of frames) {
  await renderStill({
    composition, serveUrl, frame, inputProps, puppeteerInstance: browser, browserExecutable, chromiumOptions,
    imageFormat: 'jpeg', jpegQuality: 90, output: path.join(outDir, `f${String(frame).padStart(5, '0')}.jpg`),
  });
}
await browser.close({silent: true});
console.log(`${frames.length} fotogrammi in ${outDir}`);
