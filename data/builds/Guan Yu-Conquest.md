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
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.6
  - name: Hunter's Cowl
    pick_rate: 0.14
    win_rate: 0.58
  - name: Bluestone Pendant
    pick_rate: 0.12
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-11-02'
  god_win_rate: 0.5333333333333333
  god_matches_won: 96
  god_matches_played: 180
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
  - Kinetic Cuirass
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
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Shield Splitter, Kinetic
    Cuirass, Breastplate of Valor, Runeforged Hammer, Golden Blade, Hydra''s Lament,
    Shield of the Phoenix, Helm of Radiance, Erosion, Spear of Desolation, Tyrfing,
    Eye of Providence, Helm of Darkness, Gluttonous Grimoire, Oni Hunter''s Garb,
    Tekko-Kagi, Screeching Gargoyle, Stone of Binding, Soul Gem, Titan''s Bane, Obsidian
    Shard, Avenging Blade, Midgardian Mail, Arondight, Lernaean Bow, Magi''s Cloak,
    Pharaoh''s Curse, Shifter''s Shield, Death Metal, Leviathan''s Hide, Mantle Of
    Discord, Nimble Ring, Draconic Scale, Eros'' Bow, Shogun''s Ofuda, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.63
      efficiency: 0.75
      win: 0.67
      pick: 0.16
      fit: 0.39
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
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
  - Book of Thoth
  - Chandra's Grace
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Chandra''s Grace, Jotunn''s Revenge, Shield
    of the Phoenix, Soul Gem, Kinetic Cuirass, Shield Splitter, Runeforged Hammer,
    Golden Blade, Breastplate of Valor, Ethereal Staff, Phoenix Feather, Yogi''s Necklace,
    The Reaper, Hydra''s Lament, Gluttonous Grimoire, Blood-Bound Book, Erosion, Spear
    of Desolation, Tyrfing, Eye of Providence, Oni Hunter''s Garb, Helm of Radiance,
    Avenging Blade, Sphere of Negation, Rod of Asclepius, Regrowth Striders, Tekko-Kagi,
    Midgardian Mail, Glorious Pridwen, Helm of Darkness, Titan''s Bane, Obsidian Shard,
    Pharaoh''s Curse, Arondight, Screeching Gargoyle, Lernaean Bow, Draconic Scale.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.09
    Chandra's Grace:
      total: 0.57
      efficiency: 0.47
      win: 0.69
      pick: 0.1
      fit: 0.61
    Berserker's Shield:
      total: 0.63
      efficiency: 0.75
      win: 0.67
      pick: 0.16
      fit: 0.41
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.36
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.19
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Screeching Gargoyle,
    Stone of Binding, Spear of Desolation, Avenging Blade, Gluttonous Grimoire, Obsidian
    Shard, Titan''s Bane, Tekko-Kagi, Shield Splitter, Soul Gem, Kinetic Cuirass,
    Void Stone, Breastplate of Valor, Void Shield, Spear of the Magus, Runeforged
    Hammer, The Crusher, Heartseeker, Hydra''s Lament, Toxic Blade, Silverbranch Bow,
    Golden Blade, The Reaper, Doom Orb, Helm of Radiance, The World Stone, Tyrfing,
    Shield of the Phoenix, Oni Hunter''s Garb, Erosion, Helm of Darkness, Eye of Providence,
    Dreamer''s Idol, Midgardian Mail, Lernaean Bow, Arondight.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.62
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.61
      efficiency: 0.75
      win: 0.67
      pick: 0.16
      fit: 0.3
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.87
      win: 0.6
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
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
  - Golden Blade
  - Kinetic Cuirass
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
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Nimble Ring, Golden
    Blade, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Soul Gem, Breastplate
    of Valor, Tyrfing, Runeforged Hammer, Tekko-Kagi, Hydra''s Lament, Lernaean Bow,
    Pharaoh''s Curse, Helm of Radiance, Spear of Desolation, Eros'' Bow, Toxic Blade,
    Silverbranch Bow, Obsidian Shard, Shogun''s Ofuda, Oni Hunter''s Garb, Shield
    of the Phoenix, Screeching Gargoyle, Erosion, Helm of Darkness, Blood-Bound Book,
    Eye of Providence, Stone of Binding, The Reaper, Bragi''s Harp, Midgardian Mail,
    Titan''s Bane, Riptalon, Magi''s Cloak, Dominance, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.63
      efficiency: 0.75
      win: 0.67
      pick: 0.16
      fit: 0.41
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.23
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
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
  - Kinetic Cuirass
  - Spear of Desolation
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Chandra''s Grace, Spear of Desolation, Kinetic
    Cuirass, Hydra''s Lament, Shield of the Phoenix, Soul Gem, Screeching Gargoyle,
    Shield Splitter, Chronos'' Pendant, Arondight, Runeforged Hammer, Helm of Radiance,
    Prophetic Cloak, Gluttonous Grimoire, Golden Blade, Helm of Darkness, Erosion,
    Obsidian Shard, Gem of Focus, Eye of Providence, Oni Hunter''s Garb, Gladiator''s
    Shield, Heartwood Charm, Stone of Binding, Midgardian Mail, Nimble Ring, Magi''s
    Cloak, Pharaoh''s Curse, Tyrfing, Eye of Erebus, Leviathan''s Hide, Mantle Of
    Discord, Eros'' Bow, Shifter''s Shield, Draconic Scale.'
  slot_scores:
    Chandra's Grace:
      total: 0.54
      efficiency: 0.47
      win: 0.69
      pick: 0.1
      fit: 0.43
    Berserker's Shield:
      total: 0.62
      efficiency: 0.75
      win: 0.67
      pick: 0.16
      fit: 0.34
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Chandra's Grace
  - Berserker's Shield
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
  - Shield Splitter
  - Kinetic Cuirass
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Shield
    Splitter, Kinetic Cuirass, Breastplate of Valor, Runeforged Hammer, Golden Blade,
    Hydra''s Lament, Shield of the Phoenix, Helm of Radiance, Erosion, Spear of Desolation,
    Tyrfing, Eye of Providence, Helm of Darkness, Gluttonous Grimoire, Draconic Scale,
    Oni Hunter''s Garb, Tekko-Kagi, Screeching Gargoyle, Stone of Binding, Soul Gem,
    Titan''s Bane, Obsidian Shard, Avenging Blade, Midgardian Mail, Arondight, Lernaean
    Bow, Magi''s Cloak, Pharaoh''s Curse, Shifter''s Shield, Death Metal, Leviathan''s
    Hide, Mantle Of Discord, Nimble Ring, Eros'' Bow, Shogun''s Ofuda, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.63
      efficiency: 0.75
      win: 0.67
      pick: 0.16
      fit: 0.39
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.45
      pick: 0.15
      fit: 0.29
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Berserker's Shield
  - Genji's Guard
  starter: *id001
---
