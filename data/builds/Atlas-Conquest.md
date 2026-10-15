---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.53
  slot_order:
  - name: Stampede
    pick_rate: 0.29
    win_rate: 0.52
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.15
      win_rate: 0.5
    - name: Yogi's Necklace
      pick_rate: 0.06
      win_rate: 0.3
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.51
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.54
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.75
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.45
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.48
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.54
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.62
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.5
  - name: Contagion
    pick_rate: 0.05
    win_rate: 0.36
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.55
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.57
  - name: Sage's Ring
    pick_rate: 0.07
    win_rate: 0.91
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.8
    - name: Contagion
      pick_rate: 0.04
      win_rate: 0.86
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.21
    win_rate: 0.43
  - name: Bumba's Hammer
    pick_rate: 0.18
    win_rate: 0.63
  - name: Bluestone Brooch
    pick_rate: 0.13
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-10-15'
  god_win_rate: 0.5153203342618384
  god_matches_won: 185
  god_matches_played: 359
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-15'
  god_matches_analyzed: 9899
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Rod of Tahuti, Kinetic Cuirass,
    Shifter''s Shield, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the
    Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.51
      pick: 0.25
      fit: 0.39
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.1
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.2
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
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
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Rod of Tahuti,
    Kinetic Cuirass, Rod of Asclepius, Shifter''s Shield, Soul Gem, Erosion, Eye of
    Providence, Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather,
    Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.51
      pick: 0.25
      fit: 0.36
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.1
      fit: 0.36
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.2
      fit: 0.57
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Breastplate of Valor, Rod of Tahuti, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Spear of the Magus, Soul Gem, Void Shield, Obsidian Shard, Shifter''s Shield,
    Void Stone, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Doom Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.51
      pick: 0.25
      fit: 0.27
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.1
      fit: 0.27
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.2
      fit: 0.44
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic
    Cuirass, Gluttonous Grimoire, Shifter''s Shield, Soul Gem, Helm of Radiance, Erosion,
    Stone of Binding, Eye of Providence, Shield of the Phoenix, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the Magus, Spear of Desolation,
    Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of
    The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.25
      fit: 0.2
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.75
      pick: 0.1
      fit: 0.2
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Rod of Tahuti,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion,
    Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius,
    Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.51
      pick: 0.25
      fit: 0.48
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.65
      win: 0.75
      pick: 0.1
      fit: 0.48
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.2
      fit: 0.64
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak,
    Hide of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.51
      pick: 0.25
      fit: 0.39
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.1
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.2
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
---
