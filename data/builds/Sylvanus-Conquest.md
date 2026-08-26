---
type: smite-build
god: Sylvanus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Grover's Wrath
  aspect_pick_rate: 0.23
  aspect_win_rate: 0.75
  slot_order:
  - name: Tyrfing
    pick_rate: 0.21
    win_rate: 0.73
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.33
    - name: Amanita Charm
      pick_rate: 0.12
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.73
    alternates:
    - name: Bragi's Harp
      pick_rate: 0.1
      win_rate: 0.6
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.4
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.25
      win_rate: 0.23
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.2
  - name: Qin's Blade
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.8
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.25
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.5
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 1.0
  - name: Medal of Defense
    pick_rate: 0.08
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
    - name: Legionnaire Armor
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.31
    win_rate: 0.5
  - name: Death's Toll
    pick_rate: 0.13
    win_rate: 0.71
  - name: Heroism
    pick_rate: 0.12
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/sylvanus/
  last_verified: '2026-08-26'
  god_win_rate: 0.5384615384615384
  god_matches_won: 28
  god_matches_played: 52
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Erosion,
    Eye of Providence, Shield of the Phoenix, Amanita Charm, Helm of Radiance, Gluttonous
    Grimoire, Stone of Binding, Spear of Desolation, Magi''s Cloak, Screeching Gargoyle,
    Soul Gem, Mantle Of Discord, Helm of Darkness, Rod of Asclepius, Prophetic Cloak,
    Midgardian Mail, Hide of the Nemean Lion, Spear of the Magus, Leviathan''s Hide,
    Void Shield, Ancile, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.73
      pick: 0.29
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.6
      pick: 0.16
      fit: 0.62
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.64
      pick: 0.0
      fit: 0.63
    Draconic Scale:
      total: 0.73
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.63
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.64
      pick: 0.0
      fit: 0.63
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
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Shield of the Phoenix, Amanita Charm,
    Kinetic Cuirass, Rod of Asclepius, Soul Gem, Shifter''s Shield, Ethereal Staff,
    Gluttonous Grimoire, Erosion, Eye of Providence, Chandra''s Grace, Lifebinder,
    Phoenix Feather, Yogi''s Necklace, Glorious Pridwen, Helm of Radiance, Spear of
    Desolation, Sphere of Negation, Stone of Binding, Midgardian Mail, Screeching
    Gargoyle, Jade Scepter, Wish-Granting Pearl, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.73
      pick: 0.29
      fit: 0.36
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.16
      fit: 0.55
    Draconic Scale:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.62
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.12
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Draconic Scale, Rod of Tahuti, Gluttonous Grimoire, Stone of Binding,
    Spear of Desolation, Screeching Gargoyle, Kinetic Cuirass, Soul Gem, Spear of
    the Magus, Obsidian Shard, Void Shield, Void Stone, Shifter''s Shield, Doom Orb,
    Helm of Radiance, Erosion, Shield of the Phoenix, Eye of Providence, The World
    Stone, Amanita Charm, Dreamer''s Idol, Magi''s Cloak, Rod of Asclepius, Mantle
    Of Discord, Midgardian Mail, Chronos'' Pendant.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.51
      win: 0.64
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.73
      pick: 0.29
      fit: 0.28
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.55
      win: 0.64
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.55
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.45
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.64
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Nimble Ring, Gluttonous Grimoire, Kinetic
    Cuirass, Soul Gem, Shifter''s Shield, Helm of Radiance, Shield of the Phoenix,
    Erosion, Spear of Desolation, Stone of Binding, Eye of Providence, Spear of the
    Magus, Amanita Charm, Screeching Gargoyle, Rod of Asclepius, Magi''s Cloak, Daybreak
    Gavel, Obsidian Shard, Bracer of The Abyss, Midgardian Mail, Mantle Of Discord,
    Chronos'' Pendant, Jade Scepter, Bragi''s Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.73
      pick: 0.29
      fit: 0.21
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.6
      pick: 0.14
      fit: 0.46
    Draconic Scale:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.34
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.64
      pick: 0.0
      fit: 0.11
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  flex_slots:
  - Shield of the Phoenix
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Kinetic
    Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching Gargoyle, Soul
    Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm of Radiance,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Amanita Charm, Stone
    of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear
    of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.73
      pick: 0.29
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.6
      pick: 0.16
      fit: 0.64
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.46
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - Draconic Scale
  flex_slots:
  - Tyrfing
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged
    Hammer, Gluttonous Grimoire, Hydra''s Lament, Shifter''s Shield, Spear of Desolation,
    Eye of the Storm, Heartseeker, Spear of the Magus, Soul Gem, Helm of Radiance,
    Obsidian Shard, Lernaean Bow, Shield of the Phoenix, Erosion, Silverbranch Bow,
    Eye of Providence, Avenging Blade, Nimble Ring, Tekko-Kagi, Stone of Binding,
    Amanita Charm, Titan''s Bane, Toxic Blade, The Crusher, Screeching Gargoyle, Pharaoh''s
    Curse, Rod of Asclepius, Magi''s Cloak, The Reaper, Daybreak Gavel, Bragi''s Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.73
      pick: 0.29
      fit: 0.24
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.73
      pick: 0.21
      fit: 0.52
    Qin's Blade:
      total: 0.65
      efficiency: 0.37
      win: 1.0
      pick: 0.15
      fit: 0.41
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Qin's Blade
  - Draconic Scale
  flex_slots:
  - Kinetic Cuirass
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Jotunn''s
    Revenge, Kinetic Cuirass, Gluttonous Grimoire, Spear of Desolation, Shield Splitter,
    Soul Gem, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Shifter''s
    Shield, Obsidian Shard, Berserker''s Shield, Hydra''s Lament, Eye of the Storm,
    Rod of Asclepius, Heartseeker, Shield of the Phoenix, Erosion, Eye of Providence,
    Stone of Binding, Amanita Charm, Chronos'' Pendant, Jade Scepter, Doom Orb, Death
    Metal, Wish-Granting Pearl, Avenging Blade, Screeching Gargoyle, Magi''s Cloak,
    The World Stone, Titan''s Bane, Helm of Darkness, Ancient Signet, The Crusher,
    Mantle Of Discord, Daybreak Gavel, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.73
      pick: 0.29
      fit: 0.25
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.55
      win: 0.64
      pick: 0.0
      fit: 0.53
    Qin's Blade:
      total: 0.6
      efficiency: 0.27
      win: 1.0
      pick: 0.15
      fit: 0.34
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.4
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Shifter''s
    Shield, Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Helm
    of Radiance, Gluttonous Grimoire, Stone of Binding, Spear of Desolation, Magi''s
    Cloak, Screeching Gargoyle, Soul Gem, Mantle Of Discord, Helm of Darkness, Rod
    of Asclepius, Prophetic Cloak, Midgardian Mail, Hide of the Nemean Lion, Spear
    of the Magus, Leviathan''s Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.73
      pick: 0.29
      fit: 0.39
    Breastplate of Valor:
      total: 0.39
      efficiency: 0.65
      win: 0.2
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.6
      pick: 0.16
      fit: 0.62
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.64
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.12
      fit: 0.63
  starter: *id001
---
