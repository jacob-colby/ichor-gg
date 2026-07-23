---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.26
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.34
    win_rate: 0.53
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.46
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.51
    - name: Prophetic Cloak
      pick_rate: 0.14
      win_rate: 0.58
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.42
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.47
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.14
      win_rate: 0.56
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.44
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.48
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 0.59
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.52
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.6
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.67
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.6
  source_url: https://smitebrain.com/gods/bacchus/
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
  - Erosion
  - Shifter's Shield
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
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Genji''s Guard, Erosion,
    Spectral Armor, Shield of the Phoenix, Gluttonous Grimoire, Gladiator''s Shield,
    Draconic Scale, Freya''s Tears, Breastplate of Valor, Midgardian Mail, Rod of
    Asclepius, Shroud of Vengeance, Ethereal Staff, Prophetic Cloak, Mantle Of Discord,
    Leviathan''s Hide, Chandra''s Grace, Phoenix Feather, Ancile, Magi''s Cloak, Soul
    Gem, Oni Hunter''s Garb, Stone of Binding.'
  slot_scores:
    Eye of Providence:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.49
      efficiency: 0.46
      win: 0.57
      pick: 0.15
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.83
    Shifter's Shield:
      total: 0.47
      efficiency: 0.3
      win: 0.53
      pick: 0.34
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
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Eye of Providence, Genji''s Guard, Chandra''s Grace, Soul Gem, Phoenix Feather,
    Spectral Armor, Lifebinder, Blood-Bound Book, Erosion, Spirit Robe, Gluttonous
    Grimoire, Bancroft''s Talon, Ethereal Staff, Glorious Pridwen, Gladiator''s Shield,
    Breastplate of Valor, Midgardian Mail, Leviathan''s Hide, Ancile, Oni Hunter''s
    Garb, Draconic Scale, Shroud of Vengeance.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.57
      pick: 0.15
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
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Genji''s Guard, Eye of Providence,
    Soul Gem, Amanita Charm, The Cosmic Horror, Spear of Desolation, Screeching Gargoyle,
    Spectral Armor, Stone of Binding, Void Stone, Erosion, Void Shield, Spear of the
    Magus, Shield of the Phoenix, Doom Orb, Rod of Asclepius, Ethereal Staff, The
    World Stone, Breastplate of Valor, Obsidian Shard, Chandra''s Grace, Midgardian
    Mail, Gladiator''s Shield, Shroud of Vengeance, Mantle Of Discord.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.57
      pick: 0.15
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
