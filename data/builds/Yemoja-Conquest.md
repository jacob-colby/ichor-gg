---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.46
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.35
    win_rate: 0.49
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.46
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.55
  - name: Soul Gem
    pick_rate: 0.1
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.31
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.47
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.64
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.8
  - name: Spirit Robe
    pick_rate: 0.08
    win_rate: 0.25
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.44
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.57
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.0
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.8
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.4
    win_rate: 0.48
  - name: Bluestone Brooch
    pick_rate: 0.33
    win_rate: 0.52
  - name: Archmage's Gem
    pick_rate: 0.06
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-10-28'
  god_win_rate: 0.4947916666666667
  god_matches_won: 95
  god_matches_played: 192
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
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Freya''s Tears, Stampede, Kinetic Cuirass, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Helm of Radiance, Gluttonous Grimoire, Stone of Binding, Magi''s
    Cloak, Screeching Gargoyle, Mantle Of Discord, Helm of Darkness, Rod of Asclepius,
    Prophetic Cloak, Midgardian Mail, Soul Gem, Hide of the Nemean Lion, Spear of
    the Magus, Leviathan''s Hide, Void Shield, Ancile, Genji''s Guard.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.73
    Shell of Rebuke:
      total: 0.53
      efficiency: 0.28
      win: 0.8
      pick: 0.13
      fit: 0.45
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.14
      fit: 0.62
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Stampede:
      total: 0.53
      efficiency: 0.51
      win: 0.64
      pick: 0.11
      fit: 0.41
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Stampede
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Shell of Rebuke
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Freya''s Tears, Kinetic Cuirass,
    Rod of Asclepius, Soul Gem, Shifter''s Shield, Breastplate of Valor, Ethereal
    Staff, Gluttonous Grimoire, Erosion, Eye of Providence, Draconic Scale, Chandra''s
    Grace, Lifebinder, Phoenix Feather, Yogi''s Necklace, Glorious Pridwen, Helm of
    Radiance, Sphere of Negation, Stone of Binding, Midgardian Mail, Screeching Gargoyle,
    Jade Scepter, Wish-Granting Pearl, Hide of the Nemean Lion, Genji''s Guard.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.9
    Shell of Rebuke:
      total: 0.52
      efficiency: 0.28
      win: 0.8
      pick: 0.13
      fit: 0.38
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.14
      fit: 0.55
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.92
    Stampede:
      total: 0.54
      efficiency: 0.51
      win: 0.64
      pick: 0.11
      fit: 0.43
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Shell of Rebuke
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Stampede
  flex_slots:
  - Shell of Rebuke
  - Freya's Tears
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
    for this god: Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Stone of Binding,
    Screeching Gargoyle, Kinetic Cuirass, Spear of the Magus, Soul Gem, Breastplate
    of Valor, Obsidian Shard, Void Shield, Void Stone, Shifter''s Shield, Chronos''
    Pendant, Doom Orb, Helm of Radiance, Erosion, Shield of the Phoenix, Eye of Providence,
    The World Stone, Draconic Scale, Dreamer''s Idol, Magi''s Cloak, Rod of Asclepius,
    Mantle Of Discord, Midgardian Mail, Genji''s Guard.'
  slot_scores:
    Shell of Rebuke:
      total: 0.51
      efficiency: 0.28
      win: 0.8
      pick: 0.13
      fit: 0.32
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.49
      pick: 0.35
      fit: 0.55
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.14
      fit: 0.44
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.56
      pick: 0.17
      fit: 0.43
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Stampede:
      total: 0.52
      efficiency: 0.51
      win: 0.64
      pick: 0.11
      fit: 0.29
  community_ordered:
  - Shell of Rebuke
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Stampede
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Amanita Charm
  - Stampede
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Nimble Ring, Freya''s Tears, Gluttonous Grimoire, Kinetic
    Cuirass, Breastplate of Valor, Soul Gem, Chronos'' Pendant, Shifter''s Shield,
    Helm of Radiance, Shield of the Phoenix, Erosion, Stone of Binding, Eye of Providence,
    Spear of the Magus, Draconic Scale, Screeching Gargoyle, Rod of Asclepius, Bragi''s
    Harp, Magi''s Cloak, Daybreak Gavel, Obsidian Shard, Bracer of The Abyss, Midgardian
    Mail, Mantle Of Discord, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.56
      pick: 0.17
      fit: 0.11
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
    Stampede:
      total: 0.51
      efficiency: 0.51
      win: 0.64
      pick: 0.11
      fit: 0.22
  community_ordered:
  - Rod of Tahuti
  - Stampede
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Shell of Rebuke
  - Spear of Desolation
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Shell of Rebuke
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Amanita Charm, Chronos'' Pendant, Kinetic Cuirass, Shield of the Phoenix, Screeching
    Gargoyle, Shifter''s Shield, Soul Gem, Prophetic Cloak, Erosion, Helm of Radiance,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone
    of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear
    of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel,
    Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shell of Rebuke:
      total: 0.51
      efficiency: 0.28
      win: 0.8
      pick: 0.13
      fit: 0.32
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.35
      fit: 0.46
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.14
      fit: 0.64
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Stampede:
      total: 0.52
      efficiency: 0.51
      win: 0.64
      pick: 0.11
      fit: 0.29
  community_ordered:
  - Shell of Rebuke
  - Spear of Desolation
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Shell of Rebuke
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita
    Charm, Freya''s Tears, Kinetic Cuirass, Breastplate of Valor, Shield Splitter,
    Runeforged Hammer, Gluttonous Grimoire, Golden Blade, Hydra''s Lament, Shifter''s
    Shield, Eye of the Storm, Heartseeker, Spear of the Magus, Helm of Radiance, Obsidian
    Shard, Lernaean Bow, Tyrfing, Shield of the Phoenix, Soul Gem, Erosion, Eye of
    Providence, Avenging Blade, Nimble Ring, Tekko-Kagi, Stone of Binding, Draconic
    Scale, Titan''s Bane, The Crusher, Screeching Gargoyle, Pharaoh''s Curse, Rod
    of Asclepius, Magi''s Cloak, Silverbranch Bow, Bragi''s Harp, The Reaper, Daybreak
    Gavel, Shogun''s Ofuda, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Shell of Rebuke:
      total: 0.51
      efficiency: 0.28
      win: 0.8
      pick: 0.13
      fit: 0.27
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.14
      fit: 0.38
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Stampede:
      total: 0.51
      efficiency: 0.51
      win: 0.64
      pick: 0.11
      fit: 0.25
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Stampede
  flex_slots:
  - Shell of Rebuke
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire, Breastplate of Valor, Chronos''
    Pendant, Shield Splitter, Spear of the Magus, Runeforged Hammer, Helm of Radiance,
    Shifter''s Shield, Obsidian Shard, Soul Gem, Berserker''s Shield, Hydra''s Lament,
    Eye of the Storm, Rod of Asclepius, Heartseeker, Shield of the Phoenix, Erosion,
    Eye of Providence, Stone of Binding, Draconic Scale, Jade Scepter, Doom Orb, Death
    Metal, Wish-Granting Pearl, Avenging Blade, Screeching Gargoyle, Magi''s Cloak,
    The World Stone, Titan''s Bane, Helm of Darkness, Ancient Signet, The Crusher,
    Mantle Of Discord, Daybreak Gavel, Dreamer''s Idol, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.42
    Shell of Rebuke:
      total: 0.51
      efficiency: 0.28
      win: 0.8
      pick: 0.13
      fit: 0.29
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.14
      fit: 0.39
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.56
      pick: 0.17
      fit: 0.32
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Stampede:
      total: 0.51
      efficiency: 0.51
      win: 0.64
      pick: 0.11
      fit: 0.26
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Rod of Tahuti
  - Stampede
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
    Underrated for this god: Amanita Charm, Freya''s Tears, Kinetic Cuirass, Genji''s
    Guard, Shifter''s Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield
    of the Phoenix, Draconic Scale, Helm of Radiance, Gluttonous Grimoire, Stone of
    Binding, Magi''s Cloak, Screeching Gargoyle, Soul Gem, Mantle Of Discord, Helm
    of Darkness, Rod of Asclepius, Prophetic Cloak, Midgardian Mail, Hide of the Nemean
    Lion, Spear of the Magus, Leviathan''s Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.43
      efficiency: 0.66
      win: 0.31
      pick: 0.11
      fit: 0.39
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.14
      fit: 0.62
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
