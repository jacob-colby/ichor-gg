---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.55
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.74
    win_rate: 0.57
    alternates:
    - name: Vital Amplifier
      pick_rate: 0.07
      win_rate: 0.49
    - name: Berserker's Shield
      pick_rate: 0.05
      win_rate: 0.44
  - name: Berserker's Shield
    pick_rate: 0.48
    win_rate: 0.57
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.21
      win_rate: 0.58
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.44
  - name: Sanguine Lash
    pick_rate: 0.15
    win_rate: 0.57
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.21
      win_rate: 0.57
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.47
  - name: Kinetic Cuirass
    pick_rate: 0.21
    win_rate: 0.53
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.1
      win_rate: 0.54
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.53
  - name: Hussar's Wings
    pick_rate: 0.07
    win_rate: 0.77
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.59
    - name: Shogun's Ofuda
      pick_rate: 0.05
      win_rate: 0.52
  - name: Medal of Defense
    pick_rate: 0.09
    win_rate: 0.51
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.6
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.38
    win_rate: 0.64
  - name: Death's Embrace
    pick_rate: 0.23
    win_rate: 0.6
  - name: Leather Cowl
    pick_rate: 0.18
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-11-02'
  god_win_rate: 0.5404580152671755
  god_matches_won: 354
  god_matches_played: 655
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
  - Shield Splitter
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield Splitter, Jotunn''s Revenge, Genji''s Guard, Runeforged
    Hammer, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Hydra''s
    Lament, Oni Hunter''s Garb, Shield of the Phoenix, Stone of Binding, Shifter''s
    Shield, Magi''s Cloak, Midgardian Mail, Avenging Blade, Wyrmskin Hide, Mantle
    Of Discord, Titan''s Bane, Leviathan''s Hide, Screeching Gargoyle, Arondight,
    Ancile, Prophetic Cloak, Stampede.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.38
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.67
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.53
      pick: 0.35
      fit: 0.7
    Freya's Tears:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.18
      fit: 0.54
    Hussar's Wings:
      total: 0.58
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.6
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Berserker's Shield
  - Shield of the Phoenix
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Shield Splitter,
    Genji''s Guard, Runeforged Hammer, Phoenix Feather, The Reaper, Yogi''s Necklace,
    Hydra''s Lament, Breastplate of Valor, Erosion, Eye of Providence, Oni Hunter''s
    Garb, Draconic Scale, Avenging Blade, Chandra''s Grace, Wyrmskin Hide, Midgardian
    Mail, Shifter''s Shield, Titan''s Bane, Glorious Pridwen, Leviathan''s Hide, Regrowth
    Striders, Stone of Binding, Arondight, Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.42
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.4
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.67
      pick: 0.18
      fit: 0.47
    Hussar's Wings:
      total: 0.57
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.58
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Shield Splitter,
    Avenging Blade, Titan''s Bane, Genji''s Guard, Screeching Gargoyle, Void Stone,
    Void Shield, The Crusher, Runeforged Hammer, Breastplate of Valor, Heartseeker,
    The Reaper, Hydra''s Lament, Erosion, Oni Hunter''s Garb, Eye of Providence, Tekko-Kagi,
    Draconic Scale, Shield of the Phoenix, Midgardian Mail, Magi''s Cloak, Mantle
    Of Discord, Leviathan''s Hide, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.71
    Berserker's Shield:
      total: 0.56
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.18
      fit: 0.39
    Hussar's Wings:
      total: 0.55
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.43
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Jotunn''s Revenge, Golden Blade, Shield
    Splitter, Tyrfing, Breastplate of Valor, Runeforged Hammer, Tekko-Kagi, Pharaoh''s
    Curse, Lernaean Bow, Toxic Blade, Oni Hunter''s Garb, Hydra''s Lament, Silverbranch
    Bow, Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Midgardian
    Mail, Shield of the Phoenix, Magi''s Cloak, The Reaper, Screeching Gargoyle, Riptalon,
    Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
      win: 0.57
      pick: 0.65
      fit: 0.45
    Tyrfing:
      total: 0.51
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.56
      efficiency: 0.58
      win: 0.67
      pick: 0.18
      fit: 0.34
    Hussar's Wings:
      total: 0.54
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Hussar's Wings
  - Amanita Charm
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Amanita Charm, Breastplate of Valor, Shield of the Phoenix, Hydra''s Lament, Shield
    Splitter, Screeching Gargoyle, Arondight, Prophetic Cloak, Runeforged Hammer,
    Erosion, Eye of Providence, Oni Hunter''s Garb, Gladiator''s Shield, Draconic
    Scale, Stone of Binding, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Shifter''s
    Shield, Leviathan''s Hide, Chandra''s Grace, Regrowth Striders, Eye of Erebus,
    Glorious Pridwen, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.57
      pick: 0.0
      fit: 0.48
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.29
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.61
      efficiency: 0.58
      win: 0.67
      pick: 0.18
      fit: 0.64
    Hussar's Wings:
      total: 0.55
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  - Hussar's Wings
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
    Underrated for this god: Amanita Charm, Shield Splitter, Jotunn''s Revenge, Genji''s
    Guard, Runeforged Hammer, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Hydra''s Lament, Oni Hunter''s Garb, Shield of the Phoenix, Stone of Binding,
    Shifter''s Shield, Magi''s Cloak, Midgardian Mail, Avenging Blade, Wyrmskin Hide,
    Mantle Of Discord, Titan''s Bane, Leviathan''s Hide, Screeching Gargoyle, Arondight,
    Ancile, Prophetic Cloak, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.38
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.53
      pick: 0.35
      fit: 0.7
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Hussar's Wings
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield Splitter, Jotunn''s
    Revenge, Genji''s Guard, Runeforged Hammer, Breastplate of Valor, Erosion, Eye
    of Providence, Draconic Scale, Hydra''s Lament, Oni Hunter''s Garb, Shield of
    the Phoenix, Stone of Binding, Shifter''s Shield, Magi''s Cloak, Midgardian Mail,
    Avenging Blade, Wyrmskin Hide, Mantle Of Discord, Titan''s Bane, Leviathan''s
    Hide, Screeching Gargoyle, Arondight, Ancile, Prophetic Cloak, Stampede.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.4
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.38
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.53
      pick: 0.35
      fit: 0.7
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.67
    Hussar's Wings:
      total: 0.58
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.6
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Hussar's Wings
  swaps:
  - added: Hussar's Wings
    removed: Genji's Guard
    reason: community 77% win over 46 matches (vs 54% on this god), taking the model's
      weakest slot from Genji's Guard
  starter: *id001
---
