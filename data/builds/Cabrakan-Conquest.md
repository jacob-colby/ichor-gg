---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.49
    win_rate: 0.61
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.26
      win_rate: 0.63
    - name: Stampede
      pick_rate: 0.03
      win_rate: 0.71
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.64
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.27
    win_rate: 0.53
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.74
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.59
  - name: Dwarven Plate
    pick_rate: 0.15
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.61
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.8
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.58
    - name: Glorious Pridwen
      pick_rate: 0.06
      win_rate: 0.54
  - name: Medal of Defense
    pick_rate: 0.05
    win_rate: 0.71
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 1.0
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-01'
  god_win_rate: 0.5912408759124088
  god_matches_won: 162
  god_matches_played: 274
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Oni Hunter''s Garb,
    Gluttonous Grimoire, Freya''s Tears, Shield of the Phoenix, Erosion, Blink Rune,
    Spectral Armor, Draconic Scale, Mantle Of Discord, Ethereal Staff, Leviathan''s
    Hide, Hussar''s Wings, Yogi''s Necklace, Midgardian Mail, Soul Gem, Hide of the
    Nemean Lion, Doublet of Binding, Gladiator''s Shield, Ancile, Wish-Granting Pearl,
    Chandra''s Grace, Jade Scepter.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.57
      efficiency: 0.74
      win: 0.53
      pick: 0.27
      fit: 0.4
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.67
      win: 0.58
      pick: 0.19
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.83
    Shifter's Shield:
      total: 0.61
      efficiency: 0.58
      win: 0.61
      pick: 0.49
      fit: 0.73
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.73
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Gluttonous Grimoire, Oni Hunter''s Garb, Soul Gem, Chandra''s Grace, Rod of Asclepius,
    Spectral Armor, Blink Rune, Erosion, Draconic Scale, Phoenix Feather, Ethereal
    Staff, Freya''s Tears, Mantle Of Discord, Leviathan''s Hide, Lifebinder, Yogi''s
    Necklace, Spirit Robe, Hussar''s Wings, Midgardian Mail, Wish-Granting Pearl,
    Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.74
      win: 0.53
      pick: 0.27
      fit: 0.37
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.67
      win: 0.58
      pick: 0.19
      fit: 0.37
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.82
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.94
    Shifter's Shield:
      total: 0.61
      efficiency: 0.58
      win: 0.61
      pick: 0.49
      fit: 0.72
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
  - Blink Rune
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Kinetic Cuirass
  - Blink Rune
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Soul Gem, Blink
    Rune, Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Spectral Armor,
    Void Shield, Shield of the Phoenix, Spear of the Magus, Freya''s Tears, Mantle
    Of Discord, Screeching Gargoyle, Ethereal Staff, Erosion, Void Stone, Draconic
    Scale, The Cosmic Horror, Yogi''s Necklace, Leviathan''s Hide, Spear of Desolation,
    Wish-Granting Pearl, Obsidian Shard.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Genji's Guard:
      total: 0.55
      efficiency: 0.74
      win: 0.53
      pick: 0.27
      fit: 0.27
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.67
      win: 0.58
      pick: 0.19
      fit: 0.27
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.6
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.58
      efficiency: 0.58
      win: 0.61
      pick: 0.49
      fit: 0.5
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Oni
    Hunter''s Garb, Gluttonous Grimoire, Freya''s Tears, Shield of the Phoenix, Erosion,
    Blink Rune, Spectral Armor, Draconic Scale, Mantle Of Discord, Ethereal Staff,
    Leviathan''s Hide, Hussar''s Wings, Yogi''s Necklace, Midgardian Mail, Soul Gem,
    Hide of the Nemean Lion, Doublet of Binding, Gladiator''s Shield, Ancile, Wish-Granting
    Pearl, Chandra''s Grace, Jade Scepter.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.57
      efficiency: 0.74
      win: 0.53
      pick: 0.27
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.83
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.47
    Shifter's Shield:
      total: 0.61
      efficiency: 0.58
      win: 0.61
      pick: 0.49
      fit: 0.73
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
---
