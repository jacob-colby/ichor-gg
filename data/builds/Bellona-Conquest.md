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
  last_verified: '2026-11-03'
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
    Hammer, Breastplate of Valor, Erosion, Hydra''s Lament, Eye of Providence, Draconic
    Scale, Oni Hunter''s Garb, The Reaper, Shield of the Phoenix, Stone of Binding,
    Midgardian Mail, Magi''s Cloak, Shifter''s Shield, Avenging Blade, Titan''s Bane,
    Mantle Of Discord, Leviathan''s Hide, Wyrmskin Hide, Screeching Gargoyle, Arondight,
    Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.34
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.6
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.53
      pick: 0.35
      fit: 0.64
    Freya's Tears:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.18
      fit: 0.48
    Hussar's Wings:
      total: 0.57
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.54
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
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
  - Jotunn's Revenge
  - Berserker's Shield
  - Freya's Tears
  - The Reaper
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - The Reaper
  - Jotunn's Revenge
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
    this god: Amanita Charm, The Reaper, Shield of the Phoenix, Jotunn''s Revenge,
    Shield Splitter, Genji''s Guard, Runeforged Hammer, Phoenix Feather, Bloodforge,
    Yogi''s Necklace, Breastplate of Valor, Hydra''s Lament, Erosion, Oni Hunter''s
    Garb, Eye of Providence, Chandra''s Grace, Avenging Blade, Draconic Scale, Midgardian
    Mail, Titan''s Bane, Regrowth Striders, Wyrmskin Hide, Leviathan''s Hide, Shifter''s
    Shield, Glorious Pridwen, Stone of Binding, Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.38
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.36
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.67
      pick: 0.18
      fit: 0.42
    The Reaper:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.68
    Hussar's Wings:
      total: 0.57
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.52
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.82
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
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, The Reaper,
    Avenging Blade, Shield Splitter, Genji''s Guard, Screeching Gargoyle, Titan''s
    Bane, Void Stone, Void Shield, The Crusher, Runeforged Hammer, Breastplate of
    Valor, Heartseeker, Hydra''s Lament, Oni Hunter''s Garb, Erosion, Eye of Providence,
    Tekko-Kagi, Draconic Scale, Shield of the Phoenix, Midgardian Mail, Magi''s Cloak,
    Mantle Of Discord, Leviathan''s Hide, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.69
    Berserker's Shield:
      total: 0.56
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.18
      fit: 0.36
    Hussar's Wings:
      total: 0.55
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.4
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.4
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
    Splitter, Tyrfing, Breastplate of Valor, Tekko-Kagi, Runeforged Hammer, Pharaoh''s
    Curse, Lernaean Bow, Toxic Blade, Oni Hunter''s Garb, Silverbranch Bow, Hydra''s
    Lament, Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Midgardian
    Mail, Shield of the Phoenix, Magi''s Cloak, The Reaper, Riptalon, Screeching Gargoyle,
    Titan''s Bane.'
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
    Amanita Charm, Breastplate of Valor, Hydra''s Lament, Shield of the Phoenix, Shield
    Splitter, Screeching Gargoyle, Arondight, Runeforged Hammer, Prophetic Cloak,
    Oni Hunter''s Garb, Erosion, Eye of Providence, Draconic Scale, Stone of Binding,
    Gladiator''s Shield, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Leviathan''s
    Hide, The Reaper, Shifter''s Shield, Regrowth Striders, Chandra''s Grace, Eye
    of Erebus, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.0
      fit: 0.44
    Berserker's Shield:
      total: 0.56
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.27
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.6
      efficiency: 0.58
      win: 0.67
      pick: 0.18
      fit: 0.59
    Hussar's Wings:
      total: 0.55
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.41
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
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
    Guard, Runeforged Hammer, Breastplate of Valor, Erosion, Hydra''s Lament, Eye
    of Providence, Draconic Scale, Oni Hunter''s Garb, The Reaper, Shield of the Phoenix,
    Stone of Binding, Midgardian Mail, Magi''s Cloak, Shifter''s Shield, Avenging
    Blade, Titan''s Bane, Mantle Of Discord, Leviathan''s Hide, Wyrmskin Hide, Screeching
    Gargoyle, Arondight, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.0
      fit: 0.29
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.34
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.53
      pick: 0.35
      fit: 0.64
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.54
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
    Revenge, Genji''s Guard, Runeforged Hammer, Breastplate of Valor, Erosion, Hydra''s
    Lament, Eye of Providence, Draconic Scale, Oni Hunter''s Garb, The Reaper, Shield
    of the Phoenix, Stone of Binding, Midgardian Mail, Magi''s Cloak, Shifter''s Shield,
    Avenging Blade, Titan''s Bane, Mantle Of Discord, Leviathan''s Hide, Wyrmskin
    Hide, Screeching Gargoyle, Arondight, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.57
      pick: 0.65
      fit: 0.34
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.53
      pick: 0.35
      fit: 0.64
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.6
    Hussar's Wings:
      total: 0.57
      efficiency: 0.38
      win: 0.77
      pick: 0.15
      fit: 0.54
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.54
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
