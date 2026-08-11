---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.22
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.26
    win_rate: 0.54
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.25
      win_rate: 0.53
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.51
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.5
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.53
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.49
    alternates:
    - name: Genji's Guard
      pick_rate: 0.24
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.54
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.53
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.55
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.6
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.68
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.54
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.5
    - name: Shield
      pick_rate: 0.04
      win_rate: 0.49
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.36
    win_rate: 0.49
  - name: Bluestone Brooch
    pick_rate: 0.26
    win_rate: 0.58
  - name: Selflessness
    pick_rate: 0.11
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-08-10'
  god_win_rate: 0.5280135823429541
  god_matches_won: 933
  god_matches_played: 1767
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
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
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous Grimoire,
    Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence, Draconic
    Scale, Spectral Armor, Hide of the Nemean Lion, Soul Gem, Leviathan''s Hide, Mantle
    Of Discord, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak,
    Gladiator''s Shield, Ancile, Xibalban Effigy, Prophetic Cloak, Void Shield, Screeching
    Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Freya''s Tears, Chandra''s Grace,
    Erosion, Eye of Providence, Draconic Scale, Phoenix Feather, Spectral Armor, Leviathan''s
    Hide, Blood-Bound Book, Lifebinder, Bancroft''s Talon, Midgardian Mail, Glorious
    Pridwen, Gladiator''s Shield, Ancile, Helm of Radiance, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.92
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 0.7
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.5
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
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Stone of Binding
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Amanita Charm, Stone
    of Binding, Spear of the Magus, Freya''s Tears, Screeching Gargoyle, Void Shield,
    Oni Hunter''s Garb, The Cosmic Horror, Void Stone, Shield of the Phoenix, Spear
    of Desolation, Erosion, Eye of Providence, Obsidian Shard, Spectral Armor, Draconic
    Scale, Leviathan''s Hide, Helm of Radiance, Mantle Of Discord, Midgardian Mail,
    Doom Orb.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.27
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.66
      win: 0.49
      pick: 0.16
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shifter's Shield:
      total: 0.51
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Freya''s Tears,
    Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral Armor, Erosion,
    Bracer of The Abyss, Eye of Providence, Helm of Radiance, Draconic Scale, Death
    Metal, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Yogi''s Necklace,
    Stone of Binding, Spear of the Magus, Bragi''s Harp, Rod of Asclepius, Blood-Bound
    Book, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.2
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
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
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Shield of the Phoenix
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Kinetic Cuirass, Shield
    of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire, Oni Hunter''s Garb,
    Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation, Chandra''s Grace,
    Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic Cloak,
    Draconic Scale, Helm of Radiance, Gem of Focus, Leviathan''s Hide, Death Metal,
    Midgardian Mail, Mantle Of Discord, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.49
      pick: 0.16
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.5
      efficiency: 0.52
      win: 0.54
      pick: 0.26
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
    Grimoire, Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence,
    Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s Hide, Mantle Of Discord,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s
    Shield, Ancile, Xibalban Effigy, Prophetic Cloak, Void Shield, Hide of the Nemean
    Lion, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
---
