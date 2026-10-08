---
type: smite-build
god: Odin
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.38
    win_rate: 0.5
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.19
      win_rate: 0.5
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 1.0
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.75
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.19
      win_rate: 0.5
    - name: Sanguine Lash
      pick_rate: 0.1
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 1.0
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.0
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.2
      win_rate: 1.0
    - name: Talisman of Purification
      pick_rate: 0.1
      win_rate: 1.0
  - name: Mana Tome
    pick_rate: 0.06
    win_rate: 0.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 1.0
  - name: Blinking Abyss
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Glorious Pridwen
      pick_rate: 0.1
      win_rate: 1.0
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.8
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.5
  - name: Warrior's Axe
    pick_rate: 0.19
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/odin/
  last_verified: '2026-10-08'
  god_win_rate: 0.5714285714285714
  god_matches_won: 12
  god_matches_played: 21
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Gauntlet of Thebes
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Glorious Pridwen
  flex_slots:
  - Breastplate of Valor
  - Gauntlet of Thebes
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield Splitter, Runeforged Hammer, Eye of the Storm,
    Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale, Shield of the
    Phoenix, Stone of Binding, Heartseeker, Magi''s Cloak, Avenging Blade, Mantle
    Of Discord, Midgardian Mail, Screeching Gargoyle, Titan''s Bane, The Crusher,
    Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Daybreak Gavel.'
  slot_scores:
    Gauntlet of Thebes:
      total: 0.57
      efficiency: 0.26
      win: 1.0
      pick: 0.14
      fit: 0.15
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.22
      fit: 0.29
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.26
      fit: 0.29
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.31
      fit: 0.64
    Freya's Tears:
      total: 0.75
      efficiency: 0.61
      win: 1.0
      pick: 0.17
      fit: 0.49
    Glorious Pridwen:
      total: 0.67
      efficiency: 0.38
      win: 1.0
      pick: 0.31
      fit: 0.49
  community_ordered:
  - Gauntlet of Thebes
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Glorious Pridwen
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Gauntlet of Thebes
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Glorious Pridwen
  flex_slots:
  - Breastplate of Valor
  - Gauntlet of Thebes
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Shield Splitter, Runeforged Hammer, Heartseeker, Berserker''s Shield, Eye
    of the Storm, Shield of the Phoenix, Erosion, Stone of Binding, Eye of Providence,
    Avenging Blade, Draconic Scale, Screeching Gargoyle, Magi''s Cloak, Titan''s Bane,
    The Crusher, Daybreak Gavel, Oni Hunter''s Garb, Transcendence, Midgardian Mail,
    Mantle Of Discord, The Reaper, Arondight.'
  slot_scores:
    Gauntlet of Thebes:
      total: 0.57
      efficiency: 0.26
      win: 1.0
      pick: 0.14
      fit: 0.17
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.22
      fit: 0.29
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.26
      fit: 0.29
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.31
      fit: 0.46
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.17
      fit: 0.35
    Glorious Pridwen:
      total: 0.65
      efficiency: 0.38
      win: 1.0
      pick: 0.31
      fit: 0.35
  community_ordered:
  - Gauntlet of Thebes
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Glorious Pridwen
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Glorious Pridwen
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Runeforged Hammer, The Reaper,
    Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace,
    Eye of Providence, Draconic Scale, Phoenix Feather, Avenging Blade, Heartseeker,
    Chandra''s Grace, Stone of Binding, Midgardian Mail, Daybreak Gavel, Titan''s
    Bane, The Crusher, Hide of the Nemean Lion, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.22
      fit: 0.27
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.26
      fit: 0.27
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.31
      fit: 0.62
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.17
      fit: 0.43
    Glorious Pridwen:
      total: 0.71
      efficiency: 0.38
      win: 1.0
      pick: 0.31
      fit: 0.73
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Glorious Pridwen
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Glorious Pridwen
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Avenging Blade, Screeching Gargoyle,
    Void Shield, Heartseeker, Shield Splitter, Void Stone, Runeforged Hammer, Berserker''s
    Shield, Titan''s Bane, The Crusher, Eye of the Storm, The Reaper, Erosion, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak, Pendulum
    Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.22
      fit: 0.24
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.38
      fit: 0.56
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.26
      fit: 0.24
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.31
      fit: 0.54
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.17
      fit: 0.39
    Glorious Pridwen:
      total: 0.66
      efficiency: 0.38
      win: 1.0
      pick: 0.31
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Glorious Pridwen
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  - Riptalon
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Golden Blade, Riptalon, Tyrfing,
    Silverbranch Bow, Shield Splitter, Runeforged Hammer, Pharaoh''s Curse, Lernaean
    Bow, Toxic Blade, Shogun''s Ofuda, Erosion, The Reaper, Stone of Binding, Eye
    of Providence, Eye of the Storm, Shield of the Phoenix, Tekko-Kagi, Draconic Scale,
    Magi''s Cloak, Heartseeker, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.52
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.22
      fit: 0.19
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.17
      fit: 0.32
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.31
      fit: 0.45
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Glorious Pridwen
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield of the Phoenix,
    Screeching Gargoyle, Berserker''s Shield, Shield Splitter, Runeforged Hammer,
    Prophetic Cloak, Erosion, Eye of Providence, Stone of Binding, Gladiator''s Shield,
    Draconic Scale, Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle
    Of Discord, Midgardian Mail, Daybreak Gavel, Heartseeker, Pendulum Blade, Hide
    of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.76
      efficiency: 0.66
      win: 1.0
      pick: 0.22
      fit: 0.44
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.38
      fit: 0.5
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.26
      fit: 0.44
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.31
      fit: 0.51
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 0.17
      fit: 0.59
    Glorious Pridwen:
      total: 0.69
      efficiency: 0.38
      win: 1.0
      pick: 0.31
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Glorious Pridwen
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Shield Splitter, Runeforged Hammer, Eye
    of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Stone of Binding, Heartseeker, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Titan''s Bane,
    The Crusher, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede,
    Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.38
      fit: 0.46
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.22
      fit: 0.29
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.31
      fit: 0.64
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.75
      efficiency: 0.61
      win: 1.0
      pick: 0.17
      fit: 0.49
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
