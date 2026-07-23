---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.78
  aspect_win_rate: 0.48
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.18
    win_rate: 0.43
    alternates:
    - name: Book of Thoth
      pick_rate: 0.13
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.46
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.46
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.6
  - name: Soul Gem
    pick_rate: 0.13
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.49
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.59
  - name: Rod of Tahuti
    pick_rate: 0.15
    win_rate: 0.45
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.54
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.72
  - name: Obsidian Shard
    pick_rate: 0.1
    win_rate: 0.46
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.62
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.46
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.29
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.5
    - name: Void Shard
      pick_rate: 0.04
      win_rate: 0.4
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-07-23'
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spectral Armor
  flex_slots:
  - The Cosmic Horror
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Amanita Charm,
    Spectral Armor, The Cosmic Horror, Rod of Asclepius, Ethereal Staff, Soul Gem,
    Erosion, Shield of the Phoenix, Spear of the Magus, Doom Orb, Helm of Radiance,
    Genji''s Guard, Breastplate of Valor, Blood-Bound Book, Chandra''s Grace, Alchemist
    Coat, Chronos'' Pendant, Lifebinder, Gladiator''s Shield, Jade Scepter, The World
    Stone, Ancient Signet, Midgardian Mail.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.37
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.32
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spectral Armor
  flex_slots:
  - Spectral Armor
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, The Cosmic Horror,
    Soul Gem, Amanita Charm, Spectral Armor, Rod of Asclepius, Ethereal Staff, Spear
    of the Magus, Shield of the Phoenix, Death Metal, Doom Orb, Erosion, Genji''s
    Guard, Chandra''s Grace, Breastplate of Valor, Blood-Bound Book, Chronos'' Pendant,
    The World Stone, Helm of Radiance, Triton''s Conch, Bragi''s Harp, Alchemist Coat,
    Gladiator''s Shield, Obsidian Shard.'
  slot_scores:
    Eye of Providence:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.47
    Ethereal Staff:
      total: 0.43
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.35
    Spectral Armor:
      total: 0.43
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.24
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - The Cosmic Horror
  - Spectral Armor
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - The Cosmic Horror
  - Spectral Armor
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
    this god: Amanita Charm, Rod of Asclepius, Soul Gem, Shield of the Phoenix, Gluttonous
    Grimoire, Blood-Bound Book, Chandra''s Grace, Lifebinder, Kinetic Cuirass, Bancroft''s
    Talon, Eye of Providence, Phoenix Feather, The Cosmic Horror, Spectral Armor,
    Ethereal Staff, Spirit Robe, Spear of the Magus, Erosion, Doom Orb, Genji''s Guard,
    Helm of Radiance, Alchemist Coat, Breastplate of Valor, Chronos'' Pendant, Glorious
    Pridwen, Ancient Signet.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.33
    Spectral Armor:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.26
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.69
    Rod of Asclepius:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Eye of Providence
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spear of the Magus
  flex_slots:
  - Spear of the Magus
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: Gluttonous Grimoire, The Cosmic Horror, Kinetic Cuirass, Soul Gem,
    Eye of Providence, Spear of the Magus, Screeching Gargoyle, Amanita Charm, Doom
    Orb, Spectral Armor, Rod of Asclepius, Ethereal Staff, Void Stone, Stone of Binding,
    Void Shield, The World Stone, Shield of the Phoenix, Erosion, Blood-Bound Book,
    Genji''s Guard, Helm of Radiance, Chandra''s Grace, Breastplate of Valor, Obsidian
    Shard, Alchemist Coat, Chronos'' Pendant.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.44
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.66
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of the Magus:
      total: 0.45
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.48
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
