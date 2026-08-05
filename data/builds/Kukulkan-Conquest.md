---
type: smite-build
god: Kukulkan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Squall
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.67
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.92
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.04
      win_rate: 0.64
    - name: Doom Orb
      pick_rate: 0.01
      win_rate: 0.0
  - name: Spear of Desolation
    pick_rate: 0.44
    win_rate: 0.6
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.11
      win_rate: 0.39
    - name: Polynomicon
      pick_rate: 0.06
      win_rate: 0.86
  - name: Polynomicon
    pick_rate: 0.24
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.2
      win_rate: 0.62
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.58
  - name: Rod of Tahuti
    pick_rate: 0.36
    win_rate: 0.62
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.61
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.23
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.7
    - name: Evil Eye
      pick_rate: 0.09
      win_rate: 0.5
  - name: Oracle Staff
    pick_rate: 0.08
    win_rate: 0.82
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.5
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.44
  source_url: https://smitebrain.com/gods/kukulkan/
  last_verified: '2026-08-01'
  god_win_rate: 0.5685483870967742
  god_matches_won: 141
  god_matches_played: 248
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
      total: 0.62
      efficiency: 0.52
      win: 0.6
      pick: 0.44
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
      total: 0.58
      efficiency: 0.47
      win: 0.62
      pick: 0.36
      fit: 0.79
    Obsidian Shard:
      total: 0.62
      efficiency: 0.55
      win: 0.67
      pick: 0.23
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Death Metal
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
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Death Metal, Genji''s
    Guard, The Cosmic Horror, Ethereal Staff, Chronos'' Pendant, Breastplate of Valor,
    Dreamer''s Idol, Bragi''s Harp, Triton''s Conch, Wish-Granting Pearl, The World
    Stone, Gem of Focus, Jade Scepter, Doom Orb, Bancroft''s Talon, Rod of Asclepius,
    Blood-Bound Book, Bracer of The Abyss, Shield of the Phoenix, Oni Hunter''s Garb,
    Chandra''s Grace.'
  slot_scores:
    Death Metal:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 0.78
    Spear of the Magus:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.47
      win: 0.62
      pick: 0.36
      fit: 0.56
    Obsidian Shard:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.23
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
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
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
    this god: Amanita Charm, Gluttonous Grimoire, Soul Gem, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Ethereal Staff, Eye of Providence, Chandra''s
    Grace, Oni Hunter''s Garb, Bancroft''s Talon, Genji''s Guard, Blood-Bound Book,
    Lifebinder, Spectral Armor, Wish-Granting Pearl, Jade Scepter, Shifter''s Shield,
    Phoenix Feather, Spear of the Magus, Breastplate of Valor, Yogi''s Necklace, Erosion,
    Freya''s Tears, Draconic Scale, Mantle Of Discord, Alchemist Coat.'
  slot_scores:
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
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 0.49
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.23
      fit: 0.39
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
      total: 0.62
      efficiency: 0.52
      win: 0.6
      pick: 0.44
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
      total: 0.59
      efficiency: 0.47
      win: 0.62
      pick: 0.36
      fit: 0.85
    Obsidian Shard:
      total: 0.63
      efficiency: 0.55
      win: 0.67
      pick: 0.23
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
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 0.4
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.23
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
  - Breastplate of Valor
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
      total: 0.6
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 0.86
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.23
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
      total: 0.62
      efficiency: 0.52
      win: 0.6
      pick: 0.44
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
      total: 0.62
      efficiency: 0.55
      win: 0.67
      pick: 0.23
      fit: 0.79
  starter: *id001
---
