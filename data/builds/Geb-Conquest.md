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
  - Amanita Charm
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Eye of Providence, Shifter''s
    Shield, Oni Hunter''s Garb, Erosion, Draconic Scale, Shield of the Phoenix, Spectral
    Armor, Mantle Of Discord, Blink Rune, Gluttonous Grimoire, Hussar''s Wings, Leviathan''s
    Hide, Midgardian Mail, Hide of the Nemean Lion, Ethereal Staff, Gladiator''s Shield,
    Doublet of Binding, Yogi''s Necklace, Ancile, Shroud of Vengeance, Stone of Binding,
    Chandra''s Grace, Stampede.'
  slot_scores:
    Eye of Providence:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.85
    Genji's Guard:
      total: 0.63
      efficiency: 0.74
      win: 0.65
      pick: 0.3
      fit: 0.45
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.67
      win: 0.69
      pick: 0.19
      fit: 0.45
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.66
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.76
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
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
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix,
    Eye of Providence, Oni Hunter''s Garb, Chandra''s Grace, Shifter''s Shield, Erosion,
    Spectral Armor, Draconic Scale, Gluttonous Grimoire, Rod of Asclepius, Phoenix
    Feather, Blink Rune, Soul Gem, Mantle Of Discord, Leviathan''s Hide, Hussar''s
    Wings, Ethereal Staff, Yogi''s Necklace, Spirit Robe, Midgardian Mail, Hide of
    the Nemean Lion, Gladiator''s Shield, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.74
      win: 0.65
      pick: 0.3
      fit: 0.42
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.67
      win: 0.69
      pick: 0.19
      fit: 0.42
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.94
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 1.0
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
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
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Eye of Providence, Blink Rune, Soul Gem, Oni Hunter''s Garb, Stone of Binding,
    Spectral Armor, Void Shield, Shifter''s Shield, Shield of the Phoenix, Mantle
    Of Discord, Screeching Gargoyle, Erosion, Spear of the Magus, Void Stone, Draconic
    Scale, Ethereal Staff, Yogi''s Necklace, Leviathan''s Hide, The Cosmic Horror,
    Midgardian Mail, Spear of Desolation, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.61
      efficiency: 0.74
      win: 0.65
      pick: 0.3
      fit: 0.28
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.67
      win: 0.69
      pick: 0.19
      fit: 0.28
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.3
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.33
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.31
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Death Metal:
      total: 0.32
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.33
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.31
      efficiency: 0.45
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
  - Oni Hunter's Garb
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Shifter''s
    Shield, Oni Hunter''s Garb, Erosion, Freya''s Tears, Draconic Scale, Shield of
    the Phoenix, Spectral Armor, Mantle Of Discord, Blink Rune, Gluttonous Grimoire,
    Hussar''s Wings, Leviathan''s Hide, Midgardian Mail, Hide of the Nemean Lion,
    Ethereal Staff, Gladiator''s Shield, Doublet of Binding, Yogi''s Necklace, Ancile,
    Shroud of Vengeance, Stone of Binding, Chandra''s Grace, Stampede.'
  slot_scores:
    Eye of Providence:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.85
    Genji's Guard:
      total: 0.63
      efficiency: 0.74
      win: 0.65
      pick: 0.3
      fit: 0.45
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.95
    Oni Hunter's Garb:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
---
