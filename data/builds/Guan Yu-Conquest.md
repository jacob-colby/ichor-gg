---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.73
  aspect_win_rate: 0.57
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.23
    win_rate: 0.65
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.11
      win_rate: 0.65
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.53
  - name: Breastplate of Valor
    pick_rate: 0.25
    win_rate: 0.7
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.4
  - name: Genji's Guard
    pick_rate: 0.28
    win_rate: 0.62
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.22
      win_rate: 0.58
    - name: Prophetic Cloak
      pick_rate: 0.05
      win_rate: 0.86
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.73
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.52
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.89
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.88
    alternates:
    - name: Amanita Charm
      pick_rate: 0.06
      win_rate: 1.0
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.83
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.71
    alternates:
    - name: Legionnaire Armor
      pick_rate: 0.07
      win_rate: 0.4
    - name: Adroit Ring
      pick_rate: 0.05
      win_rate: 0.25
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-08-01'
  god_win_rate: 0.5761589403973509
  god_matches_won: 87
  god_matches_played: 151
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Kinetic Cuirass, Eye of Providence, Shield Splitter,
    Amanita Charm, Runeforged Hammer, The Crusher, Hydra''s Lament, Spectral Armor,
    Eye of the Storm, Erosion, Avenging Blade, Shield of the Phoenix, Golden Blade,
    Berserker''s Shield, Pharaoh''s Curse, The Reaper, Chandra''s Grace, Tyrfing,
    Gladiator''s Shield, Wyrmskin Hide, Midgardian Mail, Lernaean Bow, Leviathan''s
    Hide, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.5
      efficiency: 0.44
      win: 0.62
      pick: 0.28
      fit: 0.32
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.4
      win: 0.7
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
      total: 0.48
      efficiency: 0.29
      win: 0.65
      pick: 0.23
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
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, The Reaper,
    Chandra''s Grace, Kinetic Cuirass, Eye of Providence, The Crusher, Runeforged
    Hammer, Shield Splitter, Hydra''s Lament, Phoenix Feather, Spectral Armor, Eye
    of the Storm, Avenging Blade, Erosion, Golden Blade, Spirit Robe, Berserker''s
    Shield, Pharaoh''s Curse, Tyrfing, Bloodforge, Lernaean Bow, Gladiator''s Shield,
    Glorious Pridwen, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.44
      win: 0.62
      pick: 0.28
      fit: 0.26
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.4
      win: 0.7
      pick: 0.25
      fit: 0.26
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.35
    Shield of the Phoenix:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.69
    Shifter's Shield:
      total: 0.47
      efficiency: 0.29
      win: 0.65
      pick: 0.23
      fit: 0.4
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
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Avenging Blade
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Kinetic Cuirass,
    The Reaper, Eye of Providence, Shield Splitter, Amanita Charm, Runeforged Hammer,
    Screeching Gargoyle, Hydra''s Lament, Spectral Armor, Tekko-Kagi, Eye of the Storm,
    Void Stone, Void Shield, Stone of Binding, Erosion, Shield of the Phoenix, Oath-Sworn
    Spear, Berserker''s Shield, Golden Blade, Pendulum Blade, Chandra''s Grace, Heartseeker,
    Pharaoh''s Curse, Tyrfing.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.48
      efficiency: 0.44
      win: 0.62
      pick: 0.28
      fit: 0.24
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.4
      win: 0.7
      pick: 0.25
      fit: 0.24
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.46
      efficiency: 0.29
      win: 0.65
      pick: 0.23
      fit: 0.38
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
