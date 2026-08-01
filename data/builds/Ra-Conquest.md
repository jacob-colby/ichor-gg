---
type: smite-build
god: Ra
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thermotherapy
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.57
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.58
    win_rate: 0.6
    alternates:
    - name: Book of Thoth
      pick_rate: 0.26
      win_rate: 0.56
    - name: Doom Orb
      pick_rate: 0.05
      win_rate: 0.73
  - name: Book of Thoth
    pick_rate: 0.25
    win_rate: 0.61
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.22
      win_rate: 0.58
    - name: The World Stone
      pick_rate: 0.19
      win_rate: 0.6
  - name: Soul Gem
    pick_rate: 0.22
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.59
    - name: The World Stone
      pick_rate: 0.17
      win_rate: 0.64
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.61
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.21
      win_rate: 0.61
    - name: Nimble Ring
      pick_rate: 0.07
      win_rate: 0.53
  - name: Obsidian Shard
    pick_rate: 0.23
    win_rate: 0.63
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.65
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.54
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.54
    alternates:
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.5
    - name: Nimble Ring
      pick_rate: 0.08
      win_rate: 0.68
  source_url: https://smitebrain.com/gods/ra/
  last_verified: '2026-08-01'
  god_win_rate: 0.6035087719298246
  god_matches_won: 344
  god_matches_played: 570
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
  - Book of Thoth
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Book of Thoth
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
    Chronos'' Pendant, The World Stone, Ethereal Staff, Rod of Asclepius, Blood-Bound
    Book, Gem of Focus, Death Metal, Bancroft''s Talon, Ancient Signet, Helm of Radiance,
    Polynomicon, Genji''s Guard, Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s
    Harp, Jade Scepter, Chandra''s Grace.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.37
      win: 0.61
      pick: 0.25
      fit: 0.41
    Spear of Desolation:
      total: 0.6
      efficiency: 0.43
      win: 0.6
      pick: 0.58
      fit: 1.0
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.72
    Obsidian Shard:
      total: 0.51
      efficiency: 0.32
      win: 0.63
      pick: 0.23
      fit: 0.72
    Soul Gem:
      total: 0.59
      efficiency: 0.41
      win: 0.64
      pick: 0.22
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
    god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom Orb, Death
    Metal, The World Stone, Chronos'' Pendant, Bragi''s Harp, Ethereal Staff, Rod
    of Asclepius, Blood-Bound Book, Genji''s Guard, Triton''s Conch, Bancroft''s Talon,
    Chandra''s Grace, Gem of Focus, Ancient Signet, Breastplate of Valor, Shield of
    the Phoenix, Spectral Armor, Helm of Radiance, Polynomicon, Alchemist Coat, Kinetic
    Cuirass.'
  slot_scores:
    Spear of Desolation:
      total: 0.56
      efficiency: 0.43
      win: 0.6
      pick: 0.58
      fit: 0.78
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.45
      efficiency: 0.22
      win: 0.61
      pick: 0.33
      fit: 0.56
    Obsidian Shard:
      total: 0.49
      efficiency: 0.32
      win: 0.63
      pick: 0.23
      fit: 0.56
    Soul Gem:
      total: 0.57
      efficiency: 0.41
      win: 0.64
      pick: 0.22
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The Cosmic Horror
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - The Cosmic Horror
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
    this god: Amanita Charm, Rod of Asclepius, Blood-Bound Book, Shield of the Phoenix,
    Gluttonous Grimoire, Bancroft''s Talon, The Cosmic Horror, Chandra''s Grace, Kinetic
    Cuirass, Eye of Providence, Lifebinder, Spear of the Magus, Genji''s Guard, Spirit
    Robe, Phoenix Feather, Doom Orb, Spectral Armor, Ethereal Staff, Helm of Radiance,
    Chronos'' Pendant, Glorious Pridwen, Breastplate of Valor, The World Stone, Death
    Metal, Erosion.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.37
      win: 0.61
      pick: 0.25
      fit: 0.2
    Spear of Desolation:
      total: 0.52
      efficiency: 0.43
      win: 0.6
      pick: 0.58
      fit: 0.5
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.36
    Obsidian Shard:
      total: 0.46
      efficiency: 0.32
      win: 0.63
      pick: 0.23
      fit: 0.36
    Amanita Charm:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.58
      efficiency: 0.41
      win: 0.64
      pick: 0.22
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
    for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom
    Orb, The World Stone, Chronos'' Pendant, Screeching Gargoyle, Ethereal Staff,
    Rod of Asclepius, Blood-Bound Book, Death Metal, Bancroft''s Talon, Ancient Signet,
    Gem of Focus, Genji''s Guard, Helm of Radiance, Polynomicon, Chandra''s Grace,
    Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s Harp, Jade Scepter.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.43
      win: 0.6
      pick: 0.58
      fit: 1.0
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.81
    Spear of the Magus:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.81
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.22
      win: 0.61
      pick: 0.33
      fit: 0.81
    Obsidian Shard:
      total: 0.53
      efficiency: 0.32
      win: 0.63
      pick: 0.23
      fit: 0.81
    Soul Gem:
      total: 0.59
      efficiency: 0.41
      win: 0.64
      pick: 0.22
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
  - Jotunn's Revenge
  - Demon Blade
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
      total: 0.23
      efficiency: 0.37
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
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Rod of Asclepius, Amanita Charm, Lifebinder, Gluttonous Grimoire, Chandra''s
    Grace, Spectral Armor, Shield of the Phoenix, Erosion, Kinetic Cuirass, The Cosmic
    Horror, Eye of Providence, Genji''s Guard, Void Stone, Triton''s Conch, Phoenix
    Feather, Ethereal Staff, Spear of the Magus, Blood-Bound Book, Doublet of Binding,
    Doom Orb, Bancroft''s Talon, Chronos'' Pendant, Screeching Gargoyle, Stampede,
    Void Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.54
      efficiency: 0.43
      win: 0.6
      pick: 0.58
      fit: 0.65
    Obsidian Shard:
      total: 0.47
      efficiency: 0.32
      win: 0.63
      pick: 0.23
      fit: 0.39
    Spectral Armor:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.49
    Erosion:
      total: 0.46
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.59
      efficiency: 0.41
      win: 0.64
      pick: 0.22
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Obsidian Shard
  - Spectral Armor
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spectral Armor
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    god: Rod of Asclepius, Amanita Charm, Gluttonous Grimoire, Lifebinder, Triton''s
    Conch, Spectral Armor, The Cosmic Horror, Chandra''s Grace, Spear of the Magus,
    Blood-Bound Book, Shield of the Phoenix, Erosion, Doom Orb, Bancroft''s Talon,
    Death Metal, Ethereal Staff, Kinetic Cuirass, The World Stone, Genji''s Guard,
    Eye of Providence, Void Stone, Chronos'' Pendant, Phoenix Feather, Bragi''s Harp,
    Doublet of Binding.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.43
      win: 0.6
      pick: 0.58
      fit: 0.62
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.45
    Obsidian Shard:
      total: 0.47
      efficiency: 0.32
      win: 0.63
      pick: 0.23
      fit: 0.45
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.59
      efficiency: 0.41
      win: 0.64
      pick: 0.22
      fit: 1.0
    Triton's Conch:
      total: 0.46
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Rod of Asclepius, Spectral Armor, Lifebinder, Shield
    of the Phoenix, Erosion, Chandra''s Grace, Kinetic Cuirass, Eye of Providence,
    Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather, Bancroft''s Talon, Void
    Stone, Stampede, Genji''s Guard, Void Shield, Spirit Robe, The Cosmic Horror,
    Umbral Link, Triton''s Conch, Doublet of Binding, Mystical Mail, Ethereal Staff,
    Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.51
      efficiency: 0.43
      win: 0.6
      pick: 0.58
      fit: 0.38
    Spectral Armor:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.47
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.59
      efficiency: 0.41
      win: 0.64
      pick: 0.22
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Stone
  - Spear of Desolation
  - The Cosmic Horror
  - Obsidian Shard
  - Spectral Armor
  - Soul Gem
  flex_slots:
  - Void Stone
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Rod of Asclepius, Amanita Charm, The Cosmic
    Horror, Void Stone, Lifebinder, Spectral Armor, Spear of the Magus, Chandra''s
    Grace, Doom Orb, Void Shield, Screeching Gargoyle, Erosion, Shield of the Phoenix,
    The World Stone, Kinetic Cuirass, Eye of Providence, Blood-Bound Book, Genji''s
    Guard, Triton''s Conch, Phoenix Feather, Ethereal Staff, Bancroft''s Talon, Doublet
    of Binding.'
  slot_scores:
    Void Stone:
      total: 0.47
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.56
      efficiency: 0.43
      win: 0.6
      pick: 0.58
      fit: 0.74
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.49
      efficiency: 0.32
      win: 0.63
      pick: 0.23
      fit: 0.56
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.59
      efficiency: 0.41
      win: 0.64
      pick: 0.22
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
---
