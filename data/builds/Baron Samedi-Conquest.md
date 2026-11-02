---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.66
  aspect_win_rate: 0.57
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.51
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.58
  - name: Breastplate of Valor
    pick_rate: 0.11
    win_rate: 0.7
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.46
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.63
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.6
    - name: Prophetic Cloak
      pick_rate: 0.05
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.6
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.68
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.48
  - name: Ethereal Staff
    pick_rate: 0.05
    win_rate: 0.47
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.7
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.5
  - name: Sage's Ring
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.73
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.2
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.54
  - name: Pendulum of the Ages
    pick_rate: 0.14
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-11-02'
  god_win_rate: 0.56
  god_matches_won: 210
  god_matches_played: 375
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Helm of Darkness — physical protection
    swap_item: Helm of Darkness
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Spear of Desolation,
    Soul Gem, Obsidian Shard, Helm of Darkness, Helm of Radiance, Spear of the Magus,
    Shield of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Oni Hunter''s
    Garb, Doom Orb, Screeching Gargoyle, The World Stone, Stone of Binding, Midgardian
    Mail, Jade Scepter, Shifter''s Shield, Magi''s Cloak, Leviathan''s Hide, Mantle
    Of Discord, Chronos'' Pendant, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.2
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.19
      fit: 0.31
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.61
      win: 0.7
      pick: 0.15
      fit: 0.31
    Freya's Tears:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.25
      fit: 0.48
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.81
      win: 0.68
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Gluttonous Grimoire, Obsidian Shard, Spear of Desolation, Kinetic Cuirass,
    Sundering Echo, Soul Gem, Helm of Radiance, Spear of the Magus, Doom Orb, Helm
    of Darkness, Oni Hunter''s Garb, The World Stone, Death Metal, Shield of the Phoenix,
    Erosion, Jade Scepter, Screeching Gargoyle, Wish-Granting Pearl, Heartwood Charm,
    Eye of Providence, Ancient Signet, Stone of Binding, Midgardian Mail, Draconic
    Scale, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.19
      fit: 0.28
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.61
      win: 0.7
      pick: 0.15
      fit: 0.28
    Freya's Tears:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.25
      fit: 0.33
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.41
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.81
      win: 0.68
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Spear of Desolation, Gluttonous Grimoire, Soul Gem, Obsidian
    Shard, Kinetic Cuirass, Spear of the Magus, Sundering Echo, Helm of Radiance,
    Doom Orb, Shield of the Phoenix, Helm of Darkness, The World Stone, Screeching
    Gargoyle, Oni Hunter''s Garb, Erosion, Eye of Providence, Draconic Scale, Stone
    of Binding, Midgardian Mail, Death Metal, Dreamer''s Idol, Magi''s Cloak, Jade
    Scepter, Leviathan''s Hide, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.19
      fit: 0.27
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.61
      win: 0.7
      pick: 0.15
      fit: 0.27
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.25
      fit: 0.39
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.81
      win: 0.68
      pick: 0.17
      fit: 0.35
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Spear of Desolation, Obsidian Shard, Phoenix Feather, Yogi''s
    Necklace, Chandra''s Grace, Blood-Bound Book, Rod of Asclepius, Sphere of Negation,
    Helm of Radiance, Spear of the Magus, Helm of Darkness, Erosion, Oni Hunter''s
    Garb, Eye of Providence, Draconic Scale, Glorious Pridwen, Regrowth Striders,
    Doom Orb, Jade Scepter, Midgardian Mail, Ethereal Staff.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.61
      win: 0.7
      pick: 0.15
      fit: 0.29
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.25
      fit: 0.44
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.81
      win: 0.68
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.6
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.57
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Gluttonous Grimoire
  - Freya's Tears
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  flex_slots:
  - Obsidian Shard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, Soul Gem,
    Amanita Charm, Screeching Gargoyle, Stone of Binding, Kinetic Cuirass, Spear of
    the Magus, Void Stone, Void Shield, Doom Orb, The World Stone, Helm of Radiance,
    Helm of Darkness, Dreamer''s Idol, Shield of the Phoenix, Erosion, Oni Hunter''s
    Garb, Eye of Providence, Draconic Scale, The Cosmic Horror, Midgardian Mail, Jade
    Scepter, Magi''s Cloak, Chronos'' Pendant.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.61
      win: 0.7
      pick: 0.15
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.25
      fit: 0.4
    Spear of Desolation:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.59
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.81
      win: 0.68
      pick: 0.17
      fit: 0.48
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Eros' Bow
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Soul Gem, Amanita Charm, Kinetic Cuirass,
    Obsidian Shard, Spear of Desolation, Eros'' Bow, Helm of Radiance, Sundering Echo,
    Spear of the Magus, Blood-Bound Book, Oni Hunter''s Garb, Helm of Darkness, Screeching
    Gargoyle, Shield of the Phoenix, Bragi''s Harp, Bracer of The Abyss, Erosion,
    Doom Orb, Midgardian Mail, Stone of Binding, The World Stone, Eye of Providence,
    Draconic Scale, Chronos'' Pendant.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.61
      win: 0.7
      pick: 0.15
      fit: 0.18
    Nimble Ring:
      total: 0.53
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.48
      efficiency: 0.41
      win: 0.58
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.81
      win: 0.68
      pick: 0.17
      fit: 0.22
    Eros' Bow:
      total: 0.49
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Breastplate of Valor
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Spear of Desolation,
    Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Gluttonous
    Grimoire, Obsidian Shard, Helm of Radiance, Oni Hunter''s Garb, Erosion, Gladiator''s
    Shield, Heartwood Charm, Gem of Focus, Helm of Darkness, Eye of Providence, Spear
    of the Magus, Draconic Scale, Chandra''s Grace, Stone of Binding, Sundering Echo,
    Midgardian Mail, Magi''s Cloak, Leviathan''s Hide, Chronos'' Pendant, Prophetic
    Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.19
      fit: 0.43
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.15
      fit: 0.43
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.25
      fit: 0.56
    Spear of Desolation:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.81
      win: 0.68
      pick: 0.17
      fit: 0.23
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Soul Gem, Obsidian Shard, Helm of Darkness, Helm of Radiance,
    Spear of the Magus, Shield of the Phoenix, Erosion, Eye of Providence, Draconic
    Scale, Oni Hunter''s Garb, Doom Orb, Screeching Gargoyle, Chronos'' Pendant, The
    World Stone, Stone of Binding, Midgardian Mail, Jade Scepter, Shifter''s Shield,
    Magi''s Cloak, Leviathan''s Hide, Mantle Of Discord, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.51
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.81
      win: 0.68
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  starter: *id001
---
