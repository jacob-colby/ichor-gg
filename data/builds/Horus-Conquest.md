---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.37
    win_rate: 0.66
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.19
      win_rate: 0.56
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.63
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.63
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.51
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.6
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.29
      win_rate: 0.57
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.6
  - name: Breastplate of Valor
    pick_rate: 0.07
    win_rate: 0.71
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.6
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.64
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.74
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.39
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.72
  - name: Shield
    pick_rate: 0.06
    win_rate: 0.8
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.5
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.44
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-08-01'
  god_win_rate: 0.6051948051948052
  god_matches_won: 233
  god_matches_played: 385
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Amanita Charm
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Kinetic Cuirass, Eye of Providence, Amanita Charm,
    Jotunn''s Revenge, Spectral Armor, Erosion, Shield Splitter, Shield of the Phoenix,
    Eye of the Storm, Runeforged Hammer, Gladiator''s Shield, Hydra''s Lament, The
    Crusher, Chandra''s Grace, Berserker''s Shield, Midgardian Mail, Freya''s Tears,
    Avenging Blade, Draconic Scale, Prophetic Cloak, Pharaoh''s Curse, Leviathan''s
    Hide, Ancile, Oni Hunter''s Garb, Phoenix Feather.'
  slot_scores:
    Eye of Providence:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.51
      efficiency: 0.44
      win: 0.63
      pick: 0.19
      fit: 0.42
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.4
      win: 0.71
      pick: 0.07
      fit: 0.42
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.76
    Shifter's Shield:
      total: 0.52
      efficiency: 0.29
      win: 0.66
      pick: 0.37
      fit: 0.66
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
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Kinetic
    Cuirass, Chandra''s Grace, Eye of Providence, Jotunn''s Revenge, Phoenix Feather,
    Spectral Armor, The Reaper, Shield Splitter, Erosion, Runeforged Hammer, The Crusher,
    Hydra''s Lament, Spirit Robe, Eye of the Storm, Gladiator''s Shield, Avenging
    Blade, Glorious Pridwen, Berserker''s Shield, Midgardian Mail, Pharaoh''s Curse,
    Leviathan''s Hide, Ancile, Oni Hunter''s Garb, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.44
      win: 0.63
      pick: 0.19
      fit: 0.32
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.4
      win: 0.71
      pick: 0.07
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
    Shifter's Shield:
      total: 0.49
      efficiency: 0.29
      win: 0.66
      pick: 0.37
      fit: 0.51
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
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - The Crusher
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
    for this god: Breastplate of Valor, Jotunn''s Revenge, The Crusher, Kinetic Cuirass,
    Eye of Providence, Avenging Blade, Amanita Charm, Screeching Gargoyle, The Reaper,
    Spectral Armor, Shield Splitter, Void Stone, Void Shield, Erosion, Stone of Binding,
    Shield of the Phoenix, Runeforged Hammer, Hydra''s Lament, Eye of the Storm, Chandra''s
    Grace, Tekko-Kagi, Berserker''s Shield, Gladiator''s Shield, Pendulum Blade, Midgardian
    Mail, Oath-Sworn Spear, Heartseeker.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.44
      win: 0.63
      pick: 0.19
      fit: 0.29
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.4
      win: 0.71
      pick: 0.07
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
    Shifter's Shield:
      total: 0.49
      efficiency: 0.29
      win: 0.66
      pick: 0.37
      fit: 0.46
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
      total: 0.23
      efficiency: 0.55
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
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.23
      efficiency: 0.37
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
