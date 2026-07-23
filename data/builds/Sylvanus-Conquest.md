---
type: smite-build
god: Sylvanus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Grover's Wrath
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.5
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.14
    win_rate: 0.48
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.49
    - name: Tyrfing
      pick_rate: 0.1
      win_rate: 0.45
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.57
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.57
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 0.58
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.52
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.62
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.58
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.61
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.63
    alternates:
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.42
    - name: Draconic Scale
      pick_rate: 0.04
      win_rate: 0.64
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Legionnaire Armor
      pick_rate: 0.05
      win_rate: 0.65
    - name: Medallion
      pick_rate: 0.04
      win_rate: 0.8
  source_url: https://smitebrain.com/gods/sylvanus/
  last_verified: '2026-07-23'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Breastplate of Valor,
    Spectral Armor, Erosion, Shield of the Phoenix, Gluttonous Grimoire, Soul Gem,
    Rod of Asclepius, Ethereal Staff, Gladiator''s Shield, Chandra''s Grace, Spear
    of Desolation, Prophetic Cloak, Freya''s Tears, Shifter''s Shield, Midgardian
    Mail, Helm of Radiance, Draconic Scale, Shroud of Vengeance, Mantle Of Discord,
    Screeching Gargoyle, Leviathan''s Hide, Phoenix Feather, The Cosmic Horror.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.63
    Genji's Guard:
      total: 0.49
      efficiency: 0.46
      win: 0.57
      pick: 0.2
      fit: 0.39
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.42
      win: 0.55
      pick: 0.15
      fit: 0.39
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
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
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Soul Gem, Kinetic
    Cuirass, Chandra''s Grace, Eye of Providence, Blood-Bound Book, Lifebinder, Phoenix
    Feather, Breastplate of Valor, Spectral Armor, Bancroft''s Talon, Gluttonous Grimoire,
    Erosion, Ethereal Staff, Spirit Robe, Spear of Desolation, Glorious Pridwen, Gladiator''s
    Shield, The Cosmic Horror, Helm of Radiance, Midgardian Mail, Alchemist Coat,
    Chronos'' Pendant, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.57
      pick: 0.2
      fit: 0.31
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.42
      win: 0.55
      pick: 0.15
      fit: 0.31
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
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  flex_slots:
  - Spear of Desolation
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Eye of Providence,
    Spear of Desolation, The Cosmic Horror, Amanita Charm, Screeching Gargoyle, Breastplate
    of Valor, Spectral Armor, Spear of the Magus, Void Stone, Stone of Binding, Void
    Shield, Doom Orb, Erosion, Shield of the Phoenix, Rod of Asclepius, Ethereal Staff,
    The World Stone, Obsidian Shard, Chandra''s Grace, Gladiator''s Shield, Helm of
    Radiance, Midgardian Mail, Blood-Bound Book.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.57
      pick: 0.2
      fit: 0.28
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
    Spear of Desolation:
      total: 0.45
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
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
