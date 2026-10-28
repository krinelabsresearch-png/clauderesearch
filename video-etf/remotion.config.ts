import {Config} from '@remotion/cli/config';

// Chromium headless preinstallato nel container: evita il download di Remotion.
Config.setBrowserExecutable(
  '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell',
);
Config.setVideoImageFormat('jpeg');
Config.setJpegQuality(94);
Config.setCrf(15);
Config.setPixelFormat('yuv420p');
Config.setConcurrency(4);
