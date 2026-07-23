---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.59
  aspect_win_rate: 0.55
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.25
    win_rate: 0.54
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.13
      win_rate: 0.55
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.51
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.15
      win_rate: 0.67
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.55
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.64
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.54
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.57
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.87
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.53
  - name: Spirit Robe
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.6
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.75
  - name: Circle of Protection
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Sage's Ring
      pick_rate: 0.07
      win_rate: 0.67
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.63
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-07-23'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Kinetic Cuirass, Eye of Providence, Amanita Charm,
    Erosion, Spectral Armor, Shield of the Phoenix, Gluttonous Grimoire, Gladiator''s
    Shield, Shifter''s Shield, Rod of Asclepius, Ethereal Staff, Draconic Scale, Prophetic
    Cloak, Freya''s Tears, Midgardian Mail, Soul Gem, Shroud of Vengeance, Mantle
    Of Discord, Chandra''s Grace, Leviathan''s Hide, Phoenix Feather, Ancile, Magi''s
    Cloak, Oni Hunter''s Garb, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.7
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.42
      win: 0.64
      pick: 0.15
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.8
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
  - Breastplate of Valor
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
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Breastplate of Valor, Shield of the Phoenix, Kinetic
    Cuirass, Rod of Asclepius, Soul Gem, Eye of Providence, Spirit Robe, Chandra''s
    Grace, Phoenix Feather, Spectral Armor, Lifebinder, Blood-Bound Book, Erosion,
    Gluttonous Grimoire, Bancroft''s Talon, Ethereal Staff, Glorious Pridwen, Gladiator''s
    Shield, Midgardian Mail, Spear of Desolation, Leviathan''s Hide, Ancile, Shifter''s
    Shield, The Cosmic Horror, Oni Hunter''s Garb.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.52
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.42
      win: 0.64
      pick: 0.15
      fit: 0.3
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
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
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
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Breastplate of Valor, Gluttonous Grimoire, Kinetic Cuirass, Eye
    of Providence, Soul Gem, Amanita Charm, Spear of Desolation, The Cosmic Horror,
    Screeching Gargoyle, Spectral Armor, Stone of Binding, Void Stone, Spear of the
    Magus, Erosion, Void Shield, Shield of the Phoenix, Doom Orb, Rod of Asclepius,
    Ethereal Staff, The World Stone, Obsidian Shard, Chandra''s Grace, Gladiator''s
    Shield, Midgardian Mail, Shroud of Vengeance, Mantle Of Discord.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.42
      win: 0.64
      pick: 0.15
      fit: 0.28
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
