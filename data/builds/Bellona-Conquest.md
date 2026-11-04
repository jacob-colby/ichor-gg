---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 1.0
    win_rate: 1.0
  - name: Berserker's Shield
    pick_rate: 1.0
    win_rate: 1.0
  - name: Kinetic Cuirass
    pick_rate: 1.0
    win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 1.0
    win_rate: 1.0
  - name: Hussar's Wings
    pick_rate: 1.0
    win_rate: 1.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 1.0
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-11-04'
  god_win_rate: 1
  god_matches_won: 1
  god_matches_played: 1
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield Splitter, Jotunn''s Revenge, Genji''s Guard, Freya''s
    Tears, Runeforged Hammer, Breastplate of Valor, Erosion, Hydra''s Lament, Eye
    of Providence, Draconic Scale, Oni Hunter''s Garb, The Reaper, Shield of the Phoenix,
    Stone of Binding, Midgardian Mail, Magi''s Cloak, Shifter''s Shield, Avenging
    Blade, Titan''s Bane, Mantle Of Discord, Leviathan''s Hide, Wyrmskin Hide, Screeching
    Gargoyle, Arondight, Sanguine Lash, Ancile, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.29
    Berserker's Shield:
      total: 0.78
      efficiency: 0.67
      win: 1.0
      pick: 1.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.79
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.64
    Shield Splitter:
      total: 0.75
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.76
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
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
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Shield of the Phoenix, Jotunn''s Revenge,
    Shield Splitter, Genji''s Guard, Runeforged Hammer, Phoenix Feather, Freya''s
    Tears, Bloodforge, Yogi''s Necklace, Breastplate of Valor, Hydra''s Lament, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Chandra''s Grace, Avenging Blade, Draconic
    Scale, Midgardian Mail, Titan''s Bane, Regrowth Striders, Wyrmskin Hide, Leviathan''s
    Hide, Shifter''s Shield, Glorious Pridwen, Stone of Binding, Arondight.'
  slot_scores:
    Berserker's Shield:
      total: 0.79
      efficiency: 0.67
      win: 1.0
      pick: 1.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.79
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.62
    Shield Splitter:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.75
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.8
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, The Reaper,
    Avenging Blade, Shield Splitter, Genji''s Guard, Screeching Gargoyle, Titan''s
    Bane, Void Stone, Void Shield, Freya''s Tears, The Crusher, Runeforged Hammer,
    Breastplate of Valor, Heartseeker, Hydra''s Lament, Oni Hunter''s Garb, Erosion,
    Eye of Providence, Tekko-Kagi, Draconic Scale, Shield of the Phoenix, Midgardian
    Mail, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.73
      efficiency: 0.5
      win: 1.0
      pick: 0.0
      fit: 0.69
    Avenging Blade:
      total: 0.72
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.77
      efficiency: 0.67
      win: 1.0
      pick: 1.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Jotunn''s Revenge, Golden Blade, Shield
    Splitter, Tyrfing, Freya''s Tears, Breastplate of Valor, Tekko-Kagi, Runeforged
    Hammer, Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Oni Hunter''s Garb, Shogun''s
    Ofuda, Silverbranch Bow, Hydra''s Lament, Erosion, Eye of Providence, Stone of
    Binding, Draconic Scale, Midgardian Mail, Shield of the Phoenix, Magi''s Cloak,
    The Reaper, Riptalon, Screeching Gargoyle, Titan''s Bane.'
  slot_scores:
    Golden Blade:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.72
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.21
    Berserker's Shield:
      total: 0.83
      efficiency: 0.74
      win: 1.0
      pick: 1.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.48
    Tyrfing:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Freya''s Tears, Amanita Charm, Breastplate of Valor, Hydra''s Lament, Shield of
    the Phoenix, Shield Splitter, Screeching Gargoyle, Arondight, Runeforged Hammer,
    Prophetic Cloak, Oni Hunter''s Garb, Erosion, Eye of Providence, Draconic Scale,
    Stone of Binding, Gladiator''s Shield, Midgardian Mail, Magi''s Cloak, Mantle
    Of Discord, Leviathan''s Hide, The Reaper, Shifter''s Shield, Regrowth Striders,
    Chandra''s Grace, Eye of Erebus, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.76
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.44
    Berserker's Shield:
      total: 0.77
      efficiency: 0.67
      win: 1.0
      pick: 1.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.51
    Freya's Tears:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
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
    Guard, Freya''s Tears, Runeforged Hammer, Breastplate of Valor, Erosion, Hydra''s
    Lament, Eye of Providence, Draconic Scale, Oni Hunter''s Garb, The Reaper, Shield
    of the Phoenix, Stone of Binding, Midgardian Mail, Magi''s Cloak, Shifter''s Shield,
    Avenging Blade, Titan''s Bane, Mantle Of Discord, Leviathan''s Hide, Wyrmskin
    Hide, Screeching Gargoyle, Arondight, Sanguine Lash, Ancile, Hide of the Nemean
    Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.29
    Berserker's Shield:
      total: 0.78
      efficiency: 0.67
      win: 1.0
      pick: 1.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.79
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.64
    Shield Splitter:
      total: 0.75
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.76
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
