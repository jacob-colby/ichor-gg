---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.65
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.48
    win_rate: 0.46
    alternates:
    - name: Book of Thoth
      pick_rate: 0.23
      win_rate: 0.62
    - name: Yogi's Necklace
      pick_rate: 0.12
      win_rate: 0.67
  - name: Book of Thoth
    pick_rate: 0.21
    win_rate: 0.46
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.58
    - name: Doom Orb
      pick_rate: 0.1
      win_rate: 0.5
  - name: Polynomicon
    pick_rate: 0.25
    win_rate: 0.49
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.6
  - name: Rod of Tahuti
    pick_rate: 0.3
    win_rate: 0.46
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.2
      win_rate: 0.53
    - name: Polynomicon
      pick_rate: 0.07
      win_rate: 0.8
  - name: Obsidian Shard
    pick_rate: 0.25
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.66
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.44
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.36
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.67
    - name: Void Shard
      pick_rate: 0.07
      win_rate: 0.73
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.41
    win_rate: 0.55
  - name: Conduit Gem
    pick_rate: 0.35
    win_rate: 0.46
  - name: Pendulum of the Ages
    pick_rate: 0.09
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-08-16'
  god_win_rate: 0.5216049382716049
  god_matches_won: 169
  god_matches_played: 324
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Genji's Guard
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Genji''s Guard, The Cosmic Horror, Spear
    of the Magus, Nimble Ring, Doom Orb, Chronos'' Pendant, The World Stone, Dreamer''s
    Idol, Gem of Focus, Totem of Death, Death Metal, Helm of Radiance, Blood-Bound
    Book, Rod of Asclepius, Breastplate of Valor, Bancroft''s Talon, Jade Scepter,
    Bracer of The Abyss, Ethereal Staff, Alchemist Coat, Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.21
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.46
      pick: 0.48
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.49
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.46
      pick: 0.5
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.54
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Yogi's Necklace
  - Spear of Desolation
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Gluttonous Grimoire, Soul Gem, Nimble Ring, Death Metal, The Cosmic Horror,
    Spear of the Magus, Breastplate of Valor, Doom Orb, Chronos'' Pendant, Bragi''s
    Harp, The World Stone, Bancroft''s Talon, Triton''s Conch, Helm of Radiance, Gem
    of Focus, Blood-Bound Book, Rod of Asclepius, Totem of Death, Oni Hunter''s Garb,
    Jade Scepter, Freya''s Tears.'
  slot_scores:
    Yogi's Necklace:
      total: 0.52
      efficiency: 0.57
      win: 0.67
      pick: 0.12
      fit: 0.1
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.24
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.46
      pick: 0.48
      fit: 0.61
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.46
      pick: 0.5
      fit: 0.57
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.54
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Genji''s Guard, Gluttonous Grimoire, The Cosmic Horror, Spear of
    the Magus, Nimble Ring, Death Metal, Chronos'' Pendant, Breastplate of Valor,
    Doom Orb, The World Stone, Freya''s Tears, Gem of Focus, Dreamer''s Idol, Totem
    of Death, Shield of the Phoenix, Bragi''s Harp, Helm of Radiance, Blood-Bound
    Book, Rod of Asclepius, Kinetic Cuirass, Amanita Charm, Screeching Gargoyle, Triton''s
    Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.22
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.46
      pick: 0.48
      fit: 0.78
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.58
      win: 0.49
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.46
      pick: 0.5
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.54
      fit: 0.56
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Yogi's Necklace
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Amanita Charm, Genji''s Guard, Soul Gem, Gluttonous Grimoire, Shield
    of the Phoenix, Kinetic Cuirass, Rod of Asclepius, Chandra''s Grace, Nimble Ring,
    Blood-Bound Book, Freya''s Tears, Oni Hunter''s Garb, Lifebinder, The Cosmic Horror,
    Bancroft''s Talon, Breastplate of Valor, Spear of the Magus, Phoenix Feather,
    Erosion, Shifter''s Shield, Spectral Armor, Eye of Providence, Draconic Scale,
    Helm of Radiance, Jade Scepter.'
  slot_scores:
    Yogi's Necklace:
      total: 0.54
      efficiency: 0.57
      win: 0.67
      pick: 0.12
      fit: 0.19
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.26
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.46
      pick: 0.5
      fit: 0.39
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.54
      fit: 0.39
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.49
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
  - The Cosmic Horror
  - Spear of the Magus
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
    for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear of the Magus,
    Genji''s Guard, Doom Orb, The World Stone, Nimble Ring, Dreamer''s Idol, Chronos''
    Pendant, Screeching Gargoyle, Breastplate of Valor, Death Metal, Helm of Radiance,
    Gem of Focus, Blood-Bound Book, Rod of Asclepius, Totem of Death, Bancroft''s
    Talon, Jade Scepter, Freya''s Tears, Stone of Binding, Bracer of The Abyss, Ethereal
    Staff.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.46
      pick: 0.48
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.49
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.55
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.46
      pick: 0.5
      fit: 0.85
    Obsidian Shard:
      total: 0.6
      efficiency: 0.52
      win: 0.58
      pick: 0.54
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Genji''s Guard, Gluttonous Grimoire, Soul Gem, The Cosmic
    Horror, Spear of the Magus, Bragi''s Harp, Death Metal, Bracer of The Abyss, Breastplate
    of Valor, Chronos'' Pendant, Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass,
    Amanita Charm, Helm of Radiance, Doom Orb, Freya''s Tears, Rod of Asclepius, Eye
    of Providence, Oni Hunter''s Garb, Shield of the Phoenix, Jade Scepter, Gem of
    Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.08
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.51
      win: 0.49
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.49
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.46
      efficiency: 0.42
      win: 0.49
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.46
      pick: 0.5
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
  - Obsidian Shard
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Soul Gem, Breastplate
    of Valor, Gluttonous Grimoire, Chronos'' Pendant, Freya''s Tears, Shield of the
    Phoenix, Gem of Focus, Nimble Ring, Totem of Death, The Cosmic Horror, Screeching
    Gargoyle, Chandra''s Grace, Spear of the Magus, Death Metal, Gladiator''s Shield,
    Doom Orb, Kinetic Cuirass, Prophetic Cloak, Amanita Charm, The World Stone, Helm
    of Radiance, Eye of Providence, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.48
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.49
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.46
      pick: 0.48
      fit: 0.86
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.46
      pick: 0.5
      fit: 0.37
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.54
      fit: 0.37
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Obsidian Shard
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
    Underrated for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear
    of the Magus, Nimble Ring, Chronos'' Pendant, Doom Orb, The World Stone, Genji''s
    Guard, Dreamer''s Idol, Gem of Focus, Totem of Death, Death Metal, Helm of Radiance,
    Blood-Bound Book, Rod of Asclepius, Breastplate of Valor, Bancroft''s Talon, Jade
    Scepter, Bracer of The Abyss, Ethereal Staff, Alchemist Coat, Freya''s Tears.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.46
      pick: 0.48
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.49
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.54
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.46
      pick: 0.5
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.54
      fit: 0.79
  starter: *id001
---
