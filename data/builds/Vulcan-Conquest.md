---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.49
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.45
    win_rate: 0.58
    alternates:
    - name: Book of Thoth
      pick_rate: 0.37
      win_rate: 0.62
    - name: Doom Orb
      pick_rate: 0.04
      win_rate: 0.31
  - name: Book of Thoth
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.59
    - name: Doom Orb
      pick_rate: 0.14
      win_rate: 0.64
  - name: Rod of Tahuti
    pick_rate: 0.22
    win_rate: 0.59
    alternates:
    - name: Soul Gem
      pick_rate: 0.21
      win_rate: 0.61
    - name: The World Stone
      pick_rate: 0.08
      win_rate: 0.74
  - name: Obsidian Shard
    pick_rate: 0.26
    win_rate: 0.6
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.32
      win_rate: 0.66
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.53
  - name: Evil Eye
    pick_rate: 0.13
    win_rate: 0.56
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.21
      win_rate: 0.71
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.65
  - name: Killing Stone
    pick_rate: 0.09
    win_rate: 0.77
    alternates:
    - name: Evil Eye
      pick_rate: 0.12
      win_rate: 0.61
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.83
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-08-01'
  god_win_rate: 0.5679012345679012
  god_matches_won: 184
  god_matches_played: 324
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - The Cosmic Horror
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror,
    Ethereal Staff, Bracer of The Abyss, Chronos'' Pendant, Genji''s Guard, Dreamer''s
    Idol, Death Metal, Wish-Granting Pearl, Bragi''s Harp, Jade Scepter, Bancroft''s
    Talon, The World Stone, Rod of Asclepius, Blood-Bound Book, Nimble Ring, Doom
    Orb, Gem of Focus, Breastplate of Valor, Helm of Radiance, Alchemist Coat, Polynomicon.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.76
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.45
      fit: 0.83
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.47
      win: 0.59
      pick: 0.22
      fit: 0.66
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.26
      fit: 0.66
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, Genji''s Guard, Death
    Metal, The Cosmic Horror, Ethereal Staff, Bragi''s Harp, Chronos'' Pendant, Breastplate
    of Valor, Bracer of The Abyss, Dreamer''s Idol, Triton''s Conch, Wish-Granting
    Pearl, Jade Scepter, Bancroft''s Talon, Gem of Focus, Rod of Asclepius, Blood-Bound
    Book, The World Stone, Oni Hunter''s Garb, Doom Orb, Shield of the Phoenix, Yogi''s
    Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.2
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.58
      pick: 0.45
      fit: 0.7
    Spear of the Magus:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.47
      win: 0.59
      pick: 0.22
      fit: 0.5
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.26
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Ethereal Staff, Chandra''s Grace, Eye of Providence,
    Oni Hunter''s Garb, Bancroft''s Talon, Blood-Bound Book, Genji''s Guard, Lifebinder,
    Spectral Armor, Wish-Granting Pearl, Jade Scepter, Shifter''s Shield, Phoenix
    Feather, Breastplate of Valor, Yogi''s Necklace, Spear of the Magus, Erosion,
    Freya''s Tears, Mantle Of Discord, Draconic Scale, Alchemist Coat.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.56
    Ethereal Staff:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.37
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.45
      fit: 0.45
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.26
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.57
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - The Cosmic Horror
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror,
    Dreamer''s Idol, The World Stone, Ethereal Staff, Doom Orb, Genji''s Guard, Bracer
    of The Abyss, Chronos'' Pendant, Death Metal, Wish-Granting Pearl, Jade Scepter,
    Bancroft''s Talon, Rod of Asclepius, Blood-Bound Book, Bragi''s Harp, Breastplate
    of Valor, Screeching Gargoyle, Nimble Ring, Gem of Focus, Helm of Radiance, Oni
    Hunter''s Garb.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.58
      pick: 0.45
      fit: 0.88
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.75
    Spear of the Magus:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.47
      win: 0.59
      pick: 0.22
      fit: 0.75
    Obsidian Shard:
      total: 0.59
      efficiency: 0.55
      win: 0.6
      pick: 0.26
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Spear of Desolation
  - Obsidian Shard
  flex_slots:
  - Bracer of The Abyss
  - Nimble Ring
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Bragi''s Harp, Bracer of The Abyss, Ethereal
    Staff, Genji''s Guard, Death Metal, Nimble Ring, Spear of the Magus, Bancroft''s
    Talon, Blood-Bound Book, The Cosmic Horror, Wish-Granting Pearl, Breastplate of
    Valor, Jade Scepter, Oni Hunter''s Garb, Rod of Asclepius, Chronos'' Pendant,
    Yogi''s Necklace, Kinetic Cuirass, Triton''s Conch, Amanita Charm, Helm of Radiance,
    Typhon’s Heart, Spectral Armor.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.45
      fit: 0.4
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.26
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Chronos' Pendant
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Gluttonous
    Grimoire, Breastplate of Valor, Chronos'' Pendant, Shield of the Phoenix, Chandra''s
    Grace, Gem of Focus, Freya''s Tears, Spear of the Magus, Ethereal Staff, Death
    Metal, The Cosmic Horror, Bragi''s Harp, Screeching Gargoyle, Bracer of The Abyss,
    Oni Hunter''s Garb, Wish-Granting Pearl, Yogi''s Necklace, Jade Scepter, Gladiator''s
    Shield, Kinetic Cuirass, Bancroft''s Talon, Rod of Asclepius, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.43
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.58
      pick: 0.45
      fit: 0.76
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.26
      fit: 0.33
    Soul Gem:
      total: 0.57
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  flex_slots:
  - Ethereal Staff
  - Bracer of The Abyss
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The
    Cosmic Horror, Ethereal Staff, Bracer of The Abyss, Chronos'' Pendant, Genji''s
    Guard, Dreamer''s Idol, Death Metal, Wish-Granting Pearl, Bragi''s Harp, Jade
    Scepter, Bancroft''s Talon, The World Stone, Rod of Asclepius, Blood-Bound Book,
    Nimble Ring, Doom Orb, Gem of Focus, Breastplate of Valor, Helm of Radiance, Alchemist
    Coat, Polynomicon.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.51
    Ethereal Staff:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.76
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.45
      fit: 0.83
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
---
