---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.44
  aspect_win_rate: 0.52
  slot_order:
  - name: Lifebinder
    pick_rate: 0.23
    win_rate: 0.45
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.13
      win_rate: 0.33
    - name: Heartwood Charm
      pick_rate: 0.1
      win_rate: 0.4
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.14
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.15
      win_rate: 0.71
    - name: Rod of Asclepius
      pick_rate: 0.1
      win_rate: 0.6
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.5
    - name: Heartwood Charm
      pick_rate: 0.11
      win_rate: 0.6
  - name: Rod of Tahuti
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 1.0
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.75
  - name: Heartwood Charm
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Rod of Asclepius
      pick_rate: 0.08
      win_rate: 0.33
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.67
  - name: Oracle Staff
    pick_rate: 0.13
    win_rate: 0.33
    alternates:
    - name: Captain's Ring
      pick_rate: 0.08
      win_rate: 0.0
    - name: Mote of Chaos
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Sands Of Time
    pick_rate: 0.19
    win_rate: 0.22
  - name: Pendulum of the Ages
    pick_rate: 0.15
    win_rate: 0.43
  - name: Bluestone Brooch
    pick_rate: 0.13
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-09-10'
  god_win_rate: 0.4166666666666667
  god_matches_won: 20
  god_matches_played: 48
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
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
    this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Spear of Desolation,
    Soul Gem, Spear of the Magus, Shifter''s Shield, Helm of Radiance, Obsidian Shard,
    Shield of the Phoenix, Erosion, Eye of Providence, Chronos'' Pendant, Draconic
    Scale, Stone of Binding, Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching
    Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s
    Idol.'
  slot_scores:
    Breastplate of Valor:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.2
      fit: 0.31
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.33
      pick: 0.0
      fit: 0.59
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.44
      win: 0.71
      pick: 0.2
      fit: 0.48
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.48
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.6
      pick: 0.2
      fit: 0.37
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  - Wish-Granting Pearl
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Wish-Granting Pearl
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation, Spear of the
    Magus, Soul Gem, Helm of Radiance, Obsidian Shard, Shifter''s Shield, Wish-Granting
    Pearl, Doom Orb, Chronos'' Pendant, Ancient Signet, The World Stone, Death Metal,
    Shield of the Phoenix, Jade Scepter, Erosion, Eye of Providence, Stone of Binding,
    Draconic Scale, Triton''s Conch, Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.2
      fit: 0.28
    Prophetic Cloak:
      total: 0.53
      efficiency: 0.44
      win: 0.71
      pick: 0.2
      fit: 0.33
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.33
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.6
      pick: 0.2
      fit: 0.37
    Wish-Granting Pearl:
      total: 0.39
      efficiency: 0.54
      win: 0.33
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
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
    god: Amanita Charm, Gluttonous Grimoire, Spear of Desolation, Soul Gem, Kinetic
    Cuirass, Spear of the Magus, Obsidian Shard, Helm of Radiance, Shifter''s Shield,
    Shield of the Phoenix, Chronos'' Pendant, Doom Orb, Erosion, The World Stone,
    Screeching Gargoyle, Eye of Providence, Stone of Binding, Draconic Scale, Dreamer''s
    Idol, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Ancient
    Signet.'
  slot_scores:
    Breastplate of Valor:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.2
      fit: 0.27
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.44
      win: 0.71
      pick: 0.2
      fit: 0.39
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.39
    Spear of Desolation:
      total: 0.42
      efficiency: 0.57
      win: 0.33
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.2
      fit: 0.35
    Amanita Charm:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  - Lifebinder
  - Amanita Charm
  flex_slots:
  - Lifebinder
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Spear of Desolation, Spear of the Magus, Shifter''s
    Shield, Obsidian Shard, Helm of Radiance, Sphere of Negation, Yogi''s Necklace,
    Chandra''s Grace, Erosion, Eye of Providence, Chronos'' Pendant, Phoenix Feather,
    Draconic Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Glorious
    Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.33
      pick: 0.0
      fit: 0.59
    Prophetic Cloak:
      total: 0.55
      efficiency: 0.44
      win: 0.71
      pick: 0.2
      fit: 0.44
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.44
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.6
      pick: 0.2
      fit: 0.37
    Lifebinder:
      total: 0.48
      efficiency: 0.46
      win: 0.45
      pick: 0.23
      fit: 0.69
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  - Lifebinder
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Prophetic Cloak
  - Freya's Tears
  - Gluttonous Grimoire
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
    for this god: Gluttonous Grimoire, Amanita Charm, Spear of Desolation, Soul Gem,
    Spear of the Magus, Stone of Binding, Obsidian Shard, Screeching Gargoyle, Kinetic
    Cuirass, Void Shield, Void Stone, Doom Orb, Helm of Radiance, Shifter''s Shield,
    The World Stone, Dreamer''s Idol, Shield of the Phoenix, Chronos'' Pendant, Erosion,
    Eye of Providence, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Magi''s
    Cloak.'
  slot_scores:
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.44
      win: 0.71
      pick: 0.2
      fit: 0.4
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.45
      efficiency: 0.55
      win: 0.33
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.0
      fit: 0.59
    Spear of the Magus:
      total: 0.43
      efficiency: 0.6
      win: 0.33
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.6
      pick: 0.2
      fit: 0.48
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Prophetic Cloak
  - Bracer of The Abyss
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Kinetic Cuirass,
    Spear of Desolation, Spear of the Magus, Helm of Radiance, Obsidian Shard, Shifter''s
    Shield, Chronos'' Pendant, Bragi''s Harp, Shield of the Phoenix, Bracer of The
    Abyss, Stone of Binding, Erosion, Daybreak Gavel, Screeching Gargoyle, Eye of
    Providence, Jade Scepter, Ancient Signet, Wish-Granting Pearl, Doom Orb, Draconic
    Scale.'
  slot_scores:
    Prophetic Cloak:
      total: 0.53
      efficiency: 0.44
      win: 0.71
      pick: 0.2
      fit: 0.28
    Bracer of The Abyss:
      total: 0.37
      efficiency: 0.52
      win: 0.33
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.37
      efficiency: 0.44
      win: 0.33
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.28
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.2
      fit: 0.22
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Amanita Charm, Spear of Desolation,
    Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire, Screeching
    Gargoyle, Chronos'' Pendant, Shifter''s Shield, Spear of the Magus, Helm of Radiance,
    Obsidian Shard, Erosion, Gladiator''s Shield, Eye of Providence, Gem of Focus,
    Stone of Binding, Draconic Scale, Eye of Erebus, Magi''s Cloak, Daybreak Gavel,
    Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.65
      win: 0.33
      pick: 0.2
      fit: 0.43
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.44
      win: 0.71
      pick: 0.2
      fit: 0.56
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.56
    Spear of Desolation:
      total: 0.43
      efficiency: 0.57
      win: 0.33
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.2
      fit: 0.23
    Amanita Charm:
      total: 0.44
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Soul Gem, Spear of the Magus, Shifter''s Shield, Helm of
    Radiance, Obsidian Shard, Shield of the Phoenix, Erosion, Eye of Providence, Draconic
    Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.33
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.35
      efficiency: 0.66
      win: 0.14
      pick: 0.2
      fit: 0.31
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.48
    Spear of Desolation:
      total: 0.43
      efficiency: 0.57
      win: 0.33
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.6
      pick: 0.2
      fit: 0.37
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
