---
type: smite-build
god: Nut
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cosmos
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.48
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.34
    win_rate: 0.44
    alternates:
    - name: Tyrfing
      pick_rate: 0.32
      win_rate: 0.48
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.55
  - name: Bragi's Harp
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Staff of Myrddin
      pick_rate: 0.12
      win_rate: 0.38
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.63
  - name: Rod of Tahuti
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.62
    - name: Barbed Carver
      pick_rate: 0.07
      win_rate: 0.35
  - name: Obsidian Shard
    pick_rate: 0.15
    win_rate: 0.45
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.53
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.63
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.44
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.54
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.56
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Evil Eye
      pick_rate: 0.09
      win_rate: 0.2
    - name: Hunter's Bow
      pick_rate: 0.06
      win_rate: 0.29
  source_url: https://smitebrain.com/gods/nut/
  last_verified: '2026-08-01'
  god_win_rate: 0.4910394265232975
  god_matches_won: 137
  god_matches_played: 279
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
  - Bracer of The Abyss
  - Bragi's Harp
  - Ethereal Staff
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spear of the Magus
  flex_slots:
  - Bracer of The Abyss
  - Ethereal Staff
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
    this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, Blood-Bound Book,
    The Cosmic Horror, Bancroft''s Talon, Bracer of The Abyss, Ethereal Staff, Rod
    of Asclepius, Obsidian Shard, Chronos'' Pendant, Nimble Ring, Ancient Signet,
    Death Metal, Genji''s Guard, Polynomicon, Doom Orb, Helm of Radiance, Alchemist
    Coat, Gem of Focus, Spectral Armor, Chandra''s Grace, Divine Ruin, Book of Thoth,
    Lifebinder.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.54
    Bragi's Harp:
      total: 0.45
      efficiency: 0.34
      win: 0.5
      pick: 0.16
      fit: 0.64
    Ethereal Staff:
      total: 0.42
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.23
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.67
    The Cosmic Horror:
      total: 0.43
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spear of the Magus:
      total: 0.46
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Bragi's Harp
  - Death Metal
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spear of the Magus
  flex_slots:
  - Death Metal
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror, Death
    Metal, Blood-Bound Book, Bancroft''s Talon, Chronos'' Pendant, Obsidian Shard,
    Ethereal Staff, Rod of Asclepius, Genji''s Guard, Ancient Signet, Bracer of The
    Abyss, Chandra''s Grace, Spectral Armor, Breastplate of Valor, Kinetic Cuirass,
    Doom Orb, Triton''s Conch, Gem of Focus, Eye of Providence, Shield of the Phoenix,
    Polynomicon, Helm of Radiance.'
  slot_scores:
    Chronos' Pendant:
      total: 0.41
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.45
      efficiency: 0.34
      win: 0.5
      pick: 0.16
      fit: 0.62
    Death Metal:
      total: 0.42
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.32
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Cosmic Horror:
      total: 0.43
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.4
    Spear of the Magus:
      total: 0.45
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of the Magus
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Spectral Armor
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
    this god: Gluttonous Grimoire, Amanita Charm, Soul Gem, Rod of Asclepius, Blood-Bound
    Book, Shield of the Phoenix, Bancroft''s Talon, Chandra''s Grace, Kinetic Cuirass,
    Lifebinder, Eye of Providence, Phoenix Feather, Spectral Armor, Spear of the Magus,
    Ethereal Staff, Erosion, Spirit Robe, Genji''s Guard, The Cosmic Horror, Alchemist
    Coat, Helm of Radiance, Yogi''s Necklace, Breastplate of Valor, Midgardian Mail,
    Jade Scepter, Obsidian Shard.'
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
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spear of the Magus:
      total: 0.43
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.28
    Spectral Armor:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.26
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Bragi's Harp
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror,
    Obsidian Shard, Blood-Bound Book, Bancroft''s Talon, Screeching Gargoyle, Doom
    Orb, Ethereal Staff, Rod of Asclepius, Bracer of The Abyss, Chronos'' Pendant,
    Rod of Tahuti, Ancient Signet, The World Stone, Death Metal, Genji''s Guard, Nimble
    Ring, Spectral Armor, Kinetic Cuirass, Polynomicon, Chandra''s Grace, Helm of
    Radiance, Alchemist Coat.'
  slot_scores:
    Bragi's Harp:
      total: 0.43
      efficiency: 0.34
      win: 0.5
      pick: 0.16
      fit: 0.53
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.76
    Spear of Desolation:
      total: 0.43
      efficiency: 0.32
      win: 0.44
      pick: 0.34
      fit: 0.66
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.44
      efficiency: 0.41
      win: 0.45
      pick: 0.15
      fit: 0.56
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
  - Bracer of The Abyss
  - Bragi's Harp
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - The Cosmic Horror
  - Bracer of The Abyss
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
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, Blood-Bound
    Book, Obsidian Shard, The Cosmic Horror, Bancroft''s Talon, Bracer of The Abyss,
    Ethereal Staff, Rod of Asclepius, Chronos'' Pendant, Nimble Ring, Ancient Signet,
    Death Metal, Genji''s Guard, Polynomicon, Doom Orb, Helm of Radiance, Alchemist
    Coat, Gem of Focus, Spectral Armor, Chandra''s Grace, Divine Ruin, Book of Thoth,
    Lifebinder.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.54
    Bragi's Harp:
      total: 0.45
      efficiency: 0.34
      win: 0.5
      pick: 0.16
      fit: 0.64
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.67
    The Cosmic Horror:
      total: 0.43
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spear of the Magus:
      total: 0.46
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.45
    Obsidian Shard:
      total: 0.42
      efficiency: 0.41
      win: 0.45
      pick: 0.15
      fit: 0.45
  starter: *id001
---
