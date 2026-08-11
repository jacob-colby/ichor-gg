---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.21
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.26
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.25
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.51
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.52
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.49
    alternates:
    - name: Genji's Guard
      pick_rate: 0.24
      win_rate: 0.55
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.54
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.51
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.56
  - name: Dwarven Plate
    pick_rate: 0.07
    win_rate: 0.69
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.58
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.54
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.54
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.51
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.51
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.36
    win_rate: 0.49
  - name: Bluestone Brooch
    pick_rate: 0.26
    win_rate: 0.58
  - name: Selflessness
    pick_rate: 0.11
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-08-11'
  god_win_rate: 0.5259570005243839
  god_matches_won: 1003
  god_matches_played: 1907
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Freya''s Tears, Gluttonous
    Grimoire, Oni Hunter''s Garb, Erosion, Shield of the Phoenix, Stampede, Breastplate
    of Valor, Draconic Scale, Hide of the Nemean Lion, Spectral Armor, Soul Gem, Leviathan''s
    Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail, Yogi''s Necklace,
    Helm of Radiance, Rod of Asclepius, Magi''s Cloak, Ancile, Gladiator''s Shield,
    Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.54
      pick: 0.25
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
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
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Chandra''s
    Grace, Stampede, Freya''s Tears, Erosion, Breastplate of Valor, Draconic Scale,
    Hide of the Nemean Lion, Phoenix Feather, Spectral Armor, Lifebinder, Yogi''s
    Necklace, Leviathan''s Hide, Blood-Bound Book, Midgardian Mail, Bancroft''s Talon,
    Glorious Pridwen, Jade Scepter.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.92
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.54
      pick: 0.25
      fit: 0.7
    Amanita Charm:
      total: 0.61
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Eye of Providence
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass, Soul Gem, Eye
    of Providence, Stone of Binding, Oni Hunter''s Garb, Spear of the Magus, Freya''s
    Tears, Screeching Gargoyle, Breastplate of Valor, Void Shield, The Cosmic Horror,
    Shield of the Phoenix, Void Stone, Spear of Desolation, Erosion, Spectral Armor,
    Draconic Scale, Obsidian Shard, Yogi''s Necklace, Leviathan''s Hide, Helm of Radiance,
    Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Eye of Providence:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.54
      pick: 0.25
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence,
    Oni Hunter''s Garb, Breastplate of Valor, Freya''s Tears, Soul Gem, Shield of
    the Phoenix, Hide of the Nemean Lion, Spectral Armor, Yogi''s Necklace, Erosion,
    Bracer of The Abyss, Death Metal, Draconic Scale, Rod of Asclepius, Helm of Radiance,
    Leviathan''s Hide, Bragi''s Harp, Midgardian Mail, Spear of the Magus, Jade Scepter,
    Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.2
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Gluttonous Grimoire,
    Eye of Providence, Oni Hunter''s Garb, Chronos'' Pendant, Screeching Gargoyle,
    Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Spectral Armor, Erosion,
    Yogi''s Necklace, Prophetic Cloak, Draconic Scale, Helm of Radiance, Rod of Asclepius,
    Gem of Focus, Death Metal, Leviathan''s Hide, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.49
      pick: 0.1
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.54
      pick: 0.25
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Freya''s
    Tears, Gluttonous Grimoire, Oni Hunter''s Garb, Erosion, Shield of the Phoenix,
    Breastplate of Valor, Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s Hide,
    Mantle Of Discord, Stone of Binding, Midgardian Mail, Yogi''s Necklace, Hide of
    the Nemean Lion, Helm of Radiance, Rod of Asclepius, Magi''s Cloak, Stampede,
    Ancile, Gladiator''s Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.54
      pick: 0.25
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
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
  - Freya's Tears
  - Dwarven Plate
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Dwarven Plate
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye
    of Providence, Freya''s Tears, Gluttonous Grimoire, Oni Hunter''s Garb, Erosion,
    Shield of the Phoenix, Breastplate of Valor, Draconic Scale, Spectral Armor, Soul
    Gem, Leviathan''s Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail,
    Yogi''s Necklace, Hide of the Nemean Lion, Helm of Radiance, Rod of Asclepius,
    Magi''s Cloak, Stampede, Ancile, Gladiator''s Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Dwarven Plate:
      total: 0.51
      efficiency: 0.35
      win: 0.69
      pick: 0.07
      fit: 0.51
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.71
  swaps:
  - added: Dwarven Plate
    removed: Shifter's Shield
    reason: community 69% win over 133 matches (vs 53% on this god), taking the model's
      weakest slot from Shifter's Shield
  starter: *id001
---
