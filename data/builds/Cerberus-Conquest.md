---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.35
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.3
    win_rate: 0.58
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.61
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.26
    win_rate: 0.61
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.63
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.7
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.68
    alternates:
    - name: Genji's Guard
      pick_rate: 0.22
      win_rate: 0.61
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.69
  - name: Dwarven Plate
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.62
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.59
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.64
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.62
    alternates:
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.64
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-07-23'
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
  - Amanita Charm
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
    this god: Breastplate of Valor, Kinetic Cuirass, Eye of Providence, Amanita Charm,
    Spectral Armor, Erosion, Shield of the Phoenix, Gluttonous Grimoire, Rod of Asclepius,
    Ethereal Staff, Gladiator''s Shield, Midgardian Mail, Soul Gem, Draconic Scale,
    Shroud of Vengeance, Mantle Of Discord, Chandra''s Grace, Prophetic Cloak, Leviathan''s
    Hide, Freya''s Tears, Phoenix Feather, Ancile, Magi''s Cloak, Oni Hunter''s Garb,
    Helm of Radiance.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.63
    Genji's Guard:
      total: 0.5
      efficiency: 0.46
      win: 0.61
      pick: 0.26
      fit: 0.35
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.42
      win: 0.68
      pick: 0.14
      fit: 0.35
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
    Shifter's Shield:
      total: 0.47
      efficiency: 0.3
      win: 0.58
      pick: 0.3
      fit: 0.63
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
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
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Soul Gem, Eye of Providence, Chandra''s Grace, Phoenix Feather,
    Spectral Armor, Blood-Bound Book, Lifebinder, Bancroft''s Talon, Gluttonous Grimoire,
    Erosion, Spirit Robe, Ethereal Staff, Glorious Pridwen, Gladiator''s Shield, Midgardian
    Mail, Spear of Desolation, The Cosmic Horror, Leviathan''s Hide, Ancile, Yogi''s
    Necklace, Oni Hunter''s Garb.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.49
      efficiency: 0.46
      win: 0.61
      pick: 0.26
      fit: 0.26
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.42
      win: 0.68
      pick: 0.14
      fit: 0.26
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shield of the Phoenix:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.72
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Eye of Providence
  - Shifter's Shield
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
    of Providence, Soul Gem, Amanita Charm, The Cosmic Horror, Spear of Desolation,
    Screeching Gargoyle, Spectral Armor, Void Stone, Stone of Binding, Spear of the
    Magus, Void Shield, Erosion, Doom Orb, Shield of the Phoenix, Rod of Asclepius,
    Ethereal Staff, The World Stone, Obsidian Shard, Chandra''s Grace, Midgardian
    Mail, Gladiator''s Shield, Shroud of Vengeance, Mantle Of Discord.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.49
      efficiency: 0.46
      win: 0.61
      pick: 0.26
      fit: 0.25
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.42
      win: 0.68
      pick: 0.14
      fit: 0.25
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shifter's Shield:
      total: 0.45
      efficiency: 0.3
      win: 0.58
      pick: 0.3
      fit: 0.45
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
