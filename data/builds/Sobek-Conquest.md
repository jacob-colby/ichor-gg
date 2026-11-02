---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.48
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.45
    win_rate: 0.58
    alternates:
    - name: Stampede
      pick_rate: 0.26
      win_rate: 0.65
    - name: Yogi's Necklace
      pick_rate: 0.05
      win_rate: 0.47
  - name: Stampede
    pick_rate: 0.29
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.61
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 0.52
  - name: Shell of Rebuke
    pick_rate: 0.22
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.52
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.59
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.61
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.62
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.55
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.66
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.66
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.51
  - name: Medal of Defense
    pick_rate: 0.09
    win_rate: 0.59
    alternates:
    - name: Sage's Ring
      pick_rate: 0.07
      win_rate: 0.69
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.65
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.36
    win_rate: 0.51
  - name: Bluestone Brooch
    pick_rate: 0.3
    win_rate: 0.64
  - name: Selflessness
    pick_rate: 0.13
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-10-30'
  god_win_rate: 0.5716312056737589
  god_matches_won: 403
  god_matches_played: 705
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Draconic Scale, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Erosion, Eye of Providence, Breastplate of Valor, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Gluttonous Grimoire, Helm of Radiance, Mantle
    Of Discord, Midgardian Mail, Oni Hunter''s Garb, Prophetic Cloak, Screeching Gargoyle,
    Leviathan''s Hide, Hide of the Nemean Lion, Helm of Darkness, Void Shield, Ancile,
    Spear of Desolation, Hussar''s Wings, Spectral Armor.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.81
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.71
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.61
      pick: 0.35
      fit: 0.64
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.66
      pick: 0.13
      fit: 0.71
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Draconic Scale,
    Kinetic Cuirass, Rod of Asclepius, Shifter''s Shield, Soul Gem, Erosion, Eye of
    Providence, Breastplate of Valor, Ethereal Staff, Gluttonous Grimoire, Phoenix
    Feather, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Oni
    Hunter''s Garb, Stone of Binding, Helm of Radiance, Leviathan''s Hide, Hide of
    the Nemean Lion, Void Shield, Ancile, Magi''s Cloak, Yogi''s Necklace.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.61
      pick: 0.35
      fit: 0.57
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.7
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.66
      pick: 0.13
      fit: 0.7
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Draconic Scale,
    Stone of Binding, Kinetic Cuirass, Spear of Desolation, Screeching Gargoyle, Spear
    of the Magus, Void Shield, Soul Gem, Obsidian Shard, Void Stone, Breastplate of
    Valor, Shifter''s Shield, Erosion, Eye of Providence, Shield of the Phoenix, Doom
    Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Oni Hunter''s Garb, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.35
      fit: 0.44
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.66
      pick: 0.13
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.85
      win: 0.58
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Draconic Scale, Kinetic Cuirass,
    Gluttonous Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of
    Radiance, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Spear of the Magus, Spear of Desolation, Daybreak Gavel, Bragi''s
    Harp, Midgardian Mail, Rod of Asclepius, Screeching Gargoyle, Oni Hunter''s Garb,
    Mantle Of Discord, Bracer of The Abyss, Lotus Sickle, Obsidian Shard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.58
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.35
      fit: 0.33
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.66
      pick: 0.13
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Draconic Scale, Kinetic Cuirass, Shield of the Phoenix, Spear of
    Desolation, Soul Gem, Lotus Sickle, Screeching Gargoyle, Shifter''s Shield, Chronos''
    Pendant, Prophetic Cloak, Helm of Radiance, Erosion, Gluttonous Grimoire, Eye
    of Providence, Gladiator''s Shield, Stone of Binding, Gem of Focus, Magi''s Cloak,
    Spear of the Magus, Rod of Asclepius, Eye of Erebus, Midgardian Mail, Mantle Of
    Discord, Oni Hunter''s Garb.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.52
      pick: 0.23
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.61
      pick: 0.35
      fit: 0.64
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.66
      pick: 0.13
      fit: 0.45
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Genji's Guard
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Erosion, Eye of Providence, Breastplate of Valor, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Gluttonous Grimoire, Helm of
    Radiance, Mantle Of Discord, Midgardian Mail, Oni Hunter''s Garb, Prophetic Cloak,
    Screeching Gargoyle, Leviathan''s Hide, Hide of the Nemean Lion, Helm of Darkness,
    Void Shield, Ancile, Spear of Desolation, Hussar''s Wings, Spectral Armor.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.81
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.52
      pick: 0.23
      fit: 0.39
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.61
      pick: 0.35
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
