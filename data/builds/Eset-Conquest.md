---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.39
  aspect_win_rate: 0.63
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.33
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.64
    - name: Runeforged Hammer
      pick_rate: 0.1
      win_rate: 0.66
  - name: Soul Gem
    pick_rate: 0.12
    win_rate: 0.68
    alternates:
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.61
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.65
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.59
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.71
  - name: Dwarven Plate
    pick_rate: 0.06
    win_rate: 0.7
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.66
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.62
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.75
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.38
    - name: Blinking Abyss
      pick_rate: 0.04
      win_rate: 0.8
  source_url: https://smitebrain.com/gods/eset/
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
  - Rod of Tahuti
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
    Rod of Tahuti, Doom Orb, The World Stone, Chronos'' Pendant, Rod of Asclepius,
    Ethereal Staff, Blood-Bound Book, Ancient Signet, Death Metal, Gem of Focus, Bancroft''s
    Talon, Polynomicon, Helm of Radiance, Divine Ruin, Alchemist Coat, Lifebinder,
    Bragi''s Harp, Book of Thoth, Genji''s Guard, Jade Scepter, Scepter of Dominion.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.42
      win: 0.56
      pick: 0.33
      fit: 1.0
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.49
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.24
      win: 0.63
      pick: 0.13
      fit: 0.77
    Obsidian Shard:
      total: 0.51
      efficiency: 0.36
      win: 0.58
      pick: 0.16
      fit: 0.77
    Soul Gem:
      total: 0.61
      efficiency: 0.41
      win: 0.68
      pick: 0.12
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
  - Rod of Tahuti
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
    god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom
    Orb, Death Metal, The World Stone, Chronos'' Pendant, Bragi''s Harp, Rod of Asclepius,
    Ethereal Staff, Blood-Bound Book, Genji''s Guard, Triton''s Conch, Ancient Signet,
    Bancroft''s Talon, Gem of Focus, Chandra''s Grace, Breastplate of Valor, Polynomicon,
    Helm of Radiance, Divine Ruin, Alchemist Coat, Shield of the Phoenix, Spectral
    Armor.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.42
      win: 0.56
      pick: 0.33
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
      pick: 0.13
      fit: 0.56
    Obsidian Shard:
      total: 0.48
      efficiency: 0.36
      win: 0.58
      pick: 0.16
      fit: 0.56
    Soul Gem:
      total: 0.59
      efficiency: 0.41
      win: 0.68
      pick: 0.12
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - The Cosmic Horror
  - Obsidian Shard
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
    Talon, Shield of the Phoenix, Gluttonous Grimoire, The Cosmic Horror, Kinetic
    Cuirass, Lifebinder, Chandra''s Grace, Eye of Providence, Spear of the Magus,
    Spirit Robe, Genji''s Guard, Phoenix Feather, Doom Orb, Helm of Radiance, Spectral
    Armor, Ethereal Staff, Chronos'' Pendant, Breastplate of Valor, Glorious Pridwen,
    The World Stone, Ancient Signet, Death Metal.'
  slot_scores:
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
      pick: 0.33
      fit: 0.5
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.38
    Obsidian Shard:
      total: 0.45
      efficiency: 0.36
      win: 0.58
      pick: 0.16
      fit: 0.38
    Amanita Charm:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.59
      efficiency: 0.41
      win: 0.68
      pick: 0.12
      fit: 0.9
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
  - Spear of the Magus
  - Rod of Tahuti
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
    for this god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus,
    Rod of Tahuti, Doom Orb, The World Stone, Chronos'' Pendant, Rod of Asclepius,
    Ethereal Staff, Blood-Bound Book, Screeching Gargoyle, Ancient Signet, Death Metal,
    Bancroft''s Talon, Gem of Focus, Polynomicon, Genji''s Guard, Helm of Radiance,
    Divine Ruin, Alchemist Coat, Lifebinder, Bragi''s Harp, Book of Thoth, Jade Scepter.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.42
      win: 0.56
      pick: 0.33
      fit: 1.0
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.84
    Spear of the Magus:
      total: 0.5
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.24
      win: 0.63
      pick: 0.13
      fit: 0.84
    Obsidian Shard:
      total: 0.52
      efficiency: 0.36
      win: 0.58
      pick: 0.16
      fit: 0.84
    Soul Gem:
      total: 0.61
      efficiency: 0.41
      win: 0.68
      pick: 0.12
      fit: 1.0
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
