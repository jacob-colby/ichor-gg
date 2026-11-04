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
    pick_rate: 0.44
    win_rate: 0.59
    alternates:
    - name: Stampede
      pick_rate: 0.26
      win_rate: 0.63
    - name: Yogi's Necklace
      pick_rate: 0.05
      win_rate: 0.48
  - name: Stampede
    pick_rate: 0.27
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.57
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 0.56
  - name: Shell of Rebuke
    pick_rate: 0.22
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.54
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.61
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.65
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.58
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.73
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
      win_rate: 0.69
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.47
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.36
    win_rate: 0.51
  - name: Bluestone Brooch
    pick_rate: 0.3
    win_rate: 0.64
  - name: Selflessness
    pick_rate: 0.13
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-11-04'
  god_win_rate: 0.5733333333333334
  god_matches_won: 559
  god_matches_played: 975
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
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
    this god: Draconic Scale, Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Gluttonous
    Grimoire, Erosion, Breastplate of Valor, Eye of Providence, Soul Gem, Helm of
    Darkness, Oni Hunter''s Garb, Shield of the Phoenix, Shifter''s Shield, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Midgardian Mail, Mantle Of Discord,
    Leviathan''s Hide, Screeching Gargoyle, Spear of Desolation, Ancile, Prophetic
    Cloak, Hide of the Nemean Lion, Obsidian Shard, Void Stone.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.54
      pick: 0.22
      fit: 0.35
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.61
      pick: 0.32
      fit: 0.57
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.64
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.64
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
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Soul Gem
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Draconic Scale, Rod of Tahuti, Soul Gem, Shield of the
    Phoenix, Kinetic Cuirass, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather,
    Ethereal Staff, Erosion, Eye of Providence, Breastplate of Valor, Oni Hunter''s
    Garb, Chandra''s Grace, Midgardian Mail, Shifter''s Shield, Glorious Pridwen,
    Bancroft''s Talon, Leviathan''s Hide, Helm of Darkness, Regrowth Striders, Helm
    of Radiance, Sphere of Negation, Stone of Binding, Spear of Desolation, Yogi''s
    Necklace.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.54
      pick: 0.22
      fit: 0.32
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.61
      pick: 0.32
      fit: 0.51
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.62
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.92
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Rod of Tahuti, Draconic Scale, Gluttonous Grimoire, Soul Gem, Amanita
    Charm, Stone of Binding, Kinetic Cuirass, Spear of Desolation, Screeching Gargoyle,
    Obsidian Shard, Void Stone, Void Shield, Spear of the Magus, Breastplate of Valor,
    Erosion, Oni Hunter''s Garb, Eye of Providence, Doom Orb, Helm of Radiance, The
    World Stone, Helm of Darkness, Shield of the Phoenix, Midgardian Mail, Magi''s
    Cloak, Dreamer''s Idol, Mantle Of Discord, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.72
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.61
      pick: 0.32
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.69
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.45
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
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
    Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Oni Hunter''s Garb, Helm
    of Radiance, Erosion, Eye of Providence, Obsidian Shard, Stone of Binding, Spear
    of Desolation, Helm of Darkness, Midgardian Mail, Shield of the Phoenix, Magi''s
    Cloak, Screeching Gargoyle, Blood-Bound Book, Leviathan''s Hide, Bragi''s Harp,
    Mantle Of Discord, Ancient Signet, Shifter''s Shield, Bracer of The Abyss.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.53
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.45
      win: 0.57
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.61
      pick: 0.32
      fit: 0.33
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
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
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Draconic Scale, Amanita
    Charm, Soul Gem, Breastplate of Valor, Kinetic Cuirass, Spear of Desolation, Gluttonous
    Grimoire, Shield of the Phoenix, Screeching Gargoyle, Chronos'' Pendant, Helm
    of Radiance, Prophetic Cloak, Oni Hunter''s Garb, Erosion, Helm of Darkness, Eye
    of Providence, Obsidian Shard, Stone of Binding, Gladiator''s Shield, Gem of Focus,
    Midgardian Mail, Heartwood Charm, Magi''s Cloak, Blood-Bound Book, Mantle Of Discord,
    Leviathan''s Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.54
      pick: 0.22
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.61
      pick: 0.32
      fit: 0.6
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.42
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.59
  community_ordered:
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
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Gluttonous
    Grimoire, Erosion, Breastplate of Valor, Eye of Providence, Soul Gem, Draconic
    Scale, Helm of Darkness, Oni Hunter''s Garb, Shield of the Phoenix, Shifter''s
    Shield, Stone of Binding, Magi''s Cloak, Helm of Radiance, Midgardian Mail, Mantle
    Of Discord, Leviathan''s Hide, Screeching Gargoyle, Spear of Desolation, Ancile,
    Prophetic Cloak, Hide of the Nemean Lion, Obsidian Shard, Void Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.35
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.54
      pick: 0.22
      fit: 0.35
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.61
      pick: 0.32
      fit: 0.57
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.64
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
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Gluttonous Grimoire, Erosion, Breastplate of Valor, Eye of Providence,
    Soul Gem, Draconic Scale, Helm of Darkness, Oni Hunter''s Garb, Shield of the
    Phoenix, Shifter''s Shield, Stone of Binding, Magi''s Cloak, Helm of Radiance,
    Midgardian Mail, Mantle Of Discord, Leviathan''s Hide, Screeching Gargoyle, Spear
    of Desolation, Ancile, Prophetic Cloak, Hide of the Nemean Lion, Obsidian Shard,
    Void Stone.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.54
      pick: 0.22
      fit: 0.35
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.61
      pick: 0.32
      fit: 0.57
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.64
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  swaps:
  - added: Draconic Scale
    removed: Breastplate of Valor
    reason: community 73% win over 49 matches (vs 57% on this god), taking the model's
      weakest slot from Breastplate of Valor
  starter: *id001
---
