---
type: smite-build
god: Sylvanus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Grover's Wrath
  aspect_pick_rate: 0.25
  aspect_win_rate: 0.64
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.23
    win_rate: 0.52
    alternates:
    - name: Tyrfing
      pick_rate: 0.21
      win_rate: 0.68
    - name: Stampede
      pick_rate: 0.18
      win_rate: 0.53
  - name: Stampede
    pick_rate: 0.15
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.57
    - name: Bragi's Harp
      pick_rate: 0.14
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.42
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.61
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.68
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.63
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.35
  - name: Spirit Robe
    pick_rate: 0.05
    win_rate: 0.81
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.71
  - name: Sage's Ring
    pick_rate: 0.09
    win_rate: 0.74
    alternates:
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 0.44
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.75
  community_starters:
  - name: Selflessness
    pick_rate: 0.32
    win_rate: 0.56
  - name: Heroism
    pick_rate: 0.18
    win_rate: 0.63
  - name: Death's Embrace
    pick_rate: 0.13
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/sylvanus/
  last_verified: '2026-10-28'
  god_win_rate: 0.5746835443037974
  god_matches_won: 227
  god_matches_played: 395
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-28'
  god_matches_analyzed: 8361
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Draconic Scale
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
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Erosion,
    Eye of Providence, Shield of the Phoenix, Helm of Radiance, Gluttonous Grimoire,
    Stone of Binding, Spear of Desolation, Magi''s Cloak, Screeching Gargoyle, Soul
    Gem, Mantle Of Discord, Helm of Darkness, Rod of Asclepius, Prophetic Cloak, Midgardian
    Mail, Hide of the Nemean Lion, Spear of the Magus, Leviathan''s Hide, Void Shield,
    Ancile, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.73
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.63
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.75
      pick: 0.18
      fit: 0.63
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Draconic Scale
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
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Rod of Asclepius, Soul Gem, Shifter''s Shield, Ethereal Staff, Gluttonous Grimoire,
    Erosion, Eye of Providence, Chandra''s Grace, Lifebinder, Phoenix Feather, Yogi''s
    Necklace, Glorious Pridwen, Helm of Radiance, Spear of Desolation, Sphere of Negation,
    Stone of Binding, Midgardian Mail, Screeching Gargoyle, Jade Scepter, Wish-Granting
    Pearl, Hide of the Nemean Lion, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.36
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.9
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.62
    Draconic Scale:
      total: 0.61
      efficiency: 0.5
      win: 0.75
      pick: 0.18
      fit: 0.62
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Spear of Desolation
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
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
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Stone of Binding,
    Spear of Desolation, Screeching Gargoyle, Kinetic Cuirass, Soul Gem, Spear of
    the Magus, Obsidian Shard, Void Shield, Void Stone, Shifter''s Shield, Doom Orb,
    Helm of Radiance, Erosion, Shield of the Phoenix, Eye of Providence, The World
    Stone, Dreamer''s Idol, Magi''s Cloak, Rod of Asclepius, Mantle Of Discord, Midgardian
    Mail, Chronos'' Pendant, Breastplate of Valor.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.28
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.55
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.75
      pick: 0.18
      fit: 0.45
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Gluttonous Grimoire, Kinetic
    Cuirass, Soul Gem, Shifter''s Shield, Helm of Radiance, Shield of the Phoenix,
    Erosion, Spear of Desolation, Stone of Binding, Eye of Providence, Spear of the
    Magus, Screeching Gargoyle, Rod of Asclepius, Magi''s Cloak, Daybreak Gavel, Obsidian
    Shard, Bracer of The Abyss, Midgardian Mail, Mantle Of Discord, Chronos'' Pendant,
    Jade Scepter, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.21
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.54
      efficiency: 0.44
      win: 0.67
      pick: 0.19
      fit: 0.46
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.75
      pick: 0.18
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Bragi's Harp
  - Draconic Scale
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching Gargoyle, Soul
    Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm of Radiance,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Stone of Binding,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Breastplate
    of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.2
      fit: 0.64
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.46
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.75
      pick: 0.18
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged Hammer, Gluttonous
    Grimoire, Hydra''s Lament, Shifter''s Shield, Spear of Desolation, Eye of the
    Storm, Heartseeker, Spear of the Magus, Soul Gem, Helm of Radiance, Obsidian Shard,
    Lernaean Bow, Shield of the Phoenix, Erosion, Silverbranch Bow, Eye of Providence,
    Avenging Blade, Nimble Ring, Tekko-Kagi, Stone of Binding, Titan''s Bane, Toxic
    Blade, The Crusher, Screeching Gargoyle, Pharaoh''s Curse, Rod of Asclepius, Magi''s
    Cloak, The Reaper, Daybreak Gavel, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.24
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.68
      pick: 0.17
      fit: 0.33
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.52
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.75
      pick: 0.18
      fit: 0.38
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Tyrfing
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Spear of Desolation, Shield
    Splitter, Soul Gem, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Shifter''s
    Shield, Obsidian Shard, Hydra''s Lament, Eye of the Storm, Rod of Asclepius, Heartseeker,
    Shield of the Phoenix, Erosion, Eye of Providence, Stone of Binding, Chronos''
    Pendant, Jade Scepter, Doom Orb, Death Metal, Wish-Granting Pearl, Avenging Blade,
    Screeching Gargoyle, Magi''s Cloak, The World Stone, Titan''s Bane, Helm of Darkness,
    Ancient Signet, The Crusher, Mantle Of Discord, Daybreak Gavel, Dreamer''s Idol,
    Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.25
    Berserker's Shield:
      total: 0.56
      efficiency: 0.6
      win: 0.68
      pick: 0.17
      fit: 0.26
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.5
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.75
      pick: 0.18
      fit: 0.4
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Draconic Scale
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
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield of the Phoenix,
    Helm of Radiance, Gluttonous Grimoire, Stone of Binding, Spear of Desolation,
    Magi''s Cloak, Screeching Gargoyle, Soul Gem, Mantle Of Discord, Helm of Darkness,
    Rod of Asclepius, Prophetic Cloak, Midgardian Mail, Hide of the Nemean Lion, Spear
    of the Magus, Leviathan''s Hide, Void Shield, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.39
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.65
      win: 0.35
      pick: 0.1
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.2
      fit: 0.62
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
---
