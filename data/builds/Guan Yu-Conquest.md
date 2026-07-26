---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.65
  aspect_win_rate: 0.64
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.27
    win_rate: 0.59
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.62
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.67
  - name: Breastplate of Valor
    pick_rate: 0.24
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.65
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.61
  - name: Genji's Guard
    pick_rate: 0.25
    win_rate: 0.58
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.2
      win_rate: 0.62
    - name: Heartwood Charm
      pick_rate: 0.07
      win_rate: 0.7
  - name: Dwarven Plate
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.58
    - name: Heartwood Charm
      pick_rate: 0.06
      win_rate: 0.6
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.62
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.15
      win_rate: 0.57
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.46
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.4
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.68
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 0.5
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-07-25'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Kinetic Cuirass, Eye of Providence, Shield Splitter,
    Amanita Charm, Runeforged Hammer, Hydra''s Lament, The Crusher, Spectral Armor,
    Eye of the Storm, Berserker''s Shield, Avenging Blade, Erosion, Shield of the
    Phoenix, Golden Blade, Pharaoh''s Curse, Chandra''s Grace, Tyrfing, Wyrmskin Hide,
    Gladiator''s Shield, The Reaper, Lernaean Bow, Midgardian Mail, Leviathan''s Hide,
    Ancile, Shogun''s Ofuda.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.48
      efficiency: 0.46
      win: 0.58
      pick: 0.25
      fit: 0.32
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.42
      win: 0.59
      pick: 0.24
      fit: 0.32
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Chandra''s
    Grace, Kinetic Cuirass, The Reaper, Eye of Providence, Runeforged Hammer, Shield
    Splitter, The Crusher, Hydra''s Lament, Phoenix Feather, Spectral Armor, Eye of
    the Storm, Avenging Blade, Berserker''s Shield, Erosion, Golden Blade, Spirit
    Robe, Tyrfing, Pharaoh''s Curse, Bloodforge, Lernaean Bow, Gladiator''s Shield,
    Glorious Pridwen, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.58
      pick: 0.25
      fit: 0.26
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.42
      win: 0.59
      pick: 0.24
      fit: 0.26
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shield of the Phoenix:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.69
    Amanita Charm:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
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
  - Breastplate of Valor
  - Kinetic Cuirass
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
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Kinetic Cuirass,
    Eye of Providence, The Reaper, Shield Splitter, Runeforged Hammer, Amanita Charm,
    Screeching Gargoyle, Hydra''s Lament, Spectral Armor, Eye of the Storm, Void Stone,
    Berserker''s Shield, Tekko-Kagi, Void Shield, Stone of Binding, Oath-Sworn Spear,
    Titan''s Bane, Erosion, Shield of the Phoenix, Golden Blade, Chandra''s Grace,
    Pharaoh''s Curse, Tyrfing.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.58
      pick: 0.25
      fit: 0.24
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.42
      win: 0.59
      pick: 0.24
      fit: 0.24
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.55
    Kinetic Cuirass:
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
      fit: 0.54
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
---
