---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 1.0
  aspect_win_rate: 0.0
  slot_order:
  - name: Spear of Desolation
    pick_rate: 1.0
    win_rate: 0.0
  - name: Reliquary
    pick_rate: 1.0
    win_rate: 0.0
  - name: Oracle Staff
    pick_rate: 1.0
    win_rate: 0.0
  community_starters:
  - name: Conduit Gem
    pick_rate: 1.0
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-11-04'
  god_win_rate: 0
  god_matches_won: 0
  god_matches_played: 1
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Genji''s Guard, Freya''s
    Tears, Gluttonous Grimoire, Erosion, Breastplate of Valor, Eye of Providence,
    Soul Gem, Draconic Scale, Helm of Darkness, Oni Hunter''s Garb, Shield of the
    Phoenix, Shifter''s Shield, Stone of Binding, Magi''s Cloak, Helm of Radiance,
    Midgardian Mail, Mantle Of Discord, Leviathan''s Hide, Screeching Gargoyle, Ancile,
    Prophetic Cloak, Hide of the Nemean Lion, Obsidian Shard, Stampede, Void Stone,
    Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.29
      efficiency: 0.69
      win: 0.0
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.3
      efficiency: 0.59
      win: 0.0
      pick: 1.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.31
      efficiency: 0.56
      win: 0.0
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.29
      efficiency: 0.58
      win: 0.0
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.32
      efficiency: 0.86
      win: 0.0
      pick: 0.0
      fit: 0.14
    Amanita Charm:
      total: 0.32
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Spear of Desolation
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Shield of the Phoenix, Kinetic
    Cuirass, Gluttonous Grimoire, Genji''s Guard, Blood-Bound Book, Freya''s Tears,
    Phoenix Feather, Ethereal Staff, Erosion, Yogi''s Necklace, Eye of Providence,
    Breastplate of Valor, Draconic Scale, Oni Hunter''s Garb, Chandra''s Grace, Midgardian
    Mail, Shifter''s Shield, Glorious Pridwen, Rod of Asclepius, Bancroft''s Talon,
    Leviathan''s Hide, Helm of Darkness, Regrowth Striders, Helm of Radiance, Sphere
    of Negation, Soul Locket, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.29
      efficiency: 0.69
      win: 0.0
      pick: 0.0
      fit: 0.32
    Spear of Desolation:
      total: 0.3
      efficiency: 0.59
      win: 0.0
      pick: 1.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.3
      efficiency: 0.56
      win: 0.0
      pick: 0.0
      fit: 0.72
    Rod of Tahuti:
      total: 0.32
      efficiency: 0.86
      win: 0.0
      pick: 0.0
      fit: 0.14
    Amanita Charm:
      total: 0.37
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.92
    Soul Gem:
      total: 0.32
      efficiency: 0.57
      win: 0.0
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Spear of Desolation
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
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
    of Binding, Kinetic Cuirass, Genji''s Guard, Screeching Gargoyle, Obsidian Shard,
    Void Stone, Void Shield, Freya''s Tears, Spear of the Magus, Breastplate of Valor,
    Erosion, Oni Hunter''s Garb, Eye of Providence, Doom Orb, Helm of Radiance, Draconic
    Scale, The World Stone, Helm of Darkness, Shield of the Phoenix, Midgardian Mail,
    Magi''s Cloak, Dreamer''s Idol, Mantle Of Discord, Shifter''s Shield, Leviathan''s
    Hide.'
  slot_scores:
    Stone of Binding:
      total: 0.28
      efficiency: 0.5
      win: 0.0
      pick: 0.0
      fit: 0.72
    Spear of Desolation:
      total: 0.33
      efficiency: 0.59
      win: 0.0
      pick: 1.0
      fit: 0.47
    Genji's Guard:
      total: 0.28
      efficiency: 0.69
      win: 0.0
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.28
      efficiency: 0.56
      win: 0.0
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.31
      efficiency: 0.59
      win: 0.0
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.36
      efficiency: 0.86
      win: 0.0
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Bragi's Harp
  - Rod of Tahuti
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Genji''s Guard, Nimble Ring, Kinetic Cuirass,
    Gluttonous Grimoire, Freya''s Tears, Breastplate of Valor, Soul Gem, Eros'' Bow,
    Oni Hunter''s Garb, Helm of Radiance, Erosion, Eye of Providence, Obsidian Shard,
    Stone of Binding, Helm of Darkness, Midgardian Mail, Draconic Scale, Shield of
    the Phoenix, Magi''s Cloak, Screeching Gargoyle, Blood-Bound Book, Leviathan''s
    Hide, Bragi''s Harp, Mantle Of Discord, Ancient Signet, Shifter''s Shield, Bracer
    of The Abyss.'
  slot_scores:
    Nimble Ring:
      total: 0.27
      efficiency: 0.63
      win: 0.0
      pick: 0.0
      fit: 0.31
    Spear of Desolation:
      total: 0.28
      efficiency: 0.59
      win: 0.0
      pick: 1.0
      fit: 0.15
    Bragi's Harp:
      total: 0.22
      efficiency: 0.45
      win: 0.0
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.31
      efficiency: 0.86
      win: 0.0
      pick: 0.0
      fit: 0.08
    Eros' Bow:
      total: 0.24
      efficiency: 0.53
      win: 0.0
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.28
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Freya''s
    Tears, Amanita Charm, Soul Gem, Breastplate of Valor, Kinetic Cuirass, Gluttonous
    Grimoire, Shield of the Phoenix, Screeching Gargoyle, Lotus Sickle, Chronos''
    Pendant, Helm of Radiance, Prophetic Cloak, Oni Hunter''s Garb, Erosion, Helm
    of Darkness, Eye of Providence, Obsidian Shard, Draconic Scale, Stone of Binding,
    Gladiator''s Shield, Gem of Focus, Midgardian Mail, Heartwood Charm, Magi''s Cloak,
    Blood-Bound Book, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.31
      efficiency: 0.69
      win: 0.0
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.32
      efficiency: 0.59
      win: 0.0
      pick: 1.0
      fit: 0.42
    Breastplate of Valor:
      total: 0.29
      efficiency: 0.63
      win: 0.0
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.27
      efficiency: 0.56
      win: 0.0
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.29
      efficiency: 0.58
      win: 0.0
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.29
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Spear of Desolation
  - Jotunn's Revenge
  - Shield Splitter
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Gluttonous Grimoire, Genji''s Guard,
    Kinetic Cuirass, Soul Gem, Runeforged Hammer, The Reaper, Tekko-Kagi, Titan''s
    Bane, Freya''s Tears, Golden Blade, Breastplate of Valor, Hydra''s Lament, Nimble
    Ring, Obsidian Shard, Tyrfing, The Crusher, Oni Hunter''s Garb, Helm of Radiance,
    Lernaean Bow, Erosion, Avenging Blade, Eye of Providence, Heartseeker, Stone of
    Binding, Draconic Scale, Helm of Darkness, Shield of the Phoenix, Midgardian Mail,
    Arondight, Spear of the Magus, Death Metal, Magi''s Cloak, Toxic Blade, Screeching
    Gargoyle, Pharaoh''s Curse, Leviathan''s Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.31
      efficiency: 0.74
      win: 0.0
      pick: 0.0
      fit: 0.33
    Spear of Desolation:
      total: 0.3
      efficiency: 0.59
      win: 0.0
      pick: 1.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.3
      efficiency: 0.67
      win: 0.0
      pick: 0.0
      fit: 0.42
    Shield Splitter:
      total: 0.28
      efficiency: 0.59
      win: 0.0
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.33
      efficiency: 0.86
      win: 0.0
      pick: 0.0
      fit: 0.19
    Amanita Charm:
      total: 0.29
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Jotunn's Revenge
  - Transcendence
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    Jotunn''s Revenge, Amanita Charm, Soul Gem, Shield Splitter, Genji''s Guard, Berserker''s
    Shield, Kinetic Cuirass, Obsidian Shard, Freya''s Tears, Helm of Radiance, Runeforged
    Hammer, Breastplate of Valor, The Reaper, Titan''s Bane, Helm of Darkness, Spear
    of the Magus, Hydra''s Lament, Blood-Bound Book, Death Metal, Oni Hunter''s Garb,
    Ancient Signet, Erosion, Lotus Sickle, Eye of Providence, The Crusher, Doom Orb,
    Jade Scepter, Stone of Binding, Draconic Scale, Shield of the Phoenix, Midgardian
    Mail, Avenging Blade, The World Stone, Magi''s Cloak, Chronos'' Pendant, Heartseeker,
    Screeching Gargoyle, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Book of Thoth:
      total: 0.2
      efficiency: 0.49
      win: 0.0
      pick: 0.0
      fit: 0.17
    Spear of Desolation:
      total: 0.31
      efficiency: 0.59
      win: 0.0
      pick: 1.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.29
      efficiency: 0.67
      win: 0.0
      pick: 0.0
      fit: 0.38
    Transcendence:
      total: 0.21
      efficiency: 0.53
      win: 0.0
      pick: 0.0
      fit: 0.17
    Gluttonous Grimoire:
      total: 0.29
      efficiency: 0.59
      win: 0.0
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.35
      efficiency: 0.86
      win: 0.0
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Spear of Desolation
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Genji''s
    Guard, Freya''s Tears, Gluttonous Grimoire, Erosion, Breastplate of Valor, Eye
    of Providence, Soul Gem, Draconic Scale, Helm of Darkness, Oni Hunter''s Garb,
    Shield of the Phoenix, Shifter''s Shield, Stone of Binding, Magi''s Cloak, Helm
    of Radiance, Midgardian Mail, Mantle Of Discord, Leviathan''s Hide, Screeching
    Gargoyle, Ancile, Prophetic Cloak, Hide of the Nemean Lion, Obsidian Shard, Stampede,
    Void Stone, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.29
      efficiency: 0.69
      win: 0.0
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.27
      efficiency: 0.63
      win: 0.0
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.31
      efficiency: 0.56
      win: 0.0
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.29
      efficiency: 0.58
      win: 0.0
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.32
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.27
      efficiency: 0.51
      win: 0.0
      pick: 0.0
      fit: 0.64
  starter: *id001
---
