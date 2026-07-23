---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.37
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.45
    win_rate: 0.54
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.35
      win_rate: 0.51
    - name: Gauntlet of Thebes
      pick_rate: 0.03
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.59
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.43
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.44
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.25
      win_rate: 0.46
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.21
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.65
  - name: Spirit Robe
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.13
      win_rate: 0.6
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.45
  - name: Engraved Guard
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.62
  source_url: https://smitebrain.com/gods/cabrakan/
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
  - Shifter's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion, Spectral
    Armor, Shield of the Phoenix, Breastplate of Valor, Gluttonous Grimoire, Gladiator''s
    Shield, Draconic Scale, Midgardian Mail, Shroud of Vengeance, Prophetic Cloak,
    Mantle Of Discord, Freya''s Tears, Rod of Asclepius, Ethereal Staff, Leviathan''s
    Hide, Chandra''s Grace, Phoenix Feather, Magi''s Cloak, Ancile, Soul Gem, Oni
    Hunter''s Garb, Stone of Binding.'
  slot_scores:
    Eye of Providence:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.5
      efficiency: 0.46
      win: 0.59
      pick: 0.19
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.83
    Shifter's Shield:
      total: 0.48
      efficiency: 0.3
      win: 0.54
      pick: 0.45
      fit: 0.73
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Erosion:
      total: 0.47
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.73
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
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Spirit Robe, Kinetic Cuirass,
    Eye of Providence, Rod of Asclepius, Chandra''s Grace, Soul Gem, Phoenix Feather,
    Spectral Armor, Lifebinder, Erosion, Blood-Bound Book, Gluttonous Grimoire, Breastplate
    of Valor, Bancroft''s Talon, Ethereal Staff, Glorious Pridwen, Gladiator''s Shield,
    Midgardian Mail, Leviathan''s Hide, Ancile, Draconic Scale, Oni Hunter''s Garb,
    Shroud of Vengeance.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.48
      efficiency: 0.46
      win: 0.59
      pick: 0.19
      fit: 0.3
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
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
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.84
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Soul Gem,
    Amanita Charm, The Cosmic Horror, Spear of Desolation, Screeching Gargoyle, Spectral
    Armor, Stone of Binding, Void Stone, Erosion, Void Shield, Spear of the Magus,
    Breastplate of Valor, Shield of the Phoenix, Doom Orb, Rod of Asclepius, Ethereal
    Staff, The World Stone, Obsidian Shard, Chandra''s Grace, Midgardian Mail, Gladiator''s
    Shield, Shroud of Vengeance, Mantle Of Discord.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.48
      efficiency: 0.46
      win: 0.59
      pick: 0.19
      fit: 0.27
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
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
      fit: 0.5
    The Cosmic Horror:
      total: 0.45
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
