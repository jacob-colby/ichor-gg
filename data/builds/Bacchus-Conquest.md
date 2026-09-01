---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.48
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.2
    win_rate: 0.49
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.46
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.52
  - name: Shifter's Shield
    pick_rate: 0.15
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.39
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.41
  - name: Genji's Guard
    pick_rate: 0.11
    win_rate: 0.45
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.67
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.61
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.36
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.64
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.54
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.54
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.55
    alternates:
    - name: Olmec Blue
      pick_rate: 0.05
      win_rate: 0.25
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.45
  - name: Bluestone Brooch
    pick_rate: 0.13
    win_rate: 0.63
  - name: Selflessness
    pick_rate: 0.13
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-09-01'
  god_win_rate: 0.5139664804469274
  god_matches_won: 184
  god_matches_played: 358
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-01'
  god_matches_analyzed: 8200
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
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
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Jotunn''s Revenge, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Berserker''s Shield, Shield
    Splitter, Shield of the Phoenix, Stone of Binding, Hide of the Nemean Lion, Magi''s
    Cloak, Eye of the Storm, Helm of Radiance, Mantle Of Discord, Gluttonous Grimoire,
    Runeforged Hammer, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy,
    Void Stone, Spectral Armor, Spear of Desolation, Hussar''s Wings, Gladiator''s
    Shield, Rod of Asclepius, Daybreak Gavel, Doublet of Binding, Hydra''s Lament,
    Soul Gem, Stampede.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.64
      pick: 0.17
      fit: 0.62
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.54
      pick: 0.2
      fit: 0.68
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
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
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Jotunn''s Revenge, Soul Gem, Breastplate of Valor, Berserker''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Ethereal Staff, Phoenix Feather,
    Gluttonous Grimoire, Hide of the Nemean Lion, Yogi''s Necklace, Shield Splitter,
    Chandra''s Grace, Runeforged Hammer, Eye of the Storm, Glorious Pridwen, Midgardian
    Mail, Stone of Binding, Lifebinder, Helm of Radiance, Leviathan''s Hide, Void
    Shield, Magi''s Cloak, Ancile, Oni Hunter''s Garb, Daybreak Gavel, Screeching
    Gargoyle, Sphere of Negation, Void Stone, Mantle Of Discord, Spectral Armor, Gladiator''s
    Shield, Stampede.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.17
      fit: 0.54
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.54
      pick: 0.2
      fit: 0.66
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Void Shield, Spear of the Magus, Breastplate of Valor, Soul Gem, Void Stone, Obsidian
    Shard, Avenging Blade, Berserker''s Shield, Heartseeker, Erosion, Shield Splitter,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom Orb, Hide of the
    Nemean Lion, Helm of Radiance, Runeforged Hammer, The World Stone, Titan''s Bane,
    Magi''s Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of Discord,
    Midgardian Mail, The Reaper, Daybreak Gavel, Rod of Asclepius, Leviathan''s Hide,
    Hydra''s Lament.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.17
      fit: 0.43
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.54
      pick: 0.2
      fit: 0.48
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.48
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Breastplate of
    Valor, Tyrfing, Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance,
    Eye of Providence, Stone of Binding, Eye of the Storm, Shield of the Phoenix,
    Hydra''s Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, The Reaper, Spear of Desolation, Spear of the Magus, Bragi''s
    Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging
    Blade.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.17
      fit: 0.33
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
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
    Draconic Scale, Stone of Binding, Hide of the Nemean Lion, Eye of the Storm, Arondight,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s
    Grace, Obsidian Shard, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.64
      pick: 0.17
      fit: 0.64
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.54
      pick: 0.2
      fit: 0.45
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.17
      fit: 0.38
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.54
      pick: 0.2
      fit: 0.42
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
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
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.17
      fit: 0.38
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.54
      pick: 0.2
      fit: 0.42
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
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
      total: 0.5
      efficiency: 0.66
      win: 0.45
      pick: 0.17
      fit: 0.37
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.64
      pick: 0.17
      fit: 0.62
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.54
      pick: 0.2
      fit: 0.68
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.68
  starter: *id001
---
