---
type: smite-build
god: Hua Mulan
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.21
    win_rate: 0.35
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.21
      win_rate: 0.55
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.53
  - name: Brawler’s Beat Stick
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.62
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.27
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.42
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.33
    - name: Brawler’s Beat Stick
      pick_rate: 0.12
      win_rate: 0.55
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.38
    alternates:
    - name: Freya's Tears
      pick_rate: 0.18
      win_rate: 0.35
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.29
  - name: Genji's Guard
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.63
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.29
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.2
    alternates:
    - name: Medal of Defense
      pick_rate: 0.1
      win_rate: 0.4
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.42
    win_rate: 0.51
  - name: Bluestone Pendant
    pick_rate: 0.25
    win_rate: 0.46
  - name: Warrior's Axe
    pick_rate: 0.12
    win_rate: 0.17
  source_url: https://smitebrain.com/gods/hua-mulan/
  last_verified: '2026-11-08'
  god_win_rate: 0.4742268041237113
  god_matches_won: 46
  god_matches_played: 97
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
  - Berserker's Shield
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Jotunn''s Revenge, Breastplate of Valor, Shield of the Phoenix, Tyrfing, Oni Hunter''s
    Garb, Erosion, Golden Blade, Eye of Providence, Hydra''s Lament, The Reaper, Midgardian
    Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s Hide, Magi''s Cloak,
    Mantle Of Discord, Wyrmskin Hide, Shogun''s Ofuda, Avenging Blade, Pharaoh''s
    Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.72
      win: 0.41
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.67
      pick: 0.15
      fit: 0.27
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.41
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.42
      pick: 0.2
      fit: 0.44
    Draconic Scale:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.25
      fit: 0.49
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    The Reaper, Jotunn''s Revenge, Shield Splitter, Phoenix Feather, Yogi''s Necklace,
    Golden Blade, Tyrfing, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s Garb,
    Hydra''s Lament, Bloodforge, Erosion, Eye of Providence, Riptalon, Regrowth Striders,
    Midgardian Mail, Leviathan''s Hide, Avenging Blade, Glorious Pridwen.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.72
      win: 0.41
      pick: 0.0
      fit: 0.42
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.67
      pick: 0.15
      fit: 0.24
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.61
      win: 0.41
      pick: 0.0
      fit: 0.57
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.57
      win: 0.41
      pick: 0.0
      fit: 0.72
    Draconic Scale:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.25
      fit: 0.47
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Screeching Gargoyle, Stone of Binding, The Reaper, Shield Splitter, Avenging Blade,
    Void Stone, Void Shield, The Crusher, Breastplate of Valor, Heartseeker, Shield
    of the Phoenix, Titan''s Bane, Tekko-Kagi, Tyrfing, Oni Hunter''s Garb, Hydra''s
    Lament, Toxic Blade, Erosion, Golden Blade, Eye of Providence, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.72
      win: 0.41
      pick: 0.0
      fit: 0.31
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.67
      pick: 0.15
      fit: 0.2
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.41
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.61
      win: 0.41
      pick: 0.0
      fit: 0.47
    Draconic Scale:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.25
      fit: 0.37
    Amanita Charm:
      total: 0.48
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Tyrfing
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Tyrfing, Jotunn''s
    Revenge, Golden Blade, Shield Splitter, Breastplate of Valor, Shield of the Phoenix,
    Oni Hunter''s Garb, Shogun''s Ofuda, Pharaoh''s Curse, Erosion, Eye of Providence,
    Hydra''s Lament, Toxic Blade, Screeching Gargoyle, Midgardian Mail, The Reaper,
    Stone of Binding, Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch Bow,
    Magi''s Cloak.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.51
      win: 0.41
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.67
      pick: 0.15
      fit: 0.21
    Berserker's Shield:
      total: 0.5
      efficiency: 0.72
      win: 0.41
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.45
      efficiency: 0.53
      win: 0.41
      pick: 0.0
      fit: 0.55
    Draconic Scale:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.25
      fit: 0.38
    Amanita Charm:
      total: 0.48
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Amanita Charm,
    Jotunn''s Revenge, Kinetic Cuirass, Breastplate of Valor, Shield of the Phoenix,
    Screeching Gargoyle, Hydra''s Lament, Shield Splitter, Oni Hunter''s Garb, Gladiator''s
    Shield, Prophetic Cloak, Arondight, Erosion, Eye of Providence, Tyrfing, Midgardian
    Mail, Stone of Binding, Chandra''s Grace, Leviathan''s Hide, The Reaper, Magi''s
    Cloak, Mantle Of Discord, Golden Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.72
      win: 0.41
      pick: 0.0
      fit: 0.32
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.67
      pick: 0.15
      fit: 0.41
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.65
      win: 0.41
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.42
      pick: 0.2
      fit: 0.55
    Draconic Scale:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.25
      fit: 0.39
    Amanita Charm:
      total: 0.48
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Shield Splitter, Jotunn''s Revenge, Breastplate of Valor, Shield of the Phoenix,
    Tyrfing, Oni Hunter''s Garb, Erosion, Golden Blade, Eye of Providence, Hydra''s
    Lament, The Reaper, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s
    Hide, Magi''s Cloak, Mantle Of Discord, Wyrmskin Hide, Shogun''s Ofuda, Avenging
    Blade, Pharaoh''s Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.72
      win: 0.41
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.67
      pick: 0.15
      fit: 0.27
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.41
      pick: 0.0
      fit: 0.59
    Shield Splitter:
      total: 0.47
      efficiency: 0.58
      win: 0.41
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.42
      pick: 0.2
      fit: 0.44
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
