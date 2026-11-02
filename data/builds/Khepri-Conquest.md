---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.76
  aspect_win_rate: 0.55
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.42
    win_rate: 0.55
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.11
      win_rate: 0.55
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.6
  - name: Stampede
    pick_rate: 0.2
    win_rate: 0.45
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.66
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.46
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.59
  - name: Omen Drum
    pick_rate: 0.11
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.74
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.67
    - name: Evil Eye
      pick_rate: 0.04
      win_rate: 0.67
  - name: Veve Charm
    pick_rate: 0.08
    win_rate: 0.73
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.67
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.75
  community_starters:
  - name: Selflessness
    pick_rate: 0.28
    win_rate: 0.56
  - name: Heroism
    pick_rate: 0.23
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-11-02'
  god_win_rate: 0.5563636363636364
  god_matches_won: 153
  god_matches_played: 275
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
  - Amanita Charm
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
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Breastplate of Valor,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Helm of Darkness,
    Shifter''s Shield, Stone of Binding, Oni Hunter''s Garb, Magi''s Cloak, Helm of
    Radiance, Midgardian Mail, Mantle Of Discord, Screeching Gargoyle, Gluttonous
    Grimoire, Leviathan''s Hide, Prophetic Cloak, Spear of Desolation, Ancile, Hide
    of the Nemean Lion, Void Stone, Soul Gem, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.69
      win: 0.66
      pick: 0.2
      fit: 0.4
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.66
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.61
      efficiency: 0.58
      win: 0.67
      pick: 0.19
      fit: 0.65
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.7
    Erosion:
      total: 0.58
      efficiency: 0.51
      win: 0.66
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
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
  - Amanita Charm
  - Erosion
  flex_slots:
  - Freya's Tears
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Phoenix Feather, Erosion, Eye of Providence, Breastplate of Valor, Ethereal
    Staff, Draconic Scale, Yogi''s Necklace, Chandra''s Grace, Shifter''s Shield,
    Oni Hunter''s Garb, Gluttonous Grimoire, Glorious Pridwen, Midgardian Mail, Helm
    of Darkness, Leviathan''s Hide, Rod of Asclepius, Regrowth Striders, Helm of Radiance,
    Stone of Binding, Spear of Desolation, Sphere of Negation, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.66
      pick: 0.2
      fit: 0.37
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.62
      efficiency: 0.52
      win: 0.66
      pick: 0.0
      fit: 0.93
    Freya's Tears:
      total: 0.6
      efficiency: 0.58
      win: 0.67
      pick: 0.19
      fit: 0.58
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.98
    Erosion:
      total: 0.58
      efficiency: 0.51
      win: 0.66
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Spear of Desolation, Kinetic Cuirass, Screeching Gargoyle, Obsidian Shard, Soul
    Gem, Void Stone, Void Shield, Breastplate of Valor, Spear of the Magus, Erosion,
    Eye of Providence, Doom Orb, The World Stone, Draconic Scale, Shield of the Phoenix,
    Helm of Radiance, Helm of Darkness, Oni Hunter''s Garb, Magi''s Cloak, Midgardian
    Mail, Dreamer''s Idol, Shifter''s Shield, Mantle Of Discord.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.5
      win: 0.66
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.66
      pick: 0.2
      fit: 0.28
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.67
      pick: 0.19
      fit: 0.45
    Spear of Desolation:
      total: 0.58
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.66
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Eros' Bow
  - Amanita Charm
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Helm of Radiance, Eros'' Bow, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Stone of Binding, Spear of Desolation,
    Obsidian Shard, Shield of the Phoenix, Helm of Darkness, Screeching Gargoyle,
    Midgardian Mail, Draconic Scale, Magi''s Cloak, Blood-Bound Book, Mantle Of Discord,
    Bragi''s Harp, Leviathan''s Hide, Shifter''s Shield, Bracer of The Abyss.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.66
      pick: 0.2
      fit: 0.21
    Nimble Ring:
      total: 0.56
      efficiency: 0.64
      win: 0.66
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.52
      efficiency: 0.45
      win: 0.66
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.56
      efficiency: 0.58
      win: 0.67
      pick: 0.19
      fit: 0.33
    Eros' Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.66
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Breastplate
    of Valor, Kinetic Cuirass, Spear of Desolation, Shield of the Phoenix, Screeching
    Gargoyle, Soul Gem, Chronos'' Pendant, Prophetic Cloak, Helm of Radiance, Helm
    of Darkness, Erosion, Eye of Providence, Gluttonous Grimoire, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Oni Hunter''s Garb, Gem of Focus, Obsidian Shard,
    Heartwood Charm, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Shifter''s
    Shield, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.69
      win: 0.66
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.64
      win: 0.66
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.61
      efficiency: 0.58
      win: 0.67
      pick: 0.19
      fit: 0.64
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Kinetic Cuirass, Golden Blade, Runeforged
    Hammer, Tekko-Kagi, Titan''s Bane, Breastplate of Valor, Tyrfing, Hydra''s Lament,
    Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, The Crusher, Soul Gem,
    Toxic Blade, Lernaean Bow, Heartseeker, Erosion, Helm of Radiance, Silverbranch
    Bow, Avenging Blade, Eye of Providence, Oni Hunter''s Garb, Stone of Binding,
    Arondight, Shield of the Phoenix, Draconic Scale, Helm of Darkness, The Reaper,
    Midgardian Mail, Death Metal, Magi''s Cloak, Screeching Gargoyle, Spear of the
    Magus, Pharaoh''s Curse, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.66
      pick: 0.2
      fit: 0.23
    Berserker's Shield:
      total: 0.61
      efficiency: 0.75
      win: 0.66
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.69
      win: 0.66
      pick: 0.0
      fit: 0.45
    Shield Splitter:
      total: 0.58
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.19
      fit: 0.38
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Shield Splitter, Berserker''s Shield, Kinetic Cuirass, Gluttonous
    Grimoire, Spear of Desolation, Obsidian Shard, Soul Gem, Breastplate of Valor,
    Helm of Radiance, Runeforged Hammer, Helm of Darkness, Titan''s Bane, Spear of
    the Magus, Hydra''s Lament, Death Metal, Erosion, Eye of Providence, Doom Orb,
    The Crusher, Oni Hunter''s Garb, Stone of Binding, Shield of the Phoenix, Draconic
    Scale, Jade Scepter, Heartseeker, The World Stone, Chronos'' Pendant, Midgardian
    Mail, Avenging Blade, Magi''s Cloak, Screeching Gargoyle, Arondight, Mantle Of
    Discord, Leviathan''s Hide, The Reaper, Shifter''s Shield, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.66
      pick: 0.2
      fit: 0.24
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.66
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.66
      pick: 0.0
      fit: 0.41
    Shield Splitter:
      total: 0.57
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.19
      fit: 0.38
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Helm
    of Darkness, Shifter''s Shield, Stone of Binding, Oni Hunter''s Garb, Magi''s
    Cloak, Helm of Radiance, Midgardian Mail, Mantle Of Discord, Screeching Gargoyle,
    Gluttonous Grimoire, Leviathan''s Hide, Prophetic Cloak, Spear of Desolation,
    Ancile, Hide of the Nemean Lion, Void Stone, Soul Gem, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.69
      win: 0.66
      pick: 0.2
      fit: 0.4
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.66
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.61
      efficiency: 0.58
      win: 0.67
      pick: 0.19
      fit: 0.65
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.7
    Erosion:
      total: 0.58
      efficiency: 0.51
      win: 0.66
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
