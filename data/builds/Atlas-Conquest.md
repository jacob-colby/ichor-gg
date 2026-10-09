---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.62
  slot_order:
  - name: Stampede
    pick_rate: 0.25
    win_rate: 0.48
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.46
    - name: Yogi's Necklace
      pick_rate: 0.08
      win_rate: 0.4
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.57
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.42
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 0.44
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.7
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.3
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.16
      win_rate: 0.67
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.38
  - name: Stygian Anchor
    pick_rate: 0.06
    win_rate: 0.83
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.71
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.5
  - name: Sage's Ring
    pick_rate: 0.07
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.75
    - name: Contagion
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.23
    win_rate: 0.45
  - name: Bumba's Hammer
    pick_rate: 0.21
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-10-09'
  god_win_rate: 0.5476190476190477
  god_matches_won: 69
  god_matches_played: 126
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-09'
  god_matches_analyzed: 2961
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Rod of Tahuti, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion, Helm of Darkness,
    Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear
    of Desolation, Hussar''s Wings, Prophetic Cloak.'
  slot_scores:
    Stygian Anchor:
      total: 0.61
      efficiency: 0.45
      win: 0.83
      pick: 0.13
      fit: 0.51
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.39
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.81
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Shifter''s Shield, Rod of Tahuti, Soul Gem, Erosion, Eye of Providence, Breastplate
    of Valor, Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather,
    Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile, Yogi''s Necklace.'
  slot_scores:
    Stygian Anchor:
      total: 0.6
      efficiency: 0.45
      win: 0.83
      pick: 0.13
      fit: 0.43
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.36
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.92
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Stygian Anchor
  - Genji's Guard
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Spear of the Magus,
    Soul Gem, Void Shield, Breastplate of Valor, Obsidian Shard, Shifter''s Shield,
    Void Stone, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Doom Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.49
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.5
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.75
    Stygian Anchor:
      total: 0.59
      efficiency: 0.45
      win: 0.83
      pick: 0.13
      fit: 0.35
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.27
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of Radiance,
    Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the Magus,
    Spear of Desolation, Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle
    Of Discord, Bracer of The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Stygian Anchor:
      total: 0.58
      efficiency: 0.45
      win: 0.83
      pick: 0.13
      fit: 0.26
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.2
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.43
      efficiency: 0.44
      win: 0.47
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Stygian Anchor
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  flex_slots:
  - Shield of the Phoenix
  - Contagion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Rod of Tahuti, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant, Erosion, Helm of Radiance,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Prophetic
    Cloak, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of
    Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail,
    Daybreak Gavel.'
  slot_scores:
    Contagion:
      total: 0.48
      efficiency: 0.39
      win: 0.67
      pick: 0.15
      fit: 0.23
    Stygian Anchor:
      total: 0.58
      efficiency: 0.45
      win: 0.83
      pick: 0.13
      fit: 0.32
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.48
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Contagion
  - Stygian Anchor
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak,
    Hide of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.45
      efficiency: 0.61
      win: 0.3
      pick: 0.15
      fit: 0.64
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
