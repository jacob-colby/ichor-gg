---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.24
  aspect_win_rate: 0.5
  slot_order:
  - name: Lifebinder
    pick_rate: 0.16
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.6
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.53
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.56
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.45
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.6
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.63
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.57
    - name: Ethereal Staff
      pick_rate: 0.05
      win_rate: 0.5
  - name: Veve Charm
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.3
    - name: Obsidian Shard
      pick_rate: 0.04
      win_rate: 0.56
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.42
    win_rate: 0.47
  - name: Bluestone Brooch
    pick_rate: 0.32
    win_rate: 0.61
  - name: Conduit Gem
    pick_rate: 0.06
    win_rate: 0.34
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-09-21'
  god_win_rate: 0.5173116089613035
  god_matches_won: 254
  god_matches_played: 491
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-21'
  god_matches_analyzed: 15551
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
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
    this god: Freya''s Tears, Shifter''s Shield, Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion,
    Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb,
    Stampede, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.19
      fit: 0.39
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.52
      pick: 0.31
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.09
      fit: 0.71
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Freya''s Tears, Shifter''s Shield, Shield of the Phoenix,
    Rod of Tahuti, Kinetic Cuirass, Rod of Asclepius, Soul Gem, Erosion, Eye of Providence,
    Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Yogi''s
    Necklace, Chandra''s Grace, Glorious Pridwen, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile, Stampede.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.19
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.57
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.09
      fit: 0.7
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Shifter's Shield
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Freya''s Tears, Shifter''s Shield, Amanita Charm,
    Obsidian Shard, Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass, Screeching
    Gargoyle, Spear of Desolation, Spear of the Magus, Soul Gem, Void Shield, Void
    Stone, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom
    Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.19
      fit: 0.27
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.09
      fit: 0.49
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.44
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.52
      pick: 0.0
      fit: 0.41
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.12
      fit: 0.51
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Breastplate of Valor
  - Shifter's Shield
  - Freya's Tears
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Rod of Tahuti, Shifter''s Shield, Amanita Charm, Nimble
    Ring, Kinetic Cuirass, Gluttonous Grimoire, Soul Gem, Obsidian Shard, Helm of
    Radiance, Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the
    Magus, Spear of Desolation, Bragi''s Harp, Rod of Asclepius, Midgardian Mail,
    Mantle Of Discord, Bracer of The Abyss, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.56
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
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.33
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.09
      fit: 0.36
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Shifter''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm
    of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Draconic
    Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of
    Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail,
    Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.19
      fit: 0.48
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.52
      pick: 0.31
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.09
      fit: 0.45
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s Revenge,
    Shifter''s Shield, Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield
    Splitter, Runeforged Hammer, Obsidian Shard, Golden Blade, Gluttonous Grimoire,
    Eye of the Storm, Hydra''s Lament, Heartseeker, Spear of Desolation, Lernaean
    Bow, Tyrfing, Erosion, Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging
    Blade, Helm of Radiance, Soul Gem, Stone of Binding, Shield of the Phoenix, Draconic
    Scale, Titan''s Bane, The Crusher, Pharaoh''s Curse, Magi''s Cloak, Nimble Ring,
    Silverbranch Bow, The Reaper, Shogun''s Ofuda, Screeching Gargoyle, Toxic Blade,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.19
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.37
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.09
      fit: 0.41
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s
    Revenge, Shifter''s Shield, Amanita Charm, Obsidian Shard, Kinetic Cuirass, Gluttonous
    Grimoire, Shield Splitter, Spear of Desolation, Spear of the Magus, Runeforged
    Hammer, Helm of Radiance, Soul Gem, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the
    Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death Metal,
    Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant, The World
    Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet, Screeching
    Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.18
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.19
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.38
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.09
      fit: 0.42
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Freya''s
    Tears, Shifter''s Shield, Erosion, Eye of Providence, Draconic Scale, Shield of
    the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide
    of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.19
      fit: 0.39
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.52
      pick: 0.31
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.09
      fit: 0.71
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
