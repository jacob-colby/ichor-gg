---
type: smite-build
god: Odin
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.53
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.53
    - name: Devourer's Gauntlet
      pick_rate: 0.07
      win_rate: 0.44
  - name: Breastplate of Valor
    pick_rate: 0.25
    win_rate: 0.64
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.16
      win_rate: 0.64
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.63
    alternates:
    - name: Transcendence
      pick_rate: 0.12
      win_rate: 0.64
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.7
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.52
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.69
  - name: Brawler’s Beat Stick
    pick_rate: 0.08
    win_rate: 0.62
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.76
    - name: Heartseeker
      pick_rate: 0.05
      win_rate: 0.63
  - name: Sage's Ring
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 0.7
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.7
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.29
    win_rate: 0.66
  - name: Bumba's Cudgel
    pick_rate: 0.18
    win_rate: 0.42
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/odin/
  last_verified: '2026-11-03'
  god_win_rate: 0.5702917771883289
  god_matches_won: 215
  god_matches_played: 377
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield Splitter, Berserker''s Shield, Runeforged Hammer,
    The Reaper, Titan''s Bane, Erosion, Eye of Providence, Oni Hunter''s Garb, Draconic
    Scale, Shield of the Phoenix, Stone of Binding, Midgardian Mail, Magi''s Cloak,
    The Crusher, Avenging Blade, Mantle Of Discord, Screeching Gargoyle, Leviathan''s
    Hide, Wyrmskin Hide, Arondight, Ancile, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.53
      fit: 0.42
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.63
      pick: 0.26
      fit: 0.27
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.7
      pick: 0.15
      fit: 0.59
    Shield Splitter:
      total: 0.57
      efficiency: 0.59
      win: 0.64
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.59
      efficiency: 0.58
      win: 0.7
      pick: 0.2
      fit: 0.44
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Transcendence
  - Freya's Tears
  flex_slots:
  - Breastplate of Valor
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Shield Splitter, Berserker''s Shield, Runeforged Hammer, The Reaper, Titan''s
    Bane, Oni Hunter''s Garb, The Crusher, Erosion, Avenging Blade, Eye of Providence,
    Shield of the Phoenix, Stone of Binding, Arondight, Screeching Gargoyle, Midgardian
    Mail, Draconic Scale, Magi''s Cloak, Leviathan''s Hide, Mantle Of Discord, Wyrmskin
    Hide, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.53
      fit: 0.43
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.64
      pick: 0.34
      fit: 0.27
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.63
      pick: 0.26
      fit: 0.27
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.7
      pick: 0.15
      fit: 0.44
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.64
      pick: 0.19
      fit: 0.23
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.7
      pick: 0.2
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Transcendence
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Shield of the Phoenix, Berserker''s Shield,
    Shield Splitter, Runeforged Hammer, Phoenix Feather, Yogi''s Necklace, Bloodforge,
    Titan''s Bane, Oni Hunter''s Garb, Chandra''s Grace, Erosion, Eye of Providence,
    Avenging Blade, Draconic Scale, Midgardian Mail, Regrowth Striders, The Crusher,
    Leviathan''s Hide, Glorious Pridwen, Stone of Binding, Wyrmskin Hide, Shifter''s
    Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.53
      fit: 0.44
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.26
      fit: 0.24
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.7
      pick: 0.15
      fit: 0.57
    Freya's Tears:
      total: 0.59
      efficiency: 0.58
      win: 0.7
      pick: 0.2
      fit: 0.39
    The Reaper:
      total: 0.59
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Transcendence
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, The Reaper, Avenging Blade, Screeching
    Gargoyle, Shield Splitter, Berserker''s Shield, Titan''s Bane, Void Stone, Void
    Shield, The Crusher, Runeforged Hammer, Oni Hunter''s Garb, Erosion, Eye of Providence,
    Draconic Scale, Tekko-Kagi, Shield of the Phoenix, Midgardian Mail, Magi''s Cloak,
    Mantle Of Discord, Leviathan''s Hide, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.67
      win: 0.57
      pick: 0.53
      fit: 0.52
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.26
      fit: 0.22
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.7
      pick: 0.15
      fit: 0.5
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.64
      pick: 0.19
      fit: 0.16
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.7
      pick: 0.2
      fit: 0.37
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Transcendence
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Golden Blade, Shield Splitter, Tekko-Kagi,
    Tyrfing, Toxic Blade, Silverbranch Bow, Runeforged Hammer, Pharaoh''s Curse, Lernaean
    Bow, The Reaper, Oni Hunter''s Garb, Titan''s Bane, Shogun''s Ofuda, Riptalon,
    Erosion, Eye of Providence, Stone of Binding, Midgardian Mail, Draconic Scale,
    Shield of the Phoenix, Magi''s Cloak, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.61
      efficiency: 0.74
      win: 0.64
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.7
      pick: 0.15
      fit: 0.45
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.7
      pick: 0.2
      fit: 0.32
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.55
      win: 0.64
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Berserker''s Shield,
    Shield of the Phoenix, Shield Splitter, Screeching Gargoyle, Arondight, Runeforged
    Hammer, Oni Hunter''s Garb, Prophetic Cloak, The Reaper, Erosion, Eye of Providence,
    Titan''s Bane, Stone of Binding, Draconic Scale, Midgardian Mail, Magi''s Cloak,
    Gladiator''s Shield, Leviathan''s Hide, Mantle Of Discord, Regrowth Striders,
    Chandra''s Grace, Eye of Erebus, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.57
      pick: 0.53
      fit: 0.46
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.63
      win: 0.64
      pick: 0.34
      fit: 0.41
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.63
      pick: 0.26
      fit: 0.41
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.7
      pick: 0.15
      fit: 0.48
    Freya's Tears:
      total: 0.61
      efficiency: 0.58
      win: 0.7
      pick: 0.2
      fit: 0.55
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Berserker's Shield
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
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
    Underrated for this god: Amanita Charm, Shield Splitter, Berserker''s Shield,
    Runeforged Hammer, The Reaper, Titan''s Bane, Erosion, Eye of Providence, Oni
    Hunter''s Garb, Draconic Scale, Shield of the Phoenix, Stone of Binding, Midgardian
    Mail, Magi''s Cloak, Shifter''s Shield, The Crusher, Avenging Blade, Mantle Of
    Discord, Screeching Gargoyle, Leviathan''s Hide, Wyrmskin Hide, Arondight, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.53
      fit: 0.42
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.64
      pick: 0.0
      fit: 0.31
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.63
      pick: 0.26
      fit: 0.27
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.7
      pick: 0.15
      fit: 0.59
    Shield Splitter:
      total: 0.57
      efficiency: 0.59
      win: 0.64
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
---
