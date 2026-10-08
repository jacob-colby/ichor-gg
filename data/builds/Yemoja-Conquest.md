---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.18
  aspect_win_rate: 0.4
  slot_order:
  - name: Circe's Hexstone
    pick_rate: 0.18
    win_rate: 0.2
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.18
      win_rate: 0.6
    - name: Chronos' Pendant
      pick_rate: 0.14
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.25
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.0
    - name: Spear of Desolation
      pick_rate: 0.07
      win_rate: 0.5
  - name: Spear of Desolation
    pick_rate: 0.15
    win_rate: 0.25
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.67
    - name: Talisman of Purification
      pick_rate: 0.11
      win_rate: 0.33
  - name: Shell of Rebuke
    pick_rate: 0.23
    win_rate: 0.0
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.33
    - name: Circe's Hexstone
      pick_rate: 0.08
      win_rate: 0.5
  - name: Rod of Asclepius
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.5
    - name: Spirit Robe
      pick_rate: 0.1
      win_rate: 0.5
  - name: Sage's Ring
    pick_rate: 0.12
    win_rate: 1.0
    alternates:
    - name: Legionnaire Armor
      pick_rate: 0.12
      win_rate: 0.0
    - name: Void Shard
      pick_rate: 0.12
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.39
    win_rate: 0.27
  - name: Bluestone Pendant
    pick_rate: 0.39
    win_rate: 0.27
  - name: Heroism
    pick_rate: 0.07
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-10-08'
  god_win_rate: 0.35714285714285715
  god_matches_won: 10
  god_matches_played: 28
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Breastplate of Valor,
    Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Helm of Radiance,
    Gluttonous Grimoire, Stone of Binding, Magi''s Cloak, Screeching Gargoyle, Soul
    Gem, Mantle Of Discord, Helm of Darkness, Prophetic Cloak, Midgardian Mail, Hide
    of the Nemean Lion, Spear of the Magus, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Genji''s Guard.'
  slot_scores:
    Chronos' Pendant:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.31
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.56
      win: 0.25
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.43
      efficiency: 0.61
      win: 0.25
      pick: 0.19
      fit: 0.62
    Shifter's Shield:
      total: 0.4
      efficiency: 0.55
      win: 0.25
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.33
      pick: 0.2
      fit: 0.2
    Rod of Asclepius:
      total: 0.48
      efficiency: 0.57
      win: 0.5
      pick: 0.22
      fit: 0.33
  community_ordered:
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Shifter''s
    Shield, Breastplate of Valor, Ethereal Staff, Gluttonous Grimoire, Erosion, Eye
    of Providence, Draconic Scale, Chandra''s Grace, Lifebinder, Phoenix Feather,
    Yogi''s Necklace, Glorious Pridwen, Helm of Radiance, Sphere of Negation, Stone
    of Binding, Midgardian Mail, Screeching Gargoyle, Jade Scepter, Wish-Granting
    Pearl, Hide of the Nemean Lion, Genji''s Guard.'
  slot_scores:
    Chronos' Pendant:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.33
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.56
      win: 0.25
      pick: 0.0
      fit: 0.72
    Freya's Tears:
      total: 0.42
      efficiency: 0.61
      win: 0.25
      pick: 0.19
      fit: 0.55
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.33
      pick: 0.2
      fit: 0.21
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.25
      pick: 0.0
      fit: 0.92
    Rod of Asclepius:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.22
      fit: 0.69
  community_ordered:
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Freya's Tears
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Chronos'' Pendant, Amanita Charm, Gluttonous Grimoire, Stone of
    Binding, Screeching Gargoyle, Kinetic Cuirass, Soul Gem, Spear of the Magus, Breastplate
    of Valor, Obsidian Shard, Void Shield, Void Stone, Shifter''s Shield, Doom Orb,
    Helm of Radiance, Erosion, Shield of the Phoenix, Eye of Providence, The World
    Stone, Draconic Scale, Dreamer''s Idol, Magi''s Cloak, Mantle Of Discord, Midgardian
    Mail, Genji''s Guard.'
  slot_scores:
    Stone of Binding:
      total: 0.4
      efficiency: 0.51
      win: 0.25
      pick: 0.0
      fit: 0.72
    Chronos' Pendant:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.22
    Spear of Desolation:
      total: 0.41
      efficiency: 0.57
      win: 0.25
      pick: 0.23
      fit: 0.55
    Freya's Tears:
      total: 0.4
      efficiency: 0.61
      win: 0.25
      pick: 0.19
      fit: 0.44
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.33
      pick: 0.2
      fit: 0.43
    Rod of Asclepius:
      total: 0.47
      efficiency: 0.57
      win: 0.5
      pick: 0.22
      fit: 0.23
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Rod of Asclepius
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
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Amanita Charm, Nimble Ring, Gluttonous Grimoire,
    Kinetic Cuirass, Breastplate of Valor, Soul Gem, Shifter''s Shield, Helm of Radiance,
    Shield of the Phoenix, Erosion, Stone of Binding, Eye of Providence, Spear of
    the Magus, Draconic Scale, Screeching Gargoyle, Bragi''s Harp, Magi''s Cloak,
    Daybreak Gavel, Obsidian Shard, Bracer of The Abyss, Midgardian Mail, Mantle Of
    Discord, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Chronos' Pendant:
      total: 0.45
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.17
    Bracer of The Abyss:
      total: 0.33
      efficiency: 0.52
      win: 0.25
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.39
      efficiency: 0.65
      win: 0.25
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.34
      efficiency: 0.44
      win: 0.25
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.86
      win: 0.33
      pick: 0.2
      fit: 0.11
    Rod of Asclepius:
      total: 0.46
      efficiency: 0.57
      win: 0.5
      pick: 0.22
      fit: 0.18
  community_ordered:
  - Chronos' Pendant
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Breastplate of Valor
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Breastplate of
    Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle,
    Soul Gem, Shifter''s Shield, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous
    Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Gem of Focus, Magi''s Cloak, Eye of Erebus, Spear of the Magus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.41
      efficiency: 0.65
      win: 0.25
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.42
    Spear of Desolation:
      total: 0.39
      efficiency: 0.57
      win: 0.25
      pick: 0.23
      fit: 0.46
    Freya's Tears:
      total: 0.43
      efficiency: 0.61
      win: 0.25
      pick: 0.19
      fit: 0.64
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.86
      win: 0.33
      pick: 0.2
      fit: 0.13
    Rod of Asclepius:
      total: 0.47
      efficiency: 0.57
      win: 0.5
      pick: 0.22
      fit: 0.22
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Chronos' Pendant
  - Jotunn's Revenge
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita
    Charm, Kinetic Cuirass, Breastplate of Valor, Shield Splitter, Runeforged Hammer,
    Gluttonous Grimoire, Golden Blade, Hydra''s Lament, Shifter''s Shield, Eye of
    the Storm, Heartseeker, Spear of the Magus, Soul Gem, Helm of Radiance, Obsidian
    Shard, Lernaean Bow, Tyrfing, Shield of the Phoenix, Erosion, Eye of Providence,
    Avenging Blade, Nimble Ring, Tekko-Kagi, Stone of Binding, Draconic Scale, Titan''s
    Bane, The Crusher, Screeching Gargoyle, Pharaoh''s Curse, Magi''s Cloak, Silverbranch
    Bow, Bragi''s Harp, The Reaper, Daybreak Gavel, Shogun''s Ofuda, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.4
      efficiency: 0.68
      win: 0.25
      pick: 0.0
      fit: 0.33
    Chronos' Pendant:
      total: 0.45
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.19
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.72
      win: 0.25
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.39
      efficiency: 0.61
      win: 0.25
      pick: 0.19
      fit: 0.38
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.33
      pick: 0.2
      fit: 0.23
    Rod of Asclepius:
      total: 0.46
      efficiency: 0.57
      win: 0.5
      pick: 0.22
      fit: 0.2
  community_ordered:
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Breastplate of Valor, Shield
    Splitter, Soul Gem, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Shifter''s
    Shield, Obsidian Shard, Berserker''s Shield, Hydra''s Lament, Eye of the Storm,
    Heartseeker, Shield of the Phoenix, Erosion, Eye of Providence, Stone of Binding,
    Draconic Scale, Jade Scepter, Doom Orb, Death Metal, Wish-Granting Pearl, Avenging
    Blade, Screeching Gargoyle, Magi''s Cloak, The World Stone, Titan''s Bane, Helm
    of Darkness, Ancient Signet, The Crusher, Mantle Of Discord, Daybreak Gavel, Dreamer''s
    Idol, Genji''s Guard.'
  slot_scores:
    Chronos' Pendant:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.28
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.72
      win: 0.25
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.39
      efficiency: 0.57
      win: 0.25
      pick: 0.23
      fit: 0.42
    Freya's Tears:
      total: 0.4
      efficiency: 0.61
      win: 0.25
      pick: 0.19
      fit: 0.39
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.2
      fit: 0.32
    Rod of Asclepius:
      total: 0.48
      efficiency: 0.57
      win: 0.5
      pick: 0.22
      fit: 0.29
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
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
  - Shifter's Shield
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Genji''s Guard, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Helm of Radiance, Gluttonous Grimoire, Stone of Binding, Magi''s
    Cloak, Screeching Gargoyle, Soul Gem, Mantle Of Discord, Helm of Darkness, Prophetic
    Cloak, Midgardian Mail, Hide of the Nemean Lion, Spear of the Magus, Leviathan''s
    Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.29
      efficiency: 0.66
      win: 0.0
      pick: 0.1
      fit: 0.39
    Breastplate of Valor:
      total: 0.4
      efficiency: 0.65
      win: 0.25
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.56
      win: 0.25
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.43
      efficiency: 0.61
      win: 0.25
      pick: 0.19
      fit: 0.62
    Shifter's Shield:
      total: 0.4
      efficiency: 0.55
      win: 0.25
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.44
      efficiency: 0.65
      win: 0.25
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
