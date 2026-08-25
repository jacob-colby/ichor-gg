---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.53
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.16
    win_rate: 0.62
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.58
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.49
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.59
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.65
  - name: Stampede
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.58
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.63
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.6
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.68
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.68
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.59
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.79
  - name: Veve Charm
    pick_rate: 0.08
    win_rate: 0.89
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.43
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.64
  community_starters:
  - name: Selflessness
    pick_rate: 0.24
    win_rate: 0.58
  - name: Warrior's Axe
    pick_rate: 0.17
    win_rate: 0.57
  - name: Heroism
    pick_rate: 0.14
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-08-25'
  god_win_rate: 0.5773809523809523
  god_matches_won: 291
  god_matches_played: 504
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-25'
  god_matches_analyzed: 18716
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Jotunn''s Revenge, Breastplate
    of Valor, Erosion, Shifter''s Shield, Eye of Providence, Draconic Scale, Berserker''s
    Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Runeforged
    Hammer, Screeching Gargoyle, Midgardian Mail, Prophetic Cloak, Leviathan''s Hide,
    Void Shield, Ancile, Oni Hunter''s Garb, Spear of Desolation, Helm of Darkness,
    Xibalban Effigy, Gladiator''s Shield, Void Stone, Spectral Armor, Hussar''s Wings,
    Rod of Asclepius, Hydra''s Lament, Daybreak Gavel, Soul Gem, Doublet of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.62
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.67
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.59
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
  - Freya's Tears
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
    Shield, Erosion, Shifter''s Shield, Eye of Providence, Draconic Scale, Ethereal
    Staff, Phoenix Feather, Chandra''s Grace, Yogi''s Necklace, Gluttonous Grimoire,
    Shield Splitter, Glorious Pridwen, Runeforged Hammer, Eye of the Storm, Midgardian
    Mail, Stone of Binding, Lifebinder, Helm of Radiance, Leviathan''s Hide, Void
    Shield, Magi''s Cloak, Ancile, Screeching Gargoyle, Oni Hunter''s Garb, Daybreak
    Gavel, Gladiator''s Shield, Sphere of Negation, Spear of Desolation, Void Stone,
    Mantle Of Discord.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.55
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.59
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
  - Rod of Tahuti
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
    Shifter''s Shield, Eye of Providence, Shield of the Phoenix, Draconic Scale, Doom
    Orb, Helm of Radiance, Runeforged Hammer, The World Stone, Titan''s Bane, Magi''s
    Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of Discord, The
    Reaper, Midgardian Mail, Daybreak Gavel, Hydra''s Lament, Rod of Asclepius, Leviathan''s
    Hide.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.59
      pick: 0.0
      fit: 0.38
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
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
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Shifter''s
    Shield, Helm of Radiance, Hydra''s Lament, Shield of the Phoenix, Stone of Binding,
    Eye of Providence, Eye of the Storm, Toxic Blade, Draconic Scale, Magi''s Cloak,
    Screeching Gargoyle, Daybreak Gavel, Spear of Desolation, The Reaper, Spear of
    the Magus, Midgardian Mail, Bragi''s Harp, Mantle Of Discord, Tekko-Kagi, Rod
    of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.21
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.29
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.59
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
    Runeforged Hammer, Gluttonous Grimoire, Shifter''s Shield, Eye of Providence,
    Gladiator''s Shield, Draconic Scale, Stone of Binding, Eye of the Storm, Arondight,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s
    Grace, Obsidian Shard, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.64
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.59
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
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.22
      fit: 0.38
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.62
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.12
      fit: 0.67
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.67
  starter: *id001
---
