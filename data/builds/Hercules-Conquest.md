---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.43
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.42
    win_rate: 0.51
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.19
      win_rate: 0.52
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.39
  - name: Genji's Guard
    pick_rate: 0.3
    win_rate: 0.55
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.27
      win_rate: 0.45
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.49
  - name: Breastplate of Valor
    pick_rate: 0.25
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.26
      win_rate: 0.44
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.46
  - name: Dwarven Plate
    pick_rate: 0.23
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.51
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.52
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.45
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.13
      win_rate: 0.51
    - name: Glorious Pridwen
      pick_rate: 0.06
      win_rate: 0.59
  - name: Shell of Rebuke
    pick_rate: 0.04
    win_rate: 0.65
    alternates:
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.53
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.6
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-07-25'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Shield Splitter, Jotunn''s Revenge,
    Amanita Charm, Eye of the Storm, Runeforged Hammer, Spectral Armor, The Crusher,
    Erosion, Hydra''s Lament, Avenging Blade, Shield of the Phoenix, Berserker''s
    Shield, Wyrmskin Hide, Golden Blade, The Reaper, Midgardian Mail, Gladiator''s
    Shield, Chandra''s Grace, Draconic Scale, Pharaoh''s Curse, Leviathan''s Hide,
    Mantle Of Discord, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.55
      pick: 0.3
      fit: 0.33
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.54
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
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.47
      efficiency: 0.44
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
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Kinetic Cuirass,
    The Reaper, Eye of Providence, Chandra''s Grace, Shield Splitter, Runeforged Hammer,
    The Crusher, Phoenix Feather, Eye of the Storm, Spectral Armor, Hydra''s Lament,
    Avenging Blade, Erosion, Spirit Robe, Berserker''s Shield, Golden Blade, Bloodforge,
    Wyrmskin Hide, Midgardian Mail, Gladiator''s Shield, Glorious Pridwen, Tyrfing,
    Pharaoh''s Curse.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.46
      efficiency: 0.46
      win: 0.55
      pick: 0.3
      fit: 0.25
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Eye of Providence
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Kinetic Cuirass,
    Eye of Providence, Shield Splitter, The Reaper, Amanita Charm, Runeforged Hammer,
    Spectral Armor, Screeching Gargoyle, Hydra''s Lament, Eye of the Storm, Void Stone,
    Stone of Binding, Void Shield, Erosion, Titan''s Bane, Oath-Sworn Spear, Shield
    of the Phoenix, Tekko-Kagi, Berserker''s Shield, Heartseeker, Golden Blade, Chandra''s
    Grace, Pendulum Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.7
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.43
    Genji's Guard:
      total: 0.46
      efficiency: 0.46
      win: 0.55
      pick: 0.3
      fit: 0.24
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.57
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.53
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
  - Jotunn's Revenge
  - Demon Blade
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
      total: 0.22
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.23
    Tyrfing:
      total: 0.23
      efficiency: 0.37
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
      total: 0.22
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Eye of Providence
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Spectral Armor, Erosion, Kinetic Cuirass, Eye of Providence,
    Shield of the Phoenix, Jotunn''s Revenge, Runeforged Hammer, Pharaoh''s Curse,
    Shield Splitter, Eye of the Storm, Chandra''s Grace, Avenging Blade, Void Stone,
    The Crusher, Stampede, Shogun''s Ofuda, Phoenix Feather, Void Shield, The Reaper,
    Hydra''s Lament, Doublet of Binding, Mystical Mail, Berserker''s Shield, Eros''
    Bow, Wyrmskin Hide, Golden Blade.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.61
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.74
    Spectral Armor:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.5
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Spectral Armor, Erosion, Shield of the Phoenix, Kinetic
    Cuirass, Jotunn''s Revenge, Chandra''s Grace, Eye of Providence, Runeforged Hammer,
    The Reaper, Pharaoh''s Curse, Phoenix Feather, Eye of the Storm, Shield Splitter,
    The Crusher, Avenging Blade, Void Stone, Hydra''s Lament, Stampede, Shogun''s
    Ofuda, Void Shield, Eros'' Bow, Doublet of Binding, Mystical Mail, Berserker''s
    Shield, Golden Blade, Spirit Robe.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.74
    Spectral Armor:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.48
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Stone
  - The Crusher
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, Spectral Armor, The Crusher, Avenging
    Blade, Void Stone, The Reaper, Void Shield, Erosion, Kinetic Cuirass, Eye of Providence,
    Shield of the Phoenix, Runeforged Hammer, Pharaoh''s Curse, Chandra''s Grace,
    Shield Splitter, Eye of the Storm, Stampede, Hydra''s Lament, Screeching Gargoyle,
    Shogun''s Ofuda, Phoenix Feather, Eros'' Bow, Doublet of Binding, Mystical Mail,
    Berserker''s Shield, Titan''s Bane, Stone of Binding.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.55
    Void Stone:
      total: 0.48
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spectral Armor:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
  aspect: Aspect of Preservation
---
