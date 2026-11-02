---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.67
  aspect_win_rate: 0.59
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.56
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.5
  - name: Stampede
    pick_rate: 0.1
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.48
    - name: Spear of Desolation
      pick_rate: 0.05
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.65
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.53
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.65
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.05
      win_rate: 0.7
    - name: Obsidian Shard
      pick_rate: 0.04
      win_rate: 0.56
  - name: Sage's Ring
    pick_rate: 0.07
    win_rate: 0.4
    alternates:
    - name: Oracle Staff
      pick_rate: 0.05
      win_rate: 0.71
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.52
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.62
  - name: Pendulum of the Ages
    pick_rate: 0.14
    win_rate: 0.66
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-10-30'
  god_win_rate: 0.5521235521235521
  god_matches_won: 143
  god_matches_played: 259
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Spear of the Magus
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of Desolation, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Soul Gem, Spear of the Magus, Breastplate of Valor, Shifter''s Shield, Helm of
    Radiance, Shield of the Phoenix, Erosion, Lotus Sickle, Rod of Asclepius, Eye
    of Providence, Draconic Scale, Obsidian Shard, Jade Scepter, Stone of Binding,
    Doom Orb, Helm of Darkness, Wish-Granting Pearl, The World Stone, Screeching Gargoyle,
    Magi''s Cloak, Dreamer''s Idol, Chronos'' Pendant.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.58
      efficiency: 0.58
      win: 0.67
      pick: 0.08
      fit: 0.51
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.65
      pick: 0.19
      fit: 0.48
    Spear of the Magus:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.65
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Spear of Desolation
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
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of Desolation, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Breastplate
    of Valor, Spear of the Magus, Soul Gem, Helm of Radiance, Lotus Sickle, Shifter''s
    Shield, Rod of Asclepius, Doom Orb, Wish-Granting Pearl, The World Stone, Obsidian
    Shard, Jade Scepter, Death Metal, Ancient Signet, Shield of the Phoenix, Erosion,
    Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Triton''s
    Conch, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.19
      fit: 0.28
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.58
      pick: 0.1
      fit: 0.28
    Spear of Desolation:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.08
      fit: 0.4
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.65
      pick: 0.19
      fit: 0.33
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.65
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Spear of the Magus
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Spear of Desolation, Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic
    Cuirass, Spear of the Magus, Breastplate of Valor, Helm of Radiance, Shifter''s
    Shield, Lotus Sickle, Obsidian Shard, Shield of the Phoenix, Doom Orb, Rod of
    Asclepius, Erosion, The World Stone, Eye of Providence, Screeching Gargoyle, Dreamer''s
    Idol, Draconic Scale, Jade Scepter, Stone of Binding, Daybreak Gavel, Wish-Granting
    Pearl, Magi''s Cloak, Chronos'' Pendant.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.58
      efficiency: 0.58
      win: 0.67
      pick: 0.08
      fit: 0.49
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.65
      pick: 0.19
      fit: 0.39
    Spear of the Magus:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.85
      win: 0.65
      pick: 0.22
      fit: 0.35
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Ethereal Staff, Soul Gem, Spear of Desolation, Shield
    of the Phoenix, Rod of Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Spear
    of the Magus, Shifter''s Shield, Lifebinder, Breastplate of Valor, Helm of Radiance,
    Yogi''s Necklace, Sphere of Negation, Erosion, Chandra''s Grace, Lotus Sickle,
    Eye of Providence, Jade Scepter, Phoenix Feather, Draconic Scale, Obsidian Shard,
    Blood-Bound Book, Wish-Granting Pearl, Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.6
      efficiency: 0.47
      win: 0.7
      pick: 0.11
      fit: 0.79
    Spear of Desolation:
      total: 0.58
      efficiency: 0.58
      win: 0.67
      pick: 0.08
      fit: 0.51
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.65
      pick: 0.19
      fit: 0.44
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.65
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Ethereal Staff
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Gluttonous Grimoire
  - Freya's Tears
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Spear of the Magus
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
    for this god: Spear of Desolation, Gluttonous Grimoire, Amanita Charm, Soul Gem,
    Spear of the Magus, Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Void
    Shield, Obsidian Shard, Void Stone, Breastplate of Valor, Doom Orb, Helm of Radiance,
    The World Stone, Shifter''s Shield, Dreamer''s Idol, Lotus Sickle, Shield of the
    Phoenix, Rod of Asclepius, Erosion, Eye of Providence, Draconic Scale, Jade Scepter,
    Wish-Granting Pearl, Chronos'' Pendant.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.68
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.65
      pick: 0.19
      fit: 0.4
    Spear of Desolation:
      total: 0.6
      efficiency: 0.58
      win: 0.67
      pick: 0.08
      fit: 0.59
    Spear of the Magus:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.85
      win: 0.65
      pick: 0.22
      fit: 0.48
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Spear of Desolation
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
    this god: Spear of Desolation, Gluttonous Grimoire, Nimble Ring, Amanita Charm,
    Soul Gem, Kinetic Cuirass, Breastplate of Valor, Spear of the Magus, Helm of Radiance,
    Shifter''s Shield, Lotus Sickle, Rod of Asclepius, Shield of the Phoenix, Bragi''s
    Harp, Bracer of The Abyss, Obsidian Shard, Erosion, Jade Scepter, Stone of Binding,
    Daybreak Gavel, Eye of Providence, Draconic Scale, Screeching Gargoyle, Doom Orb,
    Wish-Granting Pearl, Chronos'' Pendant.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.6
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.65
      pick: 0.19
      fit: 0.28
    Spear of Desolation:
      total: 0.55
      efficiency: 0.58
      win: 0.67
      pick: 0.08
      fit: 0.3
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.65
      pick: 0.22
      fit: 0.22
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Spear of Desolation, Amanita Charm,
    Breastplate of Valor, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous
    Grimoire, Lotus Sickle, Screeching Gargoyle, Shifter''s Shield, Spear of the Magus,
    Helm of Radiance, Erosion, Prophetic Cloak, Eye of Providence, Gladiator''s Shield,
    Draconic Scale, Gem of Focus, Stone of Binding, Rod of Asclepius, Eye of Erebus,
    Magi''s Cloak, Daybreak Gavel, Obsidian Shard, Midgardian Mail, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.19
      fit: 0.43
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.1
      fit: 0.43
    Spear of Desolation:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.08
      fit: 0.53
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.65
      pick: 0.19
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.85
      win: 0.65
      pick: 0.22
      fit: 0.23
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Spear of Desolation, Soul Gem, Breastplate of Valor, Spear of the Magus, Shifter''s
    Shield, Helm of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion, Lotus
    Sickle, Rod of Asclepius, Eye of Providence, Draconic Scale, Jade Scepter, Stone
    of Binding, Chronos'' Pendant, Doom Orb, Helm of Darkness, Wish-Granting Pearl,
    The World Stone, Screeching Gargoyle, Magi''s Cloak, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.58
      efficiency: 0.58
      win: 0.67
      pick: 0.08
      fit: 0.51
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.65
      pick: 0.19
      fit: 0.48
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.65
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
