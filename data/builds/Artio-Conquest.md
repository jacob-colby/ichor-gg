---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.5
  aspect_win_rate: 0.59
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.18
    win_rate: 0.51
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.15
      win_rate: 0.57
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.47
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.53
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.46
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.35
  - name: Hide of the Nemean Lion
    pick_rate: 0.04
    win_rate: 0.39
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.57
  - name: Olmec Blue
    pick_rate: 0.06
    win_rate: 0.6
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.71
    - name: Mote of Chaos
      pick_rate: 0.04
      win_rate: 0.58
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.22
    win_rate: 0.54
  - name: Bumba's Cudgel
    pick_rate: 0.14
    win_rate: 0.36
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-11-03'
  god_win_rate: 0.5303326810176126
  god_matches_won: 271
  god_matches_played: 511
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Kinetic Cuirass, Jotunn''s
    Revenge, Berserker''s Shield, Runeforged Hammer, Erosion, Eye of Providence, Hydra''s
    Lament, Prophetic Cloak, Draconic Scale, Oni Hunter''s Garb, Shield of the Phoenix,
    Helm of Darkness, Stone of Binding, Midgardian Mail, Avenging Blade, Helm of Radiance,
    Gluttonous Grimoire, Titan''s Bane, Magi''s Cloak, Wyrmskin Hide, Leviathan''s
    Hide, Mantle Of Discord, Screeching Gargoyle, Breastplate of Valor, Spear of Desolation,
    Arondight, Obsidian Shard, Ancile, Death Metal, Soul Gem, Stampede, Void Stone,
    Void Shield, The Crusher, Golden Blade, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.5
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Jotunn''s Revenge, Shield Splitter, Berserker''s Shield, Runeforged Hammer, Soul
    Gem, Phoenix Feather, Yogi''s Necklace, The Reaper, Ethereal Staff, Erosion, Eye
    of Providence, Hydra''s Lament, Oni Hunter''s Garb, Draconic Scale, Chandra''s
    Grace, Avenging Blade, Gluttonous Grimoire, Midgardian Mail, Wyrmskin Hide, Regrowth
    Striders, Glorious Pridwen, Leviathan''s Hide, Rod of Asclepius, Titan''s Bane,
    Blood-Bound Book, Helm of Radiance, Helm of Darkness, Stone of Binding, Sphere
    of Negation, Spear of Desolation, Soul Locket, Arondight, Magi''s Cloak, Screeching
    Gargoyle, Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.57
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.46
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Avenging Blade, Titan''s Bane, Gluttonous Grimoire, Screeching Gargoyle, Shield
    Splitter, Berserker''s Shield, Spear of Desolation, Kinetic Cuirass, Obsidian
    Shard, Soul Gem, Void Stone, Void Shield, The Crusher, Runeforged Hammer, Spear
    of the Magus, Heartseeker, The Reaper, Hydra''s Lament, Oni Hunter''s Garb, Doom
    Orb, Erosion, Tekko-Kagi, Eye of Providence, The World Stone, Helm of Radiance,
    Draconic Scale, Shield of the Phoenix, Midgardian Mail, Helm of Darkness, Dreamer''s
    Idol, Magi''s Cloak, Breastplate of Valor, Leviathan''s Hide, Pendulum Blade,
    Avatar''s Parashu, Mantle Of Discord.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.68
    Avenging Blade:
      total: 0.52
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.36
    Titan's Bane:
      total: 0.52
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Nimble Ring, Jotunn''s
    Revenge, Golden Blade, Kinetic Cuirass, Shield Splitter, Gluttonous Grimoire,
    Tyrfing, Soul Gem, Tekko-Kagi, Runeforged Hammer, Pharaoh''s Curse, Lernaean Bow,
    Toxic Blade, Silverbranch Bow, Eros'' Bow, Hydra''s Lament, Oni Hunter''s Garb,
    Shogun''s Ofuda, Helm of Radiance, Erosion, Eye of Providence, Obsidian Shard,
    Spear of Desolation, The Reaper, Midgardian Mail, Shield of the Phoenix, Stone
    of Binding, Draconic Scale, Riptalon, Titan''s Bane, Dominance, Screeching Gargoyle,
    Helm of Darkness, Breastplate of Valor, Magi''s Cloak, Bragi''s Harp, Blood-Bound
    Book.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.53
      pick: 0.17
      fit: 0.19
    Berserker's Shield:
      total: 0.57
      efficiency: 0.74
      win: 0.55
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.51
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.31
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Spear of Desolation, Prophetic Cloak, Kinetic Cuirass, Berserker''s
    Shield, Hydra''s Lament, Shield of the Phoenix, Soul Gem, Screeching Gargoyle,
    Breastplate of Valor, Shield Splitter, Lotus Sickle, Chronos'' Pendant, Arondight,
    Runeforged Hammer, Helm of Radiance, Gluttonous Grimoire, Oni Hunter''s Garb,
    Erosion, Gladiator''s Shield, Helm of Darkness, Eye of Providence, Gem of Focus,
    Obsidian Shard, Heartwood Charm, Draconic Scale, Stone of Binding, Midgardian
    Mail, Chandra''s Grace, Eye of Erebus, Magi''s Cloak, Regrowth Striders, Leviathan''s
    Hide, Mantle Of Discord, Ancient Signet, Glorious Pridwen, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.53
      pick: 0.17
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.63
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.14
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Kinetic Cuirass, Runeforged Hammer, Tekko-Kagi,
    Titan''s Bane, Golden Blade, Hydra''s Lament, Gluttonous Grimoire, Spear of Desolation,
    Obsidian Shard, The Crusher, Tyrfing, Lernaean Bow, Avenging Blade, Oni Hunter''s
    Garb, Soul Gem, Heartseeker, Erosion, Eye of Providence, The Reaper, Helm of Radiance,
    Arondight, Shield of the Phoenix, Draconic Scale, Midgardian Mail, Stone of Binding,
    Toxic Blade, Death Metal, Spear of the Magus, Pharaoh''s Curse, Helm of Darkness,
    Wyrmskin Hide, Magi''s Cloak, Screeching Gargoyle, Breastplate of Valor, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.53
      pick: 0.17
      fit: 0.22
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.55
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.47
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Shield Splitter, Gluttonous Grimoire, Berserker''s Shield, Kinetic
    Cuirass, Spear of Desolation, Obsidian Shard, Soul Gem, Runeforged Hammer, Helm
    of Radiance, Titan''s Bane, Spear of the Magus, Helm of Darkness, Hydra''s Lament,
    Death Metal, Oni Hunter''s Garb, Ancient Signet, Lotus Sickle, The Crusher, Erosion,
    Doom Orb, Jade Scepter, Eye of Providence, The World Stone, Avenging Blade, Shield
    of the Phoenix, Draconic Scale, Heartseeker, Midgardian Mail, Stone of Binding,
    Chronos'' Pendant, The Reaper, Magi''s Cloak, Screeching Gargoyle, Triton''s Conch,
    Arondight, Breastplate of Valor, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.53
      pick: 0.17
      fit: 0.22
    Berserker's Shield:
      total: 0.52
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.42
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Kinetic
    Cuirass, Jotunn''s Revenge, Berserker''s Shield, Runeforged Hammer, Breastplate
    of Valor, Erosion, Eye of Providence, Hydra''s Lament, Draconic Scale, Oni Hunter''s
    Garb, Shield of the Phoenix, Helm of Darkness, Stone of Binding, Midgardian Mail,
    Avenging Blade, Helm of Radiance, Gluttonous Grimoire, Titan''s Bane, Magi''s
    Cloak, Wyrmskin Hide, Leviathan''s Hide, Mantle Of Discord, Screeching Gargoyle,
    Spear of Desolation, Arondight, Obsidian Shard, Ancile, Hide of the Nemean Lion,
    Death Metal, Soul Gem, Stampede, Void Stone, Void Shield, The Crusher, Prophetic
    Cloak, Golden Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.53
      pick: 0.17
      fit: 0.31
    Berserker's Shield:
      total: 0.54
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Genji's Guard
  starter: *id001
---
