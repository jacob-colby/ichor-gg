---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.6
  aspect_win_rate: 0.67
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.3
    win_rate: 0.67
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.2
      win_rate: 1.0
    - name: Breastplate of Valor
      pick_rate: 0.2
      win_rate: 0.5
  - name: Captain's Ring
    pick_rate: 0.1
    win_rate: 0.0
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.1
      win_rate: 1.0
    - name: Golden Blade
      pick_rate: 0.1
      win_rate: 1.0
  - name: Berserker's Shield
    pick_rate: 0.3
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.0
    - name: Mana Tome
      pick_rate: 0.1
      win_rate: 0.0
  - name: Totem of Death
    pick_rate: 0.22
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.22
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 1.0
  - name: Rod of Asclepius
    pick_rate: 0.22
    win_rate: 1.0
    alternates:
    - name: Captain's Ring
      pick_rate: 0.11
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.0
  - name: Flaming Pearl
    pick_rate: 0.14
    win_rate: 1.0
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.14
      win_rate: 1.0
    - name: Heartwood Charm
      pick_rate: 0.14
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.2
    win_rate: 0.5
  - name: Warrior's Axe
    pick_rate: 0.2
    win_rate: 0.5
  - name: Hunter's Cowl
    pick_rate: 0.1
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-10-21'
  god_win_rate: 0.6
  god_matches_won: 6
  god_matches_played: 10
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Shield Splitter, Golden Blade, Shifter''s
    Shield, Runeforged Hammer, Eye of the Storm, Hydra''s Lament, Shield of the Phoenix,
    Erosion, Eye of Providence, Draconic Scale, Tyrfing, Stone of Binding, Pharaoh''s
    Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.74
      efficiency: 0.66
      win: 1.0
      pick: 0.18
      fit: 0.32
    Berserker's Shield:
      total: 0.78
      efficiency: 0.68
      win: 1.0
      pick: 0.47
      fit: 0.43
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 0.37
      fit: 0.49
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.43
      fit: 0.6
    Amanita Charm:
      total: 0.75
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Golden Blade,
    Runeforged Hammer, Shield Splitter, Shifter''s Shield, Eye of the Storm, Hydra''s
    Lament, The Reaper, Yogi''s Necklace, Erosion, Chandra''s Grace, Eye of Providence,
    Draconic Scale, Phoenix Feather, Avenging Blade, Tyrfing, Glorious Pridwen, Pharaoh''s
    Curse, Riptalon, Lernaean Bow, Stone of Binding, Screeching Gargoyle.'
  slot_scores:
    Berserker's Shield:
      total: 0.78
      efficiency: 0.68
      win: 1.0
      pick: 0.47
      fit: 0.45
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.4
    Shield of the Phoenix:
      total: 0.75
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.79
    Freya's Tears:
      total: 0.75
      efficiency: 0.61
      win: 1.0
      pick: 0.37
      fit: 0.45
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.43
      fit: 0.6
    Amanita Charm:
      total: 0.8
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    Avenging Blade, Void Shield, Heartseeker, Void Stone, Shield Splitter, Runeforged
    Hammer, Golden Blade, Silverbranch Bow, Shifter''s Shield, Tekko-Kagi, Titan''s
    Bane, The Crusher, Toxic Blade, Hydra''s Lament, Eye of the Storm, The Reaper,
    Shield of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Tyrfing.'
  slot_scores:
    Stone of Binding:
      total: 0.73
      efficiency: 0.51
      win: 1.0
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.76
      efficiency: 0.68
      win: 1.0
      pick: 0.47
      fit: 0.32
    Jotunn's Revenge:
      total: 0.78
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.37
      fit: 0.37
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.43
      fit: 0.48
    Amanita Charm:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Tyrfing
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Golden Blade, Tyrfing, Shifter''s
    Shield, Runeforged Hammer, Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean
    Bow, Silverbranch Bow, Hydra''s Lament, Shield of the Phoenix, Toxic Blade, Erosion,
    Eye of the Storm, Eye of Providence, Stone of Binding, Draconic Scale, Screeching
    Gargoyle, Daybreak Gavel, Magi''s Cloak, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.14
      fit: 0.56
    Berserker's Shield:
      total: 0.78
      efficiency: 0.68
      win: 1.0
      pick: 0.47
      fit: 0.43
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.24
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.37
      fit: 0.34
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.43
      fit: 0.45
    Tyrfing:
      total: 0.7
      efficiency: 0.48
      win: 1.0
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle, Shifter''s Shield,
    Shield Splitter, Golden Blade, Runeforged Hammer, Prophetic Cloak, Erosion, Gladiator''s
    Shield, Eye of Providence, Arondight, Draconic Scale, Stone of Binding, Eye of
    the Storm, Pharaoh''s Curse, Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian
    Mail, Mantle Of Discord, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.76
      efficiency: 0.66
      win: 1.0
      pick: 0.18
      fit: 0.44
    Berserker's Shield:
      total: 0.76
      efficiency: 0.68
      win: 1.0
      pick: 0.47
      fit: 0.34
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.77
      efficiency: 0.61
      win: 1.0
      pick: 0.37
      fit: 0.58
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.43
      fit: 0.5
    Amanita Charm:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Shield Splitter, Shifter''s
    Shield, Golden Blade, Runeforged Hammer, Eye of the Storm, Hydra''s Lament, Shield
    of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Tyrfing, Stone of
    Binding, Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle,
    Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Heartseeker, Hide of the Nemean
    Lion, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.74
      efficiency: 0.66
      win: 1.0
      pick: 0.18
      fit: 0.32
    Berserker's Shield:
      total: 0.78
      efficiency: 0.68
      win: 1.0
      pick: 0.47
      fit: 0.43
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 0.37
      fit: 0.49
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.43
      fit: 0.6
    Amanita Charm:
      total: 0.75
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  starter: *id001
---
