---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.62
  aspect_win_rate: 0.53
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.4
    win_rate: 0.51
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.14
      win_rate: 0.5
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.61
  - name: Stampede
    pick_rate: 0.2
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.6
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.42
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.41
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.47
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.65
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.48
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.4
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.54
  - name: Rod of Tahuti
    pick_rate: 0.07
    win_rate: 0.64
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.61
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.62
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.64
    alternates:
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.44
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.86
  community_starters:
  - name: Selflessness
    pick_rate: 0.36
    win_rate: 0.45
  - name: Heroism
    pick_rate: 0.24
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-10-15'
  god_win_rate: 0.5121951219512195
  god_matches_won: 147
  god_matches_played: 287
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-15'
  god_matches_analyzed: 9899
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Hide of the Nemean Lion
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Hide of the Nemean Lion, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Leviathan''s
    Hide, Helm of Darkness, Void Shield, Spear of Desolation, Ancile, Oni Hunter''s
    Garb, Gladiator''s Shield, Xibalban Effigy, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.4
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.8
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.62
      pick: 0.13
      fit: 0.45
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Hide of the Nemean
    Lion, Rod of Asclepius, Shifter''s Shield, Soul Gem, Breastplate of Valor, Erosion,
    Eye of Providence, Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix
    Feather, Yogi''s Necklace, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian
    Mail, Stone of Binding, Helm of Radiance, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.93
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.13
      fit: 0.47
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.98
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Amanita Charm, Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass,
    Hide of the Nemean Lion, Screeching Gargoyle, Spear of Desolation, Soul Gem, Spear
    of the Magus, Void Shield, Breastplate of Valor, Obsidian Shard, Void Stone, Shifter''s
    Shield, Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Doom
    Orb, Helm of Radiance, The World Stone, Magi''s Cloak, Dreamer''s Idol, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.28
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.59
    Hide of the Nemean Lion:
      total: 0.51
      efficiency: 0.52
      win: 0.62
      pick: 0.13
      fit: 0.31
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.64
      pick: 0.15
      fit: 0.41
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
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
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Nimble Ring, Hide of the Nemean Lion, Kinetic Cuirass,
    Gluttonous Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of
    Radiance, Erosion, Shield of the Phoenix, Stone of Binding, Eye of Providence,
    Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Spear of Desolation, Spear
    of the Magus, Daybreak Gavel, Bragi''s Harp, Rod of Asclepius, Midgardian Mail,
    Mantle Of Discord, Bracer of The Abyss, Obsidian Shard, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.21
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
      fit: 0.3
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.51
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.64
      pick: 0.15
      fit: 0.08
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching Gargoyle,
    Soul Gem, Shifter''s Shield, Chronos'' Pendant, Erosion, Helm of Radiance, Gluttonous
    Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Prophetic
    Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.61
    Hide of the Nemean Lion:
      total: 0.51
      efficiency: 0.52
      win: 0.62
      pick: 0.13
      fit: 0.29
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.64
      pick: 0.15
      fit: 0.13
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita
    Charm, Kinetic Cuirass, Shield Splitter, Golden Blade, Breastplate of Valor, Runeforged
    Hammer, Shifter''s Shield, Gluttonous Grimoire, Eye of the Storm, Tyrfing, Hydra''s
    Lament, Heartseeker, Spear of Desolation, Lernaean Bow, Spear of the Magus, Erosion,
    Silverbranch Bow, Tekko-Kagi, Eye of Providence, Soul Gem, Shield of the Phoenix,
    Avenging Blade, Helm of Radiance, Stone of Binding, Draconic Scale, Toxic Blade,
    Obsidian Shard, Titan''s Bane, The Crusher, Pharaoh''s Curse, Nimble Ring, Magi''s
    Cloak, The Reaper, Screeching Gargoyle, Shogun''s Ofuda, Mantle Of Discord, Midgardian
    Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.05
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.22
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
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.22
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.64
      pick: 0.15
      fit: 0.2
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Gluttonous Grimoire, Breastplate of Valor, Spear of Desolation,
    Shield Splitter, Spear of the Magus, Soul Gem, Runeforged Hammer, Helm of Radiance,
    Shifter''s Shield, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the
    Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death Metal,
    Wish-Granting Pearl, Avenging Blade, Chronos'' Pendant, Magi''s Cloak, The World
    Stone, Helm of Darkness, Titan''s Bane, Screeching Gargoyle, Ancient Signet, The
    Crusher, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.18
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.64
      pick: 0.15
      fit: 0.32
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Screeching Gargoyle, Midgardian Mail, Prophetic Cloak, Hide of the Nemean Lion,
    Leviathan''s Hide, Helm of Darkness, Void Shield, Spear of Desolation, Ancile,
    Oni Hunter''s Garb, Gladiator''s Shield, Xibalban Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.4
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.41
      pick: 0.2
      fit: 0.65
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
