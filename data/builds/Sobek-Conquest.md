---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.17
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.26
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.23
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.52
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.48
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.56
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.22
      win_rate: 0.48
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.59
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.42
    - name: Dwarven Plate
      pick_rate: 0.1
      win_rate: 0.51
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.48
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.61
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 0.55
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.62
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.6
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-08-01'
  god_win_rate: 0.535796766743649
  god_matches_won: 232
  god_matches_played: 433
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
  - Oni Hunter's Garb
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Breastplate of Valor,
    Gluttonous Grimoire, Oni Hunter''s Garb, Shifter''s Shield, Freya''s Tears, Shield
    of the Phoenix, Erosion, Spectral Armor, Draconic Scale, Mantle Of Discord, Hide
    of the Nemean Lion, Ethereal Staff, Leviathan''s Hide, Hussar''s Wings, Soul Gem,
    Yogi''s Necklace, Midgardian Mail, Wish-Granting Pearl, Doublet of Binding, Jade
    Scepter, Gladiator''s Shield, Rod of Asclepius, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.6
      efficiency: 0.74
      win: 0.6
      pick: 0.21
      fit: 0.39
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.67
      win: 0.57
      pick: 0.1
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
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
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
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Rod of Asclepius, Oni Hunter''s
    Garb, Chandra''s Grace, Shifter''s Shield, Spectral Armor, Erosion, Ethereal Staff,
    Draconic Scale, Phoenix Feather, Freya''s Tears, Lifebinder, Mantle Of Discord,
    Yogi''s Necklace, Leviathan''s Hide, Bancroft''s Talon, Blood-Bound Book, Wish-Granting
    Pearl, Spirit Robe, Jade Scepter.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.59
      efficiency: 0.74
      win: 0.6
      pick: 0.21
      fit: 0.36
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.36
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
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  flex_slots:
  - Eye of Providence
  - Oni Hunter's Garb
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
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Breastplate of Valor, Amanita
    Charm, Soul Gem, Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Spectral
    Armor, Void Shield, Spear of the Magus, Shield of the Phoenix, Shifter''s Shield,
    Ethereal Staff, Freya''s Tears, Mantle Of Discord, Screeching Gargoyle, Erosion,
    Void Stone, The Cosmic Horror, Draconic Scale, Yogi''s Necklace, Spear of Desolation,
    Leviathan''s Hide, Wish-Granting Pearl, Obsidian Shard.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.58
      efficiency: 0.74
      win: 0.6
      pick: 0.21
      fit: 0.27
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.27
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
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Breastplate of Valor, Kinetic Cuirass, Amanita
    Charm, Oni Hunter''s Garb, Eye of Providence, Ethereal Staff, Spectral Armor,
    Soul Gem, Shield of the Phoenix, Mantle Of Discord, Yogi''s Necklace, Freya''s
    Tears, Shifter''s Shield, Bracer of The Abyss, Bragi''s Harp, Erosion, Death Metal,
    Draconic Scale, Wish-Granting Pearl, Leviathan''s Hide, Jade Scepter, Rod of Asclepius,
    Nimble Ring, Midgardian Mail, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.74
      win: 0.6
      pick: 0.21
      fit: 0.2
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.2
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Freya's Tears
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Kinetic Cuirass,
    Shield of the Phoenix, Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Soul
    Gem, Eye of Providence, Oni Hunter''s Garb, Ethereal Staff, Chandra''s Grace,
    Spectral Armor, Shifter''s Shield, Chronos'' Pendant, Mantle Of Discord, Gladiator''s
    Shield, Erosion, Yogi''s Necklace, Screeching Gargoyle, Draconic Scale, Wish-Granting
    Pearl, Jade Scepter, Death Metal, Leviathan''s Hide, Rod of Asclepius, Gem of
    Focus.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.61
      efficiency: 0.74
      win: 0.6
      pick: 0.21
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
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
    Grimoire, Oni Hunter''s Garb, Shifter''s Shield, Freya''s Tears, Shield of the
    Phoenix, Erosion, Spectral Armor, Draconic Scale, Mantle Of Discord, Breastplate
    of Valor, Ethereal Staff, Leviathan''s Hide, Hussar''s Wings, Soul Gem, Yogi''s
    Necklace, Midgardian Mail, Hide of the Nemean Lion, Wish-Granting Pearl, Doublet
    of Binding, Jade Scepter, Gladiator''s Shield, Rod of Asclepius, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.6
      efficiency: 0.74
      win: 0.6
      pick: 0.21
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
      total: 0.53
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Dwarven Plate
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Dwarven Plate
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye
    of Providence, Gluttonous Grimoire, Oni Hunter''s Garb, Shifter''s Shield, Freya''s
    Tears, Shield of the Phoenix, Erosion, Spectral Armor, Draconic Scale, Mantle
    Of Discord, Breastplate of Valor, Ethereal Staff, Leviathan''s Hide, Hussar''s
    Wings, Soul Gem, Yogi''s Necklace, Midgardian Mail, Hide of the Nemean Lion, Wish-Granting
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
      total: 0.6
      efficiency: 0.74
      win: 0.6
      pick: 0.21
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
    Dwarven Plate:
      total: 0.53
      efficiency: 0.36
      win: 0.71
      pick: 0.08
      fit: 0.51
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.71
  swaps:
  - added: Dwarven Plate
    removed: Shifter's Shield
    reason: community 71% win over 35 matches (vs 54% on this god), taking the model's
      weakest slot from Shifter's Shield
  starter: *id001
---
