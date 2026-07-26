---
type: smite-build
god: Amaterasu
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.35
    win_rate: 0.69
    alternates:
    - name: Golden Blade
      pick_rate: 0.27
      win_rate: 0.52
    - name: Daybreak Gavel
      pick_rate: 0.06
      win_rate: 0.43
  - name: Berserker's Shield
    pick_rate: 0.19
    win_rate: 0.55
    alternates:
    - name: Golden Blade
      pick_rate: 0.16
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.38
  - name: Shogun's Ofuda
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.3
  - name: Dwarven Plate
    pick_rate: 0.19
    win_rate: 0.46
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.14
      win_rate: 0.59
    - name: Shogun's Ofuda
      pick_rate: 0.1
      win_rate: 0.71
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.82
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.14
      win_rate: 0.63
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.3
  - name: Contagion
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.57
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.71
  source_url: https://smitebrain.com/gods/amaterasu/
  last_verified: '2026-07-25'
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Jotunn''s Revenge, Shield Splitter,
    Amanita Charm, Eye of the Storm, Runeforged Hammer, Spectral Armor, Erosion, The
    Crusher, Hydra''s Lament, Avenging Blade, Shield of the Phoenix, Genji''s Guard,
    Wyrmskin Hide, Breastplate of Valor, Gladiator''s Shield, Golden Blade, Chandra''s
    Grace, Midgardian Mail, The Reaper, Draconic Scale, Pharaoh''s Curse, Leviathan''s
    Hide, Mantle Of Discord, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
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
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.52
      efficiency: 0.29
      win: 0.69
      pick: 0.35
      fit: 0.6
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Kinetic Cuirass,
    Chandra''s Grace, Eye of Providence, The Reaper, Shield Splitter, Runeforged Hammer,
    The Crusher, Phoenix Feather, Spectral Armor, Hydra''s Lament, Eye of the Storm,
    Avenging Blade, Erosion, Genji''s Guard, Spirit Robe, Golden Blade, Bloodforge,
    Breastplate of Valor, Wyrmskin Hide, Midgardian Mail, Gladiator''s Shield, Glorious
    Pridwen, Pharaoh''s Curse, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.46
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
      fit: 0.56
    Shield of the Phoenix:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shifter's Shield:
      total: 0.5
      efficiency: 0.29
      win: 0.69
      pick: 0.35
      fit: 0.46
    Amanita Charm:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Kinetic Cuirass,
    Eye of Providence, Shield Splitter, The Reaper, Amanita Charm, Runeforged Hammer,
    Spectral Armor, Screeching Gargoyle, Hydra''s Lament, Eye of the Storm, Void Stone,
    Stone of Binding, Void Shield, Erosion, Genji''s Guard, Titan''s Bane, Shield
    of the Phoenix, Oath-Sworn Spear, Tekko-Kagi, Breastplate of Valor, Chandra''s
    Grace, Pendulum Blade, Heartseeker, Golden Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.68
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.49
      efficiency: 0.29
      win: 0.69
      pick: 0.35
      fit: 0.44
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
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
