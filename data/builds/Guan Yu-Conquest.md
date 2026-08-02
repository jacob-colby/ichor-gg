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
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Amanita Charm
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Runeforged Hammer,
    Hydra''s Lament, Blink Rune, Jotunn''s Revenge, Eye of Providence, The Crusher,
    Oni Hunter''s Garb, Avenging Blade, Shield Splitter, Golden Blade, Pharaoh''s
    Curse, Lernaean Bow, Shield of the Phoenix, Eye of the Storm, Spectral Armor,
    Freya''s Tears, Mantle Of Discord, Erosion, Draconic Scale, Yogi''s Necklace,
    Shogun''s Ofuda, Damaru, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.74
      win: 0.62
      pick: 0.28
      fit: 0.32
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.67
      win: 0.7
      pick: 0.25
      fit: 0.32
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shifter's Shield:
      total: 0.58
      efficiency: 0.58
      win: 0.65
      pick: 0.23
      fit: 0.5
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Berserker's Shield
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
    this god: Amanita Charm, Shield of the Phoenix, Berserker''s Shield, Runeforged
    Hammer, Kinetic Cuirass, Hydra''s Lament, Chandra''s Grace, Blink Rune, Jotunn''s
    Revenge, Eye of Providence, Oni Hunter''s Garb, The Crusher, Avenging Blade, Golden
    Blade, The Reaper, Pharaoh''s Curse, Eye of the Storm, Lernaean Bow, Spectral
    Armor, Shield Splitter, Riptalon, Freya''s Tears, Phoenix Feather, Yogi''s Necklace,
    Erosion, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.74
      win: 0.62
      pick: 0.28
      fit: 0.3
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.67
      win: 0.7
      pick: 0.25
      fit: 0.3
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.79
    Shifter's Shield:
      total: 0.58
      efficiency: 0.58
      win: 0.65
      pick: 0.23
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.8
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
  - The Crusher
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Berserker''s Shield,
    Blink Rune, Runeforged Hammer, Kinetic Cuirass, Hydra''s Lament, Amanita Charm,
    Oni Hunter''s Garb, Eye of Providence, Lernaean Bow, The Reaper, Pharaoh''s Curse,
    Golden Blade, Spectral Armor, Void Shield, Screeching Gargoyle, Shield of the
    Phoenix, Heartseeker, Stone of Binding, Shield Splitter, Riptalon, Eye of the
    Storm, Freya''s Tears, Yogi''s Necklace, Mantle Of Discord.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.59
      efficiency: 0.74
      win: 0.62
      pick: 0.28
      fit: 0.24
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.67
      win: 0.7
      pick: 0.25
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.56
      efficiency: 0.58
      win: 0.65
      pick: 0.23
      fit: 0.38
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.3
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.33
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.31
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Death Metal:
      total: 0.32
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.33
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.31
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Hydra's Lament
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm,
    Runeforged Hammer, Hydra''s Lament, Blink Rune, Jotunn''s Revenge, Eye of Providence,
    The Crusher, Oni Hunter''s Garb, Avenging Blade, Shield Splitter, Golden Blade,
    Pharaoh''s Curse, Lernaean Bow, Shield of the Phoenix, Eye of the Storm, Spectral
    Armor, Freya''s Tears, Mantle Of Discord, Erosion, Draconic Scale, Yogi''s Necklace,
    Shogun''s Ofuda, Damaru, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.74
      win: 0.62
      pick: 0.28
      fit: 0.32
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.6
    Hydra's Lament:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
---
