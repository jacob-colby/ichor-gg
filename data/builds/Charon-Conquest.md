---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.57
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.22
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.0
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.5
  - name: Chronos' Pendant
    pick_rate: 0.3
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.25
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.0
  - name: Spear of Desolation
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Draconic Scale
      pick_rate: 0.13
      win_rate: 0.33
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.0
  - name: Totem of Death
    pick_rate: 0.23
    win_rate: 0.4
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.33
    - name: Divine Ruin
      pick_rate: 0.09
      win_rate: 0.5
  - name: The Cosmic Horror
    pick_rate: 0.11
    win_rate: 0.0
    alternates:
    - name: Ring of Dispel
      pick_rate: 0.11
      win_rate: 1.0
    - name: Bowl Drum
      pick_rate: 0.11
      win_rate: 0.5
  - name: Captain's Ring
    pick_rate: 0.17
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 1.0
    - name: Stalwart Sigil
      pick_rate: 0.08
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.26
    win_rate: 0.33
  - name: Bluestone Pendant
    pick_rate: 0.26
    win_rate: 0.17
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-10-07'
  god_win_rate: 0.43478260869565216
  god_matches_won: 10
  god_matches_played: 23
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shell of Rebuke
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
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Breastplate of Valor,
    Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail, Screeching
    Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Helm of Darkness, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.09
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Shell of Rebuke:
      total: 0.64
      efficiency: 0.28
      win: 1.0
      pick: 0.25
      fit: 0.51
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Breastplate of Valor
  - Shell of Rebuke
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shell of Rebuke
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
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Breastplate of Valor, Soul Gem, Erosion, Eye of Providence,
    Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace, Chandra''s
    Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding, Helm of
    Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s Cloak,
    Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.09
      fit: 0.36
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.92
    Shell of Rebuke:
      total: 0.63
      efficiency: 0.28
      win: 1.0
      pick: 0.25
      fit: 0.43
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Breastplate of Valor
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Spear of Desolation
  - Shell of Rebuke
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of the Magus, Breastplate of Valor,
    Soul Gem, Void Shield, Obsidian Shard, Void Stone, Erosion, Eye of Providence,
    Shield of the Phoenix, Doom Orb, Helm of Radiance, The World Stone, Dreamer''s
    Idol, Magi''s Cloak, Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Hide
    of the Nemean Lion.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.26
      fit: 0.51
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.25
      fit: 0.35
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Spear of Desolation
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Shell of Rebuke
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
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Breastplate
    of Valor, Gluttonous Grimoire, Soul Gem, Helm of Radiance, Erosion, Stone of Binding,
    Eye of Providence, Shield of the Phoenix, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, Spear of the Magus, Bragi''s Harp, Rod of Asclepius, Midgardian
    Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard, Hide of the Nemean
    Lion, Leviathan''s Hide.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.25
      fit: 0.26
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Kinetic Cuirass
  - Spear of Desolation
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Soul
    Gem, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of Providence,
    Gladiator''s Shield, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius,
    Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.09
      fit: 0.48
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.42
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.26
      fit: 0.46
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.25
      fit: 0.32
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Breastplate of Valor,
    Runeforged Hammer, Golden Blade, Gluttonous Grimoire, Eye of the Storm, Hydra''s
    Lament, Heartseeker, Lernaean Bow, Tyrfing, Erosion, Spear of the Magus, Tekko-Kagi,
    Eye of Providence, Avenging Blade, Helm of Radiance, Soul Gem, Stone of Binding,
    Shield of the Phoenix, Obsidian Shard, Titan''s Bane, The Crusher, Pharaoh''s
    Curse, Magi''s Cloak, Nimble Ring, Silverbranch Bow, The Reaper, Shogun''s Ofuda,
    Screeching Gargoyle, Toxic Blade, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.25
      fit: 0.29
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Shell of Rebuke
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Breastplate of Valor, Shield
    Splitter, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian
    Shard, Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius,
    Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s
    Cloak, The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient
    Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.6
      pick: 0.22
      fit: 0.18
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.18
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.25
      fit: 0.3
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Book of Thoth
  - Shell of Rebuke
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Breastplate
    of Valor, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Helm of Darkness,
    Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Hussar''s
    Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.41
      efficiency: 0.66
      win: 0.25
      pick: 0.23
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.09
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.33
      pick: 0.23
      fit: 0.64
    Shifter's Shield:
      total: 0.31
      efficiency: 0.55
      win: 0.0
      pick: 0.18
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
