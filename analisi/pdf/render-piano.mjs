import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import path from 'path';
const file = 'file://' + path.resolve('report-piano.html');
const footer = `<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:7pt;color:#7c786e;
  padding:0 18mm;display:flex;justify-content:space-between;align-items:center;">
  <span>Kriné Labs · Piano di progetto e richiesta di finanziamento · Riservato</span>
  <span style="font-weight:700;color:#6b4f2a;"><span class="pageNumber"></span></span></div>`;
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage();
await page.goto(file, { waitUntil: 'networkidle' });
await page.pdf({ path: 'cover.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true, pageRanges: '1' });
await page.pdf({ path: 'body.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true, pageRanges: '2-',
  displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: footer });
await browser.close();
console.log('render ok');
