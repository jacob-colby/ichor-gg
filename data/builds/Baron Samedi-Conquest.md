---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.74
  aspect_win_rate: 0.6
  slot_order:
  - name: Stampede
    pick_rate: 0.28
    win_rate: 0.69
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.13
      win_rate: 0.33
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.8
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.86
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.25
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.8
    alternates:
    - name: Genji's Guard
      pick_rate: 0.24
      win_rate: 0.55
    - name: Contagion
      pick_rate: 0.07
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.25
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 1.0
  - name: Ethereal Staff
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.5
  - name: Chronos' Pendant
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 1.0
    - name: Veve Charm
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.34
    win_rate: 0.75
  - name: Bluestone Brooch
    pick_rate: 0.32
    win_rate: 0.67
  - name: Conduit Gem
    pick_rate: 0.09
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-10-22'
  god_win_rate: 0.574468085106383
  god_matches_won: 27
  god_matches_played: 47
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-22'
  god_matches_analyzed: 1760
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Genji's Guard
  - Stampede
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
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Breastplate of Valor, Soul Gem, Spear of the Magus, Helm
    of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion, Rod of Asclepius,
    Eye of Providence, Draconic Scale, Stone of Binding, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.51
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.8
      pick: 0.29
      fit: 0.31
    Stampede:
      total: 0.55
      efficiency: 0.51
      win: 0.69
      pick: 0.28
      fit: 0.32
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Stampede
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Genji's Guard
  - Stampede
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Amanita Charm, Breastplate of Valor, Gluttonous Grimoire, Kinetic Cuirass,
    Spear of Desolation, Spear of the Magus, Soul Gem, Helm of Radiance, Obsidian
    Shard, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet, The World
    Stone, Death Metal, Shield of the Phoenix, Jade Scepter, Erosion, Eye of Providence,
    Stone of Binding, Draconic Scale, Triton''s Conch, Screeching Gargoyle, Daybreak
    Gavel, Shifter''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.8
      pick: 0.29
      fit: 0.28
    Stampede:
      total: 0.54
      efficiency: 0.51
      win: 0.69
      pick: 0.28
      fit: 0.23
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Stampede
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Genji's Guard
  - Stampede
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Spear of Desolation, Soul
    Gem, Breastplate of Valor, Kinetic Cuirass, Spear of the Magus, Obsidian Shard,
    Helm of Radiance, Shield of the Phoenix, Doom Orb, Rod of Asclepius, Erosion,
    The World Stone, Screeching Gargoyle, Eye of Providence, Stone of Binding, Draconic
    Scale, Dreamer''s Idol, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak
    Gavel, Ancient Signet, Shifter''s Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.14
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.29
      fit: 0.27
    Stampede:
      total: 0.54
      efficiency: 0.51
      win: 0.69
      pick: 0.28
      fit: 0.24
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.35
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Stampede
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Rod of Tahuti
  - Stampede
  - Genji's Guard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Stampede
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Soul Gem, Shield of the Phoenix, Rod of
    Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation, Breastplate
    of Valor, Spear of the Magus, Lifebinder, Obsidian Shard, Helm of Radiance, Sphere
    of Negation, Yogi''s Necklace, Chandra''s Grace, Erosion, Eye of Providence, Phoenix
    Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book,
    Glorious Pridwen, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.37
    Stampede:
      total: 0.55
      efficiency: 0.51
      win: 0.69
      pick: 0.28
      fit: 0.34
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.8
      pick: 0.29
      fit: 0.29
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Stampede
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Gluttonous Grimoire
  - Genji's Guard
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Spear of the Magus
  - Stone of Binding
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Amanita Charm, Spear of Desolation,
    Soul Gem, Spear of the Magus, Stone of Binding, Obsidian Shard, Screeching Gargoyle,
    Kinetic Cuirass, Breastplate of Valor, Void Shield, Void Stone, Doom Orb, Helm
    of Radiance, The World Stone, Dreamer''s Idol, Shield of the Phoenix, Rod of Asclepius,
    Erosion, Eye of Providence, Draconic Scale, Jade Scepter, Wish-Granting Pearl,
    Magi''s Cloak, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.68
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.29
      fit: 0.26
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.59
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Genji's Guard
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul
    Gem, Breastplate of Valor, Kinetic Cuirass, Spear of Desolation, Spear of the
    Magus, Helm of Radiance, Obsidian Shard, Rod of Asclepius, Bragi''s Harp, Shield
    of the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion, Daybreak Gavel,
    Screeching Gargoyle, Eye of Providence, Jade Scepter, Ancient Signet, Wish-Granting
    Pearl, Doom Orb, Draconic Scale, Shifter''s Shield.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.29
      fit: 0.18
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.58
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.22
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Genji's Guard
  - Stampede
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Stampede
  - Kinetic Cuirass
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Spear of Desolation, Soul Gem, Kinetic Cuirass, Shield of the Phoenix,
    Gluttonous Grimoire, Screeching Gargoyle, Spear of the Magus, Helm of Radiance,
    Obsidian Shard, Prophetic Cloak, Erosion, Gladiator''s Shield, Eye of Providence,
    Gem of Focus, Stone of Binding, Draconic Scale, Rod of Asclepius, Eye of Erebus,
    Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord, Shifter''s
    Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.8
      pick: 0.29
      fit: 0.43
    Stampede:
      total: 0.54
      efficiency: 0.51
      win: 0.69
      pick: 0.28
      fit: 0.25
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Stampede
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
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
    Grimoire, Spear of Desolation, Breastplate of Valor, Soul Gem, Spear of the Magus,
    Shifter''s Shield, Helm of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion,
    Rod of Asclepius, Eye of Providence, Draconic Scale, Stone of Binding, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.8
      pick: 0.29
      fit: 0.31
    Freya's Tears:
      total: 0.41
      efficiency: 0.61
      win: 0.25
      pick: 0.15
      fit: 0.48
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
