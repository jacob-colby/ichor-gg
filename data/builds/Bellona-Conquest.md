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
      win_rate: 0.48
    - name: Berserker's Shield
      pick_rate: 0.05
      win_rate: 0.44
  - name: Berserker's Shield
    pick_rate: 0.48
    win_rate: 0.57
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.2
      win_rate: 0.58
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.45
  - name: Sanguine Lash
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.21
      win_rate: 0.57
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.48
  - name: Kinetic Cuirass
    pick_rate: 0.21
    win_rate: 0.53
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.1
      win_rate: 0.55
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.54
  - name: Hussar's Wings
    pick_rate: 0.07
    win_rate: 0.78
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.6
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
    pick_rate: 0.37
    win_rate: 0.64
  - name: Death's Embrace
    pick_rate: 0.23
    win_rate: 0.6
  - name: Leather Cowl
    pick_rate: 0.18
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-11-04'
  god_win_rate: 0.5417298937784522
  god_matches_won: 357
  god_matches_played: 659
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
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Shield Splitter, Jotunn''s Revenge, Draconic
    Scale, Shield of the Phoenix, Breastplate of Valor, Runeforged Hammer, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Shifter''s Shield, Hydra''s Lament, The
    Reaper, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s Hide,
    Magi''s Cloak, Mantle Of Discord, Wyrmskin Hide, Tyrfing, Avenging Blade, Ancile,
    Arondight, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.29
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.65
      fit: 0.34
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.53
      pick: 0.35
      fit: 0.64
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.18
      fit: 0.48
    Hussar's Wings:
      total: 0.58
      efficiency: 0.39
      win: 0.78
      pick: 0.15
      fit: 0.54
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.54
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
  - Berserker's Shield
  - Shield of the Phoenix
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, The Reaper, Genji''s Guard, Jotunn''s
    Revenge, Shield Splitter, Phoenix Feather, Yogi''s Necklace, Runeforged Hammer,
    Draconic Scale, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s Garb, Erosion,
    Hydra''s Lament, Eye of Providence, Bloodforge, Shifter''s Shield, Midgardian
    Mail, Regrowth Striders, Leviathan''s Hide, Avenging Blade, Glorious Pridwen,
    Wyrmskin Hide, Screeching Gargoyle, Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.65
      fit: 0.36
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.76
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.53
      pick: 0.35
      fit: 0.62
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.18
      fit: 0.42
    Hussar's Wings:
      total: 0.57
      efficiency: 0.39
      win: 0.78
      pick: 0.15
      fit: 0.52
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Screeching Gargoyle,
    The Reaper, Stone of Binding, Shield Splitter, Avenging Blade, Void Stone, The
    Crusher, Void Shield, Heartseeker, Breastplate of Valor, Titan''s Bane, Shield
    of the Phoenix, Runeforged Hammer, Draconic Scale, Oni Hunter''s Garb, Hydra''s
    Lament, Erosion, Eye of Providence, Shifter''s Shield, Midgardian Mail, Leviathan''s
    Hide, Avatar''s Parashu, Magi''s Cloak, Mantle Of Discord.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.65
      fit: 0.26
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.53
      pick: 0.35
      fit: 0.5
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.18
      fit: 0.36
    Hussar's Wings:
      total: 0.56
      efficiency: 0.39
      win: 0.78
      pick: 0.15
      fit: 0.4
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Tyrfing, Jotunn''s Revenge, Golden Blade,
    Shield Splitter, Breastplate of Valor, Shield of the Phoenix, Oni Hunter''s Garb,
    Draconic Scale, Runeforged Hammer, Pharaoh''s Curse, Erosion, Eye of Providence,
    Hydra''s Lament, Toxic Blade, Shifter''s Shield, Screeching Gargoyle, Midgardian
    Mail, The Reaper, Stone of Binding, Lernaean Bow, Dominance, Leviathan''s Hide,
    Silverbranch Bow, Magi''s Cloak.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.61
      efficiency: 0.72
      win: 0.57
      pick: 0.65
      fit: 0.45
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.18
      fit: 0.34
    Hussar's Wings:
      total: 0.55
      efficiency: 0.39
      win: 0.78
      pick: 0.15
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Amanita Charm, Jotunn''s
    Revenge, Breastplate of Valor, Shield of the Phoenix, Screeching Gargoyle, Hydra''s
    Lament, Shield Splitter, Gladiator''s Shield, Draconic Scale, Oni Hunter''s Garb,
    Prophetic Cloak, Arondight, Erosion, Eye of Providence, Runeforged Hammer, Shifter''s
    Shield, Midgardian Mail, Stone of Binding, Chandra''s Grace, Leviathan''s Hide,
    Regrowth Striders, The Reaper, Magi''s Cloak, Mantle Of Discord, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.44
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.65
      fit: 0.27
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.18
      fit: 0.59
    Hussar's Wings:
      total: 0.56
      efficiency: 0.39
      win: 0.78
      pick: 0.15
      fit: 0.41
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
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
    Hammer, Erosion, Oni Hunter''s Garb, Eye of Providence, Shifter''s Shield, Hydra''s
    Lament, The Reaper, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s
    Hide, Magi''s Cloak, Mantle Of Discord, Wyrmskin Hide, Tyrfing, Avenging Blade,
    Ancile, Arondight, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.53
      pick: 0.35
      fit: 0.64
    Shield Splitter:
      total: 0.55
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.18
      fit: 0.48
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Shield Splitter
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Hussar's Wings
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Genji''s Guard, Shield
    Splitter, Jotunn''s Revenge, Draconic Scale, Shield of the Phoenix, Breastplate
    of Valor, Runeforged Hammer, Erosion, Oni Hunter''s Garb, Eye of Providence, Shifter''s
    Shield, Hydra''s Lament, The Reaper, Midgardian Mail, Stone of Binding, Screeching
    Gargoyle, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Wyrmskin Hide,
    Tyrfing, Avenging Blade, Ancile, Arondight, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.29
    Shield Splitter:
      total: 0.55
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.6
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.53
      pick: 0.35
      fit: 0.64
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.18
      fit: 0.48
    Hussar's Wings:
      total: 0.58
      efficiency: 0.39
      win: 0.78
      pick: 0.15
      fit: 0.54
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  swaps:
  - added: Hussar's Wings
    removed: Jotunn's Revenge
    reason: community 78% win over 46 matches (vs 54% on this god), taking the model's
      weakest slot from Jotunn's Revenge
  starter: *id001
---
