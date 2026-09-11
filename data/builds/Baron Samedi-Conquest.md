---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.5
  aspect_win_rate: 0.56
  slot_order:
  - name: Lifebinder
    pick_rate: 0.18
    win_rate: 0.45
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.12
      win_rate: 0.5
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.44
  - name: Prophetic Cloak
    pick_rate: 0.17
    win_rate: 0.74
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.33
    - name: The World Stone
      pick_rate: 0.08
      win_rate: 0.44
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.45
    - name: Heartwood Charm
      pick_rate: 0.06
      win_rate: 0.71
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.7
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.89
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.63
  - name: Heartwood Charm
    pick_rate: 0.06
    win_rate: 0.4
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.8
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.6
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Oracle Staff
      pick_rate: 0.05
      win_rate: 0.33
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.57
  - name: Sands Of Time
    pick_rate: 0.18
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-09-11'
  god_win_rate: 0.543859649122807
  god_matches_won: 62
  god_matches_played: 114
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Prophetic Cloak
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Soul Gem, Chronos'' Pendant, Spear of the Magus, Shifter''s
    Shield, Helm of Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye
    of Providence, Draconic Scale, Stone of Binding, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.44
      win: 0.74
      pick: 0.23
      fit: 0.48
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.22
      fit: 0.31
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.17
      fit: 0.48
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.37
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.6
      pick: 0.28
      fit: 0.47
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Prophetic Cloak
  - Genji's Guard
  - Freya's Tears
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Chronos'' Pendant,
    Spear of Desolation, Spear of the Magus, Soul Gem, Helm of Radiance, Shifter''s
    Shield, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet, The World
    Stone, Death Metal, Shield of the Phoenix, Jade Scepter, Erosion, Eye of Providence,
    Stone of Binding, Draconic Scale, Triton''s Conch, Screeching Gargoyle, Daybreak
    Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.22
      fit: 0.28
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.16
      fit: 0.28
    Prophetic Cloak:
      total: 0.55
      efficiency: 0.44
      win: 0.74
      pick: 0.23
      fit: 0.33
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.7
      pick: 0.17
      fit: 0.33
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.37
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.28
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Prophetic Cloak
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Amanita Charm
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Spear of Desolation, Soul
    Gem, Kinetic Cuirass, Spear of the Magus, Chronos'' Pendant, Helm of Radiance,
    Shifter''s Shield, Shield of the Phoenix, Doom Orb, Rod of Asclepius, The World
    Stone, Erosion, Screeching Gargoyle, Eye of Providence, Stone of Binding, Draconic
    Scale, Dreamer''s Idol, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak
    Gavel, Ancient Signet.'
  slot_scores:
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.44
      win: 0.74
      pick: 0.23
      fit: 0.39
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.22
      fit: 0.27
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.17
      fit: 0.39
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.35
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.28
      fit: 0.45
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Prophetic Cloak
  - Genji's Guard
  - Freya's Tears
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Prophetic Cloak
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Obsidian Shard
  - Genji's Guard
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
    this god: Rod of Tahuti, Amanita Charm, Soul Gem, Shield of the Phoenix, Rod of
    Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, Spear of Desolation,
    Chronos'' Pendant, Spear of the Magus, Shifter''s Shield, Helm of Radiance, Sphere
    of Negation, Yogi''s Necklace, Chandra''s Grace, Erosion, Eye of Providence, Phoenix
    Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book,
    Glorious Pridwen.'
  slot_scores:
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.44
      win: 0.74
      pick: 0.23
      fit: 0.44
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.22
      fit: 0.29
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.17
      fit: 0.44
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.37
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.6
      pick: 0.28
      fit: 0.47
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Prophetic Cloak
  - Genji's Guard
  - Freya's Tears
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Prophetic Cloak
  - Genji's Guard
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Genji's Guard
  - Gluttonous Grimoire
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
    Void Shield, Chronos'' Pendant, Void Stone, Doom Orb, Helm of Radiance, Shifter''s
    Shield, The World Stone, Dreamer''s Idol, Shield of the Phoenix, Rod of Asclepius,
    Erosion, Eye of Providence, Draconic Scale, Jade Scepter, Wish-Granting Pearl,
    Magi''s Cloak.'
  slot_scores:
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.44
      win: 0.74
      pick: 0.23
      fit: 0.4
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.22
      fit: 0.26
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.17
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.55
      win: 0.45
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.48
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.6
      pick: 0.28
      fit: 0.58
  community_ordered:
  - Prophetic Cloak
  - Genji's Guard
  - Freya's Tears
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Prophetic Cloak
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Chronos'' Pendant, Spear of Desolation, Spear of the Magus,
    Helm of Radiance, Shifter''s Shield, Rod of Asclepius, Bragi''s Harp, Shield of
    the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion, Daybreak Gavel, Screeching
    Gargoyle, Eye of Providence, Jade Scepter, Ancient Signet, Wish-Granting Pearl,
    Doom Orb, Draconic Scale.'
  slot_scores:
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.44
      win: 0.74
      pick: 0.23
      fit: 0.28
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.52
      win: 0.45
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.43
      efficiency: 0.44
      win: 0.45
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.7
      pick: 0.17
      fit: 0.28
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.6
      pick: 0.28
      fit: 0.32
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Spear
    of Desolation, Chronos'' Pendant, Soul Gem, Kinetic Cuirass, Shield of the Phoenix,
    Gluttonous Grimoire, Screeching Gargoyle, Shifter''s Shield, Spear of the Magus,
    Helm of Radiance, Erosion, Gladiator''s Shield, Eye of Providence, Gem of Focus,
    Stone of Binding, Draconic Scale, Rod of Asclepius, Eye of Erebus, Magi''s Cloak,
    Daybreak Gavel, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.22
      fit: 0.43
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.16
      fit: 0.43
    Prophetic Cloak:
      total: 0.58
      efficiency: 0.44
      win: 0.74
      pick: 0.23
      fit: 0.56
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.7
      pick: 0.17
      fit: 0.56
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.6
      pick: 0.28
      fit: 0.33
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Obsidian Shard
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
    Grimoire, Spear of Desolation, Soul Gem, Spear of the Magus, Shifter''s Shield,
    Helm of Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye of Providence,
    Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.22
      fit: 0.31
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.17
      fit: 0.48
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.44
      pick: 0.08
      fit: 0.51
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  starter: *id001
---
