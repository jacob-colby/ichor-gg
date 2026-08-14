---
type: smite-build
god: Ra
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thermotherapy
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.7
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.53
    win_rate: 0.58
    alternates:
    - name: Book of Thoth
      pick_rate: 0.26
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.05
      win_rate: 0.64
  - name: The World Stone
    pick_rate: 0.31
    win_rate: 0.58
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.42
  - name: Soul Gem
    pick_rate: 0.25
    win_rate: 0.65
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.58
    - name: The World Stone
      pick_rate: 0.11
      win_rate: 0.58
  - name: Rod of Tahuti
    pick_rate: 0.29
    win_rate: 0.53
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.22
      win_rate: 0.62
    - name: Nimble Ring
      pick_rate: 0.13
      win_rate: 0.63
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.71
    - name: Nimble Ring
      pick_rate: 0.13
      win_rate: 0.68
  - name: Evil Eye
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.81
    - name: Void Shard
      pick_rate: 0.09
      win_rate: 0.31
  community_starters:
  - name: Pendulum of The Ages
    pick_rate: 0.25
    win_rate: 0.62
  - name: Archmage's Gem
    pick_rate: 0.22
    win_rate: 0.64
  - name: Sands of Time
    pick_rate: 0.22
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/ra/
  last_verified: '2026-08-14'
  god_win_rate: 0.5652173913043478
  god_matches_won: 169
  god_matches_played: 299
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - The World Stone
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
    this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Chronos''
    Pendant, Genji''s Guard, Gem of Focus, Doom Orb, Dreamer''s Idol, Breastplate
    of Valor, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death Metal,
    Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet, Freya''s
    Tears, Polynomicon, Ethereal Staff, Wish-Granting Pearl, Shield of the Phoenix.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.72
    The World Stone:
      total: 0.56
      efficiency: 0.49
      win: 0.58
      pick: 0.42
      fit: 0.72
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.57
      pick: 0.35
      fit: 0.72
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 1.0
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
  - The Cosmic Horror
  - Genji's Guard
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
    god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Genji''s Guard,
    Death Metal, Breastplate of Valor, Chronos'' Pendant, Doom Orb, Dreamer''s Idol,
    Gem of Focus, Freya''s Tears, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance,
    Bragi''s Harp, Shield of the Phoenix, Rod of Asclepius, Bracer of The Abyss, Jade
    Scepter, Kinetic Cuirass, Triton''s Conch, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.22
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.78
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.35
      fit: 0.56
    Soul Gem:
      total: 0.65
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Shifter's Shield
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Genji''s Guard, Shifter''s Shield, Blood-Bound Book, Chandra''s
    Grace, Bancroft''s Talon, Breastplate of Valor, Freya''s Tears, Oni Hunter''s
    Garb, Lifebinder, Spear of the Magus, The Cosmic Horror, Phoenix Feather, Erosion,
    Helm of Radiance, Spectral Armor, Jade Scepter, Eye of Providence, Draconic Scale,
    Chronos'' Pendant, Sphere of Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.6
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.64
      pick: 0.05
      fit: 0.5
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.5
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.65
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - The World Stone
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
    for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Doom
    Orb, Dreamer''s Idol, Genji''s Guard, Chronos'' Pendant, Screeching Gargoyle,
    Breastplate of Valor, Gem of Focus, Blood-Bound Book, Bancroft''s Talon, Helm
    of Radiance, Death Metal, Rod of Asclepius, Bracer of The Abyss, Jade Scepter,
    Freya''s Tears, Ancient Signet, Stone of Binding, Shield of the Phoenix, Polynomicon.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 1.0
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.81
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.81
    The World Stone:
      total: 0.57
      efficiency: 0.49
      win: 0.58
      pick: 0.42
      fit: 0.81
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.57
      pick: 0.35
      fit: 0.81
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
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
    this god: Gluttonous Grimoire, Genji''s Guard, Bracer of The Abyss, Spear of the
    Magus, Breastplate of Valor, The Cosmic Horror, Bragi''s Harp, Death Metal, Blood-Bound
    Book, Bancroft''s Talon, Chronos'' Pendant, Helm of Radiance, Kinetic Cuirass,
    Freya''s Tears, Rod of Asclepius, Amanita Charm, Jade Scepter, Oni Hunter''s Garb,
    Gem of Focus, Eye of Providence, Shield of the Phoenix, Doom Orb.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.12
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.56
      efficiency: 0.49
      win: 0.68
      pick: 0.28
      fit: 0.48
    Bragi's Harp:
      total: 0.51
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.41
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Gluttonous Grimoire, Chronos'' Pendant, Freya''s Tears, Gem of Focus, Shield of
    the Phoenix, Spear of the Magus, Screeching Gargoyle, Chandra''s Grace, The Cosmic
    Horror, Death Metal, Gladiator''s Shield, Blood-Bound Book, Bancroft''s Talon,
    Helm of Radiance, Prophetic Cloak, Doom Orb, Kinetic Cuirass, Dreamer''s Idol,
    Amanita Charm, Rod of Asclepius, Bracer of The Abyss.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.5
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.65
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.85
    Soul Gem:
      total: 0.66
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Chronos'' Pendant, Genji''s Guard, Gem of Focus, Doom Orb, Dreamer''s Idol, Breastplate
    of Valor, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death Metal,
    Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet, Freya''s
    Tears, Polynomicon, Ethereal Staff, Wish-Granting Pearl, Shield of the Phoenix.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.62
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.72
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.57
      pick: 0.35
      fit: 0.72
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Kinetic Cuirass
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Genji''s Guard,
    Shield of the Phoenix, Lifebinder, Chandra''s Grace, Erosion, Spectral Armor,
    Kinetic Cuirass, Oni Hunter''s Garb, Doublet of Binding, Breastplate of Valor,
    Spear of the Magus, Freya''s Tears, Void Stone, The Cosmic Horror, Chronos'' Pendant,
    Blood-Bound Book, Bancroft''s Talon, Void Shield, Triton''s Conch, Screeching
    Gargoyle, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.65
    Spectral Armor:
      total: 0.54
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.49
    Erosion:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Genji''s Guard, Lifebinder,
    Spear of the Magus, The Cosmic Horror, Shield of the Phoenix, Triton''s Conch,
    Spectral Armor, Blood-Bound Book, Bancroft''s Talon, Breastplate of Valor, Chandra''s
    Grace, Erosion, Death Metal, Kinetic Cuirass, Chronos'' Pendant, Oni Hunter''s
    Garb, Doublet of Binding, Freya''s Tears, Void Stone, Umbral Link.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.62
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.45
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.45
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.35
      fit: 0.45
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Erosion, Kinetic Cuirass, Spectral Armor, Genji''s Guard, Shifter''s Shield, Lifebinder,
    Chandra''s Grace, Freya''s Tears, Breastplate of Valor, Umbral Link, Void Shield,
    Oni Hunter''s Garb, Doublet of Binding, Stampede, Void Stone, Phoenix Feather,
    Eye of Providence, Blood-Bound Book, Bancroft''s Talon, Draconic Scale, Mystical
    Mail, Glorious Pridwen.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.67
    Spectral Armor:
      total: 0.57
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.69
    Amanita Charm:
      total: 0.63
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.57
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.87
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Void Stone
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Void Stone,
    Spear of the Magus, Genji''s Guard, The Cosmic Horror, Void Shield, Shield of
    the Phoenix, Screeching Gargoyle, Lifebinder, Spectral Armor, Erosion, Chandra''s
    Grace, Kinetic Cuirass, Breastplate of Valor, Oni Hunter''s Garb, Doublet of Binding,
    Doom Orb, Dreamer''s Idol, Freya''s Tears, Blood-Bound Book, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.3
    Void Stone:
      total: 0.55
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.74
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.35
      fit: 0.56
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.65
      pick: 0.39
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
  - Spectral Armor
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Genji''s Guard,
    Spectral Armor, Lifebinder, Shield of the Phoenix, Blood-Bound Book, Bancroft''s
    Talon, Erosion, Umbral Link, Breastplate of Valor, Kinetic Cuirass, Chandra''s
    Grace, Oni Hunter''s Garb, Doublet of Binding, Triton''s Conch, Bracer of The
    Abyss, Spear of the Magus, Void Stone, Void Shield, Freya''s Tears, The Cosmic
    Horror, Death Metal, Stampede, Bragi''s Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.19
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.54
      efficiency: 0.49
      win: 0.68
      pick: 0.28
      fit: 0.35
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.49
    Spectral Armor:
      total: 0.52
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.39
    Soul Gem:
      total: 0.66
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 0.96
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Amanita Charm, Genji''s Guard, Rod
    of Asclepius, Gluttonous Grimoire, Shield of the Phoenix, Breastplate of Valor,
    Chandra''s Grace, Freya''s Tears, Lifebinder, Chronos'' Pendant, Spectral Armor,
    Screeching Gargoyle, Erosion, Kinetic Cuirass, Triton''s Conch, Gem of Focus,
    Spear of the Magus, Oni Hunter''s Garb, Doublet of Binding, Blood-Bound Book,
    Bancroft''s Talon, The Cosmic Horror, Void Stone, Void Shield, Umbral Link.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.49
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.39
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.67
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Kinetic Cuirass
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius,
    Genji''s Guard, Shield of the Phoenix, Lifebinder, Chandra''s Grace, Erosion,
    Spectral Armor, Kinetic Cuirass, Oni Hunter''s Garb, Doublet of Binding, Breastplate
    of Valor, Spear of the Magus, Freya''s Tears, Void Stone, The Cosmic Horror, Chronos''
    Pendant, Blood-Bound Book, Bancroft''s Talon, Void Shield, Triton''s Conch, Screeching
    Gargoyle, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.65
    Spectral Armor:
      total: 0.54
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.49
    Erosion:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.65
      pick: 0.39
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
---
