---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.33
  aspect_win_rate: 0.43
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.39
    win_rate: 0.46
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.18
      win_rate: 0.47
    - name: Chronos' Pendant
      pick_rate: 0.11
      win_rate: 0.5
  - name: Soul Gem
    pick_rate: 0.14
    win_rate: 0.4
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.43
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.12
    win_rate: 0.58
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.89
    - name: Talisman of Purification
      pick_rate: 0.07
      win_rate: 0.43
  - name: Spirit Robe
    pick_rate: 0.1
    win_rate: 0.33
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.6
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.5
  - name: Sage's Ring
    pick_rate: 0.12
    win_rate: 0.83
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.0
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.42
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.36
    win_rate: 0.42
  - name: Archmage's Gem
    pick_rate: 0.05
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-10-25'
  god_win_rate: 0.49523809523809526
  god_matches_won: 52
  god_matches_played: 105
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-25'
  god_matches_analyzed: 4936
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Kinetic Cuirass, Shifter''s Shield, Breastplate
    of Valor, Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Helm
    of Radiance, Gluttonous Grimoire, Stone of Binding, Magi''s Cloak, Screeching
    Gargoyle, Mantle Of Discord, Helm of Darkness, Rod of Asclepius, Prophetic Cloak,
    Midgardian Mail, Hide of the Nemean Lion, Spear of the Magus, Leviathan''s Hide,
    Void Shield, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.12
      fit: 0.39
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.73
    Shell of Rebuke:
      total: 0.58
      efficiency: 0.28
      win: 0.89
      pick: 0.15
      fit: 0.45
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.2
      fit: 0.2
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.6
      pick: 0.13
      fit: 0.3
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shell of Rebuke
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Genji''s Guard,
    Rod of Asclepius, Shifter''s Shield, Breastplate of Valor, Ethereal Staff, Gluttonous
    Grimoire, Erosion, Eye of Providence, Draconic Scale, Chandra''s Grace, Lifebinder,
    Phoenix Feather, Yogi''s Necklace, Glorious Pridwen, Helm of Radiance, Sphere
    of Negation, Stone of Binding, Midgardian Mail, Screeching Gargoyle, Jade Scepter,
    Wish-Granting Pearl, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.12
      fit: 0.36
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.9
    Shell of Rebuke:
      total: 0.56
      efficiency: 0.28
      win: 0.89
      pick: 0.15
      fit: 0.38
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.2
      fit: 0.21
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Shell of Rebuke
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Obsidian Shard, Amanita Charm, Genji''s Guard, Gluttonous Grimoire,
    Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Spear of the Magus, Breastplate
    of Valor, Void Shield, Void Stone, Shifter''s Shield, Doom Orb, Helm of Radiance,
    Erosion, Shield of the Phoenix, Eye of Providence, The World Stone, Chronos''
    Pendant, Draconic Scale, Dreamer''s Idol, Magi''s Cloak, Rod of Asclepius, Mantle
    Of Discord, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.12
      fit: 0.28
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.46
      pick: 0.39
      fit: 0.55
    Shell of Rebuke:
      total: 0.56
      efficiency: 0.28
      win: 0.89
      pick: 0.15
      fit: 0.32
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.2
      fit: 0.43
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.6
      pick: 0.13
      fit: 0.53
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Shell of Rebuke
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Shell of Rebuke
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Obsidian Shard, Genji''s Guard, Amanita Charm, Nimble Ring, Gluttonous
    Grimoire, Kinetic Cuirass, Breastplate of Valor, Shifter''s Shield, Helm of Radiance,
    Chronos'' Pendant, Shield of the Phoenix, Erosion, Stone of Binding, Eye of Providence,
    Spear of the Magus, Draconic Scale, Screeching Gargoyle, Rod of Asclepius, Bragi''s
    Harp, Magi''s Cloak, Daybreak Gavel, Bracer of The Abyss, Midgardian Mail, Mantle
    Of Discord, Jade Scepter.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.32
    Shell of Rebuke:
      total: 0.54
      efficiency: 0.28
      win: 0.89
      pick: 0.15
      fit: 0.24
    Bragi's Harp:
      total: 0.44
      efficiency: 0.44
      win: 0.47
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.58
      pick: 0.2
      fit: 0.11
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.6
      pick: 0.13
      fit: 0.21
  community_ordered:
  - Shell of Rebuke
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Shell of Rebuke
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Chronos'' Pendant, Screeching
    Gargoyle, Shifter''s Shield, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous
    Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.12
      fit: 0.48
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.48
    Shell of Rebuke:
      total: 0.56
      efficiency: 0.28
      win: 0.89
      pick: 0.15
      fit: 0.32
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.43
      pick: 0.2
      fit: 0.64
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.58
      pick: 0.2
      fit: 0.13
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shell of Rebuke
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Obsidian Shard, Berserker''s
    Shield, Amanita Charm, Genji''s Guard, Kinetic Cuirass, Breastplate of Valor,
    Shield Splitter, Runeforged Hammer, Gluttonous Grimoire, Golden Blade, Hydra''s
    Lament, Shifter''s Shield, Eye of the Storm, Heartseeker, Spear of the Magus,
    Helm of Radiance, Lernaean Bow, Tyrfing, Shield of the Phoenix, Erosion, Eye of
    Providence, Avenging Blade, Nimble Ring, Tekko-Kagi, Stone of Binding, Draconic
    Scale, Titan''s Bane, The Crusher, Screeching Gargoyle, Pharaoh''s Curse, Rod
    of Asclepius, Magi''s Cloak, Silverbranch Bow, Bragi''s Harp, The Reaper, Daybreak
    Gavel, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.45
    Shell of Rebuke:
      total: 0.55
      efficiency: 0.28
      win: 0.89
      pick: 0.15
      fit: 0.27
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.2
      fit: 0.23
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.6
      pick: 0.13
      fit: 0.33
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Shell of Rebuke
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Shell of Rebuke
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Obsidian Shard, Jotunn''s Revenge,
    Amanita Charm, Genji''s Guard, Kinetic Cuirass, Gluttonous Grimoire, Breastplate
    of Valor, Shield Splitter, Spear of the Magus, Runeforged Hammer, Helm of Radiance,
    Shifter''s Shield, Chronos'' Pendant, Berserker''s Shield, Hydra''s Lament, Eye
    of the Storm, Rod of Asclepius, Heartseeker, Shield of the Phoenix, Erosion, Eye
    of Providence, Stone of Binding, Draconic Scale, Jade Scepter, Doom Orb, Death
    Metal, Wish-Granting Pearl, Avenging Blade, Screeching Gargoyle, Magi''s Cloak,
    The World Stone, Titan''s Bane, Helm of Darkness, Ancient Signet, The Crusher,
    Mantle Of Discord, Daybreak Gavel, Dreamer''s Idol.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.42
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.17
    Shell of Rebuke:
      total: 0.55
      efficiency: 0.28
      win: 0.89
      pick: 0.15
      fit: 0.29
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.2
      fit: 0.32
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.6
      pick: 0.13
      fit: 0.42
  community_ordered:
  - Shell of Rebuke
  - Rod of Tahuti
  - Obsidian Shard
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
  - Shifter's Shield
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Genji''s Guard, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Helm of Radiance, Gluttonous Grimoire, Stone of Binding, Magi''s
    Cloak, Screeching Gargoyle, Mantle Of Discord, Helm of Darkness, Rod of Asclepius,
    Prophetic Cloak, Midgardian Mail, Hide of the Nemean Lion, Spear of the Magus,
    Leviathan''s Hide, Void Shield, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.12
      fit: 0.39
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.43
      pick: 0.2
      fit: 0.62
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
