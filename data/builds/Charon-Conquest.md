---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.5
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.18
    win_rate: 0.61
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.52
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.54
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.61
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.59
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.47
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.6
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.52
    - name: Ethereal Staff
      pick_rate: 0.07
      win_rate: 0.55
  - name: Rod of Tahuti
    pick_rate: 0.03
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.76
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.83
  - name: Soul Reaver
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.73
    - name: Olmec Blue
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.38
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.65
  - name: Gilded Arrow
    pick_rate: 0.07
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-11-04'
  god_win_rate: 0.5595238095238095
  god_matches_won: 235
  god_matches_played: 420
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
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Helm of Darkness — physical protection
    swap_item: Helm of Darkness
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Gluttonous Grimoire,
    Erosion, Breastplate of Valor, Eye of Providence, Soul Gem, Draconic Scale, Helm
    of Darkness, Oni Hunter''s Garb, Shield of the Phoenix, Shifter''s Shield, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Midgardian Mail, Mantle Of Discord,
    Prophetic Cloak, Leviathan''s Hide, Screeching Gargoyle, Spear of Desolation,
    Lotus Sickle, Ancile, Hide of the Nemean Lion, Obsidian Shard, Void Stone.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.35
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.74
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Eye of Providence
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Rod of Tahuti, Kinetic
    Cuirass, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather, Erosion, Yogi''s
    Necklace, Eye of Providence, Breastplate of Valor, Draconic Scale, Oni Hunter''s
    Garb, Chandra''s Grace, Midgardian Mail, Shifter''s Shield, Ethereal Staff, Glorious
    Pridwen, Rod of Asclepius, Bancroft''s Talon, Leviathan''s Hide, Helm of Darkness,
    Regrowth Striders, Helm of Radiance, Sphere of Negation, Soul Locket, Stone of
    Binding.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.32
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.72
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.92
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.62
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
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
    for this god: Rod of Tahuti, Gluttonous Grimoire, Soul Gem, Amanita Charm, Stone
    of Binding, Kinetic Cuirass, Spear of Desolation, Screeching Gargoyle, Obsidian
    Shard, Void Stone, Void Shield, Spear of the Magus, Breastplate of Valor, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Doom Orb, Helm of Radiance, Draconic Scale,
    The World Stone, Helm of Darkness, Shield of the Phoenix, Midgardian Mail, Magi''s
    Cloak, Lotus Sickle, Dreamer''s Idol, Mantle Of Discord, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.55
      pick: 0.06
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
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
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Eros'' Bow, Oni Hunter''s Garb, Helm
    of Radiance, Erosion, Lotus Sickle, Eye of Providence, Obsidian Shard, Stone of
    Binding, Spear of Desolation, Helm of Darkness, Midgardian Mail, Draconic Scale,
    Shield of the Phoenix, Magi''s Cloak, Screeching Gargoyle, Blood-Bound Book, Leviathan''s
    Hide, Bragi''s Harp, Mantle Of Discord, Ancient Signet, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.2
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.54
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.45
      win: 0.6
      pick: 0.0
      fit: 0.44
    Eros' Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
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
  - Spear of Desolation
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Lotus Sickle
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
    Gem, Breastplate of Valor, Kinetic Cuirass, Lotus Sickle, Spear of Desolation,
    Gluttonous Grimoire, Shield of the Phoenix, Screeching Gargoyle, Prophetic Cloak,
    Chronos'' Pendant, Helm of Radiance, Oni Hunter''s Garb, Erosion, Helm of Darkness,
    Eye of Providence, Obsidian Shard, Draconic Scale, Stone of Binding, Gladiator''s
    Shield, Gem of Focus, Midgardian Mail, Heartwood Charm, Magi''s Cloak, Blood-Bound
    Book, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.45
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.42
    Lotus Sickle:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.49
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Genji's Guard
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
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Gluttonous Grimoire, Kinetic Cuirass,
    Soul Gem, Runeforged Hammer, The Reaper, Tekko-Kagi, Titan''s Bane, Golden Blade,
    Breastplate of Valor, Hydra''s Lament, Nimble Ring, Obsidian Shard, Spear of Desolation,
    Tyrfing, The Crusher, Oni Hunter''s Garb, Helm of Radiance, Lernaean Bow, Erosion,
    Avenging Blade, Eye of Providence, Heartseeker, Lotus Sickle, Stone of Binding,
    Draconic Scale, Helm of Darkness, Shield of the Phoenix, Midgardian Mail, Arondight,
    Spear of the Magus, Death Metal, Magi''s Cloak, Toxic Blade, Screeching Gargoyle,
    Pharaoh''s Curse.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.21
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.6
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.6
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.49
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Gluttonous Grimoire
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    Jotunn''s Revenge, Amanita Charm, Soul Gem, Shield Splitter, Berserker''s Shield,
    Kinetic Cuirass, Obsidian Shard, Spear of Desolation, Helm of Radiance, Runeforged
    Hammer, Breastplate of Valor, The Reaper, Lotus Sickle, Titan''s Bane, Helm of
    Darkness, Spear of the Magus, Hydra''s Lament, Blood-Bound Book, Death Metal,
    Oni Hunter''s Garb, Ancient Signet, Erosion, Eye of Providence, The Crusher, Doom
    Orb, Jade Scepter, Stone of Binding, Draconic Scale, Shield of the Phoenix, Midgardian
    Mail, Avenging Blade, The World Stone, Magi''s Cloak, Chronos'' Pendant, Heartseeker,
    Screeching Gargoyle, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.21
    Berserker's Shield:
      total: 0.54
      efficiency: 0.67
      win: 0.6
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.6
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.49
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Genji's Guard
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
    Of Discord, Leviathan''s Hide, Screeching Gargoyle, Spear of Desolation, Lotus
    Sickle, Ancile, Prophetic Cloak, Hide of the Nemean Lion, Obsidian Shard, Void
    Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.35
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.51
      efficiency: 0.58
      win: 0.47
      pick: 0.19
      fit: 0.57
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
