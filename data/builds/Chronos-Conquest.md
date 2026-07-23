---
type: smite-build
god: Chronos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Relativity
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.47
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.42
    win_rate: 0.44
  - name: Spear of Desolation
    pick_rate: 0.3
    win_rate: 0.47
  - name: Nimble Ring
    pick_rate: 0.19
    win_rate: 0.44
  - name: Rod of Tahuti
    pick_rate: 0.32
    win_rate: 0.46
  - name: Obsidian Shard
    pick_rate: 0.22
    win_rate: 0.49
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/chronos/
  last_verified: '2026-07-17'
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
    this god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus,
    Blood-Bound Book, Doom Orb, Bancroft''s Talon, Bragi''s Harp, Rod of Asclepius,
    The World Stone, Chronos'' Pendant, Ethereal Staff, Ancient Signet, Death Metal,
    Divine Ruin, Bracer of The Abyss, Polynomicon, Helm of Radiance, Gem of Focus,
    Lifebinder, Alchemist Coat, Typhon’s Heart, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.4
      efficiency: 0.4
      win: 0.44
      pick: 0.42
      fit: 0.29
    Spear of Desolation:
      total: 0.46
      efficiency: 0.43
      win: 0.47
      pick: 0.3
      fit: 0.68
    The Cosmic Horror:
      total: 0.42
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Spear of the Magus:
      total: 0.41
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.53
    Obsidian Shard:
      total: 0.41
      efficiency: 0.37
      win: 0.49
      pick: 0.22
      fit: 0.53
    Soul Gem:
      total: 0.46
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.92
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
  - Spear of the Magus
  - Bragi's Harp
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Bragi''s
    Harp, Doom Orb, Death Metal, Blood-Bound Book, The World Stone, Chronos'' Pendant,
    Rod of Asclepius, Bancroft''s Talon, Ethereal Staff, Ancient Signet, Genji''s
    Guard, Triton''s Conch, Gem of Focus, Divine Ruin, Polynomicon, Chandra''s Grace,
    Helm of Radiance, Spectral Armor, Breastplate of Valor, Lifebinder, Kinetic Cuirass.'
  slot_scores:
    Bragi's Harp:
      total: 0.39
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.45
      efficiency: 0.43
      win: 0.47
      pick: 0.3
      fit: 0.62
    The Cosmic Horror:
      total: 0.41
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spear of the Magus:
      total: 0.4
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.45
    Obsidian Shard:
      total: 0.4
      efficiency: 0.37
      win: 0.49
      pick: 0.22
      fit: 0.45
    Soul Gem:
      total: 0.44
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.81
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Blood-Bound Book
  - Book of Thoth
  - Kinetic Cuirass
  - Spear of Desolation
  - The Cosmic Horror
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Book of Thoth
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
    this god: Soul Gem, Blood-Bound Book, Amanita Charm, Rod of Asclepius, Bancroft''s
    Talon, Gluttonous Grimoire, Shield of the Phoenix, Lifebinder, The Cosmic Horror,
    Kinetic Cuirass, Chandra''s Grace, Eye of Providence, Spirit Robe, Spear of the
    Magus, Phoenix Feather, Helm of Radiance, Spectral Armor, Ethereal Staff, Doom
    Orb, Genji''s Guard, Ancient Signet, Bragi''s Harp, Sphere of Negation, Glorious
    Pridwen, Chronos'' Pendant, Death Metal.'
  slot_scores:
    Blood-Bound Book:
      total: 0.42
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.55
    Book of Thoth:
      total: 0.38
      efficiency: 0.4
      win: 0.44
      pick: 0.42
      fit: 0.17
    Kinetic Cuirass:
      total: 0.38
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.37
    Spear of Desolation:
      total: 0.42
      efficiency: 0.43
      win: 0.47
      pick: 0.3
      fit: 0.38
    The Cosmic Horror:
      total: 0.38
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.3
    Soul Gem:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Doom Orb
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
    Doom Orb, The World Stone, Blood-Bound Book, Bancroft''s Talon, Rod of Asclepius,
    Screeching Gargoyle, Ethereal Staff, Bragi''s Harp, Ancient Signet, Chronos''
    Pendant, Death Metal, Divine Ruin, Polynomicon, Helm of Radiance, Bracer of The
    Abyss, Lifebinder, Alchemist Coat, Gem of Focus, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.47
      efficiency: 0.43
      win: 0.47
      pick: 0.3
      fit: 0.76
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.65
    Doom Orb:
      total: 0.42
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spear of the Magus:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    Obsidian Shard:
      total: 0.43
      efficiency: 0.37
      win: 0.49
      pick: 0.22
      fit: 0.65
    Soul Gem:
      total: 0.46
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.97
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
  - Obsidian Shard
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Rod of Asclepius, Gluttonous Grimoire, Spectral Armor, Amanita
    Charm, Lifebinder, The Cosmic Horror, Erosion, Triton''s Conch, Blood-Bound Book,
    Spear of the Magus, Ethereal Staff, Genji''s Guard, Void Stone, Kinetic Cuirass,
    Doom Orb, Chronos'' Pendant, Bancroft''s Talon, Eye of Providence, Chandra''s
    Grace, Bragi''s Harp, Shield of the Phoenix, Doublet of Binding, The World Stone,
    Ancient Signet.'
  slot_scores:
    Spear of Desolation:
      total: 0.44
      efficiency: 0.43
      win: 0.47
      pick: 0.3
      fit: 0.54
    The Cosmic Horror:
      total: 0.39
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.34
    Obsidian Shard:
      total: 0.39
      efficiency: 0.37
      win: 0.49
      pick: 0.22
      fit: 0.34
    Spectral Armor:
      total: 0.4
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.4
    Erosion:
      total: 0.39
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.5
    Soul Gem:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Relativity
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
  - The Cosmic Horror
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Rod of Asclepius, Gluttonous Grimoire, Triton''s Conch, Spectral
    Armor, The Cosmic Horror, Lifebinder, Amanita Charm, Spear of the Magus, Bragi''s
    Harp, Death Metal, Doom Orb, Blood-Bound Book, Erosion, Ethereal Staff, Chronos''
    Pendant, Bancroft''s Talon, The World Stone, Void Stone, Genji''s Guard, Kinetic
    Cuirass, Ancient Signet, Eye of Providence, Chandra''s Grace, Stampede.'
  slot_scores:
    Spear of Desolation:
      total: 0.44
      efficiency: 0.43
      win: 0.47
      pick: 0.3
      fit: 0.55
    The Cosmic Horror:
      total: 0.4
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.39
    Obsidian Shard:
      total: 0.39
      efficiency: 0.37
      win: 0.49
      pick: 0.22
      fit: 0.39
    Spectral Armor:
      total: 0.4
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.36
    Soul Gem:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.4
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
  aspect: Aspect of Relativity
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
    this god: Soul Gem, Amanita Charm, Rod of Asclepius, Lifebinder, Spectral Armor,
    Blood-Bound Book, Shield of the Phoenix, Erosion, Bancroft''s Talon, Chandra''s
    Grace, Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Umbral Link, Phoenix
    Feather, Spirit Robe, Void Stone, The Cosmic Horror, Stampede, Triton''s Conch,
    Genji''s Guard, Void Shield, Ethereal Staff, Spear of the Magus, Glorious Pridwen,
    Mystical Mail.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.39
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.41
      efficiency: 0.43
      win: 0.47
      pick: 0.3
      fit: 0.35
    Spectral Armor:
      total: 0.42
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.92
    Erosion:
      total: 0.41
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.62
    Soul Gem:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Stone
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
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Void Stone, The
    Cosmic Horror, Spear of the Magus, Spectral Armor, Amanita Charm, Void Shield,
    Doom Orb, Screeching Gargoyle, Lifebinder, Erosion, The World Stone, Triton''s
    Conch, Blood-Bound Book, Ethereal Staff, Kinetic Cuirass, Genji''s Guard, Eye
    of Providence, Bancroft''s Talon, Chronos'' Pendant, Chandra''s Grace, Stampede,
    Ancient Signet.'
  slot_scores:
    Void Stone:
      total: 0.41
      efficiency: 0.31
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.46
      efficiency: 0.43
      win: 0.47
      pick: 0.3
      fit: 0.64
    The Cosmic Horror:
      total: 0.41
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Spear of the Magus:
      total: 0.4
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.49
    Obsidian Shard:
      total: 0.41
      efficiency: 0.37
      win: 0.49
      pick: 0.22
      fit: 0.49
    Soul Gem:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Relativity
---
