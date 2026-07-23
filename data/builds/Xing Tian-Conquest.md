---
type: smite-build
god: Xing Tian
mode: Conquest
builds:
- source: community
  aspect: Aspect of Relentless Spite
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.42
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.34
    win_rate: 0.6
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.08
      win_rate: 0.54
    - name: Gauntlet of Thebes
      pick_rate: 0.07
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.63
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.16
      win_rate: 0.63
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.6
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.22
      win_rate: 0.61
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.59
  - name: Dwarven Plate
    pick_rate: 0.13
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.54
  - name: Ethereal Staff
    pick_rate: 0.06
    win_rate: 0.61
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.65
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.61
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.56
  source_url: https://smitebrain.com/gods/xing-tian/
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
  - Ethereal Staff
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Ethereal Staff, Breastplate
    of Valor, Erosion, Spectral Armor, Shield of the Phoenix, Gluttonous Grimoire,
    Gladiator''s Shield, Rod of Asclepius, Draconic Scale, Midgardian Mail, Shroud
    of Vengeance, Mantle Of Discord, Prophetic Cloak, Freya''s Tears, Soul Gem, Chandra''s
    Grace, Leviathan''s Hide, Phoenix Feather, Ancile, Magi''s Cloak, Oni Hunter''s
    Garb, Helm of Radiance.'
  slot_scores:
    Eye of Providence:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.51
      efficiency: 0.46
      win: 0.63
      pick: 0.19
      fit: 0.39
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.81
    Ethereal Staff:
      total: 0.49
      efficiency: 0.47
      win: 0.61
      pick: 0.06
      fit: 0.3
    Shifter's Shield:
      total: 0.5
      efficiency: 0.3
      win: 0.6
      pick: 0.34
      fit: 0.71
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Ethereal Staff
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Ethereal Staff, Kinetic Cuirass,
    Rod of Asclepius, Eye of Providence, Breastplate of Valor, Soul Gem, Chandra''s
    Grace, Phoenix Feather, Spectral Armor, Lifebinder, Blood-Bound Book, Erosion,
    Gluttonous Grimoire, Spirit Robe, Bancroft''s Talon, Glorious Pridwen, Gladiator''s
    Shield, Midgardian Mail, Leviathan''s Hide, Spear of Desolation, Ancile, The Cosmic
    Horror, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.46
      win: 0.63
      pick: 0.19
      fit: 0.29
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
    Ethereal Staff:
      total: 0.48
      efficiency: 0.47
      win: 0.61
      pick: 0.06
      fit: 0.26
    Shifter's Shield:
      total: 0.47
      efficiency: 0.3
      win: 0.6
      pick: 0.34
      fit: 0.53
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
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Ethereal Staff, Kinetic Cuirass, Breastplate
    of Valor, Eye of Providence, Soul Gem, Amanita Charm, The Cosmic Horror, Spear
    of Desolation, Screeching Gargoyle, Spectral Armor, Stone of Binding, Void Stone,
    Spear of the Magus, Erosion, Void Shield, Doom Orb, Shield of the Phoenix, Rod
    of Asclepius, The World Stone, Obsidian Shard, Chandra''s Grace, Midgardian Mail,
    Gladiator''s Shield, Shroud of Vengeance, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.46
      win: 0.63
      pick: 0.19
      fit: 0.27
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.42
      win: 0.6
      pick: 0.14
      fit: 0.27
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.47
      efficiency: 0.47
      win: 0.61
      pick: 0.06
      fit: 0.2
    Gluttonous Grimoire:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shifter's Shield:
      total: 0.46
      efficiency: 0.3
      win: 0.6
      pick: 0.34
      fit: 0.49
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
