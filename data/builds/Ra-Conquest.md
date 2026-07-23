---
type: smite-build
god: Ra
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thermotherapy
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.6
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.49
    win_rate: 0.59
    alternates:
    - name: Book of Thoth
      pick_rate: 0.33
      win_rate: 0.57
    - name: Doom Orb
      pick_rate: 0.04
      win_rate: 0.6
  - name: Book of Thoth
    pick_rate: 0.22
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.29
      win_rate: 0.58
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.6
  - name: Soul Gem
    pick_rate: 0.27
    win_rate: 0.58
    alternates:
    - name: The World Stone
      pick_rate: 0.17
      win_rate: 0.56
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.59
  - name: Rod of Tahuti
    pick_rate: 0.34
    win_rate: 0.61
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.18
      win_rate: 0.54
    - name: Soul Gem
      pick_rate: 0.06
      win_rate: 0.65
  - name: Obsidian Shard
    pick_rate: 0.24
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.17
      win_rate: 0.67
    - name: Nimble Ring
      pick_rate: 0.09
      win_rate: 0.73
  - name: Evil Eye
    pick_rate: 0.1
    win_rate: 0.48
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.7
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.57
  source_url: https://smitebrain.com/gods/ra/
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
  - Rod of Tahuti
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
    Chronos'' Pendant, The World Stone, Rod of Asclepius, Ethereal Staff, Blood-Bound
    Book, Gem of Focus, Ancient Signet, Death Metal, Bancroft''s Talon, Genji''s Guard,
    Polynomicon, Helm of Radiance, Divine Ruin, Alchemist Coat, Lifebinder, Bragi''s
    Harp, Jade Scepter, Chandra''s Grace, Breastplate of Valor.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.42
      win: 0.59
      pick: 0.49
      fit: 1.0
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.48
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.72
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.24
      win: 0.61
      pick: 0.34
      fit: 0.72
    Obsidian Shard:
      total: 0.53
      efficiency: 0.36
      win: 0.64
      pick: 0.24
      fit: 0.72
    Soul Gem:
      total: 0.57
      efficiency: 0.41
      win: 0.58
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
  - Rod of Tahuti
  - Spear of the Magus
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
    Metal, The World Stone, Chronos'' Pendant, Bragi''s Harp, Rod of Asclepius, Ethereal
    Staff, Blood-Bound Book, Genji''s Guard, Triton''s Conch, Ancient Signet, Bancroft''s
    Talon, Gem of Focus, Chandra''s Grace, Breastplate of Valor, Polynomicon, Helm
    of Radiance, Divine Ruin, Alchemist Coat, Shield of the Phoenix, Spectral Armor.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.42
      win: 0.59
      pick: 0.49
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
      win: 0.61
      pick: 0.34
      fit: 0.56
    Obsidian Shard:
      total: 0.51
      efficiency: 0.36
      win: 0.64
      pick: 0.24
      fit: 0.56
    Soul Gem:
      total: 0.55
      efficiency: 0.41
      win: 0.58
      pick: 0.27
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
    this god: Amanita Charm, Rod of Asclepius, Blood-Bound Book, Shield of the Phoenix,
    Bancroft''s Talon, Gluttonous Grimoire, Chandra''s Grace, The Cosmic Horror, Kinetic
    Cuirass, Lifebinder, Eye of Providence, Genji''s Guard, Spirit Robe, Spear of
    the Magus, Phoenix Feather, Helm of Radiance, Spectral Armor, Doom Orb, Ethereal
    Staff, Chronos'' Pendant, Breastplate of Valor, Glorious Pridwen, Ancient Signet,
    Death Metal, Sphere of Negation.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.51
      efficiency: 0.42
      win: 0.59
      pick: 0.49
      fit: 0.5
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.36
    Obsidian Shard:
      total: 0.48
      efficiency: 0.36
      win: 0.64
      pick: 0.24
      fit: 0.36
    Amanita Charm:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.55
      efficiency: 0.41
      win: 0.58
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
  - Rod of Tahuti
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
    Ethereal Staff, Blood-Bound Book, Ancient Signet, Death Metal, Bancroft''s Talon,
    Gem of Focus, Genji''s Guard, Polynomicon, Helm of Radiance, Divine Ruin, Alchemist
    Coat, Lifebinder, Chandra''s Grace, Bragi''s Harp.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.42
      win: 0.59
      pick: 0.49
      fit: 1.0
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.81
    Spear of the Magus:
      total: 0.49
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.81
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.24
      win: 0.61
      pick: 0.34
      fit: 0.81
    Obsidian Shard:
      total: 0.55
      efficiency: 0.36
      win: 0.64
      pick: 0.24
      fit: 0.81
    Soul Gem:
      total: 0.57
      efficiency: 0.41
      win: 0.58
      pick: 0.27
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
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Obsidian Shard
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Genji's Guard
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
    Grace, Spectral Armor, Shield of the Phoenix, Erosion, Genji''s Guard, Kinetic
    Cuirass, The Cosmic Horror, Void Stone, Eye of Providence, Triton''s Conch, Phoenix
    Feather, Blood-Bound Book, Ethereal Staff, Doublet of Binding, Spear of the Magus,
    Bancroft''s Talon, Doom Orb, Chronos'' Pendant, Screeching Gargoyle, Stampede,
    Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.53
      efficiency: 0.42
      win: 0.59
      pick: 0.49
      fit: 0.65
    Obsidian Shard:
      total: 0.49
      efficiency: 0.36
      win: 0.64
      pick: 0.24
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
      total: 0.57
      efficiency: 0.41
      win: 0.58
      pick: 0.27
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
    god: Rod of Asclepius, Amanita Charm, Lifebinder, Gluttonous Grimoire, Triton''s
    Conch, Spectral Armor, The Cosmic Horror, Chandra''s Grace, Blood-Bound Book,
    Spear of the Magus, Shield of the Phoenix, Bancroft''s Talon, Erosion, Doom Orb,
    Death Metal, Ethereal Staff, Genji''s Guard, Kinetic Cuirass, The World Stone,
    Void Stone, Chronos'' Pendant, Eye of Providence, Phoenix Feather, Bragi''s Harp.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.42
      win: 0.59
      pick: 0.49
      fit: 0.62
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.45
    Obsidian Shard:
      total: 0.49
      efficiency: 0.36
      win: 0.64
      pick: 0.24
      fit: 0.45
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.57
      efficiency: 0.41
      win: 0.58
      pick: 0.27
      fit: 1.0
    Triton's Conch:
      total: 0.46
      efficiency: 0.35
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
  - Erosion
  - Obsidian Shard
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
    this god: Amanita Charm, Rod of Asclepius, Spectral Armor, Lifebinder, Shield
    of the Phoenix, Erosion, Chandra''s Grace, Kinetic Cuirass, Eye of Providence,
    Blood-Bound Book, Gluttonous Grimoire, Phoenix Feather, Bancroft''s Talon, Genji''s
    Guard, Void Stone, Stampede, Spirit Robe, Void Shield, Umbral Link, The Cosmic
    Horror, Triton''s Conch, Doublet of Binding, Breastplate of Valor, Glorious Pridwen,
    Ethereal Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.49
      efficiency: 0.42
      win: 0.59
      pick: 0.49
      fit: 0.38
    Obsidian Shard:
      total: 0.46
      efficiency: 0.36
      win: 0.64
      pick: 0.24
      fit: 0.23
    Spectral Armor:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.53
      efficiency: 0.45
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
      total: 0.57
      efficiency: 0.41
      win: 0.58
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
  - Obsidian Shard
  - Spectral Armor
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
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
    for this god: Rod of Asclepius, Gluttonous Grimoire, Amanita Charm, Void Stone,
    Lifebinder, The Cosmic Horror, Spectral Armor, Spear of the Magus, Chandra''s
    Grace, Void Shield, Doom Orb, Screeching Gargoyle, Erosion, Shield of the Phoenix,
    The World Stone, Blood-Bound Book, Kinetic Cuirass, Genji''s Guard, Eye of Providence,
    Triton''s Conch, Phoenix Feather, Ethereal Staff, Bancroft''s Talon, Doublet of
    Binding.'
  slot_scores:
    Void Stone:
      total: 0.47
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.55
      efficiency: 0.42
      win: 0.59
      pick: 0.49
      fit: 0.74
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.51
      efficiency: 0.36
      win: 0.64
      pick: 0.24
      fit: 0.56
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.57
      efficiency: 0.41
      win: 0.58
      pick: 0.27
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
---
