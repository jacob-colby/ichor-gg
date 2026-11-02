---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.36
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.5
    win_rate: 0.5
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.55
    - name: Yogi's Necklace
      pick_rate: 0.04
      win_rate: 0.47
  - name: Stampede
    pick_rate: 0.27
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.26
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.54
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.58
  - name: Freya's Tears
    pick_rate: 0.22
    win_rate: 0.45
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.19
      win_rate: 0.62
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.52
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.75
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.59
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.55
  - name: Sage's Ring
    pick_rate: 0.09
    win_rate: 0.44
    alternates:
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 0.56
    - name: Spectral Armor
      pick_rate: 0.07
      win_rate: 0.46
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.28
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.52
  - name: Archmage's Gem
    pick_rate: 0.14
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-10-30'
  god_win_rate: 0.5231481481481481
  god_matches_won: 226
  god_matches_played: 432
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield of the Phoenix,
    Stone of Binding, Gluttonous Grimoire, Helm of Radiance, Magi''s Cloak, Mantle
    Of Discord, Midgardian Mail, Oni Hunter''s Garb, Screeching Gargoyle, Leviathan''s
    Hide, Hide of the Nemean Lion, Void Shield, Spear of Desolation, Ancile, Prophetic
    Cloak, Helm of Darkness, Rod of Asclepius, Nimble Ring.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.19
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.73
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.45
      pick: 0.37
      fit: 0.57
    Draconic Scale:
      total: 0.61
      efficiency: 0.5
      win: 0.75
      pick: 0.11
      fit: 0.63
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
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
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Amanita Charm, Rod of Tahuti, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Shifter''s Shield, Soul Gem, Breastplate of
    Valor, Erosion, Ethereal Staff, Eye of Providence, Gluttonous Grimoire, Phoenix
    Feather, Chandra''s Grace, Lifebinder, Glorious Pridwen, Midgardian Mail, Helm
    of Radiance, Oni Hunter''s Garb, Stone of Binding, Leviathan''s Hide, Hide of
    the Nemean Lion, Sphere of Negation, Void Shield, Yogi''s Necklace, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.85
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.61
    Draconic Scale:
      total: 0.61
      efficiency: 0.5
      win: 0.75
      pick: 0.11
      fit: 0.61
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Draconic Scale
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Draconic Scale, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Spear of the Magus, Void Shield, Soul Gem, Obsidian Shard, Breastplate of Valor,
    Void Stone, Shifter''s Shield, Erosion, Eye of Providence, Shield of the Phoenix,
    Helm of Radiance, Doom Orb, The World Stone, Dreamer''s Idol, Magi''s Cloak, Midgardian
    Mail, Nimble Ring, Mantle Of Discord, Oni Hunter''s Garb.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.5
      win: 0.52
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.52
      efficiency: 0.5
      win: 0.52
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.19
      fit: 0.25
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.55
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.75
      pick: 0.11
      fit: 0.45
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
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
    this god: Draconic Scale, Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass,
    Gluttonous Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of
    Radiance, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Spear of the Magus, Spear of Desolation, Daybreak Gavel, Bragi''s
    Harp, Midgardian Mail, Rod of Asclepius, Screeching Gargoyle, Oni Hunter''s Garb,
    Mantle Of Discord, Bracer of The Abyss, Lotus Sickle, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.54
      pick: 0.19
      fit: 0.2
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.52
      pick: 0.0
      fit: 0.44
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.75
      pick: 0.11
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
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
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Breastplate
    of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Soul Gem, Lotus Sickle, Screeching Gargoyle, Shifter''s Shield, Chronos'' Pendant,
    Helm of Radiance, Gluttonous Grimoire, Erosion, Prophetic Cloak, Eye of Providence,
    Gladiator''s Shield, Stone of Binding, Nimble Ring, Gem of Focus, Spear of the
    Magus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Midgardian Mail, Daybreak
    Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.19
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.45
      pick: 0.37
      fit: 0.59
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.75
      pick: 0.11
      fit: 0.42
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.42
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
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
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
    win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Breastplate of Valor, Golden Blade, Gluttonous Grimoire, Eye of the Storm,
    Shifter''s Shield, Hydra''s Lament, Heartseeker, Spear of Desolation, Tyrfing,
    Spear of the Magus, Erosion, Lernaean Bow, Eye of Providence, Tekko-Kagi, Helm
    of Radiance, Avenging Blade, Soul Gem, Shield of the Phoenix, Obsidian Shard,
    Stone of Binding, Titan''s Bane, The Crusher, Pharaoh''s Curse, Silverbranch Bow,
    Nimble Ring, Magi''s Cloak, The Reaper, Toxic Blade, Shogun''s Ofuda, Midgardian
    Mail, Daybreak Gavel, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.19
      fit: 0.23
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.51
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.75
      pick: 0.11
      fit: 0.41
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Draconic Scale, Jotunn''s
    Revenge, Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Spear of the Magus, Shield Splitter, Breastplate of Valor,
    Helm of Radiance, Runeforged Hammer, Soul Gem, Obsidian Shard, Shifter''s Shield,
    Golden Blade, Nimble Ring, Eye of the Storm, Hydra''s Lament, Rod of Asclepius,
    Erosion, Lotus Sickle, Eye of Providence, Heartseeker, Shield of the Phoenix,
    Jade Scepter, Stone of Binding, Tyrfing, Bragi''s Harp, Doom Orb, Lernaean Bow,
    Death Metal, Avenging Blade, Wish-Granting Pearl, Chronos'' Pendant, Magi''s Cloak,
    The World Stone, Pharaoh''s Curse, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.54
      pick: 0.19
      fit: 0.21
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.49
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.75
      pick: 0.11
      fit: 0.39
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
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
    of the Phoenix, Stone of Binding, Gluttonous Grimoire, Helm of Radiance, Magi''s
    Cloak, Mantle Of Discord, Midgardian Mail, Oni Hunter''s Garb, Screeching Gargoyle,
    Leviathan''s Hide, Hide of the Nemean Lion, Void Shield, Spear of Desolation,
    Ancile, Prophetic Cloak, Helm of Darkness, Rod of Asclepius, Nimble Ring.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.19
      fit: 0.35
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.45
      pick: 0.37
      fit: 0.57
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
