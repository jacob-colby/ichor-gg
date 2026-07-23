---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.6
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.51
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.16
      win_rate: 0.52
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.49
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.49
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.53
  - name: Breastplate of Valor
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.51
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.52
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.51
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.62
  - name: Spirit Robe
    pick_rate: 0.07
    win_rate: 0.59
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.47
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.43
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.57
    - name: Medallion
      pick_rate: 0.05
      win_rate: 0.7
  source_url: https://smitebrain.com/gods/ares/
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
  - Spectral Armor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion, Spectral
    Armor, Shield of the Phoenix, Gluttonous Grimoire, Breastplate of Valor, Gladiator''s
    Shield, Draconic Scale, Prophetic Cloak, Freya''s Tears, Midgardian Mail, Rod
    of Asclepius, Ethereal Staff, Shroud of Vengeance, Mantle Of Discord, Chandra''s
    Grace, Soul Gem, Leviathan''s Hide, Phoenix Feather, Ancile, Magi''s Cloak, Oni
    Hunter''s Garb, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.45
      efficiency: 0.46
      win: 0.49
      pick: 0.21
      fit: 0.41
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.82
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
      fit: 0.72
    Erosion:
      total: 0.47
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
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Spirit Robe, Kinetic Cuirass,
    Rod of Asclepius, Eye of Providence, Chandra''s Grace, Soul Gem, Phoenix Feather,
    Spectral Armor, Lifebinder, Blood-Bound Book, Erosion, Gluttonous Grimoire, Bancroft''s
    Talon, Breastplate of Valor, Ethereal Staff, Glorious Pridwen, Gladiator''s Shield,
    Midgardian Mail, Leviathan''s Hide, Ancile, Spear of Desolation, Oni Hunter''s
    Garb, Shroud of Vengeance.'
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
      fit: 0.79
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
      fit: 0.83
    Erosion:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.53
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Soul Gem,
    Amanita Charm, Spear of Desolation, The Cosmic Horror, Screeching Gargoyle, Spectral
    Armor, Stone of Binding, Void Stone, Erosion, Void Shield, Spear of the Magus,
    Shield of the Phoenix, Doom Orb, Breastplate of Valor, Rod of Asclepius, Ethereal
    Staff, The World Stone, Obsidian Shard, Chandra''s Grace, Gladiator''s Shield,
    Midgardian Mail, Shroud of Vengeance, Mantle Of Discord.'
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
      fit: 0.64
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
