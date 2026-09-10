---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.63
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.2
    win_rate: 0.6
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.16
      win_rate: 0.5
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.8
  - name: Heartwood Charm
    pick_rate: 0.1
    win_rate: 0.2
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.6
    - name: Chandra's Grace
      pick_rate: 0.08
      win_rate: 0.75
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.67
    alternates:
    - name: Rod of Asclepius
      pick_rate: 0.08
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.75
  - name: Stampede
    pick_rate: 0.08
    win_rate: 0.75
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.57
    - name: Heartwood Charm
      pick_rate: 0.1
      win_rate: 0.6
  - name: Shell of Rebuke
    pick_rate: 0.16
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.5
    - name: Chronos' Pendant
      pick_rate: 0.05
      win_rate: 1.0
  - name: Rod of Asclepius
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Engraved Guard
      pick_rate: 0.1
      win_rate: 0.0
    - name: Void Shard
      pick_rate: 0.1
      win_rate: 0.5
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.45
    win_rate: 0.61
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.5
  - name: Heroism
    pick_rate: 0.1
    win_rate: 0.2
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-09-10'
  god_win_rate: 0.5686274509803921
  god_matches_won: 29
  god_matches_played: 51
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  - Stampede
  flex_slots:
  - Stampede
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Stampede, Kinetic Cuirass, Genji''s Guard,
    Shifter''s Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield of
    the Phoenix, Draconic Scale, Helm of Radiance, Gluttonous Grimoire, Stone of Binding,
    Magi''s Cloak, Screeching Gargoyle, Soul Gem, Mantle Of Discord, Helm of Darkness,
    Prophetic Cloak, Midgardian Mail, Hide of the Nemean Lion, Spear of the Magus,
    Leviathan''s Hide, Void Shield, Ancile.'
  slot_scores:
    Chronos' Pendant:
      total: 0.69
      efficiency: 0.55
      win: 1.0
      pick: 0.11
      fit: 0.31
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.62
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.2
    Rod of Asclepius:
      total: 0.71
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.33
    Stampede:
      total: 0.58
      efficiency: 0.51
      win: 0.75
      pick: 0.13
      fit: 0.41
  community_ordered:
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Asclepius
  - Stampede
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Rod of Asclepius
  - Stampede
  flex_slots:
  - Rod of Tahuti
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Genji''s Guard, Shifter''s Shield, Breastplate of Valor, Ethereal Staff,
    Gluttonous Grimoire, Erosion, Eye of Providence, Draconic Scale, Lifebinder, Phoenix
    Feather, Yogi''s Necklace, Glorious Pridwen, Helm of Radiance, Sphere of Negation,
    Stone of Binding, Midgardian Mail, Screeching Gargoyle, Jade Scepter, Wish-Granting
    Pearl, Hide of the Nemean Lion.'
  slot_scores:
    Chronos' Pendant:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.11
      fit: 0.33
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.55
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.21
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.92
    Rod of Asclepius:
      total: 0.77
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.69
    Stampede:
      total: 0.59
      efficiency: 0.51
      win: 0.75
      pick: 0.13
      fit: 0.43
  community_ordered:
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Asclepius
  - Stampede
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  - Stampede
  flex_slots:
  - Stampede
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Chronos'' Pendant, Rod of Tahuti, Amanita Charm, Gluttonous Grimoire,
    Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Genji''s Guard, Soul Gem,
    Spear of the Magus, Breastplate of Valor, Obsidian Shard, Void Shield, Void Stone,
    Shifter''s Shield, Doom Orb, Helm of Radiance, Erosion, Shield of the Phoenix,
    Eye of Providence, The World Stone, Draconic Scale, Dreamer''s Idol, Magi''s Cloak,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Chronos' Pendant:
      total: 0.68
      efficiency: 0.55
      win: 1.0
      pick: 0.11
      fit: 0.22
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.2
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.44
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.43
    Rod of Asclepius:
      total: 0.7
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.23
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.75
      pick: 0.13
      fit: 0.29
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
  - Rod of Asclepius
  - Stampede
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
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Rod of Tahuti, Amanita Charm, Nimble Ring, Genji''s
    Guard, Gluttonous Grimoire, Kinetic Cuirass, Breastplate of Valor, Soul Gem, Shifter''s
    Shield, Helm of Radiance, Shield of the Phoenix, Erosion, Stone of Binding, Eye
    of Providence, Spear of the Magus, Draconic Scale, Screeching Gargoyle, Bragi''s
    Harp, Magi''s Cloak, Daybreak Gavel, Obsidian Shard, Bracer of The Abyss, Midgardian
    Mail, Mantle Of Discord, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.67
      efficiency: 0.55
      win: 1.0
      pick: 0.11
      fit: 0.17
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.6
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.11
    Rod of Asclepius:
      total: 0.69
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.18
  community_ordered:
  - Chronos' Pendant
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Asclepius
  - Stampede
  flex_slots:
  - Breastplate of Valor
  - Stampede
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Rod of Tahuti,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of
    the Phoenix, Screeching Gargoyle, Soul Gem, Shifter''s Shield, Prophetic Cloak,
    Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Eye of
    Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail,
    Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.14
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.11
      fit: 0.42
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.64
    Rod of Asclepius:
      total: 0.7
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.22
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.75
      pick: 0.13
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Asclepius
  - Stampede
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  - Stampede
  flex_slots:
  - Freya's Tears
  - Stampede
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Genji''s Guard, Kinetic Cuirass, Breastplate of Valor,
    Shield Splitter, Runeforged Hammer, Gluttonous Grimoire, Golden Blade, Hydra''s
    Lament, Shifter''s Shield, Eye of the Storm, Heartseeker, Spear of the Magus,
    Soul Gem, Helm of Radiance, Obsidian Shard, Lernaean Bow, Tyrfing, Shield of the
    Phoenix, Erosion, Eye of Providence, Avenging Blade, Nimble Ring, Tekko-Kagi,
    Stone of Binding, Draconic Scale, Titan''s Bane, The Crusher, Screeching Gargoyle,
    Pharaoh''s Curse, Magi''s Cloak, Silverbranch Bow, Bragi''s Harp, The Reaper,
    Daybreak Gavel, Shogun''s Ofuda.'
  slot_scores:
    Chronos' Pendant:
      total: 0.68
      efficiency: 0.55
      win: 1.0
      pick: 0.11
      fit: 0.19
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.38
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.23
    Rod of Asclepius:
      total: 0.69
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.2
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.75
      pick: 0.13
      fit: 0.25
  community_ordered:
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Asclepius
  - Stampede
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Stampede
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Rod of Tahuti,
    Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Shield Splitter, Soul Gem, Spear of the Magus,
    Runeforged Hammer, Helm of Radiance, Shifter''s Shield, Obsidian Shard, Berserker''s
    Shield, Hydra''s Lament, Eye of the Storm, Heartseeker, Shield of the Phoenix,
    Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Jade Scepter, Doom
    Orb, Death Metal, Wish-Granting Pearl, Avenging Blade, Screeching Gargoyle, Magi''s
    Cloak, The World Stone, Titan''s Bane, Helm of Darkness, Ancient Signet, The Crusher,
    Mantle Of Discord, Daybreak Gavel, Dreamer''s Idol.'
  slot_scores:
    Chronos' Pendant:
      total: 0.69
      efficiency: 0.55
      win: 1.0
      pick: 0.11
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.39
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.32
    Rod of Asclepius:
      total: 0.71
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.29
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.75
      pick: 0.13
      fit: 0.26
  community_ordered:
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Asclepius
  - Stampede
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Genji''s
    Guard, Shifter''s Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield
    of the Phoenix, Draconic Scale, Helm of Radiance, Gluttonous Grimoire, Stone of
    Binding, Magi''s Cloak, Screeching Gargoyle, Soul Gem, Mantle Of Discord, Helm
    of Darkness, Prophetic Cloak, Midgardian Mail, Hide of the Nemean Lion, Spear
    of the Magus, Leviathan''s Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.14
      fit: 0.39
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.62
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
