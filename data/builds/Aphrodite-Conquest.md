---
type: smite-build
god: Aphrodite
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.28
    win_rate: 0.66
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.23
      win_rate: 0.57
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.58
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.17
      win_rate: 0.56
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.54
  - name: Spear of Desolation
    pick_rate: 0.14
    win_rate: 0.68
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.54
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.53
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.72
    alternates:
    - name: The World Stone
      pick_rate: 0.11
      win_rate: 0.62
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.52
  - name: Obsidian Shard
    pick_rate: 0.11
    win_rate: 0.68
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.67
    - name: The World Stone
      pick_rate: 0.08
      win_rate: 0.73
  - name: Oracle Staff
    pick_rate: 0.06
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.63
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.68
  source_url: https://smitebrain.com/gods/aphrodite/
  last_verified: '2026-07-23'
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - Obsidian Shard
  flex_slots:
  - Kinetic Cuirass
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of Desolation, Kinetic Cuirass, Gluttonous Grimoire, Eye of Providence,
    Soul Gem, Amanita Charm, Spectral Armor, Rod of Asclepius, Ethereal Staff, The
    Cosmic Horror, Erosion, Shield of the Phoenix, Spear of the Magus, Helm of Radiance,
    Doom Orb, Breastplate of Valor, Chandra''s Grace, Blood-Bound Book, Alchemist
    Coat, Chronos'' Pendant, Lifebinder, Gladiator''s Shield, Jade Scepter, Midgardian
    Mail, Ancient Signet, Death Metal.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.39
      win: 0.66
      pick: 0.28
      fit: 0.2
    Genji's Guard:
      total: 0.48
      efficiency: 0.46
      win: 0.58
      pick: 0.19
      fit: 0.32
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.54
      efficiency: 0.42
      win: 0.68
      pick: 0.14
      fit: 0.5
    Obsidian Shard:
      total: 0.49
      efficiency: 0.36
      win: 0.68
      pick: 0.11
      fit: 0.36
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Rod of Tahuti
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Spear of Desolation, Obsidian Shard, Gluttonous Grimoire, Soul Gem, Kinetic
    Cuirass, Eye of Providence, The Cosmic Horror, Amanita Charm, Spectral Armor,
    Rod of Asclepius, Ethereal Staff, Spear of the Magus, Shield of the Phoenix, Death
    Metal, Doom Orb, Erosion, Chandra''s Grace, Breastplate of Valor, Blood-Bound
    Book, Chronos'' Pendant, The World Stone, Helm of Radiance, Triton''s Conch, Bragi''s
    Harp, Alchemist Coat, Gladiator''s Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.39
      win: 0.66
      pick: 0.28
      fit: 0.14
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.58
      pick: 0.19
      fit: 0.27
    Gluttonous Grimoire:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.53
      efficiency: 0.42
      win: 0.68
      pick: 0.14
      fit: 0.49
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.24
      win: 0.72
      pick: 0.17
      fit: 0.35
    Obsidian Shard:
      total: 0.49
      efficiency: 0.36
      win: 0.68
      pick: 0.11
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Genji's Guard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Spear of Desolation, Soul Gem, Amanita Charm, Rod of Asclepius, Shield
    of the Phoenix, Blood-Bound Book, Gluttonous Grimoire, Chandra''s Grace, Lifebinder,
    Kinetic Cuirass, Bancroft''s Talon, Eye of Providence, Phoenix Feather, Spectral
    Armor, Ethereal Staff, The Cosmic Horror, Spirit Robe, Erosion, Spear of the Magus,
    Helm of Radiance, Doom Orb, Alchemist Coat, Breastplate of Valor, Chronos'' Pendant,
    Glorious Pridwen, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.39
      win: 0.66
      pick: 0.28
      fit: 0.18
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.58
      pick: 0.19
      fit: 0.26
    Spear of Desolation:
      total: 0.53
      efficiency: 0.42
      win: 0.68
      pick: 0.14
      fit: 0.43
    Obsidian Shard:
      total: 0.49
      efficiency: 0.36
      win: 0.68
      pick: 0.11
      fit: 0.31
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.7
    Soul Gem:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.83
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Book of Thoth
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of Desolation, Obsidian Shard, Gluttonous Grimoire, Soul Gem,
    The Cosmic Horror, Kinetic Cuirass, Eye of Providence, Spear of the Magus, Screeching
    Gargoyle, Amanita Charm, Doom Orb, Spectral Armor, Rod of Asclepius, Ethereal
    Staff, Void Stone, Stone of Binding, Void Shield, The World Stone, Shield of the
    Phoenix, Erosion, Blood-Bound Book, Helm of Radiance, Chandra''s Grace, Breastplate
    of Valor, Alchemist Coat, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.39
      win: 0.66
      pick: 0.28
      fit: 0.17
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.58
      pick: 0.19
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.55
      efficiency: 0.42
      win: 0.68
      pick: 0.14
      fit: 0.59
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.24
      win: 0.72
      pick: 0.17
      fit: 0.48
    Obsidian Shard:
      total: 0.51
      efficiency: 0.36
      win: 0.68
      pick: 0.11
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Lernaean Bow:
      total: 0.23
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.23
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.23
    Tyrfing:
      total: 0.24
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.23
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.23
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
---
