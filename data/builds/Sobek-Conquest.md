---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.4
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.24
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.23
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.17
      win_rate: 0.51
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.52
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.25
      win_rate: 0.5
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.48
  - name: Dwarven Plate
    pick_rate: 0.13
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.55
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.54
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.58
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 0.54
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.56
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.47
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.5
  source_url: https://smitebrain.com/gods/sobek/
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion, Spectral
    Armor, Breastplate of Valor, Shield of the Phoenix, Gluttonous Grimoire, Shifter''s
    Shield, Gladiator''s Shield, Rod of Asclepius, Ethereal Staff, Draconic Scale,
    Midgardian Mail, Shroud of Vengeance, Mantle Of Discord, Prophetic Cloak, Freya''s
    Tears, Soul Gem, Chandra''s Grace, Leviathan''s Hide, Phoenix Feather, Ancile,
    Magi''s Cloak, Oni Hunter''s Garb, Helm of Radiance.'
  slot_scores:
    Eye of Providence:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.48
      efficiency: 0.46
      win: 0.55
      pick: 0.18
      fit: 0.39
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.81
    Spectral Armor:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.47
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.71
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
  - Genji's Guard
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Eye of Providence, Soul Gem, Chandra''s Grace, Phoenix Feather, Spectral Armor,
    Lifebinder, Blood-Bound Book, Breastplate of Valor, Erosion, Gluttonous Grimoire,
    Spirit Robe, Bancroft''s Talon, Ethereal Staff, Glorious Pridwen, Gladiator''s
    Shield, Midgardian Mail, Leviathan''s Hide, Spear of Desolation, Ancile, Shifter''s
    Shield, The Cosmic Horror, Oni Hunter''s Garb.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.46
      efficiency: 0.46
      win: 0.55
      pick: 0.18
      fit: 0.29
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
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
      fit: 0.35
    Amanita Charm:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.83
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Soul Gem,
    Amanita Charm, The Cosmic Horror, Spear of Desolation, Screeching Gargoyle, Spectral
    Armor, Breastplate of Valor, Stone of Binding, Void Stone, Spear of the Magus,
    Erosion, Void Shield, Doom Orb, Shield of the Phoenix, Rod of Asclepius, Ethereal
    Staff, The World Stone, Obsidian Shard, Chandra''s Grace, Midgardian Mail, Gladiator''s
    Shield, Shroud of Vengeance, Mantle Of Discord.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.46
      efficiency: 0.46
      win: 0.55
      pick: 0.18
      fit: 0.27
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
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
      fit: 0.51
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.41
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
