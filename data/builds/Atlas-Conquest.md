---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.33
  slot_order:
  - name: Stampede
    pick_rate: 0.23
    win_rate: 0.42
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.18
      win_rate: 0.53
    - name: Leviathan's Hide
      pick_rate: 0.11
      win_rate: 0.42
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.41
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.47
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.38
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.46
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.43
  - name: Sage's Ring
    pick_rate: 0.04
    win_rate: 0.25
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.48
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.59
    alternates:
    - name: Sage's Ring
      pick_rate: 0.04
      win_rate: 0.45
    - name: Shell of Rebuke
      pick_rate: 0.03
      win_rate: 0.38
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.54
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.47
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-11-02'
  god_win_rate: 0.445916114790287
  god_matches_won: 202
  god_matches_played: 453
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Erosion, Eye of Providence,
    Draconic Scale, Breastplate of Valor, Shifter''s Shield, Shield of the Phoenix,
    Helm of Darkness, Oni Hunter''s Garb, Stone of Binding, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Gluttonous Grimoire, Helm of Radiance, Screeching Gargoyle,
    Prophetic Cloak, Leviathan''s Hide, Ancile, Spear of Desolation, Hide of the Nemean
    Lion, Void Stone, Xibalban Effigy, Void Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.58
      win: 0.44
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.41
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.52
      efficiency: 0.55
      win: 0.48
      pick: 0.25
      fit: 0.64
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.44
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.48
      efficiency: 0.48
      win: 0.44
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Genji's Guard
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Soul Gem, Phoenix Feather, Erosion, Eye of Providence, Draconic Scale, Ethereal
    Staff, Yogi''s Necklace, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s
    Garb, Shifter''s Shield, Gluttonous Grimoire, Glorious Pridwen, Midgardian Mail,
    Helm of Darkness, Rod of Asclepius, Regrowth Striders, Stone of Binding, Leviathan''s
    Hide, Ancile, Sphere of Negation, Hide of the Nemean Lion, Magi''s Cloak, Helm
    of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.41
      pick: 0.16
      fit: 0.36
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.49
      win: 0.44
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.51
      efficiency: 0.55
      win: 0.48
      pick: 0.25
      fit: 0.57
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.44
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.47
      efficiency: 0.48
      win: 0.44
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Kinetic Cuirass, Screeching Gargoyle, Obsidian Shard, Spear of Desolation, Soul
    Gem, Void Stone, Void Shield, Breastplate of Valor, Spear of the Magus, Erosion,
    Doom Orb, Eye of Providence, Draconic Scale, The World Stone, Oni Hunter''s Garb,
    Shield of the Phoenix, Helm of Darkness, Midgardian Mail, Helm of Radiance, Shifter''s
    Shield, Magi''s Cloak, Mantle Of Discord, Dreamer''s Idol, Leviathan''s Hide.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.47
      efficiency: 0.49
      win: 0.44
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.48
      efficiency: 0.47
      win: 0.44
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.49
      efficiency: 0.55
      win: 0.48
      pick: 0.25
      fit: 0.44
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.81
      win: 0.44
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.49
      efficiency: 0.62
      win: 0.44
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Eros' Bow
  - Amanita Charm
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Eros'' Bow, Oni Hunter''s Garb, Erosion,
    Obsidian Shard, Helm of Radiance, Eye of Providence, Stone of Binding, Draconic
    Scale, Shield of the Phoenix, Midgardian Mail, Spear of Desolation, Screeching
    Gargoyle, Sundering Echo, Helm of Darkness, Magi''s Cloak, Mantle Of Discord,
    Blood-Bound Book, Shifter''s Shield, Bragi''s Harp, Leviathan''s Hide, Bracer
    of The Abyss.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.46
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.41
      efficiency: 0.41
      win: 0.44
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.47
      efficiency: 0.55
      win: 0.48
      pick: 0.25
      fit: 0.33
    Eros' Bow:
      total: 0.42
      efficiency: 0.49
      win: 0.44
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.47
      efficiency: 0.62
      win: 0.44
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Chronos'' Pendant, Prophetic Cloak, Erosion, Gladiator''s
    Shield, Gluttonous Grimoire, Eye of Providence, Helm of Radiance, Helm of Darkness,
    Oni Hunter''s Garb, Draconic Scale, Obsidian Shard, Stone of Binding, Heartwood
    Charm, Gem of Focus, Chandra''s Grace, Midgardian Mail, Magi''s Cloak, Sundering
    Echo, Shifter''s Shield, Glorious Pridwen.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.41
      pick: 0.16
      fit: 0.48
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.52
      efficiency: 0.55
      win: 0.48
      pick: 0.25
      fit: 0.64
    Spear of Desolation:
      total: 0.46
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.48
      efficiency: 0.62
      win: 0.44
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Erosion,
    Eye of Providence, Draconic Scale, Breastplate of Valor, Shifter''s Shield, Shield
    of the Phoenix, Helm of Darkness, Oni Hunter''s Garb, Stone of Binding, Magi''s
    Cloak, Midgardian Mail, Mantle Of Discord, Gluttonous Grimoire, Leviathan''s Hide,
    Helm of Radiance, Screeching Gargoyle, Prophetic Cloak, Ancile, Spear of Desolation,
    Hide of the Nemean Lion, Void Stone, Xibalban Effigy, Void Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.58
      win: 0.44
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.41
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.52
      efficiency: 0.55
      win: 0.48
      pick: 0.25
      fit: 0.64
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.44
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.48
      efficiency: 0.48
      win: 0.44
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
