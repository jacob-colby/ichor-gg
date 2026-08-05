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
    Dreamer''s Idol, The World Stone, Genji''s Guard, Gem of Focus, Death Metal, Rod
    of Asclepius, Blood-Bound Book, Helm of Radiance, Bancroft''s Talon, Jade Scepter,
    Breastplate of Valor, Bracer of The Abyss, Wish-Granting Pearl, Ethereal Staff,
    Ancient Signet, Chronos'' Pendant, Alchemist Coat, Typhon’s Heart, Doom Orb.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.63
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.44
      win: 0.62
      pick: 0.36
      fit: 0.79
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.67
      pick: 0.23
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Soul Reaver
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
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Genji''s
    Guard, Death Metal, Breastplate of Valor, Dreamer''s Idol, The World Stone, Gem
    of Focus, Bragi''s Harp, Rod of Asclepius, Freya''s Tears, Blood-Bound Book, Helm
    of Radiance, Bancroft''s Talon, Shield of the Phoenix, Jade Scepter, Amanita Charm,
    Triton''s Conch, Bracer of The Abyss, Oni Hunter''s Garb, Chronos'' Pendant, Doom
    Orb.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 0.78
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Reaver:
      total: 0.51
      efficiency: 0.46
      win: 0.67
      pick: 0.06
      fit: 0.32
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.44
      win: 0.62
      pick: 0.36
      fit: 0.56
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.67
      pick: 0.23
      fit: 0.56
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Eye of Providence, Genji''s Guard, Oni Hunter''s
    Garb, Blood-Bound Book, Bancroft''s Talon, Lifebinder, Chandra''s Grace, Spear
    of the Magus, Shifter''s Shield, Breastplate of Valor, Freya''s Tears, The Cosmic
    Horror, Phoenix Feather, Spectral Armor, Jade Scepter, Erosion, Helm of Radiance,
    Yogi''s Necklace, Draconic Scale, Wish-Granting Pearl.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.51
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 0.49
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.23
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.89
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
    Dreamer''s Idol, The World Stone, Genji''s Guard, Screeching Gargoyle, Death Metal,
    Rod of Asclepius, Breastplate of Valor, Blood-Bound Book, Helm of Radiance, Bancroft''s
    Talon, Gem of Focus, Jade Scepter, Bracer of The Abyss, Wish-Granting Pearl, Amanita
    Charm, Ethereal Staff, Ancient Signet, Chronos'' Pendant, Doom Orb.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.63
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.44
      win: 0.62
      pick: 0.36
      fit: 0.85
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
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
  - Bragi's Harp
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
    this god: Gluttonous Grimoire, Soul Gem, Genji''s Guard, Spear of the Magus, Bracer
    of The Abyss, Bragi''s Harp, Death Metal, The Cosmic Horror, Nimble Ring, Breastplate
    of Valor, Blood-Bound Book, Bancroft''s Talon, Rod of Asclepius, Amanita Charm,
    Oni Hunter''s Garb, Helm of Radiance, Yogi''s Necklace, Kinetic Cuirass, Jade
    Scepter, Dreamer''s Idol, The World Stone, Freya''s Tears, Eye of Providence,
    Chronos'' Pendant, Doom Orb.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 0.4
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.67
      pick: 0.23
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Rod of Tahuti
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
    Grimoire, Breastplate of Valor, Freya''s Tears, Shield of the Phoenix, Gem of
    Focus, Spear of the Magus, The Cosmic Horror, Screeching Gargoyle, Chandra''s
    Grace, Death Metal, Chronos'' Pendant, Gladiator''s Shield, Amanita Charm, Rod
    of Asclepius, Oni Hunter''s Garb, Dreamer''s Idol, The World Stone, Yogi''s Necklace,
    Blood-Bound Book, Kinetic Cuirass, Helm of Radiance, Bancroft''s Talon, Doom Orb.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 0.86
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.44
      win: 0.62
      pick: 0.36
      fit: 0.37
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.23
      fit: 0.37
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The
    Cosmic Horror, Chronos'' Pendant, Dreamer''s Idol, The World Stone, Doom Orb,
    Genji''s Guard, Gem of Focus, Death Metal, Rod of Asclepius, Blood-Bound Book,
    Helm of Radiance, Bancroft''s Talon, Jade Scepter, Breastplate of Valor, Bracer
    of The Abyss, Wish-Granting Pearl, Ethereal Staff, Ancient Signet, Alchemist Coat,
    Typhon’s Heart.'
  slot_scores:
    Chronos' Pendant:
      total: 0.47
      efficiency: 0.56
      win: 0.39
      pick: 0.11
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.63
      efficiency: 0.52
      win: 0.6
      pick: 0.44
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.67
      pick: 0.23
      fit: 0.79
  starter: *id001
---
