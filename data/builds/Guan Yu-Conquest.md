---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.47
  aspect_win_rate: 0.55
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.11
    win_rate: 0.55
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.11
      win_rate: 0.65
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.11
    win_rate: 0.45
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.61
    - name: Chandra's Grace
      pick_rate: 0.07
      win_rate: 0.69
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.42
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.52
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.59
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 1.0
    - name: Brawler’s Beat Stick
      pick_rate: 0.05
      win_rate: 0.63
  - name: Sage's Ring
    pick_rate: 0.05
    win_rate: 0.8
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.6
    - name: Olmec Blue
      pick_rate: 0.04
      win_rate: 0.5
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.15
    win_rate: 0.58
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.6
  - name: Bluestone Pendant
    pick_rate: 0.12
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-11-02'
  god_win_rate: 0.5307262569832403
  god_matches_won: 95
  god_matches_played: 179
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Breastplate of Valor, Golden Blade, Runeforged Hammer, Hydra''s Lament,
    Shield of the Phoenix, Erosion, Sundering Echo, Gluttonous Grimoire, Spear of
    Desolation, Eye of Providence, Oni Hunter''s Garb, Tyrfing, Helm of Radiance,
    Helm of Darkness, Draconic Scale, Screeching Gargoyle, Obsidian Shard, Soul Gem,
    Tekko-Kagi, Stone of Binding, Titan''s Bane, Midgardian Mail, Pharaoh''s Curse,
    Shifter''s Shield, Magi''s Cloak, Leviathan''s Hide, Nimble Ring, Lernaean Bow,
    Mantle Of Discord, Shogun''s Ofuda, Eros'' Bow, Avenging Blade, Arondight, Wyrmskin
    Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.7
      win: 0.67
      pick: 0.16
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Berserker's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Chandra's Grace
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Chandra''s Grace, Rod of Tahuti, Shield of the Phoenix,
    Jotunn''s Revenge, Soul Gem, Kinetic Cuirass, Shield Splitter, Golden Blade, Breastplate
    of Valor, Yogi''s Necklace, Phoenix Feather, Ethereal Staff, Runeforged Hammer,
    The Reaper, Hydra''s Lament, Gluttonous Grimoire, Erosion, Oni Hunter''s Garb,
    Sundering Echo, Blood-Bound Book, Spear of Desolation, Eye of Providence, Regrowth
    Striders, Glorious Pridwen, Rod of Asclepius, Tyrfing, Sphere of Negation, Draconic
    Scale, Midgardian Mail, Pharaoh''s Curse, Obsidian Shard, Helm of Radiance, Tekko-Kagi,
    Titan''s Bane, Screeching Gargoyle, Eros'' Bow, Avenging Blade, Helm of Darkness.'
  slot_scores:
    Chandra's Grace:
      total: 0.57
      efficiency: 0.46
      win: 0.69
      pick: 0.1
      fit: 0.61
    Berserker's Shield:
      total: 0.62
      efficiency: 0.7
      win: 0.67
      pick: 0.16
      fit: 0.41
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.52
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Chandra's Grace
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Screeching Gargoyle,
    Stone of Binding, Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, Titan''s
    Bane, Soul Gem, Avenging Blade, Kinetic Cuirass, Tekko-Kagi, Void Stone, Shield
    Splitter, Void Shield, Breastplate of Valor, Spear of the Magus, Toxic Blade,
    Heartseeker, Silverbranch Bow, The Crusher, Runeforged Hammer, Hydra''s Lament,
    Golden Blade, Doom Orb, The Reaper, The World Stone, Sundering Echo, Oni Hunter''s
    Garb, Helm of Radiance, Shield of the Phoenix, Erosion, Tyrfing, Eye of Providence,
    Midgardian Mail, Helm of Darkness, Nimble Ring, Draconic Scale.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.62
    Stone of Binding:
      total: 0.52
      efficiency: 0.47
      win: 0.58
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.6
      efficiency: 0.7
      win: 0.67
      pick: 0.16
      fit: 0.3
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.81
      win: 0.58
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Berserker's Shield
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Jotunn''s Revenge, Gluttonous
    Grimoire, Kinetic Cuirass, Golden Blade, Soul Gem, Breastplate of Valor, Shield
    Splitter, Tyrfing, Pharaoh''s Curse, Tekko-Kagi, Toxic Blade, Runeforged Hammer,
    Eros'' Bow, Silverbranch Bow, Hydra''s Lament, Lernaean Bow, Shogun''s Ofuda,
    Spear of Desolation, Obsidian Shard, Oni Hunter''s Garb, Helm of Radiance, Shield
    of the Phoenix, Sundering Echo, Riptalon, Screeching Gargoyle, Erosion, Stone
    of Binding, Midgardian Mail, Eye of Providence, Blood-Bound Book, Helm of Darkness,
    The Reaper, Titan''s Bane, Draconic Scale, Bragi''s Harp, Magi''s Cloak.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.62
      efficiency: 0.7
      win: 0.67
      pick: 0.16
      fit: 0.41
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.23
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.52
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chandra's Grace
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Chandra''s Grace, Amanita Charm, Spear of Desolation, Kinetic
    Cuirass, Shield of the Phoenix, Hydra''s Lament, Soul Gem, Screeching Gargoyle,
    Shield Splitter, Chronos'' Pendant, Prophetic Cloak, Gluttonous Grimoire, Arondight,
    Runeforged Hammer, Gladiator''s Shield, Obsidian Shard, Helm of Radiance, Erosion,
    Oni Hunter''s Garb, Golden Blade, Heartwood Charm, Gem of Focus, Eye of Providence,
    Helm of Darkness, Stone of Binding, Sundering Echo, Draconic Scale, Midgardian
    Mail, Nimble Ring, Pharaoh''s Curse, Magi''s Cloak, Leviathan''s Hide, Eros''
    Bow, Shifter''s Shield, Mantle Of Discord, Eye of Erebus.'
  slot_scores:
    Chandra's Grace:
      total: 0.54
      efficiency: 0.46
      win: 0.69
      pick: 0.1
      fit: 0.43
    Berserker's Shield:
      total: 0.61
      efficiency: 0.7
      win: 0.67
      pick: 0.16
      fit: 0.34
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.3
      fit: 0.58
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Chandra's Grace
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Breastplate of Valor, Golden Blade, Runeforged Hammer,
    Hydra''s Lament, Shield of the Phoenix, Erosion, Sundering Echo, Gluttonous Grimoire,
    Spear of Desolation, Eye of Providence, Oni Hunter''s Garb, Draconic Scale, Tyrfing,
    Helm of Radiance, Helm of Darkness, Screeching Gargoyle, Obsidian Shard, Soul
    Gem, Tekko-Kagi, Stone of Binding, Titan''s Bane, Midgardian Mail, Pharaoh''s
    Curse, Shifter''s Shield, Magi''s Cloak, Leviathan''s Hide, Nimble Ring, Lernaean
    Bow, Mantle Of Discord, Shogun''s Ofuda, Eros'' Bow, Avenging Blade, Arondight,
    Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.7
      win: 0.67
      pick: 0.16
      fit: 0.39
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.45
      pick: 0.15
      fit: 0.29
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Berserker's Shield
  - Genji's Guard
  starter: *id001
---
