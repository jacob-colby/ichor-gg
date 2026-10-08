---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.75
  slot_order:
  - name: Stampede
    pick_rate: 0.21
    win_rate: 0.6
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.11
      win_rate: 0.5
    - name: Leviathan's Hide
      pick_rate: 0.1
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.62
    alternates:
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.17
    - name: Gauntlet of Thebes
      pick_rate: 0.06
      win_rate: 0.75
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.56
    alternates:
    - name: Contagion
      pick_rate: 0.1
      win_rate: 0.43
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.71
  - name: Ethereal Staff
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.71
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.4
  - name: Stygian Anchor
    pick_rate: 0.07
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.8
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.5
  - name: Medallion
    pick_rate: 0.08
    win_rate: 1.0
    alternates:
    - name: Contagion
      pick_rate: 0.05
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.0
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.26
    win_rate: 0.56
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.47
  - name: Bluestone Brooch
    pick_rate: 0.11
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-10-08'
  god_win_rate: 0.5714285714285714
  god_matches_won: 40
  god_matches_played: 70
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Stygian Anchor
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Stygian Anchor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion,
    Helm of Darkness, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear
    of Desolation, Hussar''s Wings, Leviathan''s Hide.'
  slot_scores:
    Stygian Anchor:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.15
      fit: 0.51
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.81
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.62
      pick: 0.26
      fit: 0.39
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.71
      pick: 0.16
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
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
    swap: Stygian Anchor — magical protection
    swap_item: Stygian Anchor
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Shifter''s Shield, Soul Gem, Erosion, Ethereal Staff, Eye of
    Providence, Breastplate of Valor, Draconic Scale, Gluttonous Grimoire, Phoenix
    Feather, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone
    of Binding, Helm of Radiance, Hide of the Nemean Lion, Void Shield, Magi''s Cloak,
    Ancile, Leviathan''s Hide, Yogi''s Necklace.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.8
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.62
      pick: 0.26
      fit: 0.36
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.71
      pick: 0.16
      fit: 0.57
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Stygian Anchor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Stygian Anchor
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Spear of the Magus,
    Soul Gem, Void Shield, Breastplate of Valor, Obsidian Shard, Shifter''s Shield,
    Void Stone, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Doom Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.75
    Stygian Anchor:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.15
      fit: 0.35
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.62
      pick: 0.26
      fit: 0.27
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.71
      pick: 0.16
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Genji's Guard
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Stygian Anchor — magical protection
    swap_item: Stygian Anchor
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of Radiance,
    Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the Magus,
    Spear of Desolation, Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle
    Of Discord, Bracer of The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.24
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.62
      pick: 0.26
      fit: 0.2
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.6
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.71
      pick: 0.16
      fit: 0.33
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Stygian Anchor
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Stygian Anchor
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion,
    Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius,
    Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Stygian Anchor:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.15
      fit: 0.32
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.62
      pick: 0.26
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.71
      pick: 0.16
      fit: 0.64
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  - Freya's Tears
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
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak,
    Hide of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.62
      pick: 0.26
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.71
      pick: 0.16
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
