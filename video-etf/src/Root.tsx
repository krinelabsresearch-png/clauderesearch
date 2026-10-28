import React from 'react';
import {AbsoluteFill, Composition, Freeze, Html5Audio, Sequence, Still, staticFile} from 'remotion';
import {DURATION_FRAMES, FPS, TIMELINE, VOICE_CLIPS, cueSeconds} from './script';
import {C, FONT, H, W} from './theme';
import {Background} from './components/Background';
import {Captions} from './components/Captions';
import {SceneWrap, type Clock} from './components/SceneWrap';
import {HookScene} from './scenes/Hook';
import {BasketScene} from './scenes/Basket';
import {DiversScene} from './scenes/Divers';
import {CostsScene} from './scenes/Costs';
import {SimpleScene} from './scenes/Simple';
import {RiskScene} from './scenes/Risk';
import {CtaScene} from './scenes/Cta';

const SCENE_COMPONENTS: Record<string, React.FC<{clock: Clock}>> = {
  hook: HookScene,
  basket: BasketScene,
  divers: DiversScene,
  costs: CostsScene,
  simple: SimpleScene,
  risk: RiskScene,
  cta: CtaScene,
};

export const EtfVideo: React.FC = () => (
  <AbsoluteFill style={{background: C.bg, fontFamily: FONT}}>
    <Background />
    {TIMELINE.map((s, i) => {
      const Comp = SCENE_COMPONENTS[s.id];
      const last = i === TIMELINE.length - 1;
      return (
        <SceneWrap key={s.id} scene={s} noEnter={i === 0} noExit={last} push={!last}>
          {(clock) => <Comp clock={clock} />}
        </SceneWrap>
      );
    })}
    <Captions />
    {/* Voce: un file per periodo, ognuno nel punto esatto in cui inizia la sua prima frase. */}
    {VOICE_CLIPS.map((v) => (
      <Sequence key={v.file} from={Math.round(v.start * FPS)} layout="none">
        <Html5Audio src={staticFile(`voice/${v.file}`)} />
      </Sequence>
    ))}
  </AbsoluteFill>
);

// Copertina: la griglia che forma "ETF", ferma, con il titolo.
const COVER_FRAME = Math.round((cueSeconds('hook', 'etf') + 1.4) * FPS);

export const Cover: React.FC = () => (
  <AbsoluteFill style={{background: C.bg, fontFamily: FONT}}>
    <Freeze frame={COVER_FRAME}>
      <Background />
      <SceneWrap scene={TIMELINE[0]} noEnter noExit push={false}>
        {(clock) => <HookScene clock={clock} />}
      </SceneWrap>
    </Freeze>
    <div style={{position: 'absolute', top: 250, left: 70, right: 70, textAlign: 'center'}}>
      <div style={{fontWeight: 900, fontSize: 104, lineHeight: 1.02, color: C.text, letterSpacing: '-0.02em'}}>
        Cos’è un <span style={{background: C.green, color: C.ink, padding: '0 18px', borderRadius: 22}}>ETF</span>?
      </div>
      <div style={{marginTop: 26, fontWeight: 700, fontSize: 44, color: C.dim}}>3 vantaggi rispetto alle azioni</div>
    </div>
  </AbsoluteFill>
);

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="ETF" component={EtfVideo} durationInFrames={DURATION_FRAMES} fps={FPS} width={W} height={H} />
    <Still id="Cover" component={Cover} width={W} height={H} />
  </>
);
