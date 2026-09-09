---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.1
  aspect_win_rate: 1.0
  slot_order:
  - name: Stampede
    pick_rate: 0.25
    win_rate: 0.4
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 1.0
    - name: Yogi's Necklace
      pick_rate: 0.1
      win_rate: 1.0
  - name: Prophetic Cloak
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 1.0
  - name: Genji's Guard
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Ancile
      pick_rate: 0.11
      win_rate: 1.0
    - name: Screeching Gargoyle
      pick_rate: 0.11
      win_rate: 0.5
  - name: Ethereal Staff
    pick_rate: 0.18
    win_rate: 0.33
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.5
    - name: Stampede
      pick_rate: 0.12
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.2
    win_rate: 1.0
    alternates:
    - name: Contagion
      pick_rate: 0.13
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.0
  - name: Veve Charm
    pick_rate: 0.29
    win_rate: 1.0
    alternates:
    - name: Erosion
      pick_rate: 0.14
      win_rate: 1.0
    - name: Engraved Guard
      pick_rate: 0.14
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.3
    win_rate: 0.5
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.5
  - name: Conduit Gem
    pick_rate: 0.1
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-09-09'
  god_win_rate: 0.65
  god_matches_won: 13
  god_matches_played: 20
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
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
    Shield, Breastplate of Valor, Eye of Providence, Draconic Scale, Shield of the
    Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire,
    Mantle Of Discord, Midgardian Mail, Hide of the Nemean Lion, Helm of Darkness,
    Leviathan''s Hide, Void Shield, Oni Hunter''s Garb, Xibalban Effigy, Spear of
    Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.79
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.76
      efficiency: 0.51
      win: 1.0
      pick: 0.43
      fit: 0.71
  community_ordered:
  - Breastplate of Valor
  - Erosion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Freya''s Tears, Rod of Asclepius, Shifter''s Shield, Breastplate of Valor, Soul
    Gem, Eye of Providence, Draconic Scale, Yogi''s Necklace, Gluttonous Grimoire,
    Phoenix Feather, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail,
    Stone of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide,
    Void Shield, Magi''s Cloak.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.77
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.75
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.57
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.76
      efficiency: 0.51
      win: 1.0
      pick: 0.43
      fit: 0.7
  community_ordered:
  - Erosion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Freya''s Tears, Spear of Desolation, Breastplate of Valor, Spear
    of the Magus, Soul Gem, Void Shield, Obsidian Shard, Shifter''s Shield, Void Stone,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle Of Discord, Midgardian
    Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Stone of Binding:
      total: 0.74
      efficiency: 0.51
      win: 1.0
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.73
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.75
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Breastplate
    of Valor, Freya''s Tears, Gluttonous Grimoire, Shifter''s Shield, Soul Gem, Helm
    of Radiance, Stone of Binding, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Magi''s Cloak, Daybreak Gavel, Spear of the Magus, Spear of Desolation,
    Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of
    The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.71
      efficiency: 0.65
      win: 1.0
      pick: 0.14
      fit: 0.2
    Kinetic Cuirass:
      total: 0.72
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.67
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.73
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
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
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Breastplate
    of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Soul Gem, Shifter''s Shield, Chronos'' Pendant, Helm of Radiance, Gluttonous Grimoire,
    Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Gem
    of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.76
      efficiency: 0.65
      win: 1.0
      pick: 0.14
      fit: 0.48
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.73
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.72
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.77
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.13
  community_ordered:
  - Breastplate of Valor
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
    Tears, Shifter''s Shield, Breastplate of Valor, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Hide of the Nemean Lion, Helm of
    Darkness, Leviathan''s Hide, Void Shield, Oni Hunter''s Garb, Xibalban Effigy,
    Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.14
      fit: 0.39
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.17
      fit: 0.39
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.79
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  starter: *id001
---
