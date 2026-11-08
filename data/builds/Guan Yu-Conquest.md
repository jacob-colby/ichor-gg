---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.86
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.69
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.13
      win_rate: 0.5
    - name: Devourer's Gauntlet
      pick_rate: 0.11
      win_rate: 0.55
  - name: Berserker's Shield
    pick_rate: 0.15
    win_rate: 0.57
    alternates:
    - name: Tekko-Kagi
      pick_rate: 0.07
      win_rate: 0.43
    - name: Brawler’s Beat Stick
      pick_rate: 0.07
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.73
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.67
  - name: Nimble Ring
    pick_rate: 0.1
    win_rate: 0.78
    alternates:
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.44
    - name: Brawler’s Beat Stick
      pick_rate: 0.09
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.07
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.67
    - name: Brawler’s Beat Stick
      pick_rate: 0.07
      win_rate: 0.83
  - name: Stalwart Sigil
    pick_rate: 0.06
    win_rate: 0.0
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.06
      win_rate: 1.0
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.23
    win_rate: 0.59
  - name: Sands Of Time
    pick_rate: 0.21
    win_rate: 0.5
  - name: Pendulum of the Ages
    pick_rate: 0.16
    win_rate: 0.8
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-11-08'
  god_win_rate: 0.6041666666666666
  god_matches_won: 58
  god_matches_played: 96
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shield Splitter,
    Soul Gem, Gluttonous Grimoire, Breastplate of Valor, Shield of the Phoenix, Tyrfing,
    Runeforged Hammer, Hydra''s Lament, Draconic Scale, Golden Blade, Oni Hunter''s
    Garb, Spear of Desolation, Lotus Sickle, The Reaper, Erosion, Eye of Providence,
    Screeching Gargoyle, Blood-Bound Book, Helm of Radiance, Death Metal, Midgardian
    Mail, Helm of Darkness, Stone of Binding, Leviathan''s Hide, Bragi''s Harp, Hide
    of the Nemean Lion, Arondight, Ancient Signet, Magi''s Cloak, Mantle Of Discord,
    Chronos'' Pendant, Avenging Blade, The Crusher.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.58
      efficiency: 0.45
      win: 0.83
      pick: 0.15
      fit: 0.29
    Genji's Guard:
      total: 0.63
      efficiency: 0.71
      win: 0.73
      pick: 0.19
      fit: 0.26
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.68
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.68
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.82
      win: 1.0
      pick: 0.15
      fit: 0.12
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.68
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Rod of Tahuti
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Kinetic Cuirass, The
    Reaper, Blood-Bound Book, Jotunn''s Revenge, Gluttonous Grimoire, Shield Splitter,
    Phoenix Feather, Yogi''s Necklace, Ethereal Staff, Breastplate of Valor, Chandra''s
    Grace, Runeforged Hammer, Tyrfing, Bancroft''s Talon, Golden Blade, Hydra''s Lament,
    Oni Hunter''s Garb, Draconic Scale, Spear of Desolation, Regrowth Striders, Riptalon,
    Lotus Sickle, Bloodforge, Rod of Asclepius, Erosion, Soul Locket, Eye of Providence,
    Midgardian Mail, Screeching Gargoyle, Glorious Pridwen, Death Metal, Helm of Radiance,
    Sphere of Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.73
      pick: 0.19
      fit: 0.25
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.68
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.68
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.82
      win: 1.0
      pick: 0.15
      fit: 0.12
    Amanita Charm:
      total: 0.65
      efficiency: 0.68
      win: 0.68
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.62
      efficiency: 0.58
      win: 0.68
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire, Amanita Charm,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Stone of Binding, The
    Reaper, Avenging Blade, Shield Splitter, Void Stone, Void Shield, Breastplate
    of Valor, The Crusher, Obsidian Shard, Heartseeker, Shield of the Phoenix, Spear
    of the Magus, Tyrfing, Runeforged Hammer, Hydra''s Lament, Titan''s Bane, Oni
    Hunter''s Garb, Lotus Sickle, Dreamer''s Idol, Draconic Scale, Toxic Blade, Blood-Bound
    Book, Golden Blade, Helm of Radiance, Erosion, Silverbranch Bow, Death Metal,
    Eye of Providence, Midgardian Mail, Tekko-Kagi.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.48
      win: 0.68
      pick: 0.0
      fit: 0.07
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.73
      pick: 0.19
      fit: 0.21
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.68
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.5
      efficiency: 0.5
      win: 0.68
      pick: 0.0
      fit: 0.13
    Rod of Tahuti:
      total: 0.79
      efficiency: 0.82
      win: 1.0
      pick: 0.15
      fit: 0.32
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.68
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Tyrfing
  - Nimble Ring
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Tyrfing, Jotunn''s Revenge, Soul Gem,
    Gluttonous Grimoire, Golden Blade, Breastplate of Valor, Shield Splitter, Shield
    of the Phoenix, Spear of Desolation, Oni Hunter''s Garb, Lotus Sickle, Runeforged
    Hammer, Hydra''s Lament, Draconic Scale, Bragi''s Harp, Blood-Bound Book, Shogun''s
    Ofuda, Pharaoh''s Curse, Screeching Gargoyle, Eros'' Bow, Helm of Radiance, Toxic
    Blade, Erosion, The Reaper, Eye of Providence, Midgardian Mail, Ancient Signet,
    Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch Bow, Stone of Binding,
    Death Metal, Bracer of The Abyss.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.73
      pick: 0.19
      fit: 0.21
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.2
      fit: 0.41
    Tyrfing:
      total: 0.57
      efficiency: 0.53
      win: 0.68
      pick: 0.0
      fit: 0.52
    Nimble Ring:
      total: 0.6
      efficiency: 0.57
      win: 0.78
      pick: 0.17
      fit: 0.32
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.82
      win: 1.0
      pick: 0.15
      fit: 0.1
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.68
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Nimble Ring
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Soul Gem, Jotunn''s
    Revenge, Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix, Spear of
    Desolation, Lotus Sickle, Hydra''s Lament, Gluttonous Grimoire, Screeching Gargoyle,
    Shield Splitter, Chronos'' Pendant, Gladiator''s Shield, Oni Hunter''s Garb, Draconic
    Scale, Arondight, Blood-Bound Book, Tyrfing, Prophetic Cloak, Runeforged Hammer,
    Helm of Radiance, Erosion, Eye of Providence, Gem of Focus, Heartwood Charm, Midgardian
    Mail, Chandra''s Grace, Golden Blade, Ancient Signet, Helm of Darkness, The Reaper,
    Stone of Binding, Leviathan''s Hide, Regrowth Striders, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.73
      pick: 0.19
      fit: 0.41
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.63
      win: 0.68
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.68
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.68
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.82
      win: 1.0
      pick: 0.15
      fit: 0.12
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.68
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shield
    Splitter, Soul Gem, Gluttonous Grimoire, Breastplate of Valor, Shield of the Phoenix,
    Tyrfing, Runeforged Hammer, Hydra''s Lament, Draconic Scale, Golden Blade, Oni
    Hunter''s Garb, Spear of Desolation, Lotus Sickle, The Reaper, Erosion, Eye of
    Providence, Screeching Gargoyle, Blood-Bound Book, Helm of Radiance, Death Metal,
    Midgardian Mail, Helm of Darkness, Stone of Binding, Leviathan''s Hide, Bragi''s
    Harp, Hide of the Nemean Lion, Arondight, Ancient Signet, Magi''s Cloak, Mantle
    Of Discord, Chronos'' Pendant, Avenging Blade, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.71
      win: 0.73
      pick: 0.19
      fit: 0.26
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.2
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.68
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.68
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.33
      fit: 0.41
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.68
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
---
