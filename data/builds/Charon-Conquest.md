---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.28
  aspect_win_rate: 0.57
  slot_order:
  - name: Lifebinder
    pick_rate: 0.24
    win_rate: 0.33
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.8
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.67
  - name: Breastplate of Valor
    pick_rate: 0.16
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.67
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.33
  - name: Genji's Guard
    pick_rate: 0.28
    win_rate: 0.57
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.5
    - name: Damaru
      pick_rate: 0.08
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Omen Drum
      pick_rate: 0.13
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Evil Eye
      pick_rate: 0.12
      win_rate: 1.0
    - name: Medallion
      pick_rate: 0.06
      win_rate: 0.0
  - name: Sage's Ring
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Contagion
      pick_rate: 0.1
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.52
    win_rate: 0.46
  - name: Bluestone Brooch
    pick_rate: 0.16
    win_rate: 0.75
  - name: Archmage's Gem
    pick_rate: 0.08
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-09-09'
  god_win_rate: 0.56
  god_matches_won: 14
  god_matches_played: 25
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Contagion
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Erosion, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of
    Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail, Screeching
    Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Helm of Darkness, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation,
    Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.65
      win: 0.75
      pick: 0.22
      fit: 0.39
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.31
      fit: 0.3
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.77
      efficiency: 0.61
      win: 1.0
      pick: 0.22
      fit: 0.64
    Shifter's Shield:
      total: 0.67
      efficiency: 0.55
      win: 0.8
      pick: 0.2
      fit: 0.71
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Breastplate of Valor
  - Contagion
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Contagion
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Soul Gem, Erosion, Eye of Providence, Draconic Scale, Ethereal
    Staff, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace, Chandra''s Grace,
    Glorious Pridwen, Midgardian Mail, Stone of Binding, Helm of Radiance, Hide of
    the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s Cloak, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.22
      fit: 0.36
    Contagion:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.31
      fit: 0.37
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 0.22
      fit: 0.57
    Shifter's Shield:
      total: 0.67
      efficiency: 0.55
      win: 0.8
      pick: 0.2
      fit: 0.7
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Breastplate of Valor
  - Contagion
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
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
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Spear of the Magus,
    Soul Gem, Void Shield, Obsidian Shard, Void Stone, Erosion, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance, The World Stone,
    Dreamer''s Idol, Magi''s Cloak, Mantle Of Discord, Midgardian Mail, Rod of Asclepius,
    Hide of the Nemean Lion.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.31
      fit: 0.24
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.44
      fit: 0.27
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.22
      fit: 0.27
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.22
      fit: 0.44
    Shifter's Shield:
      total: 0.64
      efficiency: 0.55
      win: 0.8
      pick: 0.2
      fit: 0.49
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Contagion
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Contagion
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Soul Gem, Helm of Radiance, Erosion, Stone of Binding, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak
    Gavel, Spear of the Magus, Spear of Desolation, Bragi''s Harp, Rod of Asclepius,
    Midgardian Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard, Hide
    of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.24
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.31
      fit: 0.2
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
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.22
      fit: 0.33
    Shifter's Shield:
      total: 0.62
      efficiency: 0.55
      win: 0.8
      pick: 0.2
      fit: 0.36
  community_ordered:
  - Contagion
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  - Omen Drum
  flex_slots:
  - Omen Drum
  - Genji's Guard
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching Gargoyle, Soul
    Gem, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous
    Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.31
      fit: 0.23
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.57
      pick: 0.44
      fit: 0.48
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.22
      fit: 0.48
    Freya's Tears:
      total: 0.77
      efficiency: 0.61
      win: 1.0
      pick: 0.22
      fit: 0.64
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.8
      pick: 0.2
      fit: 0.45
    Omen Drum:
      total: 0.6
      efficiency: 0.41
      win: 1.0
      pick: 0.22
      fit: 0.0
  community_ordered:
  - Contagion
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  - Omen Drum
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Breastplate of Valor
  - Contagion
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Omen Drum
  flex_slots:
  - Omen Drum
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Golden
    Blade, Gluttonous Grimoire, Eye of the Storm, Hydra''s Lament, Heartseeker, Spear
    of Desolation, Lernaean Bow, Tyrfing, Erosion, Spear of the Magus, Tekko-Kagi,
    Eye of Providence, Avenging Blade, Helm of Radiance, Soul Gem, Stone of Binding,
    Shield of the Phoenix, Draconic Scale, Obsidian Shard, Titan''s Bane, The Crusher,
    Pharaoh''s Curse, Magi''s Cloak, Nimble Ring, Silverbranch Bow, The Reaper, Shogun''s
    Ofuda, Screeching Gargoyle, Toxic Blade, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.22
      fit: 0.23
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.31
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.22
      fit: 0.37
    Shifter's Shield:
      total: 0.62
      efficiency: 0.55
      win: 0.8
      pick: 0.2
      fit: 0.41
    Omen Drum:
      total: 0.6
      efficiency: 0.41
      win: 1.0
      pick: 0.22
      fit: 0.0
  community_ordered:
  - Breastplate of Valor
  - Contagion
  - Freya's Tears
  - Shifter's Shield
  - Omen Drum
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Contagion
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Omen Drum
  flex_slots:
  - Omen Drum
  - Jotunn's Revenge
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Spear of
    Desolation, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem,
    Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of
    Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix, Stone
    of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting
    Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant, The World Stone, Helm
    of Darkness, Titan''s Bane, The Crusher, Ancient Signet, Screeching Gargoyle,
    Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.22
      fit: 0.23
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.31
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.22
      fit: 0.38
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.8
      pick: 0.2
      fit: 0.42
    Omen Drum:
      total: 0.6
      efficiency: 0.41
      win: 1.0
      pick: 0.22
      fit: 0.0
  community_ordered:
  - Breastplate of Valor
  - Contagion
  - Freya's Tears
  - Shifter's Shield
  - Omen Drum
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Erosion,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Magi''s
    Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail,
    Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Helm of Darkness,
    Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear
    of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.65
      win: 0.75
      pick: 0.22
      fit: 0.39
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.44
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.77
      efficiency: 0.61
      win: 1.0
      pick: 0.22
      fit: 0.64
    Shifter's Shield:
      total: 0.67
      efficiency: 0.55
      win: 0.8
      pick: 0.2
      fit: 0.71
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
