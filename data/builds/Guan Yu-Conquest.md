---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.66
  aspect_win_rate: 0.62
  slot_order:
  - name: Heartwood Charm
    pick_rate: 0.16
    win_rate: 0.65
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.53
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.92
  - name: Breastplate of Valor
    pick_rate: 0.31
    win_rate: 0.74
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.48
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.53
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.17
      win_rate: 0.78
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.42
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.76
    - name: Talisman of Purification
      pick_rate: 0.07
      win_rate: 0.71
  - name: Draconic Scale
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.63
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.8
  - name: Olmec Blue
    pick_rate: 0.15
    win_rate: 0.57
    alternates:
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 0.75
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.75
  community_starters:
  - name: Sands of Time
    pick_rate: 0.28
    win_rate: 0.53
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.5
  - name: Pendulum of The Ages
    pick_rate: 0.13
    win_rate: 0.71
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-08-14'
  god_win_rate: 0.5462962962962963
  god_matches_won: 59
  god_matches_played: 108
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Jotunn''s Revenge,
    The Crusher, Hydra''s Lament, Shield of the Phoenix, Oni Hunter''s Garb, Pharaoh''s
    Curse, Shield Splitter, Runeforged Hammer, Golden Blade, Eye of the Storm, Erosion,
    Eye of Providence, Spectral Armor, Lernaean Bow, Shogun''s Ofuda, Leviathan''s
    Hide, Midgardian Mail, Avenging Blade, Mantle Of Discord, Stone of Binding, Screeching
    Gargoyle, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.74
      pick: 0.42
      fit: 0.32
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.6
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.5
      win: 0.75
      pick: 0.25
      fit: 0.33
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.71
      pick: 0.17
      fit: 0.5
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.5
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Berserker''s Shield, Kinetic Cuirass,
    Jotunn''s Revenge, Chandra''s Grace, The Crusher, Oni Hunter''s Garb, Hydra''s
    Lament, Runeforged Hammer, Pharaoh''s Curse, The Reaper, Golden Blade, Riptalon,
    Eye of the Storm, Phoenix Feather, Shield Splitter, Erosion, Spectral Armor, Eye
    of Providence, Shogun''s Ofuda, Lernaean Bow, Leviathan''s Hide, Avenging Blade,
    Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.74
      pick: 0.42
      fit: 0.3
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.79
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.5
      win: 0.75
      pick: 0.25
      fit: 0.35
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.71
      pick: 0.17
      fit: 0.5
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Draconic Scale
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Draconic Scale
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Berserker''s Shield, Kinetic Cuirass,
    Amanita Charm, Avenging Blade, Stone of Binding, Screeching Gargoyle, Void Shield,
    Hydra''s Lament, Oni Hunter''s Garb, Shield of the Phoenix, Riptalon, Void Stone,
    Runeforged Hammer, Pharaoh''s Curse, The Reaper, Silverbranch Bow, Shield Splitter,
    Golden Blade, Spectral Armor, Heartseeker, Erosion, Lernaean Bow, Eye of the Storm,
    Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.66
      win: 0.74
      pick: 0.42
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.55
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.5
      win: 0.75
      pick: 0.25
      fit: 0.25
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.71
      pick: 0.17
      fit: 0.38
    The Crusher:
      total: 0.58
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Draconic Scale
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Golden Blade, Jotunn''s
    Revenge, Pharaoh''s Curse, Riptalon, The Crusher, Oni Hunter''s Garb, Lernaean
    Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Silverbranch Bow,
    Tyrfing, Runeforged Hammer, Spectral Armor, Erosion, Shield Splitter, Eye of Providence,
    Eye of the Storm, Leviathan''s Hide, Eros'' Bow, Yogi''s Necklace, Shifter''s
    Shield.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.66
      win: 0.74
      pick: 0.42
      fit: 0.22
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.5
      win: 0.75
      pick: 0.25
      fit: 0.23
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.71
      pick: 0.17
      fit: 0.35
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.57
      win: 0.61
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
  - Hide of the Nemean Lion
  - Draconic Scale
  flex_slots:
  - Berserker's Shield
  - Draconic Scale
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield,
    Shield of the Phoenix, Kinetic Cuirass, Amanita Charm, Hydra''s Lament, Oni Hunter''s
    Garb, The Crusher, Screeching Gargoyle, Pharaoh''s Curse, Chandra''s Grace, Gladiator''s
    Shield, Spectral Armor, Erosion, Runeforged Hammer, Eye of Providence, Prophetic
    Cloak, Shield Splitter, Shogun''s Ofuda, Golden Blade, Leviathan''s Hide, Eye
    of the Storm, Lernaean Bow, Midgardian Mail, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.53
      pick: 0.25
      fit: 0.44
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.66
      win: 0.74
      pick: 0.42
      fit: 0.44
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.43
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.5
      win: 0.75
      pick: 0.25
      fit: 0.26
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.71
      pick: 0.17
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm,
    Jotunn''s Revenge, The Crusher, Hydra''s Lament, Shield of the Phoenix, Oni Hunter''s
    Garb, Pharaoh''s Curse, Shield Splitter, Runeforged Hammer, Golden Blade, Shifter''s
    Shield, Eye of the Storm, Erosion, Eye of Providence, Spectral Armor, Lernaean
    Bow, Shogun''s Ofuda, Leviathan''s Hide, Midgardian Mail, Avenging Blade, Mantle
    Of Discord, Stone of Binding, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.53
      pick: 0.25
      fit: 0.32
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.16
      fit: 0.49
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Kinetic Cuirass,
    Amanita Charm, Jotunn''s Revenge, The Crusher, Hydra''s Lament, Shield of the
    Phoenix, Oni Hunter''s Garb, Pharaoh''s Curse, Shield Splitter, Runeforged Hammer,
    Golden Blade, Shifter''s Shield, Eye of the Storm, Erosion, Eye of Providence,
    Spectral Armor, Lernaean Bow, Shogun''s Ofuda, Leviathan''s Hide, Midgardian Mail,
    Avenging Blade, Mantle Of Discord, Stone of Binding, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.53
      pick: 0.25
      fit: 0.32
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.74
      pick: 0.42
      fit: 0.32
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.5
  swaps:
  - added: Breastplate of Valor
    removed: Freya's Tears
    reason: community 74% win over 33 matches (vs 55% on this god), taking the model's
      weakest slot from Freya's Tears
  starter: *id001
---
