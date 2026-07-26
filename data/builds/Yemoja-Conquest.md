---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.41
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.18
    win_rate: 0.39
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.49
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.39
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.4
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.49
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.57
  - name: Breastplate of Valor
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.41
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.45
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.32
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.39
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.46
  - name: Freya's Tears
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.42
    - name: Stampede
      pick_rate: 0.05
      win_rate: 0.17
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.38
    alternates:
    - name: Legionnaire Armor
      pick_rate: 0.06
      win_rate: 0.25
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.43
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-07-25'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Eye of Providence, Amanita Charm, Spectral
    Armor, Erosion, Shield of the Phoenix, Gluttonous Grimoire, Ethereal Staff, Soul
    Gem, Rod of Asclepius, Breastplate of Valor, Gladiator''s Shield, Chandra''s Grace,
    Midgardian Mail, Shifter''s Shield, Draconic Scale, Prophetic Cloak, Helm of Radiance,
    Mantle Of Discord, Leviathan''s Hide, Ancile, Shroud of Vengeance, Phoenix Feather,
    Oni Hunter''s Garb, Genji''s Guard.'
  slot_scores:
    Eye of Providence:
      total: 0.49
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
    Freya's Tears:
      total: 0.5
      efficiency: 0.3
      win: 0.67
      pick: 0.05
      fit: 0.62
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.48
      efficiency: 0.44
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
  - Freya's Tears
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Soul Gem, Chandra''s
    Grace, Kinetic Cuirass, Eye of Providence, Blood-Bound Book, Lifebinder, Phoenix
    Feather, Spectral Armor, Gluttonous Grimoire, Bancroft''s Talon, Erosion, Ethereal
    Staff, Spirit Robe, Breastplate of Valor, Gladiator''s Shield, Glorious Pridwen,
    The Cosmic Horror, Midgardian Mail, Helm of Radiance, Alchemist Coat, Chronos''
    Pendant, Leviathan''s Hide, Genji''s Guard.'
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
    Freya's Tears:
      total: 0.48
      efficiency: 0.3
      win: 0.67
      pick: 0.05
      fit: 0.47
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Eye of Providence
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
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
    for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Eye of Providence,
    The Cosmic Horror, Amanita Charm, Screeching Gargoyle, Spectral Armor, Spear of
    the Magus, Void Stone, Stone of Binding, Erosion, Void Shield, Doom Orb, Shield
    of the Phoenix, Ethereal Staff, Rod of Asclepius, Breastplate of Valor, The World
    Stone, Obsidian Shard, Chandra''s Grace, Gladiator''s Shield, Midgardian Mail,
    Helm of Radiance, Blood-Bound Book, Genji''s Guard.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.44
      efficiency: 0.33
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
    Freya's Tears:
      total: 0.47
      efficiency: 0.3
      win: 0.67
      pick: 0.05
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
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
