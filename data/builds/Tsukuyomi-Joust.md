---
type: smite-build
god: Tsukuyomi
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - Demon Blade
  - The Crusher
  flex_slots:
  - Tyrfing
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.5
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.58
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.64
    Demon Blade:
      total: 0.47
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.74
    The Crusher:
      total: 0.53
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - Pendulum Blade
  - The Crusher
  flex_slots:
  - Pendulum Blade
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Hydra's Lament:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    Tekko-Kagi:
      total: 0.41
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.46
    Pendulum Blade:
      total: 0.42
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Jotunn's Revenge
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.31
    The Reaper:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.38
    Amanita Charm:
      total: 0.6
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.75
    Erosion:
      total: 0.42
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.45
    Pharaoh's Curse:
      total: 0.43
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  flex_slots:
  - Avenging Blade
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Reaper:
      total: 0.65
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.85
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Crusher:
      total: 0.6
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
    Heartseeker:
      total: 0.49
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Tyrfing
  - Rage
  - Bragi's Harp
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Bragi's Harp
  - Rage
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Tyrfing:
      total: 0.52
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rage:
      total: 0.5
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.5
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.51
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.6
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - Demon Blade
  - The Crusher
  flex_slots:
  - Tyrfing
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.5
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.58
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.64
    Demon Blade:
      total: 0.47
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.74
    The Crusher:
      total: 0.53
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
---
