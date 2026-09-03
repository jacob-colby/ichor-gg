---
type: smite-build
god: Merlin
mode: Conquest
builds:
- source: community
  aspect: Aspect of Pandemonium
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.41
  slot_order:
  - name: Chronos' Pendant
    pick_rate: 0.3
    win_rate: 0.5
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.47
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.49
  - name: Soul Reaver
    pick_rate: 0.19
    win_rate: 0.48
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.15
      win_rate: 0.47
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.53
  - name: Soul Gem
    pick_rate: 0.19
    win_rate: 0.45
    alternates:
    - name: Totem of Death
      pick_rate: 0.12
      win_rate: 0.43
    - name: Ethereal Staff
      pick_rate: 0.1
      win_rate: 0.53
  - name: Rod of Tahuti
    pick_rate: 0.25
    win_rate: 0.51
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.16
      win_rate: 0.53
    - name: Omen Drum
      pick_rate: 0.11
      win_rate: 0.56
  - name: Obsidian Shard
    pick_rate: 0.19
    win_rate: 0.54
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.62
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.43
  - name: Evil Eye
    pick_rate: 0.16
    win_rate: 0.47
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.56
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.6
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.38
  - name: Pendulum of the Ages
    pick_rate: 0.2
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/merlin/
  last_verified: '2026-09-03'
  god_win_rate: 0.48928974069898534
  god_matches_won: 434
  god_matches_played: 887
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-03'
  god_matches_analyzed: 10626
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone,
    Dreamer''s Idol, Gem of Focus, Ancient Signet, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble
    Ring.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.3
      fit: 0.63
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.47
      pick: 0.26
      fit: 1.0
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.54
      pick: 0.41
      fit: 0.89
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.45
      pick: 0.3
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, Doom Orb, The World Stone, Death Metal, Gluttonous Grimoire, Ancient
    Signet, Dreamer''s Idol, Bragi''s Harp, Gem of Focus, Polynomicon, Rod of Asclepius,
    Bancroft''s Talon, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine Ruin,
    Wish-Granting Pearl, Helm of Radiance, Breastplate of Valor.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.49
      pick: 0.16
      fit: 0.39
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.47
      pick: 0.26
      fit: 0.61
    Doom Orb:
      total: 0.49
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.57
    The World Stone:
      total: 0.49
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.57
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.54
      pick: 0.41
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone, Dreamer''s
    Idol, Death Metal, Gem of Focus, Ancient Signet, Bragi''s Harp, Rod of Asclepius,
    Polynomicon, Blood-Bound Book, Jade Scepter, Divine Ruin, Triton''s Conch, Breastplate
    of Valor, Bancroft''s Talon, Genji''s Guard, Helm of Radiance.'
  slot_scores:
    Chronos' Pendant:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.3
      fit: 0.44
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.47
      pick: 0.26
      fit: 0.78
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.54
      pick: 0.41
      fit: 0.66
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.45
      pick: 0.3
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Freya''s Tears, Spear of the Magus, Shifter''s Shield, Genji''s
    Guard, Breastplate of Valor, Lifebinder, Helm of Radiance, Sphere of Negation,
    Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale, Phoenix Feather,
    Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound Book, Doom Orb,
    Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.48
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.47
      pick: 0.26
      fit: 0.49
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.39
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.54
      pick: 0.41
      fit: 0.49
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.45
      pick: 0.3
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone,
    Dreamer''s Idol, Ancient Signet, Gem of Focus, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Screeching Gargoyle, Wish-Granting Pearl, Typhon’s Heart, Breastplate of Valor,
    Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.47
      pick: 0.26
      fit: 1.0
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.85
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.54
      pick: 0.41
      fit: 0.95
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.45
      pick: 0.3
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Doom Orb, The World Stone, Ancient Signet, Blood-Bound Book,
    Dreamer''s Idol, Death Metal, Bancroft''s Talon, Gem of Focus, Rod of Asclepius,
    Typhon’s Heart, Polynomicon, Jade Scepter, Divine Ruin, Helm of Radiance, Daybreak
    Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.48
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.32
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.54
      pick: 0.41
      fit: 0.42
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.45
      pick: 0.3
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Gem of Focus
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Gem of Focus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gem of Focus, Spear of the Magus,
    Gluttonous Grimoire, Doom Orb, The World Stone, Breastplate of Valor, Dreamer''s
    Idol, Genji''s Guard, Ancient Signet, Death Metal, Staff of Myrddin, Eye of Erebus,
    Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Chandra''s Grace, Freya''s
    Tears, Polynomicon, Blood-Bound Book, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.3
      fit: 0.63
    Gem of Focus:
      total: 0.49
      efficiency: 0.5
      win: 0.48
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.47
      pick: 0.26
      fit: 0.86
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.37
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.54
      pick: 0.41
      fit: 0.47
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.45
      pick: 0.3
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, The
    World Stone, Dreamer''s Idol, Gem of Focus, Ancient Signet, Rod of Asclepius,
    Polynomicon, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm
    of Radiance, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of
    The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.47
      pick: 0.26
      fit: 1.0
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.54
      pick: 0.41
      fit: 0.89
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.45
      pick: 0.3
      fit: 1.0
  starter: *id001
---
