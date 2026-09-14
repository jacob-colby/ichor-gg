---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.6
  aspect_win_rate: 0.54
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.5
    win_rate: 0.51
    alternates:
    - name: Lifebinder
      pick_rate: 0.11
      win_rate: 0.64
    - name: The World Stone
      pick_rate: 0.05
      win_rate: 0.17
  - name: Prophetic Cloak
    pick_rate: 0.27
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.57
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.42
  - name: Gladiator's Shield
    pick_rate: 0.28
    win_rate: 0.68
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.55
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.55
  - name: Ethereal Staff
    pick_rate: 0.15
    win_rate: 0.71
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.09
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.83
  - name: Draconic Scale
    pick_rate: 0.1
    win_rate: 0.86
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
    - name: Manchu Bow
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Sundering Axe
    pick_rate: 0.34
    win_rate: 0.67
  - name: Warrior's Axe
    pick_rate: 0.23
    win_rate: 0.36
  - name: Death's Embrace
    pick_rate: 0.08
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-09-14'
  god_win_rate: 0.5365853658536586
  god_matches_won: 66
  god_matches_played: 123
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-14'
  god_matches_analyzed: 6946
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Golden Blade, Kinetic Cuirass, Runeforged
    Hammer, Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm, Berserker''s
    Shield, Breastplate of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament,
    Shogun''s Ofuda, Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic Blade,
    Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield of the Phoenix,
    Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.3
    Gladiator's Shield:
      total: 0.52
      efficiency: 0.39
      win: 0.68
      pick: 0.44
      fit: 0.39
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.63
      pick: 0.39
      fit: 0.23
    Draconic Scale:
      total: 0.63
      efficiency: 0.5
      win: 0.86
      pick: 0.31
      fit: 0.35
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix,
    Golden Blade, Runeforged Hammer, Shield Splitter, Berserker''s Shield, Eye of
    the Storm, Breastplate of Valor, The Reaper, Yogi''s Necklace, Pharaoh''s Curse,
    Lernaean Bow, Tyrfing, Riptalon, Erosion, Shogun''s Ofuda, Phoenix Feather, Eye
    of Providence, Avenging Blade, Hydra''s Lament, Chandra''s Grace, Stone of Binding,
    Daybreak Gavel, Midgardian Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.14
      fit: 0.54
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.39
      win: 0.68
      pick: 0.44
      fit: 0.43
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.39
      fit: 0.3
    Draconic Scale:
      total: 0.64
      efficiency: 0.5
      win: 0.86
      pick: 0.31
      fit: 0.44
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Kinetic Cuirass
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Amanita Charm, Heartseeker, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Kinetic Cuirass, Runeforged Hammer, Golden
    Blade, Screeching Gargoyle, Void Shield, Toxic Blade, Titan''s Bane, Void Stone,
    The Crusher, Breastplate of Valor, Lernaean Bow, The Reaper, Tyrfing, Shield Splitter,
    Berserker''s Shield, Hydra''s Lament, Riptalon, Eye of the Storm, Pharaoh''s Curse,
    Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.48
    Gladiator's Shield:
      total: 0.51
      efficiency: 0.39
      win: 0.68
      pick: 0.44
      fit: 0.31
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.63
      pick: 0.39
      fit: 0.17
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.86
      pick: 0.31
      fit: 0.26
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Tyrfing
  - Freya's Tears
  - Draconic Scale
  - Riptalon
  flex_slots:
  - Tyrfing
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Golden Blade, Amanita Charm, Tyrfing, Kinetic Cuirass,
    Riptalon, Runeforged Hammer, Lernaean Bow, Berserker''s Shield, Silverbranch Bow,
    Breastplate of Valor, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda, Shield Splitter,
    Eye of the Storm, Hydra''s Lament, Tekko-Kagi, The Reaper, Daybreak Gavel, Avenging
    Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence, Heartseeker,
    Vital Amplifier.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.18
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.63
      pick: 0.39
      fit: 0.17
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.86
      pick: 0.31
      fit: 0.26
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic Cuirass,
    Screeching Gargoyle, Runeforged Hammer, Golden Blade, Berserker''s Shield, Arondight,
    Lernaean Bow, Pharaoh''s Curse, Tyrfing, Shield Splitter, Daybreak Gavel, Eye
    of Erebus, Shogun''s Ofuda, Eye of the Storm, Chandra''s Grace, Silverbranch Bow,
    Erosion, Avenging Blade, Eye of Providence, Stone of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.4
    Gladiator's Shield:
      total: 0.55
      efficiency: 0.39
      win: 0.68
      pick: 0.44
      fit: 0.57
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.39
      fit: 0.43
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.86
      pick: 0.31
      fit: 0.26
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
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
    Underrated for this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Golden Blade, Runeforged Hammer, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield
    Splitter, Eye of the Storm, Breastplate of Valor, Pharaoh''s Curse, Avenging Blade,
    Hydra''s Lament, Shogun''s Ofuda, Tekko-Kagi, Heartseeker, Dominance, Deathbringer,
    Toxic Blade, Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield
    of the Phoenix, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.42
      pick: 0.14
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.55
      pick: 0.14
      fit: 0.45
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
