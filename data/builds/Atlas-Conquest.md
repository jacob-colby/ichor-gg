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
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Oni Hunter's Garb
  - Erosion
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
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Eye of Providence, Gluttonous
    Grimoire, Oni Hunter''s Garb, Shield of the Phoenix, Erosion, Spectral Armor,
    Draconic Scale, Mantle Of Discord, Breastplate of Valor, Ethereal Staff, Shifter''s
    Shield, Leviathan''s Hide, Genji''s Guard, Hussar''s Wings, Soul Gem, Yogi''s
    Necklace, Midgardian Mail, Hide of the Nemean Lion, Wish-Granting Pearl, Doublet
    of Binding, Jade Scepter, Gladiator''s Shield, Rod of Asclepius, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.81
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.62
      pick: 0.06
      fit: 0.64
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.53
      efficiency: 0.56
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
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Oni Hunter's Garb
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Freya''s Tears, Kinetic Cuirass,
    Eye of Providence, Gluttonous Grimoire, Soul Gem, Rod of Asclepius, Oni Hunter''s
    Garb, Chandra''s Grace, Spectral Armor, Erosion, Ethereal Staff, Draconic Scale,
    Phoenix Feather, Breastplate of Valor, Lifebinder, Mantle Of Discord, Yogi''s
    Necklace, Leviathan''s Hide, Shifter''s Shield, Bancroft''s Talon, Blood-Bound
    Book, Wish-Granting Pearl, Spirit Robe, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.7
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.92
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.06
      fit: 0.57
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
  - Stone of Binding
  - Eye of Providence
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Oni Hunter's Garb
  - Stone of Binding
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
    for this god: Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Spectral Armor,
    Void Shield, Spear of the Magus, Shield of the Phoenix, Ethereal Staff, Breastplate
    of Valor, Mantle Of Discord, Screeching Gargoyle, Erosion, Void Stone, The Cosmic
    Horror, Draconic Scale, Yogi''s Necklace, Genji''s Guard, Spear of Desolation,
    Leviathan''s Hide, Wish-Granting Pearl, Obsidian Shard, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Eye of Providence:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.59
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.32
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.62
      pick: 0.06
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.66
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
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Gluttonous
    Grimoire, Genji''s Guard, Oni Hunter''s Garb, Shifter''s Shield, Freya''s Tears,
    Shield of the Phoenix, Erosion, Spectral Armor, Draconic Scale, Mantle Of Discord,
    Breastplate of Valor, Ethereal Staff, Leviathan''s Hide, Hussar''s Wings, Soul
    Gem, Yogi''s Necklace, Midgardian Mail, Hide of the Nemean Lion, Wish-Granting
    Pearl, Doublet of Binding, Jade Scepter, Gladiator''s Shield, Rod of Asclepius,
    Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.5
      efficiency: 0.74
      win: 0.4
      pick: 0.15
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.81
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.46
    Shifter's Shield:
      total: 0.51
      efficiency: 0.58
      win: 0.43
      pick: 0.15
      fit: 0.71
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
---
