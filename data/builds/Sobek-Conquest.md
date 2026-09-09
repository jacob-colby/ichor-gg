---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.02
  aspect_win_rate: 1.0
  slot_order:
  - name: Stampede
    pick_rate: 0.25
    win_rate: 0.47
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.17
      win_rate: 0.2
    - name: Yogi's Necklace
      pick_rate: 0.14
      win_rate: 0.75
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.38
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.75
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.25
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.05
      win_rate: 0.33
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.75
  - name: Hide of the Nemean Lion
    pick_rate: 0.11
    win_rate: 0.4
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.5
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.33
  - name: Draconic Scale
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Captain's Ring
      pick_rate: 0.07
      win_rate: 0.0
    - name: Mantle Of Discord
      pick_rate: 0.07
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.27
    win_rate: 0.69
  - name: Bluestone Pendant
    pick_rate: 0.25
    win_rate: 0.47
  - name: Selflessness
    pick_rate: 0.15
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-09-09'
  god_win_rate: 0.5423728813559322
  god_matches_won: 32
  god_matches_played: 59
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Yogi's Necklace
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Erosion,
    Eye of Providence, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Helm
    of Radiance, Gluttonous Grimoire, Midgardian Mail, Screeching Gargoyle, Prophetic
    Cloak, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Yogi's Necklace:
      total: 0.56
      efficiency: 0.52
      win: 0.75
      pick: 0.14
      fit: 0.2
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.19
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.56
      pick: 0.28
      fit: 0.64
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.71
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.71
  community_ordered:
  - Yogi's Necklace
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Yogi''s Necklace, Amanita Charm, Shield of the Phoenix, Rod of Tahuti,
    Kinetic Cuirass, Rod of Asclepius, Shifter''s Shield, Soul Gem, Erosion, Eye of
    Providence, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Chandra''s Grace,
    Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding, Helm of Radiance,
    Leviathan''s Hide, Void Shield, Magi''s Cloak, Ancile.'
  slot_scores:
    Yogi's Necklace:
      total: 0.61
      efficiency: 0.52
      win: 0.75
      pick: 0.14
      fit: 0.57
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.19
      fit: 0.36
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.56
      pick: 0.28
      fit: 0.57
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.7
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Yogi's Necklace
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Yogi's Necklace
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Spear of the Magus,
    Soul Gem, Void Shield, Obsidian Shard, Shifter''s Shield, Void Stone, Erosion,
    Eye of Providence, Shield of the Phoenix, Doom Orb, Helm of Radiance, The World
    Stone, Dreamer''s Idol, Magi''s Cloak, Midgardian Mail, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.5
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.75
    Yogi's Necklace:
      total: 0.55
      efficiency: 0.52
      win: 0.75
      pick: 0.14
      fit: 0.14
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.19
      fit: 0.27
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.28
      fit: 0.44
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.49
  community_ordered:
  - Yogi's Necklace
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Yogi's Necklace
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Draconic Scale
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Shifter''s Shield, Soul Gem, Helm of Radiance, Erosion, Stone of Binding,
    Eye of Providence, Shield of the Phoenix, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, Spear of the Magus, Spear of Desolation, Bragi''s Harp, Rod of
    Asclepius, Midgardian Mail, Bracer of The Abyss, Obsidian Shard, Leviathan''s
    Hide.'
  slot_scores:
    Yogi's Necklace:
      total: 0.54
      efficiency: 0.52
      win: 0.75
      pick: 0.14
      fit: 0.1
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.19
      fit: 0.2
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.43
      efficiency: 0.44
      win: 0.47
      pick: 0.0
      fit: 0.44
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.36
  community_ordered:
  - Yogi's Necklace
  - Breastplate of Valor
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Shield of the Phoenix
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching Gargoyle, Soul
    Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm of Radiance,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Stone of Binding,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.19
      fit: 0.48
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.38
      pick: 0.19
      fit: 0.48
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.56
      pick: 0.28
      fit: 0.64
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
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
    Shield, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding, Magi''s
    Cloak, Helm of Radiance, Gluttonous Grimoire, Midgardian Mail, Screeching Gargoyle,
    Prophetic Cloak, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni
    Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.19
      fit: 0.39
    Genji's Guard:
      total: 0.47
      efficiency: 0.66
      win: 0.38
      pick: 0.19
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.56
      pick: 0.28
      fit: 0.64
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
