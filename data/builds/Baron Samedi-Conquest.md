---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.61
  aspect_win_rate: 0.52
  slot_order:
  - name: Lifebinder
    pick_rate: 0.18
    win_rate: 0.45
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.54
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.48
  - name: Prophetic Cloak
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.36
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.44
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.44
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.54
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.58
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.67
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.53
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.65
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.58
  - name: Obsidian Shard
    pick_rate: 0.05
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.55
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 0.25
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.56
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.56
  - name: Pendulum of the Ages
    pick_rate: 0.15
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-09-19'
  god_win_rate: 0.5228915662650603
  god_matches_won: 217
  god_matches_played: 415
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-19'
  god_matches_analyzed: 12806
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Spear of Desolation, Kinetic Cuirass,
    Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Spear of the Magus, Shifter''s
    Shield, Helm of Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye
    of Providence, Draconic Scale, Stone of Binding, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, Magi''s Cloak, Midgardian Mail,
    Dreamer''s Idol, Chronos'' Pendant, The World Stone.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.12
      fit: 0.51
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.48
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.13
      fit: 0.37
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.64
      pick: 0.15
      fit: 0.47
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Amanita Charm, Breastplate of Valor, Spear of Desolation, Gluttonous
    Grimoire, Kinetic Cuirass, Spear of the Magus, Soul Gem, Helm of Radiance, Shifter''s
    Shield, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet, Death
    Metal, Shield of the Phoenix, Jade Scepter, Erosion, Eye of Providence, Stone
    of Binding, Draconic Scale, Triton''s Conch, Screeching Gargoyle, Daybreak Gavel,
    Chronos'' Pendant, The World Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.14
      fit: 0.28
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.33
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.13
      fit: 0.37
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.15
      fit: 0.41
    Wish-Granting Pearl:
      total: 0.48
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Breastplate of Valor
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Amanita Charm, Spear of Desolation, Breastplate of Valor,
    Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Spear of the Magus, Helm of Radiance,
    Shifter''s Shield, Shield of the Phoenix, Doom Orb, Rod of Asclepius, Erosion,
    Screeching Gargoyle, Eye of Providence, Stone of Binding, Draconic Scale, Dreamer''s
    Idol, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Ancient
    Signet, Chronos'' Pendant, The World Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.14
      fit: 0.27
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.54
      pick: 0.12
      fit: 0.49
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.39
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.13
      fit: 0.35
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
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
    Asclepius, Gluttonous Grimoire, Spear of Desolation, Kinetic Cuirass, Breastplate
    of Valor, Ethereal Staff, Spear of the Magus, Shifter''s Shield, Helm of Radiance,
    Sphere of Negation, Yogi''s Necklace, Chandra''s Grace, Erosion, Eye of Providence,
    Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Glorious Pridwen, Chronos'' Pendant.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.12
      fit: 0.51
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.44
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.13
      fit: 0.37
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.64
      pick: 0.15
      fit: 0.47
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Gluttonous Grimoire
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Freya's Tears
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Spear of Desolation, Gluttonous Grimoire, Amanita
    Charm, Soul Gem, Spear of the Magus, Stone of Binding, Screeching Gargoyle, Breastplate
    of Valor, Kinetic Cuirass, Void Shield, Void Stone, Doom Orb, Helm of Radiance,
    Shifter''s Shield, Dreamer''s Idol, Shield of the Phoenix, Rod of Asclepius, Erosion,
    Eye of Providence, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Magi''s
    Cloak, The World Stone, Chronos'' Pendant.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.68
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.4
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.54
      pick: 0.12
      fit: 0.59
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.13
      fit: 0.48
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.64
      pick: 0.15
      fit: 0.58
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul
    Gem, Breastplate of Valor, Kinetic Cuirass, Spear of Desolation, Spear of the
    Magus, Helm of Radiance, Shifter''s Shield, Rod of Asclepius, Bragi''s Harp, Shield
    of the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion, Daybreak Gavel,
    Screeching Gargoyle, Eye of Providence, Jade Scepter, Ancient Signet, Wish-Granting
    Pearl, Doom Orb, Draconic Scale, Chronos'' Pendant.'
  slot_scores:
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
      total: 0.58
      efficiency: 0.86
      win: 0.53
      pick: 0.13
      fit: 0.22
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.64
      pick: 0.15
      fit: 0.32
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Spear of Desolation, Amanita Charm, Soul Gem, Kinetic Cuirass, Shield of the Phoenix,
    Gluttonous Grimoire, Screeching Gargoyle, Shifter''s Shield, Spear of the Magus,
    Helm of Radiance, Erosion, Gladiator''s Shield, Eye of Providence, Gem of Focus,
    Stone of Binding, Draconic Scale, Chronos'' Pendant, Rod of Asclepius, Eye of
    Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.14
      fit: 0.43
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.12
      fit: 0.53
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.56
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.53
      pick: 0.13
      fit: 0.23
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.64
      pick: 0.15
      fit: 0.33
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Spear of Desolation, Breastplate of Valor, Soul Gem, Spear of the Magus,
    Shifter''s Shield, Helm of Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius,
    Eye of Providence, Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.44
      pick: 0.2
      fit: 0.31
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.12
      fit: 0.51
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.48
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.13
      fit: 0.37
    Amanita Charm:
      total: 0.54
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
