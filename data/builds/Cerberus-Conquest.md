---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.43
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.5
    win_rate: 0.54
    alternates:
    - name: Stampede
      pick_rate: 0.2
      win_rate: 0.53
    - name: Yogi's Necklace
      pick_rate: 0.04
      win_rate: 0.45
  - name: Stampede
    pick_rate: 0.26
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.6
    - name: Screeching Gargoyle
      pick_rate: 0.1
      win_rate: 0.49
  - name: Shell of Rebuke
    pick_rate: 0.25
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.55
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.49
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.19
      win_rate: 0.62
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.48
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.52
  - name: Medal of Defense
    pick_rate: 0.1
    win_rate: 0.58
    alternates:
    - name: Sage's Ring
      pick_rate: 0.09
      win_rate: 0.46
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.56
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.29
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.52
  - name: Archmage's Gem
    pick_rate: 0.14
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-11-02'
  god_win_rate: 0.5377855887521968
  god_matches_won: 306
  god_matches_played: 569
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
  - Draconic Scale
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
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Erosion, Eye of Providence, Helm of Darkness, Shield of the Phoenix,
    Shifter''s Shield, Stone of Binding, Oni Hunter''s Garb, Magi''s Cloak, Helm of
    Radiance, Midgardian Mail, Mantle Of Discord, Gluttonous Grimoire, Leviathan''s
    Hide, Spear of Desolation, Prophetic Cloak, Ancile, Hide of the Nemean Lion, Obsidian
    Shard, Void Stone, Eros'' Bow, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.35
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.49
      pick: 0.35
      fit: 0.57
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.63
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.63
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
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Stampede
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Draconic Scale, Shield of the Phoenix,
    Kinetic Cuirass, Soul Gem, Phoenix Feather, Ethereal Staff, Breastplate of Valor,
    Erosion, Eye of Providence, Chandra''s Grace, Oni Hunter''s Garb, Gluttonous Grimoire,
    Shifter''s Shield, Midgardian Mail, Glorious Pridwen, Helm of Darkness, Leviathan''s
    Hide, Rod of Asclepius, Helm of Radiance, Sphere of Negation, Stone of Binding,
    Regrowth Striders, Eros'' Bow, Blood-Bound Book, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.85
    Stampede:
      total: 0.52
      efficiency: 0.51
      win: 0.58
      pick: 0.35
      fit: 0.43
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.61
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Stampede
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Draconic Scale, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation, Obsidian Shard, Soul
    Gem, Void Stone, Void Shield, Breastplate of Valor, Spear of the Magus, Screeching
    Gargoyle, Erosion, Doom Orb, Eye of Providence, Helm of Radiance, The World Stone,
    Oni Hunter''s Garb, Helm of Darkness, Shield of the Phoenix, Midgardian Mail,
    Magi''s Cloak, Dreamer''s Idol, Mantle Of Discord, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.25
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.55
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.87
      win: 0.55
      pick: 0.0
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Nimble Ring
  - Bragi's Harp
  - Draconic Scale
  - Eros' Bow
  - Amanita Charm
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Draconic Scale, Amanita Charm, Nimble Ring, Kinetic Cuirass,
    Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Helm of Radiance, Eros''
    Bow, Erosion, Oni Hunter''s Garb, Eye of Providence, Stone of Binding, Obsidian
    Shard, Spear of Desolation, Helm of Darkness, Midgardian Mail, Shield of the Phoenix,
    Magi''s Cloak, Blood-Bound Book, Bragi''s Harp, Mantle Of Discord, Leviathan''s
    Hide, Shifter''s Shield, Bracer of The Abyss, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.2
    Nimble Ring:
      total: 0.52
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.47
      efficiency: 0.45
      win: 0.55
      pick: 0.0
      fit: 0.44
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.36
    Eros' Bow:
      total: 0.48
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
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
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Draconic Scale, Amanita
    Charm, Breastplate of Valor, Kinetic Cuirass, Spear of Desolation, Shield of the
    Phoenix, Soul Gem, Chronos'' Pendant, Helm of Radiance, Prophetic Cloak, Screeching
    Gargoyle, Helm of Darkness, Erosion, Gluttonous Grimoire, Eye of Providence, Obsidian
    Shard, Oni Hunter''s Garb, Stone of Binding, Gem of Focus, Gladiator''s Shield,
    Midgardian Mail, Magi''s Cloak, Heartwood Charm, Nimble Ring, Mantle Of Discord,
    Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.49
      pick: 0.35
      fit: 0.59
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Draconic Scale, Amanita Charm, Shield Splitter, Kinetic Cuirass, Runeforged
    Hammer, Tekko-Kagi, Golden Blade, Titan''s Bane, Breastplate of Valor, Hydra''s
    Lament, Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, Tyrfing, The
    Crusher, Soul Gem, Lernaean Bow, Heartseeker, Erosion, Helm of Radiance, Avenging
    Blade, Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Helm of Darkness,
    Arondight, The Reaper, Shield of the Phoenix, Toxic Blade, Midgardian Mail, Death
    Metal, Magi''s Cloak, Spear of the Magus, Pharaoh''s Curse, Silverbranch Bow,
    Mantle Of Discord, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.23
    Berserker's Shield:
      total: 0.56
      efficiency: 0.75
      win: 0.55
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.45
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.52
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.41
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield,
    Jotunn''s Revenge, Draconic Scale, Amanita Charm, Shield Splitter, Kinetic Cuirass,
    Gluttonous Grimoire, Obsidian Shard, Spear of Desolation, Soul Gem, Breastplate
    of Valor, Helm of Radiance, Runeforged Hammer, Titan''s Bane, Tekko-Kagi, Helm
    of Darkness, Spear of the Magus, Golden Blade, Hydra''s Lament, Death Metal, Nimble
    Ring, Tyrfing, Erosion, Eye of Providence, Oni Hunter''s Garb, Eros'' Bow, Doom
    Orb, The Crusher, Stone of Binding, Bragi''s Harp, Jade Scepter, Heartseeker,
    Shield of the Phoenix, The World Stone, Midgardian Mail, Avenging Blade, Lernaean
    Bow, Magi''s Cloak, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.21
    Berserker's Shield:
      total: 0.56
      efficiency: 0.75
      win: 0.55
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.38
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.44
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.39
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Erosion
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Helm of Darkness, Shield
    of the Phoenix, Shifter''s Shield, Stone of Binding, Oni Hunter''s Garb, Magi''s
    Cloak, Helm of Radiance, Midgardian Mail, Mantle Of Discord, Gluttonous Grimoire,
    Leviathan''s Hide, Screeching Gargoyle, Spear of Desolation, Prophetic Cloak,
    Ancile, Hide of the Nemean Lion, Obsidian Shard, Void Stone, Eros'' Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.35
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.49
      pick: 0.35
      fit: 0.57
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.52
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
