---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.51
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.51
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.54
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.38
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.48
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.52
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.43
  - name: The World Stone
    pick_rate: 0.09
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.43
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.53
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.48
  - name: Freya's Tears
    pick_rate: 0.05
    win_rate: 0.56
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.63
    - name: Rod of Tahuti
      pick_rate: 0.04
      win_rate: 0.56
  - name: Hide of the Nemean Lion
    pick_rate: 0.04
    win_rate: 0.53
    alternates:
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.47
    - name: Medal of Defense
      pick_rate: 0.03
      win_rate: 0.57
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.2
    win_rate: 0.47
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.38
  - name: Pendulum of The Ages
    pick_rate: 0.09
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-08-11'
  god_win_rate: 0.47578692493946734
  god_matches_won: 393
  god_matches_played: 826
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous Grimoire,
    Breastplate of Valor, Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye
    of Providence, Draconic Scale, Spectral Armor, Soul Gem, Mantle Of Discord, Leviathan''s
    Hide, Stone of Binding, Midgardian Mail, Hide of the Nemean Lion, Helm of Radiance,
    Magi''s Cloak, Gladiator''s Shield, Ancile, Xibalban Effigy, Void Shield, Screeching
    Gargoyle, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.48
      pick: 0.18
      fit: 0.39
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.52
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.56
      pick: 0.11
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.51
      pick: 0.17
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.52
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
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Freya''s Tears,
    Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Breastplate
    of Valor, Chandra''s Grace, Erosion, Eye of Providence, Draconic Scale, Phoenix
    Feather, Spectral Armor, Leviathan''s Hide, Blood-Bound Book, Lifebinder, Bancroft''s
    Talon, Midgardian Mail, Glorious Pridwen, Gladiator''s Shield, Ancile, Jade Scepter,
    Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.48
      pick: 0.18
      fit: 0.36
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.92
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.11
      fit: 0.57
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
    for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Freya''s Tears,
    Amanita Charm, Stone of Binding, Breastplate of Valor, Spear of the Magus, Screeching
    Gargoyle, Void Shield, The Cosmic Horror, Oni Hunter''s Garb, Void Stone, Shield
    of the Phoenix, Spear of Desolation, Erosion, Obsidian Shard, Eye of Providence,
    Spectral Armor, Draconic Scale, The World Stone, Leviathan''s Hide, Helm of Radiance,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.48
      win: 0.52
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.48
      pick: 0.18
      fit: 0.27
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.52
      pick: 0.14
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.11
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
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
    this god: Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass, Amanita Charm,
    Breastplate of Valor, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral
    Armor, Erosion, Bracer of The Abyss, Eye of Providence, Helm of Radiance, Draconic
    Scale, Leviathan''s Hide, Death Metal, Midgardian Mail, Yogi''s Necklace, Mantle
    Of Discord, Stone of Binding, Spear of the Magus, Rod of Asclepius, Blood-Bound
    Book, Bragi''s Harp, Bancroft''s Talon.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.45
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.52
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.56
      pick: 0.11
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire,
    Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation,
    Chandra''s Grace, Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence,
    Draconic Scale, Helm of Radiance, Gem of Focus, Leviathan''s Hide, Mantle Of Discord,
    Midgardian Mail, Rod of Asclepius, Stone of Binding, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.48
      pick: 0.18
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.52
      pick: 0.14
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.61
    Oni Hunter's Garb:
      total: 0.5
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.29
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.56
      pick: 0.11
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Breastplate of Valor, Erosion, Oni Hunter''s Garb, Shield of the Phoenix,
    Eye of Providence, Draconic Scale, Spectral Armor, Soul Gem, Mantle Of Discord,
    Leviathan''s Hide, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s
    Cloak, Gladiator''s Shield, Ancile, Xibalban Effigy, Prophetic Cloak, Void Shield,
    Hide of the Nemean Lion, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.48
      pick: 0.18
      fit: 0.39
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.52
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.56
      pick: 0.11
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.51
      pick: 0.17
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.71
  starter: *id001
---
