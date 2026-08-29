---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.56
  slot_order:
  - name: Stampede
    pick_rate: 0.26
    win_rate: 0.47
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.42
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.25
  - name: Genji's Guard
    pick_rate: 0.25
    win_rate: 0.48
    alternates:
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.35
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.41
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.42
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.32
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.62
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.35
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.55
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.38
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.4
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
  - name: Veve Charm
    pick_rate: 0.05
    win_rate: 0.83
    alternates:
    - name: Ancile
      pick_rate: 0.04
      win_rate: 0.4
    - name: Engraved Guard
      pick_rate: 0.04
      win_rate: 0.4
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.33
  - name: Bumba's Cudgel
    pick_rate: 0.16
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-08-29'
  god_win_rate: 0.47641509433962265
  god_matches_won: 101
  god_matches_played: 212
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-29'
  god_matches_analyzed: 4291
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
    of Valor, Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion,
    Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb,
    Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.34
      fit: 0.39
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.41
      pick: 0.11
      fit: 0.39
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.41
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.42
      pick: 0.15
      fit: 0.71
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.41
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
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
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Shifter''s Shield, Rod of Asclepius, Soul Gem, Breastplate of Valor, Erosion,
    Eye of Providence, Gluttonous Grimoire, Phoenix Feather, Draconic Scale, Yogi''s
    Necklace, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone
    of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void
    Shield, Magi''s Cloak, Ancile, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.34
      fit: 0.36
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.41
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.53
      win: 0.41
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.62
      pick: 0.18
      fit: 0.57
    Shifter's Shield:
      total: 0.49
      efficiency: 0.55
      win: 0.42
      pick: 0.15
      fit: 0.7
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.41
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Shifter''s Shield,
    Spear of the Magus, Breastplate of Valor, Soul Gem, Void Shield, Obsidian Shard,
    Void Stone, Erosion, Eye of Providence, Shield of the Phoenix, Doom Orb, Helm
    of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Draconic Scale,
    Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.47
      efficiency: 0.51
      win: 0.41
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.48
      efficiency: 0.51
      win: 0.41
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.48
      pick: 0.34
      fit: 0.27
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.41
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.18
      fit: 0.44
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.41
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
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
    Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Draconic
    Scale, Bracer of The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.34
      fit: 0.2
    Bracer of The Abyss:
      total: 0.41
      efficiency: 0.52
      win: 0.41
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.46
      efficiency: 0.65
      win: 0.41
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.41
      efficiency: 0.44
      win: 0.41
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.62
      pick: 0.18
      fit: 0.33
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.41
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
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Shifter''s Shield, Spear
    of Desolation, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Prophetic Cloak,
    Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Draconic
    Scale, Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen,
    Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.48
      pick: 0.34
      fit: 0.48
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.41
      pick: 0.11
      fit: 0.48
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.41
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.42
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.41
      pick: 0.0
      fit: 0.45
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
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.34
      fit: 0.39
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.41
      pick: 0.11
      fit: 0.39
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.41
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.42
      pick: 0.15
      fit: 0.71
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.41
      pick: 0.0
      fit: 0.71
  starter: *id001
---
