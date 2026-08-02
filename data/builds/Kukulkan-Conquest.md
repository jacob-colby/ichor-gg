---
type: smite-build
god: Kukulkan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Squall
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.67
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.92
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.04
      win_rate: 0.64
    - name: Doom Orb
      pick_rate: 0.01
      win_rate: 0.0
  - name: Spear of Desolation
    pick_rate: 0.44
    win_rate: 0.6
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.11
      win_rate: 0.39
    - name: Polynomicon
      pick_rate: 0.06
      win_rate: 0.86
  - name: Polynomicon
    pick_rate: 0.24
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.2
      win_rate: 0.62
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.58
  - name: Rod of Tahuti
    pick_rate: 0.36
    win_rate: 0.62
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.61
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.23
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.7
    - name: Evil Eye
      pick_rate: 0.09
      win_rate: 0.5
  - name: Oracle Staff
    pick_rate: 0.08
    win_rate: 0.82
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.5
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.44
  source_url: https://smitebrain.com/gods/kukulkan/
  last_verified: '2026-08-01'
  god_win_rate: 0.5685483870967742
  god_matches_won: 141
  god_matches_played: 248
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
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Rod of Tahuti
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
    this god: Gluttonous Grimoire, Spear of the Magus, Soul Gem, The Cosmic Horror,
    Chronos'' Pendant, Ethereal Staff, Doom Orb, Rod of Asclepius, Blood-Bound Book,
    Bancroft''s Talon, Ancient Signet, The World Stone, Death Metal, Gem of Focus,
    Helm of Radiance, Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s Harp, Jade
    Scepter, Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.39
      win: 0.57
      pick: 0.92
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.55
      efficiency: 0.32
      win: 0.6
      pick: 0.44
      fit: 1.0
    Spear of the Magus:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.26
      win: 0.62
      pick: 0.36
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.41
      win: 0.67
      pick: 0.23
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Book of Thoth
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
    god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror, Death
    Metal, Chronos'' Pendant, Bragi''s Harp, Ethereal Staff, Rod of Asclepius, Blood-Bound
    Book, Genji''s Guard, Doom Orb, Bancroft''s Talon, Ancient Signet, Triton''s Conch,
    Gem of Focus, Chandra''s Grace, Breastplate of Valor, The World Stone, Shield
    of the Phoenix, Helm of Radiance, Spectral Armor, Alchemist Coat.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.39
      win: 0.57
      pick: 0.92
      fit: 0.22
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.52
      efficiency: 0.32
      win: 0.6
      pick: 0.44
      fit: 0.78
    Spear of the Magus:
      total: 0.47
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.26
      win: 0.62
      pick: 0.36
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.41
      win: 0.67
      pick: 0.23
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Book of Thoth
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
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Soul Gem, Shield
    of the Phoenix, Kinetic Cuirass, Chandra''s Grace, Eye of Providence, Lifebinder,
    Blood-Bound Book, Bancroft''s Talon, Phoenix Feather, Spear of the Magus, Spectral
    Armor, Ethereal Staff, Erosion, Spirit Robe, The Cosmic Horror, Genji''s Guard,
    Alchemist Coat, Helm of Radiance, Jade Scepter, Midgardian Mail, Gladiator''s
    Shield, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.39
      win: 0.57
      pick: 0.92
      fit: 0.21
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
    Spear of Desolation:
      total: 0.48
      efficiency: 0.32
      win: 0.6
      pick: 0.44
      fit: 0.49
    Obsidian Shard:
      total: 0.52
      efficiency: 0.41
      win: 0.67
      pick: 0.23
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
  - Rod of Tahuti
  - The Cosmic Horror
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
    for this god: Gluttonous Grimoire, Spear of the Magus, Soul Gem, The Cosmic Horror,
    Doom Orb, The World Stone, Ethereal Staff, Chronos'' Pendant, Rod of Asclepius,
    Blood-Bound Book, Screeching Gargoyle, Bancroft''s Talon, Ancient Signet, Death
    Metal, Dreamer''s Idol, Gem of Focus, Helm of Radiance, Genji''s Guard, Alchemist
    Coat, Divine Ruin, Lifebinder, Bragi''s Harp.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.55
      efficiency: 0.32
      win: 0.6
      pick: 0.44
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
      total: 0.52
      efficiency: 0.26
      win: 0.62
      pick: 0.36
      fit: 0.85
    Obsidian Shard:
      total: 0.58
      efficiency: 0.41
      win: 0.67
      pick: 0.23
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, Soul Gem, The
    Cosmic Horror, Chronos'' Pendant, Ethereal Staff, Doom Orb, Rod of Asclepius,
    Blood-Bound Book, Bancroft''s Talon, Ancient Signet, The World Stone, Death Metal,
    Gem of Focus, Helm of Radiance, Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s
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
      total: 0.55
      efficiency: 0.32
      win: 0.6
      pick: 0.44
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
      total: 0.58
      efficiency: 0.41
      win: 0.67
      pick: 0.23
      fit: 0.79
  starter: *id001
---
