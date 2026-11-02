---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.49
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.17
    win_rate: 0.65
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.54
    - name: Prophetic Cloak
      pick_rate: 0.14
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.61
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.59
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.63
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.69
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.62
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.54
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.58
  - name: Rod of Tahuti
    pick_rate: 0.04
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.8
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.8
  - name: Soul Reaver
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Olmec Blue
      pick_rate: 0.06
      win_rate: 0.6
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.75
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.66
  - name: Bluestone Pendant
    pick_rate: 0.37
    win_rate: 0.54
  - name: Gilded Arrow
    pick_rate: 0.09
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-10-30'
  god_win_rate: 0.5772870662460567
  god_matches_won: 183
  god_matches_played: 317
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Rod of Tahuti, Erosion,
    Eye of Providence, Breastplate of Valor, Draconic Scale, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Gluttonous Grimoire, Helm of Radiance, Mantle
    Of Discord, Midgardian Mail, Oni Hunter''s Garb, Screeching Gargoyle, Leviathan''s
    Hide, Hide of the Nemean Lion, Helm of Darkness, Void Shield, Prophetic Cloak,
    Ancile, Spear of Desolation, Hussar''s Wings, Spectral Armor.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.23
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.81
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.58
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
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Shifter''s Shield, Rod of Tahuti, Soul Gem, Erosion, Eye of Providence, Draconic
    Scale, Breastplate of Valor, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace,
    Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Oni Hunter''s
    Garb, Stone of Binding, Helm of Radiance, Leviathan''s Hide, Hide of the Nemean
    Lion, Void Shield, Ancile, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.23
      fit: 0.36
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.92
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.58
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
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Stone of Binding,
    Kinetic Cuirass, Spear of Desolation, Screeching Gargoyle, Spear of the Magus,
    Void Shield, Soul Gem, Obsidian Shard, Void Stone, Breastplate of Valor, Shifter''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom
    Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Oni Hunter''s Garb, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.23
      fit: 0.27
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.54
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.85
      win: 0.5
      pick: 0.09
      fit: 0.41
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of Radiance,
    Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Magi''s Cloak, Spear of the Magus, Spear of Desolation, Daybreak Gavel,
    Bragi''s Harp, Midgardian Mail, Rod of Asclepius, Screeching Gargoyle, Oni Hunter''s
    Garb, Mantle Of Discord, Bracer of The Abyss, Lotus Sickle, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.23
      fit: 0.2
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.58
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Rod of Tahuti, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Soul
    Gem, Lotus Sickle, Screeching Gargoyle, Shifter''s Shield, Chronos'' Pendant,
    Prophetic Cloak, Helm of Radiance, Erosion, Gluttonous Grimoire, Eye of Providence,
    Gladiator''s Shield, Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak,
    Spear of the Magus, Rod of Asclepius, Eye of Erebus, Midgardian Mail, Mantle Of
    Discord, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.23
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.19
      fit: 0.64
    Spear of Desolation:
      total: 0.53
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
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
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti, Amanita
    Charm, Berserker''s Shield, Kinetic Cuirass, Shield Splitter, Runeforged Hammer,
    Breastplate of Valor, Golden Blade, Gluttonous Grimoire, Eye of the Storm, Shifter''s
    Shield, Hydra''s Lament, Heartseeker, Spear of Desolation, Spear of the Magus,
    Erosion, Tyrfing, Lernaean Bow, Eye of Providence, Tekko-Kagi, Helm of Radiance,
    Avenging Blade, Soul Gem, Draconic Scale, Shield of the Phoenix, Obsidian Shard,
    Stone of Binding, Titan''s Bane, The Crusher, Pharaoh''s Curse, Nimble Ring, Silverbranch
    Bow, Magi''s Cloak, The Reaper, Toxic Blade, Shogun''s Ofuda, Midgardian Mail,
    Daybreak Gavel, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.23
      fit: 0.23
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Spear of Desolation, Shield
    Splitter, Spear of the Magus, Breastplate of Valor, Helm of Radiance, Soul Gem,
    Runeforged Hammer, Obsidian Shard, Shifter''s Shield, Berserker''s Shield, Eye
    of the Storm, Hydra''s Lament, Rod of Asclepius, Erosion, Eye of Providence, Lotus
    Sickle, Heartseeker, Draconic Scale, Shield of the Phoenix, Jade Scepter, Stone
    of Binding, Doom Orb, Death Metal, Avenging Blade, Wish-Granting Pearl, The World
    Stone, Magi''s Cloak, Chronos'' Pendant, Helm of Darkness, Titan''s Bane, The
    Crusher, Dreamer''s Idol, Triton''s Conch, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.23
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.52
    Transcendence:
      total: 0.47
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.18
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Erosion, Eye of Providence, Breastplate of Valor, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Gluttonous Grimoire, Helm of
    Radiance, Mantle Of Discord, Midgardian Mail, Oni Hunter''s Garb, Prophetic Cloak,
    Screeching Gargoyle, Leviathan''s Hide, Hide of the Nemean Lion, Helm of Darkness,
    Void Shield, Ancile, Spear of Desolation, Hussar''s Wings, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.23
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.19
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
