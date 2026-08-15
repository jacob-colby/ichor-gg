---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.35
  aspect_win_rate: 0.7
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.3
    win_rate: 0.71
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.56
    - name: Chronos' Pendant
      pick_rate: 0.12
      win_rate: 0.71
  - name: Soul Gem
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.75
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.31
  - name: Genji's Guard
    pick_rate: 0.11
    win_rate: 0.58
    alternates:
    - name: The World Stone
      pick_rate: 0.1
      win_rate: 0.55
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.33
  - name: Obsidian Shard
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.8
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.33
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.83
  - name: Soul Reaver
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Adroit Ring
      pick_rate: 0.06
      win_rate: 1.0
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.43
    win_rate: 0.62
  - name: Bluestone Pendant
    pick_rate: 0.41
    win_rate: 0.6
  - name: Bumba's Cudgel
    pick_rate: 0.09
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-08-15'
  god_win_rate: 0.6173913043478261
  god_matches_won: 71
  god_matches_played: 115
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix,
    Erosion, Shifter''s Shield, Oni Hunter''s Garb, Eye of Providence, Draconic Scale,
    Spectral Armor, Nimble Ring, Leviathan''s Hide, Helm of Radiance, Midgardian Mail,
    Mantle Of Discord, Stone of Binding, Gladiator''s Shield, Screeching Gargoyle,
    Prophetic Cloak, Magi''s Cloak, Rod of Asclepius, Ancile, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.17
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.68
      efficiency: 0.59
      win: 0.83
      pick: 0.15
      fit: 0.62
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.71
      pick: 0.3
      fit: 0.37
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.67
      pick: 0.15
      fit: 0.2
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.63
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Gluttonous Grimoire,
    Rod of Asclepius, Chandra''s Grace, Oni Hunter''s Garb, Erosion, Shifter''s Shield,
    Eye of Providence, Phoenix Feather, Spectral Armor, Draconic Scale, Lifebinder,
    Nimble Ring, Blood-Bound Book, Glorious Pridwen, Leviathan''s Hide, Bancroft''s
    Talon, Midgardian Mail, Gladiator''s Shield, Helm of Radiance, Breastplate of
    Valor.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.67
      efficiency: 0.59
      win: 0.83
      pick: 0.15
      fit: 0.55
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.71
      pick: 0.3
      fit: 0.38
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.67
      pick: 0.15
      fit: 0.21
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Stone of Binding,
    Screeching Gargoyle, The Cosmic Horror, Void Shield, Spear of the Magus, Shield
    of the Phoenix, Oni Hunter''s Garb, Void Stone, Nimble Ring, Erosion, Shifter''s
    Shield, Spectral Armor, Eye of Providence, Draconic Scale, Helm of Radiance, Leviathan''s
    Hide, Midgardian Mail, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.17
      fit: 0.28
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.83
      pick: 0.15
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.71
      pick: 0.3
      fit: 0.55
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.67
      pick: 0.15
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Chronos'' Pendant, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, Oni Hunter''s Garb, Shield of the Phoenix, Spectral Armor, Erosion,
    Shifter''s Shield, Eye of Providence, Draconic Scale, Helm of Radiance, Leviathan''s
    Hide, Death Metal, Midgardian Mail, The Cosmic Horror, Screeching Gargoyle, Mantle
    Of Discord, Rod of Asclepius, Bracer of The Abyss, Stone of Binding, Breastplate
    of Valor.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.48
      efficiency: 0.42
      win: 0.58
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.64
      efficiency: 0.59
      win: 0.83
      pick: 0.15
      fit: 0.33
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.3
      fit: 0.2
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.67
      pick: 0.15
      fit: 0.11
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Chronos' Pendant
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Chronos' Pendant
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Kinetic Cuirass,
    Shield of the Phoenix, Amanita Charm, Gluttonous Grimoire, Screeching Gargoyle,
    Oni Hunter''s Garb, Nimble Ring, Chandra''s Grace, Gladiator''s Shield, Erosion,
    Shifter''s Shield, Spectral Armor, Eye of Providence, Prophetic Cloak, Draconic
    Scale, Leviathan''s Hide, Gem of Focus, Helm of Radiance, Midgardian Mail, Mantle
    Of Discord, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.58
      pick: 0.17
      fit: 0.48
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.12
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.68
      efficiency: 0.59
      win: 0.83
      pick: 0.15
      fit: 0.64
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.71
      pick: 0.3
      fit: 0.46
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.67
      pick: 0.15
      fit: 0.13
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: The Crusher, Jotunn''s Revenge, Gluttonous
    Grimoire, Kinetic Cuirass, Berserker''s Shield, Amanita Charm, Nimble Ring, Hydra''s
    Lament, Runeforged Hammer, Oni Hunter''s Garb, Shield Splitter, Shield of the
    Phoenix, Golden Blade, Eye of the Storm, Pharaoh''s Curse, Death Metal, Spectral
    Armor, Erosion, Shifter''s Shield, The Cosmic Horror, Eye of Providence, Lernaean
    Bow, Spear of the Magus, The Reaper, Draconic Scale, Damaru, Avenging Blade, Helm
    of Radiance, Leviathan''s Hide, Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord,
    Screeching Gargoyle, Stone of Binding, Rod of Asclepius, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.17
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.64
      efficiency: 0.59
      win: 0.83
      pick: 0.15
      fit: 0.38
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.71
      pick: 0.3
      fit: 0.33
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.67
      pick: 0.15
      fit: 0.23
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Chronos' Pendant
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Chronos' Pendant
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Chronos'' Pendant,
    The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Nimble Ring, Oni Hunter''s Garb, Shield of the Phoenix, Hydra''s Lament, The Cosmic
    Horror, Runeforged Hammer, Death Metal, Shield Splitter, Spear of the Magus, Erosion,
    Helm of Radiance, Spectral Armor, Shifter''s Shield, Eye of the Storm, Eye of
    Providence, Rod of Asclepius, Draconic Scale, Pharaoh''s Curse, The Reaper, Leviathan''s
    Hide, Golden Blade, Jade Scepter, Midgardian Mail, Avenging Blade, Damaru, Mantle
    Of Discord, Screeching Gargoyle, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.17
      fit: 0.25
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.71
      pick: 0.12
      fit: 0.28
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.83
      pick: 0.15
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.71
      pick: 0.3
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.67
      pick: 0.15
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Shield of the Phoenix, Breastplate of Valor, Erosion, Shifter''s Shield, Oni Hunter''s
    Garb, Eye of Providence, Draconic Scale, Spectral Armor, Nimble Ring, Leviathan''s
    Hide, Helm of Radiance, Midgardian Mail, Mantle Of Discord, Stone of Binding,
    Gladiator''s Shield, Screeching Gargoyle, Prophetic Cloak, Magi''s Cloak, Rod
    of Asclepius, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.17
      fit: 0.39
    Breastplate of Valor:
      total: 0.44
      efficiency: 0.64
      win: 0.33
      pick: 0.12
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.68
      efficiency: 0.59
      win: 0.83
      pick: 0.15
      fit: 0.62
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.67
      pick: 0.15
      fit: 0.2
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.63
  starter: *id001
---
