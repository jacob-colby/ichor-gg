---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.09
  aspect_win_rate: 1.0
  slot_order:
  - name: Stampede
    pick_rate: 0.26
    win_rate: 0.33
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.13
      win_rate: 1.0
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 1.0
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.33
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.67
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 1.0
  - name: Ancile
    pick_rate: 0.14
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.0
  - name: Ethereal Staff
    pick_rate: 0.2
    win_rate: 0.25
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.0
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.24
    win_rate: 0.75
    alternates:
    - name: Contagion
      pick_rate: 0.12
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.0
  - name: Veve Charm
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Erosion
      pick_rate: 0.13
      win_rate: 1.0
    - name: Engraved Guard
      pick_rate: 0.13
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.26
    win_rate: 0.5
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.09
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-09-10'
  god_win_rate: 0.6086956521739131
  god_matches_won: 14
  god_matches_played: 23
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Contagion
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Freya''s Tears, Shifter''s
    Shield, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Helm of Darkness, Leviathan''s
    Hide, Void Shield, Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s
    Wings.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.81
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.26
      fit: 0.3
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.64
      efficiency: 0.55
      win: 0.75
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.76
      efficiency: 0.51
      win: 1.0
      pick: 0.4
      fit: 0.71
  community_ordered:
  - Contagion
  - Erosion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Contagion
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Yogi''s Necklace, Amanita Charm, Shield of the Phoenix, Rod of Tahuti,
    Kinetic Cuirass, Freya''s Tears, Rod of Asclepius, Shifter''s Shield, Soul Gem,
    Eye of Providence, Draconic Scale, Gluttonous Grimoire, Phoenix Feather, Chandra''s
    Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding, Helm of
    Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s Cloak.'
  slot_scores:
    Yogi's Necklace:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.13
      fit: 0.57
    Contagion:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.26
      fit: 0.37
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.75
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.72
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.75
      efficiency: 0.51
      win: 1.0
      pick: 0.4
      fit: 0.7
  community_ordered:
  - Yogi's Necklace
  - Contagion
  - Erosion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Contagion
  - Yogi's Necklace
  - Kinetic Cuirass
  - Freya's Tears
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Freya''s Tears, Screeching Gargoyle, Spear of Desolation, Spear
    of the Magus, Soul Gem, Void Shield, Obsidian Shard, Shifter''s Shield, Void Stone,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle Of Discord, Midgardian
    Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Stone of Binding:
      total: 0.63
      efficiency: 0.51
      win: 0.75
      pick: 0.0
      fit: 0.75
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.26
      fit: 0.24
    Yogi's Necklace:
      total: 0.66
      efficiency: 0.52
      win: 1.0
      pick: 0.13
      fit: 0.14
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.0
      fit: 0.44
    Erosion:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.4
      fit: 0.49
  community_ordered:
  - Contagion
  - Yogi's Necklace
  - Erosion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Yogi's Necklace
  - Contagion
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Erosion
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Freya''s
    Tears, Gluttonous Grimoire, Shifter''s Shield, Soul Gem, Helm of Radiance, Stone
    of Binding, Eye of Providence, Shield of the Phoenix, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the Magus, Spear of Desolation,
    Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of
    The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Yogi's Necklace:
      total: 0.65
      efficiency: 0.52
      win: 1.0
      pick: 0.13
      fit: 0.1
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.26
      fit: 0.2
    Bracer of The Abyss:
      total: 0.56
      efficiency: 0.52
      win: 0.75
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.56
      efficiency: 0.44
      win: 0.75
      pick: 0.0
      fit: 0.44
    Erosion:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.4
      fit: 0.36
  community_ordered:
  - Yogi's Necklace
  - Contagion
  - Erosion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Kinetic Cuirass
  - Contagion
  - Shield of the Phoenix
  - Freya's Tears
  - Spear of Desolation
  - Erosion
  flex_slots:
  - Shield of the Phoenix
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Amanita
    Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant, Helm of Radiance, Gluttonous
    Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.55
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.26
      fit: 0.23
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.53
      win: 0.75
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.75
      pick: 0.0
      fit: 0.46
    Erosion:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.4
      fit: 0.45
  community_ordered:
  - Contagion
  - Erosion
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Freya''s
    Tears, Shifter''s Shield, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion, Helm
    of Darkness, Leviathan''s Hide, Void Shield, Oni Hunter''s Garb, Xibalban Effigy,
    Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.29
      efficiency: 0.65
      win: 0.0
      pick: 0.16
      fit: 0.39
    Genji's Guard:
      total: 0.45
      efficiency: 0.66
      win: 0.33
      pick: 0.18
      fit: 0.39
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.64
      efficiency: 0.55
      win: 0.75
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  starter: *id001
---
