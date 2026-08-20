---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.19
    win_rate: 0.56
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.53
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.6
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 0.71
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.57
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.62
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.59
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.62
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.63
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.58
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.59
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.69
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.54
    - name: Olmec Blue
      pick_rate: 0.04
      win_rate: 0.73
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.61
  - name: Bumba's Hammer
    pick_rate: 0.09
    win_rate: 0.66
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-08-20'
  god_win_rate: 0.5625
  god_matches_won: 261
  god_matches_played: 464
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-20'
  god_matches_analyzed: 11556
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Prophetic Cloak, Gluttonous
    Grimoire, Erosion, Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb,
    Draconic Scale, Breastplate of Valor, Spectral Armor, Leviathan''s Hide, Mantle
    Of Discord, Midgardian Mail, Soul Gem, Stone of Binding, Nimble Ring, Magi''s
    Cloak, Gladiator''s Shield, Ancile, Helm of Radiance, Screeching Gargoyle, Hide
    of the Nemean Lion, Void Shield, Doublet of Binding.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.59
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.81
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.43
      win: 0.71
      pick: 0.1
      fit: 0.64
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.63
      pick: 0.19
      fit: 0.64
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Tahuti,
    Soul Gem, Gluttonous Grimoire, Ethereal Staff, Chandra''s Grace, Rod of Asclepius,
    Oni Hunter''s Garb, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale,
    Phoenix Feather, Spectral Armor, Breastplate of Valor, Leviathan''s Hide, Midgardian
    Mail, Lifebinder, Glorious Pridwen, Nimble Ring, Gladiator''s Shield, Ancile,
    Blood-Bound Book, Hide of the Nemean Lion.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.8
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.43
      win: 0.71
      pick: 0.1
      fit: 0.57
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.92
    Oni Hunter's Garb:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.63
      pick: 0.19
      fit: 0.57
    Amanita Charm:
      total: 0.64
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Stone of Binding, Screeching Gargoyle, Void Shield, The Cosmic Horror,
    Spear of the Magus, Oni Hunter''s Garb, Breastplate of Valor, Void Stone, Shield
    of the Phoenix, Spear of Desolation, Obsidian Shard, Erosion, Eye of Providence,
    Spectral Armor, Nimble Ring, Draconic Scale, Leviathan''s Hide, Midgardian Mail,
    Mantle Of Discord, Helm of Radiance, Magi''s Cloak.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.47
      win: 0.59
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.59
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.43
      win: 0.71
      pick: 0.1
      fit: 0.44
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.63
      pick: 0.19
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.62
      pick: 0.13
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Kinetic Cuirass, Amanita Charm, Gluttonous
    Grimoire, Breastplate of Valor, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix,
    Spectral Armor, Erosion, Eye of Providence, Draconic Scale, Leviathan''s Hide,
    Midgardian Mail, Ethereal Staff, Helm of Radiance, Mantle Of Discord, Stone of
    Binding, Death Metal, Screeching Gargoyle, The Cosmic Horror, Yogi''s Necklace,
    Bracer of The Abyss, Ancile, Rod of Asclepius.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.42
      win: 0.59
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.63
      pick: 0.19
      fit: 0.33
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Prophetic Cloak, Breastplate
    of Valor, Kinetic Cuirass, Shield of the Phoenix, Amanita Charm, Soul Gem, Gluttonous
    Grimoire, Screeching Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring,
    Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Spectral
    Armor, Eye of Providence, Totem of Death, Draconic Scale, Leviathan''s Hide, Gem
    of Focus, Helm of Radiance, Midgardian Mail, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.53
      pick: 0.23
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.57
      pick: 0.14
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.55
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.43
      win: 0.71
      pick: 0.1
      fit: 0.64
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.63
      pick: 0.19
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Gluttonous
    Grimoire, Erosion, Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb,
    Breastplate of Valor, Draconic Scale, Spectral Armor, Leviathan''s Hide, Mantle
    Of Discord, Midgardian Mail, Soul Gem, Stone of Binding, Nimble Ring, Magi''s
    Cloak, Gladiator''s Shield, Ancile, Helm of Radiance, Prophetic Cloak, Screeching
    Gargoyle, Hide of the Nemean Lion, Void Shield, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.53
      pick: 0.23
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.63
      pick: 0.19
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.56
      pick: 0.19
      fit: 0.71
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.71
  starter: *id001
---
