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
  last_verified: '2026-11-02'
  god_win_rate: 0.5584725536992841
  god_matches_won: 234
  god_matches_played: 419
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
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Amanita Charm
  - Erosion
  flex_slots:
  - Eye of Providence
  - Breastplate of Valor
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
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Erosion, Eye of Providence,
    Breastplate of Valor, Draconic Scale, Helm of Darkness, Shifter''s Shield, Shield
    of the Phoenix, Stone of Binding, Oni Hunter''s Garb, Magi''s Cloak, Prophetic
    Cloak, Midgardian Mail, Helm of Radiance, Mantle Of Discord, Gluttonous Grimoire,
    Leviathan''s Hide, Screeching Gargoyle, Spear of Desolation, Ancile, Hide of the
    Nemean Lion, Void Stone, Void Shield, Xibalban Effigy.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.39
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.81
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.51
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
    Soul Gem, Phoenix Feather, Erosion, Eye of Providence, Draconic Scale, Breastplate
    of Valor, Yogi''s Necklace, Chandra''s Grace, Shifter''s Shield, Oni Hunter''s
    Garb, Gluttonous Grimoire, Midgardian Mail, Glorious Pridwen, Helm of Darkness,
    Ethereal Staff, Leviathan''s Hide, Rod of Asclepius, Stone of Binding, Helm of
    Radiance, Sphere of Negation, Regrowth Striders, Spear of Desolation, Magi''s
    Cloak.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.36
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.92
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
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
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Spear of Desolation, Screeching Gargoyle, Obsidian Shard, Soul
    Gem, Void Stone, Void Shield, Spear of the Magus, Breastplate of Valor, Erosion,
    Eye of Providence, Doom Orb, Draconic Scale, The World Stone, Helm of Radiance,
    Helm of Darkness, Oni Hunter''s Garb, Shield of the Phoenix, Magi''s Cloak, Midgardian
    Mail, Dreamer''s Idol, Shifter''s Shield, Mantle Of Discord.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.55
      pick: 0.06
      fit: 0.41
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.49
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
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Helm of Radiance, Eros'' Bow, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Stone of Binding, Obsidian Shard, Spear
    of Desolation, Helm of Darkness, Draconic Scale, Midgardian Mail, Shield of the
    Phoenix, Magi''s Cloak, Screeching Gargoyle, Blood-Bound Book, Bragi''s Harp,
    Mantle Of Discord, Leviathan''s Hide, Shifter''s Shield, Bracer of The Abyss.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.2
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.54
      efficiency: 0.64
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
      total: 0.5
      efficiency: 0.52
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
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Breastplate
    of Valor, Kinetic Cuirass, Spear of Desolation, Shield of the Phoenix, Screeching
    Gargoyle, Soul Gem, Prophetic Cloak, Chronos'' Pendant, Helm of Radiance, Helm
    of Darkness, Erosion, Eye of Providence, Gluttonous Grimoire, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Oni Hunter''s Garb, Gem of Focus, Obsidian Shard,
    Heartwood Charm, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Shifter''s
    Shield, Chandra''s Grace.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.58
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
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
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Kinetic Cuirass, Runeforged Hammer, Tekko-Kagi,
    Titan''s Bane, Golden Blade, Breastplate of Valor, Hydra''s Lament, Gluttonous
    Grimoire, Spear of Desolation, Obsidian Shard, Tyrfing, The Crusher, Soul Gem,
    Lernaean Bow, Heartseeker, Erosion, Helm of Radiance, Avenging Blade, Eye of Providence,
    Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Helm of Darkness, Arondight,
    The Reaper, Shield of the Phoenix, Midgardian Mail, Death Metal, Magi''s Cloak,
    Toxic Blade, Spear of the Magus, Screeching Gargoyle, Pharaoh''s Curse, Mantle
    Of Discord, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.23
    Berserker's Shield:
      total: 0.58
      efficiency: 0.75
      win: 0.6
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
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
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Helm of Darkness — magical protection
    swap_item: Helm of Darkness
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Shield Splitter, Berserker''s Shield, Kinetic Cuirass, Gluttonous
    Grimoire, Spear of Desolation, Obsidian Shard, Soul Gem, Helm of Radiance, Breastplate
    of Valor, Runeforged Hammer, Helm of Darkness, Titan''s Bane, Spear of the Magus,
    Hydra''s Lament, Death Metal, Erosion, Eye of Providence, Doom Orb, The Crusher,
    Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Jade Scepter, Heartseeker,
    Shield of the Phoenix, The World Stone, Midgardian Mail, Avenging Blade, Magi''s
    Cloak, Chronos'' Pendant, Screeching Gargoyle, Mantle Of Discord, Arondight, The
    Reaper, Leviathan''s Hide, Shifter''s Shield, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.23
    Berserker's Shield:
      total: 0.54
      efficiency: 0.67
      win: 0.6
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.52
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Erosion,
    Eye of Providence, Breastplate of Valor, Draconic Scale, Helm of Darkness, Shifter''s
    Shield, Shield of the Phoenix, Stone of Binding, Oni Hunter''s Garb, Magi''s Cloak,
    Midgardian Mail, Helm of Radiance, Mantle Of Discord, Gluttonous Grimoire, Leviathan''s
    Hide, Screeching Gargoyle, Prophetic Cloak, Spear of Desolation, Ancile, Hide
    of the Nemean Lion, Void Stone, Void Shield, Xibalban Effigy.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.52
      efficiency: 0.58
      win: 0.47
      pick: 0.19
      fit: 0.64
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
