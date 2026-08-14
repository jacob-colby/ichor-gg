---
type: smite-build
god: Ra
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thermotherapy
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.65
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.51
    win_rate: 0.61
    alternates:
    - name: Book of Thoth
      pick_rate: 0.32
      win_rate: 0.53
    - name: Doom Orb
      pick_rate: 0.03
      win_rate: 0.8
  - name: The World Stone
    pick_rate: 0.3
    win_rate: 0.67
    alternates:
    - name: Book of Thoth
      pick_rate: 0.17
      win_rate: 0.36
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.5
  - name: Soul Gem
    pick_rate: 0.24
    win_rate: 0.69
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.54
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.3
    win_rate: 0.51
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.26
      win_rate: 0.69
    - name: Nimble Ring
      pick_rate: 0.09
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.75
    - name: Nimble Ring
      pick_rate: 0.1
      win_rate: 0.62
  - name: Void Shard
    pick_rate: 0.1
    win_rate: 0.25
    alternates:
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.38
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.24
    win_rate: 0.65
  - name: Pendulum of the Ages
    pick_rate: 0.23
    win_rate: 0.61
  - name: Conduit Gem
    pick_rate: 0.2
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/ra/
  last_verified: '2026-08-13'
  god_win_rate: 0.5609756097560976
  god_matches_won: 92
  god_matches_played: 164
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
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
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
    this god: Doom Orb, Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Chronos'' Pendant, Genji''s Guard, Gem of Focus, Totem of Death, Dreamer''s Idol,
    Breastplate of Valor, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death
    Metal, Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet, Freya''s
    Tears, Polynomicon, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.72
    Doom Orb:
      total: 0.64
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.72
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.72
    The World Stone:
      total: 0.6
      efficiency: 0.49
      win: 0.67
      pick: 0.41
      fit: 0.72
    Soul Gem:
      total: 0.69
      efficiency: 0.59
      win: 0.69
      pick: 0.37
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Doom Orb, Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Genji''s
    Guard, Death Metal, Breastplate of Valor, Chronos'' Pendant, Dreamer''s Idol,
    Gem of Focus, Totem of Death, Freya''s Tears, Blood-Bound Book, Bancroft''s Talon,
    Helm of Radiance, Bragi''s Harp, Shield of the Phoenix, Rod of Asclepius, Bracer
    of The Abyss, Jade Scepter, Kinetic Cuirass, Triton''s Conch.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 0.78
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.56
    Doom Orb:
      total: 0.62
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.56
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.58
      efficiency: 0.49
      win: 0.67
      pick: 0.41
      fit: 0.56
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.69
      pick: 0.37
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Doom Orb
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
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
    Kinetic Cuirass, Genji''s Guard, Blood-Bound Book, Chandra''s Grace, Bancroft''s
    Talon, Breastplate of Valor, Freya''s Tears, Oni Hunter''s Garb, Lifebinder, Spear
    of the Magus, The Cosmic Horror, Phoenix Feather, Shifter''s Shield, Erosion,
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
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 0.5
    Doom Orb:
      total: 0.59
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.36
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.69
      pick: 0.37
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
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
    for this god: Doom Orb, Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Dreamer''s Idol, Genji''s Guard, Chronos'' Pendant, Screeching Gargoyle, Breastplate
    of Valor, Gem of Focus, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance,
    Totem of Death, Death Metal, Rod of Asclepius, Bracer of The Abyss, Jade Scepter,
    Freya''s Tears, Ancient Signet, Stone of Binding, Shield of the Phoenix.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 1.0
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.81
    Doom Orb:
      total: 0.65
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.81
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.81
    The World Stone:
      total: 0.61
      efficiency: 0.49
      win: 0.67
      pick: 0.41
      fit: 0.81
    Soul Gem:
      total: 0.69
      efficiency: 0.59
      win: 0.69
      pick: 0.37
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Doom Orb
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
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
    this god: Gluttonous Grimoire, Genji''s Guard, Bracer of The Abyss, Spear of the
    Magus, Breastplate of Valor, The Cosmic Horror, Bragi''s Harp, Death Metal, Blood-Bound
    Book, Bancroft''s Talon, Chronos'' Pendant, Helm of Radiance, Freya''s Tears,
    Rod of Asclepius, Kinetic Cuirass, Amanita Charm, Gem of Focus, Jade Scepter,
    Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence, Totem of Death.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.53
      efficiency: 0.49
      win: 0.62
      pick: 0.22
      fit: 0.48
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 0.41
    Doom Orb:
      total: 0.58
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.29
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.69
      pick: 0.37
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
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
    + fit + win/pick). Underrated for this god: Doom Orb, Genji''s Guard, Breastplate
    of Valor, Gluttonous Grimoire, Chronos'' Pendant, Freya''s Tears, Gem of Focus,
    Shield of the Phoenix, Totem of Death, Spear of the Magus, Screeching Gargoyle,
    Chandra''s Grace, The Cosmic Horror, Death Metal, Gladiator''s Shield, Blood-Bound
    Book, Bancroft''s Talon, Helm of Radiance, Prophetic Cloak, Kinetic Cuirass, Dreamer''s
    Idol, Amanita Charm, Rod of Asclepius.'
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
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 0.85
    Doom Orb:
      total: 0.58
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.35
    Soul Gem:
      total: 0.68
      efficiency: 0.59
      win: 0.69
      pick: 0.37
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
    Chronos'' Pendant, Genji''s Guard, Gem of Focus, Doom Orb, Totem of Death, Dreamer''s
    Idol, Breastplate of Valor, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance,
    Death Metal, Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet,
    Freya''s Tears, Polynomicon, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.63
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.72
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.5
      pick: 0.37
      fit: 0.72
    Soul Gem:
      total: 0.69
      efficiency: 0.59
      win: 0.69
      pick: 0.37
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Erosion
  - Soul Gem
  flex_slots:
  - The World Stone
  - Erosion
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
    Kinetic Cuirass, Doublet of Binding, Oni Hunter''s Garb, Breastplate of Valor,
    Freya''s Tears, Spear of the Magus, Void Stone, The Cosmic Horror, Chronos'' Pendant,
    Blood-Bound Book, Bancroft''s Talon, Void Shield, Screeching Gargoyle, Triton''s
    Conch, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 0.65
    Doom Orb:
      total: 0.59
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.39
    The World Stone:
      total: 0.55
      efficiency: 0.49
      win: 0.67
      pick: 0.41
      fit: 0.39
    Erosion:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.69
      efficiency: 0.59
      win: 0.69
      pick: 0.37
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Spear of the Magus
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
    Grace, Erosion, Death Metal, Kinetic Cuirass, Chronos'' Pendant, Doublet of Binding,
    Oni Hunter''s Garb, Freya''s Tears, Void Stone, Umbral Link.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 0.62
    Doom Orb:
      total: 0.6
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.45
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.45
    The World Stone:
      total: 0.56
      efficiency: 0.49
      win: 0.67
      pick: 0.41
      fit: 0.45
    Soul Gem:
      total: 0.69
      efficiency: 0.59
      win: 0.69
      pick: 0.37
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Doom Orb
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Erosion, Kinetic Cuirass, Spectral Armor, Genji''s Guard, Lifebinder, Chandra''s
    Grace, Freya''s Tears, Breastplate of Valor, Umbral Link, Void Shield, Doublet
    of Binding, Oni Hunter''s Garb, Stampede, Void Stone, Shifter''s Shield, Phoenix
    Feather, Eye of Providence, Blood-Bound Book, Bancroft''s Talon, Draconic Scale,
    Mystical Mail, Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.67
    Doom Orb:
      total: 0.57
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.26
    Spectral Armor:
      total: 0.56
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
      total: 0.69
      efficiency: 0.59
      win: 0.69
      pick: 0.37
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Stone
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Void Stone
  - Spear of the Magus
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
    for this god: Doom Orb, Gluttonous Grimoire, Amanita Charm, Rod of Asclepius,
    Void Stone, Spear of the Magus, Genji''s Guard, The Cosmic Horror, Void Shield,
    Shield of the Phoenix, Screeching Gargoyle, Lifebinder, Spectral Armor, Erosion,
    Chandra''s Grace, Kinetic Cuirass, Breastplate of Valor, Doublet of Binding, Oni
    Hunter''s Garb, Dreamer''s Idol, Freya''s Tears, Blood-Bound Book, Bancroft''s
    Talon.'
  slot_scores:
    Void Stone:
      total: 0.55
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 0.74
    Doom Orb:
      total: 0.62
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.56
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.58
      efficiency: 0.49
      win: 0.67
      pick: 0.41
      fit: 0.56
    Soul Gem:
      total: 0.69
      efficiency: 0.59
      win: 0.69
      pick: 0.37
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
  - Doom Orb
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
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Genji''s Guard,
    Spectral Armor, Lifebinder, Shield of the Phoenix, Blood-Bound Book, Bancroft''s
    Talon, Erosion, Umbral Link, Breastplate of Valor, Kinetic Cuirass, Chandra''s
    Grace, Doublet of Binding, Oni Hunter''s Garb, Triton''s Conch, Bracer of The
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
      total: 0.49
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.51
      efficiency: 0.49
      win: 0.62
      pick: 0.22
      fit: 0.35
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.49
    Doom Orb:
      total: 0.56
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.17
    Soul Gem:
      total: 0.68
      efficiency: 0.59
      win: 0.69
      pick: 0.37
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
  - Doom Orb
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
    + fit + win/pick). Underrated for this god: Amanita Charm, Genji''s Guard, Rod
    of Asclepius, Shield of the Phoenix, Gluttonous Grimoire, Breastplate of Valor,
    Chandra''s Grace, Freya''s Tears, Lifebinder, Chronos'' Pendant, Spectral Armor,
    Screeching Gargoyle, Erosion, Kinetic Cuirass, Triton''s Conch, Gem of Focus,
    Spear of the Magus, Blood-Bound Book, Doublet of Binding, Oni Hunter''s Garb,
    Bancroft''s Talon, Totem of Death, The Cosmic Horror, Void Stone, Umbral Link.'
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
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 0.67
    Doom Orb:
      total: 0.57
      efficiency: 0.49
      win: 0.8
      pick: 0.03
      fit: 0.27
    Soul Gem:
      total: 0.69
      efficiency: 0.59
      win: 0.69
      pick: 0.37
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
    Spectral Armor, Kinetic Cuirass, Doublet of Binding, Oni Hunter''s Garb, Breastplate
    of Valor, Freya''s Tears, Spear of the Magus, Void Stone, The Cosmic Horror, Chronos''
    Pendant, Blood-Bound Book, Bancroft''s Talon, Void Shield, Screeching Gargoyle,
    Triton''s Conch, Phoenix Feather.'
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
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.51
      fit: 0.65
    Spectral Armor:
      total: 0.53
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
      total: 0.69
      efficiency: 0.59
      win: 0.69
      pick: 0.37
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
---
