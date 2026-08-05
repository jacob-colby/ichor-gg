---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.56
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.2
      win_rate: 0.44
    - name: Yogi's Necklace
      pick_rate: 0.11
      win_rate: 0.43
  - name: Book of Thoth
    pick_rate: 0.29
    win_rate: 0.47
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.19
      win_rate: 0.44
    - name: Doom Orb
      pick_rate: 0.15
      win_rate: 0.59
  - name: Polynomicon
    pick_rate: 0.31
    win_rate: 0.49
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.17
      win_rate: 0.53
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.47
  - name: Rod of Tahuti
    pick_rate: 0.35
    win_rate: 0.54
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.24
      win_rate: 0.52
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.45
  - name: Obsidian Shard
    pick_rate: 0.21
    win_rate: 0.59
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.51
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.52
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.47
    - name: Soul Gem
      pick_rate: 0.07
      win_rate: 0.31
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-08-01'
  god_win_rate: 0.5107758620689655
  god_matches_won: 237
  god_matches_played: 464
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
  - The Cosmic Horror
  - Rod of Tahuti
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
    this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror,
    Ethereal Staff, Dreamer''s Idol, Chronos'' Pendant, The World Stone, Doom Orb,
    Genji''s Guard, Death Metal, Wish-Granting Pearl, Jade Scepter, Gem of Focus,
    Bancroft''s Talon, Rod of Asclepius, Blood-Bound Book, Bracer of The Abyss, Helm
    of Radiance, Alchemist Coat, Breastplate of Valor, Bragi''s Harp, Soul Reaver.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.47
      win: 0.54
      pick: 0.35
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.55
      win: 0.59
      pick: 0.21
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Death Metal
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Death Metal
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
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Death Metal, Genji''s
    Guard, The Cosmic Horror, Ethereal Staff, Chronos'' Pendant, Breastplate of Valor,
    Dreamer''s Idol, Bragi''s Harp, Triton''s Conch, Wish-Granting Pearl, The World
    Stone, Gem of Focus, Jade Scepter, Doom Orb, Bancroft''s Talon, Rod of Asclepius,
    Blood-Bound Book, Bracer of The Abyss, Shield of the Phoenix, Oni Hunter''s Garb,
    Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.22
    Death Metal:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 0.78
    Spear of the Magus:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.59
      pick: 0.21
      fit: 0.56
    Soul Gem:
      total: 0.57
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Soul Gem, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Ethereal Staff, Eye of Providence, Chandra''s
    Grace, Oni Hunter''s Garb, Bancroft''s Talon, Genji''s Guard, Blood-Bound Book,
    Lifebinder, Spectral Armor, Wish-Granting Pearl, Jade Scepter, Shifter''s Shield,
    Phoenix Feather, Spear of the Magus, Breastplate of Valor, Yogi''s Necklace, Erosion,
    Freya''s Tears, Draconic Scale, Mantle Of Discord, Alchemist Coat.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.61
    Ethereal Staff:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.81
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
  - The Cosmic Horror
  - Rod of Tahuti
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
    Dreamer''s Idol, The World Stone, Doom Orb, Ethereal Staff, Genji''s Guard, Chronos''
    Pendant, Death Metal, Wish-Granting Pearl, Jade Scepter, Bancroft''s Talon, Rod
    of Asclepius, Blood-Bound Book, Bracer of The Abyss, Breastplate of Valor, Gem
    of Focus, Screeching Gargoyle, Helm of Radiance, Alchemist Coat, Oni Hunter''s
    Garb.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.62
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.57
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.47
      win: 0.54
      pick: 0.35
      fit: 0.85
    Obsidian Shard:
      total: 0.6
      efficiency: 0.55
      win: 0.59
      pick: 0.21
      fit: 0.85
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
      total: 0.51
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 0.4
    Obsidian Shard:
      total: 0.51
      efficiency: 0.55
      win: 0.59
      pick: 0.21
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
  - Chronos' Pendant
  - Obsidian Shard
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
    Grimoire, Breastplate of Valor, Chronos'' Pendant, Shield of the Phoenix, Gem
    of Focus, Chandra''s Grace, Freya''s Tears, Spear of the Magus, Death Metal, Ethereal
    Staff, Screeching Gargoyle, The Cosmic Horror, Gladiator''s Shield, Oni Hunter''s
    Garb, Wish-Granting Pearl, Jade Scepter, Yogi''s Necklace, Bragi''s Harp, Bancroft''s
    Talon, Rod of Asclepius, Blood-Bound Book, Dreamer''s Idol, Kinetic Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 0.86
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.59
      pick: 0.21
      fit: 0.37
    Soul Gem:
      total: 0.59
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Ethereal Staff
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
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The
    Cosmic Horror, Ethereal Staff, Dreamer''s Idol, Chronos'' Pendant, The World Stone,
    Doom Orb, Genji''s Guard, Death Metal, Wish-Granting Pearl, Jade Scepter, Gem
    of Focus, Bancroft''s Talon, Rod of Asclepius, Blood-Bound Book, Bracer of The
    Abyss, Helm of Radiance, Alchemist Coat, Breastplate of Valor, Bragi''s Harp,
    Soul Reaver.'
  slot_scores:
    Ethereal Staff:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.55
      win: 0.59
      pick: 0.21
      fit: 0.79
  starter: *id001
---
