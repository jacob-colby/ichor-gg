---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.12
    win_rate: 0.39
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.44
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.43
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.23
      win_rate: 0.59
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.7
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.78
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.8
  - name: Mote of Chaos
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.53
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.5
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.75
    alternates:
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 0.75
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.75
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-08-01'
  god_win_rate: 0.5167785234899329
  god_matches_won: 77
  god_matches_played: 149
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
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
  - Spectral Armor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Kinetic Cuirass, Eye of Providence, Amanita Charm,
    Gluttonous Grimoire, Spectral Armor, Erosion, Shield of the Phoenix, Ethereal
    Staff, Rod of Asclepius, Gladiator''s Shield, Chandra''s Grace, Freya''s Tears,
    Midgardian Mail, Soul Gem, Prophetic Cloak, Shifter''s Shield, Spear of the Magus,
    Draconic Scale, Genji''s Guard, Helm of Radiance, Mantle Of Discord, Leviathan''s
    Hide, Shroud of Vengeance, Screeching Gargoyle, Oni Hunter''s Garb, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.63
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.42
      win: 0.62
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
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
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Breastplate
    of Valor, Kinetic Cuirass, Chandra''s Grace, Eye of Providence, Gluttonous Grimoire,
    Soul Gem, Lifebinder, Phoenix Feather, Spectral Armor, Blood-Bound Book, Erosion,
    Ethereal Staff, Bancroft''s Talon, Spirit Robe, Gladiator''s Shield, Glorious
    Pridwen, Midgardian Mail, Spear of the Magus, Alchemist Coat, Leviathan''s Hide,
    Shifter''s Shield, Oni Hunter''s Garb, Ancile, Genji''s Guard.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.62
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.42
      win: 0.62
      pick: 0.14
      fit: 0.36
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.9
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.43
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
  - Screeching Gargoyle
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of the Magus
  flex_slots:
  - Spear of the Magus
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
    for this god: Gluttonous Grimoire, Breastplate of Valor, Kinetic Cuirass, Eye
    of Providence, Spear of the Magus, Soul Gem, Amanita Charm, Screeching Gargoyle,
    Spectral Armor, Obsidian Shard, Void Stone, Stone of Binding, The Cosmic Horror,
    Void Shield, Erosion, Shield of the Phoenix, Ethereal Staff, Rod of Asclepius,
    Chandra''s Grace, Gladiator''s Shield, Midgardian Mail, Helm of Radiance, Genji''s
    Guard, Blood-Bound Book, Yogi''s Necklace, Leviathan''s Hide, Spear of Desolation.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.44
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.68
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.42
      win: 0.62
      pick: 0.14
      fit: 0.28
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.46
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
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
    Golden Blade:
      total: 0.22
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Tyrfing:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.24
      efficiency: 0.41
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
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Gluttonous
    Grimoire, Spectral Armor, Erosion, Shield of the Phoenix, Genji''s Guard, Ethereal
    Staff, Rod of Asclepius, Breastplate of Valor, Gladiator''s Shield, Chandra''s
    Grace, Freya''s Tears, Midgardian Mail, Soul Gem, Prophetic Cloak, Shifter''s
    Shield, Spear of the Magus, Draconic Scale, Helm of Radiance, Mantle Of Discord,
    Leviathan''s Hide, Shroud of Vengeance, Screeching Gargoyle, Oni Hunter''s Garb,
    Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.63
    Genji's Guard:
      total: 0.42
      efficiency: 0.46
      win: 0.43
      pick: 0.15
      fit: 0.39
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.46
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
---
