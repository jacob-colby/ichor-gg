---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.64
  aspect_win_rate: 0.51
  slot_order:
  - name: Chronos' Pendant
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Lifebinder
      pick_rate: 0.1
      win_rate: 0.52
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 0.67
  - name: Shifter's Shield
    pick_rate: 0.1
    win_rate: 0.48
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.64
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.52
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.71
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.45
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.71
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.63
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.42
  - name: Rod of Tahuti
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.56
  - name: Engraved Guard
    pick_rate: 0.04
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.29
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.8
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.43
  - name: Archmage's Gem
    pick_rate: 0.13
    win_rate: 0.57
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-09-29'
  god_win_rate: 0.5359712230215827
  god_matches_won: 149
  god_matches_played: 278
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-29'
  god_matches_analyzed: 8229
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Chronos' Pendant
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Soul Gem, Spear of the Magus, Helm of Radiance, Shifter''s
    Shield, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye of Providence, Draconic
    Scale, Stone of Binding, Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching
    Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s
    Idol, Obsidian Shard.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.61
      pick: 0.16
      fit: 0.34
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.2
      fit: 0.48
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.11
      fit: 0.37
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Chronos' Pendant
  - Genji's Guard
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
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation,
    Spear of the Magus, Soul Gem, Helm of Radiance, Rod of Asclepius, Wish-Granting
    Pearl, Doom Orb, Ancient Signet, The World Stone, Death Metal, Shifter''s Shield,
    Shield of the Phoenix, Jade Scepter, Erosion, Eye of Providence, Stone of Binding,
    Draconic Scale, Triton''s Conch, Screeching Gargoyle, Daybreak Gavel, Obsidian
    Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.28
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.17
      fit: 0.28
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.61
      pick: 0.16
      fit: 0.28
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.2
      fit: 0.33
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.11
      fit: 0.37
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Chronos' Pendant
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Spear of Desolation, Soul
    Gem, Kinetic Cuirass, Spear of the Magus, Helm of Radiance, Shield of the Phoenix,
    Doom Orb, Shifter''s Shield, Rod of Asclepius, Erosion, The World Stone, Screeching
    Gargoyle, Eye of Providence, Stone of Binding, Draconic Scale, Dreamer''s Idol,
    Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Ancient Signet,
    Obsidian Shard.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.61
      pick: 0.16
      fit: 0.28
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.27
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.2
      fit: 0.39
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.11
      fit: 0.35
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Chronos' Pendant
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Chandra's Grace
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Chandra''s Grace, Soul Gem, Shield of
    the Phoenix, Rod of Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Ethereal
    Staff, Spear of Desolation, Lifebinder, Spear of the Magus, Helm of Radiance,
    Sphere of Negation, Shifter''s Shield, Yogi''s Necklace, Erosion, Eye of Providence,
    Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Glorious Pridwen, Obsidian Shard.'
  slot_scores:
    Chandra's Grace:
      total: 0.56
      efficiency: 0.45
      win: 0.67
      pick: 0.1
      fit: 0.63
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.29
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.61
      pick: 0.16
      fit: 0.34
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.2
      fit: 0.44
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.11
      fit: 0.37
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Chandra's Grace
  - Genji's Guard
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Gluttonous Grimoire
  - Freya's Tears
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Spear of the Magus
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
    for this god: Rod of Tahuti, Gluttonous Grimoire, Amanita Charm, Spear of Desolation,
    Soul Gem, Spear of the Magus, Stone of Binding, Screeching Gargoyle, Kinetic Cuirass,
    Void Shield, Void Stone, Doom Orb, Helm of Radiance, The World Stone, Dreamer''s
    Idol, Shield of the Phoenix, Shifter''s Shield, Rod of Asclepius, Erosion, Eye
    of Providence, Obsidian Shard, Draconic Scale, Jade Scepter, Wish-Granting Pearl,
    Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.2
      fit: 0.4
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.59
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.11
      fit: 0.48
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Genji's Guard
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
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
    this god: Rod of Tahuti, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Spear of Desolation, Spear of the Magus, Helm of Radiance,
    Rod of Asclepius, Bragi''s Harp, Shield of the Phoenix, Shifter''s Shield, Bracer
    of The Abyss, Stone of Binding, Erosion, Daybreak Gavel, Screeching Gargoyle,
    Eye of Providence, Jade Scepter, Ancient Signet, Wish-Granting Pearl, Doom Orb,
    Draconic Scale, Obsidian Shard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.28
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.18
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.52
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.2
      fit: 0.28
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.11
      fit: 0.22
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Chronos' Pendant
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Chandra's Grace
  - Spear of Desolation
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Spear
    of Desolation, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire,
    Screeching Gargoyle, Spear of the Magus, Helm of Radiance, Shifter''s Shield,
    Prophetic Cloak, Erosion, Gladiator''s Shield, Eye of Providence, Gem of Focus,
    Stone of Binding, Draconic Scale, Rod of Asclepius, Eye of Erebus, Magi''s Cloak,
    Daybreak Gavel, Midgardian Mail, Mantle Of Discord, Obsidian Shard.'
  slot_scores:
    Chandra's Grace:
      total: 0.53
      efficiency: 0.45
      win: 0.67
      pick: 0.1
      fit: 0.42
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.43
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.61
      pick: 0.16
      fit: 0.39
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.2
      fit: 0.56
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.11
      fit: 0.23
  community_ordered:
  - Chandra's Grace
  - Genji's Guard
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Spear of Desolation, Soul Gem, Spear of the Magus, Shifter''s Shield,
    Helm of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion, Rod of Asclepius,
    Eye of Providence, Draconic Scale, Stone of Binding, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.31
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.2
      fit: 0.48
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.11
      fit: 0.37
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
