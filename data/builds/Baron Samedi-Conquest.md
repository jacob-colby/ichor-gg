---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.65
  aspect_win_rate: 0.53
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.17
    win_rate: 0.54
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.14
      win_rate: 0.68
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 0.71
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.43
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.69
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.58
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.4
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.56
  - name: Stampede
    pick_rate: 0.11
    win_rate: 0.53
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.4
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.58
    alternates:
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.71
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.29
  - name: Olmec Blue
    pick_rate: 0.07
    win_rate: 0.8
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.07
      win_rate: 0.8
    - name: Sage's Ring
      pick_rate: 0.07
      win_rate: 0.6
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.46
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.67
  - name: Sands Of Time
    pick_rate: 0.14
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-10-11'
  god_win_rate: 0.5460526315789473
  god_matches_won: 83
  god_matches_played: 152
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-11'
  god_matches_analyzed: 5242
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Spear of the Magus
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Soul Gem, Spear
    of the Magus, Helm of Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius,
    Eye of Providence, Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Shifter''s Shield, Midgardian Mail, Dreamer''s Idol, Rod
    of Tahuti, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.58
      pick: 0.2
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.48
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.17
      fit: 0.51
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Doom Orb
  - Wish-Granting Pearl
  - Amanita Charm
  flex_slots:
  - Wish-Granting Pearl
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of the Magus, Soul Gem, Helm
    of Radiance, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet,
    The World Stone, Death Metal, Chronos'' Pendant, Shield of the Phoenix, Jade Scepter,
    Erosion, Rod of Tahuti, Eye of Providence, Stone of Binding, Draconic Scale, Triton''s
    Conch, Screeching Gargoyle, Daybreak Gavel, Shifter''s Shield, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.2
      fit: 0.28
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.33
    Doom Orb:
      total: 0.5
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.37
    Wish-Granting Pearl:
      total: 0.5
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Spear of the Magus
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Spear of the
    Magus, Helm of Radiance, Shield of the Phoenix, Doom Orb, Rod of Asclepius, Erosion,
    Chronos'' Pendant, The World Stone, Screeching Gargoyle, Eye of Providence, Stone
    of Binding, Draconic Scale, Dreamer''s Idol, Rod of Tahuti, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak, Daybreak Gavel, Ancient Signet, Shifter''s Shield, Obsidian
    Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.39
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.17
      fit: 0.49
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
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
  - Freya's Tears
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Spear of Desolation
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Chandra''s Grace, Shield of the Phoenix, Rod
    of Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, Spear of the
    Magus, Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s Necklace, Erosion,
    Eye of Providence, Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Glorious Pridwen, Chronos'' Pendant, Shifter''s Shield,
    Rod of Tahuti, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.2
      fit: 0.29
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.44
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.17
      fit: 0.51
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
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Rod of Tahuti
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
    Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Void Shield, Void Stone,
    Doom Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Rod of Tahuti, Shield
    of the Phoenix, Rod of Asclepius, Erosion, Eye of Providence, Draconic Scale,
    Chronos'' Pendant, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Shifter''s
    Shield, Obsidian Shard.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.68
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.54
      pick: 0.17
      fit: 0.59
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.29
      pick: 0.13
      fit: 0.48
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Gluttonous Grimoire
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
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Kinetic Cuirass,
    Spear of the Magus, Helm of Radiance, Rod of Asclepius, Bragi''s Harp, Shield
    of the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion, Chronos'' Pendant,
    Daybreak Gavel, Screeching Gargoyle, Eye of Providence, Jade Scepter, Ancient
    Signet, Wish-Granting Pearl, Doom Orb, Draconic Scale, Rod of Tahuti, Shifter''s
    Shield, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.2
      fit: 0.18
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
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.58
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.28
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Soul Gem, Kinetic Cuirass,
    Shield of the Phoenix, Gluttonous Grimoire, Screeching Gargoyle, Chronos'' Pendant,
    Spear of the Magus, Helm of Radiance, Prophetic Cloak, Erosion, Gladiator''s Shield,
    Eye of Providence, Gem of Focus, Stone of Binding, Draconic Scale, Rod of Asclepius,
    Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord,
    Shifter''s Shield, Rod of Tahuti, Obsidian Shard.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.58
      pick: 0.2
      fit: 0.43
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.56
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.17
      fit: 0.53
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
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
    Grimoire, Soul Gem, Spear of the Magus, Shifter''s Shield, Helm of Radiance, Obsidian
    Shard, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye of Providence, Draconic
    Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.58
      pick: 0.2
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.48
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.17
      fit: 0.51
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.29
      pick: 0.13
      fit: 0.37
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
