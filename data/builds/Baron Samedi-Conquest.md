---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.79
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.2
    win_rate: 0.46
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.57
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.49
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.49
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.52
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.59
  - name: Breastplate of Valor
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.49
    - name: Soul Gem
      pick_rate: 0.11
      win_rate: 0.41
  - name: Rod of Tahuti
    pick_rate: 0.14
    win_rate: 0.45
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.68
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.61
  - name: Obsidian Shard
    pick_rate: 0.1
    win_rate: 0.42
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.48
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.66
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.31
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.53
    - name: Obsidian Shard
      pick_rate: 0.04
      win_rate: 0.64
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-07-25'
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spectral Armor
  flex_slots:
  - Spectral Armor
  - The Cosmic Horror
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
    this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Soul Gem, Breastplate
    of Valor, Amanita Charm, Spectral Armor, The Cosmic Horror, Ethereal Staff, Rod
    of Asclepius, Genji''s Guard, Erosion, Shield of the Phoenix, Spear of the Magus,
    Doom Orb, Helm of Radiance, Chandra''s Grace, Blood-Bound Book, Alchemist Coat,
    Chronos'' Pendant, Lifebinder, Gladiator''s Shield, Jade Scepter, Midgardian Mail,
    The World Stone, Death Metal.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.42
      win: 0.57
      pick: 0.12
      fit: 0.31
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.43
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  flex_slots:
  - The Cosmic Horror
  - Spear of Desolation
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Breastplate of Valor, Eye
    of Providence, The Cosmic Horror, Amanita Charm, Spectral Armor, Genji''s Guard,
    Ethereal Staff, Rod of Asclepius, Spear of the Magus, Shield of the Phoenix, Death
    Metal, Doom Orb, Erosion, Chandra''s Grace, Blood-Bound Book, Chronos'' Pendant,
    Triton''s Conch, The World Stone, Helm of Radiance, Bragi''s Harp, Gladiator''s
    Shield, Alchemist Coat, Obsidian Shard.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.37
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.42
      win: 0.57
      pick: 0.12
      fit: 0.27
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.44
      efficiency: 0.41
      win: 0.46
      pick: 0.2
      fit: 0.49
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
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
    this god: Soul Gem, Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Chandra''s Grace, Blood-Bound Book, Kinetic Cuirass, Lifebinder, Eye
    of Providence, Bancroft''s Talon, Breastplate of Valor, Phoenix Feather, Spectral
    Armor, Ethereal Staff, The Cosmic Horror, Genji''s Guard, Erosion, Spear of the
    Magus, Spirit Robe, Doom Orb, Helm of Radiance, Alchemist Coat, Chronos'' Pendant,
    Jade Scepter, Death Metal.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.42
      win: 0.57
      pick: 0.12
      fit: 0.25
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.49
    Spectral Armor:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.26
    Amanita Charm:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  flex_slots:
  - Spear of Desolation
  - Breastplate of Valor
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
    for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Kinetic Cuirass,
    Eye of Providence, Breastplate of Valor, Spear of the Magus, Amanita Charm, Screeching
    Gargoyle, Spectral Armor, Doom Orb, Ethereal Staff, Rod of Asclepius, Void Stone,
    Genji''s Guard, Void Shield, The World Stone, Stone of Binding, Erosion, Shield
    of the Phoenix, Blood-Bound Book, Chandra''s Grace, Helm of Radiance, Alchemist
    Coat, Chronos'' Pendant, Obsidian Shard.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.41
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.42
      win: 0.57
      pick: 0.12
      fit: 0.26
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.45
      efficiency: 0.41
      win: 0.46
      pick: 0.2
      fit: 0.59
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.46
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
