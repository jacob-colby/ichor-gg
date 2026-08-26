---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.67
  slot_order:
  - name: Stampede
    pick_rate: 0.29
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.17
    - name: Yogi's Necklace
      pick_rate: 0.1
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.57
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.17
      win_rate: 0.43
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.14
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.22
    - name: Ethereal Staff
      pick_rate: 0.1
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.22
    win_rate: 0.38
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.67
    - name: Sphere of Negation
      pick_rate: 0.08
      win_rate: 0.0
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.25
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.21
      win_rate: 0.33
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.5
  - name: Ancile
    pick_rate: 0.19
    win_rate: 0.0
    alternates:
    - name: Plated Metal
      pick_rate: 0.06
      win_rate: 1.0
    - name: Sphere of Negation
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.22
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-08-26'
  god_win_rate: 0.4634146341463415
  god_matches_won: 19
  god_matches_played: 41
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Sphere of Negation
  - Erosion
  flex_slots:
  - Erosion
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Erosion, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak,
    Hide of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Oni
    Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings, Shifter''s
    Shield.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.15
      fit: 0.81
    Sphere of Negation:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.35
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Sphere of Negation
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Rod of Asclepius,
    Soul Gem, Erosion, Eye of Providence, Draconic Scale, Yogi''s Necklace, Gluttonous
    Grimoire, Phoenix Feather, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian
    Mail, Stone of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.36
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.15
      fit: 0.8
    Sphere of Negation:
      total: 0.71
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.61
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Sphere of Negation
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Screeching Gargoyle, Spear of Desolation, Spear of the Magus, Soul Gem, Void Shield,
    Obsidian Shard, Void Stone, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Doom Orb, Helm of Radiance, The World Stone, Dreamer''s Idol,
    Magi''s Cloak, Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the
    Nemean Lion, Shifter''s Shield.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.15
      fit: 0.59
    Sphere of Negation:
      total: 0.65
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.24
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Sphere of Negation
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Gluttonous Grimoire, Soul
    Gem, Helm of Radiance, Erosion, Stone of Binding, Eye of Providence, Shield of
    the Phoenix, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel,
    Spear of the Magus, Spear of Desolation, Bragi''s Harp, Rod of Asclepius, Midgardian
    Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard, Hide of the Nemean
    Lion, Leviathan''s Hide, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.2
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Sphere of Negation:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.18
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.08
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Shield of the Phoenix
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Shield
    of the Phoenix, Spear of Desolation, Screeching Gargoyle, Soul Gem, Chronos''
    Pendant, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous Grimoire, Eye
    of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Gem of Focus,
    Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of
    Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.15
      fit: 0.55
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.13
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Shifter''s Shield, Erosion,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Magi''s
    Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail,
    Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Helm of Darkness,
    Leviathan''s Hide, Void Shield, Oni Hunter''s Garb, Xibalban Effigy, Spear of
    Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.23
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.15
      fit: 0.81
    Freya's Tears:
      total: 0.44
      efficiency: 0.61
      win: 0.25
      pick: 0.3
      fit: 0.64
    Shifter's Shield:
      total: 0.38
      efficiency: 0.55
      win: 0.17
      pick: 0.15
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
---
