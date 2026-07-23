---
type: smite-build
god: Agni
mode: Conquest
builds:
- source: community
  aspect: Aspect of Combustion
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.3
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.59
    win_rate: 0.51
  - name: Book of Thoth
    pick_rate: 0.26
    win_rate: 0.46
  - name: Soul Gem
    pick_rate: 0.3
    win_rate: 0.52
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.53
  - name: Obsidian Shard
    pick_rate: 0.25
    win_rate: 0.58
  - name: Evil Eye
    pick_rate: 0.12
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/agni/
  last_verified: '2026-07-17'
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
    this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom Orb,
    The World Stone, Chronos'' Pendant, Rod of Asclepius, Blood-Bound Book, Ethereal
    Staff, Ancient Signet, Death Metal, Gem of Focus, Bancroft''s Talon, Divine Ruin,
    Polynomicon, Helm of Radiance, Lifebinder, Bragi''s Harp, Alchemist Coat, Jade
    Scepter, Gem of Isolation, Scepter of Dominion.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.43
      win: 0.51
      pick: 0.59
      fit: 1.0
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.44
      efficiency: 0.25
      win: 0.53
      pick: 0.33
      fit: 0.79
    Obsidian Shard:
      total: 0.49
      efficiency: 0.37
      win: 0.58
      pick: 0.25
      fit: 0.79
    Soul Gem:
      total: 0.52
      efficiency: 0.41
      win: 0.52
      pick: 0.3
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom Orb, Death
    Metal, The World Stone, Chronos'' Pendant, Bragi''s Harp, Rod of Asclepius, Blood-Bound
    Book, Ethereal Staff, Ancient Signet, Triton''s Conch, Gem of Focus, Genji''s
    Guard, Bancroft''s Talon, Divine Ruin, Polynomicon, Chandra''s Grace, Helm of
    Radiance, Breastplate of Valor, Lifebinder, Alchemist Coat, Jade Scepter.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.43
      win: 0.51
      pick: 0.59
      fit: 0.78
    The Cosmic Horror:
      total: 0.42
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.41
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.41
      efficiency: 0.25
      win: 0.53
      pick: 0.33
      fit: 0.56
    Obsidian Shard:
      total: 0.45
      efficiency: 0.37
      win: 0.58
      pick: 0.25
      fit: 0.56
    Soul Gem:
      total: 0.5
      efficiency: 0.41
      win: 0.52
      pick: 0.3
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
    this god: Amanita Charm, Rod of Asclepius, Blood-Bound Book, Bancroft''s Talon,
    Gluttonous Grimoire, Shield of the Phoenix, The Cosmic Horror, Lifebinder, Kinetic
    Cuirass, Spear of the Magus, Eye of Providence, Chandra''s Grace, Spirit Robe,
    Doom Orb, Helm of Radiance, Phoenix Feather, Ethereal Staff, Genji''s Guard, Spectral
    Armor, Glorious Pridwen, Sphere of Negation, Ancient Signet, Chronos'' Pendant,
    The World Stone.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.39
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.49
      efficiency: 0.43
      win: 0.51
      pick: 0.59
      fit: 0.49
    The Cosmic Horror:
      total: 0.4
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.39
    Obsidian Shard:
      total: 0.43
      efficiency: 0.37
      win: 0.58
      pick: 0.25
      fit: 0.39
    Amanita Charm:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.5
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 0.89
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
    for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom
    Orb, The World Stone, Rod of Asclepius, Blood-Bound Book, Chronos'' Pendant, Ethereal
    Staff, Ancient Signet, Screeching Gargoyle, Death Metal, Bancroft''s Talon, Divine
    Ruin, Polynomicon, Helm of Radiance, Gem of Focus, Lifebinder, Bragi''s Harp,
    Alchemist Coat, Dreamer''s Idol, Jade Scepter.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.43
      win: 0.51
      pick: 0.59
      fit: 1.0
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.45
      efficiency: 0.25
      win: 0.53
      pick: 0.33
      fit: 0.85
    Obsidian Shard:
      total: 0.5
      efficiency: 0.37
      win: 0.58
      pick: 0.25
      fit: 0.85
    Soul Gem:
      total: 0.52
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Tyrfing
  - Rage
  - Bragi's Harp
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Rage
  - Bragi's Harp
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
    Tyrfing:
      total: 0.24
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rage:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.23
      efficiency: 0.36
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
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.23
      efficiency: 0.23
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
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
    this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom Orb,
    The World Stone, Chronos'' Pendant, Rod of Asclepius, Blood-Bound Book, Ethereal
    Staff, Bragi''s Harp, Ancient Signet, Death Metal, Bancroft''s Talon, Gem of Focus,
    Divine Ruin, Polynomicon, Helm of Radiance, Bracer of The Abyss, Lifebinder, Alchemist
    Coat, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.43
      win: 0.51
      pick: 0.59
      fit: 0.86
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
    Rod of Tahuti:
      total: 0.42
      efficiency: 0.25
      win: 0.53
      pick: 0.33
      fit: 0.68
    Obsidian Shard:
      total: 0.47
      efficiency: 0.37
      win: 0.58
      pick: 0.25
      fit: 0.68
    Soul Gem:
      total: 0.51
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 0.96
  starter: *id001
  aspect: Aspect of Combustion
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom Orb, Death
    Metal, Bragi''s Harp, The World Stone, Chronos'' Pendant, Rod of Asclepius, Blood-Bound
    Book, Ethereal Staff, Ancient Signet, Triton''s Conch, Genji''s Guard, Gem of
    Focus, Bancroft''s Talon, Divine Ruin, Polynomicon, Chandra''s Grace, Helm of
    Radiance, Breastplate of Valor, Lifebinder, Alchemist Coat, Jade Scepter.'
  slot_scores:
    Spear of Desolation:
      total: 0.52
      efficiency: 0.43
      win: 0.51
      pick: 0.59
      fit: 0.71
    The Cosmic Horror:
      total: 0.41
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of the Magus:
      total: 0.41
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.4
      efficiency: 0.25
      win: 0.53
      pick: 0.33
      fit: 0.51
    Obsidian Shard:
      total: 0.45
      efficiency: 0.37
      win: 0.58
      pick: 0.25
      fit: 0.51
    Soul Gem:
      total: 0.49
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 0.81
  starter: *id001
  aspect: Aspect of Combustion
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
    this god: Amanita Charm, Rod of Asclepius, Blood-Bound Book, Bancroft''s Talon,
    Shield of the Phoenix, Gluttonous Grimoire, The Cosmic Horror, Lifebinder, Kinetic
    Cuirass, Spear of the Magus, Chandra''s Grace, Eye of Providence, Spirit Robe,
    Phoenix Feather, Doom Orb, Helm of Radiance, Ethereal Staff, Genji''s Guard, Spectral
    Armor, Ancient Signet, Sphere of Negation, Glorious Pridwen, Chronos'' Pendant,
    The World Stone.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.39
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.49
      efficiency: 0.43
      win: 0.51
      pick: 0.59
      fit: 0.46
    The Cosmic Horror:
      total: 0.39
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.36
    Obsidian Shard:
      total: 0.43
      efficiency: 0.37
      win: 0.58
      pick: 0.25
      fit: 0.36
    Amanita Charm:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.5
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 0.86
  starter: *id001
  aspect: Aspect of Combustion
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
    for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom
    Orb, The World Stone, Rod of Asclepius, Blood-Bound Book, Ethereal Staff, Chronos''
    Pendant, Screeching Gargoyle, Ancient Signet, Bragi''s Harp, Death Metal, Bancroft''s
    Talon, Divine Ruin, Polynomicon, Helm of Radiance, Gem of Focus, Lifebinder, Alchemist
    Coat, Jade Scepter, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.43
      win: 0.51
      pick: 0.59
      fit: 0.9
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.44
      efficiency: 0.25
      win: 0.53
      pick: 0.33
      fit: 0.77
    Obsidian Shard:
      total: 0.49
      efficiency: 0.37
      win: 0.58
      pick: 0.25
      fit: 0.77
    Soul Gem:
      total: 0.52
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 1.0
  starter: *id001
  aspect: Aspect of Combustion
---
