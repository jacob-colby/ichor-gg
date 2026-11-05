---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.33
  slot_order:
  - name: Stampede
    pick_rate: 0.23
    win_rate: 0.42
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.18
      win_rate: 0.53
    - name: Leviathan's Hide
      pick_rate: 0.12
      win_rate: 0.42
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.41
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.47
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.46
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.38
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.46
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.42
  - name: Sage's Ring
    pick_rate: 0.04
    win_rate: 0.25
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.48
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.59
    alternates:
    - name: Sage's Ring
      pick_rate: 0.04
      win_rate: 0.45
    - name: Shell of Rebuke
      pick_rate: 0.03
      win_rate: 0.38
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.54
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.47
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-11-04'
  god_win_rate: 0.44493392070484583
  god_matches_won: 202
  god_matches_played: 454
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Draconic Scale, Gluttonous
    Grimoire, Shield of the Phoenix, Erosion, Breastplate of Valor, Soul Gem, Eye
    of Providence, Shifter''s Shield, Oni Hunter''s Garb, Helm of Darkness, Stone
    of Binding, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Screeching Gargoyle,
    Spear of Desolation, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide,
    Gladiator''s Shield, Lotus Sickle, Ancile, Prophetic Cloak, Blood-Bound Book,
    Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.41
      pick: 0.16
      fit: 0.35
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.48
      pick: 0.25
      fit: 0.57
    Draconic Scale:
      total: 0.48
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.47
      efficiency: 0.51
      win: 0.44
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
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
  - Genji's Guard
  - Draconic Scale
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
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Rod
    of Tahuti, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather, Draconic Scale,
    Yogi''s Necklace, Ethereal Staff, Erosion, Oni Hunter''s Garb, Eye of Providence,
    Chandra''s Grace, Breastplate of Valor, Shifter''s Shield, Midgardian Mail, Bancroft''s
    Talon, Rod of Asclepius, Regrowth Striders, Glorious Pridwen, Soul Locket, Hide
    of the Nemean Lion, Spear of Desolation, Leviathan''s Hide, Gladiator''s Shield,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.41
      pick: 0.16
      fit: 0.32
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.44
      pick: 0.0
      fit: 0.85
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.48
      pick: 0.25
      fit: 0.51
    Draconic Scale:
      total: 0.48
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.44
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
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic
    Cuirass, Screeching Gargoyle, Spear of Desolation, Stone of Binding, Void Stone,
    Void Shield, Obsidian Shard, Breastplate of Valor, Shield of the Phoenix, Draconic
    Scale, Spear of the Magus, Oni Hunter''s Garb, Erosion, Eye of Providence, Dreamer''s
    Idol, Shifter''s Shield, Midgardian Mail, Helm of Radiance, Doom Orb, Lotus Sickle,
    Helm of Darkness, Blood-Bound Book, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.48
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.65
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.48
      pick: 0.25
      fit: 0.41
    Spear of Desolation:
      total: 0.48
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.82
      win: 0.44
      pick: 0.0
      fit: 0.38
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Breastplate of Valor, Soul Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s
    Garb, Draconic Scale, Erosion, Spear of Desolation, Eye of Providence, Bragi''s
    Harp, Lotus Sickle, Blood-Bound Book, Helm of Radiance, Screeching Gargoyle, Shifter''s
    Shield, Midgardian Mail, Eros'' Bow, Stone of Binding, Magi''s Cloak, Helm of
    Darkness, Mantle Of Discord, Hide of the Nemean Lion, Ancient Signet, Leviathan''s
    Hide.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.44
      efficiency: 0.57
      win: 0.44
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.43
      efficiency: 0.47
      win: 0.44
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.48
      pick: 0.25
      fit: 0.33
    Eros' Bow:
      total: 0.43
      efficiency: 0.5
      win: 0.44
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.49
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Freya's Tears
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
    Shield, Draconic Scale, Oni Hunter''s Garb, Prophetic Cloak, Erosion, Eye of Providence,
    Helm of Radiance, Blood-Bound Book, Shifter''s Shield, Gem of Focus, Heartwood
    Charm, Helm of Darkness, Midgardian Mail, Chandra''s Grace, Stone of Binding,
    Regrowth Striders, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.41
      pick: 0.16
      fit: 0.45
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.48
      pick: 0.25
      fit: 0.6
    Spear of Desolation:
      total: 0.47
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.49
      efficiency: 0.58
      win: 0.44
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
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, Tyrfing, The Reaper, Golden Blade, Runeforged Hammer, Breastplate of
    Valor, Spear of Desolation, Hydra''s Lament, Shield of the Phoenix, The Crusher,
    Oni Hunter''s Garb, Draconic Scale, Heartseeker, Erosion, Eye of Providence, Death
    Metal, Tekko-Kagi, Titan''s Bane, Shifter''s Shield, Lotus Sickle, Screeching
    Gargoyle, Midgardian Mail, Bragi''s Harp, Helm of Radiance, Blood-Bound Book,
    Obsidian Shard, Stone of Binding, Toxic Blade, Avenging Blade, Nimble Ring, Arondight,
    Helm of Darkness, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.71
      win: 0.41
      pick: 0.16
      fit: 0.21
    Berserker's Shield:
      total: 0.5
      efficiency: 0.72
      win: 0.44
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.48
      pick: 0.25
      fit: 0.35
    Amanita Charm:
      total: 0.49
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Freya's Tears
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
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
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
    of Providence, Polynomicon, Heartseeker, Dreamer''s Idol, Tyrfing, Chronos'' Pendant,
    Shifter''s Shield, Midgardian Mail, Screeching Gargoyle, Stone of Binding, Jade
    Scepter, Titan''s Bane, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.71
      win: 0.41
      pick: 0.16
      fit: 0.21
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.49
    Shield Splitter:
      total: 0.47
      efficiency: 0.58
      win: 0.44
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.48
      pick: 0.25
      fit: 0.35
    Amanita Charm:
      total: 0.49
      efficiency: 0.68
      win: 0.44
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
    Nemean Lion, Gladiator''s Shield, Lotus Sickle, Ancile, Prophetic Cloak, Blood-Bound
    Book, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.41
      pick: 0.16
      fit: 0.35
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.44
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.48
      pick: 0.25
      fit: 0.57
    Draconic Scale:
      total: 0.48
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.47
      efficiency: 0.51
      win: 0.44
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
