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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Shield Splitter, Kinetic
    Cuirass, Breastplate of Valor, Runeforged Hammer, Golden Blade, Hydra''s Lament,
    Helm of Radiance, Spear of Desolation, Erosion, Shield of the Phoenix, Oni Hunter''s
    Garb, Eye of Providence, Tyrfing, Gluttonous Grimoire, Helm of Darkness, Tekko-Kagi,
    Soul Gem, Obsidian Shard, Screeching Gargoyle, Stone of Binding, Titan''s Bane,
    Midgardian Mail, Avenging Blade, Arondight, Lernaean Bow, Pharaoh''s Curse, Magi''s
    Cloak, Lotus Sickle, Death Metal, Leviathan''s Hide, Shifter''s Shield, Eros''
    Bow, Mantle Of Discord, Nimble Ring, Draconic Scale, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.63
      efficiency: 0.74
      win: 0.67
      pick: 0.16
      fit: 0.39
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
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
    this god: Amanita Charm, Rod of Tahuti, Chandra''s Grace, Shield of the Phoenix,
    Jotunn''s Revenge, Soul Gem, Kinetic Cuirass, Shield Splitter, Runeforged Hammer,
    Golden Blade, Ethereal Staff, Breastplate of Valor, Phoenix Feather, Yogi''s Necklace,
    The Reaper, Hydra''s Lament, Gluttonous Grimoire, Blood-Bound Book, Oni Hunter''s
    Garb, Spear of Desolation, Erosion, Eye of Providence, Tyrfing, Rod of Asclepius,
    Helm of Radiance, Regrowth Striders, Avenging Blade, Sphere of Negation, Tekko-Kagi,
    Midgardian Mail, Glorious Pridwen, Helm of Darkness, Obsidian Shard, Titan''s
    Bane, Eros'' Bow, Pharaoh''s Curse, Arondight, Screeching Gargoyle, Draconic Scale.'
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
      efficiency: 0.74
      win: 0.67
      pick: 0.16
      fit: 0.41
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
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
  - Berserker's Shield
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Screeching Gargoyle,
    Spear of Desolation, Stone of Binding, Avenging Blade, Gluttonous Grimoire, Obsidian
    Shard, Titan''s Bane, Tekko-Kagi, Shield Splitter, Soul Gem, Kinetic Cuirass,
    Void Stone, Void Shield, Breastplate of Valor, Spear of the Magus, Runeforged
    Hammer, The Crusher, Hydra''s Lament, Toxic Blade, Heartseeker, Silverbranch Bow,
    Golden Blade, The Reaper, Doom Orb, Helm of Radiance, The World Stone, Oni Hunter''s
    Garb, Tyrfing, Shield of the Phoenix, Erosion, Helm of Darkness, Eye of Providence,
    Dreamer''s Idol, Midgardian Mail, Lotus Sickle, Draconic Scale.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.61
      efficiency: 0.74
      win: 0.67
      pick: 0.16
      fit: 0.3
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.6
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.44
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
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Jotunn''s Revenge, Golden
    Blade, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Soul Gem, Breastplate
    of Valor, Tyrfing, Runeforged Hammer, Tekko-Kagi, Hydra''s Lament, Eros'' Bow,
    Pharaoh''s Curse, Lernaean Bow, Helm of Radiance, Spear of Desolation, Toxic Blade,
    Silverbranch Bow, Oni Hunter''s Garb, Obsidian Shard, Shogun''s Ofuda, Shield
    of the Phoenix, Erosion, Blood-Bound Book, Helm of Darkness, Screeching Gargoyle,
    Eye of Providence, Midgardian Mail, Bragi''s Harp, Stone of Binding, The Reaper,
    Lotus Sickle, Titan''s Bane, Dominance, Riptalon, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.63
      efficiency: 0.74
      win: 0.67
      pick: 0.16
      fit: 0.41
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
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
      efficiency: 0.63
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
    Amanita Charm, Breastplate of Valor, Chandra''s Grace, Spear of Desolation, Kinetic
    Cuirass, Hydra''s Lament, Shield of the Phoenix, Soul Gem, Shield Splitter, Screeching
    Gargoyle, Lotus Sickle, Chronos'' Pendant, Arondight, Runeforged Hammer, Helm
    of Radiance, Prophetic Cloak, Gluttonous Grimoire, Oni Hunter''s Garb, Golden
    Blade, Helm of Darkness, Obsidian Shard, Erosion, Eye of Providence, Gem of Focus,
    Gladiator''s Shield, Heartwood Charm, Stone of Binding, Midgardian Mail, Nimble
    Ring, Magi''s Cloak, Eros'' Bow, Pharaoh''s Curse, Leviathan''s Hide, Tyrfing,
    Eye of Erebus, Mantle Of Discord, Draconic Scale.'
  slot_scores:
    Chandra's Grace:
      total: 0.54
      efficiency: 0.47
      win: 0.69
      pick: 0.1
      fit: 0.43
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
      win: 0.67
      pick: 0.16
      fit: 0.34
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
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
    Hydra''s Lament, Helm of Radiance, Spear of Desolation, Erosion, Shield of the
    Phoenix, Oni Hunter''s Garb, Eye of Providence, Tyrfing, Gluttonous Grimoire,
    Helm of Darkness, Draconic Scale, Tekko-Kagi, Soul Gem, Obsidian Shard, Screeching
    Gargoyle, Stone of Binding, Titan''s Bane, Midgardian Mail, Avenging Blade, Arondight,
    Lernaean Bow, Pharaoh''s Curse, Magi''s Cloak, Lotus Sickle, Death Metal, Leviathan''s
    Hide, Shifter''s Shield, Eros'' Bow, Mantle Of Discord, Nimble Ring, Shogun''s
    Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.63
      efficiency: 0.74
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
      total: 0.56
      efficiency: 0.67
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
