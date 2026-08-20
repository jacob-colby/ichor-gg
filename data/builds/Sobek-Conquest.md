---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.31
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.31
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.51
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.51
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.49
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.56
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.5
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.48
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.49
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.56
  - name: Draconic Scale
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.62
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.52
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.66
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.52
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.37
    win_rate: 0.47
  - name: Bluestone Brooch
    pick_rate: 0.28
    win_rate: 0.58
  - name: Selflessness
    pick_rate: 0.12
    win_rate: 0.48
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-08-20'
  god_win_rate: 0.5153526970954356
  god_matches_won: 621
  god_matches_played: 1205
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
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Gluttonous Grimoire,
    Erosion, Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb, Breastplate
    of Valor, Spectral Armor, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail,
    Soul Gem, Stone of Binding, Nimble Ring, Magi''s Cloak, Gladiator''s Shield, Ancile,
    Helm of Radiance, Prophetic Cloak, Screeching Gargoyle, Void Shield, Doublet of
    Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.49
      pick: 0.27
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.49
      pick: 0.15
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.51
      pick: 0.17
      fit: 0.71
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.56
      pick: 0.15
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
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Grimoire, Ethereal Staff, Rod of Tahuti, Chandra''s Grace, Rod of Asclepius, Oni
    Hunter''s Garb, Erosion, Yogi''s Necklace, Eye of Providence, Phoenix Feather,
    Breastplate of Valor, Spectral Armor, Leviathan''s Hide, Midgardian Mail, Lifebinder,
    Glorious Pridwen, Nimble Ring, Gladiator''s Shield, Ancile, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.49
      pick: 0.27
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
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.51
      pick: 0.17
      fit: 0.7
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.56
      pick: 0.15
      fit: 0.7
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
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Breastplate of Valor, Spear of the Magus, Oni Hunter''s Garb, Void Stone, Shield
    of the Phoenix, Spear of Desolation, Obsidian Shard, Erosion, Eye of Providence,
    Spectral Armor, Nimble Ring, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord,
    Helm of Radiance, Magi''s Cloak.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.47
      win: 0.52
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.49
      pick: 0.27
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.66
    Draconic Scale:
      total: 0.51
      efficiency: 0.5
      win: 0.56
      pick: 0.15
      fit: 0.49
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.52
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Rod of Tahuti, Kinetic Cuirass, Amanita Charm, Gluttonous
    Grimoire, Breastplate of Valor, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix,
    Spectral Armor, Erosion, Eye of Providence, Leviathan''s Hide, Midgardian Mail,
    Helm of Radiance, Mantle Of Discord, Stone of Binding, Death Metal, Screeching
    Gargoyle, Ethereal Staff, The Cosmic Horror, Yogi''s Necklace, Bracer of The Abyss,
    Ancile, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.49
      pick: 0.27
      fit: 0.2
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.42
      win: 0.52
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.51
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Shield of the Phoenix
  - Draconic Scale
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Kinetic Cuirass,
    Shield of the Phoenix, Rod of Tahuti, Amanita Charm, Soul Gem, Gluttonous Grimoire,
    Screeching Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring, Chandra''s
    Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Spectral Armor, Eye
    of Providence, Prophetic Cloak, Totem of Death, Leviathan''s Hide, Gem of Focus,
    Helm of Radiance, Midgardian Mail, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.49
      pick: 0.27
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.52
      pick: 0.0
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
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.49
      pick: 0.15
      fit: 0.64
    Draconic Scale:
      total: 0.5
      efficiency: 0.5
      win: 0.56
      pick: 0.15
      fit: 0.45
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
    Breastplate of Valor, Spectral Armor, Leviathan''s Hide, Mantle Of Discord, Midgardian
    Mail, Soul Gem, Stone of Binding, Nimble Ring, Magi''s Cloak, Gladiator''s Shield,
    Ancile, Helm of Radiance, Prophetic Cloak, Screeching Gargoyle, Void Shield, Doublet
    of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.49
      pick: 0.27
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.49
      pick: 0.15
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
    Erosion:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.71
  starter: *id001
---
