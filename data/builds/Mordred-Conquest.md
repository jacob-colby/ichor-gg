---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.64
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.43
    win_rate: 0.57
    alternates:
    - name: Barbed Carver
      pick_rate: 0.2
      win_rate: 0.45
    - name: Bracer of The Abyss
      pick_rate: 0.08
      win_rate: 0.63
  - name: Shield of the Phoenix
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.14
      win_rate: 0.71
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.67
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.63
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.65
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.5
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.31
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.55
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-08-01'
  god_win_rate: 0.5451977401129944
  god_matches_won: 193
  god_matches_played: 354
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
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
  - Amanita Charm
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Kinetic Cuirass, Eye of Providence, Shield Splitter,
    Amanita Charm, Runeforged Hammer, Spectral Armor, Eye of the Storm, The Crusher,
    Hydra''s Lament, Erosion, Avenging Blade, Berserker''s Shield, Wyrmskin Hide,
    Breastplate of Valor, Chandra''s Grace, Golden Blade, Midgardian Mail, Gladiator''s
    Shield, Pendulum Blade, Heartseeker, Pharaoh''s Curse, Mantle Of Discord, Titan''s
    Bane, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shifter's Shield:
      total: 0.46
      efficiency: 0.29
      win: 0.57
      pick: 0.43
      fit: 0.54
    Amanita Charm:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - The Crusher
  flex_slots:
  - The Crusher
  - Hide of the Nemean Lion
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Kinetic Cuirass, Eye of Providence, The Crusher, Hydra''s
    Lament, Amanita Charm, Shield Splitter, Runeforged Hammer, Spectral Armor, Eye
    of the Storm, Avenging Blade, Erosion, Pendulum Blade, Chandra''s Grace, Breastplate
    of Valor, Heartseeker, Titan''s Bane, Berserker''s Shield, Gladiator''s Shield,
    Screeching Gargoyle, Midgardian Mail, Yogi''s Necklace, Golden Blade, Pharaoh''s
    Curse, The Reaper, Freya''s Tears.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.38
    Genji's Guard:
      total: 0.45
      efficiency: 0.46
      win: 0.53
      pick: 0.18
      fit: 0.27
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.48
    Hide of the Nemean Lion:
      total: 0.44
      efficiency: 0.32
      win: 0.65
      pick: 0.06
      fit: 0.25
    The Crusher:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Eye of Providence,
    Chandra''s Grace, Runeforged Hammer, Shield Splitter, Phoenix Feather, Spectral
    Armor, Eye of the Storm, The Crusher, Hydra''s Lament, The Reaper, Avenging Blade,
    Erosion, Spirit Robe, Golden Blade, Berserker''s Shield, Wyrmskin Hide, Midgardian
    Mail, Pendulum Blade, Gladiator''s Shield, Heartseeker, Bloodforge, Pharaoh''s
    Curse, Breastplate of Valor.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.52
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.4
      win: 0.5
      pick: 0.17
      fit: 0.77
    Hide of the Nemean Lion:
      total: 0.46
      efficiency: 0.32
      win: 0.65
      pick: 0.06
      fit: 0.36
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - The Crusher
  flex_slots:
  - Eye of Providence
  - Hide of the Nemean Lion
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
    for this god: Jotunn''s Revenge, Avenging Blade, The Crusher, Kinetic Cuirass,
    Eye of Providence, Shield Splitter, Amanita Charm, Runeforged Hammer, Spectral
    Armor, Screeching Gargoyle, Hydra''s Lament, Eye of the Storm, Heartseeker, Void
    Stone, Stone of Binding, Pendulum Blade, Void Shield, Titan''s Bane, Erosion,
    Oath-Sworn Spear, The Reaper, Berserker''s Shield, Breastplate of Valor, Chandra''s
    Grace, Midgardian Mail, Golden Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.69
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.54
    Hide of the Nemean Lion:
      total: 0.45
      efficiency: 0.32
      win: 0.65
      pick: 0.06
      fit: 0.28
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
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Runeforged Hammer
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Kinetic Cuirass, Eye of Providence,
    Shield Splitter, Amanita Charm, Runeforged Hammer, Spectral Armor, Eye of the
    Storm, The Crusher, Hydra''s Lament, Erosion, Avenging Blade, Berserker''s Shield,
    Wyrmskin Hide, Breastplate of Valor, Chandra''s Grace, Golden Blade, Midgardian
    Mail, Gladiator''s Shield, Pendulum Blade, Heartseeker, Pharaoh''s Curse, Mantle
    Of Discord, Titan''s Bane, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.59
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
---
