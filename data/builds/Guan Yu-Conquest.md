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
    Hydra''s Lament, Jotunn''s Revenge, Eye of Providence, The Crusher, Oni Hunter''s
    Garb, Avenging Blade, Shield Splitter, Golden Blade, Pharaoh''s Curse, Lernaean
    Bow, Shield of the Phoenix, Eye of the Storm, Spectral Armor, Freya''s Tears,
    Mantle Of Discord, Erosion, Draconic Scale, Yogi''s Necklace, Shogun''s Ofuda,
    Damaru, Leviathan''s Hide.'
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
    Hammer, Kinetic Cuirass, Hydra''s Lament, Chandra''s Grace, Jotunn''s Revenge,
    Eye of Providence, Oni Hunter''s Garb, The Crusher, Avenging Blade, Golden Blade,
    The Reaper, Pharaoh''s Curse, Eye of the Storm, Lernaean Bow, Spectral Armor,
    Shield Splitter, Riptalon, Freya''s Tears, Phoenix Feather, Yogi''s Necklace,
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
    Runeforged Hammer, Kinetic Cuirass, Hydra''s Lament, Amanita Charm, Oni Hunter''s
    Garb, Eye of Providence, Lernaean Bow, The Reaper, Pharaoh''s Curse, Golden Blade,
    Spectral Armor, Void Shield, Screeching Gargoyle, Shield of the Phoenix, Heartseeker,
    Stone of Binding, Shield Splitter, Riptalon, Eye of the Storm, Freya''s Tears,
    Yogi''s Necklace, Mantle Of Discord.'
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
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Shifter's Shield
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Kinetic Cuirass, Runeforged Hammer,
    Amanita Charm, Pharaoh''s Curse, Lernaean Bow, Hydra''s Lament, Oni Hunter''s
    Garb, The Crusher, Eye of Providence, Jotunn''s Revenge, Riptalon, Spectral Armor,
    Avenging Blade, Shogun''s Ofuda, Shield of the Phoenix, Tyrfing, Yogi''s Necklace,
    Freya''s Tears, Mantle Of Discord, Shield Splitter, Eros'' Bow, Eye of the Storm,
    Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.58
      efficiency: 0.74
      win: 0.62
      pick: 0.28
      fit: 0.22
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.67
      win: 0.7
      pick: 0.25
      fit: 0.22
    Shifter's Shield:
      total: 0.56
      efficiency: 0.58
      win: 0.65
      pick: 0.23
      fit: 0.35
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Berserker''s Shield,
    Jotunn''s Revenge, Shield of the Phoenix, Kinetic Cuirass, Amanita Charm, Freya''s
    Tears, Runeforged Hammer, Eye of Providence, Oni Hunter''s Garb, The Crusher,
    Chandra''s Grace, Pharaoh''s Curse, Spectral Armor, Lernaean Bow, Avenging Blade,
    Arondight, Mantle Of Discord, Golden Blade, Yogi''s Necklace, Gladiator''s Shield,
    Shield Splitter, Eye of the Storm, Erosion, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.74
      win: 0.62
      pick: 0.28
      fit: 0.44
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.67
      win: 0.7
      pick: 0.25
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shifter's Shield:
      total: 0.57
      efficiency: 0.58
      win: 0.65
      pick: 0.23
      fit: 0.4
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
    Runeforged Hammer, Hydra''s Lament, Jotunn''s Revenge, Eye of Providence, The
    Crusher, Oni Hunter''s Garb, Avenging Blade, Shield Splitter, Golden Blade, Pharaoh''s
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
