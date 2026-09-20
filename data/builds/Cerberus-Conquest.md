---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.54
  slot_order:
  - name: Stampede
    pick_rate: 0.26
    win_rate: 0.59
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.24
      win_rate: 0.51
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.56
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.52
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.64
  - name: Shell of Rebuke
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.54
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.54
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.62
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.17
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.65
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.64
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.58
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.48
    alternates:
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.79
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.44
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.26
    win_rate: 0.49
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.65
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-09-20'
  god_win_rate: 0.5647530040053405
  god_matches_won: 423
  god_matches_played: 749
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-20'
  god_matches_analyzed: 14083
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Breastplate of Valor, Kinetic Cuirass,
    Draconic Scale, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Helm of Radiance, Magi''s Cloak, Gluttonous Grimoire, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Leviathan''s Hide, Prophetic
    Cloak, Void Shield, Ancile, Spear of Desolation, Nimble Ring, Helm of Darkness,
    Oni Hunter''s Garb, Rod of Asclepius.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.12
      fit: 0.35
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.27
      fit: 0.35
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.32
      fit: 0.57
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.61
      pick: 0.11
      fit: 0.63
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Breastplate of
    Valor, Kinetic Cuirass, Rod of Asclepius, Draconic Scale, Soul Gem, Erosion, Eye
    of Providence, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace,
    Chandra''s Grace, Lifebinder, Glorious Pridwen, Stone of Binding, Midgardian Mail,
    Helm of Radiance, Hide of the Nemean Lion, Sphere of Negation, Leviathan''s Hide,
    Magi''s Cloak, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.12
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.85
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.62
      pick: 0.32
      fit: 0.5
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.61
      pick: 0.11
      fit: 0.61
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Rod of Tahuti, Breastplate of Valor, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Spear of the Magus, Void Shield, Soul Gem, Draconic Scale, Obsidian Shard, Void
    Stone, Erosion, Eye of Providence, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    The World Stone, Magi''s Cloak, Dreamer''s Idol, Nimble Ring, Mantle Of Discord,
    Midgardian Mail, Rod of Asclepius.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.72
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.64
      pick: 0.12
      fit: 0.25
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.32
      fit: 0.41
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
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
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Breastplate of Valor, Amanita Charm, Nimble Ring, Kinetic
    Cuirass, Gluttonous Grimoire, Draconic Scale, Soul Gem, Helm of Radiance, Erosion,
    Stone of Binding, Eye of Providence, Shield of the Phoenix, Magi''s Cloak, Screeching
    Gargoyle, Daybreak Gavel, Spear of the Magus, Spear of Desolation, Bragi''s Harp,
    Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian
    Shard, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.64
      pick: 0.12
      fit: 0.2
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.32
      fit: 0.33
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Rod of Tahuti,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Draconic Scale, Chronos'' Pendant, Helm of Radiance, Prophetic
    Cloak, Gluttonous Grimoire, Erosion, Eye of Providence, Stone of Binding, Gladiator''s
    Shield, Nimble Ring, Gem of Focus, Magi''s Cloak, Spear of the Magus, Rod of Asclepius,
    Eye of Erebus, Mantle Of Discord, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.64
      pick: 0.12
      fit: 0.45
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.27
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.32
      fit: 0.59
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Breastplate
    of Valor, Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Runeforged Hammer, Golden Blade, Draconic Scale, Gluttonous Grimoire, Eye of the
    Storm, Hydra''s Lament, Heartseeker, Tyrfing, Spear of Desolation, Lernaean Bow,
    Erosion, Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging Blade, Helm
    of Radiance, Soul Gem, Stone of Binding, Shield of the Phoenix, Obsidian Shard,
    Titan''s Bane, The Crusher, Pharaoh''s Curse, Silverbranch Bow, Magi''s Cloak,
    Nimble Ring, The Reaper, Toxic Blade, Shogun''s Ofuda, Screeching Gargoyle, Mantle
    Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.64
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.32
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Gluttonous
    Grimoire, Shield Splitter, Spear of Desolation, Spear of the Magus, Runeforged
    Hammer, Draconic Scale, Helm of Radiance, Soul Gem, Obsidian Shard, Golden Blade,
    Nimble Ring, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker,
    Erosion, Eye of Providence, Stone of Binding, Shield of the Phoenix, Tyrfing,
    Lernaean Bow, Bragi''s Harp, Jade Scepter, Doom Orb, Wish-Granting Pearl, Avenging
    Blade, Death Metal, Magi''s Cloak, Chronos'' Pendant, Tekko-Kagi, Pharaoh''s Curse,
    The World Stone, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.64
      pick: 0.12
      fit: 0.21
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.32
      fit: 0.35
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
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
    Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion, Leviathan''s Hide,
    Prophetic Cloak, Void Shield, Ancile, Spear of Desolation, Nimble Ring, Helm of
    Darkness, Oni Hunter''s Garb, Rod of Asclepius.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.12
      fit: 0.35
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.27
      fit: 0.35
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.73
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.51
      pick: 0.24
      fit: 0.63
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.32
      fit: 0.57
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
---
