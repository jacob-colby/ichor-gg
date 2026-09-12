---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.43
  slot_order:
  - name: Stampede
    pick_rate: 0.28
    win_rate: 0.62
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.21
      win_rate: 0.53
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.52
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.56
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.62
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.53
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.49
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.44
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.63
  - name: Dwarven Plate
    pick_rate: 0.06
    win_rate: 0.53
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.71
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.63
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.46
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.64
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.35
    win_rate: 0.46
  - name: Bluestone Brooch
    pick_rate: 0.25
    win_rate: 0.63
  - name: Selflessness
    pick_rate: 0.14
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-09-12'
  god_win_rate: 0.5368421052631579
  god_matches_won: 204
  god_matches_played: 380
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-12'
  god_matches_analyzed: 4284
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
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
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Breastplate
    of Valor, Erosion, Eye of Providence, Prophetic Cloak, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion, Helm
    of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban
    Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.57
      pick: 0.23
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.58
      pick: 0.09
      fit: 0.71
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.64
      pick: 0.15
      fit: 0.71
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Freya's Tears
  - Shifter's Shield
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
  - Freya's Tears
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Shifter''s Shield, Rod of Asclepius, Soul Gem, Erosion, Eye of Providence, Breastplate
    of Valor, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace,
    Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.23
      fit: 0.57
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.09
      fit: 0.7
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.64
      pick: 0.15
      fit: 0.7
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Shifter''s Shield,
    Spear of the Magus, Soul Gem, Void Shield, Breastplate of Valor, Obsidian Shard,
    Void Stone, Erosion, Eye of Providence, Shield of the Phoenix, Doom Orb, Helm
    of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle Of Discord,
    Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.23
      fit: 0.44
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.64
      pick: 0.15
      fit: 0.49
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.57
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
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of Radiance,
    Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix, Magi''s Cloak,
    Screeching Gargoyle, Daybreak Gavel, Spear of the Magus, Spear of Desolation,
    Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of
    The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.23
      fit: 0.33
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.64
      pick: 0.15
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
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
  - Prophetic Cloak
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Prophetic Cloak, Kinetic Cuirass, Shield of the Phoenix, Shifter''s
    Shield, Spear of Desolation, Screeching Gargoyle, Soul Gem, Chronos'' Pendant,
    Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of
    Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail,
    Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.52
      pick: 0.3
      fit: 0.48
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.44
      win: 0.62
      pick: 0.14
      fit: 0.64
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.57
      pick: 0.23
      fit: 0.64
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.64
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
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
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the
    Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.52
      pick: 0.3
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.57
      pick: 0.23
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.58
      pick: 0.09
      fit: 0.71
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
