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
}

export interface Item {
  type: string;
  name: string;
  tier: number | string;
  cost: number;
  stats: Record<string, string>;
  passive: string;
  builds_from: string[];
  builds_into: string[];
  source_url: string;
  last_verified: string;
  effect_tags?: string[];
  efficiency_tier?: string | null;
  /** The gold-value model's working, not just its verdict. Null for items
   * outside the scored pool: non-numeric cost, and tier-1 starters, which are
   * passive-priced and deliberately sit out the regression.
   * `cost - predicted_cost === residual` holds exactly. */
  efficiency?: {
    /** What the item's stats are worth at the fitted per-stat gold prices. */
    predicted_cost: number;
    /** actual - predicted. Negative = underpriced. */
    residual: number;
    /** Min-max normalised value across the scored set, 1 = best value. */
    score: number;
  } | null;
  meta?: { win_avg: number; gods: number };
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

export interface TierEntry {
  name: string;
  ours: number | null;
  community: number | null;
  tier_ours: "S" | "A" | "B" | "C" | null;
  tier_community: "S" | "A" | "B" | "C" | null;
}

export interface GodTierEntry extends TierEntry {
  role?: string;
  damage_type?: string;
}

export interface ItemTierEntry extends TierEntry {
  tier?: number | string;
  efficiency_tier?: string | null;
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

export interface DraftConfig {
  max_bonus: number;
  per_share: number;
  tag_bonus: Record<string, Record<string, number>>;
  stat_bonus: Record<string, Record<string, number>>;
  ally_covered: number;
  ally_gap: number;
}

export interface TierListModeData {
  gods: GodTierEntry[];
  items: ItemTierEntry[];
}

/** Per-mode tier lists (Task R2). `gods`/`items` at the top level mirror
 * Conquest for older consumers; `conquest`/`joust` carry the per-mode slices.
 * Either per-mode key may be absent on an index built before R2. */
export interface TierListData extends TierListModeData {
  conquest?: TierListModeData;
  joust?: TierListModeData;
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
  god_item_scores?: Record<string, Record<string, number>>;
  /** Fitted marginal gold price per stat — what makes a predicted cost
   * auditable rather than asserted. */
  item_gold_values?: Record<string, number>;
  draft?: DraftConfig;
}
