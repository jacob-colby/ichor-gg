---
type: smite-build
god: Agni
mode: Conquest
builds:
- source: community
  aspect: Aspect of Combustion
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.53
    win_rate: 0.5
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.16
      win_rate: 0.57
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.46
  - name: Book of Thoth
    pick_rate: 0.16
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.61
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.56
  - name: Soul Gem
    pick_rate: 0.33
    win_rate: 0.56
    alternates:
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.45
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.48
  - name: Rod of Tahuti
    pick_rate: 0.36
    win_rate: 0.54
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.4
    - name: Soul Gem
      pick_rate: 0.06
      win_rate: 0.65
  - name: Obsidian Shard
    pick_rate: 0.24
    win_rate: 0.49
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.57
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.39
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.45
    alternates:
    - name: Void Shard
      pick_rate: 0.09
      win_rate: 0.4
    - name: Dreamer's Idol
      pick_rate: 0.07
      win_rate: 0.47
  source_url: https://smitebrain.com/gods/agni/
  last_verified: '2026-08-01'
  god_win_rate: 0.513953488372093
  god_matches_won: 221
  god_matches_played: 430
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
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
    this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Chronos''
    Pendant, Ethereal Staff, Doom Orb, Rod of Asclepius, Blood-Bound Book, Bancroft''s
    Talon, Ancient Signet, The World Stone, Death Metal, Gem of Focus, Polynomicon,
    Helm of Radiance, Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s Harp, Jade
    Scepter, Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Spear of Desolation:
      total: 0.51
      efficiency: 0.32
      win: 0.5
      pick: 0.53
      fit: 1.0
    The Cosmic Horror:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.26
      win: 0.54
      pick: 0.36
      fit: 0.79
    Obsidian Shard:
      total: 0.49
      efficiency: 0.41
      win: 0.49
      pick: 0.24
      fit: 0.79
    Soul Gem:
      total: 0.55
      efficiency: 0.36
      win: 0.56
      pick: 0.33
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Death Metal
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
    god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Death Metal,
    Chronos'' Pendant, Bragi''s Harp, Ethereal Staff, Rod of Asclepius, Blood-Bound
    Book, Genji''s Guard, Doom Orb, Bancroft''s Talon, Ancient Signet, Triton''s Conch,
    Gem of Focus, Chandra''s Grace, Breastplate of Valor, The World Stone, Shield
    of the Phoenix, Polynomicon, Helm of Radiance, Spectral Armor, Alchemist Coat.'
  slot_scores:
    Death Metal:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.48
      efficiency: 0.32
      win: 0.5
      pick: 0.53
      fit: 0.78
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.47
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.46
      efficiency: 0.41
      win: 0.49
      pick: 0.24
      fit: 0.56
    Soul Gem:
      total: 0.53
      efficiency: 0.36
      win: 0.56
      pick: 0.33
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Spear of the Magus
  - Spectral Armor
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Spectral Armor
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
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Shield of the
    Phoenix, Kinetic Cuirass, Chandra''s Grace, Eye of Providence, Lifebinder, Blood-Bound
    Book, Bancroft''s Talon, Phoenix Feather, Spear of the Magus, Spectral Armor,
    Ethereal Staff, Erosion, Spirit Robe, The Cosmic Horror, Genji''s Guard, Alchemist
    Coat, Helm of Radiance, Jade Scepter, Midgardian Mail, Gladiator''s Shield, Chronos''
    Pendant.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.51
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of the Magus:
      total: 0.45
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.39
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.35
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.53
      efficiency: 0.36
      win: 0.56
      pick: 0.33
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
  - The Cosmic Horror
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
    for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Doom
    Orb, The World Stone, Ethereal Staff, Chronos'' Pendant, Rod of Asclepius, Blood-Bound
    Book, Screeching Gargoyle, Bancroft''s Talon, Ancient Signet, Death Metal, Dreamer''s
    Idol, Gem of Focus, Polynomicon, Helm of Radiance, Genji''s Guard, Alchemist Coat,
    Divine Ruin, Lifebinder, Bragi''s Harp.'
  slot_scores:
    Spear of Desolation:
      total: 0.51
      efficiency: 0.32
      win: 0.5
      pick: 0.53
      fit: 1.0
    The Cosmic Horror:
      total: 0.49
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.52
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.26
      win: 0.54
      pick: 0.36
      fit: 0.85
    Obsidian Shard:
      total: 0.5
      efficiency: 0.41
      win: 0.49
      pick: 0.24
      fit: 0.85
    Soul Gem:
      total: 0.55
      efficiency: 0.36
      win: 0.56
      pick: 0.33
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
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
    Golden Blade:
      total: 0.22
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Tyrfing:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.24
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.22
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - The Cosmic Horror
  - Chronos' Pendant
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Chronos'' Pendant, Ethereal Staff, Doom Orb, Rod of Asclepius, Blood-Bound Book,
    Bancroft''s Talon, Ancient Signet, The World Stone, Death Metal, Gem of Focus,
    Polynomicon, Helm of Radiance, Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s
    Harp, Jade Scepter, Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Chronos' Pendant:
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.51
      efficiency: 0.32
      win: 0.5
      pick: 0.53
      fit: 1.0
    The Cosmic Horror:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.49
      efficiency: 0.41
      win: 0.49
      pick: 0.24
      fit: 0.79
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
  - The Cosmic Horror
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
    this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Chronos''
    Pendant, Ethereal Staff, Rod of Asclepius, Blood-Bound Book, Doom Orb, Bragi''s
    Harp, Bancroft''s Talon, Ancient Signet, Death Metal, Gem of Focus, The World
    Stone, Bracer of The Abyss, Polynomicon, Helm of Radiance, Alchemist Coat, Divine
    Ruin, Lifebinder, Genji''s Guard, Jade Scepter.'
  slot_scores:
    Spear of Desolation:
      total: 0.49
      efficiency: 0.32
      win: 0.5
      pick: 0.53
      fit: 0.86
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.49
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.68
    Rod of Tahuti:
      total: 0.45
      efficiency: 0.26
      win: 0.54
      pick: 0.36
      fit: 0.68
    Obsidian Shard:
      total: 0.48
      efficiency: 0.41
      win: 0.49
      pick: 0.24
      fit: 0.68
    Soul Gem:
      total: 0.54
      efficiency: 0.36
      win: 0.56
      pick: 0.33
      fit: 0.96
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Death Metal
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
    god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Death Metal,
    Bragi''s Harp, Chronos'' Pendant, Ethereal Staff, Rod of Asclepius, Blood-Bound
    Book, Genji''s Guard, Bancroft''s Talon, Doom Orb, Ancient Signet, Chandra''s
    Grace, Triton''s Conch, Gem of Focus, Breastplate of Valor, The World Stone, Shield
    of the Phoenix, Spectral Armor, Polynomicon, Helm of Radiance, Kinetic Cuirass,
    Alchemist Coat.'
  slot_scores:
    Death Metal:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.47
      efficiency: 0.32
      win: 0.5
      pick: 0.53
      fit: 0.71
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of the Magus:
      total: 0.47
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.51
    Obsidian Shard:
      total: 0.45
      efficiency: 0.41
      win: 0.49
      pick: 0.24
      fit: 0.51
    Soul Gem:
      total: 0.52
      efficiency: 0.36
      win: 0.56
      pick: 0.33
      fit: 0.81
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Spear of the Magus
  - Spectral Armor
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Spectral Armor
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
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Shield of the
    Phoenix, Kinetic Cuirass, Chandra''s Grace, Lifebinder, Eye of Providence, Blood-Bound
    Book, Bancroft''s Talon, Phoenix Feather, Spear of the Magus, Spectral Armor,
    Ethereal Staff, Erosion, Spirit Robe, Genji''s Guard, The Cosmic Horror, Alchemist
    Coat, Helm of Radiance, Jade Scepter, Midgardian Mail, Chronos'' Pendant, Breastplate
    of Valor, Gladiator''s Shield.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spear of the Magus:
      total: 0.45
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.36
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.52
      efficiency: 0.36
      win: 0.56
      pick: 0.33
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
  - The Cosmic Horror
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
    for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Doom
    Orb, The World Stone, Ethereal Staff, Rod of Asclepius, Blood-Bound Book, Chronos''
    Pendant, Screeching Gargoyle, Bancroft''s Talon, Ancient Signet, Death Metal,
    Bragi''s Harp, Polynomicon, Genji''s Guard, Dreamer''s Idol, Helm of Radiance,
    Gem of Focus, Alchemist Coat, Bracer of The Abyss, Divine Ruin.'
  slot_scores:
    Spear of Desolation:
      total: 0.5
      efficiency: 0.32
      win: 0.5
      pick: 0.53
      fit: 0.9
    The Cosmic Horror:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.26
      win: 0.54
      pick: 0.36
      fit: 0.77
    Obsidian Shard:
      total: 0.49
      efficiency: 0.41
      win: 0.49
      pick: 0.24
      fit: 0.77
    Soul Gem:
      total: 0.55
      efficiency: 0.36
      win: 0.56
      pick: 0.33
      fit: 1.0
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Chronos' Pendant
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Chronos'' Pendant, Ethereal Staff, Rod of Asclepius, Blood-Bound Book, Doom Orb,
    Bragi''s Harp, Bancroft''s Talon, Ancient Signet, Death Metal, Gem of Focus, The
    World Stone, Bracer of The Abyss, Polynomicon, Helm of Radiance, Alchemist Coat,
    Divine Ruin, Lifebinder, Genji''s Guard, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.45
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spear of Desolation:
      total: 0.49
      efficiency: 0.32
      win: 0.5
      pick: 0.53
      fit: 0.86
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.49
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.68
    Obsidian Shard:
      total: 0.48
      efficiency: 0.41
      win: 0.49
      pick: 0.24
      fit: 0.68
  starter: *id001
  aspect: Aspect of Combustion
---
