---
type: smite-build
god: The Morrigan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mischief
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.48
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.38
    win_rate: 0.51
    alternates:
    - name: Book of Thoth
      pick_rate: 0.21
      win_rate: 0.5
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.54
  - name: The World Stone
    pick_rate: 0.3
    win_rate: 0.54
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.5
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.49
  - name: Polynomicon
    pick_rate: 0.33
    win_rate: 0.52
    alternates:
    - name: The World Stone
      pick_rate: 0.1
      win_rate: 0.52
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.51
  - name: Rod of Tahuti
    pick_rate: 0.3
    win_rate: 0.53
    alternates:
    - name: Polynomicon
      pick_rate: 0.15
      win_rate: 0.55
    - name: Gem of Focus
      pick_rate: 0.07
      win_rate: 0.44
  - name: Obsidian Shard
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.63
    - name: Polynomicon
      pick_rate: 0.12
      win_rate: 0.54
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.42
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.69
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.62
  source_url: https://smitebrain.com/gods/the-morrigan/
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
  - The World Stone
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    this god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus,
    Doom Orb, Chronos'' Pendant, Ethereal Staff, Rod of Asclepius, Blood-Bound Book,
    Death Metal, Bancroft''s Talon, Ancient Signet, Gem of Focus, Helm of Radiance,
    Alchemist Coat, Divine Ruin, Lifebinder, Jade Scepter, Bragi''s Harp, Book of
    Thoth, Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.41
      win: 0.51
      pick: 0.38
      fit: 1.0
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.8
    Spear of the Magus:
      total: 0.49
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.8
    The World Stone:
      total: 0.5
      efficiency: 0.36
      win: 0.54
      pick: 0.3
      fit: 0.8
    Obsidian Shard:
      total: 0.49
      efficiency: 0.36
      win: 0.53
      pick: 0.2
      fit: 0.8
    Soul Gem:
      total: 0.52
      efficiency: 0.41
      win: 0.5
      pick: 0.0
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
  - The World Stone
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom
    Orb, Death Metal, Chronos'' Pendant, Bragi''s Harp, Ethereal Staff, Rod of Asclepius,
    Blood-Bound Book, Genji''s Guard, Triton''s Conch, Bancroft''s Talon, Ancient
    Signet, Chandra''s Grace, Gem of Focus, Breastplate of Valor, Spectral Armor,
    Shield of the Phoenix, Helm of Radiance, Alchemist Coat, Divine Ruin.'
  slot_scores:
    Spear of Desolation:
      total: 0.51
      efficiency: 0.41
      win: 0.51
      pick: 0.38
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
    The World Stone:
      total: 0.47
      efficiency: 0.36
      win: 0.54
      pick: 0.3
      fit: 0.56
    Obsidian Shard:
      total: 0.46
      efficiency: 0.36
      win: 0.53
      pick: 0.2
      fit: 0.56
    Soul Gem:
      total: 0.5
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - The Cosmic Horror
  - The World Stone
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - The World Stone
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
    Talon, Gluttonous Grimoire, Shield of the Phoenix, The Cosmic Horror, Kinetic
    Cuirass, Eye of Providence, Lifebinder, Chandra''s Grace, Spear of the Magus,
    Spirit Robe, Genji''s Guard, Phoenix Feather, Doom Orb, Spectral Armor, Ethereal
    Staff, Helm of Radiance, Breastplate of Valor, Erosion, Death Metal, Chronos''
    Pendant.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.47
      efficiency: 0.41
      win: 0.51
      pick: 0.38
      fit: 0.49
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.39
    The World Stone:
      total: 0.44
      efficiency: 0.36
      win: 0.54
      pick: 0.3
      fit: 0.39
    Amanita Charm:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.5
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
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
    for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear of the Magus,
    Doom Orb, Ethereal Staff, Rod of Asclepius, Blood-Bound Book, Chronos'' Pendant,
    Screeching Gargoyle, Death Metal, Bancroft''s Talon, Ancient Signet, Genji''s
    Guard, Helm of Radiance, Gem of Focus, Alchemist Coat, Divine Ruin, Lifebinder,
    Jade Scepter, Bragi''s Harp, Book of Thoth.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.54
      efficiency: 0.41
      win: 0.51
      pick: 0.38
      fit: 1.0
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.86
    Spear of the Magus:
      total: 0.5
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.86
    The World Stone:
      total: 0.51
      efficiency: 0.36
      win: 0.54
      pick: 0.3
      fit: 0.86
    Obsidian Shard:
      total: 0.5
      efficiency: 0.36
      win: 0.53
      pick: 0.2
      fit: 0.86
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
---
