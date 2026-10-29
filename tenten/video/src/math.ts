// Funzioni numeriche senza dipendenze, usabili anche dagli script in Node.
export const clamp01 = (x: number) => Math.min(1, Math.max(0, x));
