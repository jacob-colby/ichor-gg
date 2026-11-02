---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.26
  aspect_win_rate: 0.52
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.33
    win_rate: 0.53
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.17
      win_rate: 0.45
    - name: Chronos' Pendant
      pick_rate: 0.11
      win_rate: 0.53
  - name: Stampede
    pick_rate: 0.1
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.38
    - name: Soul Gem
      pick_rate: 0.07
      win_rate: 0.54
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.46
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.29
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.48
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.66
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.56
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.6
  - name: Obsidian Shard
    pick_rate: 0.05
    win_rate: 0.71
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.62
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.44
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.69
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.29
    - name: Engraved Guard
      pick_rate: 0.04
      win_rate: 0.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.43
    win_rate: 0.41
  - name: Bluestone Brooch
    pick_rate: 0.31
    win_rate: 0.54
  - name: War Banner
    pick_rate: 0.09
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-11-02'
  god_win_rate: 0.4852941176470588
  god_matches_won: 165
  god_matches_played: 340
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Obsidian Shard, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Erosion, Stampede, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Helm of Darkness, Gluttonous Grimoire, Soul Gem, Shifter''s Shield, Oni
    Hunter''s Garb, Helm of Radiance, Stone of Binding, Screeching Gargoyle, Magi''s
    Cloak, Midgardian Mail, Mantle Of Discord, Prophetic Cloak, Leviathan''s Hide,
    Ancile, Hide of the Nemean Lion, Gladiator''s Shield, Void Stone, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.73
    Spear of Desolation:
      total: 0.5
      efficiency: 0.56
      win: 0.53
      pick: 0.33
      fit: 0.37
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.71
      pick: 0.11
      fit: 0.3
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.6
      pick: 0.13
      fit: 0.2
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.54
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
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
    this god: Amanita Charm, Rod of Tahuti, Obsidian Shard, Shield of the Phoenix,
    Soul Gem, Kinetic Cuirass, Ethereal Staff, Phoenix Feather, Breastplate of Valor,
    Chandra''s Grace, Yogi''s Necklace, Gluttonous Grimoire, Erosion, Eye of Providence,
    Draconic Scale, Glorious Pridwen, Oni Hunter''s Garb, Rod of Asclepius, Helm of
    Darkness, Shifter''s Shield, Regrowth Striders, Sphere of Negation, Midgardian
    Mail, Helm of Radiance, Blood-Bound Book, Leviathan''s Hide, Screeching Gargoyle,
    Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.9
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.71
      pick: 0.11
      fit: 0.31
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.6
      pick: 0.13
      fit: 0.21
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.54
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Obsidian Shard, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Void Stone,
    Void Shield, Breastplate of Valor, Spear of the Magus, Doom Orb, The World Stone,
    Erosion, Shield of the Phoenix, Helm of Darkness, Helm of Radiance, Eye of Providence,
    Oni Hunter''s Garb, Draconic Scale, Dreamer''s Idol, Midgardian Mail, Magi''s
    Cloak, Shifter''s Shield, Mantle Of Discord, Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.68
    Stone of Binding:
      total: 0.51
      efficiency: 0.47
      win: 0.54
      pick: 0.0
      fit: 0.72
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.53
      pick: 0.33
      fit: 0.55
    Obsidian Shard:
      total: 0.6
      efficiency: 0.55
      win: 0.71
      pick: 0.11
      fit: 0.53
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.81
      win: 0.6
      pick: 0.13
      fit: 0.43
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.54
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Obsidian Shard
  - Rod of Tahuti
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
    this god: Rod of Tahuti, Obsidian Shard, Amanita Charm, Nimble Ring, Soul Gem,
    Gluttonous Grimoire, Kinetic Cuirass, Breastplate of Valor, Eros'' Bow, Helm of
    Radiance, Oni Hunter''s Garb, Sundering Echo, Erosion, Shield of the Phoenix,
    Screeching Gargoyle, Helm of Darkness, Stone of Binding, Eye of Providence, Blood-Bound
    Book, Draconic Scale, Midgardian Mail, Magi''s Cloak, Bragi''s Harp, Leviathan''s
    Hide, Chronos'' Pendant, Mantle Of Discord, Bracer of The Abyss, Genji''s Guard.'
  slot_scores:
    Nimble Ring:
      total: 0.5
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.45
      efficiency: 0.41
      win: 0.54
      pick: 0.0
      fit: 0.46
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.71
      pick: 0.11
      fit: 0.21
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.81
      win: 0.6
      pick: 0.13
      fit: 0.11
    Eros' Bow:
      total: 0.47
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.62
      win: 0.54
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Obsidian Shard, Breastplate
    of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Screeching
    Gargoyle, Chronos'' Pendant, Prophetic Cloak, Erosion, Gladiator''s Shield, Gluttonous
    Grimoire, Eye of Providence, Helm of Radiance, Helm of Darkness, Oni Hunter''s
    Garb, Draconic Scale, Stone of Binding, Heartwood Charm, Gem of Focus, Chandra''s
    Grace, Midgardian Mail, Magi''s Cloak, Sundering Echo, Shifter''s Shield, Glorious
    Pridwen, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.33
      fit: 0.46
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.71
      pick: 0.11
      fit: 0.23
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.81
      win: 0.6
      pick: 0.13
      fit: 0.13
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Obsidian Shard, Berserker''s
    Shield, Jotunn''s Revenge, Amanita Charm, Shield Splitter, Kinetic Cuirass, Breastplate
    of Valor, Soul Gem, Titan''s Bane, Gluttonous Grimoire, Tekko-Kagi, Runeforged
    Hammer, Hydra''s Lament, Golden Blade, Sundering Echo, Tyrfing, Helm of Radiance,
    Heartseeker, Erosion, Oni Hunter''s Garb, Shield of the Phoenix, The Crusher,
    Helm of Darkness, Lernaean Bow, Eye of Providence, Screeching Gargoyle, Spear
    of the Magus, Draconic Scale, Stone of Binding, Nimble Ring, Toxic Blade, Midgardian
    Mail, Death Metal, Avenging Blade, Arondight, Pharaoh''s Curse, Silverbranch Bow,
    The Reaper, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.7
      win: 0.54
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.45
    Shield Splitter:
      total: 0.5
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.48
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.71
      pick: 0.11
      fit: 0.33
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.6
      pick: 0.13
      fit: 0.23
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.54
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Obsidian Shard, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Berserker''s Shield, Soul Gem, Gluttonous
    Grimoire, Shield Splitter, Breastplate of Valor, Sundering Echo, Helm of Radiance,
    Titan''s Bane, Runeforged Hammer, Helm of Darkness, Hydra''s Lament, Spear of
    the Magus, Erosion, Shield of the Phoenix, Oni Hunter''s Garb, Death Metal, Chronos''
    Pendant, Eye of Providence, Doom Orb, Draconic Scale, Screeching Gargoyle, Stone
    of Binding, The World Stone, Heartseeker, Midgardian Mail, The Crusher, Magi''s
    Cloak, Jade Scepter, Mantle Of Discord, Leviathan''s Hide, Shifter''s Shield,
    Avenging Blade, Arondight, The Reaper, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.33
      fit: 0.42
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.11
      fit: 0.42
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.6
      pick: 0.13
      fit: 0.32
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.54
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Genji''s
    Guard, Breastplate of Valor, Erosion, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Helm of Darkness, Gluttonous Grimoire, Shifter''s Shield, Oni
    Hunter''s Garb, Helm of Radiance, Stone of Binding, Screeching Gargoyle, Magi''s
    Cloak, Soul Gem, Midgardian Mail, Mantle Of Discord, Prophetic Cloak, Obsidian
    Shard, Leviathan''s Hide, Ancile, Hide of the Nemean Lion, Gladiator''s Shield,
    Void Stone, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.43
      efficiency: 0.66
      win: 0.29
      pick: 0.12
      fit: 0.39
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.5
      efficiency: 0.55
      win: 0.46
      pick: 0.17
      fit: 0.62
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.6
      pick: 0.13
      fit: 0.2
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.54
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shell of Rebuke
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Genji''s Guard, Breastplate of Valor, Erosion, Eye of Providence, Shield
    of the Phoenix, Draconic Scale, Helm of Darkness, Gluttonous Grimoire, Shifter''s
    Shield, Oni Hunter''s Garb, Helm of Radiance, Stone of Binding, Screeching Gargoyle,
    Magi''s Cloak, Soul Gem, Midgardian Mail, Mantle Of Discord, Prophetic Cloak,
    Obsidian Shard, Leviathan''s Hide, Ancile, Hide of the Nemean Lion, Gladiator''s
    Shield, Void Stone, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.43
      efficiency: 0.66
      win: 0.29
      pick: 0.12
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.73
    Shell of Rebuke:
      total: 0.47
      efficiency: 0.27
      win: 0.66
      pick: 0.18
      fit: 0.45
    Freya's Tears:
      total: 0.5
      efficiency: 0.55
      win: 0.46
      pick: 0.17
      fit: 0.62
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.6
      pick: 0.13
      fit: 0.2
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.54
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Rod of Tahuti
  swaps:
  - added: Shell of Rebuke
    removed: Breastplate of Valor
    reason: community 66% win over 37 matches (vs 49% on this god), taking the model's
      weakest slot from Breastplate of Valor
  starter: *id001
---
