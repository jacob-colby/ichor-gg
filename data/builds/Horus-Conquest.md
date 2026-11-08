---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.5
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.38
    win_rate: 0.48
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.17
      win_rate: 0.6
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.55
  - name: Stampede
    pick_rate: 0.24
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.6
    - name: Stone of Binding
      pick_rate: 0.09
      win_rate: 0.74
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.57
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.56
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.51
  - name: Shell of Rebuke
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.47
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.81
  - name: Spectral Armor
    pick_rate: 0.05
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.53
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.67
  - name: Sage's Ring
    pick_rate: 0.15
    win_rate: 0.73
    alternates:
    - name: Veve Charm
      pick_rate: 0.14
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Selflessness
    pick_rate: 0.34
    win_rate: 0.53
  - name: Heroism
    pick_rate: 0.16
    win_rate: 0.63
  - name: War Flag
    pick_rate: 0.1
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-11-08'
  god_win_rate: 0.5247148288973384
  god_matches_won: 138
  god_matches_played: 263
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
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Stone of Binding, Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge,
    Shield Splitter, Berserker''s Shield, Shield of the Phoenix, Breastplate of Valor,
    Hydra''s Lament, Draconic Scale, Oni Hunter''s Garb, Erosion, The Reaper, Eye
    of Providence, Shifter''s Shield, Screeching Gargoyle, Midgardian Mail, Leviathan''s
    Hide, Arondight, Hide of the Nemean Lion, Wyrmskin Hide, Magi''s Cloak, Mantle
    Of Discord, Avenging Blade, Gladiator''s Shield, Tyrfing, The Crusher.'
  slot_scores:
    Stone of Binding:
      total: 0.58
      efficiency: 0.49
      win: 0.74
      pick: 0.12
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.25
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Stone of Binding
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, The Reaper, Jotunn''s
    Revenge, Berserker''s Shield, Shield Splitter, Phoenix Feather, Yogi''s Necklace,
    Breastplate of Valor, Chandra''s Grace, Hydra''s Lament, Draconic Scale, Oni Hunter''s
    Garb, Erosion, Bloodforge, Eye of Providence, Regrowth Striders, Shifter''s Shield,
    Glorious Pridwen, Midgardian Mail, Screeching Gargoyle, Leviathan''s Hide, Avenging
    Blade, Hide of the Nemean Lion, Wyrmskin Hide, Arondight.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.49
      win: 0.74
      pick: 0.12
      fit: 0.41
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.79
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.25
      fit: 0.45
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Stone of Binding
  - Freya's Tears
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
  - Screeching Gargoyle
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Stone of Binding, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Screeching Gargoyle, The Reaper, Berserker''s Shield, Avenging Blade, Shield Splitter,
    Void Stone, The Crusher, Void Shield, Breastplate of Valor, Heartseeker, Shield
    of the Phoenix, Titan''s Bane, Hydra''s Lament, Oni Hunter''s Garb, Draconic Scale,
    Erosion, Eye of Providence, Shifter''s Shield, Midgardian Mail, Avatar''s Parashu,
    Leviathan''s Hide, Arondight, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.63
    Stone of Binding:
      total: 0.61
      efficiency: 0.49
      win: 0.74
      pick: 0.12
      fit: 0.66
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.55
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.25
      fit: 0.36
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Stone of Binding
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Stone of Binding
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Stone of Binding, Amanita Charm, Kinetic Cuirass,
    Tyrfing, Jotunn''s Revenge, Golden Blade, Shield Splitter, Breastplate of Valor,
    Shield of the Phoenix, Oni Hunter''s Garb, Draconic Scale, Hydra''s Lament, Shogun''s
    Ofuda, Pharaoh''s Curse, Toxic Blade, Screeching Gargoyle, Erosion, Eye of Providence,
    The Reaper, Midgardian Mail, Lernaean Bow, Shifter''s Shield, Dominance, Silverbranch
    Bow, Leviathan''s Hide, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.56
    Stone of Binding:
      total: 0.56
      efficiency: 0.49
      win: 0.74
      pick: 0.12
      fit: 0.34
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Stone of Binding
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Stone of Binding, Amanita Charm, Jotunn''s
    Revenge, Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Hydra''s Lament, Screeching Gargoyle, Shield Splitter, Gladiator''s Shield,
    Oni Hunter''s Garb, Draconic Scale, Arondight, Prophetic Cloak, Erosion, Eye of
    Providence, Chandra''s Grace, Shifter''s Shield, Midgardian Mail, The Reaper,
    Regrowth Striders, Leviathan''s Hide, Eye of Erebus, Hide of the Nemean Lion,
    Magi''s Cloak, Mantle Of Discord.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.49
      win: 0.74
      pick: 0.12
      fit: 0.37
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.51
      pick: 0.22
      fit: 0.44
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.25
      fit: 0.58
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Stone of Binding
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shield
    Splitter, Berserker''s Shield, Shield of the Phoenix, Breastplate of Valor, Hydra''s
    Lament, Draconic Scale, Oni Hunter''s Garb, Erosion, The Reaper, Eye of Providence,
    Shifter''s Shield, Screeching Gargoyle, Midgardian Mail, Stone of Binding, Leviathan''s
    Hide, Arondight, Hide of the Nemean Lion, Wyrmskin Hide, Magi''s Cloak, Mantle
    Of Discord, Avenging Blade, Gladiator''s Shield, Tyrfing, The Crusher.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.51
      pick: 0.22
      fit: 0.31
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.25
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-10-20'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of the Falcon
    status: below minimum
    matches_by_window:
      ob47: 1
      ob46: 9
---
