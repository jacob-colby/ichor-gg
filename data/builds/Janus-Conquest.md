---
type: smite-build
god: Janus
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.47
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.34
      win_rate: 0.53
    - name: Doom Orb
      pick_rate: 0.07
      win_rate: 0.45
  - name: Book of Thoth
    pick_rate: 0.25
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.29
      win_rate: 0.51
    - name: The World Stone
      pick_rate: 0.11
      win_rate: 0.46
  - name: Soul Gem
    pick_rate: 0.4
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.53
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.55
  - name: Rod of Tahuti
    pick_rate: 0.39
    win_rate: 0.56
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.22
      win_rate: 0.49
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.62
  - name: Obsidian Shard
    pick_rate: 0.31
    win_rate: 0.65
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.2
      win_rate: 0.6
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.37
  - name: Evil Eye
    pick_rate: 0.12
    win_rate: 0.43
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.63
    - name: Dreamer's Idol
      pick_rate: 0.08
      win_rate: 0.72
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.49
    win_rate: 0.58
  - name: Conduit Gem
    pick_rate: 0.29
    win_rate: 0.4
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/janus/
  last_verified: '2026-08-19'
  god_win_rate: 0.5180878552971576
  god_matches_won: 401
  god_matches_played: 774
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - The Cosmic Horror
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Chronos'' Pendant, Genji''s Guard, Gem of Focus, Totem of Death, Death Metal,
    Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Breastplate of Valor, Bancroft''s
    Talon, Jade Scepter, Bracer of The Abyss, Ethereal Staff, Doom Orb, Alchemist
    Coat, Freya''s Tears, Polynomicon, Ancient Signet.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.47
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.56
      pick: 0.65
      fit: 0.78
    Obsidian Shard:
      total: 0.62
      efficiency: 0.52
      win: 0.65
      pick: 0.67
      fit: 0.78
    Dreamer's Idol:
      total: 0.61
      efficiency: 0.44
      win: 0.72
      pick: 0.25
      fit: 0.78
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    the Magus, Breastplate of Valor, Chronos'' Pendant, Bragi''s Harp, Bancroft''s
    Talon, Triton''s Conch, Helm of Radiance, Gem of Focus, Blood-Bound Book, Rod
    of Asclepius, Totem of Death, Oni Hunter''s Garb, Polynomicon, Jade Scepter, Freya''s
    Tears, Ancient Signet, Doom Orb.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.49
      win: 0.57
      pick: 0.34
      fit: 0.39
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.24
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.56
      pick: 0.65
      fit: 0.57
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.65
      pick: 0.67
      fit: 0.47
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.44
      win: 0.72
      pick: 0.25
      fit: 0.47
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.52
      pick: 0.62
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Nimble Ring, Death Metal, Chronos'' Pendant, Breastplate of Valor, Freya''s Tears,
    Gem of Focus, Totem of Death, Shield of the Phoenix, Bragi''s Harp, Helm of Radiance,
    Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Amanita Charm, Screeching
    Gargoyle, Triton''s Conch, Bancroft''s Talon, Chandra''s Grace, Doom Orb.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.54
      pick: 0.47
      fit: 0.78
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.56
      pick: 0.65
      fit: 0.56
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.65
      pick: 0.67
      fit: 0.56
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.44
      win: 0.72
      pick: 0.25
      fit: 0.56
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.52
      pick: 0.62
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
  - Kinetic Cuirass
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
    Rod of Asclepius, Genji''s Guard, Chandra''s Grace, Nimble Ring, Freya''s Tears,
    Oni Hunter''s Garb, Blood-Bound Book, Lifebinder, Breastplate of Valor, Bancroft''s
    Talon, Phoenix Feather, Erosion, The Cosmic Horror, Shifter''s Shield, Spectral
    Armor, Eye of Providence, Spear of the Magus, Draconic Scale, Helm of Radiance,
    Jade Scepter, Leviathan''s Hide, Midgardian Mail.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.56
      pick: 0.65
      fit: 0.37
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.65
      pick: 0.67
      fit: 0.37
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.44
      win: 0.72
      pick: 0.25
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.82
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.52
      pick: 0.62
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - The Cosmic Horror
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Nimble
    Ring, Genji''s Guard, Chronos'' Pendant, Screeching Gargoyle, Doom Orb, Breastplate
    of Valor, Death Metal, Helm of Radiance, Gem of Focus, Blood-Bound Book, Rod of
    Asclepius, Totem of Death, Bancroft''s Talon, Jade Scepter, Freya''s Tears, Stone
    of Binding, Bracer of The Abyss, Ethereal Staff, Kinetic Cuirass, Void Shield.'
  slot_scores:
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.47
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.77
      win: 0.56
      pick: 0.65
      fit: 0.85
    Obsidian Shard:
      total: 0.64
      efficiency: 0.52
      win: 0.65
      pick: 0.67
      fit: 0.85
    Dreamer's Idol:
      total: 0.62
      efficiency: 0.44
      win: 0.72
      pick: 0.25
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
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
    this god: Nimble Ring, Gluttonous Grimoire, Genji''s Guard, The Cosmic Horror,
    Spear of the Magus, Bragi''s Harp, Death Metal, Bracer of The Abyss, Breastplate
    of Valor, Chronos'' Pendant, Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass,
    Amanita Charm, Helm of Radiance, Freya''s Tears, Rod of Asclepius, Eye of Providence,
    Oni Hunter''s Garb, Shield of the Phoenix, Jade Scepter, Gem of Focus, Totem of
    Death, Doom Orb.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.41
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.49
    Bragi's Harp:
      total: 0.49
      efficiency: 0.42
      win: 0.54
      pick: 0.0
      fit: 0.64
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.56
      pick: 0.65
      fit: 0.3
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.65
      pick: 0.67
      fit: 0.3
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.52
      pick: 0.62
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Dreamer's Idol
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Chronos'' Pendant, Gluttonous Grimoire, Freya''s Tears, Shield of the Phoenix,
    Gem of Focus, Totem of Death, Nimble Ring, Screeching Gargoyle, Chandra''s Grace,
    The Cosmic Horror, Spear of the Magus, Death Metal, Gladiator''s Shield, Prophetic
    Cloak, Kinetic Cuirass, Amanita Charm, Helm of Radiance, Eye of Providence, Oni
    Hunter''s Garb, Blood-Bound Book, Rod of Asclepius, Regrowth Striders, Doom Orb.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.54
      pick: 0.47
      fit: 0.85
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.56
      pick: 0.65
      fit: 0.35
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.65
      pick: 0.67
      fit: 0.35
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.44
      win: 0.72
      pick: 0.25
      fit: 0.35
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.52
      pick: 0.62
      fit: 0.95
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
    Magus, Nimble Ring, Chronos'' Pendant, Doom Orb, Genji''s Guard, Gem of Focus,
    Totem of Death, Death Metal, Helm of Radiance, Blood-Bound Book, Rod of Asclepius,
    Breastplate of Valor, Bancroft''s Talon, Jade Scepter, Bracer of The Abyss, Ethereal
    Staff, Alchemist Coat, Freya''s Tears, Polynomicon, Ancient Signet.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.88
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.47
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.78
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.56
      pick: 0.65
      fit: 0.78
    Obsidian Shard:
      total: 0.62
      efficiency: 0.52
      win: 0.65
      pick: 0.67
      fit: 0.78
  starter: *id001
---
