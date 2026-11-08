---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.5
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.17
      win_rate: 0.71
    - name: Yogi's Necklace
      pick_rate: 0.09
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.83
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.6
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.56
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.33
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.29
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.82
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.38
    - name: Omen Drum
      pick_rate: 0.07
      win_rate: 0.67
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.5
    - name: Ethereal Staff
      pick_rate: 0.05
      win_rate: 0.5
  - name: Spectral Armor
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.06
      win_rate: 0.33
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.39
    win_rate: 0.54
  - name: Bluestone Brooch
    pick_rate: 0.3
    win_rate: 0.63
  - name: War Flag
    pick_rate: 0.06
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-11-08'
  god_win_rate: 0.5656565656565656
  god_matches_won: 56
  god_matches_played: 99
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shell of Rebuke
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Draconic Scale, Gluttonous
    Grimoire, Shield of the Phoenix, Erosion, Breastplate of Valor, Soul Gem, Eye
    of Providence, Shifter''s Shield, Oni Hunter''s Garb, Helm of Darkness, Stone
    of Binding, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Screeching Gargoyle,
    Leviathan''s Hide, Spear of Desolation, Helm of Radiance, Hide of the Nemean Lion,
    Gladiator''s Shield, Lotus Sickle, Ancile, Blood-Bound Book, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.68
      efficiency: 0.71
      win: 0.83
      pick: 0.16
      fit: 0.35
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.74
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.41
      win: 0.82
      pick: 0.2
      fit: 0.45
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.57
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
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
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Rod
    of Tahuti, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather, Draconic Scale,
    Erosion, Oni Hunter''s Garb, Eye of Providence, Chandra''s Grace, Breastplate
    of Valor, Shifter''s Shield, Midgardian Mail, Bancroft''s Talon, Rod of Asclepius,
    Regrowth Striders, Glorious Pridwen, Leviathan''s Hide, Soul Locket, Hide of the
    Nemean Lion, Spear of Desolation, Gladiator''s Shield, Screeching Gargoyle, Yogi''s
    Necklace, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.68
      efficiency: 0.71
      win: 0.83
      pick: 0.16
      fit: 0.32
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.85
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.51
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.68
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic
    Cuirass, Screeching Gargoyle, Spear of Desolation, Stone of Binding, Void Stone,
    Void Shield, Obsidian Shard, Breastplate of Valor, Shield of the Phoenix, Draconic
    Scale, Spear of the Magus, Oni Hunter''s Garb, Erosion, Eye of Providence, Dreamer''s
    Idol, Shifter''s Shield, Midgardian Mail, Helm of Radiance, Doom Orb, Lotus Sickle,
    Helm of Darkness, Blood-Bound Book, Leviathan''s Hide, Magi''s Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.67
      efficiency: 0.71
      win: 0.83
      pick: 0.16
      fit: 0.25
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.67
      pick: 0.0
      fit: 0.38
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Nimble Ring
  - Bragi's Harp
  - Eros' Bow
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Breastplate of Valor, Soul Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s
    Garb, Draconic Scale, Erosion, Spear of Desolation, Eye of Providence, Bragi''s
    Harp, Lotus Sickle, Blood-Bound Book, Helm of Radiance, Screeching Gargoyle, Shifter''s
    Shield, Midgardian Mail, Eros'' Bow, Stone of Binding, Leviathan''s Hide, Magi''s
    Cloak, Helm of Darkness, Mantle Of Discord, Hide of the Nemean Lion, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.66
      efficiency: 0.71
      win: 0.83
      pick: 0.16
      fit: 0.2
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.55
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.53
      efficiency: 0.47
      win: 0.67
      pick: 0.0
      fit: 0.44
    Eros' Bow:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Breastplate of Valor, Shield of the Phoenix, Spear of Desolation,
    Lotus Sickle, Screeching Gargoyle, Gluttonous Grimoire, Chronos'' Pendant, Gladiator''s
    Shield, Draconic Scale, Oni Hunter''s Garb, Erosion, Eye of Providence, Helm of
    Radiance, Blood-Bound Book, Shifter''s Shield, Gem of Focus, Heartwood Charm,
    Helm of Darkness, Midgardian Mail, Chandra''s Grace, Stone of Binding, Leviathan''s
    Hide, Regrowth Striders.'
  slot_scores:
    Genji's Guard:
      total: 0.7
      efficiency: 0.71
      win: 0.83
      pick: 0.16
      fit: 0.45
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.6
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, The Reaper, Tyrfing, Runeforged Hammer, Breastplate of Valor, Spear
    of Desolation, Hydra''s Lament, Shield of the Phoenix, Golden Blade, The Crusher,
    Oni Hunter''s Garb, Draconic Scale, Heartseeker, Erosion, Eye of Providence, Death
    Metal, Tekko-Kagi, Titan''s Bane, Shifter''s Shield, Lotus Sickle, Screeching
    Gargoyle, Midgardian Mail, Bragi''s Harp, Helm of Radiance, Blood-Bound Book,
    Obsidian Shard, Stone of Binding, Avenging Blade, Nimble Ring, Leviathan''s Hide,
    Arondight, Helm of Darkness, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.66
      efficiency: 0.71
      win: 0.83
      pick: 0.16
      fit: 0.21
    Berserker's Shield:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.49
    Shield Splitter:
      total: 0.58
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Kinetic Cuirass, Soul Gem, Jotunn''s Revenge, Shield Splitter, Spear
    of Desolation, Berserker''s Shield, The Reaper, Breastplate of Valor, Lotus Sickle,
    Helm of Radiance, Blood-Bound Book, Runeforged Hammer, Shield of the Phoenix,
    Obsidian Shard, Death Metal, Oni Hunter''s Garb, Draconic Scale, Helm of Darkness,
    Hydra''s Lament, Spear of the Magus, Ancient Signet, The Crusher, Erosion, Eye
    of Providence, Polynomicon, Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Shifter''s
    Shield, Midgardian Mail, Screeching Gargoyle, Stone of Binding, Jade Scepter,
    Titan''s Bane, Leviathan''s Hide, Tyrfing, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.66
      efficiency: 0.71
      win: 0.83
      pick: 0.16
      fit: 0.21
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.49
    Shield Splitter:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.35
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Draconic Scale
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Draconic
    Scale, Gluttonous Grimoire, Shield of the Phoenix, Erosion, Breastplate of Valor,
    Soul Gem, Eye of Providence, Shifter''s Shield, Oni Hunter''s Garb, Helm of Darkness,
    Stone of Binding, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Screeching
    Gargoyle, Leviathan''s Hide, Spear of Desolation, Helm of Radiance, Hide of the
    Nemean Lion, Gladiator''s Shield, Lotus Sickle, Ancile, Blood-Bound Book, Void
    Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.68
      efficiency: 0.71
      win: 0.83
      pick: 0.16
      fit: 0.35
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.57
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.58
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
