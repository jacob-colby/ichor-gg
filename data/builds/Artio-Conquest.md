---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.28
  aspect_win_rate: 0.59
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.35
    win_rate: 0.57
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.07
      win_rate: 0.55
    - name: Gauntlet of Thebes
      pick_rate: 0.06
      win_rate: 0.42
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.58
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.19
      win_rate: 0.62
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.49
  - name: Dwarven Plate
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.57
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.54
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.55
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.17
      win_rate: 0.53
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.46
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.4
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 0.62
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
  - name: Spirit Robe
    pick_rate: 0.06
    win_rate: 0.64
    alternates:
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.65
    - name: Olmec Blue
      pick_rate: 0.04
      win_rate: 0.64
  source_url: https://smitebrain.com/gods/artio/
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
    Armor, Shield of the Phoenix, Gladiator''s Shield, Draconic Scale, Midgardian
    Mail, Prophetic Cloak, Freya''s Tears, Breastplate of Valor, Shroud of Vengeance,
    Mantle Of Discord, Leviathan''s Hide, Phoenix Feather, Chandra''s Grace, Ancile,
    Oni Hunter''s Garb, Magi''s Cloak, Gluttonous Grimoire, Void Stone, Rod of Asclepius,
    Stone of Binding, Ethereal Staff.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.84
    Genji's Guard:
      total: 0.5
      efficiency: 0.46
      win: 0.58
      pick: 0.2
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.94
    Shifter's Shield:
      total: 0.5
      efficiency: 0.3
      win: 0.57
      pick: 0.35
      fit: 0.84
    Amanita Charm:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.84
    Erosion:
      total: 0.49
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Spirit Robe
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Spirit Robe, Shield of the Phoenix, Kinetic Cuirass,
    Eye of Providence, Chandra''s Grace, Rod of Asclepius, Phoenix Feather, Spectral
    Armor, Erosion, Soul Gem, Lifebinder, Blood-Bound Book, Glorious Pridwen, Gladiator''s
    Shield, Bancroft''s Talon, Midgardian Mail, Gluttonous Grimoire, Breastplate of
    Valor, Ethereal Staff, Draconic Scale, Leviathan''s Hide, Ancile, Oni Hunter''s
    Garb, Shroud of Vengeance.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.48
      efficiency: 0.46
      win: 0.58
      pick: 0.2
      fit: 0.33
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
    Spirit Robe:
      total: 0.51
      efficiency: 0.32
      win: 0.64
      pick: 0.06
      fit: 0.71
    Shifter's Shield:
      total: 0.47
      efficiency: 0.3
      win: 0.57
      pick: 0.35
      fit: 0.62
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
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  - Spectral Armor
  flex_slots:
  - Shifter's Shield
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Amanita
    Charm, Soul Gem, Spectral Armor, The Cosmic Horror, Screeching Gargoyle, Spear
    of Desolation, Void Stone, Stone of Binding, Erosion, Void Shield, Spear of the
    Magus, Shield of the Phoenix, Doom Orb, Breastplate of Valor, Chandra''s Grace,
    Rod of Asclepius, The World Stone, Ethereal Staff, Midgardian Mail, Obsidian Shard,
    Gladiator''s Shield, Leviathan''s Hide, Phoenix Feather.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.51
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.58
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.45
      efficiency: 0.3
      win: 0.57
      pick: 0.35
      fit: 0.51
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.33
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
