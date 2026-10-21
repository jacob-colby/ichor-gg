---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.25
  aspect_win_rate: 0.0
  slot_order:
  - name: Berserker's Shield
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.25
      win_rate: 1.0
    - name: Shifter's Shield
      pick_rate: 0.25
      win_rate: 0.0
  - name: Genji's Guard
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Toxic Blade
      pick_rate: 0.25
      win_rate: 1.0
    - name: Golden Blade
      pick_rate: 0.25
      win_rate: 0.0
  - name: Contagion
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Draconic Scale
      pick_rate: 0.25
      win_rate: 0.0
    - name: Freya's Tears
      pick_rate: 0.25
      win_rate: 1.0
  - name: Shogun's Ofuda
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Contagion
      pick_rate: 0.25
      win_rate: 1.0
    - name: Xibalban Effigy
      pick_rate: 0.25
      win_rate: 0.0
  - name: Sundering Echo
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Rune
      pick_rate: 0.33
      win_rate: 0.0
    - name: Hide of the Nemean Lion
      pick_rate: 0.33
      win_rate: 1.0
  - name: Medal of Defense
    pick_rate: 1.0
    win_rate: 1.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.75
    win_rate: 0.67
  - name: Conduit Gem
    pick_rate: 0.25
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-10-21'
  god_win_rate: 0.5
  god_matches_won: 2
  god_matches_played: 4
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
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Kinetic Cuirass,
    Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm, Breastplate of Valor,
    Pharaoh''s Curse, Avenging Blade, Hydra''s Lament, Tekko-Kagi, Heartseeker, Dominance,
    Deathbringer, Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield
    of the Phoenix, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.34
      fit: 0.13
    Berserker's Shield:
      total: 0.77
      efficiency: 0.68
      win: 1.0
      pick: 0.25
      fit: 0.45
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.3
    Runeforged Hammer:
      total: 0.72
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.39
      fit: 0.23
    Amanita Charm:
      total: 0.73
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Breastplate of Valor, The
    Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean Bow, Tyrfing, Riptalon, Erosion,
    Phoenix Feather, Eye of Providence, Avenging Blade, Hydra''s Lament, Chandra''s
    Grace, Stone of Binding, Daybreak Gavel, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.77
      efficiency: 0.68
      win: 1.0
      pick: 0.25
      fit: 0.47
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.54
    Shield of the Phoenix:
      total: 0.73
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.39
      fit: 0.3
    Amanita Charm:
      total: 0.79
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Amanita Charm, Heartseeker, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Runeforged Hammer, Screeching Gargoyle, Void
    Shield, Kinetic Cuirass, Titan''s Bane, Void Stone, The Crusher, Breastplate of
    Valor, Lernaean Bow, The Reaper, Tyrfing, Shield Splitter, Hydra''s Lament, Riptalon,
    Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.72
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.68
    Toxic Blade:
      total: 0.72
      efficiency: 0.46
      win: 1.0
      pick: 0.34
      fit: 0.6
    Berserker's Shield:
      total: 0.75
      efficiency: 0.68
      win: 1.0
      pick: 0.25
      fit: 0.33
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.48
    Heartseeker:
      total: 0.71
      efficiency: 0.47
      win: 1.0
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Toxic Blade
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Tyrfing
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Tyrfing, Kinetic Cuirass, Riptalon,
    Runeforged Hammer, Lernaean Bow, Silverbranch Bow, Breastplate of Valor, Pharaoh''s
    Curse, Shield Splitter, Eye of the Storm, Hydra''s Lament, Tekko-Kagi, The Reaper,
    Daybreak Gavel, Avenging Blade, Dominance, Erosion, Shield of the Phoenix, Eye
    of Providence, Heartseeker, Vital Amplifier.'
  slot_scores:
    Genji's Guard:
      total: 0.71
      efficiency: 0.66
      win: 1.0
      pick: 0.34
      fit: 0.1
    Berserker's Shield:
      total: 0.76
      efficiency: 0.68
      win: 1.0
      pick: 0.25
      fit: 0.41
    Jotunn's Revenge:
      total: 0.73
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.18
    Tyrfing:
      total: 0.71
      efficiency: 0.48
      win: 1.0
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.26
    Shogun's Ofuda:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.42
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic Cuirass,
    Screeching Gargoyle, Runeforged Hammer, Arondight, Lernaean Bow, Pharaoh''s Curse,
    Tyrfing, Shield Splitter, Daybreak Gavel, Eye of Erebus, Gladiator''s Shield,
    Eye of the Storm, Chandra''s Grace, Silverbranch Bow, Erosion, Avenging Blade,
    Eye of Providence, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.75
      efficiency: 0.66
      win: 1.0
      pick: 0.34
      fit: 0.36
    Berserker's Shield:
      total: 0.75
      efficiency: 0.68
      win: 1.0
      pick: 0.25
      fit: 0.33
    Breastplate of Valor:
      total: 0.73
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.75
      efficiency: 0.61
      win: 1.0
      pick: 0.39
      fit: 0.43
    Amanita Charm:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm, Breastplate
    of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament, Tekko-Kagi, Heartseeker,
    Dominance, Deathbringer, Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence,
    Shield of the Phoenix, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.3
      efficiency: 0.52
      win: 0.0
      pick: 0.34
      fit: 0.64
    Berserker's Shield:
      total: 0.77
      efficiency: 0.68
      win: 1.0
      pick: 0.25
      fit: 0.45
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.72
      win: 1.0
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.72
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.73
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  starter: *id001
---
