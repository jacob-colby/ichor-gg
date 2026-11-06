---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.0
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.59
    win_rate: 0.59
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.73
    - name: Shogun's Ofuda
      pick_rate: 0.07
      win_rate: 0.5
  - name: Berserker's Shield
    pick_rate: 0.33
    win_rate: 0.6
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.17
      win_rate: 0.5
    - name: Golden Blade
      pick_rate: 0.14
      win_rate: 0.85
  - name: Kinetic Cuirass
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.27
      win_rate: 0.38
    - name: Shogun's Ofuda
      pick_rate: 0.1
      win_rate: 0.67
  - name: Shogun's Ofuda
    pick_rate: 0.11
    win_rate: 0.6
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.36
      win_rate: 0.53
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.75
  - name: Hussar's Wings
    pick_rate: 0.1
    win_rate: 0.75
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.75
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.86
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.25
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.83
    - name: Hussar's Wings
      pick_rate: 0.07
      win_rate: 0.5
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.39
    win_rate: 0.58
  - name: Hunter's Cowl
    pick_rate: 0.36
    win_rate: 0.52
  - name: Death's Toll
    pick_rate: 0.13
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-11-06'
  god_win_rate: 0.5543478260869565
  god_matches_won: 51
  god_matches_played: 92
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
  - Golden Blade
  - Genji's Guard
  - Freya's Tears
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Shield Splitter, Jotunn''s Revenge, Draconic
    Scale, Shield of the Phoenix, Breastplate of Valor, Runeforged Hammer, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Hydra''s Lament, The Reaper, Midgardian
    Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s Hide, Magi''s Cloak,
    Mantle Of Discord, Hide of the Nemean Lion, Wyrmskin Hide, Tyrfing, Avenging Blade,
    Ancile, Arondight, The Crusher.'
  slot_scores:
    Golden Blade:
      total: 0.62
      efficiency: 0.44
      win: 0.85
      pick: 0.19
      fit: 0.45
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.63
      pick: 0.0
      fit: 0.29
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.75
      pick: 0.22
      fit: 0.48
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.61
      win: 0.63
      pick: 0.28
      fit: 0.64
    Shifter's Shield:
      total: 0.6
      efficiency: 0.5
      win: 0.75
      pick: 0.15
      fit: 0.54
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Golden Blade
  - Freya's Tears
  - Kinetic Cuirass
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Shield of the Phoenix
  - Freya's Tears
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    this god: Amanita Charm, Shield of the Phoenix, The Reaper, Genji''s Guard, Jotunn''s
    Revenge, Shield Splitter, Phoenix Feather, Yogi''s Necklace, Runeforged Hammer,
    Draconic Scale, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s Garb, Erosion,
    Hydra''s Lament, Eye of Providence, Bloodforge, Midgardian Mail, Regrowth Striders,
    Leviathan''s Hide, Avenging Blade, Glorious Pridwen, Wyrmskin Hide, Hide of the
    Nemean Lion, Screeching Gargoyle, Tyrfing.'
  slot_scores:
    Golden Blade:
      total: 0.62
      efficiency: 0.44
      win: 0.85
      pick: 0.19
      fit: 0.51
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.22
      fit: 0.42
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.28
      fit: 0.62
    Shifter's Shield:
      total: 0.6
      efficiency: 0.5
      win: 0.75
      pick: 0.15
      fit: 0.52
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Golden Blade
  - Freya's Tears
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Screeching Gargoyle,
    The Reaper, Stone of Binding, Shield Splitter, Avenging Blade, Void Stone, The
    Crusher, Void Shield, Heartseeker, Breastplate of Valor, Titan''s Bane, Shield
    of the Phoenix, Runeforged Hammer, Draconic Scale, Oni Hunter''s Garb, Hydra''s
    Lament, Erosion, Eye of Providence, Midgardian Mail, Leviathan''s Hide, Avatar''s
    Parashu, Magi''s Cloak, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.44
      win: 0.85
      pick: 0.19
      fit: 0.34
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.22
      fit: 0.36
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.28
      fit: 0.5
    Shifter's Shield:
      total: 0.58
      efficiency: 0.5
      win: 0.75
      pick: 0.15
      fit: 0.4
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Golden Blade
  - Freya's Tears
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Tyrfing, Jotunn''s Revenge, Shield Splitter,
    Breastplate of Valor, Shield of the Phoenix, Oni Hunter''s Garb, Draconic Scale,
    Runeforged Hammer, Pharaoh''s Curse, Erosion, Eye of Providence, Hydra''s Lament,
    Toxic Blade, Screeching Gargoyle, Midgardian Mail, The Reaper, Stone of Binding,
    Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch Bow, Magi''s Cloak.'
  slot_scores:
    Golden Blade:
      total: 0.65
      efficiency: 0.51
      win: 0.85
      pick: 0.19
      fit: 0.56
    Berserker's Shield:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.45
      fit: 0.45
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.55
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.28
      fit: 0.48
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.75
      pick: 0.22
      fit: 0.34
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Amanita Charm, Jotunn''s
    Revenge, Breastplate of Valor, Shield of the Phoenix, Screeching Gargoyle, Hydra''s
    Lament, Shield Splitter, Gladiator''s Shield, Draconic Scale, Oni Hunter''s Garb,
    Prophetic Cloak, Arondight, Erosion, Eye of Providence, Runeforged Hammer, Midgardian
    Mail, Stone of Binding, Chandra''s Grace, Leviathan''s Hide, Regrowth Striders,
    The Reaper, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean Lion, Eye of
    Erebus.'
  slot_scores:
    Golden Blade:
      total: 0.59
      efficiency: 0.44
      win: 0.85
      pick: 0.19
      fit: 0.27
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.63
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.28
      fit: 0.51
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.22
      fit: 0.59
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Golden Blade
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Shield Splitter
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
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
    Underrated for this god: Amanita Charm, Genji''s Guard, Shield Splitter, Jotunn''s
    Revenge, Draconic Scale, Shield of the Phoenix, Breastplate of Valor, Runeforged
    Hammer, Erosion, Oni Hunter''s Garb, Eye of Providence, Hydra''s Lament, The Reaper,
    Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s Hide, Magi''s
    Cloak, Mantle Of Discord, Hide of the Nemean Lion, Wyrmskin Hide, Tyrfing, Avenging
    Blade, Ancile, Arondight, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.63
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.36
    Shield Splitter:
      total: 0.58
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.6
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.61
      win: 0.63
      pick: 0.28
      fit: 0.64
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.75
      pick: 0.22
      fit: 0.48
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
