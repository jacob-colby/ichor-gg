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
      pick_rate: 0.1
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
      pick_rate: 0.13
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
      win_rate: 0.54
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
  - name: Hunter's Cowl
    pick_rate: 0.15
    win_rate: 0.59
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.6
  - name: Bluestone Pendant
    pick_rate: 0.12
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-11-04'
  god_win_rate: 0.5359116022099447
  god_matches_won: 97
  god_matches_played: 181
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
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
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shield
    Splitter, Soul Gem, Gluttonous Grimoire, Breastplate of Valor, Shield of the Phoenix,
    Tyrfing, Runeforged Hammer, Hydra''s Lament, Golden Blade, Oni Hunter''s Garb,
    Spear of Desolation, Lotus Sickle, The Reaper, Erosion, Eye of Providence, Screeching
    Gargoyle, Blood-Bound Book, Shifter''s Shield, Draconic Scale, Helm of Radiance,
    Death Metal, Midgardian Mail, Nimble Ring, Helm of Darkness, Stone of Binding,
    Leviathan''s Hide, Bragi''s Harp, Arondight, Ancient Signet, Magi''s Cloak, Mantle
    Of Discord, Chronos'' Pendant, Avenging Blade, The Crusher.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.16
      fit: 0.36
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Rod of Tahuti, Chandra''s
    Grace, Kinetic Cuirass, The Reaper, Blood-Bound Book, Jotunn''s Revenge, Gluttonous
    Grimoire, Shield Splitter, Phoenix Feather, Yogi''s Necklace, Ethereal Staff,
    Breastplate of Valor, Runeforged Hammer, Tyrfing, Bancroft''s Talon, Golden Blade,
    Hydra''s Lament, Oni Hunter''s Garb, Spear of Desolation, Regrowth Striders, Riptalon,
    Lotus Sickle, Bloodforge, Rod of Asclepius, Erosion, Soul Locket, Eye of Providence,
    Shifter''s Shield, Midgardian Mail, Draconic Scale, Screeching Gargoyle, Glorious
    Pridwen, Death Metal, Nimble Ring, Helm of Radiance, Sphere of Negation.'
  slot_scores:
    Berserker's Shield:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.16
      fit: 0.37
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire,
    Amanita Charm, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Stone
    of Binding, The Reaper, Avenging Blade, Shield Splitter, Void Stone, Void Shield,
    Breastplate of Valor, The Crusher, Obsidian Shard, Heartseeker, Shield of the
    Phoenix, Spear of the Magus, Tyrfing, Runeforged Hammer, Hydra''s Lament, Titan''s
    Bane, Oni Hunter''s Garb, Tekko-Kagi, Lotus Sickle, Dreamer''s Idol, Toxic Blade,
    Blood-Bound Book, Golden Blade, Helm of Radiance, Erosion, Silverbranch Bow, Death
    Metal, Eye of Providence, Nimble Ring, Midgardian Mail, Draconic Scale.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.61
    Berserker's Shield:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.16
      fit: 0.28
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.6
      pick: 0.0
      fit: 0.32
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.58
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
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
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
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Tyrfing, Jotunn''s Revenge,
    Soul Gem, Gluttonous Grimoire, Golden Blade, Breastplate of Valor, Shield Splitter,
    Shield of the Phoenix, Nimble Ring, Spear of Desolation, Oni Hunter''s Garb, Lotus
    Sickle, Runeforged Hammer, Hydra''s Lament, Bragi''s Harp, Blood-Bound Book, Shogun''s
    Ofuda, Pharaoh''s Curse, Screeching Gargoyle, Eros'' Bow, Helm of Radiance, Toxic
    Blade, Erosion, The Reaper, Eye of Providence, Midgardian Mail, Ancient Signet,
    Lernaean Bow, Dominance, Shifter''s Shield, Draconic Scale, Leviathan''s Hide,
    Silverbranch Bow, Stone of Binding, Death Metal, Bracer of The Abyss.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.16
      fit: 0.41
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.23
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Jotunn''s Revenge, Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix,
    Chandra''s Grace, Spear of Desolation, Lotus Sickle, Hydra''s Lament, Gluttonous
    Grimoire, Screeching Gargoyle, Shield Splitter, Chronos'' Pendant, Gladiator''s
    Shield, Oni Hunter''s Garb, Arondight, Blood-Bound Book, Tyrfing, Prophetic Cloak,
    Runeforged Hammer, Helm of Radiance, Erosion, Eye of Providence, Gem of Focus,
    Heartwood Charm, Nimble Ring, Midgardian Mail, Shifter''s Shield, Draconic Scale,
    Golden Blade, Ancient Signet, Helm of Darkness, The Reaper, Stone of Binding,
    Leviathan''s Hide, Regrowth Striders.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.16
      fit: 0.31
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.54
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.58
  community_ordered:
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Jotunn''s
    Revenge, Shield Splitter, Soul Gem, Gluttonous Grimoire, Breastplate of Valor,
    Shield of the Phoenix, Tyrfing, Runeforged Hammer, Hydra''s Lament, Draconic Scale,
    Golden Blade, Oni Hunter''s Garb, Spear of Desolation, Lotus Sickle, The Reaper,
    Erosion, Eye of Providence, Screeching Gargoyle, Blood-Bound Book, Shifter''s
    Shield, Helm of Radiance, Death Metal, Midgardian Mail, Nimble Ring, Helm of Darkness,
    Stone of Binding, Leviathan''s Hide, Bragi''s Harp, Arondight, Ancient Signet,
    Magi''s Cloak, Mantle Of Discord, Chronos'' Pendant, Avenging Blade, The Crusher.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.16
      fit: 0.36
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.45
      pick: 0.15
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.41
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
