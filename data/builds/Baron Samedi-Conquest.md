---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.67
  aspect_win_rate: 0.61
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.72
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.38
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.67
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.55
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.71
  - name: Rod of Tahuti
    pick_rate: 0.11
    win_rate: 0.71
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.43
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.89
  - name: Ethereal Staff
    pick_rate: 0.07
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.57
  - name: Chronos' Pendant
    pick_rate: 0.07
    win_rate: 0.2
    alternates:
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.75
    - name: Obsidian Shard
      pick_rate: 0.05
      win_rate: 0.75
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.24
    win_rate: 0.64
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.64
  - name: Pendulum of the Ages
    pick_rate: 0.14
    win_rate: 0.7
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-10-26'
  god_win_rate: 0.5693430656934306
  god_matches_won: 78
  god_matches_played: 137
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-26'
  god_matches_analyzed: 6194
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
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
    this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Freya''s Tears,
    Breastplate of Valor, Soul Gem, Spear of the Magus, Shifter''s Shield, Helm of
    Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye of Providence,
    Draconic Scale, Stone of Binding, Jade Scepter, Doom Orb, Wish-Granting Pearl,
    Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak, Midgardian
    Mail, Dreamer''s Idol, Spear of Desolation.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.31
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.11
      fit: 0.48
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.71
      pick: 0.18
      fit: 0.37
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.75
      pick: 0.15
      fit: 0.47
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Breastplate of Valor, Gluttonous Grimoire, Kinetic Cuirass, Spear of the
    Magus, Freya''s Tears, Soul Gem, Helm of Radiance, Shifter''s Shield, Rod of Asclepius,
    Wish-Granting Pearl, Doom Orb, Ancient Signet, The World Stone, Death Metal, Shield
    of the Phoenix, Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Draconic
    Scale, Triton''s Conch, Screeching Gargoyle, Daybreak Gavel, Spear of Desolation.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.28
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.71
      pick: 0.18
      fit: 0.37
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.75
      pick: 0.15
      fit: 0.41
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Gluttonous Grimoire, Soul Gem, Breastplate of Valor, Kinetic
    Cuirass, Freya''s Tears, Spear of the Magus, Helm of Radiance, Shifter''s Shield,
    Shield of the Phoenix, Doom Orb, Rod of Asclepius, Erosion, The World Stone, Screeching
    Gargoyle, Eye of Providence, Stone of Binding, Draconic Scale, Dreamer''s Idol,
    Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Spear of Desolation,
    Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.14
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.27
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.27
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.71
      pick: 0.18
      fit: 0.35
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.75
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Rod of Asclepius, Gluttonous
    Grimoire, Kinetic Cuirass, Freya''s Tears, Breastplate of Valor, Spear of the
    Magus, Shifter''s Shield, Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s
    Necklace, Chandra''s Grace, Erosion, Eye of Providence, Phoenix Feather, Draconic
    Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Glorious Pridwen,
    Spear of Desolation.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.29
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.71
      pick: 0.18
      fit: 0.37
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.75
      pick: 0.15
      fit: 0.47
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
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
    for this god: Gluttonous Grimoire, Amanita Charm, Soul Gem, Spear of the Magus,
    Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Breastplate of Valor,
    Freya''s Tears, Void Shield, Void Stone, Doom Orb, Helm of Radiance, Shifter''s
    Shield, The World Stone, Dreamer''s Idol, Shield of the Phoenix, Rod of Asclepius,
    Erosion, Spear of Desolation, Eye of Providence, Draconic Scale, Jade Scepter,
    Wish-Granting Pearl, Magi''s Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.55
      win: 0.63
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.71
      pick: 0.18
      fit: 0.48
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.75
      pick: 0.15
      fit: 0.58
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Breastplate
    of Valor, Kinetic Cuirass, Freya''s Tears, Spear of the Magus, Helm of Radiance,
    Shifter''s Shield, Rod of Asclepius, Bragi''s Harp, Shield of the Phoenix, Bracer
    of The Abyss, Stone of Binding, Erosion, Daybreak Gavel, Screeching Gargoyle,
    Eye of Providence, Jade Scepter, Ancient Signet, Wish-Granting Pearl, Doom Orb,
    Draconic Scale, Spear of Desolation.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.18
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.51
      efficiency: 0.44
      win: 0.63
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.71
      pick: 0.18
      fit: 0.22
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.75
      pick: 0.15
      fit: 0.32
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Freya''s Tears,
    Amanita Charm, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire,
    Screeching Gargoyle, Shifter''s Shield, Spear of the Magus, Helm of Radiance,
    Prophetic Cloak, Erosion, Gladiator''s Shield, Eye of Providence, Gem of Focus,
    Stone of Binding, Draconic Scale, Rod of Asclepius, Spear of Desolation, Eye of
    Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.43
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.11
      fit: 0.56
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.71
      pick: 0.18
      fit: 0.23
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.75
      pick: 0.15
      fit: 0.33
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
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
    Underrated for this god: Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous
    Grimoire, Spear of Desolation, Breastplate of Valor, Soul Gem, Spear of the Magus,
    Shifter''s Shield, Helm of Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius,
    Eye of Providence, Draconic Scale, Stone of Binding, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.31
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.14
      fit: 0.51
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.11
      fit: 0.48
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.71
      pick: 0.18
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
