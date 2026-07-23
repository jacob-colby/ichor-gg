---
type: smite-build
god: Ullr
mode: Joust
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Transcendence
    pick_rate: 0.86
    win_rate: 0.55
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.06
      win_rate: 0.54
    - name: Hydra's Lament
      pick_rate: 0.05
      win_rate: 0.72
  - name: Jotunn's Revenge
    pick_rate: 0.44
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.39
      win_rate: 0.57
    - name: Transcendence
      pick_rate: 0.1
      win_rate: 0.6
  - name: Hydra's Lament
    pick_rate: 0.38
    win_rate: 0.55
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.3
      win_rate: 0.6
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.53
  - name: Heartseeker
    pick_rate: 0.4
    win_rate: 0.54
    alternates:
    - name: Titan's Bane
      pick_rate: 0.38
      win_rate: 0.59
    - name: The Crusher
      pick_rate: 0.03
      win_rate: 0.53
  - name: Titan's Bane
    pick_rate: 0.29
    win_rate: 0.56
    alternates:
    - name: Heartseeker
      pick_rate: 0.3
      win_rate: 0.62
    - name: Lucerne Hammer
      pick_rate: 0.1
      win_rate: 0.55
  - name: Blinking Abyss
    pick_rate: 0.15
    win_rate: 0.62
    alternates:
    - name: Lucerne Hammer
      pick_rate: 0.11
      win_rate: 0.57
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.73
  source_url: https://smitebrain.com/gods/ullr/
  last_verified: '2026-07-23'
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  - Demon Blade
  - The Crusher
  flex_slots:
  - Tyrfing
  - Demon Blade
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
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.4
    Tyrfing:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.5
    The Reaper:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    Riptalon:
      total: 0.51
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.75
    Demon Blade:
      total: 0.44
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
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
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.4
    Rage:
      total: 0.4
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.43
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    Damaru:
      total: 0.41
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.43
    Demon Blade:
      total: 0.44
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.4
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
  - Tyrfing
  - Pendulum Blade
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
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.39
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.4
    Hydra's Lament:
      total: 0.41
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.36
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    Pendulum Blade:
      total: 0.37
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.46
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
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
      total: 0.41
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.27
    The Reaper:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
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
      total: 0.42
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.47
    Shogun's Ofuda:
      total: 0.4
      efficiency: 0.33
      win: 0.5
      pick: 0.0
      fit: 0.47
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
  - Void Stone
  - Void Shield
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    Void Shield:
      total: 0.45
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.6
    Void Stone:
      total: 0.45
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.6
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    The Crusher:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
---
