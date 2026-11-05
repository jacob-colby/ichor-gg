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
  last_verified: '2026-11-04'
  god_win_rate: 0.4852941176470588
  god_matches_won: 165
  god_matches_played: 340
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
    this god: Rod of Tahuti, Obsidian Shard, Amanita Charm, Kinetic Cuirass, Soul
    Gem, Gluttonous Grimoire, Breastplate of Valor, Erosion, Helm of Darkness, Eye
    of Providence, Shield of the Phoenix, Draconic Scale, Helm of Radiance, Oni Hunter''s
    Garb, Lotus Sickle, Stone of Binding, Shifter''s Shield, Screeching Gargoyle,
    Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Leviathan''s Hide, Blood-Bound
    Book, Prophetic Cloak, Chronos'' Pendant, Ancile, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.67
    Spear of Desolation:
      total: 0.51
      efficiency: 0.59
      win: 0.53
      pick: 0.33
      fit: 0.33
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.28
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.18
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.57
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
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Blood-Bound Book, Ethereal Staff, Phoenix Feather,
    Breastplate of Valor, Yogi''s Necklace, Chandra''s Grace, Erosion, Eye of Providence,
    Oni Hunter''s Garb, Bancroft''s Talon, Lotus Sickle, Rod of Asclepius, Draconic
    Scale, Helm of Radiance, Helm of Darkness, Sphere of Negation, Regrowth Striders,
    Glorious Pridwen, Soul Locket, Midgardian Mail, Shifter''s Shield, Genji''s Guard.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.51
      efficiency: 0.59
      win: 0.53
      pick: 0.33
      fit: 0.35
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.29
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.19
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.85
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.54
      pick: 0.1
      fit: 0.85
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Obsidian Shard, Soul Gem, Gluttonous Grimoire, Amanita
    Charm, Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Void Stone, Void
    Shield, Spear of the Magus, Breastplate of Valor, Doom Orb, Helm of Radiance,
    Lotus Sickle, The World Stone, Oni Hunter''s Garb, Helm of Darkness, Erosion,
    Eye of Providence, Shield of the Phoenix, Draconic Scale, Dreamer''s Idol, Midgardian
    Mail, Magi''s Cloak, Blood-Bound Book, Mantle Of Discord, Genji''s Guard.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.52
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.53
      pick: 0.33
      fit: 0.51
    Obsidian Shard:
      total: 0.6
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.5
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.4
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.54
      pick: 0.1
      fit: 0.68
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
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
    Soul Gem, Gluttonous Grimoire, Breastplate of Valor, Lotus Sickle, Helm of Radiance,
    Eros'' Bow, Oni Hunter''s Garb, Helm of Darkness, Erosion, Shield of the Phoenix,
    Eye of Providence, Blood-Bound Book, Stone of Binding, Screeching Gargoyle, Midgardian
    Mail, Bragi''s Harp, Draconic Scale, Ancient Signet, Magi''s Cloak, Leviathan''s
    Hide, Mantle Of Discord, Bracer of The Abyss, Genji''s Guard.'
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
  - Spear of Desolation
  - Kinetic Cuirass
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Obsidian Shard, Soul
    Gem, Amanita Charm, Breastplate of Valor, Kinetic Cuirass, Lotus Sickle, Gluttonous
    Grimoire, Shield of the Phoenix, Screeching Gargoyle, Chronos'' Pendant, Helm
    of Radiance, Prophetic Cloak, Oni Hunter''s Garb, Erosion, Helm of Darkness, Eye
    of Providence, Draconic Scale, Stone of Binding, Gladiator''s Shield, Gem of Focus,
    Midgardian Mail, Heartwood Charm, Magi''s Cloak, Blood-Bound Book, Mantle Of Discord,
    Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.33
      fit: 0.42
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
      total: 0.54
      efficiency: 0.57
      win: 0.54
      pick: 0.1
      fit: 0.59
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
    Shield, Jotunn''s Revenge, Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield
    Splitter, Kinetic Cuirass, Runeforged Hammer, Nimble Ring, Breastplate of Valor,
    The Reaper, Tekko-Kagi, Hydra''s Lament, Titan''s Bane, Golden Blade, Lotus Sickle,
    Helm of Radiance, Tyrfing, The Crusher, Oni Hunter''s Garb, Lernaean Bow, Helm
    of Darkness, Spear of the Magus, Avenging Blade, Erosion, Death Metal, Arondight,
    Shield of the Phoenix, Eye of Providence, Heartseeker, Stone of Binding, Screeching
    Gargoyle, Blood-Bound Book, Midgardian Mail, Draconic Scale, Magi''s Cloak, Toxic
    Blade, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.54
      pick: 0.0
      fit: 0.31
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
      fit: 0.45
    Obsidian Shard:
      total: 0.58
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
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.36
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
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Obsidian Shard, Jotunn''s
    Revenge, Soul Gem, Gluttonous Grimoire, Amanita Charm, Shield Splitter, Berserker''s
    Shield, Kinetic Cuirass, Breastplate of Valor, Helm of Radiance, Lotus Sickle,
    Runeforged Hammer, The Reaper, Hydra''s Lament, Titan''s Bane, Helm of Darkness,
    Spear of the Magus, Blood-Bound Book, Death Metal, Oni Hunter''s Garb, Ancient
    Signet, Erosion, Chronos'' Pendant, Shield of the Phoenix, Eye of Providence,
    The Crusher, Jade Scepter, Stone of Binding, Doom Orb, Screeching Gargoyle, Draconic
    Scale, Midgardian Mail, Avenging Blade, The World Stone, Magi''s Cloak, Arondight,
    Heartseeker, Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.54
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.51
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.33
      fit: 0.4
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.71
      pick: 0.11
      fit: 0.4
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.6
      pick: 0.13
      fit: 0.3
    Soul Gem:
      total: 0.53
      efficiency: 0.57
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
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Helm of Darkness — magical protection
    swap_item: Helm of Darkness
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Genji''s
    Guard, Gluttonous Grimoire, Soul Gem, Breastplate of Valor, Erosion, Helm of Darkness,
    Eye of Providence, Shield of the Phoenix, Draconic Scale, Helm of Radiance, Oni
    Hunter''s Garb, Lotus Sickle, Stone of Binding, Shifter''s Shield, Screeching
    Gargoyle, Magi''s Cloak, Midgardian Mail, Obsidian Shard, Mantle Of Discord, Leviathan''s
    Hide, Blood-Bound Book, Prophetic Cloak, Ancile, Jade Scepter, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.43
      efficiency: 0.69
      win: 0.29
      pick: 0.12
      fit: 0.36
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.5
      efficiency: 0.58
      win: 0.46
      pick: 0.17
      fit: 0.56
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.57
    Erosion:
      total: 0.5
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shell of Rebuke
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Genji''s Guard, Gluttonous Grimoire, Soul Gem, Breastplate of Valor,
    Erosion, Helm of Darkness, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Helm of Radiance, Oni Hunter''s Garb, Lotus Sickle, Stone of Binding, Shifter''s
    Shield, Screeching Gargoyle, Magi''s Cloak, Midgardian Mail, Obsidian Shard, Mantle
    Of Discord, Leviathan''s Hide, Blood-Bound Book, Prophetic Cloak, Ancile, Jade
    Scepter, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.43
      efficiency: 0.69
      win: 0.29
      pick: 0.12
      fit: 0.36
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.67
    Shell of Rebuke:
      total: 0.47
      efficiency: 0.29
      win: 0.66
      pick: 0.18
      fit: 0.41
    Freya's Tears:
      total: 0.5
      efficiency: 0.58
      win: 0.46
      pick: 0.17
      fit: 0.56
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  swaps:
  - added: Shell of Rebuke
    removed: Erosion
    reason: community 66% win over 37 matches (vs 49% on this god), taking the model's
      weakest slot from Erosion
  starter: *id001
---
