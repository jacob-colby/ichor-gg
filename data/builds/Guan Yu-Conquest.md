---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.1
  aspect_win_rate: 1.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.22
    win_rate: 0.69
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.14
      win_rate: 0.38
    - name: Necronomicon
      pick_rate: 0.14
      win_rate: 0.38
  - name: Berserker's Shield
    pick_rate: 0.17
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.6
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.75
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.75
    - name: Nimble Ring
      pick_rate: 0.11
      win_rate: 0.5
  - name: Brawler’s Beat Stick
    pick_rate: 0.13
    win_rate: 0.43
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.22
    - name: Nimble Ring
      pick_rate: 0.11
      win_rate: 0.83
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.1
      win_rate: 0.8
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.75
  - name: Stalwart Sigil
    pick_rate: 0.11
    win_rate: 0.0
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.11
      win_rate: 0.33
    - name: Mote of Chaos
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.24
    win_rate: 0.64
  - name: Sands Of Time
    pick_rate: 0.24
    win_rate: 0.43
  - name: Leather Cowl
    pick_rate: 0.15
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-11-06'
  god_win_rate: 0.5932203389830508
  god_matches_won: 35
  god_matches_played: 59
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shield Splitter,
    Soul Gem, Gluttonous Grimoire, Breastplate of Valor, Shield of the Phoenix, Tyrfing,
    Runeforged Hammer, Hydra''s Lament, Draconic Scale, Golden Blade, Oni Hunter''s
    Garb, Spear of Desolation, Lotus Sickle, The Reaper, Erosion, Eye of Providence,
    Screeching Gargoyle, Blood-Bound Book, Helm of Radiance, Death Metal, Midgardian
    Mail, Helm of Darkness, Stone of Binding, Leviathan''s Hide, Bragi''s Harp, Arondight,
    Ancient Signet, Magi''s Cloak, Mantle Of Discord, Chronos'' Pendant, Avenging
    Blade, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.71
      win: 0.75
      pick: 0.22
      fit: 0.26
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.23
      fit: 0.36
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.33
      fit: 0.41
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.82
      win: 1.0
      pick: 0.22
      fit: 0.12
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Rod of Tahuti
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
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
      total: 0.64
      efficiency: 0.71
      win: 0.75
      pick: 0.22
      fit: 0.25
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.23
      fit: 0.37
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.82
      win: 1.0
      pick: 0.22
      fit: 0.12
    Amanita Charm:
      total: 0.65
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.61
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire, Amanita Charm,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Stone of Binding, The
    Reaper, Avenging Blade, Shield Splitter, Void Stone, Void Shield, Breastplate
    of Valor, The Crusher, Obsidian Shard, Heartseeker, Shield of the Phoenix, Spear
    of the Magus, Tyrfing, Runeforged Hammer, Hydra''s Lament, Titan''s Bane, Oni
    Hunter''s Garb, Tekko-Kagi, Lotus Sickle, Dreamer''s Idol, Draconic Scale, Toxic
    Blade, Blood-Bound Book, Golden Blade, Helm of Radiance, Erosion, Silverbranch
    Bow, Death Metal, Eye of Providence, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.48
      win: 0.67
      pick: 0.0
      fit: 0.07
    Genji's Guard:
      total: 0.63
      efficiency: 0.71
      win: 0.75
      pick: 0.22
      fit: 0.21
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.5
      efficiency: 0.5
      win: 0.67
      pick: 0.0
      fit: 0.13
    Nimble Ring:
      total: 0.61
      efficiency: 0.57
      win: 0.83
      pick: 0.18
      fit: 0.19
    Rod of Tahuti:
      total: 0.79
      efficiency: 0.82
      win: 1.0
      pick: 0.22
      fit: 0.32
  community_ordered:
  - Genji's Guard
  - Nimble Ring
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
  - Amanita Charm
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
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
      total: 0.63
      efficiency: 0.71
      win: 0.75
      pick: 0.22
      fit: 0.21
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.23
      fit: 0.41
    Tyrfing:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.52
    Nimble Ring:
      total: 0.63
      efficiency: 0.57
      win: 0.83
      pick: 0.18
      fit: 0.32
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.82
      win: 1.0
      pick: 0.22
      fit: 0.1
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.67
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
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Soul Gem, Jotunn''s
    Revenge, Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix, Spear of
    Desolation, Lotus Sickle, Hydra''s Lament, Gluttonous Grimoire, Screeching Gargoyle,
    Shield Splitter, Chronos'' Pendant, Gladiator''s Shield, Oni Hunter''s Garb, Draconic
    Scale, Arondight, Blood-Bound Book, Tyrfing, Prophetic Cloak, Runeforged Hammer,
    Helm of Radiance, Erosion, Eye of Providence, Gem of Focus, Heartwood Charm, Midgardian
    Mail, Chandra''s Grace, Golden Blade, Ancient Signet, Helm of Darkness, The Reaper,
    Stone of Binding, Leviathan''s Hide, Regrowth Striders.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.48
      win: 0.67
      pick: 0.0
      fit: 0.08
    Genji's Guard:
      total: 0.66
      efficiency: 0.71
      win: 0.75
      pick: 0.22
      fit: 0.41
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.33
      fit: 0.54
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.82
      win: 1.0
      pick: 0.22
      fit: 0.12
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
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
    Harp, Arondight, Ancient Signet, Magi''s Cloak, Mantle Of Discord, Chronos'' Pendant,
    Avenging Blade, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.71
      win: 0.75
      pick: 0.22
      fit: 0.26
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.23
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.33
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.33
      fit: 0.41
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
---
