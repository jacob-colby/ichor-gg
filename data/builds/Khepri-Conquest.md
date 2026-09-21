---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.7
  aspect_win_rate: 0.51
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.24
    win_rate: 0.55
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.15
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.56
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.41
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.62
  - name: Stampede
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.6
    - name: Omen Drum
      pick_rate: 0.08
      win_rate: 0.53
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.73
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.65
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.68
    alternates:
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.55
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.7
  community_starters:
  - name: Selflessness
    pick_rate: 0.34
    win_rate: 0.49
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.42
  - name: Bluestone Brooch
    pick_rate: 0.16
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-09-21'
  god_win_rate: 0.5104166666666666
  god_matches_won: 245
  god_matches_played: 480
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-21'
  god_matches_analyzed: 15551
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
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
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Breastplate of Valor, Rod of Tahuti, Kinetic Cuirass,
    Shifter''s Shield, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Screeching Gargoyle, Midgardian Mail, Prophetic Cloak, Hide of the
    Nemean Lion, Leviathan''s Hide, Helm of Darkness, Void Shield, Spear of Desolation,
    Ancile, Oni Hunter''s Garb, Gladiator''s Shield, Xibalban Effigy, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.25
      fit: 0.4
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.12
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.8
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.7
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Breastplate of
    Valor, Kinetic Cuirass, Rod of Asclepius, Shifter''s Shield, Soul Gem, Erosion,
    Eye of Providence, Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix
    Feather, Yogi''s Necklace, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian
    Mail, Stone of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Ancile, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.25
      fit: 0.37
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.12
      fit: 0.37
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.93
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.98
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Breastplate of Valor
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Breastplate of Valor, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Soul Gem, Spear of the Magus, Void Shield, Obsidian Shard, Void Stone, Shifter''s
    Shield, Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Doom
    Orb, Helm of Radiance, The World Stone, Magi''s Cloak, Dreamer''s Idol, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.68
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.75
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.12
      fit: 0.28
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Breastplate of Valor, Amanita Charm, Nimble Ring, Kinetic
    Cuirass, Gluttonous Grimoire, Shifter''s Shield, Soul Gem, Helm of Radiance, Erosion,
    Shield of the Phoenix, Stone of Binding, Eye of Providence, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Spear of Desolation, Spear of the Magus, Daybreak
    Gavel, Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer
    of The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.62
      pick: 0.12
      fit: 0.21
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.55
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Shield of the Phoenix
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Rod of Tahuti,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion,
    Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius,
    Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.25
      fit: 0.48
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.62
      pick: 0.12
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.13
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Breastplate
    of Valor, Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Golden Blade, Runeforged Hammer, Shifter''s Shield, Gluttonous Grimoire, Eye of
    the Storm, Tyrfing, Hydra''s Lament, Heartseeker, Spear of Desolation, Lernaean
    Bow, Spear of the Magus, Erosion, Silverbranch Bow, Tekko-Kagi, Eye of Providence,
    Soul Gem, Shield of the Phoenix, Avenging Blade, Helm of Radiance, Stone of Binding,
    Draconic Scale, Toxic Blade, Obsidian Shard, Titan''s Bane, The Crusher, Pharaoh''s
    Curse, Nimble Ring, Magi''s Cloak, The Reaper, Screeching Gargoyle, Shogun''s
    Ofuda, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.62
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Spear
    of Desolation, Shield Splitter, Spear of the Magus, Soul Gem, Runeforged Hammer,
    Helm of Radiance, Shifter''s Shield, Obsidian Shard, Berserker''s Shield, Eye
    of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of
    Providence, Shield of the Phoenix, Stone of Binding, Draconic Scale, Doom Orb,
    Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Chronos'' Pendant,
    Magi''s Cloak, The World Stone, Helm of Darkness, Titan''s Bane, Screeching Gargoyle,
    Ancient Signet, The Crusher, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.18
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.62
      pick: 0.12
      fit: 0.24
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.18
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Breastplate of Valor
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
    Grimoire, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Prophetic Cloak,
    Hide of the Nemean Lion, Leviathan''s Hide, Helm of Darkness, Void Shield, Stampede,
    Spear of Desolation, Ancile, Oni Hunter''s Garb, Gladiator''s Shield, Xibalban
    Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.25
      fit: 0.4
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.12
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.41
      pick: 0.19
      fit: 0.65
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
---
