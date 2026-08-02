---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.42
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.15
    win_rate: 0.43
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.11
      win_rate: 0.32
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.3
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.4
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.48
    - name: The Cosmic Horror
      pick_rate: 0.09
      win_rate: 0.43
  - name: The World Stone
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.41
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.44
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.62
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.62
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.42
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.33
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.33
  - name: Veve Charm
    pick_rate: 0.04
    win_rate: 0.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.4
    - name: Rod of Tahuti
      pick_rate: 0.04
      win_rate: 0.4
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-08-01'
  god_win_rate: 0.41810344827586204
  god_matches_won: 97
  god_matches_played: 232
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
  - Freya's Tears
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
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Erosion, Spectral Armor, Shield of the Phoenix, Gladiator''s Shield,
    Ethereal Staff, Draconic Scale, Rod of Asclepius, Breastplate of Valor, Midgardian
    Mail, Chandra''s Grace, Mantle Of Discord, Prophetic Cloak, Shroud of Vengeance,
    Leviathan''s Hide, Oni Hunter''s Garb, Ancile, Phoenix Feather, Magi''s Cloak,
    Screeching Gargoyle, Helm of Radiance, Shifter''s Shield, Genji''s Guard.'
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
    Freya's Tears:
      total: 0.49
      efficiency: 0.31
      win: 0.62
      pick: 0.06
      fit: 0.64
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
  - Freya's Tears
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
    Armor, Erosion, Lifebinder, Soul Gem, Blood-Bound Book, Spirit Robe, Ethereal
    Staff, Gladiator''s Shield, Bancroft''s Talon, Midgardian Mail, Glorious Pridwen,
    Draconic Scale, Leviathan''s Hide, Oni Hunter''s Garb, Ancile, Breastplate of
    Valor, Yogi''s Necklace, Shifter''s Shield, Genji''s Guard.'
  slot_scores:
    Eye of Providence:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.7
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.48
      efficiency: 0.31
      win: 0.62
      pick: 0.06
      fit: 0.57
    Spectral Armor:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of the Magus
  - Spectral Armor
  flex_slots:
  - Spear of the Magus
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Amanita
    Charm, Spear of the Magus, Spectral Armor, Soul Gem, Screeching Gargoyle, Stone
    of Binding, Void Stone, Erosion, Void Shield, Obsidian Shard, The Cosmic Horror,
    Shield of the Phoenix, Ethereal Staff, Rod of Asclepius, Spear of Desolation,
    Breastplate of Valor, Chandra''s Grace, Midgardian Mail, Gladiator''s Shield,
    Mantle Of Discord, Leviathan''s Hide, Oni Hunter''s Garb, Yogi''s Necklace, Genji''s
    Guard.'
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
    Freya's Tears:
      total: 0.46
      efficiency: 0.31
      win: 0.62
      pick: 0.06
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.45
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spectral Armor:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.32
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
  - Spectral Armor
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Gluttonous
    Grimoire, Erosion, Spectral Armor, Shield of the Phoenix, Genji''s Guard, Shifter''s
    Shield, Gladiator''s Shield, Ethereal Staff, Draconic Scale, Rod of Asclepius,
    Breastplate of Valor, Midgardian Mail, Freya''s Tears, Chandra''s Grace, Mantle
    Of Discord, Prophetic Cloak, Shroud of Vengeance, Leviathan''s Hide, Oni Hunter''s
    Garb, Ancile, Phoenix Feather, Magi''s Cloak, Screeching Gargoyle, Helm of Radiance.'
  slot_scores:
    Eye of Providence:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.41
      efficiency: 0.46
      win: 0.4
      pick: 0.15
      fit: 0.39
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.81
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
  starter: *id001
---
