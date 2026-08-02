---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.46
    win_rate: 0.55
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.17
      win_rate: 0.55
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.52
  - name: Breastplate of Valor
    pick_rate: 0.29
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.52
  - name: Genji's Guard
    pick_rate: 0.31
    win_rate: 0.55
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.2
      win_rate: 0.53
    - name: Regrowth Striders
      pick_rate: 0.05
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.13
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.65
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.62
  - name: Hide of the Nemean Lion
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.46
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.57
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.86
    - name: Glorious Pridwen
      pick_rate: 0.06
      win_rate: 1.0
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-08-01'
  god_win_rate: 0.5470588235294118
  god_matches_won: 93
  god_matches_played: 170
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Shield Splitter, Amanita Charm,
    Jotunn''s Revenge, Eye of the Storm, Runeforged Hammer, Spectral Armor, Hydra''s
    Lament, Erosion, Avenging Blade, Shield of the Phoenix, The Crusher, Wyrmskin
    Hide, Berserker''s Shield, Golden Blade, Gladiator''s Shield, Chandra''s Grace,
    Midgardian Mail, Pharaoh''s Curse, Draconic Scale, Mantle Of Discord, Freya''s
    Tears, Leviathan''s Hide, Shroud of Vengeance.'
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
      pick: 0.31
      fit: 0.33
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.42
      win: 0.61
      pick: 0.29
      fit: 0.33
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
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Chandra''s Grace, Jotunn''s Revenge, Runeforged Hammer, Shield Splitter, Eye of
    the Storm, Phoenix Feather, Spectral Armor, Hydra''s Lament, Avenging Blade, Erosion,
    The Crusher, The Reaper, Spirit Robe, Wyrmskin Hide, Golden Blade, Berserker''s
    Shield, Gladiator''s Shield, Midgardian Mail, Bloodforge, Pharaoh''s Curse, Glorious
    Pridwen, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.58
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.42
      win: 0.61
      pick: 0.29
      fit: 0.3
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.82
    Amanita Charm:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, The Crusher, Kinetic Cuirass,
    Eye of Providence, Shield Splitter, Amanita Charm, Runeforged Hammer, Spectral
    Armor, Screeching Gargoyle, Hydra''s Lament, Eye of the Storm, Heartseeker, Void
    Stone, Stone of Binding, Pendulum Blade, Titan''s Bane, Void Shield, Erosion,
    Shield of the Phoenix, Oath-Sworn Spear, The Reaper, Berserker''s Shield, Chandra''s
    Grace, Golden Blade, Midgardian Mail.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.46
      efficiency: 0.46
      win: 0.55
      pick: 0.31
      fit: 0.24
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.42
      win: 0.61
      pick: 0.29
      fit: 0.24
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.52
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
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
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
    Golden Blade:
      total: 0.22
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Tyrfing:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.24
      efficiency: 0.41
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
  archetype: model
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Eye of the Storm
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Eye of Providence, Shield Splitter,
    Amanita Charm, Jotunn''s Revenge, Eye of the Storm, Runeforged Hammer, Spectral
    Armor, Hydra''s Lament, Erosion, Avenging Blade, Shield of the Phoenix, The Crusher,
    Wyrmskin Hide, Berserker''s Shield, Golden Blade, Gladiator''s Shield, Chandra''s
    Grace, Midgardian Mail, Pharaoh''s Curse, Draconic Scale, Mantle Of Discord, Freya''s
    Tears, Leviathan''s Hide, Shroud of Vengeance.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.52
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
    Eye of the Storm:
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Eye of Providence
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Spectral Armor, Erosion, Kinetic Cuirass, Eye of Providence,
    Shield of the Phoenix, Runeforged Hammer, Pharaoh''s Curse, Shield Splitter, Jotunn''s
    Revenge, Eye of the Storm, Chandra''s Grace, Avenging Blade, Stampede, Void Stone,
    Shogun''s Ofuda, Hydra''s Lament, Void Shield, Phoenix Feather, Doublet of Binding,
    Eros'' Bow, Mystical Mail, The Crusher, Wyrmskin Hide, Golden Blade, Berserker''s
    Shield, Midgardian Mail.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.61
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.42
      win: 0.61
      pick: 0.29
      fit: 0.29
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.71
    Spectral Armor:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.53
      efficiency: 0.45
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
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
    Cuirass, Eye of Providence, Chandra''s Grace, Jotunn''s Revenge, Runeforged Hammer,
    Shield Splitter, Pharaoh''s Curse, Eye of the Storm, Phoenix Feather, Hydra''s
    Lament, Avenging Blade, Stampede, Void Stone, Shogun''s Ofuda, Void Shield, The
    Crusher, Doublet of Binding, Eros'' Bow, Mystical Mail, The Reaper, Spirit Robe,
    Wyrmskin Hide, Golden Blade.'
  slot_scores:
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.42
      win: 0.61
      pick: 0.29
      fit: 0.3
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.82
    Spectral Armor:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.49
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Void Stone
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, Spectral Armor, Avenging Blade,
    Void Stone, Void Shield, Erosion, The Crusher, Kinetic Cuirass, Eye of Providence,
    Shield of the Phoenix, Pharaoh''s Curse, Runeforged Hammer, Chandra''s Grace,
    The Reaper, Shield Splitter, Eye of the Storm, Hydra''s Lament, Stampede, Screeching
    Gargoyle, Shogun''s Ofuda, Phoenix Feather, Eros'' Bow, Heartseeker, Pendulum
    Blade, Titan''s Bane, Doublet of Binding, Mystical Mail.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.55
    Void Shield:
      total: 0.48
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.48
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 1.0
    Spectral Armor:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: model
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
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Spectral Armor, Erosion, Kinetic Cuirass,
    Eye of Providence, Shield of the Phoenix, Runeforged Hammer, Pharaoh''s Curse,
    Shield Splitter, Jotunn''s Revenge, Eye of the Storm, Chandra''s Grace, Avenging
    Blade, Stampede, Void Stone, Shogun''s Ofuda, Hydra''s Lament, Void Shield, Phoenix
    Feather, Doublet of Binding, Eros'' Bow, Mystical Mail, The Crusher, Wyrmskin
    Hide, Golden Blade, Berserker''s Shield, Midgardian Mail.'
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
      total: 0.48
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
      efficiency: 0.45
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
---
