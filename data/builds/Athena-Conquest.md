---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.62
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.53
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.6
  - name: Breastplate of Valor
    pick_rate: 0.18
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.59
  - name: Dwarven Plate
    pick_rate: 0.06
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.68
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.62
  - name: Spirit Robe
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.67
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.51
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.63
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.6
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.61
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-07-25'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion, Spectral
    Armor, Shield of the Phoenix, Gluttonous Grimoire, Draconic Scale, Gladiator''s
    Shield, Ethereal Staff, Midgardian Mail, Rod of Asclepius, Freya''s Tears, Mantle
    Of Discord, Chandra''s Grace, Leviathan''s Hide, Prophetic Cloak, Shroud of Vengeance,
    Ancile, Phoenix Feather, Oni Hunter''s Garb, Soul Gem, Magi''s Cloak, Screeching
    Gargoyle.'
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
      win: 0.58
      pick: 0.17
      fit: 0.4
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.42
      win: 0.57
      pick: 0.18
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.83
    Shifter's Shield:
      total: 0.47
      efficiency: 0.29
      win: 0.56
      pick: 0.16
      fit: 0.73
    Amanita Charm:
      total: 0.49
      efficiency: 0.44
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Breastplate of Valor
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Rod of Asclepius, Chandra''s Grace, Soul Gem, Spirit Robe, Phoenix Feather, Spectral
    Armor, Lifebinder, Erosion, Blood-Bound Book, Gluttonous Grimoire, Bancroft''s
    Talon, Ethereal Staff, Gladiator''s Shield, Glorious Pridwen, Midgardian Mail,
    Leviathan''s Hide, Ancile, Oni Hunter''s Garb, Draconic Scale, Spear of Desolation.'
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
      win: 0.58
      pick: 0.17
      fit: 0.3
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.42
      win: 0.57
      pick: 0.18
      fit: 0.3
    Kinetic Cuirass:
      total: 0.47
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
    Amanita Charm:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Cosmic Horror
  flex_slots:
  - Breastplate of Valor
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Soul Gem,
    Amanita Charm, The Cosmic Horror, Spectral Armor, Spear of Desolation, Screeching
    Gargoyle, Void Stone, Erosion, Stone of Binding, Void Shield, Spear of the Magus,
    Shield of the Phoenix, Doom Orb, Ethereal Staff, Rod of Asclepius, The World Stone,
    Obsidian Shard, Chandra''s Grace, Midgardian Mail, Gladiator''s Shield, Leviathan''s
    Hide, Ancile.'
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
      win: 0.58
      pick: 0.17
      fit: 0.27
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.42
      win: 0.57
      pick: 0.18
      fit: 0.27
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.65
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
