---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.5
  slot_order:
  - name: Prophetic Cloak
    pick_rate: 0.16
    win_rate: 0.63
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.38
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 1.0
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.42
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.4
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.67
    - name: Gladiator's Shield
      pick_rate: 0.1
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.2
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.8
    - name: Ethereal Staff
      pick_rate: 0.11
      win_rate: 0.6
  - name: Divine Ruin
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.8
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.67
  - name: Soul Reaver
    pick_rate: 0.11
    win_rate: 0.33
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.11
      win_rate: 0.33
    - name: Olmec Blue
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.42
    win_rate: 0.62
  - name: Bluestone Pendant
    pick_rate: 0.34
    win_rate: 0.53
  - name: Conduit Gem
    pick_rate: 0.08
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-10-22'
  god_win_rate: 0.54
  god_matches_won: 27
  god_matches_played: 50
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-22'
  god_matches_analyzed: 1760
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  - Erosion
  flex_slots:
  - Breastplate of Valor
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion, Helm of Darkness,
    Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear
    of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.81
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.1
      fit: 0.71
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.71
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.2
      fit: 0.46
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Shifter's Shield
  - Stampede
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  - Erosion
  flex_slots:
  - Stampede
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Shield of the Phoenix, Rod of Tahuti,
    Kinetic Cuirass, Rod of Asclepius, Soul Gem, Erosion, Eye of Providence, Breastplate
    of Valor, Draconic Scale, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace,
    Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.92
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.1
      fit: 0.7
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 1.0
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.2
      fit: 0.48
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Shifter's Shield
  - Stampede
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Shifter's Shield
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Shifter''s Shield, Rod of Tahuti, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Spear of the Magus, Soul Gem, Void Shield, Breastplate of Valor, Obsidian Shard,
    Void Stone, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Doom Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.59
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.1
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic
    Cuirass, Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Helm of Radiance,
    Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the Magus,
    Spear of Desolation, Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle
    Of Discord, Bracer of The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.6
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.1
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shield of the Phoenix
  - Shifter's Shield
  - Spear of Desolation
  flex_slots:
  - Prophetic Cloak
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti,
    Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear
    of Desolation, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Erosion, Helm
    of Radiance, Gluttonous Grimoire, Eye of Providence, Draconic Scale, Stone of
    Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of
    the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.55
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.44
      win: 0.63
      pick: 0.16
      fit: 0.64
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.61
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.1
      fit: 0.45
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Prophetic Cloak
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti, Jotunn''s
    Revenge, Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Runeforged Hammer, Breastplate of Valor, Golden Blade, Gluttonous Grimoire, Eye
    of the Storm, Hydra''s Lament, Heartseeker, Spear of Desolation, Lernaean Bow,
    Tyrfing, Erosion, Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging
    Blade, Helm of Radiance, Soul Gem, Stone of Binding, Shield of the Phoenix, Draconic
    Scale, Obsidian Shard, Titan''s Bane, The Crusher, Pharaoh''s Curse, Magi''s Cloak,
    Nimble Ring, Silverbranch Bow, The Reaper, Shogun''s Ofuda, Screeching Gargoyle,
    Toxic Blade, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.52
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.1
      fit: 0.41
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti,
    Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield
    Splitter, Breastplate of Valor, Spear of Desolation, Spear of the Magus, Runeforged
    Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield, Eye of
    the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence,
    Shield of the Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter,
    Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.1
      fit: 0.42
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the
    Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.42
      pick: 0.33
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.41
      efficiency: 0.61
      win: 0.2
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.1
      fit: 0.71
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
