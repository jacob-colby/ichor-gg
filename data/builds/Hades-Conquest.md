---
type: smite-build
god: Hades
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.27
    win_rate: 0.68
    alternates:
    - name: Bancroft's Talon
      pick_rate: 0.18
      win_rate: 0.6
    - name: Book of Thoth
      pick_rate: 0.07
      win_rate: 0.55
  - name: Book of Thoth
    pick_rate: 0.13
    win_rate: 0.72
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.64
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.61
  - name: Soul Gem
    pick_rate: 0.1
    win_rate: 0.58
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.48
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.8
  - name: Rod of Tahuti
    pick_rate: 0.26
    win_rate: 0.63
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.79
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.75
  - name: Obsidian Shard
    pick_rate: 0.08
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.68
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.62
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.56
    - name: Void Shard
      pick_rate: 0.05
      win_rate: 0.43
  source_url: https://smitebrain.com/gods/hades/
  last_verified: '2026-07-23'
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Kinetic Cuirass
  - Ethereal Staff
  - Spear of Desolation
  - The Cosmic Horror
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Ethereal Staff
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
    this god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Kinetic Cuirass, Rod
    of Asclepius, Ethereal Staff, Eye of Providence, Spear of the Magus, Amanita Charm,
    Obsidian Shard, Spectral Armor, Doom Orb, Alchemist Coat, Shield of the Phoenix,
    Blood-Bound Book, Lifebinder, The World Stone, Genji''s Guard, Chronos'' Pendant,
    Helm of Radiance, Jade Scepter, Erosion, Chandra''s Grace, Ancient Signet, Death
    Metal, Bancroft''s Talon.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.39
      win: 0.72
      pick: 0.13
      fit: 0.25
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.5
    Ethereal Staff:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.56
      efficiency: 0.42
      win: 0.68
      pick: 0.27
      fit: 0.6
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.51
      efficiency: 0.41
      win: 0.58
      pick: 0.1
      fit: 0.7
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Kinetic Cuirass
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Kinetic Cuirass, Spear
    of the Magus, Rod of Asclepius, Eye of Providence, Ethereal Staff, Obsidian Shard,
    Death Metal, Doom Orb, Spectral Armor, Genji''s Guard, Amanita Charm, Shield of
    the Phoenix, Chandra''s Grace, The World Stone, Chronos'' Pendant, Blood-Bound
    Book, Triton''s Conch, Bragi''s Harp, Breastplate of Valor, Alchemist Coat, Lifebinder,
    Ancient Signet, Bancroft''s Talon.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.39
      win: 0.72
      pick: 0.13
      fit: 0.16
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.37
    Spear of Desolation:
      total: 0.55
      efficiency: 0.42
      win: 0.68
      pick: 0.27
      fit: 0.56
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.44
      efficiency: 0.24
      win: 0.63
      pick: 0.26
      fit: 0.4
    Soul Gem:
      total: 0.51
      efficiency: 0.41
      win: 0.58
      pick: 0.1
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Eye of Providence
  - Kinetic Cuirass
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Blood-Bound Book, Kinetic Cuirass, Lifebinder, Chandra''s Grace, Bancroft''s
    Talon, Eye of Providence, Phoenix Feather, The Cosmic Horror, Spectral Armor,
    Ethereal Staff, Spear of the Magus, Spirit Robe, Genji''s Guard, Erosion, Doom
    Orb, Helm of Radiance, Alchemist Coat, Ancient Signet, Breastplate of Valor, Death
    Metal, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.39
      win: 0.72
      pick: 0.13
      fit: 0.18
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.53
      efficiency: 0.42
      win: 0.68
      pick: 0.27
      fit: 0.43
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.54
      efficiency: 0.41
      win: 0.58
      pick: 0.1
      fit: 0.83
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Spear of the Magus
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
    for this god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus,
    Obsidian Shard, Doom Orb, Kinetic Cuirass, The World Stone, Rod of Asclepius,
    Ethereal Staff, Eye of Providence, Screeching Gargoyle, Spectral Armor, Amanita
    Charm, Void Stone, Void Shield, Blood-Bound Book, Genji''s Guard, Alchemist Coat,
    Shield of the Phoenix, Stone of Binding, Lifebinder, Chronos'' Pendant, Helm of
    Radiance, Chandra''s Grace, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.39
      win: 0.72
      pick: 0.13
      fit: 0.2
    Spear of Desolation:
      total: 0.57
      efficiency: 0.42
      win: 0.68
      pick: 0.27
      fit: 0.68
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.58
    Spear of the Magus:
      total: 0.46
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.24
      win: 0.63
      pick: 0.26
      fit: 0.58
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.58
      pick: 0.1
      fit: 0.78
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
