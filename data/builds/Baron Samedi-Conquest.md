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
    - name: Alchemist Coat
      pick_rate: 0.1
      win_rate: 0.56
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
    win_rate: 0.57
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.6
    - name: Prophetic Cloak
      pick_rate: 0.06
      win_rate: 0.61
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
  - name: Doublet of Binding
    pick_rate: 0.05
    win_rate: 0.71
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.7
    - name: Ethereal Staff
      pick_rate: 0.05
      win_rate: 0.47
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
    pick_rate: 0.21
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.53
  - name: Pendulum of the Ages
    pick_rate: 0.14
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-11-03'
  god_win_rate: 0.5605263157894737
  god_matches_won: 213
  god_matches_played: 380
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Spear of Desolation, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Obsidian Shard, Helm of Radiance, Helm of Darkness, Spear of the Magus,
    Erosion, Shield of the Phoenix, Eye of Providence, Lotus Sickle, Oni Hunter''s
    Garb, Draconic Scale, Jade Scepter, Doom Orb, Ancient Signet, Screeching Gargoyle,
    Stone of Binding, Midgardian Mail, The World Stone, Magi''s Cloak, Shifter''s
    Shield, Leviathan''s Hide, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.2
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.31
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.63
      win: 0.7
      pick: 0.15
      fit: 0.31
    Freya's Tears:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.25
      fit: 0.48
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.68
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
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
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
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
    Charm, Spear of Desolation, Gluttonous Grimoire, Obsidian Shard, Kinetic Cuirass,
    Soul Gem, Helm of Radiance, Lotus Sickle, Ancient Signet, Spear of the Magus,
    Death Metal, Helm of Darkness, Oni Hunter''s Garb, Doom Orb, The World Stone,
    Jade Scepter, Shield of the Phoenix, Erosion, Eye of Providence, Wish-Granting
    Pearl, Screeching Gargoyle, Midgardian Mail, Polynomicon, Stone of Binding, Triton''s
    Conch, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.28
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.63
      win: 0.7
      pick: 0.15
      fit: 0.28
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.6
      pick: 0.25
      fit: 0.33
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.68
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
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
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Spear of Desolation, Gluttonous Grimoire, Soul Gem, Obsidian
    Shard, Kinetic Cuirass, Spear of the Magus, Helm of Radiance, Helm of Darkness,
    Lotus Sickle, Doom Orb, Shield of the Phoenix, Oni Hunter''s Garb, The World Stone,
    Screeching Gargoyle, Ancient Signet, Erosion, Death Metal, Eye of Providence,
    Dreamer''s Idol, Midgardian Mail, Jade Scepter, Stone of Binding, Draconic Scale,
    Magi''s Cloak, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.14
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.27
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.63
      win: 0.7
      pick: 0.15
      fit: 0.27
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.68
      pick: 0.17
      fit: 0.35
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Book of Thoth
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
    Spear of Desolation, Kinetic Cuirass, Obsidian Shard, Blood-Bound Book, Phoenix
    Feather, Rod of Asclepius, Yogi''s Necklace, Helm of Radiance, Sphere of Negation,
    Spear of the Magus, Helm of Darkness, Chandra''s Grace, Oni Hunter''s Garb, Erosion,
    Eye of Providence, Lotus Sickle, Jade Scepter, Regrowth Striders, Draconic Scale,
    Midgardian Mail, Glorious Pridwen, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.2
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.63
      win: 0.7
      pick: 0.15
      fit: 0.29
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.25
      fit: 0.44
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.68
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.58
      efficiency: 0.53
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
  - Book of Thoth
  - Breastplate of Valor
  - Gluttonous Grimoire
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of Desolation, Gluttonous Grimoire, Obsidian Shard, Amanita
    Charm, Soul Gem, Screeching Gargoyle, Stone of Binding, Spear of the Magus, Kinetic
    Cuirass, Void Stone, Void Shield, Doom Orb, The World Stone, Helm of Radiance,
    Helm of Darkness, Dreamer''s Idol, Lotus Sickle, Oni Hunter''s Garb, Shield of
    the Phoenix, Erosion, Eye of Providence, Ancient Signet, Draconic Scale, Jade
    Scepter, Midgardian Mail, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.17
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.63
      win: 0.7
      pick: 0.15
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.59
    Obsidian Shard:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.68
      pick: 0.17
      fit: 0.48
  community_ordered:
  - Breastplate of Valor
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
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Kinetic Cuirass,
    Spear of Desolation, Obsidian Shard, Helm of Radiance, Eros'' Bow, Spear of the
    Magus, Blood-Bound Book, Ancient Signet, Helm of Darkness, Oni Hunter''s Garb,
    Lotus Sickle, Bragi''s Harp, Bracer of The Abyss, Shield of the Phoenix, Screeching
    Gargoyle, Jade Scepter, Death Metal, Midgardian Mail, Erosion, Stone of Binding,
    Doom Orb, Chronos'' Pendant.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.7
      pick: 0.15
      fit: 0.18
    Nimble Ring:
      total: 0.53
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.49
      efficiency: 0.45
      win: 0.58
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.68
      pick: 0.17
      fit: 0.22
    Eros' Bow:
      total: 0.5
      efficiency: 0.53
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
    Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Lotus Sickle,
    Gluttonous Grimoire, Obsidian Shard, Helm of Radiance, Oni Hunter''s Garb, Erosion,
    Spear of the Magus, Helm of Darkness, Eye of Providence, Gem of Focus, Gladiator''s
    Shield, Heartwood Charm, Draconic Scale, Midgardian Mail, Stone of Binding, Magi''s
    Cloak, Leviathan''s Hide, Ancient Signet, Chronos'' Pendant, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.43
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.63
      win: 0.7
      pick: 0.15
      fit: 0.43
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.6
      pick: 0.25
      fit: 0.56
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.68
      pick: 0.17
      fit: 0.23
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
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
  - Kinetic Cuirass
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
    Underrated for this god: Amanita Charm, Spear of Desolation, Kinetic Cuirass,
    Gluttonous Grimoire, Soul Gem, Obsidian Shard, Helm of Radiance, Helm of Darkness,
    Spear of the Magus, Erosion, Shield of the Phoenix, Eye of Providence, Lotus Sickle,
    Oni Hunter''s Garb, Draconic Scale, Jade Scepter, Chronos'' Pendant, Doom Orb,
    Ancient Signet, Screeching Gargoyle, Stone of Binding, Midgardian Mail, The World
    Stone, Magi''s Cloak, Shifter''s Shield, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.51
    Obsidian Shard:
      total: 0.54
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.68
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  starter: *id001
---
