---
type: smite-build
god: The Morrigan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mischief
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.63
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.32
    win_rate: 0.48
    alternates:
    - name: Book of Thoth
      pick_rate: 0.31
      win_rate: 0.65
    - name: The World Stone
      pick_rate: 0.1
      win_rate: 0.6
  - name: The World Stone
    pick_rate: 0.38
    win_rate: 0.59
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.19
      win_rate: 0.62
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.59
  - name: Polynomicon
    pick_rate: 0.44
    win_rate: 0.63
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.78
    - name: The World Stone
      pick_rate: 0.07
      win_rate: 0.64
  - name: Rod of Tahuti
    pick_rate: 0.29
    win_rate: 0.52
    alternates:
    - name: Gem of Focus
      pick_rate: 0.16
      win_rate: 0.67
    - name: Polynomicon
      pick_rate: 0.15
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.2
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.27
      win_rate: 0.68
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.59
  - name: The Cosmic Horror
    pick_rate: 0.1
    win_rate: 0.73
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.15
      win_rate: 0.65
    - name: Gem of Focus
      pick_rate: 0.09
      win_rate: 0.7
  source_url: https://smitebrain.com/gods/the-morrigan/
  last_verified: '2026-08-01'
  god_win_rate: 0.6105769230769231
  god_matches_won: 127
  god_matches_played: 208
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
  - Polynomicon
  - Spear of Desolation
  - The Cosmic Horror
  - The World Stone
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Polynomicon
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
    this god: The Cosmic Horror, Soul Gem, Gluttonous Grimoire, Spear of the Magus,
    Doom Orb, Chronos'' Pendant, Ethereal Staff, Rod of Asclepius, Blood-Bound Book,
    Death Metal, Bancroft''s Talon, Ancient Signet, Gem of Focus, Helm of Radiance,
    Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s Harp, Jade Scepter, Book of
    Thoth, Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Polynomicon:
      total: 0.5
      efficiency: 0.35
      win: 0.63
      pick: 0.44
      fit: 0.5
    Spear of Desolation:
      total: 0.53
      efficiency: 0.43
      win: 0.48
      pick: 0.32
      fit: 1.0
    The Cosmic Horror:
      total: 0.62
      efficiency: 0.47
      win: 0.73
      pick: 0.1
      fit: 0.8
    The World Stone:
      total: 0.54
      efficiency: 0.37
      win: 0.59
      pick: 0.38
      fit: 0.8
    Obsidian Shard:
      total: 0.54
      efficiency: 0.32
      win: 0.67
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
  - Polynomicon
  - Spear of Desolation
  - The Cosmic Horror
  - The World Stone
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Polynomicon
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
    god: The Cosmic Horror, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom
    Orb, Death Metal, Chronos'' Pendant, Bragi''s Harp, Ethereal Staff, Rod of Asclepius,
    Blood-Bound Book, Genji''s Guard, Triton''s Conch, Bancroft''s Talon, Chandra''s
    Grace, Gem of Focus, Ancient Signet, Breastplate of Valor, Shield of the Phoenix,
    Spectral Armor, Helm of Radiance, Alchemist Coat, Kinetic Cuirass.'
  slot_scores:
    Polynomicon:
      total: 0.48
      efficiency: 0.35
      win: 0.63
      pick: 0.44
      fit: 0.32
    Spear of Desolation:
      total: 0.5
      efficiency: 0.43
      win: 0.48
      pick: 0.32
      fit: 0.78
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.47
      win: 0.73
      pick: 0.1
      fit: 0.56
    The World Stone:
      total: 0.5
      efficiency: 0.37
      win: 0.59
      pick: 0.38
      fit: 0.56
    Obsidian Shard:
      total: 0.51
      efficiency: 0.32
      win: 0.67
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
  - Polynomicon
  - The Cosmic Horror
  - The World Stone
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Amanita Charm
  - Polynomicon
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
    this god: The Cosmic Horror, Soul Gem, Amanita Charm, Rod of Asclepius, Blood-Bound
    Book, Gluttonous Grimoire, Bancroft''s Talon, Shield of the Phoenix, Kinetic Cuirass,
    Eye of Providence, Lifebinder, Spear of the Magus, Chandra''s Grace, Doom Orb,
    Spirit Robe, Phoenix Feather, Spectral Armor, Genji''s Guard, Ethereal Staff,
    Helm of Radiance, Erosion, Death Metal, Glorious Pridwen, Chronos'' Pendant, Breastplate
    of Valor.'
  slot_scores:
    Polynomicon:
      total: 0.47
      efficiency: 0.35
      win: 0.63
      pick: 0.44
      fit: 0.3
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.47
      win: 0.73
      pick: 0.1
      fit: 0.39
    The World Stone:
      total: 0.47
      efficiency: 0.37
      win: 0.59
      pick: 0.38
      fit: 0.39
    Obsidian Shard:
      total: 0.48
      efficiency: 0.32
      win: 0.67
      pick: 0.2
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
  - Gluttonous Grimoire
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
    for this god: The Cosmic Horror, Gluttonous Grimoire, Soul Gem, Spear of the Magus,
    Doom Orb, Ethereal Staff, Rod of Asclepius, Blood-Bound Book, Chronos'' Pendant,
    Screeching Gargoyle, Death Metal, Bancroft''s Talon, Ancient Signet, Helm of Radiance,
    Alchemist Coat, Gem of Focus, Divine Ruin, Lifebinder, Genji''s Guard, Bragi''s
    Harp, Dreamer''s Idol, Jade Scepter.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.53
      efficiency: 0.43
      win: 0.48
      pick: 0.32
      fit: 1.0
    The Cosmic Horror:
      total: 0.63
      efficiency: 0.47
      win: 0.73
      pick: 0.1
      fit: 0.86
    Spear of the Magus:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.86
    The World Stone:
      total: 0.54
      efficiency: 0.37
      win: 0.59
      pick: 0.38
      fit: 0.86
    Obsidian Shard:
      total: 0.55
      efficiency: 0.32
      win: 0.67
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
---
