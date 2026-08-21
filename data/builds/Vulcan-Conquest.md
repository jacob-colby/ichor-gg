---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.54
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.34
    win_rate: 0.53
    alternates:
    - name: Book of Thoth
      pick_rate: 0.33
      win_rate: 0.55
    - name: The World Stone
      pick_rate: 0.06
      win_rate: 0.49
  - name: The World Stone
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.51
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.54
    alternates:
    - name: Soul Gem
      pick_rate: 0.14
      win_rate: 0.66
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.55
  - name: Obsidian Shard
    pick_rate: 0.29
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.24
      win_rate: 0.62
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.43
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.43
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.64
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.6
  - name: Shrapnel Mod
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Thermal Mod
      pick_rate: 0.11
      win_rate: 0.47
    - name: Surplus Mod
      pick_rate: 0.09
      win_rate: 0.51
  - name: Surplus Mod
    pick_rate: 0.25
    win_rate: 0.52
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.32
      win_rate: 0.55
    - name: Thermal Mod
      pick_rate: 0.24
      win_rate: 0.63
  - name: Seismic Mod
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Surplus Mod
      pick_rate: 0.67
      win_rate: 0.57
    - name: Thermal Mod
      pick_rate: 0.12
      win_rate: 0.53
  - name: Masterwork Mod
    pick_rate: 0.06
    win_rate: 0.0
    alternates:
    - name: Seismic Mod
      pick_rate: 0.62
      win_rate: 0.48
    - name: Surplus Mod
      pick_rate: 0.32
      win_rate: 0.55
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.32
    win_rate: 0.59
  - name: Sands Of Time
    pick_rate: 0.22
    win_rate: 0.44
  - name: Archmage's Gem
    pick_rate: 0.21
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-08-21'
  god_win_rate: 0.5342465753424658
  god_matches_won: 351
  god_matches_played: 657
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
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
    this god: Gluttonous Grimoire, Nimble Ring, The Cosmic Horror, Spear of the Magus,
    Chronos'' Pendant, Genji''s Guard, Doom Orb, Totem of Death, Bracer of The Abyss,
    Dreamer''s Idol, Gem of Focus, Breastplate of Valor, Death Metal, Helm of Radiance,
    Ethereal Staff, Blood-Bound Book, Rod of Asclepius, Bragi''s Harp, Bancroft''s
    Talon, Jade Scepter, Freya''s Tears, Alchemist Coat, Shield of the Phoenix.'
  slot_scores:
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.53
      pick: 0.34
      fit: 0.83
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.54
      pick: 0.3
      fit: 0.66
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.57
      pick: 0.48
      fit: 0.76
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.93
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
  - Book of Thoth
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
    Grimoire, Nimble Ring, Genji''s Guard, Death Metal, The Cosmic Horror, Spear of
    the Magus, Breastplate of Valor, Bragi''s Harp, Chronos'' Pendant, Doom Orb, Totem
    of Death, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Bracer of The Abyss,
    Blood-Bound Book, Rod of Asclepius, Triton''s Conch, Gem of Focus, Oni Hunter''s
    Garb, Freya''s Tears, Jade Scepter, Polynomicon.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.49
      win: 0.55
      pick: 0.33
      fit: 0.35
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.22
    The World Stone:
      total: 0.5
      efficiency: 0.46
      win: 0.57
      pick: 0.19
      fit: 0.52
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.54
      pick: 0.3
      fit: 0.52
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.48
      fit: 0.53
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.66
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
    god: Gluttonous Grimoire, Nimble Ring, The Cosmic Horror, Spear of the Magus,
    Genji''s Guard, Death Metal, Breastplate of Valor, Chronos'' Pendant, Totem of
    Death, Doom Orb, Bragi''s Harp, Freya''s Tears, Gem of Focus, Dreamer''s Idol,
    Shield of the Phoenix, Helm of Radiance, Bracer of The Abyss, Ethereal Staff,
    Kinetic Cuirass, Blood-Bound Book, Rod of Asclepius, Amanita Charm, Screeching
    Gargoyle, Eye of Providence.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.53
      pick: 0.34
      fit: 0.7
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.5
    Spear of the Magus:
      total: 0.51
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.54
      pick: 0.3
      fit: 0.5
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.48
      fit: 0.6
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Ethereal
    Staff, Kinetic Cuirass, Rod of Asclepius, Nimble Ring, Genji''s Guard, Chandra''s
    Grace, Yogi''s Necklace, Blood-Bound Book, Oni Hunter''s Garb, Freya''s Tears,
    Bancroft''s Talon, Lifebinder, Breastplate of Valor, The Cosmic Horror, Phoenix
    Feather, Spear of the Magus, Erosion, Spectral Armor, Shifter''s Shield, Eye of
    Providence, Helm of Radiance, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.54
      pick: 0.3
      fit: 0.36
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.48
      fit: 0.46
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.85
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
    for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Nimble
    Ring, Doom Orb, Dreamer''s Idol, Genji''s Guard, Screeching Gargoyle, Chronos''
    Pendant, Breastplate of Valor, Totem of Death, Bracer of The Abyss, Death Metal,
    Helm of Radiance, Ethereal Staff, Blood-Bound Book, Rod of Asclepius, Gem of Focus,
    Stone of Binding, Bancroft''s Talon, Freya''s Tears, Jade Scepter, Kinetic Cuirass,
    Void Shield.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.53
      pick: 0.34
      fit: 0.88
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.75
    Spear of the Magus:
      total: 0.55
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.54
      pick: 0.3
      fit: 0.75
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.48
      fit: 0.85
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.98
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
    Amanita Charm, Helm of Radiance, Totem of Death, Ethereal Staff, Freya''s Tears,
    Rod of Asclepius, Eye of Providence, Oni Hunter''s Garb, Shield of the Phoenix,
    Jade Scepter, Doom Orb, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.42
      win: 0.53
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.54
      pick: 0.3
      fit: 0.32
    Obsidian Shard:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.48
      fit: 0.42
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.58
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Gluttonous Grimoire, Chronos'' Pendant, Nimble Ring, Freya''s Tears, Totem of
    Death, Shield of the Phoenix, Gem of Focus, The Cosmic Horror, Screeching Gargoyle,
    Chandra''s Grace, Spear of the Magus, Death Metal, Gladiator''s Shield, Kinetic
    Cuirass, Amanita Charm, Bragi''s Harp, Eye of Providence, Oni Hunter''s Garb,
    Bracer of The Abyss, Prophetic Cloak, Helm of Radiance, Ethereal Staff, Doom Orb.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.53
      pick: 0.34
      fit: 0.76
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.54
      pick: 0.3
      fit: 0.33
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.48
      fit: 0.43
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Nimble Ring
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Nimble Ring, The Cosmic Horror,
    Spear of the Magus, Chronos'' Pendant, Genji''s Guard, Doom Orb, Totem of Death,
    Bracer of The Abyss, Dreamer''s Idol, Gem of Focus, Breastplate of Valor, Death
    Metal, Helm of Radiance, Ethereal Staff, Blood-Bound Book, Rod of Asclepius, Bragi''s
    Harp, Bancroft''s Talon, Jade Scepter, Freya''s Tears, Alchemist Coat, Shield
    of the Phoenix.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.53
      pick: 0.34
      fit: 0.83
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.54
      pick: 0.3
      fit: 0.66
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.57
      pick: 0.48
      fit: 0.76
  starter: *id001
---
