---
type: smite-build
god: Agni
mode: Conquest
builds:
- source: community
  aspect: Aspect of Combustion
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.53
    win_rate: 0.5
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.16
      win_rate: 0.57
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.46
  - name: Book of Thoth
    pick_rate: 0.16
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.61
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.56
  - name: Soul Gem
    pick_rate: 0.33
    win_rate: 0.56
    alternates:
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.45
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.48
  - name: Rod of Tahuti
    pick_rate: 0.36
    win_rate: 0.54
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.4
    - name: Soul Gem
      pick_rate: 0.06
      win_rate: 0.65
  - name: Obsidian Shard
    pick_rate: 0.24
    win_rate: 0.49
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.57
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.39
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.45
    alternates:
    - name: Void Shard
      pick_rate: 0.09
      win_rate: 0.4
    - name: Dreamer's Idol
      pick_rate: 0.07
      win_rate: 0.47
  source_url: https://smitebrain.com/gods/agni/
  last_verified: '2026-08-01'
  god_win_rate: 0.513953488372093
  god_matches_won: 221
  god_matches_played: 430
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
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
    The World Stone, Chronos'' Pendant, Ethereal Staff, Rod of Asclepius, Blood-Bound
    Book, Death Metal, Bancroft''s Talon, Ancient Signet, Gem of Focus, Helm of Radiance,
    Polynomicon, Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s Harp, Jade Scepter,
    Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.53
      fit: 1.0
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.79
    Doom Orb:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.49
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.79
    The World Stone:
      total: 0.47
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.56
      efficiency: 0.41
      win: 0.56
      pick: 0.33
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Death Metal
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
    Chandra''s Grace, Gem of Focus, Ancient Signet, Breastplate of Valor, Shield of
    the Phoenix, Spectral Armor, Helm of Radiance, Polynomicon, Alchemist Coat, Kinetic
    Cuirass.'
  slot_scores:
    Death Metal:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.52
      efficiency: 0.43
      win: 0.5
      pick: 0.53
      fit: 0.78
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Doom Orb:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.54
      efficiency: 0.41
      win: 0.56
      pick: 0.33
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Spear of Desolation
  - The Cosmic Horror
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Asclepius, Blood-Bound Book, Gluttonous Grimoire,
    Bancroft''s Talon, Shield of the Phoenix, The Cosmic Horror, Kinetic Cuirass,
    Eye of Providence, Lifebinder, Chandra''s Grace, Spear of the Magus, Doom Orb,
    Spirit Robe, Phoenix Feather, Spectral Armor, Genji''s Guard, Ethereal Staff,
    Helm of Radiance, The World Stone, Erosion, Chronos'' Pendant, Death Metal, Glorious
    Pridwen, Breastplate of Valor.'
  slot_scores:
    Eye of Providence:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.53
      fit: 0.49
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.54
      efficiency: 0.41
      win: 0.56
      pick: 0.33
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
    Orb, The World Stone, Ethereal Staff, Rod of Asclepius, Chronos'' Pendant, Blood-Bound
    Book, Screeching Gargoyle, Death Metal, Bancroft''s Talon, Ancient Signet, Helm
    of Radiance, Polynomicon, Gem of Focus, Alchemist Coat, Divine Ruin, Lifebinder,
    Genji''s Guard, Bragi''s Harp, Jade Scepter.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.53
      fit: 1.0
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.85
    Doom Orb:
      total: 0.5
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.85
    The World Stone:
      total: 0.48
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.85
    Soul Gem:
      total: 0.56
      efficiency: 0.41
      win: 0.56
      pick: 0.33
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
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
    Underrated for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the
    Magus, Doom Orb, The World Stone, Chronos'' Pendant, Ethereal Staff, Rod of Asclepius,
    Blood-Bound Book, Death Metal, Bancroft''s Talon, Ancient Signet, Gem of Focus,
    Helm of Radiance, Polynomicon, Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s
    Harp, Jade Scepter, Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.53
      fit: 1.0
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.79
    Doom Orb:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.49
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.79
    The World Stone:
      total: 0.47
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.56
      efficiency: 0.41
      win: 0.56
      pick: 0.33
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
    The World Stone, Chronos'' Pendant, Ethereal Staff, Rod of Asclepius, Blood-Bound
    Book, Bragi''s Harp, Death Metal, Bancroft''s Talon, Ancient Signet, Gem of Focus,
    Bracer of The Abyss, Helm of Radiance, Polynomicon, Alchemist Coat, Divine Ruin,
    Lifebinder, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.43
      win: 0.5
      pick: 0.53
      fit: 0.86
    The Cosmic Horror:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.68
    Doom Orb:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.68
    The World Stone:
      total: 0.46
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.56
      efficiency: 0.41
      win: 0.56
      pick: 0.33
      fit: 0.96
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Death Metal
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
    god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom Orb, Death
    Metal, The World Stone, Bragi''s Harp, Chronos'' Pendant, Ethereal Staff, Rod
    of Asclepius, Blood-Bound Book, Genji''s Guard, Triton''s Conch, Bancroft''s Talon,
    Chandra''s Grace, Ancient Signet, Gem of Focus, Spectral Armor, Breastplate of
    Valor, Shield of the Phoenix, Kinetic Cuirass, Helm of Radiance, Polynomicon,
    Alchemist Coat.'
  slot_scores:
    Death Metal:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.51
      efficiency: 0.43
      win: 0.5
      pick: 0.53
      fit: 0.71
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.51
    Doom Orb:
      total: 0.44
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of the Magus:
      total: 0.45
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.51
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.56
      pick: 0.33
      fit: 0.81
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Spear of Desolation
  - The Cosmic Horror
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Asclepius, Blood-Bound Book, Gluttonous Grimoire,
    Bancroft''s Talon, Shield of the Phoenix, The Cosmic Horror, Kinetic Cuirass,
    Lifebinder, Eye of Providence, Chandra''s Grace, Spear of the Magus, Doom Orb,
    Spirit Robe, Phoenix Feather, Spectral Armor, Genji''s Guard, Ethereal Staff,
    Helm of Radiance, The World Stone, Death Metal, Erosion, Chronos'' Pendant, Glorious
    Pridwen, Breastplate of Valor.'
  slot_scores:
    Eye of Providence:
      total: 0.43
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.53
      fit: 0.46
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.54
      efficiency: 0.41
      win: 0.56
      pick: 0.33
      fit: 0.86
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
    Orb, The World Stone, Ethereal Staff, Rod of Asclepius, Blood-Bound Book, Chronos''
    Pendant, Screeching Gargoyle, Death Metal, Bancroft''s Talon, Bragi''s Harp, Ancient
    Signet, Helm of Radiance, Polynomicon, Alchemist Coat, Genji''s Guard, Divine
    Ruin, Lifebinder, Gem of Focus, Bracer of The Abyss, Spectral Armor.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.43
      win: 0.5
      pick: 0.53
      fit: 0.9
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.77
    Doom Orb:
      total: 0.48
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.49
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.77
    The World Stone:
      total: 0.47
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.56
      efficiency: 0.41
      win: 0.56
      pick: 0.33
      fit: 1.0
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
    Underrated for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the
    Magus, Doom Orb, The World Stone, Chronos'' Pendant, Ethereal Staff, Rod of Asclepius,
    Blood-Bound Book, Bragi''s Harp, Death Metal, Bancroft''s Talon, Ancient Signet,
    Gem of Focus, Bracer of The Abyss, Helm of Radiance, Polynomicon, Alchemist Coat,
    Divine Ruin, Lifebinder, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.43
      win: 0.5
      pick: 0.53
      fit: 0.86
    The Cosmic Horror:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.68
    Doom Orb:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.68
    The World Stone:
      total: 0.46
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.56
      efficiency: 0.41
      win: 0.56
      pick: 0.33
      fit: 0.96
  starter: *id001
  aspect: Aspect of Combustion
---
