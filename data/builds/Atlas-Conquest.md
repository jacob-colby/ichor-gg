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
  god_matches_analyzed: 14484
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
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Erosion, Eye of Providence,
    Draconic Scale, Breastplate of Valor, Helm of Darkness, Shield of the Phoenix,
    Shifter''s Shield, Oni Hunter''s Garb, Stone of Binding, Magi''s Cloak, Midgardian
    Mail, Helm of Radiance, Mantle Of Discord, Gluttonous Grimoire, Screeching Gargoyle,
    Leviathan''s Hide, Prophetic Cloak, Spear of Desolation, Ancile, Hide of the Nemean
    Lion, Void Stone, Void Shield, Soul Gem, Xibalban Effigy.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.41
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.64
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.49
      efficiency: 0.51
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
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Phoenix Feather, Erosion, Eye of Providence, Ethereal Staff, Draconic
    Scale, Yogi''s Necklace, Breastplate of Valor, Oni Hunter''s Garb, Chandra''s
    Grace, Shifter''s Shield, Gluttonous Grimoire, Midgardian Mail, Glorious Pridwen,
    Helm of Darkness, Rod of Asclepius, Regrowth Striders, Helm of Radiance, Stone
    of Binding, Leviathan''s Hide, Sphere of Negation, Spear of Desolation, Ancile,
    Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.41
      pick: 0.16
      fit: 0.36
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.52
      win: 0.44
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.52
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.57
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.48
      efficiency: 0.51
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
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
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
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Spear of Desolation, Obsidian Shard, Screeching Gargoyle, Soul
    Gem, Void Stone, Void Shield, Spear of the Magus, Breastplate of Valor, Erosion,
    Eye of Providence, Doom Orb, Oni Hunter''s Garb, Draconic Scale, The World Stone,
    Helm of Radiance, Helm of Darkness, Shield of the Phoenix, Midgardian Mail, Magi''s
    Cloak, Dreamer''s Idol, Shifter''s Shield, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Stone of Binding:
      total: 0.49
      efficiency: 0.5
      win: 0.44
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.5
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.44
    Spear of Desolation:
      total: 0.48
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.87
      win: 0.44
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
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
    Grimoire, Breastplate of Valor, Soul Gem, Helm of Radiance, Eros'' Bow, Oni Hunter''s
    Garb, Erosion, Eye of Providence, Obsidian Shard, Stone of Binding, Spear of Desolation,
    Helm of Darkness, Midgardian Mail, Draconic Scale, Shield of the Phoenix, Magi''s
    Cloak, Screeching Gargoyle, Blood-Bound Book, Bragi''s Harp, Mantle Of Discord,
    Shifter''s Shield, Bracer of The Abyss, Lotus Sickle, Leviathan''s Hide.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.47
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.42
      efficiency: 0.45
      win: 0.44
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.48
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.33
    Eros' Bow:
      total: 0.44
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Breastplate
    of Valor, Kinetic Cuirass, Spear of Desolation, Shield of the Phoenix, Screeching
    Gargoyle, Soul Gem, Lotus Sickle, Chronos'' Pendant, Prophetic Cloak, Helm of
    Radiance, Erosion, Helm of Darkness, Eye of Providence, Oni Hunter''s Garb, Gluttonous
    Grimoire, Gladiator''s Shield, Draconic Scale, Gem of Focus, Stone of Binding,
    Obsidian Shard, Heartwood Charm, Midgardian Mail, Magi''s Cloak, Mantle Of Discord,
    Shifter''s Shield, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.41
      pick: 0.16
      fit: 0.48
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.64
    Spear of Desolation:
      total: 0.48
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Erosion,
    Eye of Providence, Draconic Scale, Breastplate of Valor, Helm of Darkness, Shield
    of the Phoenix, Shifter''s Shield, Oni Hunter''s Garb, Stone of Binding, Magi''s
    Cloak, Midgardian Mail, Helm of Radiance, Mantle Of Discord, Gluttonous Grimoire,
    Leviathan''s Hide, Screeching Gargoyle, Prophetic Cloak, Spear of Desolation,
    Ancile, Hide of the Nemean Lion, Void Stone, Void Shield, Soul Gem, Xibalban Effigy.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.41
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.64
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.49
      efficiency: 0.51
      win: 0.44
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
