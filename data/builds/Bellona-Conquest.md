---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.25
  aspect_win_rate: 0.47
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.5
    win_rate: 0.49
    alternates:
    - name: Golden Blade
      pick_rate: 0.2
      win_rate: 0.56
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.5
  - name: Berserker's Shield
    pick_rate: 0.34
    win_rate: 0.48
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.17
      win_rate: 0.51
    - name: Golden Blade
      pick_rate: 0.14
      win_rate: 0.53
  - name: Shogun's Ofuda
    pick_rate: 0.18
    win_rate: 0.57
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.28
      win_rate: 0.5
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.43
  - name: Dwarven Plate
    pick_rate: 0.19
    win_rate: 0.58
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.14
      win_rate: 0.58
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 0.51
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.46
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.18
      win_rate: 0.44
    - name: Eros' Bow
      pick_rate: 0.06
      win_rate: 0.46
  - name: Hunter's Bow
    pick_rate: 0.06
    win_rate: 0.56
    alternates:
    - name: Engraved Guard
      pick_rate: 0.11
      win_rate: 0.52
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.62
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-07-23'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Eye of the Storm
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Eye of the Storm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Shield Splitter, Eye of Providence, Jotunn''s Revenge,
    Amanita Charm, Eye of the Storm, Runeforged Hammer, Spectral Armor, The Crusher,
    Erosion, Hydra''s Lament, Avenging Blade, Shield of the Phoenix, Genji''s Guard,
    Wyrmskin Hide, Golden Blade, The Reaper, Breastplate of Valor, Gladiator''s Shield,
    Midgardian Mail, Chandra''s Grace, Shroud of Vengeance, Mantle Of Discord, Draconic
    Scale, Leviathan''s Hide, Pharaoh''s Curse.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.67
    Eye of the Storm:
      total: 0.46
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Kinetic Cuirass,
    The Reaper, Chandra''s Grace, Eye of Providence, Shield Splitter, Runeforged Hammer,
    The Crusher, Phoenix Feather, Hydra''s Lament, Eye of the Storm, Spectral Armor,
    Avenging Blade, Erosion, Spirit Robe, Genji''s Guard, Bloodforge, Golden Blade,
    Wyrmskin Hide, Breastplate of Valor, Glorious Pridwen, Midgardian Mail, Tyrfing,
    Gladiator''s Shield, Devourer''s Gauntlet.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.52
    Shield of the Phoenix:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - The Crusher
  flex_slots:
  - Eye of Providence
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Kinetic Cuirass,
    Eye of Providence, Shield Splitter, The Reaper, Amanita Charm, Runeforged Hammer,
    Screeching Gargoyle, Spectral Armor, Hydra''s Lament, Eye of the Storm, Void Stone,
    Stone of Binding, Void Shield, Erosion, Titan''s Bane, Oath-Sworn Spear, Genji''s
    Guard, Shield of the Phoenix, Tekko-Kagi, Heartseeker, Pendulum Blade, Breastplate
    of Valor, Chandra''s Grace, Golden Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.7
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.57
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.53
    Shield Splitter:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Lernaean Bow:
      total: 0.23
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.23
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.23
    Tyrfing:
      total: 0.24
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.23
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.23
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
---
