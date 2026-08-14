---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.18
    win_rate: 0.58
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.54
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.73
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.58
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.65
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.46
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.86
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.56
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.46
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.55
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.33
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.86
    alternates:
    - name: Contagion
      pick_rate: 0.05
      win_rate: 0.33
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.83
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.83
    alternates:
    - name: Flaming Pearl
      pick_rate: 0.04
      win_rate: 0.33
    - name: Adroit Ring
      pick_rate: 0.04
      win_rate: 0.67
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.48
  - name: Bluestone Brooch
    pick_rate: 0.2
    win_rate: 0.59
  - name: Bumba's Cudgel
    pick_rate: 0.1
    win_rate: 0.79
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-08-14'
  god_win_rate: 0.6054421768707483
  god_matches_won: 89
  god_matches_played: 147
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Prophetic Cloak
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
    this god: Hide of the Nemean Lion, Kinetic Cuirass, Amanita Charm, Prophetic Cloak,
    Gluttonous Grimoire, Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye of
    Providence, Draconic Scale, Spectral Armor, Soul Gem, Mantle Of Discord, Leviathan''s
    Hide, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s
    Shield, Ancile, Xibalban Effigy, Void Shield, Screeching Gargoyle.'
  slot_scores:
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.65
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.81
    Prophetic Cloak:
      total: 0.58
      efficiency: 0.43
      win: 0.73
      pick: 0.1
      fit: 0.64
    Hide of the Nemean Lion:
      total: 0.64
      efficiency: 0.5
      win: 0.86
      pick: 0.13
      fit: 0.46
    Freya's Tears:
      total: 0.7
      efficiency: 0.59
      win: 0.86
      pick: 0.16
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Chandra''s Grace, Erosion, Eye
    of Providence, Draconic Scale, Phoenix Feather, Spectral Armor, Leviathan''s Hide,
    Blood-Bound Book, Lifebinder, Bancroft''s Talon, Midgardian Mail, Glorious Pridwen,
    Gladiator''s Shield, Ancile, Jade Scepter, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.65
      pick: 0.16
      fit: 0.36
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.92
    Hide of the Nemean Lion:
      total: 0.64
      efficiency: 0.5
      win: 0.86
      pick: 0.13
      fit: 0.48
    Freya's Tears:
      total: 0.69
      efficiency: 0.59
      win: 0.86
      pick: 0.16
      fit: 0.57
    Amanita Charm:
      total: 0.65
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Amanita Charm, Stone
    of Binding, Spear of the Magus, Screeching Gargoyle, Void Shield, The Cosmic Horror,
    Oni Hunter''s Garb, Void Stone, Shield of the Phoenix, Spear of Desolation, Erosion,
    Obsidian Shard, Eye of Providence, Spectral Armor, Draconic Scale, Leviathan''s
    Hide, Helm of Radiance, Mantle Of Discord, Midgardian Mail, The World Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.58
      pick: 0.18
      fit: 0.27
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.65
      pick: 0.16
      fit: 0.27
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.59
    Hide of the Nemean Lion:
      total: 0.62
      efficiency: 0.5
      win: 0.86
      pick: 0.13
      fit: 0.32
    Freya's Tears:
      total: 0.67
      efficiency: 0.59
      win: 0.86
      pick: 0.16
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Hide of the Nemean Lion
  - Freya's Tears
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Oni Hunter''s Garb,
    Soul Gem, Shield of the Phoenix, Spectral Armor, Erosion, Bracer of The Abyss,
    Eye of Providence, Helm of Radiance, Draconic Scale, Leviathan''s Hide, Death
    Metal, Midgardian Mail, Yogi''s Necklace, Mantle Of Discord, Stone of Binding,
    Spear of the Magus, Rod of Asclepius, Blood-Bound Book, Bragi''s Harp, Bancroft''s
    Talon.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.65
      pick: 0.16
      fit: 0.2
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.49
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.61
      pick: 0.0
      fit: 0.44
    Hide of the Nemean Lion:
      total: 0.6
      efficiency: 0.5
      win: 0.86
      pick: 0.13
      fit: 0.23
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.86
      pick: 0.16
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Hide of the Nemean Lion
  - Freya's Tears
  flex_slots:
  - Prophetic Cloak
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
    Shield of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire, Oni Hunter''s
    Garb, Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation, Chandra''s
    Grace, Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence, Draconic
    Scale, Helm of Radiance, Gem of Focus, Leviathan''s Hide, Mantle Of Discord, Midgardian
    Mail, Rod of Asclepius, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.58
      pick: 0.18
      fit: 0.48
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.66
      win: 0.65
      pick: 0.16
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.55
    Prophetic Cloak:
      total: 0.58
      efficiency: 0.43
      win: 0.73
      pick: 0.1
      fit: 0.64
    Hide of the Nemean Lion:
      total: 0.61
      efficiency: 0.5
      win: 0.86
      pick: 0.13
      fit: 0.29
    Freya's Tears:
      total: 0.7
      efficiency: 0.59
      win: 0.86
      pick: 0.16
      fit: 0.64
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
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence, Draconic
    Scale, Spectral Armor, Soul Gem, Mantle Of Discord, Leviathan''s Hide, Stone of
    Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s Shield,
    Ancile, Xibalban Effigy, Prophetic Cloak, Void Shield, Hide of the Nemean Lion,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.58
      pick: 0.18
      fit: 0.39
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.65
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.7
      efficiency: 0.59
      win: 0.86
      pick: 0.16
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.58
      pick: 0.18
      fit: 0.71
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.71
  starter: *id001
---
