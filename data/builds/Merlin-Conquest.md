---
type: smite-build
god: Merlin
mode: Conquest
builds:
- source: community
  aspect: Aspect of Pandemonium
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.53
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.34
    win_rate: 0.47
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.18
      win_rate: 0.55
    - name: The World Stone
      pick_rate: 0.1
      win_rate: 0.56
  - name: Totem of Death
    pick_rate: 0.17
    win_rate: 0.67
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.52
    - name: Soul Reaver
      pick_rate: 0.16
      win_rate: 0.45
  - name: Soul Gem
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Totem of Death
      pick_rate: 0.22
      win_rate: 0.41
    - name: Soul Reaver
      pick_rate: 0.12
      win_rate: 0.59
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.53
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.16
      win_rate: 0.54
    - name: Totem of Death
      pick_rate: 0.13
      win_rate: 0.61
  - name: Obsidian Shard
    pick_rate: 0.22
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.59
    - name: Evil Eye
      pick_rate: 0.12
      win_rate: 0.25
  - name: Evil Eye
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.64
    - name: Void Shard
      pick_rate: 0.09
      win_rate: 0.45
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.32
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.23
    win_rate: 0.4
  - name: Pendulum of the Ages
    pick_rate: 0.23
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/merlin/
  last_verified: '2026-08-14'
  god_win_rate: 0.5035971223021583
  god_matches_won: 140
  god_matches_played: 278
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
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spear of the Magus
  - Totem of Death
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Nimble Ring,
    The World Stone, Doom Orb, Genji''s Guard, Dreamer''s Idol, Gem of Focus, Death
    Metal, Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Breastplate of Valor,
    Bancroft''s Talon, Jade Scepter, Bracer of The Abyss, Ethereal Staff, Alchemist
    Coat, Freya''s Tears, Book of Thoth.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.89
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.79
    Totem of Death:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.23
      fit: 0.63
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.53
      pick: 0.28
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.58
      pick: 0.48
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Gluttonous Grimoire
  - The World Stone
  - Totem of Death
  - Rod of Tahuti
  - Obsidian Shard
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
    Grimoire, Nimble Ring, Death Metal, Genji''s Guard, The Cosmic Horror, Spear of
    the Magus, The World Stone, Breastplate of Valor, Doom Orb, Bragi''s Harp, Bancroft''s
    Talon, Triton''s Conch, Helm of Radiance, Gem of Focus, Blood-Bound Book, Rod
    of Asclepius, Book of Thoth, Oni Hunter''s Garb, Polynomicon, Jade Scepter, Freya''s
    Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.24
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.57
    The World Stone:
      total: 0.5
      efficiency: 0.46
      win: 0.56
      pick: 0.1
      fit: 0.57
    Totem of Death:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.23
      fit: 0.43
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.53
      pick: 0.28
      fit: 0.57
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.48
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Spear of Desolation
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
    Nimble Ring, Death Metal, The World Stone, Breastplate of Valor, Doom Orb, Freya''s
    Tears, Gem of Focus, Dreamer''s Idol, Shield of the Phoenix, Bragi''s Harp, Helm
    of Radiance, Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Amanita Charm,
    Screeching Gargoyle, Triton''s Conch.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.47
      pick: 0.34
      fit: 0.78
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.56
    Totem of Death:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.23
      fit: 0.44
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.53
      pick: 0.28
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.48
      fit: 0.56
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.26
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Totem of Death
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Totem of Death
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Kinetic Cuirass,
    Rod of Asclepius, Genji''s Guard, Chandra''s Grace, Nimble Ring, Blood-Bound Book,
    Freya''s Tears, Oni Hunter''s Garb, Lifebinder, The Cosmic Horror, Bancroft''s
    Talon, Breastplate of Valor, Spear of the Magus, Phoenix Feather, Erosion, Shifter''s
    Shield, Spectral Armor, Eye of Providence, Draconic Scale, Helm of Radiance, Jade
    Scepter.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.61
    Totem of Death:
      total: 0.53
      efficiency: 0.47
      win: 0.67
      pick: 0.23
      fit: 0.31
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.53
      pick: 0.28
      fit: 0.39
    Obsidian Shard:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.48
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.26
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
  - Spear of Desolation
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
    for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, The
    World Stone, Doom Orb, Nimble Ring, Dreamer''s Idol, Genji''s Guard, Screeching
    Gargoyle, Breastplate of Valor, Death Metal, Helm of Radiance, Gem of Focus, Blood-Bound
    Book, Rod of Asclepius, Bancroft''s Talon, Jade Scepter, Freya''s Tears, Stone
    of Binding, Bracer of The Abyss, Ethereal Staff.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.47
      pick: 0.34
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.57
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.77
      win: 0.53
      pick: 0.28
      fit: 0.85
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.48
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Totem of Death
  - Rod of Tahuti
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
    this god: Nimble Ring, Gluttonous Grimoire, Genji''s Guard, The Cosmic Horror,
    Spear of the Magus, Bragi''s Harp, Death Metal, Bracer of The Abyss, Breastplate
    of Valor, Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass, Amanita Charm,
    Helm of Radiance, Freya''s Tears, Rod of Asclepius, Eye of Providence, Oni Hunter''s
    Garb, Shield of the Phoenix, Jade Scepter, Doom Orb, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.42
      win: 0.54
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.49
    Totem of Death:
      total: 0.52
      efficiency: 0.47
      win: 0.67
      pick: 0.23
      fit: 0.25
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.53
      pick: 0.28
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Chronos' Pendant
  - Spear of Desolation
  - Totem of Death
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - Spear of Desolation
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Gluttonous Grimoire, Freya''s Tears, Shield of the Phoenix, Gem of Focus, Nimble
    Ring, The Cosmic Horror, Screeching Gargoyle, Chandra''s Grace, Spear of the Magus,
    Death Metal, Gladiator''s Shield, The World Stone, Kinetic Cuirass, Prophetic
    Cloak, Amanita Charm, Doom Orb, Helm of Radiance, Eye of Providence, Oni Hunter''s
    Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.18
      fit: 0.63
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.47
      pick: 0.34
      fit: 0.86
    Totem of Death:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.23
      fit: 0.63
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.53
      pick: 0.28
      fit: 0.37
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.26
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
    Underrated for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the
    Magus, Nimble Ring, Doom Orb, The World Stone, Genji''s Guard, Dreamer''s Idol,
    Gem of Focus, Death Metal, Helm of Radiance, Blood-Bound Book, Rod of Asclepius,
    Breastplate of Valor, Bancroft''s Talon, Jade Scepter, Bracer of The Abyss, Ethereal
    Staff, Alchemist Coat, Freya''s Tears, Book of Thoth.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.47
      pick: 0.34
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.53
      pick: 0.28
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.58
      pick: 0.48
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Totem of Death
  - Rod of Tahuti
  flex_slots:
  - Spear of the Magus
  - Totem of Death
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, The Cosmic Horror,
    Spear of the Magus, Nimble Ring, Doom Orb, The World Stone, Genji''s Guard, Dreamer''s
    Idol, Gem of Focus, Death Metal, Helm of Radiance, Blood-Bound Book, Rod of Asclepius,
    Breastplate of Valor, Bancroft''s Talon, Jade Scepter, Bracer of The Abyss, Ethereal
    Staff, Alchemist Coat, Freya''s Tears, Book of Thoth.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.47
      pick: 0.34
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.79
    Totem of Death:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.23
      fit: 0.63
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.53
      pick: 0.28
      fit: 0.79
  swaps:
  - added: Totem of Death
    removed: Obsidian Shard
    reason: community 67% win over 47 matches (vs 50% on this god), taking the model's
      weakest slot from Obsidian Shard
  starter: *id001
---
