---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.52
  aspect_win_rate: 0.71
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.19
    win_rate: 0.6
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.15
      win_rate: 0.5
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.75
  - name: Berserker's Shield
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.5
    - name: Golden Blade
      pick_rate: 0.07
      win_rate: 1.0
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.4
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 1.0
    - name: Sanguine Lash
      pick_rate: 0.11
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.27
      win_rate: 0.71
    - name: Totem of Death
      pick_rate: 0.08
      win_rate: 1.0
  - name: Draconic Scale
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 1.0
  - name: Rod of Tahuti
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Contagion
      pick_rate: 0.05
      win_rate: 0.0
    - name: Glorious Pridwen
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.5
  - name: Pendulum of the Ages
    pick_rate: 0.19
    win_rate: 0.4
  - name: Sands Of Time
    pick_rate: 0.15
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-10-22'
  god_win_rate: 0.6296296296296297
  god_matches_won: 17
  god_matches_played: 27
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-22'
  god_matches_analyzed: 1760
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Glorious Pridwen
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Shield Splitter, Shifter''s Shield, Runeforged Hammer, Eye of the Storm,
    Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence, Tyrfing, Stone
    of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle,
    Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Heartseeker,
    Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.57
    Genji's Guard:
      total: 0.74
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.32
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.6
    Glorious Pridwen:
      total: 0.66
      efficiency: 0.38
      win: 1.0
      pick: 0.15
      fit: 0.49
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.75
      pick: 0.15
      fit: 0.33
  community_ordered:
  - Golden Blade
  - Genji's Guard
  - Glorious Pridwen
  - Stampede
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Glorious Pridwen
  - Amanita Charm
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Stampede
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
    this god: Golden Blade, Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Breastplate of Valor, Runeforged Hammer, Shield Splitter, Shifter''s
    Shield, Eye of the Storm, Hydra''s Lament, The Reaper, Yogi''s Necklace, Erosion,
    Chandra''s Grace, Eye of Providence, Phoenix Feather, Avenging Blade, Tyrfing,
    Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Stone of Binding, Screeching
    Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.61
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.3
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.4
    Glorious Pridwen:
      total: 0.7
      efficiency: 0.38
      win: 1.0
      pick: 0.15
      fit: 0.75
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.8
    Stampede:
      total: 0.58
      efficiency: 0.51
      win: 0.75
      pick: 0.15
      fit: 0.35
  community_ordered:
  - Golden Blade
  - Genji's Guard
  - Glorious Pridwen
  - Stampede
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Glorious Pridwen
  - Stampede
  flex_slots:
  - Stone of Binding
  - Stampede
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
    for this god: Golden Blade, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Screeching Gargoyle, Avenging Blade, Kinetic Cuirass, Breastplate of Valor, Void
    Shield, Heartseeker, Void Stone, Shield Splitter, Runeforged Hammer, Silverbranch
    Bow, Shifter''s Shield, Tekko-Kagi, Titan''s Bane, The Crusher, Toxic Blade, Hydra''s
    Lament, Eye of the Storm, The Reaper, Shield of the Phoenix, Erosion, Eye of Providence,
    Tyrfing.'
  slot_scores:
    Golden Blade:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.43
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.64
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.24
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.55
    Glorious Pridwen:
      total: 0.65
      efficiency: 0.38
      win: 1.0
      pick: 0.15
      fit: 0.37
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.75
      pick: 0.15
      fit: 0.25
  community_ordered:
  - Golden Blade
  - Genji's Guard
  - Glorious Pridwen
  - Stampede
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Glorious Pridwen
  flex_slots:
  - Berserker's Shield
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Tyrfing, Shifter''s Shield, Runeforged Hammer, Shield Splitter, Pharaoh''s
    Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Hydra''s Lament,
    Shield of the Phoenix, Toxic Blade, Erosion, Eye of the Storm, Eye of Providence,
    Stone of Binding, Screeching Gargoyle, Daybreak Gavel, Magi''s Cloak, The Reaper,
    Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.56
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.22
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.3
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.64
      pick: 0.0
      fit: 0.55
    Glorious Pridwen:
      total: 0.64
      efficiency: 0.38
      win: 1.0
      pick: 0.15
      fit: 0.34
  community_ordered:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Glorious Pridwen
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Glorious Pridwen
  - Stampede
  flex_slots:
  - Breastplate of Valor
  - Stampede
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
    + fit + win/pick). Underrated for this god: Golden Blade, Jotunn''s Revenge, Breastplate
    of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament,
    Screeching Gargoyle, Shifter''s Shield, Shield Splitter, Runeforged Hammer, Prophetic
    Cloak, Erosion, Gladiator''s Shield, Eye of Providence, Arondight, Stone of Binding,
    Eye of the Storm, Pharaoh''s Curse, Eye of Erebus, Magi''s Cloak, Daybreak Gavel,
    Midgardian Mail, Shogun''s Ofuda, Mantle Of Discord, Chandra''s Grace.'
  slot_scores:
    Golden Blade:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.38
    Genji's Guard:
      total: 0.76
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.44
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.43
    Glorious Pridwen:
      total: 0.68
      efficiency: 0.38
      win: 1.0
      pick: 0.15
      fit: 0.58
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.75
      pick: 0.15
      fit: 0.26
  community_ordered:
  - Golden Blade
  - Genji's Guard
  - Glorious Pridwen
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Shield Splitter, Shifter''s Shield, Golden Blade, Runeforged Hammer,
    Eye of the Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence,
    Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching
    Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord,
    Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.74
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.32
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.3
      fit: 0.43
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.4
      pick: 0.3
      fit: 0.49
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
---
