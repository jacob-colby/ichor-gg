---
type: smite-build
god: Ra
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thermotherapy
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.62
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.49
    win_rate: 0.59
    alternates:
    - name: Book of Thoth
      pick_rate: 0.34
      win_rate: 0.57
    - name: Doom Orb
      pick_rate: 0.04
      win_rate: 0.62
  - name: Book of Thoth
    pick_rate: 0.22
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.29
      win_rate: 0.57
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.62
  - name: Soul Gem
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: The World Stone
      pick_rate: 0.16
      win_rate: 0.56
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.6
  - name: Rod of Tahuti
    pick_rate: 0.34
    win_rate: 0.62
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.18
      win_rate: 0.53
    - name: Soul Gem
      pick_rate: 0.06
      win_rate: 0.66
  - name: Obsidian Shard
    pick_rate: 0.24
    win_rate: 0.65
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.17
      win_rate: 0.66
    - name: Nimble Ring
      pick_rate: 0.09
      win_rate: 0.72
  - name: Evil Eye
    pick_rate: 0.1
    win_rate: 0.46
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.72
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.55
  source_url: https://smitebrain.com/gods/ra/
  last_verified: '2026-07-22'
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
  - Spear of the Magus
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
    Chronos'' Pendant, The World Stone, Rod of Asclepius, Gem of Focus, Blood-Bound
    Book, Ethereal Staff, Ancient Signet, Death Metal, Bancroft''s Talon, Divine Ruin,
    Polynomicon, Helm of Radiance, Lifebinder, Bragi''s Harp, Alchemist Coat, Jade
    Scepter, Genji''s Guard, Chandra''s Grace.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.43
      win: 0.59
      pick: 0.49
      fit: 1.0
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
    Rod of Tahuti:
      total: 0.46
      efficiency: 0.25
      win: 0.62
      pick: 0.34
      fit: 0.72
    Obsidian Shard:
      total: 0.5
      efficiency: 0.37
      win: 0.65
      pick: 0.24
      fit: 0.72
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.57
      pick: 0.27
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
  - The Cosmic Horror
  - Spear of the Magus
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
      total: 0.55
      efficiency: 0.43
      win: 0.59
      pick: 0.49
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
      total: 0.44
      efficiency: 0.25
      win: 0.62
      pick: 0.34
      fit: 0.56
    Obsidian Shard:
      total: 0.48
      efficiency: 0.37
      win: 0.65
      pick: 0.24
      fit: 0.56
    Soul Gem:
      total: 0.51
      efficiency: 0.41
      win: 0.57
      pick: 0.27
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Book of Thoth
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
    this god: Amanita Charm, Rod of Asclepius, Blood-Bound Book, Bancroft''s Talon,
    Shield of the Phoenix, Gluttonous Grimoire, Lifebinder, The Cosmic Horror, Kinetic
    Cuirass, Chandra''s Grace, Eye of Providence, Spear of the Magus, Spirit Robe,
    Phoenix Feather, Helm of Radiance, Genji''s Guard, Doom Orb, Glorious Pridwen,
    Chronos'' Pendant, Ethereal Staff, Spectral Armor, Sphere of Negation, Ancient
    Signet, Breastplate of Valor, Death Metal.'
  slot_scores:
    Book of Thoth:
      total: 0.4
      efficiency: 0.4
      win: 0.57
      pick: 0.22
      fit: 0.2
    Spear of Desolation:
      total: 0.5
      efficiency: 0.43
      win: 0.59
      pick: 0.49
      fit: 0.5
    Rod of Tahuti:
      total: 0.41
      efficiency: 0.25
      win: 0.62
      pick: 0.34
      fit: 0.36
    Obsidian Shard:
      total: 0.45
      efficiency: 0.37
      win: 0.65
      pick: 0.24
      fit: 0.36
    Amanita Charm:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.52
      efficiency: 0.41
      win: 0.57
      pick: 0.27
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
  - The Cosmic Horror
  - Spear of the Magus
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
    Orb, The World Stone, Chronos'' Pendant, Screeching Gargoyle, Rod of Asclepius,
    Blood-Bound Book, Ethereal Staff, Ancient Signet, Death Metal, Bancroft''s Talon,
    Gem of Focus, Divine Ruin, Polynomicon, Helm of Radiance, Genji''s Guard, Lifebinder,
    Bragi''s Harp, Alchemist Coat, Jade Scepter.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.43
      win: 0.59
      pick: 0.49
      fit: 1.0
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.81
    Spear of the Magus:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.81
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.25
      win: 0.62
      pick: 0.34
      fit: 0.81
    Obsidian Shard:
      total: 0.51
      efficiency: 0.37
      win: 0.65
      pick: 0.24
      fit: 0.81
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.57
      pick: 0.27
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
  - Rod of Tahuti
  - Obsidian Shard
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Erosion
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
    Grace, Spectral Armor, Shield of the Phoenix, Erosion, Void Stone, The Cosmic
    Horror, Kinetic Cuirass, Triton''s Conch, Genji''s Guard, Eye of Providence, Phoenix
    Feather, Blood-Bound Book, Ethereal Staff, Spear of the Magus, Doublet of Binding,
    Bancroft''s Talon, Doom Orb, Chronos'' Pendant, Screeching Gargoyle, Stampede,
    Void Shield.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.43
      win: 0.59
      pick: 0.49
      fit: 0.65
    Rod of Tahuti:
      total: 0.41
      efficiency: 0.25
      win: 0.62
      pick: 0.34
      fit: 0.39
    Obsidian Shard:
      total: 0.45
      efficiency: 0.37
      win: 0.65
      pick: 0.24
      fit: 0.39
    Spectral Armor:
      total: 0.42
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.49
    Erosion:
      total: 0.41
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.57
      pick: 0.27
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Spectral Armor
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Spectral Armor
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
    god: Rod of Asclepius, Lifebinder, Amanita Charm, Gluttonous Grimoire, Triton''s
    Conch, Spectral Armor, The Cosmic Horror, Blood-Bound Book, Spear of the Magus,
    Chandra''s Grace, Shield of the Phoenix, Erosion, Bancroft''s Talon, Doom Orb,
    Death Metal, Ethereal Staff, Void Stone, Kinetic Cuirass, The World Stone, Chronos''
    Pendant, Genji''s Guard, Bragi''s Harp, Eye of Providence, Phoenix Feather.'
  slot_scores:
    Spear of Desolation:
      total: 0.52
      efficiency: 0.43
      win: 0.59
      pick: 0.49
      fit: 0.62
    Rod of Tahuti:
      total: 0.42
      efficiency: 0.25
      win: 0.62
      pick: 0.34
      fit: 0.45
    Obsidian Shard:
      total: 0.46
      efficiency: 0.37
      win: 0.65
      pick: 0.24
      fit: 0.45
    Spectral Armor:
      total: 0.41
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.57
      pick: 0.27
      fit: 1.0
    Triton's Conch:
      total: 0.42
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - Obsidian Shard
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Rod of Asclepius, Lifebinder, Spectral Armor, Shield
    of the Phoenix, Erosion, Chandra''s Grace, Kinetic Cuirass, Eye of Providence,
    Blood-Bound Book, Phoenix Feather, Gluttonous Grimoire, Bancroft''s Talon, Void
    Stone, Stampede, Spirit Robe, Void Shield, Genji''s Guard, Umbral Link, Triton''s
    Conch, Glorious Pridwen, The Cosmic Horror, Mystical Mail, Doublet of Binding,
    Ethereal Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.49
      efficiency: 0.43
      win: 0.59
      pick: 0.49
      fit: 0.38
    Obsidian Shard:
      total: 0.43
      efficiency: 0.37
      win: 0.65
      pick: 0.24
      fit: 0.23
    Spectral Armor:
      total: 0.43
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.42
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.57
      pick: 0.27
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Stone
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Void Stone
  - The Cosmic Horror
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
    for this god: Rod of Asclepius, Gluttonous Grimoire, Amanita Charm, Void Stone,
    Lifebinder, The Cosmic Horror, Spear of the Magus, Spectral Armor, Void Shield,
    Doom Orb, Screeching Gargoyle, Chandra''s Grace, Erosion, Shield of the Phoenix,
    The World Stone, Blood-Bound Book, Kinetic Cuirass, Triton''s Conch, Eye of Providence,
    Phoenix Feather, Genji''s Guard, Ethereal Staff, Bancroft''s Talon, Doublet of
    Binding.'
  slot_scores:
    Void Stone:
      total: 0.43
      efficiency: 0.31
      win: 0.5
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.54
      efficiency: 0.43
      win: 0.59
      pick: 0.49
      fit: 0.74
    The Cosmic Horror:
      total: 0.42
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.44
      efficiency: 0.25
      win: 0.62
      pick: 0.34
      fit: 0.56
    Obsidian Shard:
      total: 0.48
      efficiency: 0.37
      win: 0.65
      pick: 0.24
      fit: 0.56
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.57
      pick: 0.27
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
---
