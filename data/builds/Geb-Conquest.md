---
type: smite-build
god: Geb
mode: Conquest
builds:
- source: community
  aspect: Aspect of Calamity
  aspect_pick_rate: 0.01
  aspect_win_rate: 1.0
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.69
    - name: Chronos' Pendant
      pick_rate: 0.16
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.3
    win_rate: 0.65
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.18
      win_rate: 0.61
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.33
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.22
      win_rate: 0.59
    - name: Ragnarok's Wake
      pick_rate: 0.09
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.74
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.59
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
  - name: Glorious Pridwen
    pick_rate: 0.08
    win_rate: 0.58
    alternates:
    - name: Spirit Robe
      pick_rate: 0.08
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.45
  - name: Engraved Guard
    pick_rate: 0.12
    win_rate: 0.7
    alternates:
    - name: Olmec Blue
      pick_rate: 0.07
      win_rate: 0.33
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 1.0
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-08-01'
  god_win_rate: 0.5755813953488372
  god_matches_won: 99
  god_matches_played: 172
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
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Amanita Charm
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
    this god: Freya''s Tears, Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion,
    Spectral Armor, Shield of the Phoenix, Shifter''s Shield, Draconic Scale, Gladiator''s
    Shield, Midgardian Mail, Prophetic Cloak, Mantle Of Discord, Shroud of Vengeance,
    Leviathan''s Hide, Ancile, Oni Hunter''s Garb, Phoenix Feather, Magi''s Cloak,
    Chandra''s Grace, Gluttonous Grimoire, Stone of Binding, Void Stone, Stampede,
    Spirit Robe.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.85
    Genji's Guard:
      total: 0.53
      efficiency: 0.44
      win: 0.65
      pick: 0.3
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.4
      win: 0.69
      pick: 0.19
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.56
      efficiency: 0.3
      win: 0.74
      pick: 0.14
      fit: 0.76
    Amanita Charm:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Chandra''s Grace, Glorious Pridwen, Rod of Asclepius, Phoenix Feather, Spectral
    Armor, Erosion, Soul Gem, Spirit Robe, Lifebinder, Blood-Bound Book, Gluttonous
    Grimoire, Gladiator''s Shield, Midgardian Mail, Shifter''s Shield, Bancroft''s
    Talon, Draconic Scale, Ethereal Staff, Leviathan''s Hide, Ancile, Oni Hunter''s
    Garb, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.44
      win: 0.65
      pick: 0.3
      fit: 0.33
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.4
      win: 0.69
      pick: 0.19
      fit: 0.33
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.84
    Freya's Tears:
      total: 0.52
      efficiency: 0.3
      win: 0.74
      pick: 0.14
      fit: 0.54
    Amanita Charm:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
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
    Charm, Soul Gem, Spectral Armor, The Cosmic Horror, Spear of Desolation, Screeching
    Gargoyle, Erosion, Void Stone, Stone of Binding, Void Shield, Spear of the Magus,
    Shield of the Phoenix, Doom Orb, Midgardian Mail, The World Stone, Chandra''s
    Grace, Ethereal Staff, Gladiator''s Shield, Rod of Asclepius, Leviathan''s Hide,
    Mantle Of Discord, Shifter''s Shield.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.5
      efficiency: 0.44
      win: 0.65
      pick: 0.3
      fit: 0.28
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.4
      win: 0.69
      pick: 0.19
      fit: 0.28
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.51
      efficiency: 0.3
      win: 0.74
      pick: 0.14
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.63
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
      total: 0.23
      efficiency: 0.55
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
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.23
      efficiency: 0.37
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
  - Kinetic Cuirass
  - Shifter's Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Shifter's Shield
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion,
    Spectral Armor, Shield of the Phoenix, Shifter''s Shield, Draconic Scale, Gladiator''s
    Shield, Midgardian Mail, Freya''s Tears, Prophetic Cloak, Mantle Of Discord, Shroud
    of Vengeance, Leviathan''s Hide, Ancile, Oni Hunter''s Garb, Phoenix Feather,
    Magi''s Cloak, Chandra''s Grace, Gluttonous Grimoire, Stone of Binding, Void Stone,
    Stampede, Spirit Robe.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.85
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.95
    Shifter's Shield:
      total: 0.45
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spectral Armor:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.49
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
---
