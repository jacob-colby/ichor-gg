---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.33
  slot_order:
  - name: Stampede
    pick_rate: 0.23
    win_rate: 0.42
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.18
      win_rate: 0.53
    - name: Leviathan's Hide
      pick_rate: 0.11
      win_rate: 0.42
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.41
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.47
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.38
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.46
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.43
  - name: Sage's Ring
    pick_rate: 0.04
    win_rate: 0.25
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.48
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.59
    alternates:
    - name: Sage's Ring
      pick_rate: 0.04
      win_rate: 0.45
    - name: Shell of Rebuke
      pick_rate: 0.03
      win_rate: 0.38
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.54
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.47
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-11-03'
  god_win_rate: 0.445916114790287
  god_matches_won: 202
  god_matches_played: 453
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Gluttonous Grimoire,
    Erosion, Breastplate of Valor, Eye of Providence, Soul Gem, Draconic Scale, Helm
    of Darkness, Oni Hunter''s Garb, Shield of the Phoenix, Shifter''s Shield, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Midgardian Mail, Mantle Of Discord,
    Screeching Gargoyle, Spear of Desolation, Leviathan''s Hide, Ancile, Prophetic
    Cloak, Hide of the Nemean Lion, Obsidian Shard, Void Stone, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.41
      pick: 0.16
      fit: 0.35
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.52
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.57
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.47
      efficiency: 0.51
      win: 0.44
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Cuirass, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather, Ethereal Staff,
    Erosion, Yogi''s Necklace, Eye of Providence, Breastplate of Valor, Draconic Scale,
    Oni Hunter''s Garb, Chandra''s Grace, Midgardian Mail, Shifter''s Shield, Glorious
    Pridwen, Rod of Asclepius, Bancroft''s Talon, Helm of Darkness, Regrowth Striders,
    Helm of Radiance, Sphere of Negation, Soul Locket, Stone of Binding, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.69
      win: 0.41
      pick: 0.16
      fit: 0.32
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.72
    Freya's Tears:
      total: 0.51
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.51
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.92
    Erosion:
      total: 0.47
      efficiency: 0.51
      win: 0.44
      pick: 0.0
      fit: 0.62
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.44
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
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
    Cloak, Dreamer''s Idol, Mantle Of Discord, Shifter''s Shield, Leviathan''s Hide.'
  slot_scores:
    Stone of Binding:
      total: 0.48
      efficiency: 0.5
      win: 0.44
      pick: 0.0
      fit: 0.72
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.49
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.48
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.44
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Eros'' Bow, Oni Hunter''s Garb, Helm
    of Radiance, Erosion, Eye of Providence, Obsidian Shard, Stone of Binding, Spear
    of Desolation, Helm of Darkness, Midgardian Mail, Draconic Scale, Shield of the
    Phoenix, Magi''s Cloak, Screeching Gargoyle, Blood-Bound Book, Bragi''s Harp,
    Mantle Of Discord, Ancient Signet, Shifter''s Shield, Leviathan''s Hide, Bracer
    of The Abyss.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.47
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.42
      efficiency: 0.45
      win: 0.44
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.48
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.33
    Eros' Bow:
      total: 0.44
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
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
    Gem, Breastplate of Valor, Kinetic Cuirass, Spear of Desolation, Gluttonous Grimoire,
    Shield of the Phoenix, Screeching Gargoyle, Lotus Sickle, Chronos'' Pendant, Helm
    of Radiance, Prophetic Cloak, Oni Hunter''s Garb, Erosion, Helm of Darkness, Eye
    of Providence, Obsidian Shard, Draconic Scale, Stone of Binding, Gladiator''s
    Shield, Gem of Focus, Midgardian Mail, Heartwood Charm, Magi''s Cloak, Blood-Bound
    Book, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.41
      pick: 0.16
      fit: 0.45
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.52
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.6
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.44
      pick: 0.0
      fit: 0.13
    Soul Gem:
      total: 0.49
      efficiency: 0.57
      win: 0.44
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Gluttonous Grimoire, Kinetic Cuirass,
    Soul Gem, Runeforged Hammer, Golden Blade, The Reaper, Tekko-Kagi, Titan''s Bane,
    Breastplate of Valor, Hydra''s Lament, Nimble Ring, Tyrfing, Obsidian Shard, Spear
    of Desolation, The Crusher, Oni Hunter''s Garb, Helm of Radiance, Lernaean Bow,
    Erosion, Avenging Blade, Toxic Blade, Eye of Providence, Heartseeker, Stone of
    Binding, Silverbranch Bow, Draconic Scale, Helm of Darkness, Shield of the Phoenix,
    Midgardian Mail, Arondight, Spear of the Magus, Death Metal, Magi''s Cloak, Screeching
    Gargoyle, Pharaoh''s Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.74
      win: 0.44
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.67
      win: 0.44
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.49
    Shield Splitter:
      total: 0.48
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.48
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.35
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
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
    Hammer, Breastplate of Valor, The Reaper, Titan''s Bane, Helm of Darkness, Spear
    of the Magus, Hydra''s Lament, Blood-Bound Book, Death Metal, Oni Hunter''s Garb,
    Ancient Signet, Erosion, Lotus Sickle, Eye of Providence, The Crusher, Doom Orb,
    Jade Scepter, Stone of Binding, Draconic Scale, Shield of the Phoenix, Midgardian
    Mail, Avenging Blade, The World Stone, Magi''s Cloak, Chronos'' Pendant, Heartseeker,
    Screeching Gargoyle, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.47
      efficiency: 0.67
      win: 0.44
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.67
      win: 0.44
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.49
    Shield Splitter:
      total: 0.47
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.48
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Freya's Tears
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
    Of Discord, Leviathan''s Hide, Screeching Gargoyle, Spear of Desolation, Ancile,
    Prophetic Cloak, Hide of the Nemean Lion, Obsidian Shard, Void Stone, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.41
      pick: 0.16
      fit: 0.35
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.52
      efficiency: 0.58
      win: 0.48
      pick: 0.25
      fit: 0.57
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.47
      efficiency: 0.51
      win: 0.44
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
