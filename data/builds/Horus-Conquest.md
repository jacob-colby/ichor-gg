---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.33
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.31
    win_rate: 0.55
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.23
      win_rate: 0.59
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.63
  - name: Genji's Guard
    pick_rate: 0.23
    win_rate: 0.61
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.55
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.24
      win_rate: 0.59
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.6
  - name: Dwarven Plate
    pick_rate: 0.13
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.54
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.71
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.38
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.1
      win_rate: 0.63
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.71
  - name: Veve Charm
    pick_rate: 0.07
    win_rate: 0.76
    alternates:
    - name: Engraved Guard
      pick_rate: 0.1
      win_rate: 0.63
    - name: Legionnaire Armor
      pick_rate: 0.05
      win_rate: 0.75
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-07-25'
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
  god_win_rate: 0.5947540983606557
  god_matches_won: 907
  god_matches_played: 1525
  god_division: obsidian
  god_window_start: '2026-07-14'
  god_window_end: '2026-07-27'
  god_matches_analyzed: 17172
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
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
    this god: Kinetic Cuirass, Eye of Providence, Breastplate of Valor, Amanita Charm,
    Jotunn''s Revenge, Spectral Armor, Erosion, Shield Splitter, Shield of the Phoenix,
    Eye of the Storm, Runeforged Hammer, Berserker''s Shield, Hydra''s Lament, Gladiator''s
    Shield, Chandra''s Grace, The Crusher, Avenging Blade, Midgardian Mail, Freya''s
    Tears, Draconic Scale, Prophetic Cloak, Pharaoh''s Curse, Leviathan''s Hide, Ancile,
    Phoenix Feather, Oni Hunter''s Garb.'
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
      win: 0.61
      pick: 0.23
      fit: 0.42
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.42
      win: 0.59
      pick: 0.13
      fit: 0.42
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.76
    Amanita Charm:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
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
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Eye of Providence
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Chandra''s Grace,
    Breastplate of Valor, Eye of Providence, Jotunn''s Revenge, Phoenix Feather, Spectral
    Armor, The Reaper, Shield Splitter, Erosion, Runeforged Hammer, Hydra''s Lament,
    Spirit Robe, The Crusher, Eye of the Storm, Berserker''s Shield, Avenging Blade,
    Gladiator''s Shield, Glorious Pridwen, Midgardian Mail, Pharaoh''s Curse, Leviathan''s
    Hide, Ancile, Oni Hunter''s Garb, Screeching Gargoyle.'
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
      win: 0.61
      pick: 0.23
      fit: 0.32
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.42
      win: 0.59
      pick: 0.13
      fit: 0.32
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.79
    Amanita Charm:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.81
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - Eye of Providence
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
    for this god: Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Breastplate of
    Valor, Eye of Providence, Avenging Blade, Amanita Charm, Screeching Gargoyle,
    Spectral Armor, The Reaper, Shield Splitter, Void Stone, Erosion, Void Shield,
    Shield of the Phoenix, Stone of Binding, Runeforged Hammer, Hydra''s Lament, Eye
    of the Storm, Berserker''s Shield, Chandra''s Grace, Titan''s Bane, Gladiator''s
    Shield, Tekko-Kagi, Midgardian Mail, Oath-Sworn Spear, Pendulum Blade.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.49
      efficiency: 0.46
      win: 0.61
      pick: 0.23
      fit: 0.29
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.42
      win: 0.59
      pick: 0.13
      fit: 0.29
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
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
