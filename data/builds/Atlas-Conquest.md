---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.52
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.2
    win_rate: 0.57
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.53
    - name: Yogi's Necklace
      pick_rate: 0.1
      win_rate: 0.77
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.59
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 0.72
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.58
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.64
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.63
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.44
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.7
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.58
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.5
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.75
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.45
    - name: Olmec Blue
      pick_rate: 0.04
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.53
  - name: Bumba's Hammer
    pick_rate: 0.08
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-08-19'
  god_win_rate: 0.5739348370927319
  god_matches_won: 229
  god_matches_played: 399
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Yogi's Necklace
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Prophetic Cloak, Rod of Tahuti, Gluttonous
    Grimoire, Erosion, Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb,
    Draconic Scale, Spectral Armor, Leviathan''s Hide, Mantle Of Discord, Midgardian
    Mail, Soul Gem, Stone of Binding, Nimble Ring, Magi''s Cloak, Gladiator''s Shield,
    Ancile, Helm of Radiance, Screeching Gargoyle, Hide of the Nemean Lion.'
  slot_scores:
    Yogi's Necklace:
      total: 0.58
      efficiency: 0.57
      win: 0.77
      pick: 0.1
      fit: 0.2
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.81
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.43
      win: 0.72
      pick: 0.1
      fit: 0.64
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.7
      pick: 0.17
      fit: 0.64
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Yogi's Necklace
  - Prophetic Cloak
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Rod of Tahuti, Chandra''s Grace, Rod of Asclepius, Oni Hunter''s Garb,
    Erosion, Eye of Providence, Draconic Scale, Phoenix Feather, Spectral Armor, Leviathan''s
    Hide, Midgardian Mail, Lifebinder, Glorious Pridwen, Nimble Ring, Gladiator''s
    Shield, Ancile, Blood-Bound Book, Hide of the Nemean Lion.'
  slot_scores:
    Yogi's Necklace:
      total: 0.59
      efficiency: 0.57
      win: 0.77
      pick: 0.1
      fit: 0.27
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.8
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.43
      win: 0.72
      pick: 0.1
      fit: 0.57
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.7
      pick: 0.17
      fit: 0.57
    Amanita Charm:
      total: 0.64
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Yogi's Necklace
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Stone of Binding, Screeching Gargoyle, Void Shield, The Cosmic Horror,
    Spear of the Magus, Oni Hunter''s Garb, Void Stone, Shield of the Phoenix, Spear
    of Desolation, Erosion, Eye of Providence, Spectral Armor, Nimble Ring, Draconic
    Scale, Obsidian Shard, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.75
    Yogi's Necklace:
      total: 0.57
      efficiency: 0.57
      win: 0.77
      pick: 0.1
      fit: 0.14
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.7
      pick: 0.17
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.61
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Yogi's Necklace
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Yogi''s Necklace, Nimble Ring, Rod of Tahuti, Kinetic Cuirass, Amanita
    Charm, Gluttonous Grimoire, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix,
    Spectral Armor, Erosion, Eye of Providence, Draconic Scale, Leviathan''s Hide,
    Midgardian Mail, Helm of Radiance, Mantle Of Discord, Stone of Binding, Death
    Metal, Screeching Gargoyle, The Cosmic Horror, Bracer of The Abyss, Ancile.'
  slot_scores:
    Yogi's Necklace:
      total: 0.57
      efficiency: 0.57
      win: 0.77
      pick: 0.1
      fit: 0.1
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.42
      win: 0.61
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.7
      pick: 0.17
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  flex_slots:
  - Yogi's Necklace
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Prophetic Cloak, Kinetic Cuirass,
    Shield of the Phoenix, Rod of Tahuti, Amanita Charm, Soul Gem, Gluttonous Grimoire,
    Screeching Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring, Chandra''s
    Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Spectral Armor, Eye
    of Providence, Draconic Scale, Leviathan''s Hide, Gem of Focus, Helm of Radiance,
    Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Yogi's Necklace:
      total: 0.57
      efficiency: 0.57
      win: 0.77
      pick: 0.1
      fit: 0.13
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.56
      pick: 0.22
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.61
      pick: 0.16
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.55
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.43
      win: 0.72
      pick: 0.1
      fit: 0.64
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.17
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
    Draconic Scale, Spectral Armor, Leviathan''s Hide, Mantle Of Discord, Midgardian
    Mail, Soul Gem, Stone of Binding, Nimble Ring, Magi''s Cloak, Gladiator''s Shield,
    Ancile, Helm of Radiance, Prophetic Cloak, Screeching Gargoyle, Hide of the Nemean
    Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.56
      pick: 0.22
      fit: 0.39
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.7
      pick: 0.17
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.2
      fit: 0.71
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.56
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.71
  starter: *id001
---
