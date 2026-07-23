---
type: smite-build
god: Nut
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cosmos
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.4
  slot_order:
  - name: Tyrfing
    pick_rate: 0.36
    win_rate: 0.58
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.29
      win_rate: 0.47
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.5
  - name: Bragi's Harp
    pick_rate: 0.18
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.52
  - name: Barbed Carver
    pick_rate: 0.11
    win_rate: 0.57
    alternates:
    - name: Avenging Blade
      pick_rate: 0.11
      win_rate: 0.69
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.53
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.55
    alternates:
    - name: Titan's Bane
      pick_rate: 0.13
      win_rate: 0.51
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.31
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.54
    alternates:
    - name: Titan's Bane
      pick_rate: 0.11
      win_rate: 0.6
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.49
  - name: Void Shard
    pick_rate: 0.06
    win_rate: 0.71
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.65
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 0.58
  source_url: https://smitebrain.com/gods/nut/
  last_verified: '2026-07-23'
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Bragi's Harp
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Spear of the Magus
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
    this god: Soul Gem, Gluttonous Grimoire, Spear of Desolation, The Cosmic Horror,
    Obsidian Shard, Spear of the Magus, Blood-Bound Book, Doom Orb, Bancroft''s Talon,
    Bracer of The Abyss, Rod of Asclepius, Ethereal Staff, The World Stone, Chronos''
    Pendant, Nimble Ring, Ancient Signet, Death Metal, Genji''s Guard, Polynomicon,
    Helm of Radiance, Divine Ruin, Alchemist Coat, Gem of Focus, Lifebinder, Spectral
    Armor, Book of Thoth.'
  slot_scores:
    Bragi's Harp:
      total: 0.49
      efficiency: 0.35
      win: 0.58
      pick: 0.18
      fit: 0.64
    Spear of Desolation:
      total: 0.46
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spear of the Magus:
      total: 0.44
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.45
    Obsidian Shard:
      total: 0.44
      efficiency: 0.36
      win: 0.54
      pick: 0.13
      fit: 0.45
    Soul Gem:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Bragi's Harp
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Spear of Desolation, The Cosmic Horror, Obsidian
    Shard, Spear of the Magus, Death Metal, Doom Orb, Blood-Bound Book, Bancroft''s
    Talon, The World Stone, Rod of Asclepius, Chronos'' Pendant, Ethereal Staff, Genji''s
    Guard, Ancient Signet, Bracer of The Abyss, Chandra''s Grace, Spectral Armor,
    Breastplate of Valor, Triton''s Conch, Kinetic Cuirass, Gem of Focus, Polynomicon,
    Helm of Radiance, Divine Ruin.'
  slot_scores:
    Bragi's Harp:
      total: 0.49
      efficiency: 0.35
      win: 0.58
      pick: 0.18
      fit: 0.62
    Spear of Desolation:
      total: 0.46
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.4
    Spear of the Magus:
      total: 0.43
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.4
    Obsidian Shard:
      total: 0.44
      efficiency: 0.36
      win: 0.54
      pick: 0.13
      fit: 0.4
    Soul Gem:
      total: 0.48
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Blood-Bound Book
  - Kinetic Cuirass
  - Bragi's Harp
  - Spear of Desolation
  - The Cosmic Horror
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Blood-Bound Book, Amanita Charm, Bancroft''s Talon, Rod of
    Asclepius, Gluttonous Grimoire, Shield of the Phoenix, Chandra''s Grace, Lifebinder,
    The Cosmic Horror, Kinetic Cuirass, Spear of Desolation, Eye of Providence, Phoenix
    Feather, Spirit Robe, Genji''s Guard, Spear of the Magus, Spectral Armor, Ethereal
    Staff, Doom Orb, Helm of Radiance, Breastplate of Valor, Ancient Signet, Death
    Metal, Chronos'' Pendant, The World Stone.'
  slot_scores:
    Blood-Bound Book:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.52
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.46
      efficiency: 0.35
      win: 0.58
      pick: 0.18
      fit: 0.43
    Spear of Desolation:
      total: 0.43
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.36
    The Cosmic Horror:
      total: 0.43
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.28
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
  - Bragi's Harp
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of Desolation,
    Obsidian Shard, Spear of the Magus, Doom Orb, The World Stone, Blood-Bound Book,
    Bancroft''s Talon, Screeching Gargoyle, Rod of Asclepius, Ethereal Staff, Bracer
    of The Abyss, Chronos'' Pendant, Ancient Signet, Death Metal, Genji''s Guard,
    Nimble Ring, Spectral Armor, Polynomicon, Kinetic Cuirass, Helm of Radiance, Divine
    Ruin, Alchemist Coat.'
  slot_scores:
    Bragi's Harp:
      total: 0.47
      efficiency: 0.35
      win: 0.58
      pick: 0.18
      fit: 0.53
    Spear of Desolation:
      total: 0.47
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.66
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
    Obsidian Shard:
      total: 0.46
      efficiency: 0.36
      win: 0.54
      pick: 0.13
      fit: 0.56
    Soul Gem:
      total: 0.5
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.86
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
      win: 0.58
      pick: 0.36
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
