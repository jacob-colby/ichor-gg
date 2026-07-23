---
type: smite-build
god: Geb
mode: Conquest
builds:
- source: community
  aspect: Aspect of Calamity
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.36
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.31
    win_rate: 0.56
    alternates:
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.61
    - name: Yogi's Necklace
      pick_rate: 0.1
      win_rate: 0.77
  - name: Genji's Guard
    pick_rate: 0.29
    win_rate: 0.59
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.11
      win_rate: 0.62
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.42
  - name: Breastplate of Valor
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.56
  - name: Dwarven Plate
    pick_rate: 0.12
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.64
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.45
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.69
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.65
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.64
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.58
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.38
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.63
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-07-23'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion, Spectral
    Armor, Shield of the Phoenix, Shifter''s Shield, Draconic Scale, Gladiator''s
    Shield, Prophetic Cloak, Freya''s Tears, Shroud of Vengeance, Mantle Of Discord,
    Midgardian Mail, Magi''s Cloak, Leviathan''s Hide, Phoenix Feather, Ancile, Oni
    Hunter''s Garb, Chandra''s Grace, Stone of Binding, Spirit Robe, Gluttonous Grimoire,
    Void Stone, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.85
    Genji's Guard:
      total: 0.51
      efficiency: 0.46
      win: 0.59
      pick: 0.29
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.95
    Spectral Armor:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.49
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Chandra''s Grace, Rod of Asclepius, Phoenix Feather, Spectral Armor, Erosion,
    Soul Gem, Spirit Robe, Lifebinder, Blood-Bound Book, Glorious Pridwen, Gladiator''s
    Shield, Bancroft''s Talon, Midgardian Mail, Gluttonous Grimoire, Shifter''s Shield,
    Ethereal Staff, Draconic Scale, Leviathan''s Hide, Ancile, Oni Hunter''s Garb,
    Shroud of Vengeance.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.49
      efficiency: 0.46
      win: 0.59
      pick: 0.29
      fit: 0.33
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.84
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spectral Armor
  flex_slots:
  - Spectral Armor
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Kinetic Cuirass, Gluttonous Grimoire, Eye of Providence, Amanita
    Charm, Soul Gem, Spectral Armor, Screeching Gargoyle, The Cosmic Horror, Stone
    of Binding, Spear of Desolation, Void Stone, Erosion, Void Shield, Shield of the
    Phoenix, Spear of the Magus, Doom Orb, Midgardian Mail, Rod of Asclepius, Ethereal
    Staff, Chandra''s Grace, Gladiator''s Shield, The World Stone, Shroud of Vengeance,
    Mantle Of Discord, Obsidian Shard.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.45
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.68
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.48
      efficiency: 0.46
      win: 0.59
      pick: 0.29
      fit: 0.28
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.34
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
