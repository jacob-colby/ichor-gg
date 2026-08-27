---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.6
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.24
    win_rate: 0.6
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.24
      win_rate: 0.63
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.5
  - name: Stampede
    pick_rate: 0.2
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.46
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.45
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.81
    - name: Screeching Gargoyle
      pick_rate: 0.11
      win_rate: 0.36
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.65
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.46
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.62
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.25
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.73
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.33
  - name: Legionnaire Armor
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Engraved Guard
      pick_rate: 0.1
      win_rate: 0.5
    - name: Rune
      pick_rate: 0.08
      win_rate: 0.6
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.3
    win_rate: 0.47
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.73
  - name: Heroism
    pick_rate: 0.09
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-08-27'
  god_win_rate: 0.5354330708661418
  god_matches_won: 68
  god_matches_played: 127
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Breastplate of Valor,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding,
    Helm of Radiance, Magi''s Cloak, Gluttonous Grimoire, Mantle Of Discord, Midgardian
    Mail, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Ancile, Spear of
    Desolation, Nimble Ring, Helm of Darkness, Oni Hunter''s Garb, Rod of Asclepius,
    Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.35
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.73
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.24
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.5
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.63
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Rod of Asclepius, Soul Gem, Breastplate of Valor, Erosion, Eye of Providence,
    Ethereal Staff, Draconic Scale, Gluttonous Grimoire, Phoenix Feather, Yogi''s
    Necklace, Chandra''s Grace, Lifebinder, Glorious Pridwen, Stone of Binding, Midgardian
    Mail, Helm of Radiance, Hide of the Nemean Lion, Sphere of Negation, Leviathan''s
    Hide, Magi''s Cloak, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.31
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.85
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.24
      fit: 0.61
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Spear of Desolation, Spear of the Magus, Void Shield, Soul Gem,
    Breastplate of Valor, Obsidian Shard, Void Stone, Erosion, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance, The World Stone,
    Magi''s Cloak, Dreamer''s Idol, Nimble Ring, Mantle Of Discord, Midgardian Mail,
    Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.25
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.24
      fit: 0.45
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.51
      pick: 0.0
      fit: 0.38
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Helm of Radiance, Erosion, Stone of
    Binding, Eye of Providence, Shield of the Phoenix, Draconic Scale, Magi''s Cloak,
    Daybreak Gavel, Spear of the Magus, Spear of Desolation, Bragi''s Harp, Rod of
    Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard,
    Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.2
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.51
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.24
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Spear of Desolation
  flex_slots:
  - Shield of the Phoenix
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Soul
    Gem, Chronos'' Pendant, Helm of Radiance, Gluttonous Grimoire, Erosion, Eye of
    Providence, Stone of Binding, Gladiator''s Shield, Draconic Scale, Nimble Ring,
    Gem of Focus, Magi''s Cloak, Spear of the Magus, Rod of Asclepius, Eye of Erebus,
    Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.45
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.52
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.24
      fit: 0.42
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Breastplate
    of Valor, Golden Blade, Gluttonous Grimoire, Eye of the Storm, Hydra''s Lament,
    Heartseeker, Tyrfing, Spear of Desolation, Lernaean Bow, Erosion, Spear of the
    Magus, Tekko-Kagi, Eye of Providence, Avenging Blade, Helm of Radiance, Soul Gem,
    Stone of Binding, Shield of the Phoenix, Draconic Scale, Obsidian Shard, Titan''s
    Bane, The Crusher, Pharaoh''s Curse, Silverbranch Bow, Magi''s Cloak, Nimble Ring,
    The Reaper, Toxic Blade, Shogun''s Ofuda, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.23
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.51
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.24
      fit: 0.41
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Gluttonous Grimoire, Breastplate
    of Valor, Shield Splitter, Spear of Desolation, Spear of the Magus, Runeforged
    Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Golden Blade, Nimble Ring,
    Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion, Eye
    of Providence, Stone of Binding, Shield of the Phoenix, Draconic Scale, Tyrfing,
    Lernaean Bow, Bragi''s Harp, Jade Scepter, Doom Orb, Wish-Granting Pearl, Avenging
    Blade, Death Metal, Magi''s Cloak, Chronos'' Pendant, Tekko-Kagi, Pharaoh''s Curse,
    The World Stone, Silverbranch Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.21
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.49
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.24
      fit: 0.39
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.39
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone
    of Binding, Helm of Radiance, Magi''s Cloak, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Hide of the Nemean Lion, Leviathan''s Hide, Prophetic Cloak,
    Void Shield, Ancile, Spear of Desolation, Nimble Ring, Helm of Darkness, Oni Hunter''s
    Garb, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.35
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.42
      efficiency: 0.61
      win: 0.25
      pick: 0.17
      fit: 0.57
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.24
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.63
  starter: *id001
---
