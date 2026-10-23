---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.29
  slot_order:
  - name: Stampede
    pick_rate: 0.22
    win_rate: 0.32
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.17
      win_rate: 0.47
    - name: Mana Tome
      pick_rate: 0.12
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.21
    alternates:
    - name: Stampede
      pick_rate: 0.21
      win_rate: 0.52
    - name: Bragi's Harp
      pick_rate: 0.07
      win_rate: 0.14
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.38
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.14
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.5
    - name: Ancile
      pick_rate: 0.07
      win_rate: 0.67
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.4
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.46
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.5
  - name: Ethereal Staff
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Flaming Pearl
      pick_rate: 0.06
      win_rate: 0.33
    - name: Hussar's Wings
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.25
    win_rate: 0.56
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.46
  - name: Bluestone Pendant
    pick_rate: 0.14
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-10-23'
  god_win_rate: 0.43434343434343436
  god_matches_won: 43
  god_matches_played: 99
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-23'
  god_matches_analyzed: 2743
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Ancile
  - Ethereal Staff
  - Freya's Tears
  - Shifter's Shield
  - Hussar's Wings
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
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
    this god: Ancile, Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield,
    Draconic Scale, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Helm of Darkness,
    Leviathan''s Hide, Void Shield, Oni Hunter''s Garb, Xibalban Effigy, Spear of
    Desolation, Breastplate of Valor.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.4
      pick: 0.0
      fit: 0.81
    Ancile:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.12
      fit: 0.46
    Ethereal Staff:
      total: 0.54
      efficiency: 0.46
      win: 0.67
      pick: 0.4
      fit: 0.4
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.27
      fit: 0.64
    Shifter's Shield:
      total: 0.48
      efficiency: 0.55
      win: 0.4
      pick: 0.0
      fit: 0.71
    Hussar's Wings:
      total: 0.55
      efficiency: 0.39
      win: 0.67
      pick: 0.18
      fit: 0.71
  community_ordered:
  - Ancile
  - Ethereal Staff
  - Freya's Tears
  - Hussar's Wings
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Ancile
  - Ethereal Staff
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
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
    this god: Amanita Charm, Ancile, Shield of the Phoenix, Rod of Tahuti, Kinetic
    Cuirass, Rod of Asclepius, Shifter''s Shield, Soul Gem, Draconic Scale, Erosion,
    Eye of Providence, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace, Chandra''s
    Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding, Helm of
    Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s Cloak,
    Breastplate of Valor.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.4
      pick: 0.0
      fit: 0.8
    Ancile:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.12
      fit: 0.48
    Ethereal Staff:
      total: 0.6
      efficiency: 0.46
      win: 0.67
      pick: 0.4
      fit: 0.76
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.27
      fit: 0.57
    Hussar's Wings:
      total: 0.55
      efficiency: 0.39
      win: 0.67
      pick: 0.18
      fit: 0.7
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Ancile
  - Ethereal Staff
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Ancile
  - Ethereal Staff
  - Freya's Tears
  - Rod of Tahuti
  - Hussar's Wings
  flex_slots:
  - Freya's Tears
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Spear of the Magus,
    Soul Gem, Void Shield, Obsidian Shard, Shifter''s Shield, Void Stone, Draconic
    Scale, Erosion, Eye of Providence, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle Of Discord, Midgardian
    Mail, Rod of Asclepius, Hide of the Nemean Lion, Breastplate of Valor.'
  slot_scores:
    Stone of Binding:
      total: 0.47
      efficiency: 0.51
      win: 0.4
      pick: 0.0
      fit: 0.75
    Ancile:
      total: 0.53
      efficiency: 0.51
      win: 0.67
      pick: 0.12
      fit: 0.32
    Ethereal Staff:
      total: 0.53
      efficiency: 0.46
      win: 0.67
      pick: 0.4
      fit: 0.3
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.27
      fit: 0.44
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.4
      pick: 0.0
      fit: 0.41
    Hussar's Wings:
      total: 0.52
      efficiency: 0.39
      win: 0.67
      pick: 0.18
      fit: 0.49
  community_ordered:
  - Ancile
  - Ethereal Staff
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Ancile
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Ethereal Staff
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Shifter''s Shield, Soul Gem, Draconic Scale, Helm of Radiance, Erosion,
    Stone of Binding, Eye of Providence, Shield of the Phoenix, Magi''s Cloak, Screeching
    Gargoyle, Daybreak Gavel, Spear of the Magus, Spear of Desolation, Rod of Asclepius,
    Midgardian Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard, Hide
    of the Nemean Lion, Leviathan''s Hide, Breastplate of Valor, Bragi''s Harp.'
  slot_scores:
    Ancile:
      total: 0.52
      efficiency: 0.51
      win: 0.67
      pick: 0.12
      fit: 0.23
    Bracer of The Abyss:
      total: 0.4
      efficiency: 0.52
      win: 0.4
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.45
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.29
      efficiency: 0.44
      win: 0.14
      pick: 0.1
      fit: 0.44
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.27
      fit: 0.33
    Ethereal Staff:
      total: 0.52
      efficiency: 0.46
      win: 0.67
      pick: 0.4
      fit: 0.25
  community_ordered:
  - Ancile
  - Bragi's Harp
  - Freya's Tears
  - Ethereal Staff
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Ancile
  - Freya's Tears
  - Spear of Desolation
  - Hussar's Wings
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching Gargoyle, Soul
    Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Draconic Scale, Erosion,
    Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus,
    Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak
    Gavel, Breastplate of Valor.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.56
      win: 0.4
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.46
      efficiency: 0.53
      win: 0.4
      pick: 0.0
      fit: 0.61
    Ancile:
      total: 0.53
      efficiency: 0.51
      win: 0.67
      pick: 0.12
      fit: 0.29
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.27
      fit: 0.64
    Spear of Desolation:
      total: 0.45
      efficiency: 0.57
      win: 0.4
      pick: 0.0
      fit: 0.46
    Hussar's Wings:
      total: 0.51
      efficiency: 0.39
      win: 0.67
      pick: 0.18
      fit: 0.45
  community_ordered:
  - Ancile
  - Freya's Tears
  - Hussar's Wings
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak,
    Hide of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation.'
  slot_scores:
    Genji's Guard:
      total: 0.39
      efficiency: 0.66
      win: 0.21
      pick: 0.19
      fit: 0.39
    Breastplate of Valor:
      total: 0.36
      efficiency: 0.65
      win: 0.14
      pick: 0.11
      fit: 0.39
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.4
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.27
      fit: 0.64
    Shifter's Shield:
      total: 0.48
      efficiency: 0.55
      win: 0.4
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
---
