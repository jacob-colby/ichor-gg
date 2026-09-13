---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.56
  aspect_win_rate: 0.52
  slot_order:
  - name: Lifebinder
    pick_rate: 0.22
    win_rate: 0.49
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.38
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.44
  - name: Prophetic Cloak
    pick_rate: 0.15
    win_rate: 0.77
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.29
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.58
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.43
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.58
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.7
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.76
  - name: Rod of Asclepius
    pick_rate: 0.05
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.83
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.44
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.83
    - name: Mote of Chaos
      pick_rate: 0.05
      win_rate: 0.8
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.64
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.56
  - name: Sands Of Time
    pick_rate: 0.16
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-09-13'
  god_win_rate: 0.5240384615384616
  god_matches_won: 109
  god_matches_played: 208
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-13'
  god_matches_analyzed: 5560
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Obsidian Shard
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
    Soul Gem, Spear of the Magus, Shifter''s Shield, Helm of Radiance, Rod of Asclepius,
    Shield of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Stone of Binding,
    Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness,
    The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol, Spear of Desolation,
    Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.58
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.59
    Prophetic Cloak:
      total: 0.58
      efficiency: 0.44
      win: 0.77
      pick: 0.2
      fit: 0.48
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.48
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.28
      fit: 0.47
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  - Wish-Granting Pearl
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of the Magus,
    Soul Gem, Helm of Radiance, Rod of Asclepius, Shifter''s Shield, Wish-Granting
    Pearl, Doom Orb, Ancient Signet, The World Stone, Death Metal, Shield of the Phoenix,
    Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Triton''s
    Conch, Screeching Gargoyle, Daybreak Gavel, Spear of Desolation, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.19
      fit: 0.28
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.44
      win: 0.77
      pick: 0.2
      fit: 0.33
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.33
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.44
      pick: 0.11
      fit: 0.37
    Wish-Granting Pearl:
      total: 0.49
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Obsidian Shard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass,
    Spear of the Magus, Helm of Radiance, Shifter''s Shield, Shield of the Phoenix,
    Rod of Asclepius, Doom Orb, Erosion, The World Stone, Screeching Gargoyle, Eye
    of Providence, Stone of Binding, Draconic Scale, Dreamer''s Idol, Jade Scepter,
    Wish-Granting Pearl, Spear of Desolation, Magi''s Cloak, Daybreak Gavel, Ancient
    Signet, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.19
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.47
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.44
      win: 0.77
      pick: 0.2
      fit: 0.39
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.39
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.28
      fit: 0.45
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
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
    this god: Amanita Charm, Soul Gem, Rod of Asclepius, Rod of Tahuti, Shield of
    the Phoenix, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, Spear of the
    Magus, Shifter''s Shield, Helm of Radiance, Sphere of Negation, Yogi''s Necklace,
    Chandra''s Grace, Erosion, Eye of Providence, Phoenix Feather, Draconic Scale,
    Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Glorious Pridwen, Spear of
    Desolation, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.19
      fit: 0.29
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.59
    Prophetic Cloak:
      total: 0.58
      efficiency: 0.44
      win: 0.77
      pick: 0.2
      fit: 0.44
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.44
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Prophetic Cloak
  - Gluttonous Grimoire
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Genji's Guard
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
    for this god: Rod of Tahuti, Gluttonous Grimoire, Amanita Charm, Soul Gem, Spear
    of the Magus, Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Void Shield,
    Void Stone, Doom Orb, Helm of Radiance, Shifter''s Shield, The World Stone, Dreamer''s
    Idol, Rod of Asclepius, Shield of the Phoenix, Erosion, Spear of Desolation, Eye
    of Providence, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak,
    Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.19
      fit: 0.26
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.44
      win: 0.77
      pick: 0.2
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.4
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.44
      pick: 0.11
      fit: 0.48
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.56
      pick: 0.28
      fit: 0.58
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
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
  - Gluttonous Grimoire
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
    Gem, Kinetic Cuirass, Spear of the Magus, Helm of Radiance, Shifter''s Shield,
    Rod of Asclepius, Bragi''s Harp, Shield of the Phoenix, Bracer of The Abyss, Stone
    of Binding, Erosion, Daybreak Gavel, Screeching Gargoyle, Eye of Providence, Jade
    Scepter, Ancient Signet, Wish-Granting Pearl, Doom Orb, Draconic Scale, Spear
    of Desolation, Chronos'' Pendant.'
  slot_scores:
    Prophetic Cloak:
      total: 0.55
      efficiency: 0.44
      win: 0.77
      pick: 0.2
      fit: 0.28
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.28
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Soul
    Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire, Screeching Gargoyle,
    Shifter''s Shield, Spear of the Magus, Helm of Radiance, Erosion, Gladiator''s
    Shield, Eye of Providence, Rod of Asclepius, Gem of Focus, Stone of Binding, Draconic
    Scale, Spear of Desolation, Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian
    Mail, Mantle Of Discord, Chronos'' Pendant.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.58
      pick: 0.19
      fit: 0.43
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.49
    Prophetic Cloak:
      total: 0.6
      efficiency: 0.44
      win: 0.77
      pick: 0.2
      fit: 0.56
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.56
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Spear of Desolation, Soul Gem, Spear of the Magus, Shifter''s Shield,
    Helm of Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye of Providence,
    Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.58
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.44
      pick: 0.09
      fit: 0.51
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.48
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.44
      pick: 0.11
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Kinetic Cuirass
  - Prophetic Cloak
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Gluttonous Grimoire, Spear of Desolation, Soul Gem, Spear of the Magus,
    Shifter''s Shield, Helm of Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius,
    Eye of Providence, Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.59
    Prophetic Cloak:
      total: 0.58
      efficiency: 0.44
      win: 0.77
      pick: 0.2
      fit: 0.48
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.44
      pick: 0.09
      fit: 0.51
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.48
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.44
      pick: 0.11
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Prophetic Cloak
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  swaps:
  - added: Prophetic Cloak
    removed: Genji's Guard
    reason: community 77% win over 31 matches (vs 52% on this god), taking the model's
      weakest slot from Genji's Guard
  starter: *id001
---
