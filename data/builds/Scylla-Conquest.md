---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.24
  aspect_win_rate: 0.64
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.46
    win_rate: 0.43
    alternates:
    - name: Book of Thoth
      pick_rate: 0.24
      win_rate: 0.57
    - name: Yogi's Necklace
      pick_rate: 0.16
      win_rate: 0.56
  - name: Book of Thoth
    pick_rate: 0.2
    win_rate: 0.39
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.3
      win_rate: 0.56
    - name: Doom Orb
      pick_rate: 0.12
      win_rate: 0.5
  - name: Polynomicon
    pick_rate: 0.28
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.46
  - name: Rod of Tahuti
    pick_rate: 0.32
    win_rate: 0.5
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.18
      win_rate: 0.45
    - name: Polynomicon
      pick_rate: 0.08
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.26
    win_rate: 0.62
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.42
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.63
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.4
    alternates:
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.0
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.8
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.43
    win_rate: 0.51
  - name: Conduit Gem
    pick_rate: 0.33
    win_rate: 0.45
  - name: Pendulum of the Ages
    pick_rate: 0.11
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-08-13'
  god_win_rate: 0.4956521739130435
  god_matches_won: 57
  god_matches_played: 115
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
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
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
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
    this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror,
    Chronos'' Pendant, The World Stone, Dreamer''s Idol, Gem of Focus, Totem of Death,
    Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death Metal, Breastplate
    of Valor, Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet,
    Ethereal Staff, Wish-Granting Pearl, Alchemist Coat.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.19
      fit: 0.21
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.43
      pick: 0.46
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.62
      pick: 0.56
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
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
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Death
    Metal, Breastplate of Valor, Chronos'' Pendant, The World Stone, Dreamer''s Idol,
    Gem of Focus, Totem of Death, Freya''s Tears, Blood-Bound Book, Bancroft''s Talon,
    Helm of Radiance, Bragi''s Harp, Shield of the Phoenix, Rod of Asclepius, Bracer
    of The Abyss, Jade Scepter, Kinetic Cuirass, Triton''s Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.19
      fit: 0.22
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.43
      pick: 0.46
      fit: 0.78
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.62
      pick: 0.56
      fit: 0.56
    Soul Gem:
      total: 0.55
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Kinetic Cuirass
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Yogi's Necklace
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Blood-Bound Book, Bancroft''s Talon, Chandra''s
    Grace, Oni Hunter''s Garb, Breastplate of Valor, Spear of the Magus, Freya''s
    Tears, Lifebinder, The Cosmic Horror, Phoenix Feather, Shifter''s Shield, Erosion,
    Helm of Radiance, Spectral Armor, Jade Scepter, Eye of Providence, Draconic Scale,
    Sphere of Negation.'
  slot_scores:
    Yogi's Necklace:
      total: 0.5
      efficiency: 0.59
      win: 0.56
      pick: 0.16
      fit: 0.19
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.19
      fit: 0.26
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.61
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.62
      pick: 0.56
      fit: 0.39
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.55
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - The Cosmic Horror
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror,
    The World Stone, Dreamer''s Idol, Chronos'' Pendant, Screeching Gargoyle, Breastplate
    of Valor, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death Metal,
    Gem of Focus, Rod of Asclepius, Bracer of The Abyss, Totem of Death, Jade Scepter,
    Ancient Signet, Ethereal Staff, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.19
      fit: 0.15
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.43
      pick: 0.46
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.85
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.62
      pick: 0.56
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
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
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
    this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, Bracer of The Abyss,
    The Cosmic Horror, Bragi''s Harp, Death Metal, Breastplate of Valor, Nimble Ring,
    Blood-Bound Book, Bancroft''s Talon, Chronos'' Pendant, Helm of Radiance, Rod
    of Asclepius, Kinetic Cuirass, Amanita Charm, Jade Scepter, Oni Hunter''s Garb,
    Freya''s Tears, The World Stone, Dreamer''s Idol, Eye of Providence, Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.57
      pick: 0.19
      fit: 0.08
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.45
      efficiency: 0.49
      win: 0.47
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.47
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.49
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.62
      pick: 0.56
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
    + fit + win/pick). Underrated for this god: Soul Gem, Breastplate of Valor, Gluttonous
    Grimoire, Chronos'' Pendant, Freya''s Tears, Gem of Focus, Shield of the Phoenix,
    Totem of Death, Spear of the Magus, The Cosmic Horror, Screeching Gargoyle, Chandra''s
    Grace, Death Metal, Gladiator''s Shield, The World Stone, Blood-Bound Book, Dreamer''s
    Idol, Bancroft''s Talon, Helm of Radiance, Kinetic Cuirass, Prophetic Cloak, Amanita
    Charm, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.57
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.5
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.43
      pick: 0.46
      fit: 0.86
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.62
      pick: 0.56
      fit: 0.37
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.47
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
    Cosmic Horror, Chronos'' Pendant, The World Stone, Dreamer''s Idol, Gem of Focus,
    Totem of Death, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death Metal,
    Breastplate of Valor, Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient
    Signet, Ethereal Staff, Wish-Granting Pearl, Alchemist Coat.'
  slot_scores:
    Chronos' Pendant:
      total: 0.5
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.43
      pick: 0.46
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.62
      pick: 0.56
      fit: 0.79
  starter: *id001
---
