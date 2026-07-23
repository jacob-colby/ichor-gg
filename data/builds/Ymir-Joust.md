---
type: smite-build
god: Ymir
mode: Joust
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.24
    win_rate: 0.55
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.52
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.51
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.56
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.53
  - name: Spirit Robe
    pick_rate: 0.09
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.54
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.43
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.63
    alternates:
    - name: Spirit Robe
      pick_rate: 0.1
      win_rate: 0.58
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.45
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.35
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.61
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.71
  - name: Circle of Protection
    pick_rate: 0.07
    win_rate: 0.43
    alternates:
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.56
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.3
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-07-23'
- source: suggested
  archetype: core
  slot_order:
  - Stygian Anchor
  - Eye of Providence
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Stygian Anchor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Stygian Anchor:
      total: 0.54
      efficiency: 0.26
      win: 0.5
      pick: 0.0
      fit: 0.81
    Eye of Providence:
      total: 0.6
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.72
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.82
    Spectral Armor:
      total: 0.58
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.66
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.92
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Rod of Asclepius
  - Erosion
  flex_slots:
  - Spectral Armor
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Eye of Providence:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spectral Armor:
      total: 0.52
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Rod of Asclepius:
      total: 0.61
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.75
    Erosion:
      total: 0.56
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Void Shield
  - Void Stone
  - Erosion
  - Soul Gem
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.74
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    Void Shield:
      total: 0.6
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.91
    Void Stone:
      total: 0.6
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.53
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.71
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
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
      total: 0.53
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rage:
      total: 0.51
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.51
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.52
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.61
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
---
