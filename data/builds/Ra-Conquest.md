---
type: smite-build
god: Ra
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thermotherapy
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.52
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.51
    win_rate: 0.57
    alternates:
    - name: Book of Thoth
      pick_rate: 0.25
      win_rate: 0.52
    - name: Shifter's Shield
      pick_rate: 0.05
      win_rate: 0.52
  - name: The World Stone
    pick_rate: 0.3
    win_rate: 0.56
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.51
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.48
  - name: Soul Gem
    pick_rate: 0.22
    win_rate: 0.62
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.57
    - name: The World Stone
      pick_rate: 0.11
      win_rate: 0.54
  - name: Rod of Tahuti
    pick_rate: 0.28
    win_rate: 0.51
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.21
      win_rate: 0.62
    - name: Nimble Ring
      pick_rate: 0.13
      win_rate: 0.59
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.71
    - name: Nimble Ring
      pick_rate: 0.14
      win_rate: 0.67
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.47
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.75
    - name: Void Shard
      pick_rate: 0.07
      win_rate: 0.27
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.26
    win_rate: 0.6
  - name: Sands Of Time
    pick_rate: 0.21
    win_rate: 0.43
  - name: Archmage's Gem
    pick_rate: 0.2
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/ra/
  last_verified: '2026-08-15'
  god_win_rate: 0.5379310344827586
  god_matches_won: 234
  god_matches_played: 435
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Chronos''
    Pendant, Genji''s Guard, Gem of Focus, Totem of Death, Doom Orb, Breastplate of
    Valor, Dreamer''s Idol, Death Metal, Helm of Radiance, Blood-Bound Book, Rod of
    Asclepius, Freya''s Tears, Bancroft''s Talon, Jade Scepter, Shield of the Phoenix,
    Bracer of The Abyss, Ethereal Staff, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.55
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.72
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.72
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.56
      pick: 0.35
      fit: 0.72
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Death Metal
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - The World Stone
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Death Metal, Genji''s Guard, The Cosmic Horror, Spear of the Magus,
    Breastplate of Valor, Chronos'' Pendant, Doom Orb, Bragi''s Harp, Bancroft''s
    Talon, Triton''s Conch, Helm of Radiance, Gem of Focus, Blood-Bound Book, Rod
    of Asclepius, Totem of Death, Oni Hunter''s Garb, Polynomicon, Jade Scepter, Freya''s
    Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.24
    Death Metal:
      total: 0.52
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.61
    The World Stone:
      total: 0.52
      efficiency: 0.46
      win: 0.56
      pick: 0.41
      fit: 0.57
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.57
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Genji''s Guard,
    Death Metal, Chronos'' Pendant, Breastplate of Valor, Doom Orb, Freya''s Tears,
    Gem of Focus, Dreamer''s Idol, Totem of Death, Shield of the Phoenix, Bragi''s
    Harp, Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Amanita
    Charm, Screeching Gargoyle, Triton''s Conch.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.78
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.56
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.35
      fit: 0.56
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Kinetic Cuirass,
    Rod of Asclepius, Genji''s Guard, Chandra''s Grace, Freya''s Tears, Breastplate
    of Valor, Blood-Bound Book, Oni Hunter''s Garb, Lifebinder, Bancroft''s Talon,
    Phoenix Feather, The Cosmic Horror, Erosion, Spectral Armor, Spear of the Magus,
    Eye of Providence, Shifter''s Shield, Draconic Scale, Helm of Radiance, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.6
    Nimble Ring:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.3
      fit: 0.2
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.5
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.36
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom
    Orb, Dreamer''s Idol, Genji''s Guard, Chronos'' Pendant, Screeching Gargoyle,
    Breastplate of Valor, Gem of Focus, Death Metal, Totem of Death, Helm of Radiance,
    Freya''s Tears, Blood-Bound Book, Rod of Asclepius, Bancroft''s Talon, Shield
    of the Phoenix, Jade Scepter, Stone of Binding, Kinetic Cuirass.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.81
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.81
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.81
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.56
      pick: 0.35
      fit: 0.81
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Genji''s Guard, The Cosmic Horror, Spear of the
    Magus, Breastplate of Valor, Death Metal, Bragi''s Harp, Bracer of The Abyss,
    Chronos'' Pendant, Blood-Bound Book, Freya''s Tears, Bancroft''s Talon, Kinetic
    Cuirass, Amanita Charm, Helm of Radiance, Rod of Asclepius, Eye of Providence,
    Shield of the Phoenix, Oni Hunter''s Garb, Gem of Focus, Jade Scepter, Totem of
    Death.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.63
      efficiency: 0.68
      win: 0.67
      pick: 0.3
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.42
      win: 0.54
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.41
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.29
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Chronos'' Pendant, Gluttonous Grimoire, Freya''s Tears, Shield of the Phoenix,
    Gem of Focus, Totem of Death, Screeching Gargoyle, Chandra''s Grace, The Cosmic
    Horror, Spear of the Magus, Death Metal, Gladiator''s Shield, Prophetic Cloak,
    Kinetic Cuirass, Amanita Charm, Helm of Radiance, Eye of Providence, Doom Orb,
    Oni Hunter''s Garb, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.5
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.85
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.35
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the
    Magus, Chronos'' Pendant, Genji''s Guard, Gem of Focus, Totem of Death, Doom Orb,
    Breastplate of Valor, Dreamer''s Idol, Death Metal, Helm of Radiance, Blood-Bound
    Book, Rod of Asclepius, Freya''s Tears, Bancroft''s Talon, Jade Scepter, Shield
    of the Phoenix, Bracer of The Abyss, Ethereal Staff, Alchemist Coat.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.55
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.72
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.72
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Genji''s Guard,
    Shield of the Phoenix, Chandra''s Grace, Lifebinder, Erosion, Spectral Armor,
    Kinetic Cuirass, Doublet of Binding, Freya''s Tears, Oni Hunter''s Garb, Void
    Stone, The Cosmic Horror, Breastplate of Valor, Spear of the Magus, Screeching
    Gargoyle, Void Shield, Chronos'' Pendant, Triton''s Conch, Phoenix Feather, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.65
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.39
    Spectral Armor:
      total: 0.52
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.49
    Erosion:
      total: 0.52
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Genji's Guard
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Triton's Conch
  flex_slots:
  - Death Metal
  - Bancroft's Talon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Rod of Asclepius, Gluttonous Grimoire, Genji''s Guard, Lifebinder, Triton''s
    Conch, Death Metal, Bancroft''s Talon, Spectral Armor, The Cosmic Horror, Shield
    of the Phoenix, Spear of the Magus, Blood-Bound Book, Oni Hunter''s Garb, Erosion,
    Breastplate of Valor, Kinetic Cuirass, Chandra''s Grace, Doublet of Binding, Chronos''
    Pendant, Void Stone, Void Shield.'
  slot_scores:
    Bancroft's Talon:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.52
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.28
    Death Metal:
      total: 0.51
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.5
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.47
    Triton's Conch:
      total: 0.53
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.87
  starter: *id001
  aspect: Aspect of Thermotherapy
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
  - Obsidian Shard
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Genji''s Guard, Lifebinder,
    Shield of the Phoenix, The Cosmic Horror, Triton''s Conch, Spear of the Magus,
    Spectral Armor, Chandra''s Grace, Erosion, Kinetic Cuirass, Death Metal, Breastplate
    of Valor, Doublet of Binding, Blood-Bound Book, Freya''s Tears, Chronos'' Pendant,
    Oni Hunter''s Garb, Bancroft''s Talon, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.62
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.45
    Obsidian Shard:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.35
      fit: 0.45
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Rod of Tahuti
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Spectral Armor
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Erosion, Gluttonous
    Grimoire, Kinetic Cuirass, Spectral Armor, Lifebinder, Genji''s Guard, Chandra''s
    Grace, Freya''s Tears, Void Shield, Doublet of Binding, Breastplate of Valor,
    Oni Hunter''s Garb, Umbral Link, Stampede, Void Stone, Phoenix Feather, Eye of
    Providence, Shifter''s Shield, Draconic Scale, Mystical Mail, Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.67
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.26
    Spectral Armor:
      total: 0.55
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.69
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.87
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Stone
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Void Stone,
    The Cosmic Horror, Genji''s Guard, Void Shield, Spear of the Magus, Screeching
    Gargoyle, Shield of the Phoenix, Lifebinder, Spectral Armor, Erosion, Chandra''s
    Grace, Kinetic Cuirass, Doublet of Binding, Oni Hunter''s Garb, Breastplate of
    Valor, Freya''s Tears, Doom Orb, Stone of Binding.'
  slot_scores:
    Void Stone:
      total: 0.54
      efficiency: 0.43
      win: 0.54
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.74
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.56
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.35
      fit: 0.56
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Asclepius, Gluttonous Grimoire, Genji''s Guard,
    Spectral Armor, Shield of the Phoenix, Lifebinder, Erosion, Kinetic Cuirass, Chandra''s
    Grace, Doublet of Binding, Umbral Link, Blood-Bound Book, Breastplate of Valor,
    Oni Hunter''s Garb, Triton''s Conch, Void Stone, Bancroft''s Talon, Void Shield,
    Freya''s Tears, The Cosmic Horror, Stampede, Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.19
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.3
      fit: 0.35
    Bragi's Harp:
      total: 0.46
      efficiency: 0.42
      win: 0.54
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.17
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 0.96
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Genji''s Guard, Shield
    of the Phoenix, Rod of Asclepius, Gluttonous Grimoire, Chandra''s Grace, Breastplate
    of Valor, Freya''s Tears, Lifebinder, Chronos'' Pendant, Spectral Armor, Screeching
    Gargoyle, Erosion, Kinetic Cuirass, Doublet of Binding, Triton''s Conch, Gem of
    Focus, Oni Hunter''s Garb, The Cosmic Horror, Void Stone, Totem of Death, Spear
    of the Magus, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.49
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.67
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.27
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius,
    Genji''s Guard, Shield of the Phoenix, Chandra''s Grace, Lifebinder, Erosion,
    Spectral Armor, Kinetic Cuirass, Doublet of Binding, Freya''s Tears, Oni Hunter''s
    Garb, Void Stone, The Cosmic Horror, Breastplate of Valor, Spear of the Magus,
    Screeching Gargoyle, Void Shield, Chronos'' Pendant, Triton''s Conch, Phoenix
    Feather, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.57
      pick: 0.51
      fit: 0.65
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.51
      pick: 0.47
      fit: 0.39
    Spectral Armor:
      total: 0.52
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.49
    Erosion:
      total: 0.52
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.62
      pick: 0.34
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
---
