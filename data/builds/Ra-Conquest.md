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
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - The Cosmic Horror
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Chronos''
    Pendant, Ethereal Staff, Blink Rune, Genji''s Guard, Gem of Focus, Dreamer''s
    Idol, Death Metal, Wish-Granting Pearl, Jade Scepter, Bancroft''s Talon, Rod of
    Asclepius, Blood-Bound Book, The World Stone, Doom Orb, Breastplate of Valor,
    Bracer of The Abyss, Helm of Radiance, Alchemist Coat, Polynomicon, Bragi''s Harp,
    Shield of the Phoenix.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.52
      win: 0.6
      pick: 0.58
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.72
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.47
      win: 0.61
      pick: 0.33
      fit: 0.72
    Obsidian Shard:
      total: 0.59
      efficiency: 0.55
      win: 0.63
      pick: 0.23
      fit: 0.72
    Soul Gem:
      total: 0.67
      efficiency: 0.62
      win: 0.64
      pick: 0.22
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Blink Rune
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Blink Rune
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
    god: Gluttonous Grimoire, Blink Rune, Spear of the Magus, Death Metal, Genji''s
    Guard, The Cosmic Horror, Ethereal Staff, Chronos'' Pendant, Breastplate of Valor,
    Dreamer''s Idol, Bragi''s Harp, Triton''s Conch, Wish-Granting Pearl, The World
    Stone, Gem of Focus, Jade Scepter, Doom Orb, Bancroft''s Talon, Rod of Asclepius,
    Blood-Bound Book, Bracer of The Abyss, Shield of the Phoenix, Oni Hunter''s Garb,
    Chandra''s Grace.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.6
      pick: 0.58
      fit: 0.78
    Spear of the Magus:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.47
      win: 0.61
      pick: 0.33
      fit: 0.56
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.63
      pick: 0.23
      fit: 0.56
    Soul Gem:
      total: 0.65
      efficiency: 0.62
      win: 0.64
      pick: 0.22
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Ethereal Staff
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Chandra''s Grace, Ethereal Staff, Blink Rune, Eye of Providence,
    Genji''s Guard, Oni Hunter''s Garb, Bancroft''s Talon, Blood-Bound Book, Lifebinder,
    Spectral Armor, Wish-Granting Pearl, Jade Scepter, Breastplate of Valor, Shifter''s
    Shield, Phoenix Feather, Freya''s Tears, Yogi''s Necklace, Erosion, Spear of the
    Magus, Draconic Scale, Mantle Of Discord, Alchemist Coat.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.6
    Ethereal Staff:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.6
      pick: 0.58
      fit: 0.5
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.63
      pick: 0.23
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.65
      efficiency: 0.62
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
  - The Cosmic Horror
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Dreamer''s
    Idol, Blink Rune, The World Stone, Doom Orb, Ethereal Staff, Genji''s Guard, Chronos''
    Pendant, Death Metal, Wish-Granting Pearl, Breastplate of Valor, Jade Scepter,
    Screeching Gargoyle, Bancroft''s Talon, Rod of Asclepius, Blood-Bound Book, Gem
    of Focus, Bracer of The Abyss, Helm of Radiance, Oni Hunter''s Garb, Alchemist
    Coat, Shield of the Phoenix.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.52
      win: 0.6
      pick: 0.58
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.81
    Spear of the Magus:
      total: 0.56
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.81
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.47
      win: 0.61
      pick: 0.33
      fit: 0.81
    Obsidian Shard:
      total: 0.61
      efficiency: 0.55
      win: 0.63
      pick: 0.23
      fit: 0.81
    Soul Gem:
      total: 0.67
      efficiency: 0.62
      win: 0.64
      pick: 0.22
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.3
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.33
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.31
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Death Metal:
      total: 0.32
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.33
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.31
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  flex_slots:
  - Chronos' Pendant
  - Ethereal Staff
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Chronos'' Pendant, Ethereal Staff, Blink Rune, Genji''s Guard, Gem of Focus, Dreamer''s
    Idol, Death Metal, Wish-Granting Pearl, Jade Scepter, Bancroft''s Talon, Rod of
    Asclepius, Blood-Bound Book, The World Stone, Doom Orb, Breastplate of Valor,
    Bracer of The Abyss, Helm of Radiance, Alchemist Coat, Polynomicon, Bragi''s Harp,
    Shield of the Phoenix.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.69
    Ethereal Staff:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.82
    Spear of Desolation:
      total: 0.63
      efficiency: 0.52
      win: 0.6
      pick: 0.58
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Blink Rune
  - Genji's Guard
  - Spear of Desolation
  - Obsidian Shard
  - Spectral Armor
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Blink Rune
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Genji''s Guard,
    Shield of the Phoenix, Lifebinder, Chandra''s Grace, Spectral Armor, Blink Rune,
    Oni Hunter''s Garb, Doublet of Binding, Erosion, Ethereal Staff, Kinetic Cuirass,
    Triton''s Conch, Eye of Providence, Void Stone, Spear of the Magus, Breastplate
    of Valor, Wish-Granting Pearl, Yogi''s Necklace, Freya''s Tears, Jade Scepter,
    Bancroft''s Talon, Blood-Bound Book, Chronos'' Pendant.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Genji's Guard:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.6
      pick: 0.58
      fit: 0.65
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.63
      pick: 0.23
      fit: 0.39
    Spectral Armor:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Soul Gem:
      total: 0.67
      efficiency: 0.62
      win: 0.64
      pick: 0.22
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: burst
  slot_order:
  - Blink Rune
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Blink Rune
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Triton''s Conch, Lifebinder,
    Blink Rune, Genji''s Guard, Spectral Armor, Ethereal Staff, Shield of the Phoenix,
    Chandra''s Grace, Spear of the Magus, Death Metal, Bancroft''s Talon, Blood-Bound
    Book, Oni Hunter''s Garb, Doublet of Binding, The Cosmic Horror, Erosion, Kinetic
    Cuirass, Wish-Granting Pearl, Jade Scepter, Breastplate of Valor, Chronos'' Pendant,
    Yogi''s Necklace.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.6
      pick: 0.58
      fit: 0.62
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.47
      win: 0.61
      pick: 0.33
      fit: 0.45
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.63
      pick: 0.23
      fit: 0.45
    Soul Gem:
      total: 0.67
      efficiency: 0.62
      win: 0.64
      pick: 0.22
      fit: 1.0
    Triton's Conch:
      total: 0.53
      efficiency: 0.56
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
  - Kinetic Cuirass
  - Spear of Desolation
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Spectral Armor, Erosion, Kinetic Cuirass, Lifebinder, Chandra''s Grace, Eye of
    Providence, Genji''s Guard, Oni Hunter''s Garb, Blink Rune, Doublet of Binding,
    Umbral Link, Stampede, Ethereal Staff, Void Shield, Breastplate of Valor, Shifter''s
    Shield, Freya''s Tears, Triton''s Conch, Phoenix Feather, Void Stone, Mystical
    Mail, Bancroft''s Talon, Blood-Bound Book.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.58
      fit: 0.43
    Spectral Armor:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.69
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.87
    Soul Gem:
      total: 0.67
      efficiency: 0.62
      win: 0.64
      pick: 0.22
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: anti-tank
  slot_order:
  - Blink Rune
  - Void Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Void Stone
  - Blink Rune
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Void Stone,
    Blink Rune, Genji''s Guard, Spear of the Magus, Spectral Armor, Lifebinder, Void
    Shield, Shield of the Phoenix, Chandra''s Grace, The Cosmic Horror, Oni Hunter''s
    Garb, Doublet of Binding, Ethereal Staff, Erosion, Screeching Gargoyle, Kinetic
    Cuirass, Triton''s Conch, Dreamer''s Idol, Eye of Providence, Yogi''s Necklace,
    Bancroft''s Talon, Blood-Bound Book.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Void Stone:
      total: 0.53
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.6
      pick: 0.58
      fit: 0.74
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.47
      win: 0.61
      pick: 0.33
      fit: 0.56
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.63
      pick: 0.23
      fit: 0.56
    Soul Gem:
      total: 0.67
      efficiency: 0.62
      win: 0.64
      pick: 0.22
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: model
  slot_order:
  - Blink Rune
  - Genji's Guard
  - Oni Hunter's Garb
  - Spectral Armor
  - Soul Gem
  - Doublet of Binding
  flex_slots:
  - Oni Hunter's Garb
  - Doublet of Binding
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius,
    Genji''s Guard, Shield of the Phoenix, Lifebinder, Chandra''s Grace, Spectral
    Armor, Blink Rune, Oni Hunter''s Garb, Doublet of Binding, Erosion, Ethereal Staff,
    Kinetic Cuirass, Triton''s Conch, Eye of Providence, Void Stone, Spear of the
    Magus, Breastplate of Valor, Wish-Granting Pearl, Yogi''s Necklace, Freya''s Tears,
    Jade Scepter, Bancroft''s Talon, Blood-Bound Book, Chronos'' Pendant.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Genji's Guard:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.42
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.35
    Spectral Armor:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Soul Gem:
      total: 0.67
      efficiency: 0.62
      win: 0.64
      pick: 0.22
      fit: 1.0
    Doublet of Binding:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
  aspect: Aspect of Thermotherapy
---
