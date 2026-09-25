---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.6
  slot_order:
  - name: Stampede
    pick_rate: 0.46
    win_rate: 0.54
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.08
      win_rate: 0.56
    - name: Mana Tome
      pick_rate: 0.06
      win_rate: 0.43
  - name: Genji's Guard
    pick_rate: 0.31
    win_rate: 0.54
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.33
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.42
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.56
  - name: Ethereal Staff
    pick_rate: 0.13
    win_rate: 0.86
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.62
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.46
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.5
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.75
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.75
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.25
    win_rate: 0.75
  - name: Bumba's Cudgel
    pick_rate: 0.24
    win_rate: 0.3
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-09-25'
  god_win_rate: 0.49122807017543857
  god_matches_won: 56
  god_matches_played: 114
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-25'
  god_matches_analyzed: 2996
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Shifter's Shield
  - Erosion
  flex_slots:
  - Erosion
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Freya''s Tears, Shield of
    the Phoenix, Prophetic Cloak, Stone of Binding, Magi''s Cloak, Helm of Radiance,
    Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle,
    Hide of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.42
      fit: 0.39
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.81
    Ethereal Staff:
      total: 0.62
      efficiency: 0.46
      win: 0.86
      pick: 0.22
      fit: 0.4
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Ethereal Staff
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Ethereal Staff
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Shifter''s Shield, Soul Gem, Erosion, Eye of Providence, Breastplate
    of Valor, Draconic Scale, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace,
    Chandra''s Grace, Freya''s Tears, Glorious Pridwen, Lifebinder, Midgardian Mail,
    Stone of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide,
    Void Shield, Magi''s Cloak, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.8
    Ethereal Staff:
      total: 0.67
      efficiency: 0.46
      win: 0.86
      pick: 0.22
      fit: 0.76
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Ethereal Staff
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Ethereal Staff
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Screeching Gargoyle
  - Spear of Desolation
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
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Spear of the Magus,
    Soul Gem, Void Shield, Breastplate of Valor, Obsidian Shard, Shifter''s Shield,
    Void Stone, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Doom Orb, Freya''s Tears, Helm of Radiance, The World Stone, Dreamer''s Idol,
    Magi''s Cloak, Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the
    Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.6
      efficiency: 0.46
      win: 0.86
      pick: 0.22
      fit: 0.3
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.59
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Ethereal Staff
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of Radiance,
    Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Freya''s Tears, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Spear
    of the Magus, Spear of Desolation, Bragi''s Harp, Rod of Asclepius, Midgardian
    Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard, Hide of the Nemean
    Lion, Leviathan''s Hide.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.59
      pick: 0.0
      fit: 0.44
    Ethereal Staff:
      total: 0.6
      efficiency: 0.46
      win: 0.86
      pick: 0.22
      fit: 0.25
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.59
      pick: 0.0
      fit: 0.08
  community_ordered:
  - Ethereal Staff
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Prophetic Cloak
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Freya''s Tears, Prophetic
    Cloak, Spear of Desolation, Screeching Gargoyle, Soul Gem, Shifter''s Shield,
    Chronos'' Pendant, Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of Providence,
    Gladiator''s Shield, Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak,
    Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious
    Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.54
      pick: 0.42
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.55
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.44
      win: 0.63
      pick: 0.1
      fit: 0.64
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.13
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Freya''s
    Tears, Shifter''s Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance,
    Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle,
    Prophetic Cloak, Hide of the Nemean Lion, Helm of Darkness, Leviathan''s Hide,
    Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation,
    Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.42
      fit: 0.39
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
