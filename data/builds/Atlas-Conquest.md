---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.58
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.18
    win_rate: 0.57
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.14
      win_rate: 0.52
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.4
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.49
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.32
  - name: Rod of Tahuti
    pick_rate: 0.07
    win_rate: 0.74
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.51
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.13
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.59
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.4
  - name: Obsidian Shard
    pick_rate: 0.07
    win_rate: 0.61
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.44
    - name: Hide of the Nemean Lion
      pick_rate: 0.04
      win_rate: 0.38
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.61
    - name: Legionnaire Armor
      pick_rate: 0.05
      win_rate: 0.64
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-07-23'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shifter's Shield
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
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion, Spectral
    Armor, Shield of the Phoenix, Gluttonous Grimoire, Gladiator''s Shield, Rod of
    Asclepius, Ethereal Staff, Draconic Scale, Breastplate of Valor, Midgardian Mail,
    Shroud of Vengeance, Mantle Of Discord, Prophetic Cloak, Freya''s Tears, Soul
    Gem, Chandra''s Grace, Leviathan''s Hide, Phoenix Feather, Ancile, Magi''s Cloak,
    Oni Hunter''s Garb, Helm of Radiance, Genji''s Guard.'
  slot_scores:
    Eye of Providence:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.71
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.81
    Shifter's Shield:
      total: 0.48
      efficiency: 0.3
      win: 0.57
      pick: 0.18
      fit: 0.71
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
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Spectral Armor
  - Shifter's Shield
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
    Eye of Providence, Soul Gem, Chandra''s Grace, Phoenix Feather, Spectral Armor,
    Lifebinder, Blood-Bound Book, Erosion, Gluttonous Grimoire, Spirit Robe, Bancroft''s
    Talon, Ethereal Staff, Glorious Pridwen, Gladiator''s Shield, Breastplate of Valor,
    Midgardian Mail, Leviathan''s Hide, Spear of Desolation, Ancile, The Cosmic Horror,
    Oni Hunter''s Garb, Genji''s Guard.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
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
    Shifter's Shield:
      total: 0.45
      efficiency: 0.3
      win: 0.57
      pick: 0.18
      fit: 0.53
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
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Eye of Providence
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
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Obsidian Shard, Eye of Providence,
    Soul Gem, Amanita Charm, The Cosmic Horror, Spear of Desolation, Screeching Gargoyle,
    Spectral Armor, Stone of Binding, Void Stone, Spear of the Magus, Erosion, Void
    Shield, Doom Orb, Shield of the Phoenix, Rod of Asclepius, Ethereal Staff, The
    World Stone, Breastplate of Valor, Chandra''s Grace, Midgardian Mail, Gladiator''s
    Shield, Shroud of Vengeance, Mantle Of Discord, Genji''s Guard.'
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
      fit: 0.41
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.24
      win: 0.74
      pick: 0.07
      fit: 0.41
    Obsidian Shard:
      total: 0.47
      efficiency: 0.36
      win: 0.61
      pick: 0.07
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
