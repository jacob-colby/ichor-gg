---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.23
  aspect_win_rate: 0.43
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.25
    win_rate: 0.56
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.38
    - name: Golden Blade
      pick_rate: 0.12
      win_rate: 0.42
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.4
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.56
  - name: Stampede
    pick_rate: 0.09
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.3
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.38
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.42
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.57
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.8
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.25
  - name: Shield
    pick_rate: 0.11
    win_rate: 0.6
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 1.0
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.47
  - name: Selflessness
    pick_rate: 0.17
    win_rate: 0.47
  - name: Heroism
    pick_rate: 0.13
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-08-27'
  god_win_rate: 0.48514851485148514
  god_matches_won: 49
  god_matches_played: 101
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Rod of Tahuti, Kinetic Cuirass, Jotunn''s
    Revenge, Erosion, Eye of Providence, Draconic Scale, Berserker''s Shield, Shield
    Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of the Storm,
    Helm of Radiance, Mantle Of Discord, Gluttonous Grimoire, Prophetic Cloak, Runeforged
    Hammer, Stampede, Midgardian Mail, Screeching Gargoyle, Leviathan''s Hide, Void
    Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy, Void Stone,
    Spectral Armor, Spear of Desolation, Hussar''s Wings, Gladiator''s Shield, Rod
    of Asclepius, Daybreak Gavel, Doublet of Binding, Hydra''s Lament, Soul Gem, Breastplate
    of Valor.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.68
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Freya''s Tears, Rod of Asclepius, Jotunn''s Revenge, Soul Gem, Berserker''s Shield,
    Erosion, Eye of Providence, Draconic Scale, Ethereal Staff, Phoenix Feather, Gluttonous
    Grimoire, Yogi''s Necklace, Shield Splitter, Chandra''s Grace, Runeforged Hammer,
    Eye of the Storm, Glorious Pridwen, Stampede, Midgardian Mail, Stone of Binding,
    Lifebinder, Helm of Radiance, Leviathan''s Hide, Void Shield, Magi''s Cloak, Ancile,
    Oni Hunter''s Garb, Daybreak Gavel, Screeching Gargoyle, Sphere of Negation, Void
    Stone, Mantle Of Discord, Spectral Armor, Gladiator''s Shield, Breastplate of
    Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.46
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.54
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.96
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
  - Kinetic Cuirass
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Freya''s Tears,
    Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear
    of Desolation, Void Shield, Spear of the Magus, Soul Gem, Void Stone, Obsidian
    Shard, Avenging Blade, Berserker''s Shield, Heartseeker, Erosion, Shield Splitter,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    Runeforged Hammer, The World Stone, Titan''s Bane, Magi''s Cloak, The Crusher,
    Dreamer''s Idol, Eye of the Storm, Mantle Of Discord, Midgardian Mail, The Reaper,
    Daybreak Gavel, Rod of Asclepius, Leviathan''s Hide, Hydra''s Lament, Breastplate
    of Valor.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.43
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Freya''s Tears, Nimble Ring, Kinetic Cuirass, Gluttonous Grimoire, Tyrfing, Shield
    Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence,
    Stone of Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic
    Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The
    Reaper, Spear of Desolation, Spear of the Magus, Bragi''s Harp, Midgardian Mail,
    Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging Blade, Golden Blade,
    Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.21
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.53
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.33
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Shield of the Phoenix
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Hydra''s Lament, Screeching Gargoyle, Soul Gem, Prophetic Cloak, Chronos'' Pendant,
    Shield Splitter, Berserker''s Shield, Erosion, Helm of Radiance, Runeforged Hammer,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone
    of Binding, Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius,
    Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel, Chandra''s Grace, Obsidian Shard, Breastplate of Valor,
    Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.64
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.13
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
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Freya''s Tears, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker, Tyrfing,
    Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence, Spear
    of the Magus, Avenging Blade, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Helm of Radiance, Titan''s Bane, Soul Gem, The Crusher, Obsidian Shard,
    Pharaoh''s Curse, Silverbranch Bow, Magi''s Cloak, The Reaper, Nimble Ring, Toxic
    Blade, Shogun''s Ofuda, Screeching Gargoyle, Mantle Of Discord, Midgardian Mail,
    Golden Blade, Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter,
    Spear of Desolation, Spear of the Magus, Runeforged Hammer, Helm of Radiance,
    Soul Gem, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s Lament,
    Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix,
    Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting
    Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant, The World Stone, Helm
    of Darkness, Titan''s Bane, The Crusher, Ancient Signet, Screeching Gargoyle,
    Mantle Of Discord, Dreamer''s Idol, Midgardian Mail, Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.38
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Freya''s
    Tears, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Mantle Of Discord, Gluttonous
    Grimoire, Runeforged Hammer, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak,
    Leviathan''s Hide, Void Shield, Stampede, Ancile, Oni Hunter''s Garb, Helm of
    Darkness, Xibalban Effigy, Void Stone, Spectral Armor, Spear of Desolation, Hussar''s
    Wings, Gladiator''s Shield, Rod of Asclepius, Daybreak Gavel, Doublet of Binding,
    Hydra''s Lament, Soul Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.4
      pick: 0.2
      fit: 0.37
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.62
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.19
      fit: 0.68
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.68
  starter: *id001
---
