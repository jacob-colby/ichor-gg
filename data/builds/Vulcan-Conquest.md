---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.51
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.38
    win_rate: 0.55
    alternates:
    - name: Book of Thoth
      pick_rate: 0.33
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.5
  - name: Book of Thoth
    pick_rate: 0.2
    win_rate: 0.56
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.32
      win_rate: 0.6
    - name: Doom Orb
      pick_rate: 0.06
      win_rate: 0.55
  - name: Rod of Tahuti
    pick_rate: 0.21
    win_rate: 0.59
    alternates:
    - name: Soul Gem
      pick_rate: 0.16
      win_rate: 0.57
    - name: Gem of Focus
      pick_rate: 0.09
      win_rate: 0.6
  - name: Obsidian Shard
    pick_rate: 0.28
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.26
      win_rate: 0.65
    - name: Helm of Radiance
      pick_rate: 0.04
      win_rate: 0.48
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.62
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.59
  - name: Oracle Staff
    pick_rate: 0.06
    win_rate: 0.38
    alternates:
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.61
    - name: Killing Stone
      pick_rate: 0.06
      win_rate: 0.5
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-07-23'
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
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
    Doom Orb, The World Stone, Chronos'' Pendant, Rod of Asclepius, Ethereal Staff,
    Blood-Bound Book, Bragi''s Harp, Ancient Signet, Death Metal, Bancroft''s Talon,
    Gem of Focus, Bracer of The Abyss, Polynomicon, Helm of Radiance, Divine Ruin,
    Alchemist Coat, Lifebinder, Genji''s Guard, Jade Scepter.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.42
      win: 0.55
      pick: 0.38
      fit: 0.83
    The Cosmic Horror:
      total: 0.49
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.66
    Doom Orb:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.47
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.5
      efficiency: 0.36
      win: 0.57
      pick: 0.28
      fit: 0.66
    Soul Gem:
      total: 0.51
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.93
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom
    Orb, Death Metal, Bragi''s Harp, The World Stone, Chronos'' Pendant, Rod of Asclepius,
    Ethereal Staff, Blood-Bound Book, Genji''s Guard, Ancient Signet, Bancroft''s
    Talon, Triton''s Conch, Chandra''s Grace, Gem of Focus, Breastplate of Valor,
    Polynomicon, Spectral Armor, Helm of Radiance, Divine Ruin, Alchemist Coat, Shield
    of the Phoenix.'
  slot_scores:
    Spear of Desolation:
      total: 0.52
      efficiency: 0.42
      win: 0.55
      pick: 0.38
      fit: 0.7
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.5
    Doom Orb:
      total: 0.44
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.5
    Spear of the Magus:
      total: 0.45
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.5
    Obsidian Shard:
      total: 0.47
      efficiency: 0.36
      win: 0.57
      pick: 0.28
      fit: 0.5
    Soul Gem:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.8
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
    this god: Soul Gem, Amanita Charm, Rod of Asclepius, Blood-Bound Book, Bancroft''s
    Talon, Shield of the Phoenix, Gluttonous Grimoire, The Cosmic Horror, Kinetic
    Cuirass, Lifebinder, Chandra''s Grace, Eye of Providence, Spear of the Magus,
    Spirit Robe, Phoenix Feather, Genji''s Guard, Doom Orb, Spectral Armor, Ethereal
    Staff, Helm of Radiance, Chronos'' Pendant, Breastplate of Valor, Ancient Signet,
    Death Metal, The World Stone, Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.38
    Spear of Desolation:
      total: 0.48
      efficiency: 0.42
      win: 0.55
      pick: 0.38
      fit: 0.45
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.36
    Obsidian Shard:
      total: 0.45
      efficiency: 0.36
      win: 0.57
      pick: 0.28
      fit: 0.36
    Amanita Charm:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.58
    Soul Gem:
      total: 0.5
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.85
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
    Doom Orb, The World Stone, Rod of Asclepius, Ethereal Staff, Blood-Bound Book,
    Chronos'' Pendant, Screeching Gargoyle, Bragi''s Harp, Ancient Signet, Death Metal,
    Bancroft''s Talon, Polynomicon, Genji''s Guard, Helm of Radiance, Divine Ruin,
    Alchemist Coat, Gem of Focus, Bracer of The Abyss, Lifebinder.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.42
      win: 0.55
      pick: 0.38
      fit: 0.88
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.75
    Doom Orb:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.75
    Spear of the Magus:
      total: 0.49
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.75
    Obsidian Shard:
      total: 0.51
      efficiency: 0.36
      win: 0.57
      pick: 0.28
      fit: 0.75
    Soul Gem:
      total: 0.52
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.98
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
---
