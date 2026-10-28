---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.68
  aspect_win_rate: 0.59
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.46
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.65
  - name: Stampede
    pick_rate: 0.12
    win_rate: 0.64
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.57
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.04
      win_rate: 0.63
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.62
  - name: Ethereal Staff
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.5
  - name: Sage's Ring
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.05
      win_rate: 0.2
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.55
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.69
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-10-28'
  god_win_rate: 0.5675675675675675
  god_matches_won: 105
  god_matches_played: 185
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-28'
  god_matches_analyzed: 8361
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Spear of the Magus, Shifter''s Shield, Helm of Radiance, Obsidian Shard,
    Shield of the Phoenix, Erosion, Rod of Asclepius, Eye of Providence, Spear of
    Desolation, Draconic Scale, Stone of Binding, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.2
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.19
      fit: 0.31
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.11
      fit: 0.31
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.18
      fit: 0.48
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.18
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.54
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
  - Ethereal Staff
  - Freya's Tears
  - Stampede
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Stampede
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Breastplate
    of Valor, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of the Magus,
    Soul Gem, Helm of Radiance, Obsidian Shard, Shifter''s Shield, Rod of Asclepius,
    Wish-Granting Pearl, Doom Orb, Ancient Signet, The World Stone, Death Metal, Shield
    of the Phoenix, Jade Scepter, Erosion, Spear of Desolation, Eye of Providence,
    Stone of Binding, Draconic Scale, Triton''s Conch, Screeching Gargoyle, Daybreak
    Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.19
      fit: 0.28
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.11
      fit: 0.28
    Ethereal Staff:
      total: 0.53
      efficiency: 0.46
      win: 0.67
      pick: 0.13
      fit: 0.39
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.53
      pick: 0.18
      fit: 0.33
    Stampede:
      total: 0.51
      efficiency: 0.51
      win: 0.64
      pick: 0.16
      fit: 0.23
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.18
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Ethereal Staff
  - Freya's Tears
  - Stampede
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Breastplate of Valor, Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic
    Cuirass, Spear of the Magus, Obsidian Shard, Helm of Radiance, Shifter''s Shield,
    Spear of Desolation, Shield of the Phoenix, Doom Orb, Rod of Asclepius, Erosion,
    The World Stone, Screeching Gargoyle, Eye of Providence, Stone of Binding, Draconic
    Scale, Dreamer''s Idol, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak
    Gavel, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.14
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.19
      fit: 0.27
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.11
      fit: 0.27
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.18
      fit: 0.39
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.18
      fit: 0.35
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
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
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Ethereal Staff
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Ethereal Staff, Soul Gem, Breastplate of Valor, Shield
    of the Phoenix, Rod of Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Spear
    of the Magus, Shifter''s Shield, Lifebinder, Obsidian Shard, Helm of Radiance,
    Sphere of Negation, Yogi''s Necklace, Chandra''s Grace, Erosion, Eye of Providence,
    Phoenix Feather, Spear of Desolation, Draconic Scale, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Glorious Pridwen.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.2
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.19
      fit: 0.29
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.11
      fit: 0.29
    Ethereal Staff:
      total: 0.59
      efficiency: 0.46
      win: 0.67
      pick: 0.13
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.18
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Ethereal Staff
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Gluttonous Grimoire
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Breastplate of Valor, Gluttonous Grimoire, Amanita Charm, Soul Gem,
    Spear of the Magus, Stone of Binding, Obsidian Shard, Screeching Gargoyle, Kinetic
    Cuirass, Void Shield, Spear of Desolation, Void Stone, Doom Orb, Helm of Radiance,
    Shifter''s Shield, The World Stone, Dreamer''s Idol, Shield of the Phoenix, Rod
    of Asclepius, Erosion, Eye of Providence, Draconic Scale, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.17
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.19
      fit: 0.26
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.11
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.7
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.18
      fit: 0.48
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Gluttonous Grimoire, Nimble Ring, Amanita Charm,
    Soul Gem, Kinetic Cuirass, Spear of the Magus, Helm of Radiance, Obsidian Shard,
    Shifter''s Shield, Rod of Asclepius, Bragi''s Harp, Shield of the Phoenix, Bracer
    of The Abyss, Stone of Binding, Erosion, Daybreak Gavel, Screeching Gargoyle,
    Eye of Providence, Jade Scepter, Ancient Signet, Wish-Granting Pearl, Doom Orb,
    Draconic Scale, Spear of Desolation.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.6
      pick: 0.11
      fit: 0.18
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.18
      fit: 0.22
  community_ordered:
  - Breastplate of Valor
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire, Screeching
    Gargoyle, Shifter''s Shield, Spear of Desolation, Spear of the Magus, Helm of
    Radiance, Obsidian Shard, Prophetic Cloak, Erosion, Gladiator''s Shield, Eye of
    Providence, Gem of Focus, Stone of Binding, Draconic Scale, Rod of Asclepius,
    Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.19
      fit: 0.43
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.11
      fit: 0.43
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.18
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.18
      fit: 0.23
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Breastplate of Valor, Soul Gem, Spear of the Magus, Shifter''s
    Shield, Helm of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion, Rod
    of Asclepius, Eye of Providence, Draconic Scale, Stone of Binding, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.46
      pick: 0.13
      fit: 0.51
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.18
      fit: 0.48
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.18
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
