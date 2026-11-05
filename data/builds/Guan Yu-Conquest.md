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
    Cuirass, Gluttonous Grimoire, Soul Gem, Breastplate of Valor, Nimble Ring, Runeforged
    Hammer, Golden Blade, Hydra''s Lament, Lotus Sickle, Spear of Desolation, Helm
    of Radiance, Oni Hunter''s Garb, Shield of the Phoenix, Erosion, The Reaper, Tyrfing,
    Eye of Providence, Helm of Darkness, Tekko-Kagi, Obsidian Shard, Titan''s Bane,
    Screeching Gargoyle, Stone of Binding, Midgardian Mail, Avenging Blade, Blood-Bound
    Book, Arondight, Lernaean Bow, Magi''s Cloak, Pharaoh''s Curse, Leviathan''s Hide,
    Death Metal, Eros'' Bow, Mantle Of Discord, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
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
      efficiency: 0.67
      win: 0.6
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
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
  - Kinetic Cuirass
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Chandra''s Grace, Shield of
    the Phoenix, The Reaper, Jotunn''s Revenge, Blood-Bound Book, Gluttonous Grimoire,
    Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Ethereal Staff, Nimble Ring,
    Golden Blade, Yogi''s Necklace, Breastplate of Valor, Phoenix Feather, Bloodforge,
    Hydra''s Lament, Riptalon, Bancroft''s Talon, Oni Hunter''s Garb, Lotus Sickle,
    Spear of Desolation, Rod of Asclepius, Erosion, Regrowth Striders, Helm of Radiance,
    Tyrfing, Eye of Providence, Sphere of Negation, Avenging Blade, Tekko-Kagi, Obsidian
    Shard, Midgardian Mail, Soul Locket, Titan''s Bane, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
      win: 0.67
      pick: 0.16
      fit: 0.37
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.6
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.58
      efficiency: 0.57
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
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Screeching Gargoyle
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, Soul Gem,
    Amanita Charm, Screeching Gargoyle, Stone of Binding, Spear of Desolation, Avenging
    Blade, Obsidian Shard, The Reaper, Titan''s Bane, Tekko-Kagi, Shield Splitter,
    Kinetic Cuirass, Void Stone, Void Shield, Breastplate of Valor, Nimble Ring, Spear
    of the Magus, Runeforged Hammer, The Crusher, Hydra''s Lament, Toxic Blade, Heartseeker,
    Silverbranch Bow, Golden Blade, Lotus Sickle, Helm of Radiance, Doom Orb, Oni
    Hunter''s Garb, The World Stone, Tyrfing, Riptalon, Shield of the Phoenix, Erosion,
    Blood-Bound Book, Helm of Darkness, Eye of Providence.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.61
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.63
    Berserker's Shield:
      total: 0.61
      efficiency: 0.74
      win: 0.67
      pick: 0.16
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.6
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.32
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
    Lotus Sickle, Pharaoh''s Curse, Lernaean Bow, Helm of Radiance, Spear of Desolation,
    Toxic Blade, Oni Hunter''s Garb, Silverbranch Bow, Obsidian Shard, Shogun''s Ofuda,
    Shield of the Phoenix, Erosion, Screeching Gargoyle, Helm of Darkness, Blood-Bound
    Book, Eye of Providence, The Reaper, Midgardian Mail, Stone of Binding, Bragi''s
    Harp, Titan''s Bane, Riptalon, Ancient Signet, Draconic Scale.'
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
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Spear of Desolation
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Lotus Sickle
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
    Soul Gem, Amanita Charm, Breastplate of Valor, Lotus Sickle, Spear of Desolation,
    Gluttonous Grimoire, Kinetic Cuirass, Hydra''s Lament, Shield of the Phoenix,
    Shield Splitter, Screeching Gargoyle, Nimble Ring, Chronos'' Pendant, Arondight,
    Runeforged Hammer, Helm of Radiance, Oni Hunter''s Garb, Obsidian Shard, Prophetic
    Cloak, Golden Blade, Erosion, Helm of Darkness, Eye of Providence, Gem of Focus,
    Blood-Bound Book, Midgardian Mail, Heartwood Charm, Stone of Binding, Gladiator''s
    Shield, Magi''s Cloak, The Reaper, Eros'' Bow, Ancient Signet, Leviathan''s Hide,
    Tyrfing, Pharaoh''s Curse, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
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
      efficiency: 0.67
      win: 0.6
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.4
    Lotus Sickle:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.58
  community_ordered:
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
    Splitter, Kinetic Cuirass, Gluttonous Grimoire, Soul Gem, Breastplate of Valor,
    Nimble Ring, Runeforged Hammer, Golden Blade, Hydra''s Lament, Lotus Sickle, Spear
    of Desolation, Helm of Radiance, Oni Hunter''s Garb, Shield of the Phoenix, Erosion,
    The Reaper, Tyrfing, Eye of Providence, Helm of Darkness, Tekko-Kagi, Obsidian
    Shard, Draconic Scale, Titan''s Bane, Screeching Gargoyle, Stone of Binding, Midgardian
    Mail, Avenging Blade, Blood-Bound Book, Arondight, Lernaean Bow, Magi''s Cloak,
    Pharaoh''s Curse, Leviathan''s Hide, Death Metal, Eros'' Bow, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
      win: 0.67
      pick: 0.16
      fit: 0.36
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.45
      pick: 0.15
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.6
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Genji's Guard
  starter: *id001
---
