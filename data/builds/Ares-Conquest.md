---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.57
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.16
    win_rate: 0.62
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.51
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.68
  - name: Stampede
    pick_rate: 0.12
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.59
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.62
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.56
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.73
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.63
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.64
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.86
  - name: Veve Charm
    pick_rate: 0.09
    win_rate: 0.89
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.43
    - name: Medallion
      pick_rate: 0.05
      win_rate: 0.78
  community_starters:
  - name: Selflessness
    pick_rate: 0.24
    win_rate: 0.6
  - name: Warrior's Axe
    pick_rate: 0.17
    win_rate: 0.53
  - name: Heroism
    pick_rate: 0.14
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-08-23'
  god_win_rate: 0.5862068965517241
  god_matches_won: 255
  god_matches_played: 435
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-23'
  god_matches_analyzed: 15677
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
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Jotunn''s Revenge, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Berserker''s Shield, Shield
    Splitter, Shield of the Phoenix, Shifter''s Shield, Stone of Binding, Magi''s
    Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Runeforged Hammer, Screeching Gargoyle, Midgardian Mail, Prophetic Cloak, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Spear of Desolation, Helm of Darkness,
    Xibalban Effigy, Gladiator''s Shield, Void Stone, Spectral Armor, Hussar''s Wings,
    Rod of Asclepius, Hydra''s Lament, Daybreak Gavel, Soul Gem, Doublet of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.7
      efficiency: 0.61
      win: 0.86
      pick: 0.15
      fit: 0.62
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.67
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.67
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Jotunn''s Revenge, Rod of Asclepius, Soul Gem, Breastplate of Valor, Berserker''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Ethereal Staff, Phoenix Feather,
    Shifter''s Shield, Chandra''s Grace, Yogi''s Necklace, Gluttonous Grimoire, Shield
    Splitter, Glorious Pridwen, Runeforged Hammer, Eye of the Storm, Midgardian Mail,
    Stone of Binding, Lifebinder, Helm of Radiance, Leviathan''s Hide, Void Shield,
    Magi''s Cloak, Ancile, Screeching Gargoyle, Oni Hunter''s Garb, Daybreak Gavel,
    Gladiator''s Shield, Sphere of Negation, Spear of Desolation, Void Stone, Mantle
    Of Discord.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.69
      efficiency: 0.61
      win: 0.86
      pick: 0.15
      fit: 0.55
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.95
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Void Shield, Breastplate of Valor, Spear of the Magus, Soul Gem, Void Stone, Obsidian
    Shard, Avenging Blade, Berserker''s Shield, Heartseeker, Erosion, Shield Splitter,
    Eye of Providence, Shield of the Phoenix, Draconic Scale, Doom Orb, Helm of Radiance,
    Runeforged Hammer, The World Stone, Shifter''s Shield, Titan''s Bane, Magi''s
    Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of Discord, The
    Reaper, Midgardian Mail, Daybreak Gavel, Hydra''s Lament, Rod of Asclepius, Leviathan''s
    Hide.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.57
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.86
      pick: 0.15
      fit: 0.44
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.47
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
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Breastplate of
    Valor, Tyrfing, Shield Splitter, Soul Gem, Runeforged Hammer, Pharaoh''s Curse,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance,
    Hydra''s Lament, Shield of the Phoenix, Stone of Binding, Eye of Providence, Eye
    of the Storm, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, Spear of Desolation, Shifter''s Shield, The Reaper, Spear of the
    Magus, Midgardian Mail, Bragi''s Harp, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius,
    Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.29
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.86
      pick: 0.15
      fit: 0.34
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
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
    Draconic Scale, Stone of Binding, Eye of the Storm, Arondight, Gem of Focus, Shifter''s
    Shield, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle
    Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace,
    Obsidian Shard, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 0.86
      pick: 0.15
      fit: 0.64
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.45
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Runeforged Hammer, Screeching Gargoyle, Midgardian Mail, Prophetic
    Cloak, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Spear of Desolation,
    Helm of Darkness, Xibalban Effigy, Gladiator''s Shield, Void Stone, Spectral Armor,
    Hussar''s Wings, Rod of Asclepius, Hydra''s Lament, Daybreak Gavel, Soul Gem,
    Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.51
      pick: 0.22
      fit: 0.38
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.7
      efficiency: 0.61
      win: 0.86
      pick: 0.15
      fit: 0.62
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.12
      fit: 0.67
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.67
  starter: *id001
---
