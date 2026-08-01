---
type: smite-build
god: Chiron
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - The Crusher
  - Eros' Bow
  flex_slots:
  - The Crusher
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
    Riptalon:
      total: 0.51
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.75
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.44
    Eros' Bow:
      total: 0.46
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Rage
  - The Reaper
  - Damaru
  - Demon Blade
  flex_slots:
  - Damaru
  - Rage
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Crit / auto-attack skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.46
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.57
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.41
    Rage:
      total: 0.39
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.39
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.42
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Eros' Bow
  - Pharaoh's Curse
  flex_slots:
  - Eros' Bow
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.43
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.46
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.43
    Eros' Bow:
      total: 0.42
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.47
    Pharaoh's Curse:
      total: 0.42
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - The Reaper
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    The Reaper:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spectral Armor:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.4
    Amanita Charm:
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.8
    Erosion:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.5
    Pharaoh's Curse:
      total: 0.47
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shogun's Ofuda:
      total: 0.44
      efficiency: 0.33
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - The Reaper
  - The Crusher
  flex_slots:
  - Void Shield
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.53
    Void Shield:
      total: 0.49
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.7
    Void Stone:
      total: 0.5
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Reaper:
      total: 0.61
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    The Crusher:
      total: 0.52
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - The Crusher
  - Eros' Bow
  flex_slots:
  - The Crusher
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
    Riptalon:
      total: 0.51
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.75
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.44
    Eros' Bow:
      total: 0.46
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Riptalon
  - Damaru
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Damaru
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.53
    Hydra's Lament:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.61
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.78
    Riptalon:
      total: 0.45
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.64
    Damaru:
      total: 0.43
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Rage
  - The Reaper
  - Damaru
  - Demon Blade
  flex_slots:
  - Damaru
  - Rage
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
  rationale: Crit / auto-attack skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.46
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.57
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.41
    Rage:
      total: 0.39
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.39
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.42
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  flex_slots:
  - Pendulum Blade
  - Heartseeker
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
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.53
    Hydra's Lament:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.4
    The Reaper:
      total: 0.57
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    Pendulum Blade:
      total: 0.41
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.48
    Heartseeker:
      total: 0.38
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Mantle Of Discord
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Mantle Of Discord
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.34
    Shield Splitter:
      total: 0.39
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.36
    Mantle Of Discord:
      total: 0.39
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.43
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.43
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  flex_slots:
  - Pendulum Blade
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.57
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Reaper:
      total: 0.65
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.87
    Pendulum Blade:
      total: 0.46
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.56
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.63
    Heartseeker:
      total: 0.45
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Riptalon
  - Damaru
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Damaru
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.53
    Hydra's Lament:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.61
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.78
    Riptalon:
      total: 0.45
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.64
    Damaru:
      total: 0.43
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
