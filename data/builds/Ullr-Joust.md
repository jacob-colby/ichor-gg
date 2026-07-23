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
  - Hydra's Lament
  - The Reaper
  - Riptalon
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Tyrfing
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.55
    Tyrfing:
      total: 0.43
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.47
    Hydra's Lament:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.8
    Riptalon:
      total: 0.51
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.75
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.52
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
      total: 0.56
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Hydra's Lament:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.59
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
    Pendulum Blade:
      total: 0.43
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.5
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
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - The Crusher
  - Spectral Armor
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
      total: 0.44
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.33
    The Reaper:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.42
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.35
    Spectral Armor:
      total: 0.41
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
    Erosion:
      total: 0.42
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
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
    swap: Void Stone — magical protection
    swap_item: Void Stone
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
      fit: 0.56
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
      fit: 0.91
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
---
