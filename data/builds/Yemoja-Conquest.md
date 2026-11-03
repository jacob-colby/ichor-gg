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
  last_verified: '2026-11-03'
  god_win_rate: 0.4852941176470588
  god_matches_won: 165
  god_matches_played: 340
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
    swap: Helm of Darkness — physical protection
    swap_item: Helm of Darkness
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Obsidian Shard, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Erosion, Helm of Darkness, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Helm of Radiance, Oni Hunter''s Garb, Soul Gem, Gluttonous Grimoire,
    Shifter''s Shield, Stone of Binding, Magi''s Cloak, Screeching Gargoyle, Midgardian
    Mail, Mantle Of Discord, Leviathan''s Hide, Prophetic Cloak, Lotus Sickle, Chronos''
    Pendant, Ancile, Jade Scepter, Hide of the Nemean Lion, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.73
    Spear of Desolation:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.33
      fit: 0.37
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.3
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.2
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
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
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Rod of Tahuti, Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic
    Cuirass, Ethereal Staff, Phoenix Feather, Breastplate of Valor, Erosion, Gluttonous
    Grimoire, Yogi''s Necklace, Chandra''s Grace, Eye of Providence, Draconic Scale,
    Oni Hunter''s Garb, Rod of Asclepius, Helm of Darkness, Glorious Pridwen, Helm
    of Radiance, Regrowth Striders, Sphere of Negation, Soul Locket, Blood-Bound Book,
    Midgardian Mail, Shifter''s Shield, Leviathan''s Hide, Screeching Gargoyle, Genji''s
    Guard.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.9
    Spear of Desolation:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.33
      fit: 0.38
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.31
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.21
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Spear of Desolation
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
    for this god: Rod of Tahuti, Obsidian Shard, Amanita Charm, Soul Gem, Gluttonous
    Grimoire, Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Spear of the
    Magus, Void Stone, Void Shield, Breastplate of Valor, Doom Orb, Helm of Radiance,
    The World Stone, Helm of Darkness, Erosion, Oni Hunter''s Garb, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Dreamer''s Idol, Midgardian Mail, Magi''s
    Cloak, Lotus Sickle, Mantle Of Discord, Shifter''s Shield, Genji''s Guard.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.68
    Stone of Binding:
      total: 0.52
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.72
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.53
      pick: 0.33
      fit: 0.55
    Obsidian Shard:
      total: 0.61
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.53
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.43
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
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
    this god: Rod of Tahuti, Obsidian Shard, Amanita Charm, Nimble Ring, Kinetic Cuirass,
    Soul Gem, Gluttonous Grimoire, Breastplate of Valor, Helm of Radiance, Eros''
    Bow, Oni Hunter''s Garb, Helm of Darkness, Erosion, Shield of the Phoenix, Eye
    of Providence, Blood-Bound Book, Stone of Binding, Screeching Gargoyle, Midgardian
    Mail, Bragi''s Harp, Draconic Scale, Lotus Sickle, Ancient Signet, Magi''s Cloak,
    Leviathan''s Hide, Mantle Of Discord, Bracer of The Abyss, Genji''s Guard.'
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.47
      efficiency: 0.45
      win: 0.54
      pick: 0.0
      fit: 0.46
    Obsidian Shard:
      total: 0.56
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.21
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.11
    Eros' Bow:
      total: 0.48
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
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
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Obsidian Shard, Amanita
    Charm, Breastplate of Valor, Kinetic Cuirass, Soul Gem, Shield of the Phoenix,
    Screeching Gargoyle, Lotus Sickle, Chronos'' Pendant, Prophetic Cloak, Helm of
    Radiance, Erosion, Helm of Darkness, Oni Hunter''s Garb, Eye of Providence, Gluttonous
    Grimoire, Gladiator''s Shield, Draconic Scale, Stone of Binding, Gem of Focus,
    Midgardian Mail, Heartwood Charm, Magi''s Cloak, Mantle Of Discord, Leviathan''s
    Hide, Shifter''s Shield, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.33
      fit: 0.46
    Obsidian Shard:
      total: 0.56
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.23
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.13
    Soul Gem:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.1
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
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
    Shield, Jotunn''s Revenge, Amanita Charm, Shield Splitter, Kinetic Cuirass, Runeforged
    Hammer, Tekko-Kagi, Breastplate of Valor, Hydra''s Lament, Titan''s Bane, Soul
    Gem, Gluttonous Grimoire, Golden Blade, Helm of Radiance, Tyrfing, The Crusher,
    Oni Hunter''s Garb, Helm of Darkness, Lernaean Bow, Erosion, Avenging Blade, Spear
    of the Magus, Death Metal, Shield of the Phoenix, Eye of Providence, Arondight,
    Heartseeker, Stone of Binding, Draconic Scale, Screeching Gargoyle, The Reaper,
    Midgardian Mail, Nimble Ring, Magi''s Cloak, Toxic Blade, Bragi''s Harp, Lotus
    Sickle, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.54
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.54
      pick: 0.0
      fit: 0.45
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.48
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.33
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.23
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
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
  - Shield Splitter
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Obsidian Shard, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Berserker''s Shield, Kinetic Cuirass,
    Soul Gem, Gluttonous Grimoire, Breastplate of Valor, Helm of Radiance, Runeforged
    Hammer, Titan''s Bane, Hydra''s Lament, Helm of Darkness, Spear of the Magus,
    Death Metal, Lotus Sickle, Oni Hunter''s Garb, Erosion, Ancient Signet, Chronos''
    Pendant, Eye of Providence, Shield of the Phoenix, The Crusher, Doom Orb, Draconic
    Scale, Jade Scepter, Stone of Binding, Screeching Gargoyle, Midgardian Mail, The
    World Stone, Avenging Blade, Magi''s Cloak, Arondight, Heartseeker, Mantle Of
    Discord, Leviathan''s Hide, The Reaper, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.54
      pick: 0.0
      fit: 0.42
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.33
      fit: 0.42
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.32
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
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
    swap: Helm of Darkness — physical protection
    swap_item: Helm of Darkness
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Genji''s
    Guard, Breastplate of Valor, Erosion, Helm of Darkness, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Helm of Radiance, Oni Hunter''s Garb, Gluttonous
    Grimoire, Shifter''s Shield, Stone of Binding, Magi''s Cloak, Screeching Gargoyle,
    Midgardian Mail, Soul Gem, Mantle Of Discord, Leviathan''s Hide, Obsidian Shard,
    Prophetic Cloak, Lotus Sickle, Ancile, Jade Scepter, Hide of the Nemean Lion,
    Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.44
      efficiency: 0.69
      win: 0.29
      pick: 0.12
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.51
      efficiency: 0.58
      win: 0.46
      pick: 0.17
      fit: 0.62
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.2
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
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
    Cuirass, Genji''s Guard, Breastplate of Valor, Erosion, Helm of Darkness, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Helm of Radiance, Oni Hunter''s
    Garb, Gluttonous Grimoire, Shifter''s Shield, Stone of Binding, Magi''s Cloak,
    Screeching Gargoyle, Midgardian Mail, Soul Gem, Mantle Of Discord, Leviathan''s
    Hide, Obsidian Shard, Prophetic Cloak, Lotus Sickle, Ancile, Jade Scepter, Hide
    of the Nemean Lion, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.44
      efficiency: 0.69
      win: 0.29
      pick: 0.12
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.73
    Shell of Rebuke:
      total: 0.47
      efficiency: 0.29
      win: 0.66
      pick: 0.18
      fit: 0.45
    Freya's Tears:
      total: 0.51
      efficiency: 0.58
      win: 0.46
      pick: 0.17
      fit: 0.62
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.2
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
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
