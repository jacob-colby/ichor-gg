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
      win_rate: 0.58
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.48
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
      pick_rate: 0.13
      win_rate: 0.53
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.61
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
  last_verified: '2026-11-02'
  god_win_rate: 0.5611510791366906
  god_matches_won: 234
  god_matches_played: 417
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
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Eye of Providence
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Erosion, Eye of Providence,
    Draconic Scale, Breastplate of Valor, Shifter''s Shield, Shield of the Phoenix,
    Helm of Darkness, Oni Hunter''s Garb, Stone of Binding, Prophetic Cloak, Magi''s
    Cloak, Midgardian Mail, Mantle Of Discord, Gluttonous Grimoire, Leviathan''s Hide,
    Helm of Radiance, Screeching Gargoyle, Ancile, Spear of Desolation, Hide of the
    Nemean Lion, Void Stone, Xibalban Effigy, Void Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.81
    Draconic Scale:
      total: 0.54
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.71
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
  - Shield of the Phoenix
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
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Tahuti,
    Soul Gem, Phoenix Feather, Erosion, Eye of Providence, Draconic Scale, Ethereal
    Staff, Yogi''s Necklace, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s
    Garb, Shifter''s Shield, Gluttonous Grimoire, Glorious Pridwen, Midgardian Mail,
    Leviathan''s Hide, Helm of Darkness, Rod of Asclepius, Regrowth Striders, Stone
    of Binding, Ancile, Sphere of Negation, Hide of the Nemean Lion, Magi''s Cloak,
    Helm of Radiance.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.36
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.92
    Amanita Charm:
      total: 0.64
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Obsidian Shard, Spear of Desolation, Soul
    Gem, Void Stone, Void Shield, Breastplate of Valor, Spear of the Magus, Erosion,
    Doom Orb, Eye of Providence, Draconic Scale, The World Stone, Oni Hunter''s Garb,
    Shield of the Phoenix, Helm of Darkness, Midgardian Mail, Helm of Radiance, Shifter''s
    Shield, Magi''s Cloak, Mantle Of Discord, Dreamer''s Idol, Leviathan''s Hide.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.55
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.59
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.56
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.49
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
    Grimoire, Breastplate of Valor, Soul Gem, Eros'' Bow, Oni Hunter''s Garb, Erosion,
    Obsidian Shard, Helm of Radiance, Eye of Providence, Stone of Binding, Draconic
    Scale, Shield of the Phoenix, Midgardian Mail, Spear of Desolation, Screeching
    Gargoyle, Sundering Echo, Helm of Darkness, Magi''s Cloak, Leviathan''s Hide,
    Mantle Of Discord, Blood-Bound Book, Shifter''s Shield, Bragi''s Harp, Bracer
    of The Abyss.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.2
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.53
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.41
      win: 0.6
      pick: 0.0
      fit: 0.44
    Eros' Bow:
      total: 0.49
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spear of Desolation
  flex_slots:
  - Spear of Desolation
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Rod of Tahuti,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Prophetic Cloak, Chronos'' Pendant, Erosion, Gladiator''s
    Shield, Gluttonous Grimoire, Eye of Providence, Helm of Radiance, Helm of Darkness,
    Oni Hunter''s Garb, Draconic Scale, Obsidian Shard, Stone of Binding, Heartwood
    Charm, Gem of Focus, Chandra''s Grace, Midgardian Mail, Magi''s Cloak, Sundering
    Echo, Shifter''s Shield, Glorious Pridwen.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.58
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.46
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
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, Rod of Tahuti, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Kinetic Cuirass, Tekko-Kagi, Titan''s
    Bane, Runeforged Hammer, Breastplate of Valor, Golden Blade, Gluttonous Grimoire,
    Hydra''s Lament, Obsidian Shard, Spear of Desolation, Sundering Echo, Tyrfing,
    Soul Gem, Erosion, Heartseeker, Oni Hunter''s Garb, The Crusher, Eye of Providence,
    Lernaean Bow, Draconic Scale, Stone of Binding, Toxic Blade, Shield of the Phoenix,
    Helm of Radiance, Midgardian Mail, Avenging Blade, Pharaoh''s Curse, Helm of Darkness,
    The Reaper, Silverbranch Bow, Screeching Gargoyle, Magi''s Cloak, Spear of the
    Magus, Wyrmskin Hide, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.23
    Berserker's Shield:
      total: 0.57
      efficiency: 0.7
      win: 0.6
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.41
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
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Helm of Darkness — magical protection
    swap_item: Helm of Darkness
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Berserker''s Shield, Shield
    Splitter, Obsidian Shard, Spear of Desolation, Soul Gem, Sundering Echo, Breastplate
    of Valor, Helm of Radiance, Titan''s Bane, Runeforged Hammer, Helm of Darkness,
    Spear of the Magus, Hydra''s Lament, Erosion, Oni Hunter''s Garb, Death Metal,
    Eye of Providence, Doom Orb, Draconic Scale, Stone of Binding, Shield of the Phoenix,
    The World Stone, Heartseeker, Midgardian Mail, The Crusher, Screeching Gargoyle,
    Magi''s Cloak, Jade Scepter, Chronos'' Pendant, Mantle Of Discord, Leviathan''s
    Hide, Shifter''s Shield, Avenging Blade, The Reaper, Triton''s Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.53
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
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
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.51
      efficiency: 0.55
      win: 0.48
      pick: 0.17
      fit: 0.64
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
