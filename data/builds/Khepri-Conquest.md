---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.73
  aspect_win_rate: 0.55
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.3
    win_rate: 0.54
    alternates:
    - name: Damaru
      pick_rate: 0.12
      win_rate: 0.56
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.42
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.14
      win_rate: 0.68
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.59
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.47
    - name: Totem of Death
      pick_rate: 0.11
      win_rate: 0.7
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.63
    alternates:
    - name: Omen Drum
      pick_rate: 0.1
      win_rate: 0.62
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.57
  - name: Spirit Robe
    pick_rate: 0.07
    win_rate: 0.73
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.45
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.7
  - name: Engraved Guard
    pick_rate: 0.11
    win_rate: 0.64
    alternates:
    - name: Captain's Ring
      pick_rate: 0.06
      win_rate: 0.63
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.63
  community_starters:
  - name: Selflessness
    pick_rate: 0.25
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-10-01'
  god_win_rate: 0.541958041958042
  god_matches_won: 155
  god_matches_played: 286
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-10-01'
  god_matches_analyzed: 10386
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Breastplate of Valor,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Screeching
    Gargoyle, Midgardian Mail, Prophetic Cloak, Hide of the Nemean Lion, Rod of Tahuti,
    Leviathan''s Hide, Helm of Darkness, Void Shield, Spear of Desolation, Ancile,
    Oni Hunter''s Garb, Gladiator''s Shield, Xibalban Effigy, Stampede.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.8
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.7
    Erosion:
      total: 0.57
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.7
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
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
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Shifter''s Shield, Soul Gem, Breastplate of Valor, Erosion, Eye of Providence,
    Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Chandra''s
    Grace, Yogi''s Necklace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone
    of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void
    Shield, Magi''s Cloak, Rod of Tahuti, Ancile, Stampede.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.93
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.66
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.98
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.68
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Amanita Charm, Stone of Binding, Gluttonous Grimoire, Rod of Tahuti,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Soul Gem, Spear of
    the Magus, Void Shield, Breastplate of Valor, Obsidian Shard, Void Stone, Shifter''s
    Shield, Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Doom
    Orb, Helm of Radiance, The World Stone, Magi''s Cloak, Dreamer''s Idol, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.68
    Stone of Binding:
      total: 0.57
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.11
      fit: 0.41
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous Grimoire, Breastplate
    of Valor, Shifter''s Shield, Soul Gem, Rod of Tahuti, Helm of Radiance, Erosion,
    Shield of the Phoenix, Stone of Binding, Eye of Providence, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Spear of Desolation, Spear of the Magus, Daybreak
    Gavel, Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer
    of The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.21
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.62
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spear of Desolation
  flex_slots:
  - Spear of Desolation
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Soul Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm
    of Radiance, Rod of Tahuti, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of
    Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen,
    Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.58
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Golden Blade
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
    Charm, Kinetic Cuirass, Shield Splitter, Golden Blade, Breastplate of Valor, Runeforged
    Hammer, Rod of Tahuti, Shifter''s Shield, Gluttonous Grimoire, Eye of the Storm,
    Tyrfing, Hydra''s Lament, Heartseeker, Spear of Desolation, Lernaean Bow, Spear
    of the Magus, Erosion, Silverbranch Bow, Tekko-Kagi, Eye of Providence, Soul Gem,
    Shield of the Phoenix, Avenging Blade, Helm of Radiance, Stone of Binding, Draconic
    Scale, Toxic Blade, Obsidian Shard, Titan''s Bane, The Crusher, Pharaoh''s Curse,
    Nimble Ring, Magi''s Cloak, The Reaper, Screeching Gargoyle, Shogun''s Ofuda,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.57
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.55
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Rod of Tahuti, Kinetic Cuirass, Gluttonous Grimoire, Breastplate of Valor, Spear
    of Desolation, Shield Splitter, Spear of the Magus, Soul Gem, Runeforged Hammer,
    Helm of Radiance, Shifter''s Shield, Obsidian Shard, Berserker''s Shield, Eye
    of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of
    Providence, Shield of the Phoenix, Stone of Binding, Draconic Scale, Doom Orb,
    Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Chronos'' Pendant,
    Magi''s Cloak, The World Stone, Helm of Darkness, Titan''s Bane, Screeching Gargoyle,
    Ancient Signet, The Crusher, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.18
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.51
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.18
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.41
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
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Prophetic Cloak,
    Hide of the Nemean Lion, Leviathan''s Hide, Helm of Darkness, Void Shield, Stampede,
    Spear of Desolation, Ancile, Oni Hunter''s Garb, Gladiator''s Shield, Xibalban
    Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.2
      fit: 0.4
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.19
      fit: 0.65
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
