---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.24
  aspect_win_rate: 0.4
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.12
    win_rate: 0.7
    alternates:
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.1
    - name: Prophetic Cloak
      pick_rate: 0.11
      win_rate: 0.44
  - name: Chronos' Pendant
    pick_rate: 0.13
    win_rate: 0.55
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.29
  - name: Rod of Tahuti
    pick_rate: 0.12
    win_rate: 0.9
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.14
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.33
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.11
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.89
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.33
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.2
    alternates:
    - name: The World Stone
      pick_rate: 0.06
      win_rate: 1.0
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.5
  - name: Captain's Ring
    pick_rate: 0.05
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 1.0
    - name: Totem of Death
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.27
    win_rate: 0.22
  - name: Conduit Gem
    pick_rate: 0.11
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-10-09'
  god_win_rate: 0.40476190476190477
  god_matches_won: 34
  god_matches_played: 84
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-09'
  god_matches_analyzed: 2961
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
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
    this god: Spear of Desolation, Amanita Charm, Kinetic Cuirass, Shifter''s Shield,
    Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield of the
    Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion,
    Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb,
    Xibalban Effigy, Hussar''s Wings, Prophetic Cloak, Genji''s Guard, Stampede.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.29
    The World Stone:
      total: 0.66
      efficiency: 0.52
      win: 1.0
      pick: 0.13
      fit: 0.15
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.9
      pick: 0.19
      fit: 0.15
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.89
      pick: 0.18
      fit: 0.25
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Shield of the Phoenix
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Shifter''s Shield, Breastplate of Valor, Soul Gem, Erosion, Eye of Providence,
    Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Yogi''s
    Necklace, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone
    of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void
    Shield, Magi''s Cloak, Ancile, Genji''s Guard, Stampede.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.92
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.3
    The World Stone:
      total: 0.66
      efficiency: 0.52
      win: 1.0
      pick: 0.13
      fit: 0.16
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.9
      pick: 0.19
      fit: 0.16
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.89
      pick: 0.18
      fit: 0.26
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The World Stone, Spear of Desolation, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Breastplate of Valor,
    Spear of the Magus, Soul Gem, Void Shield, Shifter''s Shield, Void Stone, Erosion,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    Dreamer''s Idol, Magi''s Cloak, Mantle Of Discord, Midgardian Mail, Rod of Asclepius,
    Hide of the Nemean Lion, Genji''s Guard.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.51
    The World Stone:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.13
      fit: 0.41
    Rod of Tahuti:
      total: 0.78
      efficiency: 0.86
      win: 0.9
      pick: 0.19
      fit: 0.41
    Obsidian Shard:
      total: 0.68
      efficiency: 0.54
      win: 0.89
      pick: 0.18
      fit: 0.51
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Spear of Desolation, Amanita Charm, Nimble Ring, Kinetic Cuirass, Breastplate
    of Valor, Gluttonous Grimoire, Shifter''s Shield, Soul Gem, Helm of Radiance,
    Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the Magus,
    Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of
    The Abyss, Hide of the Nemean Lion, Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    The World Stone:
      total: 0.65
      efficiency: 0.52
      win: 1.0
      pick: 0.13
      fit: 0.08
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.9
      pick: 0.19
      fit: 0.08
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.89
      pick: 0.18
      fit: 0.18
  community_ordered:
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Breastplate of Valor
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Spear of Desolation, Breastplate of
    Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle,
    Soul Gem, Shifter''s Shield, Erosion, Helm of Radiance, Gluttonous Grimoire, Eye
    of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Gem of Focus,
    Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of
    Discord, Glorious Pridwen, Prophetic Cloak, Midgardian Mail, Daybreak Gavel, Genji''s
    Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.14
      fit: 0.48
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.55
      pick: 0.18
      fit: 0.42
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.46
    The World Stone:
      total: 0.66
      efficiency: 0.52
      win: 1.0
      pick: 0.13
      fit: 0.13
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.9
      pick: 0.19
      fit: 0.13
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.89
      pick: 0.18
      fit: 0.23
  community_ordered:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Jotunn's Revenge
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Spear of Desolation, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Breastplate of Valor,
    Runeforged Hammer, Golden Blade, Shifter''s Shield, Gluttonous Grimoire, Eye of
    the Storm, Hydra''s Lament, Heartseeker, Lernaean Bow, Tyrfing, Erosion, Spear
    of the Magus, Tekko-Kagi, Eye of Providence, Avenging Blade, Helm of Radiance,
    Soul Gem, Stone of Binding, Shield of the Phoenix, Draconic Scale, Titan''s Bane,
    The Crusher, Pharaoh''s Curse, Magi''s Cloak, Nimble Ring, Silverbranch Bow, The
    Reaper, Shogun''s Ofuda, Screeching Gargoyle, Toxic Blade, Mantle Of Discord,
    Midgardian Mail, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.22
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.28
    The World Stone:
      total: 0.67
      efficiency: 0.52
      win: 1.0
      pick: 0.13
      fit: 0.2
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.9
      pick: 0.19
      fit: 0.2
    Obsidian Shard:
      total: 0.65
      efficiency: 0.54
      win: 0.89
      pick: 0.18
      fit: 0.3
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: The World Stone, Spear of Desolation,
    Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Breastplate
    of Valor, Shield Splitter, Spear of the Magus, Runeforged Hammer, Helm of Radiance,
    Soul Gem, Shifter''s Shield, Berserker''s Shield, Eye of the Storm, Hydra''s Lament,
    Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix,
    Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting
    Pearl, Avenging Blade, Magi''s Cloak, Helm of Darkness, Titan''s Bane, The Crusher,
    Ancient Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian
    Mail, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.41
    The World Stone:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.13
      fit: 0.33
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.9
      pick: 0.19
      fit: 0.33
    Obsidian Shard:
      total: 0.66
      efficiency: 0.54
      win: 0.89
      pick: 0.18
      fit: 0.43
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Spear of Desolation
  - The World Stone
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
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Genji''s
    Guard, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak,
    Hide of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.42
      efficiency: 0.66
      win: 0.29
      pick: 0.11
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.41
      efficiency: 0.61
      win: 0.2
      pick: 0.17
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
---
