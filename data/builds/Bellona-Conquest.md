---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.33
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.53
    win_rate: 0.56
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.16
      win_rate: 0.63
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.31
  - name: Berserker's Shield
    pick_rate: 0.31
    win_rate: 0.52
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.16
      win_rate: 0.57
    - name: Golden Blade
      pick_rate: 0.16
      win_rate: 0.68
  - name: Kinetic Cuirass
    pick_rate: 0.17
    win_rate: 0.62
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.22
      win_rate: 0.5
    - name: Vital Amplifier
      pick_rate: 0.11
      win_rate: 0.68
  - name: Shogun's Ofuda
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.26
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.79
  - name: Hussar's Wings
    pick_rate: 0.09
    win_rate: 0.77
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 0.81
    - name: Shogun's Ofuda
      pick_rate: 0.09
      win_rate: 0.79
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.29
    alternates:
    - name: Hussar's Wings
      pick_rate: 0.09
      win_rate: 0.6
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.36
    win_rate: 0.6
  - name: Hunter's Cowl
    pick_rate: 0.31
    win_rate: 0.57
  - name: Death's Toll
    pick_rate: 0.17
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-11-08'
  god_win_rate: 0.5549132947976878
  god_matches_won: 96
  god_matches_played: 173
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
  - Genji's Guard
  - Shield Splitter
  - Shifter's Shield
  - Kinetic Cuirass
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Hussar's Wings
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Shield Splitter, Freya''s Tears, Jotunn''s
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
    Shield Splitter:
      total: 0.58
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.6
    Shifter's Shield:
      total: 0.62
      efficiency: 0.5
      win: 0.79
      pick: 0.15
      fit: 0.54
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.26
      fit: 0.64
    Hussar's Wings:
      total: 0.57
      efficiency: 0.39
      win: 0.77
      pick: 0.19
      fit: 0.54
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Shifter's Shield
  - Kinetic Cuirass
  - Hussar's Wings
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Shield of the Phoenix
  - Shifter's Shield
  - Kinetic Cuirass
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Hussar's Wings
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, The Reaper, Genji''s Guard, Jotunn''s
    Revenge, Shield Splitter, Phoenix Feather, Freya''s Tears, Yogi''s Necklace, Runeforged
    Hammer, Draconic Scale, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s
    Garb, Erosion, Hydra''s Lament, Eye of Providence, Bloodforge, Midgardian Mail,
    Regrowth Striders, Leviathan''s Hide, Avenging Blade, Glorious Pridwen, Wyrmskin
    Hide, Hide of the Nemean Lion, Screeching Gargoyle, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.63
      pick: 0.0
      fit: 0.26
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.76
    Shifter's Shield:
      total: 0.62
      efficiency: 0.5
      win: 0.79
      pick: 0.15
      fit: 0.52
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.26
      fit: 0.62
    Hussar's Wings:
      total: 0.57
      efficiency: 0.39
      win: 0.77
      pick: 0.19
      fit: 0.52
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Shifter's Shield
  - Kinetic Cuirass
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    for this god: Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Screeching Gargoyle,
    The Reaper, Stone of Binding, Shield Splitter, Freya''s Tears, Avenging Blade,
    Void Stone, The Crusher, Void Shield, Heartseeker, Breastplate of Valor, Titan''s
    Bane, Shield of the Phoenix, Runeforged Hammer, Draconic Scale, Oni Hunter''s
    Garb, Hydra''s Lament, Erosion, Eye of Providence, Midgardian Mail, Leviathan''s
    Hide, Avatar''s Parashu, Magi''s Cloak, Mantle Of Discord.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.63
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.52
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.62
      pick: 0.26
      fit: 0.5
    Shifter's Shield:
      total: 0.6
      efficiency: 0.5
      win: 0.79
      pick: 0.15
      fit: 0.4
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.4
  community_ordered:
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Tyrfing, Freya''s Tears, Jotunn''s Revenge,
    Shield Splitter, Breastplate of Valor, Shield of the Phoenix, Oni Hunter''s Garb,
    Draconic Scale, Runeforged Hammer, Pharaoh''s Curse, Erosion, Eye of Providence,
    Hydra''s Lament, Toxic Blade, Screeching Gargoyle, Midgardian Mail, The Reaper,
    Stone of Binding, Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch Bow,
    Magi''s Cloak.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.51
      win: 0.68
      pick: 0.22
      fit: 0.56
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.52
      pick: 0.42
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
      win: 0.62
      pick: 0.26
      fit: 0.48
    Shifter's Shield:
      total: 0.59
      efficiency: 0.5
      win: 0.79
      pick: 0.15
      fit: 0.38
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
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Freya''s Tears, Amanita
    Charm, Jotunn''s Revenge, Breastplate of Valor, Shield of the Phoenix, Screeching
    Gargoyle, Hydra''s Lament, Shield Splitter, Gladiator''s Shield, Draconic Scale,
    Oni Hunter''s Garb, Prophetic Cloak, Arondight, Erosion, Eye of Providence, Runeforged
    Hammer, Midgardian Mail, Stone of Binding, Chandra''s Grace, Leviathan''s Hide,
    Regrowth Striders, The Reaper, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean
    Lion, Eye of Erebus.'
  slot_scores:
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
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.59
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.62
      pick: 0.26
      fit: 0.51
    Shifter's Shield:
      total: 0.6
      efficiency: 0.5
      win: 0.79
      pick: 0.15
      fit: 0.41
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
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
    Underrated for this god: Amanita Charm, Genji''s Guard, Shield Splitter, Freya''s
    Tears, Jotunn''s Revenge, Draconic Scale, Shield of the Phoenix, Breastplate of
    Valor, Runeforged Hammer, Erosion, Oni Hunter''s Garb, Eye of Providence, Hydra''s
    Lament, The Reaper, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s
    Hide, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean Lion, Wyrmskin Hide,
    Tyrfing, Avenging Blade, Ancile, Arondight, The Crusher.'
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
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.26
      fit: 0.64
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
