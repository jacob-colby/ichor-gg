---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.55
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.48
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.51
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.54
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.55
    - name: Ethereal Staff
      pick_rate: 0.08
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.53
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.52
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.48
    - name: Ethereal Staff
      pick_rate: 0.08
      win_rate: 0.52
  - name: Ethereal Staff
    pick_rate: 0.06
    win_rate: 0.51
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.59
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.61
  - name: Olmec Blue
    pick_rate: 0.04
    win_rate: 0.8
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.55
    - name: Engraved Guard
      pick_rate: 0.04
      win_rate: 0.6
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.48
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.63
  - name: Bumba's Hammer
    pick_rate: 0.14
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-08-24'
  god_win_rate: 0.541374474053296
  god_matches_won: 386
  god_matches_played: 713
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-24'
  god_matches_analyzed: 17273
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Rod of Tahuti, Kinetic Cuirass, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion,
    Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb,
    Xibalban Effigy, Spear of Desolation, Hussar''s Wings, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.27
      fit: 0.39
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.14
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.55
      pick: 0.17
      fit: 0.71
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.55
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
  - Shifter's Shield
  - Genji's Guard
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Freya''s Tears, Rod of Asclepius, Breastplate of Valor, Soul Gem, Erosion, Eye
    of Providence, Draconic Scale, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace,
    Chandra''s Grace, Ethereal Staff, Glorious Pridwen, Lifebinder, Midgardian Mail,
    Stone of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide,
    Void Shield, Magi''s Cloak, Ancile, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.27
      fit: 0.36
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.14
      fit: 0.57
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.17
      fit: 0.7
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.55
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
  - Genji's Guard
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Rod of Tahuti, Amanita Charm, Freya''s Tears, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Breastplate of Valor, Spear of the Magus, Soul Gem, Void Shield, Obsidian Shard,
    Void Stone, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Doom Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.27
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.14
      fit: 0.44
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.55
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Rod of Tahuti, Amanita Charm, Freya''s Tears, Nimble Ring, Kinetic Cuirass,
    Breastplate of Valor, Gluttonous Grimoire, Soul Gem, Helm of Radiance, Erosion,
    Stone of Binding, Eye of Providence, Shield of the Phoenix, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the Magus, Spear of Desolation,
    Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of
    The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.27
      fit: 0.2
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.55
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.14
      fit: 0.33
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
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
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Breastplate
    of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm
    of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Draconic
    Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of
    Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail,
    Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.27
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.14
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.14
      fit: 0.64
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Freya''s
    Tears, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak,
    Hide of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.27
      fit: 0.39
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.14
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.55
      pick: 0.17
      fit: 0.71
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.71
  starter: *id001
---
