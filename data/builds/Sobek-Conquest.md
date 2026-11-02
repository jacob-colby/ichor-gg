---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.48
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.43
    win_rate: 0.58
    alternates:
    - name: Stampede
      pick_rate: 0.26
      win_rate: 0.64
    - name: Yogi's Necklace
      pick_rate: 0.05
      win_rate: 0.48
  - name: Stampede
    pick_rate: 0.27
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.57
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 0.56
  - name: Shell of Rebuke
    pick_rate: 0.22
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.55
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.59
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.65
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.57
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.72
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.66
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.54
  - name: Medal of Defense
    pick_rate: 0.08
    win_rate: 0.62
    alternates:
    - name: Sage's Ring
      pick_rate: 0.07
      win_rate: 0.68
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.47
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.35
    win_rate: 0.51
  - name: Bluestone Brooch
    pick_rate: 0.3
    win_rate: 0.64
  - name: Selflessness
    pick_rate: 0.13
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-11-02'
  god_win_rate: 0.5730688935281837
  god_matches_won: 549
  god_matches_played: 958
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Genji's Guard
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Erosion,
    Eye of Providence, Breastplate of Valor, Shifter''s Shield, Shield of the Phoenix,
    Helm of Darkness, Oni Hunter''s Garb, Stone of Binding, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Gluttonous Grimoire, Leviathan''s Hide, Helm of Radiance,
    Screeching Gargoyle, Prophetic Cloak, Ancile, Spear of Desolation, Hide of the
    Nemean Lion, Void Stone, Xibalban Effigy, Void Shield, Hussar''s Wings.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.81
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.39
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.32
      fit: 0.64
    Draconic Scale:
      total: 0.6
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.71
    Amanita Charm:
      total: 0.58
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.53
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
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
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Draconic Scale, Shield of the Phoenix, Rod of Tahuti,
    Kinetic Cuirass, Soul Gem, Phoenix Feather, Erosion, Eye of Providence, Ethereal
    Staff, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s Garb, Shifter''s
    Shield, Gluttonous Grimoire, Glorious Pridwen, Midgardian Mail, Leviathan''s Hide,
    Helm of Darkness, Rod of Asclepius, Regrowth Striders, Stone of Binding, Ancile,
    Sphere of Negation, Hide of the Nemean Lion, Magi''s Cloak, Helm of Radiance,
    Yogi''s Necklace.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.8
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.36
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.32
      fit: 0.57
    Draconic Scale:
      total: 0.6
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.7
    Amanita Charm:
      total: 0.62
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Draconic Scale, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Obsidian Shard, Spear
    of Desolation, Soul Gem, Void Stone, Void Shield, Breastplate of Valor, Spear
    of the Magus, Erosion, Doom Orb, Eye of Providence, The World Stone, Oni Hunter''s
    Garb, Shield of the Phoenix, Helm of Darkness, Midgardian Mail, Helm of Radiance,
    Shifter''s Shield, Magi''s Cloak, Mantle Of Discord, Dreamer''s Idol, Leviathan''s
    Hide.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.32
      fit: 0.44
    Draconic Scale:
      total: 0.57
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.49
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Draconic Scale
  - Eros' Bow
  - Amanita Charm
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Draconic Scale, Amanita Charm, Nimble Ring, Kinetic Cuirass,
    Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Eros'' Bow, Oni Hunter''s
    Garb, Erosion, Obsidian Shard, Helm of Radiance, Eye of Providence, Stone of Binding,
    Shield of the Phoenix, Midgardian Mail, Spear of Desolation, Screeching Gargoyle,
    Sundering Echo, Helm of Darkness, Magi''s Cloak, Leviathan''s Hide, Mantle Of
    Discord, Blood-Bound Book, Shifter''s Shield, Bragi''s Harp, Bracer of The Abyss.'
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.46
      efficiency: 0.41
      win: 0.56
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.32
      fit: 0.33
    Draconic Scale:
      total: 0.55
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.36
    Eros' Bow:
      total: 0.48
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Breastplate
    of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Prophetic Cloak, Erosion, Gladiator''s
    Shield, Gluttonous Grimoire, Eye of Providence, Helm of Radiance, Helm of Darkness,
    Oni Hunter''s Garb, Obsidian Shard, Stone of Binding, Heartwood Charm, Gem of
    Focus, Chandra''s Grace, Midgardian Mail, Magi''s Cloak, Sundering Echo, Shifter''s
    Shield, Glorious Pridwen.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.32
      fit: 0.64
    Draconic Scale:
      total: 0.56
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.45
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Erosion,
    Eye of Providence, Draconic Scale, Breastplate of Valor, Shifter''s Shield, Shield
    of the Phoenix, Helm of Darkness, Oni Hunter''s Garb, Stone of Binding, Magi''s
    Cloak, Midgardian Mail, Mantle Of Discord, Gluttonous Grimoire, Leviathan''s Hide,
    Helm of Radiance, Screeching Gargoyle, Prophetic Cloak, Ancile, Spear of Desolation,
    Hide of the Nemean Lion, Void Stone, Xibalban Effigy, Void Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.32
      fit: 0.64
    Amanita Charm:
      total: 0.58
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.53
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod
    of Tahuti, Erosion, Eye of Providence, Draconic Scale, Breastplate of Valor, Shifter''s
    Shield, Shield of the Phoenix, Helm of Darkness, Oni Hunter''s Garb, Stone of
    Binding, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Gluttonous Grimoire,
    Leviathan''s Hide, Helm of Radiance, Screeching Gargoyle, Prophetic Cloak, Ancile,
    Spear of Desolation, Hide of the Nemean Lion, Void Stone, Xibalban Effigy, Void
    Shield, Hussar''s Wings.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.81
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.39
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.32
      fit: 0.64
    Draconic Scale:
      total: 0.6
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.71
    Amanita Charm:
      total: 0.58
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.53
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  swaps:
  - added: Draconic Scale
    removed: Eye of Providence
    reason: community 72% win over 48 matches (vs 57% on this god), taking the model's
      weakest slot from Eye of Providence
  starter: *id001
---
