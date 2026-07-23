---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.24
    win_rate: 0.55
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.52
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.51
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.56
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.53
  - name: Spirit Robe
    pick_rate: 0.09
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.54
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.43
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.63
    alternates:
    - name: Spirit Robe
      pick_rate: 0.1
      win_rate: 0.58
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.45
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.35
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.61
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.71
  - name: Circle of Protection
    pick_rate: 0.07
    win_rate: 0.43
    alternates:
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.56
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.3
  source_url: https://smitebrain.com/gods/ymir/
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
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Genji's Guard
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion, Spectral
    Armor, Shield of the Phoenix, Gluttonous Grimoire, Gladiator''s Shield, Draconic
    Scale, Rod of Asclepius, Ethereal Staff, Midgardian Mail, Breastplate of Valor,
    Shroud of Vengeance, Mantle Of Discord, Prophetic Cloak, Freya''s Tears, Leviathan''s
    Hide, Phoenix Feather, Chandra''s Grace, Ancile, Magi''s Cloak, Oni Hunter''s
    Garb, Stone of Binding, Helm of Radiance.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.42
      efficiency: 0.46
      win: 0.51
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.44
      efficiency: 0.3
      win: 0.55
      pick: 0.24
      fit: 0.72
    Amanita Charm:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.42
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.72
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Eye of Providence, Chandra''s Grace, Soul Gem, Phoenix Feather, Spectral Armor,
    Lifebinder, Blood-Bound Book, Spirit Robe, Erosion, Bancroft''s Talon, Gluttonous
    Grimoire, Ethereal Staff, Glorious Pridwen, Gladiator''s Shield, Breastplate of
    Valor, Midgardian Mail, Leviathan''s Hide, Ancile, Oni Hunter''s Garb, Shroud
    of Vengeance, Draconic Scale.'
  slot_scores:
    Eye of Providence:
      total: 0.42
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.41
      efficiency: 0.46
      win: 0.51
      pick: 0.16
      fit: 0.29
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shield of the Phoenix:
      total: 0.43
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.77
    Shifter's Shield:
      total: 0.41
      efficiency: 0.3
      win: 0.55
      pick: 0.24
      fit: 0.53
    Amanita Charm:
      total: 0.46
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
  - Shifter's Shield
  - The Cosmic Horror
  flex_slots:
  - Genji's Guard
  - The Cosmic Horror
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
    Amanita Charm, The Cosmic Horror, Spear of Desolation, Spectral Armor, Screeching
    Gargoyle, Stone of Binding, Void Stone, Spear of the Magus, Void Shield, Erosion,
    Doom Orb, Shield of the Phoenix, Rod of Asclepius, Ethereal Staff, The World Stone,
    Obsidian Shard, Breastplate of Valor, Chandra''s Grace, Midgardian Mail, Gladiator''s
    Shield, Shroud of Vengeance, Mantle Of Discord.'
  slot_scores:
    Eye of Providence:
      total: 0.41
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.4
      efficiency: 0.46
      win: 0.51
      pick: 0.16
      fit: 0.25
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.4
      efficiency: 0.3
      win: 0.55
      pick: 0.24
      fit: 0.48
    The Cosmic Horror:
      total: 0.4
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.4
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
