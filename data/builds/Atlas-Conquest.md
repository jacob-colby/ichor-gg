---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.58
  slot_order:
  - name: Stampede
    pick_rate: 0.24
    win_rate: 0.48
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.5
    - name: Yogi's Necklace
      pick_rate: 0.09
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.52
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.47
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.43
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.39
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.33
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.61
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.11
      win_rate: 0.33
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.64
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.43
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.61
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.29
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.83
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.4
    - name: Spear of the Magus
      pick_rate: 0.06
      win_rate: 0.8
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.41
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.73
  - name: Bumba's Cudgel
    pick_rate: 0.16
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-09-13'
  god_win_rate: 0.5174418604651163
  god_matches_won: 89
  god_matches_played: 172
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-13'
  god_matches_analyzed: 5560
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Spear of the Magus
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Breastplate
    of Valor, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Helm of Darkness, Leviathan''s
    Hide, Void Shield, Ancile, Draconic Scale, Oni Hunter''s Garb, Xibalban Effigy,
    Spear of Desolation, Hussar''s Wings, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.52
      pick: 0.26
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.54
      pick: 0.22
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.71
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.8
      pick: 0.18
      fit: 0.15
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of the Magus
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Spear of the Magus
  - Rod of Tahuti
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
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Shifter''s Shield, Soul Gem, Erosion, Eye of Providence, Breastplate
    of Valor, Yogi''s Necklace, Gluttonous Grimoire, Phoenix Feather, Chandra''s Grace,
    Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding, Helm of Radiance,
    Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s Cloak, Ancile,
    Draconic Scale.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.22
      fit: 0.57
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.8
      pick: 0.18
      fit: 0.16
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.52
      pick: 0.0
      fit: 0.16
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Freya's Tears
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of the Magus
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Soul Gem, Void Shield,
    Breastplate of Valor, Obsidian Shard, Shifter''s Shield, Void Stone, Erosion,
    Eye of Providence, Shield of the Phoenix, Doom Orb, Helm of Radiance, The World
    Stone, Dreamer''s Idol, Magi''s Cloak, Mantle Of Discord, Midgardian Mail, Rod
    of Asclepius, Hide of the Nemean Lion, Draconic Scale.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.22
      fit: 0.44
    Spear of the Magus:
      total: 0.64
      efficiency: 0.6
      win: 0.8
      pick: 0.18
      fit: 0.41
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.52
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Freya's Tears
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Spear of the Magus
  - Rod of Tahuti
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
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of Radiance,
    Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix, Magi''s Cloak,
    Screeching Gargoyle, Daybreak Gavel, Spear of Desolation, Bragi''s Harp, Rod of
    Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard,
    Hide of the Nemean Lion, Leviathan''s Hide, Draconic Scale.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.52
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.54
      pick: 0.22
      fit: 0.33
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.8
      pick: 0.18
      fit: 0.08
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.52
      pick: 0.0
      fit: 0.08
  community_ordered:
  - Freya's Tears
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of the Magus
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant, Erosion, Helm of Radiance,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Stone of Binding,
    Gem of Focus, Prophetic Cloak, Magi''s Cloak, Rod of Asclepius, Eye of Erebus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Draconic
    Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.52
      pick: 0.26
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.22
      fit: 0.64
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.8
      pick: 0.18
      fit: 0.13
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.52
      pick: 0.0
      fit: 0.13
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of the Magus
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
    Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.52
      pick: 0.26
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.54
      pick: 0.22
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
