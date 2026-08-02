---
type: smite-build
god: Morgan Le Fay
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cursed Crown
  aspect_pick_rate: 0.42
  aspect_win_rate: 0.59
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.21
    win_rate: 0.47
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.14
      win_rate: 0.48
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.68
  - name: Soul Reaver
    pick_rate: 0.11
    win_rate: 0.43
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.39
    - name: Shield of the Phoenix
      pick_rate: 0.08
      win_rate: 0.52
  - name: Soul Gem
    pick_rate: 0.14
    win_rate: 0.45
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.52
    - name: Soul Reaver
      pick_rate: 0.08
      win_rate: 0.39
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.33
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.46
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.45
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.41
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.46
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.62
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.55
  source_url: https://smitebrain.com/gods/morgan-le-fay/
  last_verified: '2026-08-01'
  god_win_rate: 0.50997150997151
  god_matches_won: 179
  god_matches_played: 351
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
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
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
    this god: Obsidian Shard, Gluttonous Grimoire, Spear of the Magus, Soul Gem, The
    Cosmic Horror, Chronos'' Pendant, Ethereal Staff, Doom Orb, Rod of Asclepius,
    Blood-Bound Book, Bancroft''s Talon, Ancient Signet, The World Stone, Death Metal,
    Gem of Focus, Polynomicon, Helm of Radiance, Alchemist Coat, Divine Ruin, Book
    of Thoth, Lifebinder, Bragi''s Harp, Jade Scepter, Genji''s Guard, Scepter of
    Dominion.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.48
      efficiency: 0.32
      win: 0.47
      pick: 0.21
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
      win: 0.56
      pick: 0.17
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.41
      win: 0.67
      pick: 0.13
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
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
    god: Obsidian Shard, Gluttonous Grimoire, Spear of the Magus, Soul Gem, The Cosmic
    Horror, Death Metal, Chronos'' Pendant, Bragi''s Harp, Ethereal Staff, Rod of
    Asclepius, Blood-Bound Book, Genji''s Guard, Doom Orb, Bancroft''s Talon, Ancient
    Signet, Triton''s Conch, Gem of Focus, Chandra''s Grace, Breastplate of Valor,
    The World Stone, Shield of the Phoenix, Polynomicon, Helm of Radiance, Spectral
    Armor, Alchemist Coat.'
  slot_scores:
    Death Metal:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.45
      efficiency: 0.32
      win: 0.47
      pick: 0.21
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
      total: 0.54
      efficiency: 0.41
      win: 0.67
      pick: 0.13
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of the Magus
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Spear of the Magus
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
    this god: Obsidian Shard, Amanita Charm, Gluttonous Grimoire, Rod of Asclepius,
    Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Chandra''s Grace, Eye of Providence,
    Lifebinder, Blood-Bound Book, Bancroft''s Talon, Phoenix Feather, Spear of the
    Magus, Spectral Armor, Ethereal Staff, Erosion, Spirit Robe, The Cosmic Horror,
    Genji''s Guard, Alchemist Coat, Helm of Radiance, Jade Scepter, Midgardian Mail,
    Gladiator''s Shield, Chronos'' Pendant.'
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
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.45
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.39
    Obsidian Shard:
      total: 0.51
      efficiency: 0.41
      win: 0.67
      pick: 0.13
      fit: 0.39
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.81
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
  - Spear of Desolation
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
    for this god: Obsidian Shard, Gluttonous Grimoire, Spear of the Magus, The Cosmic
    Horror, Soul Gem, Doom Orb, The World Stone, Ethereal Staff, Chronos'' Pendant,
    Rod of Asclepius, Blood-Bound Book, Screeching Gargoyle, Bancroft''s Talon, Ancient
    Signet, Death Metal, Dreamer''s Idol, Gem of Focus, Polynomicon, Helm of Radiance,
    Genji''s Guard, Alchemist Coat, Divine Ruin, Book of Thoth, Lifebinder, Bragi''s
    Harp.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.48
      efficiency: 0.32
      win: 0.47
      pick: 0.21
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
      win: 0.56
      pick: 0.17
      fit: 0.85
    Obsidian Shard:
      total: 0.58
      efficiency: 0.41
      win: 0.67
      pick: 0.13
      fit: 0.85
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, Soul Gem, Obsidian
    Shard, The Cosmic Horror, Chronos'' Pendant, Ethereal Staff, Doom Orb, Rod of
    Asclepius, Blood-Bound Book, Bancroft''s Talon, Ancient Signet, The World Stone,
    Death Metal, Gem of Focus, Polynomicon, Helm of Radiance, Alchemist Coat, Divine
    Ruin, Book of Thoth, Lifebinder, Bragi''s Harp, Jade Scepter, Genji''s Guard,
    Scepter of Dominion.'
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
      total: 0.48
      efficiency: 0.32
      win: 0.47
      pick: 0.21
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
      total: 0.57
      efficiency: 0.41
      win: 0.67
      pick: 0.13
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Asclepius
  flex_slots:
  - Ethereal Staff
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Obsidian Shard, Rod of Asclepius, Soul Gem, Chandra''s
    Grace, Amanita Charm, Lifebinder, Spear of the Magus, Ethereal Staff, Shield of
    the Phoenix, Kinetic Cuirass, Blood-Bound Book, Eye of Providence, Bancroft''s
    Talon, Phoenix Feather, Spectral Armor, The Cosmic Horror, Alchemist Coat, Jade
    Scepter, Genji''s Guard, Yogi''s Necklace, Scepter of Dominion, Chronos'' Pendant,
    Erosion, Triton''s Conch, Gem of Isolation.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.48
    Ethereal Staff:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.46
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.47
    Obsidian Shard:
      total: 0.52
      efficiency: 0.41
      win: 0.67
      pick: 0.13
      fit: 0.47
    Rod of Asclepius:
      total: 0.49
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: burst
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - The Cosmic Horror
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Obsidian Shard, Gluttonous Grimoire, Soul Gem, Rod of Asclepius, Chandra''s
    Grace, Spear of the Magus, Amanita Charm, Shield of the Phoenix, Blood-Bound Book,
    Lifebinder, Ethereal Staff, Bancroft''s Talon, The Cosmic Horror, Kinetic Cuirass,
    Death Metal, Eye of Providence, Spectral Armor, Genji''s Guard, Triton''s Conch,
    Phoenix Feather, Chronos'' Pendant, Alchemist Coat, Bragi''s Harp, Jade Scepter,
    Yogi''s Necklace, Ancient Signet.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.34
    Ethereal Staff:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.34
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.69
    The Cosmic Horror:
      total: 0.43
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.42
    Spear of the Magus:
      total: 0.46
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.42
    Obsidian Shard:
      total: 0.52
      efficiency: 0.41
      win: 0.67
      pick: 0.13
      fit: 0.42
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Obsidian Shard
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Eye of Providence
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
    this god: Amanita Charm, Obsidian Shard, Gluttonous Grimoire, Rod of Asclepius,
    Shield of the Phoenix, Kinetic Cuirass, Eye of Providence, Chandra''s Grace, Soul
    Gem, Lifebinder, Blood-Bound Book, Phoenix Feather, Spectral Armor, Bancroft''s
    Talon, Spear of the Magus, Ethereal Staff, Erosion, Spirit Robe, Genji''s Guard,
    The Cosmic Horror, Alchemist Coat, Midgardian Mail, Gladiator''s Shield, Breastplate
    of Valor, Helm of Radiance, Jade Scepter, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.51
      efficiency: 0.41
      win: 0.67
      pick: 0.13
      fit: 0.36
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.83
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Ethereal Staff
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Obsidian Shard, Gluttonous Grimoire, Soul Gem, Spear of the Magus,
    Rod of Asclepius, Amanita Charm, Chandra''s Grace, The Cosmic Horror, Lifebinder,
    Ethereal Staff, Shield of the Phoenix, Blood-Bound Book, Kinetic Cuirass, Eye
    of Providence, Bancroft''s Talon, Screeching Gargoyle, Void Stone, Phoenix Feather,
    Spectral Armor, Doom Orb, Alchemist Coat, Void Shield, Jade Scepter, Genji''s
    Guard, Yogi''s Necklace, The World Stone.'
  slot_scores:
    Ethereal Staff:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.9
    Spear of Desolation:
      total: 0.44
      efficiency: 0.32
      win: 0.47
      pick: 0.21
      fit: 0.7
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spear of the Magus:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.59
    Obsidian Shard:
      total: 0.54
      efficiency: 0.41
      win: 0.67
      pick: 0.13
      fit: 0.59
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of the Magus
  - Rod of Asclepius
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Rod of Asclepius, Soul Gem, Chandra''s
    Grace, Amanita Charm, Lifebinder, Spear of the Magus, Ethereal Staff, Shield of
    the Phoenix, Kinetic Cuirass, Blood-Bound Book, Eye of Providence, Bancroft''s
    Talon, Phoenix Feather, Obsidian Shard, Spectral Armor, The Cosmic Horror, Alchemist
    Coat, Jade Scepter, Genji''s Guard, Yogi''s Necklace, Scepter of Dominion, Chronos''
    Pendant, Erosion, Triton''s Conch, Gem of Isolation.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.48
    Ethereal Staff:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.46
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.47
    Rod of Asclepius:
      total: 0.49
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: hybrid
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Asclepius
  flex_slots:
  - Kinetic Cuirass
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Rod of Asclepius,
    Soul Gem, Chandra''s Grace, Amanita Charm, Lifebinder, Spear of the Magus, Ethereal
    Staff, Shield of the Phoenix, Kinetic Cuirass, Blood-Bound Book, Eye of Providence,
    Bancroft''s Talon, Phoenix Feather, Obsidian Shard, Spectral Armor, The Cosmic
    Horror, Alchemist Coat, Jade Scepter, Genji''s Guard, Yogi''s Necklace, Scepter
    of Dominion, Chronos'' Pendant, Erosion, Triton''s Conch, Gem of Isolation.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.48
    Ethereal Staff:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.46
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.47
    Obsidian Shard:
      total: 0.52
      efficiency: 0.41
      win: 0.67
      pick: 0.13
      fit: 0.47
    Rod of Asclepius:
      total: 0.49
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.69
  swaps:
  - added: Obsidian Shard
    removed: Eye of Providence
    reason: community 67% win over 46 matches (vs 51% on this god), taking the model's
      weakest slot from Eye of Providence
  starter: *id001
  aspect: Aspect of the Cursed Crown
---
