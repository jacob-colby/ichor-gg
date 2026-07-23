---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.2
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.28
    win_rate: 0.56
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.25
      win_rate: 0.6
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.63
  - name: Genji's Guard
    pick_rate: 0.23
    win_rate: 0.62
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.62
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.57
  - name: Breastplate of Valor
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.62
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.54
  - name: Dwarven Plate
    pick_rate: 0.13
    win_rate: 0.65
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.54
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.76
  - name: Spirit Robe
    pick_rate: 0.07
    win_rate: 0.72
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.1
      win_rate: 0.64
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.35
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Veve Charm
      pick_rate: 0.08
      win_rate: 0.81
    - name: Legionnaire Armor
      pick_rate: 0.05
      win_rate: 0.75
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-07-23'
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Spirit Robe
  - Shifter's Shield
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Breastplate of Valor, Amanita Charm,
    Jotunn''s Revenge, Spectral Armor, Shield Splitter, Erosion, Shield of the Phoenix,
    Eye of the Storm, Runeforged Hammer, Gladiator''s Shield, Hydra''s Lament, Berserker''s
    Shield, Chandra''s Grace, The Crusher, Prophetic Cloak, Freya''s Tears, Avenging
    Blade, Midgardian Mail, Draconic Scale, Screeching Gargoyle, Shroud of Vengeance,
    Leviathan''s Hide, Mantle Of Discord, Pharaoh''s Curse.'
  slot_scores:
    Eye of Providence:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.51
      efficiency: 0.46
      win: 0.62
      pick: 0.23
      fit: 0.42
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.42
      win: 0.6
      pick: 0.12
      fit: 0.42
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.76
    Spirit Robe:
      total: 0.51
      efficiency: 0.32
      win: 0.72
      pick: 0.07
      fit: 0.46
    Shifter's Shield:
      total: 0.47
      efficiency: 0.3
      win: 0.56
      pick: 0.28
      fit: 0.66
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Spirit Robe
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Spirit Robe, Amanita Charm, Shield of the Phoenix, Breastplate of Valor,
    Kinetic Cuirass, Chandra''s Grace, Eye of Providence, Jotunn''s Revenge, Phoenix
    Feather, Spectral Armor, The Reaper, Shield Splitter, Erosion, Runeforged Hammer,
    Hydra''s Lament, The Crusher, Eye of the Storm, Berserker''s Shield, Glorious
    Pridwen, Gladiator''s Shield, Avenging Blade, Midgardian Mail, Screeching Gargoyle,
    Leviathan''s Hide, Pharaoh''s Curse, Prophetic Cloak, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.51
    Genji's Guard:
      total: 0.5
      efficiency: 0.46
      win: 0.62
      pick: 0.23
      fit: 0.32
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.42
      win: 0.6
      pick: 0.12
      fit: 0.32
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spirit Robe:
      total: 0.54
      efficiency: 0.32
      win: 0.72
      pick: 0.07
      fit: 0.64
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.81
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spirit Robe
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
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Breastplate of Valor, Kinetic Cuirass,
    Avenging Blade, Eye of Providence, Amanita Charm, Screeching Gargoyle, Spectral
    Armor, The Reaper, Shield Splitter, Void Stone, Stone of Binding, Void Shield,
    Erosion, Shield of the Phoenix, Runeforged Hammer, Hydra''s Lament, Eye of the
    Storm, Berserker''s Shield, Titan''s Bane, Chandra''s Grace, Gladiator''s Shield,
    Oath-Sworn Spear, Tekko-Kagi, Pendulum Blade, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.46
      win: 0.62
      pick: 0.23
      fit: 0.29
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.42
      win: 0.6
      pick: 0.12
      fit: 0.29
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spirit Robe:
      total: 0.49
      efficiency: 0.32
      win: 0.72
      pick: 0.07
      fit: 0.32
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.51
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
