export interface StatValue {
  base: number;
  per_level: number;
}

export interface Ability {
  slot: string;
  name: string;
  cooldown?: number[];
  cost?: number[];
}

export interface Aspect {
  name: string;
  kit_changes: string;
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
}

export interface Item {
  type: string;
  name: string;
  tier: number;
  cost: number;
  stats: Record<string, string>;
  passive: string;
  builds_from: string[];
  builds_into: string[];
  source_url: string;
  last_verified: string;
  effect_tags?: string[];
  efficiency_tier?: string | null;
}

export interface CommunitySlotEntry {
  name: string;
  pick_rate: number;
  win_rate: number;
}

export type SlotEntry = string | CommunitySlotEntry;

export interface SituationalSwap {
  vs_tag: string;
  swap: string;
  swap_item?: string | null;
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
}

export interface CuratedBuildEntry {
  source: "pro" | "mine" | "suggested";
  aspect?: string;
  archetype?: string;
  name?: string;
  aspect?: string;
  rationale?: string;
  slot_order: string[];
  flex_slots?: string[];
  situational_swaps?: SituationalSwap[];
  notes?: string;
  starter?: { base: string; upgrade: string };
}

export type BuildEntry = CommunityBuildEntry | CuratedBuildEntry;

export interface BuildNote {
  type: string;
  god: string;
  mode: string;
  builds: BuildEntry[];
  last_verified?: string;
}

export interface IndexData {
  gods: God[];
  items: Item[];
  builds: BuildNote[];
  starters?: { base: string; upgrade: string }[];
}
