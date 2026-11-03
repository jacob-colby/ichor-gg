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
  last_verified: '2026-11-03'
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
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Freya's Tears
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Draconic Scale, Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Erosion,
    Breastplate of Valor, Eye of Providence, Oni Hunter''s Garb, Helm of Darkness,
    Shield of the Phoenix, Shifter''s Shield, Stone of Binding, Helm of Radiance,
    Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Gluttonous Grimoire, Leviathan''s
    Hide, Spear of Desolation, Eros'' Bow, Ancile, Prophetic Cloak, Hide of the Nemean
    Lion, Obsidian Shard, Void Stone, Soul Gem, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.16
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
      total: 0.58
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
    Erosion:
      total: 0.52
      efficiency: 0.51
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
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Draconic Scale, Rod of Tahuti, Shield of the Phoenix,
    Kinetic Cuirass, Soul Gem, Phoenix Feather, Ethereal Staff, Erosion, Eye of Providence,
    Breastplate of Valor, Oni Hunter''s Garb, Chandra''s Grace, Gluttonous Grimoire,
    Midgardian Mail, Shifter''s Shield, Rod of Asclepius, Glorious Pridwen, Leviathan''s
    Hide, Helm of Darkness, Regrowth Striders, Eros'' Bow, Helm of Radiance, Sphere
    of Negation, Soul Locket, Stone of Binding, Spear of Desolation, Yogi''s Necklace.'
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
      efficiency: 0.5
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
  - Stone of Binding
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
    Gem, Void Stone, Void Shield, Spear of the Magus, Breastplate of Valor, Screeching
    Gargoyle, Erosion, Oni Hunter''s Garb, Eye of Providence, Doom Orb, Helm of Radiance,
    The World Stone, Helm of Darkness, Shield of the Phoenix, Midgardian Mail, Magi''s
    Cloak, Dreamer''s Idol, Mantle Of Discord, Shifter''s Shield, Leviathan''s Hide.'
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
      efficiency: 0.86
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
    Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Eros'' Bow, Oni Hunter''s
    Garb, Helm of Radiance, Erosion, Eye of Providence, Obsidian Shard, Stone of Binding,
    Spear of Desolation, Helm of Darkness, Midgardian Mail, Shield of the Phoenix,
    Magi''s Cloak, Blood-Bound Book, Leviathan''s Hide, Bragi''s Harp, Mantle Of Discord,
    Ancient Signet, Shifter''s Shield, Bracer of The Abyss, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.2
    Nimble Ring:
      total: 0.51
      efficiency: 0.63
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
      efficiency: 0.53
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
    Phoenix, Soul Gem, Lotus Sickle, Chronos'' Pendant, Helm of Radiance, Prophetic
    Cloak, Screeching Gargoyle, Oni Hunter''s Garb, Erosion, Helm of Darkness, Gluttonous
    Grimoire, Eye of Providence, Obsidian Shard, Stone of Binding, Gladiator''s Shield,
    Gem of Focus, Midgardian Mail, Magi''s Cloak, Heartwood Charm, Nimble Ring, Mantle
    Of Discord, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
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
    Hammer, Tekko-Kagi, Titan''s Bane, Golden Blade, Hydra''s Lament, Breastplate
    of Valor, Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, Tyrfing, The
    Crusher, Oni Hunter''s Garb, Soul Gem, Erosion, Lernaean Bow, Helm of Radiance,
    Avenging Blade, Eye of Providence, Heartseeker, Stone of Binding, Helm of Darkness,
    The Reaper, Shield of the Phoenix, Toxic Blade, Arondight, Midgardian Mail, Death
    Metal, Spear of the Magus, Magi''s Cloak, Pharaoh''s Curse, Silverbranch Bow,
    Wyrmskin Hide, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.23
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.55
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield,
    Jotunn''s Revenge, Draconic Scale, Amanita Charm, Shield Splitter, Kinetic Cuirass,
    Gluttonous Grimoire, Obsidian Shard, Spear of Desolation, Soul Gem, Helm of Radiance,
    Runeforged Hammer, Breastplate of Valor, Titan''s Bane, Tekko-Kagi, Helm of Darkness,
    Spear of the Magus, Golden Blade, Hydra''s Lament, Death Metal, Nimble Ring, Oni
    Hunter''s Garb, Ancient Signet, Eros'' Bow, Erosion, Tyrfing, Lotus Sickle, Eye
    of Providence, The Crusher, Doom Orb, Jade Scepter, Stone of Binding, Bragi''s
    Harp, Shield of the Phoenix, Midgardian Mail, Avenging Blade, The World Stone,
    Magi''s Cloak, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.21
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.55
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Erosion,
    Breastplate of Valor, Eye of Providence, Draconic Scale, Oni Hunter''s Garb, Helm
    of Darkness, Shield of the Phoenix, Shifter''s Shield, Stone of Binding, Helm
    of Radiance, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Gluttonous Grimoire,
    Leviathan''s Hide, Screeching Gargoyle, Spear of Desolation, Eros'' Bow, Ancile,
    Prophetic Cloak, Hide of the Nemean Lion, Obsidian Shard, Void Stone, Soul Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.16
      fit: 0.35
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
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
