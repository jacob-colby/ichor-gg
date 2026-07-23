---
type: smite-build
god: Kukulkan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Squall
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.53
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.88
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.06
      win_rate: 0.5
    - name: Doom Orb
      pick_rate: 0.01
      win_rate: 0.38
  - name: Spear of Desolation
    pick_rate: 0.4
    win_rate: 0.56
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.13
      win_rate: 0.51
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.51
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.63
    alternates:
    - name: Polynomicon
      pick_rate: 0.15
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.15
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.32
      win_rate: 0.54
    - name: Soul Reaver
      pick_rate: 0.08
      win_rate: 0.54
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.42
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.25
      win_rate: 0.54
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.52
  - name: Oracle Staff
    pick_rate: 0.09
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.59
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.64
  source_url: https://smitebrain.com/gods/kukulkan/
  last_verified: '2026-07-23'
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus,
    Obsidian Shard, Doom Orb, The World Stone, Chronos'' Pendant, Rod of Asclepius,
    Ethereal Staff, Blood-Bound Book, Ancient Signet, Death Metal, Bancroft''s Talon,
    Gem of Focus, Polynomicon, Helm of Radiance, Divine Ruin, Alchemist Coat, Lifebinder,
    Bragi''s Harp, Jade Scepter, Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.42
      win: 0.56
      pick: 0.4
      fit: 1.0
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.49
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.24
      win: 0.63
      pick: 0.17
      fit: 0.79
    Obsidian Shard:
      total: 0.49
      efficiency: 0.36
      win: 0.53
      pick: 0.15
      fit: 0.79
    Soul Gem:
      total: 0.52
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Obsidian
    Shard, Doom Orb, Death Metal, The World Stone, Chronos'' Pendant, Bragi''s Harp,
    Rod of Asclepius, Ethereal Staff, Blood-Bound Book, Genji''s Guard, Triton''s
    Conch, Ancient Signet, Bancroft''s Talon, Gem of Focus, Chandra''s Grace, Breastplate
    of Valor, Polynomicon, Helm of Radiance, Divine Ruin, Alchemist Coat, Shield of
    the Phoenix, Spectral Armor.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.42
      win: 0.56
      pick: 0.4
      fit: 0.78
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.46
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.46
      efficiency: 0.24
      win: 0.63
      pick: 0.17
      fit: 0.56
    Obsidian Shard:
      total: 0.46
      efficiency: 0.36
      win: 0.53
      pick: 0.15
      fit: 0.56
    Soul Gem:
      total: 0.5
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Kinetic Cuirass
  - Spear of Desolation
  - The Cosmic Horror
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Rod of Asclepius, Blood-Bound Book, Bancroft''s
    Talon, Gluttonous Grimoire, Shield of the Phoenix, The Cosmic Horror, Kinetic
    Cuirass, Lifebinder, Eye of Providence, Chandra''s Grace, Spear of the Magus,
    Obsidian Shard, Spirit Robe, Genji''s Guard, Phoenix Feather, Doom Orb, Helm of
    Radiance, Spectral Armor, Ethereal Staff, The World Stone, Chronos'' Pendant,
    Breastplate of Valor, Glorious Pridwen, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.39
      win: 0.53
      pick: 0.88
      fit: 0.21
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.49
      efficiency: 0.42
      win: 0.56
      pick: 0.4
      fit: 0.49
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.5
      efficiency: 0.41
      win: 0.5
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
  - Spear of the Magus
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear of the Magus,
    Obsidian Shard, Doom Orb, The World Stone, Rod of Asclepius, Ethereal Staff, Blood-Bound
    Book, Chronos'' Pendant, Screeching Gargoyle, Ancient Signet, Death Metal, Bancroft''s
    Talon, Polynomicon, Gem of Focus, Helm of Radiance, Divine Ruin, Alchemist Coat,
    Genji''s Guard, Lifebinder, Bragi''s Harp, Jade Scepter.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.57
      efficiency: 0.42
      win: 0.56
      pick: 0.4
      fit: 1.0
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.5
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.24
      win: 0.63
      pick: 0.17
      fit: 0.85
    Obsidian Shard:
      total: 0.5
      efficiency: 0.36
      win: 0.53
      pick: 0.15
      fit: 0.85
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
