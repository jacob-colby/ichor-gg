---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.71
  aspect_win_rate: 0.52
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.15
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.54
    - name: Daybreak Gavel
      pick_rate: 0.09
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.54
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.41
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.47
    - name: Alchemist Coat
      pick_rate: 0.05
      win_rate: 0.53
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.62
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.56
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.05
      win_rate: 0.63
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.67
  - name: Veve Charm
    pick_rate: 0.05
    win_rate: 0.6
    alternates:
    - name: Shield
      pick_rate: 0.04
      win_rate: 0.38
    - name: Oracle Staff
      pick_rate: 0.04
      win_rate: 0.43
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.45
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.52
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-08-22'
  god_win_rate: 0.5070754716981132
  god_matches_won: 215
  god_matches_played: 424
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Obsidian Shard, Amanita Charm, Kinetic Cuirass, Spear
    of Desolation, Gluttonous Grimoire, Soul Gem, Breastplate of Valor, Spear of the
    Magus, Helm of Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye
    of Providence, Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.48
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.15
      fit: 0.51
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.48
      pick: 0.17
      fit: 0.37
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.63
      pick: 0.11
      fit: 0.47
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.49
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Freya''s
    Tears, Obsidian Shard, Amanita Charm, Gluttonous Grimoire, Spear of Desolation,
    Kinetic Cuirass, Breastplate of Valor, Spear of the Magus, Soul Gem, Helm of Radiance,
    Daybreak Gavel, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet,
    The World Stone, Death Metal, Chronos'' Pendant, Shield of the Phoenix, Jade Scepter,
    Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Triton''s Conch,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.19
      fit: 0.28
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.51
      pick: 0.14
      fit: 0.28
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.33
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.48
      pick: 0.17
      fit: 0.37
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.63
      pick: 0.11
      fit: 0.41
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
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
    god: Freya''s Tears, Obsidian Shard, Amanita Charm, Spear of Desolation, Gluttonous
    Grimoire, Soul Gem, Kinetic Cuirass, Spear of the Magus, Breastplate of Valor,
    Helm of Radiance, Daybreak Gavel, Shield of the Phoenix, Doom Orb, Rod of Asclepius,
    Erosion, Chronos'' Pendant, The World Stone, Screeching Gargoyle, Eye of Providence,
    Stone of Binding, Draconic Scale, Dreamer''s Idol, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.19
      fit: 0.27
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.39
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.15
      fit: 0.49
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.48
      pick: 0.17
      fit: 0.35
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.63
      pick: 0.11
      fit: 0.45
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Soul Gem, Obsidian Shard, Shield of the
    Phoenix, Rod of Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation,
    Ethereal Staff, Spear of the Magus, Breastplate of Valor, Lifebinder, Helm of
    Radiance, Sphere of Negation, Yogi''s Necklace, Chandra''s Grace, Erosion, Eye
    of Providence, Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl,
    Blood-Bound Book, Glorious Pridwen, Chronos'' Pendant.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.44
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.48
      pick: 0.17
      fit: 0.37
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.63
      pick: 0.11
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
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Gluttonous Grimoire
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
    for this god: Freya''s Tears, Obsidian Shard, Spear of Desolation, Gluttonous
    Grimoire, Amanita Charm, Soul Gem, Spear of the Magus, Stone of Binding, Screeching
    Gargoyle, Kinetic Cuirass, Void Shield, Breastplate of Valor, Void Stone, Doom
    Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Shield of the Phoenix,
    Rod of Asclepius, Erosion, Eye of Providence, Draconic Scale, Chronos'' Pendant,
    Jade Scepter, Wish-Granting Pearl, Magi''s Cloak.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.68
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.54
      pick: 0.15
      fit: 0.59
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.48
      pick: 0.17
      fit: 0.48
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.63
      pick: 0.11
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
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
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Obsidian Shard, Gluttonous Grimoire, Nimble Ring, Amanita
    Charm, Soul Gem, Kinetic Cuirass, Spear of Desolation, Breastplate of Valor, Spear
    of the Magus, Daybreak Gavel, Helm of Radiance, Rod of Asclepius, Bragi''s Harp,
    Shield of the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion, Chronos''
    Pendant, Screeching Gargoyle, Eye of Providence, Jade Scepter, Ancient Signet,
    Wish-Granting Pearl, Doom Orb, Draconic Scale.'
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
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.28
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.48
      pick: 0.17
      fit: 0.22
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.63
      pick: 0.11
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Spear of Desolation,
    Amanita Charm, Breastplate of Valor, Obsidian Shard, Soul Gem, Kinetic Cuirass,
    Shield of the Phoenix, Gluttonous Grimoire, Screeching Gargoyle, Chronos'' Pendant,
    Daybreak Gavel, Spear of the Magus, Helm of Radiance, Prophetic Cloak, Erosion,
    Gladiator''s Shield, Eye of Providence, Gem of Focus, Stone of Binding, Draconic
    Scale, Rod of Asclepius, Eye of Erebus, Magi''s Cloak, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.19
      fit: 0.43
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.51
      pick: 0.14
      fit: 0.43
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.56
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.15
      fit: 0.53
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.63
      pick: 0.11
      fit: 0.33
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
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
    Underrated for this god: Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous
    Grimoire, Spear of Desolation, Breastplate of Valor, Soul Gem, Spear of the Magus,
    Helm of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion, Rod of Asclepius,
    Eye of Providence, Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.48
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.15
      fit: 0.51
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.48
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.49
  starter: *id001
---
