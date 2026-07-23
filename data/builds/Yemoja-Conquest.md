---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.42
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.2
    win_rate: 0.4
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.52
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.41
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.36
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.48
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.59
  - name: Breastplate of Valor
    pick_rate: 0.11
    win_rate: 0.42
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.42
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.38
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.2
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.44
    alternates:
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.18
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.05
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.6
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-07-23'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Ethereal Staff
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Spectral Armor, Erosion,
    Shield of the Phoenix, Gluttonous Grimoire, Soul Gem, Rod of Asclepius, Ethereal
    Staff, Gladiator''s Shield, Chandra''s Grace, Prophetic Cloak, Freya''s Tears,
    Shifter''s Shield, Midgardian Mail, Helm of Radiance, Draconic Scale, Shroud of
    Vengeance, Mantle Of Discord, Screeching Gargoyle, Leviathan''s Hide, Phoenix
    Feather, The Cosmic Horror, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.63
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
    Ethereal Staff:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.33
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.46
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Soul Gem, Kinetic
    Cuirass, Chandra''s Grace, Eye of Providence, Blood-Bound Book, Lifebinder, Phoenix
    Feather, Spectral Armor, Bancroft''s Talon, Gluttonous Grimoire, Erosion, Ethereal
    Staff, Spirit Robe, Glorious Pridwen, Gladiator''s Shield, The Cosmic Horror,
    Helm of Radiance, Midgardian Mail, Alchemist Coat, Chronos'' Pendant, Screeching
    Gargoyle, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.78
    Erosion:
      total: 0.43
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Eye of Providence
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Obsidian Shard
  flex_slots:
  - The Cosmic Horror
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
    for this god: Gluttonous Grimoire, Soul Gem, Obsidian Shard, Kinetic Cuirass,
    Eye of Providence, The Cosmic Horror, Amanita Charm, Screeching Gargoyle, Spectral
    Armor, Spear of the Magus, Void Stone, Stone of Binding, Void Shield, Doom Orb,
    Erosion, Shield of the Phoenix, Rod of Asclepius, Ethereal Staff, The World Stone,
    Chandra''s Grace, Gladiator''s Shield, Helm of Radiance, Midgardian Mail, Blood-Bound
    Book, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.45
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.68
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.43
    Obsidian Shard:
      total: 0.46
      efficiency: 0.36
      win: 0.6
      pick: 0.05
      fit: 0.43
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
