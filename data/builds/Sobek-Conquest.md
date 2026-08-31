---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.35
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.29
    win_rate: 0.56
    alternates:
    - name: Stampede
      pick_rate: 0.21
      win_rate: 0.52
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.61
  - name: Stampede
    pick_rate: 0.18
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.55
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.6
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.52
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.51
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.55
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.69
    alternates:
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.52
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.83
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Captain's Ring
      pick_rate: 0.06
      win_rate: 0.67
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.38
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.26
    win_rate: 0.62
  - name: Selflessness
    pick_rate: 0.14
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-08-31'
  god_win_rate: 0.561046511627907
  god_matches_won: 386
  god_matches_played: 688
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-31'
  god_matches_analyzed: 7103
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
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Breastplate
    of Valor, Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Helm of Darkness, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation,
    Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.28
      fit: 0.39
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.69
      pick: 0.22
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.12
      fit: 0.71
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.56
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
  - Spirit Robe
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Shifter''s Shield, Rod of Asclepius, Soul Gem, Erosion, Eye of Providence, Breastplate
    of Valor, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Draconic Scale,
    Yogi''s Necklace, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail,
    Stone of Binding, Helm of Radiance, Leviathan''s Hide, Void Shield, Magi''s Cloak,
    Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.28
      fit: 0.36
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.8
    Spirit Robe:
      total: 0.61
      efficiency: 0.34
      win: 0.83
      pick: 0.11
      fit: 0.73
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.69
      pick: 0.22
      fit: 0.57
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.12
      fit: 0.7
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Spear of the Magus,
    Soul Gem, Void Shield, Breastplate of Valor, Shifter''s Shield, Obsidian Shard,
    Void Stone, Erosion, Eye of Providence, Shield of the Phoenix, Doom Orb, Helm
    of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Draconic Scale,
    Mantle Of Discord, Midgardian Mail, Rod of Asclepius.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.69
      pick: 0.22
      fit: 0.44
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Spirit Robe
  - Bragi's Harp
  - Freya's Tears
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of Radiance,
    Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix, Magi''s Cloak,
    Screeching Gargoyle, Daybreak Gavel, Spear of the Magus, Spear of Desolation,
    Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of
    The Abyss, Draconic Scale, Obsidian Shard, Leviathan''s Hide.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.31
    Spirit Robe:
      total: 0.54
      efficiency: 0.34
      win: 0.83
      pick: 0.11
      fit: 0.26
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.69
      pick: 0.22
      fit: 0.33
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
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion,
    Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus,
    Spear of the Magus, Draconic Scale, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.28
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.69
      pick: 0.22
      fit: 0.64
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
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
    Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb,
    Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.28
      fit: 0.39
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.69
      pick: 0.22
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.12
      fit: 0.71
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shell of Rebuke
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Shifter''s Shield, Breastplate of Valor, Erosion, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of
    Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail, Screeching
    Gargoyle, Prophetic Cloak, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.28
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.81
    Shell of Rebuke:
      total: 0.49
      efficiency: 0.28
      win: 0.67
      pick: 0.23
      fit: 0.51
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.69
      pick: 0.22
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.12
      fit: 0.71
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.71
  swaps:
  - added: Shell of Rebuke
    removed: Breastplate of Valor
    reason: community 67% win over 96 matches (vs 56% on this god), taking the model's
      weakest slot from Breastplate of Valor
  starter: *id001
---
