---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.29
  aspect_win_rate: 0.46
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.19
    win_rate: 0.49
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.51
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.53
  - name: Shifter's Shield
    pick_rate: 0.15
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.49
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.49
  - name: Genji's Guard
    pick_rate: 0.11
    win_rate: 0.47
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.62
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.58
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.55
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.55
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 0.58
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.85
    - name: Legionnaire Armor
      pick_rate: 0.05
      win_rate: 0.69
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.43
  - name: Selflessness
    pick_rate: 0.12
    win_rate: 0.52
  - name: Warrior's Axe
    pick_rate: 0.12
    win_rate: 0.39
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-09-05'
  god_win_rate: 0.5164835164835165
  god_matches_won: 282
  god_matches_played: 546
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-05'
  god_matches_analyzed: 13197
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Jotunn''s Revenge, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Berserker''s Shield, Shield
    Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of the Storm,
    Helm of Radiance, Mantle Of Discord, Gluttonous Grimoire, Runeforged Hammer, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Prophetic Cloak, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy,
    Void Stone, Spectral Armor, Spear of Desolation, Hussar''s Wings, Gladiator''s
    Shield, Rod of Asclepius, Daybreak Gavel, Doublet of Binding, Hydra''s Lament,
    Soul Gem, Stampede.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.11
      fit: 0.78
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.54
      pick: 0.2
      fit: 0.68
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Rod of Tahuti,
    Rod of Asclepius, Jotunn''s Revenge, Soul Gem, Breastplate of Valor, Berserker''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Ethereal Staff, Phoenix Feather,
    Gluttonous Grimoire, Yogi''s Necklace, Shield Splitter, Chandra''s Grace, Runeforged
    Hammer, Eye of the Storm, Glorious Pridwen, Midgardian Mail, Stone of Binding,
    Lifebinder, Hide of the Nemean Lion, Helm of Radiance, Leviathan''s Hide, Void
    Shield, Magi''s Cloak, Ancile, Oni Hunter''s Garb, Daybreak Gavel, Screeching
    Gargoyle, Sphere of Negation, Void Stone, Mantle Of Discord, Spectral Armor, Gladiator''s
    Shield, Stampede.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.11
      fit: 0.76
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.9
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.54
      pick: 0.2
      fit: 0.66
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.54
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Stone of Binding, Gluttonous Grimoire, Screeching Gargoyle, Spear of Desolation,
    Void Shield, Spear of the Magus, Breastplate of Valor, Soul Gem, Void Stone, Obsidian
    Shard, Avenging Blade, Berserker''s Shield, Heartseeker, Erosion, Shield Splitter,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    Runeforged Hammer, The World Stone, Titan''s Bane, Magi''s Cloak, The Crusher,
    Dreamer''s Idol, Eye of the Storm, Mantle Of Discord, Midgardian Mail, The Reaper,
    Daybreak Gavel, Hide of the Nemean Lion, Rod of Asclepius, Leviathan''s Hide,
    Hydra''s Lament.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.11
      fit: 0.58
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.43
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Nimble Ring, Golden Blade, Gluttonous Grimoire, Breastplate of
    Valor, Tyrfing, Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance,
    Eye of Providence, Stone of Binding, Eye of the Storm, Shield of the Phoenix,
    Hydra''s Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, The Reaper, Spear of Desolation, Spear of the Magus, Bragi''s
    Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging
    Blade.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.33
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear
    of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant,
    Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Helm of Radiance,
    Runeforged Hammer, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Eye of the Storm, Arondight, Gem of Focus, Magi''s
    Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Obsidian
    Shard, Hide of the Nemean Lion, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.11
      fit: 0.55
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.64
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
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
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Breastplate
    of Valor, Golden Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament,
    Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi,
    Eye of Providence, Spear of the Magus, Avenging Blade, Shield of the Phoenix,
    Stone of Binding, Draconic Scale, Helm of Radiance, Titan''s Bane, Soul Gem, The
    Crusher, Obsidian Shard, Pharaoh''s Curse, Silverbranch Bow, Magi''s Cloak, The
    Reaper, Nimble Ring, Toxic Blade, Shogun''s Ofuda, Screeching Gargoyle, Mantle
    Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.11
      fit: 0.52
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Breastplate of Valor
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Breastplate
    of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer, Helm of
    Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the
    Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death Metal,
    Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant, The World
    Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet, Screeching
    Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.11
      fit: 0.52
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Jotunn''s
    Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Berserker''s
    Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Eye of the Storm, Helm of Radiance, Mantle Of Discord, Gluttonous Grimoire, Runeforged
    Hammer, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion, Prophetic
    Cloak, Leviathan''s Hide, Void Shield, Stampede, Ancile, Oni Hunter''s Garb, Helm
    of Darkness, Xibalban Effigy, Void Stone, Spectral Armor, Spear of Desolation,
    Hussar''s Wings, Gladiator''s Shield, Rod of Asclepius, Daybreak Gavel, Doublet
    of Binding, Hydra''s Lament, Soul Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.47
      pick: 0.17
      fit: 0.37
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.11
      fit: 0.78
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.54
      pick: 0.2
      fit: 0.68
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
---
