---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.48
  aspect_win_rate: 0.64
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.14
    win_rate: 0.63
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.43
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.83
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.63
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.43
    - name: Chandra's Grace
      pick_rate: 0.07
      win_rate: 1.0
  - name: Freya's Tears
    pick_rate: 0.25
    win_rate: 0.64
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.83
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.4
  - name: Rod of Asclepius
    pick_rate: 0.08
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.56
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 1.0
  - name: Draconic Scale
    pick_rate: 0.1
    win_rate: 0.6
    alternates:
    - name: Captain's Ring
      pick_rate: 0.06
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.33
  - name: Sage's Ring
    pick_rate: 0.12
    win_rate: 0.75
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.33
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.5
  - name: Sands Of Time
    pick_rate: 0.17
    win_rate: 0.7
  - name: Hunter's Cowl
    pick_rate: 0.14
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-10-25'
  god_win_rate: 0.6206896551724138
  god_matches_won: 36
  god_matches_played: 58
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-25'
  god_matches_analyzed: 4936
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Chandra's Grace
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Golden Blade, Runeforged Hammer, Eye of the Storm, Hydra''s Lament, Shield of
    the Phoenix, Erosion, Eye of Providence, Tyrfing, Stone of Binding, Pharaoh''s
    Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak, Shogun''s
    Ofuda, Midgardian Mail, Mantle Of Discord, Heartseeker, Hide of the Nemean Lion,
    Daybreak Gavel.'
  slot_scores:
    Chandra's Grace:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.1
      fit: 0.3
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.64
      pick: 0.39
      fit: 0.49
    Shifter's Shield:
      total: 0.65
      efficiency: 0.55
      win: 0.83
      pick: 0.17
      fit: 0.5
    Stampede:
      total: 0.61
      efficiency: 0.51
      win: 0.83
      pick: 0.1
      fit: 0.33
  community_ordered:
  - Chandra's Grace
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Chandra's Grace
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Chandra''s Grace, Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Golden Blade, Runeforged Hammer, Shield Splitter, Eye of the
    Storm, Hydra''s Lament, The Reaper, Yogi''s Necklace, Erosion, Eye of Providence,
    Phoenix Feather, Avenging Blade, Tyrfing, Glorious Pridwen, Pharaoh''s Curse,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Stone of Binding, Screeching Gargoyle.'
  slot_scores:
    Chandra's Grace:
      total: 0.71
      efficiency: 0.45
      win: 1.0
      pick: 0.1
      fit: 0.64
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.39
      fit: 0.45
    Shifter's Shield:
      total: 0.65
      efficiency: 0.55
      win: 0.83
      pick: 0.17
      fit: 0.5
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.8
    Stampede:
      total: 0.61
      efficiency: 0.51
      win: 0.83
      pick: 0.1
      fit: 0.35
  community_ordered:
  - Chandra's Grace
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Chandra's Grace
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Freya's Tears
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    Avenging Blade, Kinetic Cuirass, Void Shield, Heartseeker, Void Stone, Shield
    Splitter, Runeforged Hammer, Silverbranch Bow, Tekko-Kagi, Titan''s Bane, The
    Crusher, Golden Blade, Toxic Blade, Hydra''s Lament, Eye of the Storm, The Reaper,
    Shield of the Phoenix, Erosion, Eye of Providence, Tyrfing.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.66
    Chandra's Grace:
      total: 0.65
      efficiency: 0.45
      win: 1.0
      pick: 0.1
      fit: 0.22
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.39
      fit: 0.37
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.83
      pick: 0.17
      fit: 0.38
    Stampede:
      total: 0.59
      efficiency: 0.51
      win: 0.83
      pick: 0.1
      fit: 0.25
  community_ordered:
  - Chandra's Grace
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Chandra's Grace
  - Tyrfing
  - Shifter's Shield
  - Stampede
  - Pharaoh's Curse
  flex_slots:
  - Tyrfing
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Golden Blade, Tyrfing,
    Runeforged Hammer, Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Silverbranch Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Toxic
    Blade, Erosion, Eye of the Storm, Eye of Providence, Stone of Binding, Screeching
    Gargoyle, Daybreak Gavel, Magi''s Cloak, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.56
    Chandra's Grace:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.1
      fit: 0.21
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.63
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.83
      pick: 0.17
      fit: 0.35
    Stampede:
      total: 0.59
      efficiency: 0.51
      win: 0.83
      pick: 0.1
      fit: 0.23
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Chandra's Grace
  - Shifter's Shield
  - Stampede
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Stampede
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chandra''s Grace, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Shield Splitter, Runeforged Hammer, Prophetic Cloak, Erosion, Golden
    Blade, Gladiator''s Shield, Eye of Providence, Arondight, Stone of Binding, Eye
    of the Storm, Pharaoh''s Curse, Eye of Erebus, Magi''s Cloak, Daybreak Gavel,
    Midgardian Mail, Shogun''s Ofuda, Mantle Of Discord.'
  slot_scores:
    Chandra's Grace:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.1
      fit: 0.43
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.63
      pick: 0.19
      fit: 0.44
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.64
      pick: 0.39
      fit: 0.58
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.83
      pick: 0.17
      fit: 0.4
    Stampede:
      total: 0.6
      efficiency: 0.51
      win: 0.83
      pick: 0.1
      fit: 0.26
  community_ordered:
  - Chandra's Grace
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  - Stampede
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield
    Splitter, Golden Blade, Runeforged Hammer, Eye of the Storm, Hydra''s Lament,
    Shield of the Phoenix, Erosion, Eye of Providence, Tyrfing, Stone of Binding,
    Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak,
    Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Heartseeker, Hide of the
    Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.63
      pick: 0.19
      fit: 0.32
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.43
      pick: 0.16
      fit: 0.43
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.64
      pick: 0.39
      fit: 0.49
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
---
