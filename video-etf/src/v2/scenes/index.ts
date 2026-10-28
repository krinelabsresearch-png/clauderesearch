import type {SceneDef} from '../world';
import {basket} from './Basket';
import {costs} from './Costs';
import {cta} from './Cta';
import {divers} from './Divers';
import {hook} from './Hook';
import {risk} from './Risk';
import {simple} from './Simple';

export const SCENE_DEFS: Record<string, SceneDef> = {hook, basket, divers, costs, simple, risk, cta};
