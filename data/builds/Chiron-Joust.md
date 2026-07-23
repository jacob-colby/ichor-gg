---
type: smite-build
god: Chiron
mode: Joust
builds:
- source: community
  aspect: Aspect of the Heroic Tutor
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.51
  slot_order:
  - name: Transcendence
    pick_rate: 0.53
    win_rate: 0.52
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.51
    - name: Lernaean Bow
      pick_rate: 0.11
      win_rate: 0.51
  - name: Jotunn's Revenge
    pick_rate: 0.44
    win_rate: 0.53
    alternates:
    - name: Transcendence
      pick_rate: 0.11
      win_rate: 0.52
    - name: Avenging Blade
      pick_rate: 0.09
      win_rate: 0.59
  - name: Heartseeker
    pick_rate: 0.22
    win_rate: 0.53
    alternates:
    - name: The Crusher
      pick_rate: 0.17
      win_rate: 0.61
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.56
  - name: Titan's Bane
    pick_rate: 0.39
    win_rate: 0.53
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.64
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.48
  - name: The Crusher
    pick_rate: 0.08
    win_rate: 0.51
    alternates:
    - name: Titan's Bane
      pick_rate: 0.21
      win_rate: 0.55
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.58
  - name: Hunter's Bow
    pick_rate: 0.07
    win_rate: 0.52
    alternates:
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.58
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.58
  source_url: https://smitebrain.com/gods/chiron/
  last_verified: '2026-07-23'
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - The Reaper
  - Riptalon
  - The Crusher
  flex_slots:
  - Tyrfing
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.42
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.4
    The Reaper:
      total: 0.59
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
    Riptalon:
      total: 0.51
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.75
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Rage
  - The Reaper
  - Damaru
  - Demon Blade
  - The Crusher
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
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Crit / auto-attack skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.41
    Rage:
      total: 0.39
      efficiency: 0.36
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
      total: 0.4
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.43
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - The Crusher
  flex_slots:
  - Pendulum Blade
  - Tyrfing
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
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.39
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.42
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.39
    The Reaper:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
    Pendulum Blade:
      total: 0.39
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.46
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
  - Pharaoh's Curse
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
      fit: 0.32
    The Reaper:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.42
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.35
    Amanita Charm:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.4
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.41
    Pharaoh's Curse:
      total: 0.41
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Stone
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - Void Stone
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
      total: 0.48
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.58
    Void Stone:
      total: 0.45
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.63
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.82
    Tekko-Kagi:
      total: 0.45
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.54
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Riptalon
  - Pendulum Blade
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Pendulum Blade
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
      total: 0.56
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.57
    Hydra's Lament:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.45
    The Reaper:
      total: 0.63
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.81
    Riptalon:
      total: 0.47
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.67
    Pendulum Blade:
      total: 0.43
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.57
    The Crusher:
      total: 0.52
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Rage
  - The Reaper
  - Damaru
  - Demon Blade
  - The Crusher
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
  rationale: Crit / auto-attack skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.41
    Rage:
      total: 0.39
      efficiency: 0.36
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
      total: 0.4
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.43
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
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
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.58
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
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
    Heartseeker:
      total: 0.39
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Stygian Anchor
  - Jotunn's Revenge
  - Shield Splitter
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Stygian Anchor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Stygian Anchor:
      total: 0.4
      efficiency: 0.26
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.35
    Shield Splitter:
      total: 0.41
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.43
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.54
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.64
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.58
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Reaper:
      total: 0.67
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.9
    Pendulum Blade:
      total: 0.47
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Crusher:
      total: 0.57
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.47
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
