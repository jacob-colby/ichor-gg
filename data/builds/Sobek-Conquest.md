---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.07
  aspect_win_rate: 1.0
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.48
    win_rate: 0.52
    alternates:
    - name: Stampede
      pick_rate: 0.24
      win_rate: 0.5
    - name: Yogi's Necklace
      pick_rate: 0.06
      win_rate: 0.78
  - name: Stampede
    pick_rate: 0.21
    win_rate: 0.31
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.68
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.33
  - name: Shell of Rebuke
    pick_rate: 0.18
    win_rate: 0.35
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.63
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.47
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.56
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.14
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.75
  - name: Spectral Armor
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.4
    - name: Captain's Ring
      pick_rate: 0.06
      win_rate: 0.25
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.4
    win_rate: 0.48
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.58
  - name: Selflessness
    pick_rate: 0.14
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-11-06'
  god_win_rate: 0.5234899328859061
  god_matches_won: 78
  god_matches_played: 149
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Spectral Armor
  flex_slots:
  - Freya's Tears
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Draconic Scale, Gluttonous
    Grimoire, Shield of the Phoenix, Erosion, Breastplate of Valor, Soul Gem, Eye
    of Providence, Shifter''s Shield, Oni Hunter''s Garb, Helm of Darkness, Stone
    of Binding, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Screeching Gargoyle,
    Leviathan''s Hide, Spear of Desolation, Helm of Radiance, Gladiator''s Shield,
    Ancile, Blood-Bound Book, Void Stone, Hide of the Nemean Lion.'
  slot_scores:
    Yogi's Necklace:
      total: 0.58
      efficiency: 0.56
      win: 0.78
      pick: 0.06
      fit: 0.18
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.63
      pick: 0.2
      fit: 0.35
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.74
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.45
      win: 0.68
      pick: 0.18
      fit: 0.57
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.25
      fit: 0.57
    Spectral Armor:
      total: 0.52
      efficiency: 0.5
      win: 0.6
      pick: 0.22
      fit: 0.41
  community_ordered:
  - Yogi's Necklace
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  - Spectral Armor
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Yogi''s Necklace, Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic
    Cuirass, Rod of Tahuti, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather,
    Draconic Scale, Ethereal Staff, Erosion, Oni Hunter''s Garb, Eye of Providence,
    Chandra''s Grace, Breastplate of Valor, Shifter''s Shield, Midgardian Mail, Bancroft''s
    Talon, Regrowth Striders, Glorious Pridwen, Leviathan''s Hide, Spear of Desolation,
    Gladiator''s Shield, Screeching Gargoyle, Helm of Darkness, Hide of the Nemean
    Lion.'
  slot_scores:
    Yogi's Necklace:
      total: 0.63
      efficiency: 0.56
      win: 0.78
      pick: 0.06
      fit: 0.54
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.63
      pick: 0.2
      fit: 0.32
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.72
    Prophetic Cloak:
      total: 0.55
      efficiency: 0.45
      win: 0.68
      pick: 0.18
      fit: 0.51
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.25
      fit: 0.51
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Yogi's Necklace
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Yogi's Necklace
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic
    Cuirass, Screeching Gargoyle, Spear of Desolation, Stone of Binding, Void Stone,
    Void Shield, Obsidian Shard, Breastplate of Valor, Shield of the Phoenix, Draconic
    Scale, Spear of the Magus, Oni Hunter''s Garb, Erosion, Eye of Providence, Dreamer''s
    Idol, Shifter''s Shield, Midgardian Mail, Helm of Radiance, Doom Orb, Helm of
    Darkness, Blood-Bound Book, Leviathan''s Hide, Magi''s Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.65
    Yogi's Necklace:
      total: 0.57
      efficiency: 0.56
      win: 0.78
      pick: 0.06
      fit: 0.13
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.63
      pick: 0.2
      fit: 0.25
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.55
    Prophetic Cloak:
      total: 0.53
      efficiency: 0.45
      win: 0.68
      pick: 0.18
      fit: 0.41
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.25
      fit: 0.41
  community_ordered:
  - Yogi's Necklace
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Prophetic Cloak
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Breastplate of Valor, Soul Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s
    Garb, Draconic Scale, Erosion, Spear of Desolation, Eye of Providence, Bragi''s
    Harp, Blood-Bound Book, Helm of Radiance, Screeching Gargoyle, Shifter''s Shield,
    Midgardian Mail, Stone of Binding, Leviathan''s Hide, Magi''s Cloak, Helm of Darkness,
    Mantle Of Discord, Ancient Signet, Death Metal, Hide of the Nemean Lion.'
  slot_scores:
    Yogi's Necklace:
      total: 0.56
      efficiency: 0.56
      win: 0.78
      pick: 0.06
      fit: 0.1
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.63
      pick: 0.2
      fit: 0.2
    Prophetic Cloak:
      total: 0.52
      efficiency: 0.45
      win: 0.68
      pick: 0.18
      fit: 0.33
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.47
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.46
      efficiency: 0.47
      win: 0.51
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Yogi's Necklace
  - Genji's Guard
  - Prophetic Cloak
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
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Breastplate of Valor, Shield of the Phoenix, Spear of Desolation,
    Screeching Gargoyle, Gluttonous Grimoire, Chronos'' Pendant, Gladiator''s Shield,
    Draconic Scale, Oni Hunter''s Garb, Erosion, Eye of Providence, Helm of Radiance,
    Blood-Bound Book, Shifter''s Shield, Gem of Focus, Heartwood Charm, Helm of Darkness,
    Midgardian Mail, Chandra''s Grace, Stone of Binding, Leviathan''s Hide, Regrowth
    Striders.'
  slot_scores:
    Yogi's Necklace:
      total: 0.57
      efficiency: 0.56
      win: 0.78
      pick: 0.06
      fit: 0.12
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.63
      pick: 0.2
      fit: 0.45
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.52
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.45
      win: 0.68
      pick: 0.18
      fit: 0.6
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.25
      fit: 0.6
  community_ordered:
  - Yogi's Necklace
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Draconic Scale
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Draconic
    Scale, Gluttonous Grimoire, Shield of the Phoenix, Erosion, Breastplate of Valor,
    Soul Gem, Eye of Providence, Shifter''s Shield, Oni Hunter''s Garb, Helm of Darkness,
    Stone of Binding, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Screeching
    Gargoyle, Leviathan''s Hide, Spear of Desolation, Helm of Radiance, Hide of the
    Nemean Lion, Gladiator''s Shield, Ancile, Blood-Bound Book, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.63
      pick: 0.2
      fit: 0.35
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.25
      fit: 0.57
    Draconic Scale:
      total: 0.51
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.5
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
