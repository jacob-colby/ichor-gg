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
  - Spear of Desolation
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Shield of the Phoenix, Breastplate of Valor, Draconic Scale, Erosion,
    Eye of Providence, Oni Hunter''s Garb, Shifter''s Shield, Helm of Darkness, Lotus
    Sickle, Helm of Radiance, Screeching Gargoyle, Stone of Binding, Midgardian Mail,
    Blood-Bound Book, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Gladiator''s
    Shield, Hide of the Nemean Lion, Chronos'' Pendant, Prophetic Cloak, Ancile, Genji''s
    Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.67
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.33
      fit: 0.33
    Obsidian Shard:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.11
      fit: 0.28
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.6
      pick: 0.13
      fit: 0.18
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
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
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Shield of the Phoenix, Kinetic
    Cuirass, Blood-Bound Book, Gluttonous Grimoire, Phoenix Feather, Ethereal Staff,
    Yogi''s Necklace, Breastplate of Valor, Chandra''s Grace, Draconic Scale, Oni
    Hunter''s Garb, Bancroft''s Talon, Erosion, Eye of Providence, Rod of Asclepius,
    Lotus Sickle, Shifter''s Shield, Soul Locket, Regrowth Striders, Glorious Pridwen,
    Midgardian Mail, Helm of Radiance, Screeching Gargoyle, Helm of Darkness, Genji''s
    Guard.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.33
      fit: 0.35
    Obsidian Shard:
      total: 0.56
      efficiency: 0.53
      win: 0.71
      pick: 0.11
      fit: 0.29
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.6
      pick: 0.13
      fit: 0.19
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.85
    Soul Gem:
      total: 0.58
      efficiency: 0.58
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
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Obsidian Shard, Soul Gem, Gluttonous Grimoire, Amanita
    Charm, Kinetic Cuirass, Screeching Gargoyle, Stone of Binding, Void Stone, Void
    Shield, Breastplate of Valor, Shield of the Phoenix, Spear of the Magus, Draconic
    Scale, Dreamer''s Idol, Oni Hunter''s Garb, Lotus Sickle, Erosion, Eye of Providence,
    Helm of Radiance, Blood-Bound Book, Doom Orb, Shifter''s Shield, Helm of Darkness,
    Midgardian Mail, The World Stone, Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.66
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.33
      fit: 0.51
    Obsidian Shard:
      total: 0.59
      efficiency: 0.53
      win: 0.71
      pick: 0.11
      fit: 0.5
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.6
      pick: 0.13
      fit: 0.4
    Soul Gem:
      total: 0.55
      efficiency: 0.58
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
  - Bragi's Harp
  - Eros' Bow
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
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Breastplate of Valor, Nimble Ring, Shield of the Phoenix, Oni Hunter''s
    Garb, Lotus Sickle, Draconic Scale, Blood-Bound Book, Bragi''s Harp, Helm of Radiance,
    Screeching Gargoyle, Erosion, Eros'' Bow, Eye of Providence, Ancient Signet, Midgardian
    Mail, Shifter''s Shield, Chronos'' Pendant, Helm of Darkness, Stone of Binding,
    Death Metal, Leviathan''s Hide, Bracer of The Abyss, Genji''s Guard.'
  slot_scores:
    Nimble Ring:
      total: 0.49
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.47
      efficiency: 0.47
      win: 0.54
      pick: 0.0
      fit: 0.46
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.71
      pick: 0.11
      fit: 0.21
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.6
      pick: 0.13
      fit: 0.11
    Eros' Bow:
      total: 0.47
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
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
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Breastplate of Valor, Shield of the Phoenix, Lotus Sickle,
    Screeching Gargoyle, Gluttonous Grimoire, Chronos'' Pendant, Gladiator''s Shield,
    Draconic Scale, Oni Hunter''s Garb, Prophetic Cloak, Erosion, Eye of Providence,
    Helm of Radiance, Blood-Bound Book, Shifter''s Shield, Gem of Focus, Heartwood
    Charm, Helm of Darkness, Midgardian Mail, Chandra''s Grace, Stone of Binding,
    Leviathan''s Hide, Regrowth Striders, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.33
      fit: 0.42
    Obsidian Shard:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.11
      fit: 0.23
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.6
      pick: 0.13
      fit: 0.13
    Soul Gem:
      total: 0.54
      efficiency: 0.58
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
  - Kinetic Cuirass
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    win/pick). Underrated for this god: Rod of Tahuti, Obsidian Shard, Berserker''s
    Shield, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Shield Splitter, The Reaper, Breastplate of Valor, Tyrfing, Runeforged
    Hammer, Hydra''s Lament, Shield of the Phoenix, Golden Blade, Oni Hunter''s Garb,
    The Crusher, Lotus Sickle, Draconic Scale, Death Metal, Heartseeker, Blood-Bound
    Book, Helm of Radiance, Erosion, Screeching Gargoyle, Bragi''s Harp, Eye of Providence,
    Tekko-Kagi, Nimble Ring, Titan''s Bane, Shifter''s Shield, Midgardian Mail, Helm
    of Darkness, Arondight, Ancient Signet, Spear of the Magus, Stone of Binding,
    Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.46
    Obsidian Shard:
      total: 0.56
      efficiency: 0.53
      win: 0.71
      pick: 0.11
      fit: 0.31
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.6
      pick: 0.13
      fit: 0.21
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Obsidian Shard, Soul
    Gem, Amanita Charm, Jotunn''s Revenge, Gluttonous Grimoire, Kinetic Cuirass, Shield
    Splitter, Berserker''s Shield, Breastplate of Valor, Lotus Sickle, The Reaper,
    Shield of the Phoenix, Blood-Bound Book, Helm of Radiance, Runeforged Hammer,
    Hydra''s Lament, Death Metal, Oni Hunter''s Garb, Draconic Scale, Helm of Darkness,
    Spear of the Magus, Ancient Signet, Chronos'' Pendant, The Crusher, Erosion, Screeching
    Gargoyle, Eye of Providence, Polynomicon, Heartseeker, Dreamer''s Idol, Shifter''s
    Shield, Midgardian Mail, Stone of Binding, Jade Scepter, Titan''s Bane, Leviathan''s
    Hide, Tyrfing, Magi''s Cloak, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.33
      fit: 0.4
    Obsidian Shard:
      total: 0.57
      efficiency: 0.53
      win: 0.71
      pick: 0.11
      fit: 0.4
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.6
      pick: 0.13
      fit: 0.3
    Soul Gem:
      total: 0.54
      efficiency: 0.58
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
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Genji''s
    Guard, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix, Breastplate of Valor,
    Draconic Scale, Erosion, Eye of Providence, Oni Hunter''s Garb, Shifter''s Shield,
    Helm of Darkness, Lotus Sickle, Helm of Radiance, Screeching Gargoyle, Stone of
    Binding, Midgardian Mail, Blood-Bound Book, Magi''s Cloak, Mantle Of Discord,
    Leviathan''s Hide, Gladiator''s Shield, Hide of the Nemean Lion, Prophetic Cloak,
    Chronos'' Pendant, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.44
      efficiency: 0.71
      win: 0.29
      pick: 0.12
      fit: 0.36
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.46
      pick: 0.17
      fit: 0.56
    Draconic Scale:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
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
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod
    of Tahuti, Genji''s Guard, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Breastplate of Valor, Draconic Scale, Erosion, Eye of Providence, Oni Hunter''s
    Garb, Shifter''s Shield, Helm of Darkness, Lotus Sickle, Helm of Radiance, Screeching
    Gargoyle, Stone of Binding, Midgardian Mail, Blood-Bound Book, Magi''s Cloak,
    Mantle Of Discord, Leviathan''s Hide, Gladiator''s Shield, Hide of the Nemean
    Lion, Prophetic Cloak, Chronos'' Pendant, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.44
      efficiency: 0.71
      win: 0.29
      pick: 0.12
      fit: 0.36
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.67
    Shell of Rebuke:
      total: 0.51
      efficiency: 0.41
      win: 0.66
      pick: 0.18
      fit: 0.41
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.46
      pick: 0.17
      fit: 0.56
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  swaps:
  - added: Shell of Rebuke
    removed: Draconic Scale
    reason: community 66% win over 37 matches (vs 49% on this god), taking the model's
      weakest slot from Draconic Scale
  starter: *id001
---
