---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.47
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.14
    win_rate: 0.48
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.13
      win_rate: 0.46
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.55
  - name: Totem of Death
    pick_rate: 0.14
    win_rate: 0.46
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.52
    - name: Soul Reaver
      pick_rate: 0.1
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.45
    alternates:
    - name: Totem of Death
      pick_rate: 0.14
      win_rate: 0.48
    - name: The Cosmic Horror
      pick_rate: 0.12
      win_rate: 0.46
  - name: Omen Drum
    pick_rate: 0.1
    win_rate: 0.44
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.57
    - name: The Cosmic Horror
      pick_rate: 0.08
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Omen Drum
      pick_rate: 0.08
      win_rate: 0.44
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.36
  - name: Void Shard
    pick_rate: 0.05
    win_rate: 0.29
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.65
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.48
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.38
    win_rate: 0.39
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.54
  - name: War Flag
    pick_rate: 0.07
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-08-24'
  god_win_rate: 0.484394506866417
  god_matches_won: 388
  god_matches_played: 801
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-24'
  god_matches_analyzed: 17273
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Freya''s Tears, Shifter''s Shield, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion,
    Helm of Darkness, Leviathan''s Hide, Void Shield, Stampede, Ancile, Oni Hunter''s
    Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.45
      pick: 0.2
      fit: 0.39
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.48
      pick: 0.14
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Shifter''s Shield,
    Freya''s Tears, Rod of Asclepius, Soul Gem, Erosion, Eye of Providence, Breastplate
    of Valor, Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather,
    Yogi''s Necklace, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail,
    Stone of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide,
    Void Shield, Stampede, Magi''s Cloak, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.45
      pick: 0.2
      fit: 0.36
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.57
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.48
      pick: 0.14
      fit: 0.7
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass,
    Freya''s Tears, Screeching Gargoyle, Shifter''s Shield, Spear of Desolation, Spear
    of the Magus, Soul Gem, Void Shield, Breastplate of Valor, Obsidian Shard, Void
    Stone, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom
    Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.49
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.5
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.49
      efficiency: 0.55
      win: 0.48
      pick: 0.14
      fit: 0.49
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Nimble Ring, Kinetic Cuirass, Freya''s Tears, Gluttonous
    Grimoire, Shifter''s Shield, Breastplate of Valor, Soul Gem, Helm of Radiance,
    Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the Magus,
    Spear of Desolation, Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle
    Of Discord, Bracer of The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.43
      efficiency: 0.44
      win: 0.47
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.5
      pick: 0.15
      fit: 0.08
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Shifter''s Shield, Spear
    of Desolation, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Prophetic Cloak,
    Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of
    Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen,
    Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.45
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.48
      efficiency: 0.55
      win: 0.48
      pick: 0.14
      fit: 0.45
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.45
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
  - Freya's Tears
  - Shield Splitter
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita
    Charm, Kinetic Cuirass, Freya''s Tears, Shield Splitter, Shifter''s Shield, Runeforged
    Hammer, Breastplate of Valor, Golden Blade, Gluttonous Grimoire, Eye of the Storm,
    Hydra''s Lament, Heartseeker, Spear of Desolation, Lernaean Bow, Tyrfing, Erosion,
    Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging Blade, Helm of Radiance,
    Soul Gem, Stone of Binding, Shield of the Phoenix, Draconic Scale, Obsidian Shard,
    Titan''s Bane, The Crusher, Pharaoh''s Curse, Magi''s Cloak, Nimble Ring, Silverbranch
    Bow, The Reaper, Shogun''s Ofuda, Screeching Gargoyle, Toxic Blade, Mantle Of
    Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.48
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Gluttonous Grimoire, Freya''s Tears, Shifter''s Shield, Shield
    Splitter, Breastplate of Valor, Spear of Desolation, Spear of the Magus, Runeforged
    Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield, Eye of
    the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence,
    Shield of the Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter,
    Death Metal, Chronos'' Pendant, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.45
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.38
    Shifter's Shield:
      total: 0.48
      efficiency: 0.55
      win: 0.48
      pick: 0.14
      fit: 0.42
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.42
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Freya''s Tears, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak,
    Hide of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.45
      pick: 0.2
      fit: 0.39
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.48
      pick: 0.14
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.71
  starter: *id001
---
