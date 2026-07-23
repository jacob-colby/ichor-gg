---
type: smite-build
god: Ganesha
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Triumphant
  aspect_pick_rate: 0.26
  aspect_win_rate: 0.51
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.26
    win_rate: 0.47
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.47
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.38
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.38
    alternates:
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.44
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.56
  - name: Stampede
    pick_rate: 0.07
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.49
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.48
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.71
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.6
  - name: Dwarven Plate
    pick_rate: 0.06
    win_rate: 0.56
    alternates:
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.67
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.46
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Olmec Blue
      pick_rate: 0.03
      win_rate: 0.83
    - name: Circle of Protection
      pick_rate: 0.03
      win_rate: 0.67
  source_url: https://smitebrain.com/gods/ganesha/
  last_verified: '2026-07-23'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Gladiator's Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Gladiator's Shield
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
    Armor, Shield of the Phoenix, Gluttonous Grimoire, Gladiator''s Shield, Shifter''s
    Shield, Rod of Asclepius, Ethereal Staff, Breastplate of Valor, Draconic Scale,
    Prophetic Cloak, Freya''s Tears, Midgardian Mail, Soul Gem, Shroud of Vengeance,
    Mantle Of Discord, Chandra''s Grace, Leviathan''s Hide, Phoenix Feather, Ancile,
    Magi''s Cloak, Oni Hunter''s Garb, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.7
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.8
    Gladiator's Shield:
      total: 0.44
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.7
    Erosion:
      total: 0.47
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.7
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Soul Gem, Eye of Providence, Chandra''s Grace, Phoenix Feather, Spectral Armor,
    Lifebinder, Blood-Bound Book, Erosion, Gluttonous Grimoire, Bancroft''s Talon,
    Spirit Robe, Ethereal Staff, Glorious Pridwen, Breastplate of Valor, Gladiator''s
    Shield, Midgardian Mail, Spear of Desolation, Leviathan''s Hide, Ancile, Shifter''s
    Shield, The Cosmic Horror, Oni Hunter''s Garb.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.52
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.35
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.82
    Erosion:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Eye of Providence
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
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
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Soul Gem,
    Amanita Charm, Spear of Desolation, The Cosmic Horror, Screeching Gargoyle, Spectral
    Armor, Stone of Binding, Void Stone, Spear of the Magus, Erosion, Void Shield,
    Shield of the Phoenix, Doom Orb, Rod of Asclepius, Ethereal Staff, The World Stone,
    Breastplate of Valor, Obsidian Shard, Chandra''s Grace, Gladiator''s Shield, Midgardian
    Mail, Shroud of Vengeance, Mantle Of Discord.'
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
      fit: 0.49
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
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
