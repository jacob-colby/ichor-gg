export interface StatValue {
  base: number;
  per_level: number;
}

export interface Ability {
  slot: string;
  name: string;
  cooldown?: number[];
  cost?: number[];
  description?: string;
  details?: string[];
}

export interface Aspect {
  name: string;
  kit_changes: string;
}

/** Emitted by pipeline/smite/abilities.py (Task P1) — a derived, not scraped,
 * 20-level upgrade order. Absent for stance gods with no levelable abilities
 * (Artio, Merlin, Ullr) — the UI must hide the section, not placeholder it. */
export interface AbilityOrder {
  order: string[];
  summary: { max_order: string[]; ult_levels: number[] };
}

export interface God {
  type: string;
  name: string;
  pantheon: string;
  role: string;
  specializations: string[];
  damage_type: string;
  release_date: string;
  base_stats: Record<string, StatValue>;
  abilities: Ability[];
  aspects: Aspect[];
  source_url: string;
  last_verified: string;
  ability_order?: AbilityOrder;
  /** Counts of what this god's kit does TO you, read off the ability text by
   *  pipeline/smite/threat_kit.py. Optional: an index built before it shipped
   *  simply falls back to the role labels. */
  threat_kit?: { hard_cc: number; slow: number; heal: number; shield: number; wall: number };
}

export interface Item {
  type: string;
  name: string;
  tier: number | string;
  cost: number;
  /** The one god who can buy this, for a `God Specific` item — Ratatoskr's
   *  three acorns and Aladdin's Genie's Lamp today.
   *
   *  It has always been in index.json and was never declared here, so the
   *  viewer had no way to say that an item on a build is unbuyable for every
   *  other god in the game. `scoring.is_buildable` enforces exactly that on the
   *  pipeline side; this is the same fact, made sayable on the surface. */
  god?: string;
  stats: Record<string, string>;
  passive: string;
  builds_from: string[];
  builds_into: string[];
  source_url: string;
  last_verified: string;
  effect_tags?: string[];
  efficiency_tier?: string | null;
  /** The gold-value model's working, not just its verdict. Null for items
   * outside the scored pool: non-numeric cost, tier-1 starters (passive-priced,
   * so they sit out the regression), and statless items, whose "residual" is
   * just their cost against the intercept and means nothing at all.
   * `cost - predicted_cost === residual` holds exactly. */
  efficiency?: {
    /** What the item's stats are worth at the fitted per-stat gold prices. */
    predicted_cost: number;
    /** actual - predicted. Negative = underpriced. */
    residual: number;
    /** Min-max normalised value across the scored set, 1 = best value. */
    score: number;
    /** Whether this price belongs on a ranking against every other item.
     *  False for god-specific items: the number is real, but only one god can
     *  act on it, so it sorts with its own kind rather than heading the board. */
    comparable?: boolean;
  } | null;
  /** Community record. `matches` is the item's own denominator from the god
   *  index; `gods` is the legacy fallback (a count of builds listing it, not
   *  a sample size). Exactly one of them is present. */
  meta?: { win_avg: number; matches?: number; matches_won?: number; gods?: number };
}

export interface CommunitySlotEntry {
  name: string;
  pick_rate: number;
  win_rate: number;
  alternates?: { name: string; pick_rate: number; win_rate: number }[];
}

export type SlotEntry = string | CommunitySlotEntry;

export interface SituationalSwap {
  vs_tag: string;
  swap: string;
  swap_item?: string | null;
}

/** Emitted by build_index (Task P2) on the community entry — every item this
 * god's playerbase actually buys, deduped across slots (highest pick_rate
 * wins) and sorted pick-rate descending. Distinct from slot_order, which is
 * the ordered build; this is the "what do people buy" list. Absent/empty for
 * gods with no community data. */
export interface PopularItem {
  name: string;
  pick_rate: number;
  win_rate: number;
}

export interface CommunityBuildEntry {
  source: "community";
  aspect: string | null;
  aspect_pick_rate: number | null;
  aspect_win_rate: number | null;
  slot_order: CommunitySlotEntry[];
  /** What this god's players actually open with, top 3 by pick rate. Distinct
   *  from `starter`, which is a role RULE from _weights.yaml and so gives every
   *  Carry the same opener regardless of what Carry players bought. */
  community_starters?: PopularItem[];
  source_url: string;
  last_verified?: string;
  starter?: { base: string; upgrade: string };
  popular_items?: PopularItem[];
}

/** Per-item score breakdown stamped by the Python pipeline (2dp). win 0.5
 * means "no data" neutral; pick 0 means unpicked. */
export interface SlotScore {
  total: number;
  efficiency: number;
  win: number;
  pick: number;
  fit: number;
}

export interface CuratedBuildEntry {
  source: "pro" | "mine" | "suggested";
  archetype?: string;
  name?: string;
  aspect?: string;
  rationale?: string;
  slot_order: string[];
  flex_slots?: string[];
  situational_swaps?: SituationalSwap[];
  notes?: string;
  starter?: { base: string; upgrade: string };
  /** Off-class for-fun build — win/pick signals zeroed, not meta-scored. */
  fun?: boolean;
  slot_scores?: Record<string, SlotScore>;
  /** Hybrid builds only: where the community's record overrode the model, and
   *  the evidence that earned it. A correction that can't say why it fired is
   *  just a third opinion. */
  swaps?: HybridSwap[];
}

export interface HybridSwap {
  added: string;
  removed: string;
  reason: string;
}

export type BuildEntry = CommunityBuildEntry | CuratedBuildEntry;

export interface BuildNote {
  type: string;
  god: string;
  mode: string;
  builds: BuildEntry[];
  last_verified?: string;
}

export interface RosterGod {
  name: string;
  thumb?: string;
}

/** One subject's standing, measured from real matches.
 *
 * This used to carry two scores — `ours` and `community` — and the site led
 * with the disagreement between them. `ours` for a god was the mean blended
 * score of the six items we picked for it, which measured nothing about the
 * god; against real win rates it correlated +0.28, while the model's own half
 * of it correlated −0.117. See `pipeline/smite/tierlist.py` for the numbers.
 * There is one ranking now, and it comes from outcomes. */
export interface TierEntry {
  name: string;
  /** Wilson lower bound on real wins/matches — the ranking. Null when the
   *  sample is too thin to say anything, which is left unranked rather than
   *  ranked badly. */
  score: number | null;
  /** The raw observed rate, shown next to the bound so a reader can see what
   *  confidence cost. Never ranked on. */
  win_rate?: number | null;
  /** The denominator. 44 matches and 670 read identically without it. */
  matches?: number | null;
  tier_score: "S" | "A" | "B" | "C" | null;
}

export interface GodTierEntry extends TierEntry {
  role?: string;
  damage_type?: string;
  /** This god's share of the analysed matches. Popularity, deliberately kept
   *  apart from performance: they are different questions. */
  play_share?: number | null;
}

/** One god played with one aspect. An aspect rewrites part of a kit and often
 *  the role with it, so this is a different subject from the god, not a
 *  variant of the same row. `name` is the god's, so icons and links resolve. */
export interface AspectTierEntry extends TierEntry {
  god: string;
  aspect: string;
  role?: string;
  damage_type?: string;
  /** Share of the GOD's games played with this aspect — "when Sol is picked,
   *  how often is it this one" — not a share of all games. */
  play_share?: number | null;
}

export interface ItemTierEntry extends TierEntry {
  tier?: number | string;
  efficiency_tier?: string | null;
  /** Normalised gold-efficiency residual — "does it cost less than its stats
   *  are worth". A property of the item, not a competing ranking: ranking on
   *  it put it against win rate, and it correlated −0.267. */
  value?: number | null;
}

export interface PatchDelta {
  name: string;
  cost?: [number | null, number | null];
  stats: Record<string, [string | null, string | null]>;
  verdict: "buff" | "nerf" | "mixed" | "adjusted";
}

export interface PatchPeriod {
  from: string;
  to: string;
  added: string[];
  removed: string[];
  changed: PatchDelta[];
}

export interface DraftComp {
  allies: string[];
  enemies: string[];
}

export interface ThreatModel {
  magical: number;
  physical: number; // enemy damage-type counts
  healers: number;
  lockdown: number;
  crit: number;
  tanks: number;
  /** Enemies whose kit CREATES a wall (Cabrakan, Odin, Thor, Ymir). No wiki
   *  label describes this, so it exists only because `threat_kit` reads the
   *  ability text; and it is answered by one specific relic rather than by a
   *  stat, so it does not drive the core overlay. */
  walls: number;
  enemyCount: number; // enemies actually entered so far
  /** Slots on the enemy team for this mode (Conquest 5, Joust 3) — the honest
   * denominator. Dividing by `enemyCount` made one known healer a 100% threat
   * and let a 20%-complete draft drive a maximal overlay. */
  rosterSize: number;
  allyCovers: Record<string, boolean>; // effect_tag -> covered by an ally
  allyAllPhysical: boolean;
  /** Allies entered so far, and how many of them are physical. Scaled against
   * `rosterSize` for the same reason enemy threats are: one entered ally is
   * not evidence that "my team is all physical". */
  allyCount: number;
  allyPhysical: number;
}

/** One `lifesteal_caps` rule from _weights.yaml, shipped rather than
 *  reimplemented. A null/absent condition means "any". */
export interface LifestealCap {
  damage_types?: string[] | null;
  match_any?: string[] | null;
  max_lifesteal: number;
}

export interface DraftConfig {
  max_bonus: number;
  per_share: number;
  tag_bonus: Record<string, Record<string, number>>;
  stat_bonus: Record<string, Record<string, number>>;
  /** Threat -> the relic that answers it. Separate from `tag_bonus` because a
   *  relic does not compete for one of the six core slots — the game gives it
   *  its own — so there is no displacement to compute and no bonus to clamp. */
  relics?: Record<string, { item: string; because: string }>;
  ally_covered: number;
  ally_gap: number;
  /** Fraction of a draft bonus that survives when the core already covers the
   *  job earning it. Absent on an index built before the rule was shipped, in
   *  which case the client falls back to 1 — the old pay-in-full behaviour. */
  self_covered?: number;
  /** Absent on an index built before the rule was shipped. */
  lifesteal_caps?: LifestealCap[];
}

/** The model's own weights, shipped so the method page states what the
 *  pipeline actually used rather than a restatement of it. */
export interface MethodData {
  signals: { efficiency: number; win: number; pick: number; fit: number };
  kit_blend: number;
  underrated: { max_pick?: number; top_quality_frac?: number };
}

export interface TierListModeData {
  gods: GodTierEntry[];
  items: ItemTierEntry[];
  aspects?: AspectTierEntry[];
}

/** Per-mode tier lists (Task R2). `gods`/`items` at the top level mirror
 * Conquest for older consumers; the named keys carry the per-mode slices.
 * Any per-mode key may be absent on an index built before that mode shipped. */
export interface TierListData extends TierListModeData {
  conquest?: TierListModeData;
  joust?: TierListModeData;
  arena?: TierListModeData;
}

/** Provenance for the community figures: which rank band, drawn from how
 *  many matches, over what window. A win rate without these isn't checkable —
 *  "the community" means something different per division, and a window means
 *  something different the week a patch lands. */
export interface CommunitySource {
  division: string;
  window_start?: string | null;
  window_end?: string | null;
  matches_analyzed?: number | null;
}

export interface IndexData {
  gods: God[];
  items: Item[];
  builds: BuildNote[];
  starters?: { base: string; upgrade: string }[];
  roster?: RosterGod[];
  data_updated?: string;
  /** Current game patch label (e.g. "Open Beta 39"), Task R1. Absent on an
   * older index. */
  data_patch?: string;
  /** Where the community comparison came from. Absent on an index built
   *  before the god-index scrape existed. */
  community_source?: CommunitySource;
  tierlist?: TierListData;
  patch_notes?: PatchPeriod[];
  /** god -> mode -> item -> blended score. One table per mode: the draft
   *  page's mode toggle used to change only which build note it showed. */
  god_item_scores?: Record<string, Record<string, Record<string, number>>>;
  /** Fitted marginal gold price per stat — what makes a predicted cost
   * auditable rather than asserted. */
  item_gold_values?: Record<string, number>;
  method?: MethodData;
  /** B6: per-god, per-item damage gained against a squishy and against a
   *  tank, each column normalised on its own scale. Absent for gods whose
   *  kit didn't parse — the damage overlay just doesn't fire for them. */
  god_item_damage?: Record<string, Record<string, [number, number]>>;
  /** Mode display order from the pipeline. Absent on an older index. */
  modes?: string[];
  draft?: DraftConfig;
}
