---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.55
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.31
    win_rate: 0.57
    alternates:
    - name: Eye of Erebus
      pick_rate: 0.18
      win_rate: 0.43
    - name: Devourer's Gauntlet
      pick_rate: 0.13
      win_rate: 0.44
  - name: Prophetic Cloak
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.26
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.46
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.38
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.27
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.43
  - name: Ethereal Staff
    pick_rate: 0.11
    win_rate: 0.25
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.54
    - name: Dwarven Plate
      pick_rate: 0.1
      win_rate: 0.36
  - name: Soul Reaver
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.17
    - name: Midgardian Mail
      pick_rate: 0.05
      win_rate: 0.2
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.2
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.25
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-08-01'
  god_win_rate: 0.475
  god_matches_won: 57
  god_matches_played: 120
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
  - Kinetic Cuirass
  - Shifter's Shield
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
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Gluttonous Grimoire,
    Spectral Armor, Erosion, Shield of the Phoenix, Rod of Asclepius, Breastplate
    of Valor, Chandra''s Grace, Midgardian Mail, Gladiator''s Shield, Prophetic Cloak,
    Mantle Of Discord, Draconic Scale, Leviathan''s Hide, Freya''s Tears, Shroud of
    Vengeance, Oni Hunter''s Garb, Ancile, Phoenix Feather, Spear of the Magus, Magi''s
    Cloak, Yogi''s Necklace, Ethereal Staff.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.58
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shifter's Shield:
      total: 0.46
      efficiency: 0.29
      win: 0.57
      pick: 0.31
      fit: 0.58
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.58
    Erosion:
      total: 0.45
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.58
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
  - Shifter's Shield
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Rod of Asclepius, Chandra''s Grace, Gluttonous Grimoire, Phoenix Feather, Spectral
    Armor, Soul Gem, Lifebinder, Erosion, Blood-Bound Book, Bancroft''s Talon, Spirit
    Robe, Gladiator''s Shield, Midgardian Mail, Breastplate of Valor, Glorious Pridwen,
    Leviathan''s Hide, Yogi''s Necklace, Oni Hunter''s Garb, Ancile, Draconic Scale,
    Ethereal Staff.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shifter's Shield:
      total: 0.46
      efficiency: 0.29
      win: 0.57
      pick: 0.31
      fit: 0.56
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Eye of Providence
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  - Spear of the Magus
  flex_slots:
  - Shifter's Shield
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
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Amanita
    Charm, Spear of the Magus, Screeching Gargoyle, Spectral Armor, Soul Gem, Void
    Stone, Stone of Binding, Void Shield, Erosion, Obsidian Shard, Shield of the Phoenix,
    The Cosmic Horror, Rod of Asclepius, Breastplate of Valor, Chandra''s Grace, Midgardian
    Mail, Spear of Desolation, Yogi''s Necklace, Gladiator''s Shield, Leviathan''s
    Hide, Mantle Of Discord, Oni Hunter''s Garb, Ethereal Staff.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.44
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.63
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.48
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.44
      efficiency: 0.29
      win: 0.57
      pick: 0.31
      fit: 0.42
    Spear of the Magus:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.34
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Gluttonous
    Grimoire, Spectral Armor, Erosion, Shield of the Phoenix, Ethereal Staff, Rod
    of Asclepius, Breastplate of Valor, Chandra''s Grace, Midgardian Mail, Gladiator''s
    Shield, Mantle Of Discord, Draconic Scale, Leviathan''s Hide, Freya''s Tears,
    Shroud of Vengeance, Oni Hunter''s Garb, Ancile, Phoenix Feather, Prophetic Cloak,
    Spear of the Magus, Magi''s Cloak, Yogi''s Necklace.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.58
    Genji's Guard:
      total: 0.39
      efficiency: 0.46
      win: 0.38
      pick: 0.22
      fit: 0.32
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.58
    Erosion:
      total: 0.45
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.58
  starter: *id001
---
