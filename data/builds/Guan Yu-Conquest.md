---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.66
  aspect_win_rate: 0.63
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.22
    win_rate: 0.61
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.65
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.65
  - name: Breastplate of Valor
    pick_rate: 0.25
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.2
      win_rate: 0.66
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.59
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.2
      win_rate: 0.6
    - name: Heartwood Charm
      pick_rate: 0.07
      win_rate: 0.69
  - name: Dwarven Plate
    pick_rate: 0.12
    win_rate: 0.64
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.57
    - name: Heartwood Charm
      pick_rate: 0.06
      win_rate: 0.59
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.14
      win_rate: 0.53
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.43
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.44
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.73
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.73
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-07-23'
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
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Kinetic Cuirass, Eye of Providence, Shield Splitter,
    Amanita Charm, Runeforged Hammer, Hydra''s Lament, The Crusher, Eye of the Storm,
    Spectral Armor, Avenging Blade, Berserker''s Shield, Erosion, Shield of the Phoenix,
    Golden Blade, Pharaoh''s Curse, Tyrfing, Chandra''s Grace, Wyrmskin Hide, Gladiator''s
    Shield, The Reaper, Lernaean Bow, Midgardian Mail, Screeching Gargoyle, Leviathan''s
    Hide, Prophetic Cloak.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.49
      efficiency: 0.46
      win: 0.59
      pick: 0.24
      fit: 0.32
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.42
      win: 0.57
      pick: 0.25
      fit: 0.32
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shifter's Shield:
      total: 0.47
      efficiency: 0.3
      win: 0.61
      pick: 0.22
      fit: 0.5
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Chandra''s
    Grace, The Reaper, Kinetic Cuirass, Eye of Providence, Shield Splitter, Runeforged
    Hammer, The Crusher, Hydra''s Lament, Phoenix Feather, Spectral Armor, Eye of
    the Storm, Avenging Blade, Berserker''s Shield, Spirit Robe, Erosion, Golden Blade,
    Tyrfing, Bloodforge, Pharaoh''s Curse, Glorious Pridwen, Lernaean Bow, Gladiator''s
    Shield, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.46
      win: 0.59
      pick: 0.24
      fit: 0.26
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.42
      win: 0.57
      pick: 0.25
      fit: 0.26
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.46
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
      efficiency: 0.45
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Kinetic Cuirass,
    Eye of Providence, The Reaper, Shield Splitter, Screeching Gargoyle, Runeforged
    Hammer, Amanita Charm, Hydra''s Lament, Spectral Armor, Void Stone, Eye of the
    Storm, Stone of Binding, Void Shield, Tekko-Kagi, Oath-Sworn Spear, Berserker''s
    Shield, Titan''s Bane, Shield of the Phoenix, Erosion, Golden Blade, Tyrfing,
    Chandra''s Grace, Pendulum Blade.'
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
      win: 0.59
      pick: 0.24
      fit: 0.24
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.42
      win: 0.57
      pick: 0.25
      fit: 0.24
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
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
