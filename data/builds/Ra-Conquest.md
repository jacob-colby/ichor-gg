---
type: smite-build
god: Ra
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thermotherapy
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.59
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.51
    win_rate: 0.6
    alternates:
    - name: Book of Thoth
      pick_rate: 0.31
      win_rate: 0.56
    - name: Doom Orb
      pick_rate: 0.04
      win_rate: 0.56
  - name: Book of Thoth
    pick_rate: 0.24
    win_rate: 0.6
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.27
      win_rate: 0.57
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.61
  - name: Soul Gem
    pick_rate: 0.27
    win_rate: 0.58
    alternates:
    - name: The World Stone
      pick_rate: 0.16
      win_rate: 0.56
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.58
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.62
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.52
    - name: Nimble Ring
      pick_rate: 0.06
      win_rate: 0.65
  - name: Obsidian Shard
    pick_rate: 0.23
    win_rate: 0.65
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.66
    - name: Nimble Ring
      pick_rate: 0.1
      win_rate: 0.68
  - name: Evil Eye
    pick_rate: 0.1
    win_rate: 0.51
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.66
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.6
  source_url: https://smitebrain.com/gods/ra/
  last_verified: '2026-07-25'
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
    Chronos'' Pendant, The World Stone, Ethereal Staff, Rod of Asclepius, Blood-Bound
    Book, Gem of Focus, Death Metal, Bancroft''s Talon, Ancient Signet, Genji''s Guard,
    Polynomicon, Helm of Radiance, Alchemist Coat, Divine Ruin, Lifebinder, Jade Scepter,
    Bragi''s Harp, Chandra''s Grace, Breastplate of Valor.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.41
      win: 0.6
      pick: 0.51
      fit: 1.0
    The Cosmic Horror:
      total: 0.49
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
      efficiency: 0.22
      win: 0.62
      pick: 0.33
      fit: 0.72
    Obsidian Shard:
      total: 0.54
      efficiency: 0.36
      win: 0.65
      pick: 0.23
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
    Metal, The World Stone, Chronos'' Pendant, Bragi''s Harp, Ethereal Staff, Rod
    of Asclepius, Blood-Bound Book, Genji''s Guard, Triton''s Conch, Bancroft''s Talon,
    Ancient Signet, Chandra''s Grace, Gem of Focus, Breastplate of Valor, Polynomicon,
    Spectral Armor, Shield of the Phoenix, Helm of Radiance, Alchemist Coat, Divine
    Ruin.'
  slot_scores:
    Spear of Desolation:
      total: 0.56
      efficiency: 0.41
      win: 0.6
      pick: 0.51
      fit: 0.78
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.45
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.46
      efficiency: 0.22
      win: 0.62
      pick: 0.33
      fit: 0.56
    Obsidian Shard:
      total: 0.51
      efficiency: 0.36
      win: 0.65
      pick: 0.23
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
  - Book of Thoth
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Book of Thoth
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
    Bancroft''s Talon, Gluttonous Grimoire, Chandra''s Grace, Kinetic Cuirass, The
    Cosmic Horror, Lifebinder, Eye of Providence, Genji''s Guard, Spirit Robe, Spear
    of the Magus, Phoenix Feather, Spectral Armor, Ethereal Staff, Helm of Radiance,
    Doom Orb, Breastplate of Valor, Chronos'' Pendant, Glorious Pridwen, Death Metal,
    Erosion, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.38
      win: 0.6
      pick: 0.24
      fit: 0.2
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.51
      efficiency: 0.41
      win: 0.6
      pick: 0.51
      fit: 0.5
    Obsidian Shard:
      total: 0.48
      efficiency: 0.36
      win: 0.65
      pick: 0.23
      fit: 0.36
    Amanita Charm:
      total: 0.47
      efficiency: 0.44
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
    Orb, The World Stone, Chronos'' Pendant, Ethereal Staff, Screeching Gargoyle,
    Rod of Asclepius, Blood-Bound Book, Death Metal, Bancroft''s Talon, Ancient Signet,
    Genji''s Guard, Gem of Focus, Polynomicon, Helm of Radiance, Chandra''s Grace,
    Alchemist Coat, Divine Ruin, Lifebinder, Jade Scepter, Bragi''s Harp.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.41
      win: 0.6
      pick: 0.51
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
      efficiency: 0.22
      win: 0.62
      pick: 0.33
      fit: 0.81
    Obsidian Shard:
      total: 0.55
      efficiency: 0.36
      win: 0.65
      pick: 0.23
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
      total: 0.22
      efficiency: 0.54
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
    Cuirass, The Cosmic Horror, Eye of Providence, Void Stone, Triton''s Conch, Phoenix
    Feather, Ethereal Staff, Blood-Bound Book, Doublet of Binding, Spear of the Magus,
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
      total: 0.54
      efficiency: 0.41
      win: 0.6
      pick: 0.51
      fit: 0.65
    Obsidian Shard:
      total: 0.49
      efficiency: 0.36
      win: 0.65
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
    Spear of the Magus, Shield of the Phoenix, Erosion, Bancroft''s Talon, Ethereal
    Staff, Death Metal, Doom Orb, Genji''s Guard, Kinetic Cuirass, Eye of Providence,
    The World Stone, Void Stone, Chronos'' Pendant, Phoenix Feather, Bragi''s Harp.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.41
      win: 0.6
      pick: 0.51
      fit: 0.62
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.45
    Obsidian Shard:
      total: 0.5
      efficiency: 0.36
      win: 0.65
      pick: 0.23
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
    Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather, Bancroft''s Talon, Genji''s
    Guard, Void Stone, Stampede, Void Shield, Spirit Robe, Umbral Link, The Cosmic
    Horror, Triton''s Conch, Doublet of Binding, Ethereal Staff, Breastplate of Valor,
    Mystical Mail.'
  slot_scores:
    Spear of Desolation:
      total: 0.5
      efficiency: 0.41
      win: 0.6
      pick: 0.51
      fit: 0.38
    Obsidian Shard:
      total: 0.46
      efficiency: 0.36
      win: 0.65
      pick: 0.23
      fit: 0.23
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
    The World Stone, Kinetic Cuirass, Genji''s Guard, Blood-Bound Book, Eye of Providence,
    Triton''s Conch, Ethereal Staff, Phoenix Feather, Bancroft''s Talon, Doublet of
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
      efficiency: 0.41
      win: 0.6
      pick: 0.51
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
      win: 0.65
      pick: 0.23
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
