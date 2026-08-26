---
type: smite-build
god: Cu Chulainn
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Warped
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.59
    win_rate: 0.5
    alternates:
    - name: Mystical Mail
      pick_rate: 0.24
      win_rate: 0.47
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.4
  - name: Gladiator's Shield
    pick_rate: 0.22
    win_rate: 0.41
    alternates:
    - name: Mystical Mail
      pick_rate: 0.18
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.55
    - name: Gladiator's Shield
      pick_rate: 0.13
      win_rate: 0.2
  - name: Shell of Rebuke
    pick_rate: 0.23
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.89
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.57
  - name: Draconic Scale
    pick_rate: 0.19
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.5
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.75
  - name: Contagion
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Draconic Scale
      pick_rate: 0.09
      win_rate: 0.5
    - name: Olmec Blue
      pick_rate: 0.09
      win_rate: 0.25
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.41
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.38
    win_rate: 0.5
  - name: Sundering Axe
    pick_rate: 0.08
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/cu-chulainn/
  last_verified: '2026-08-26'
  god_win_rate: 0.5
  god_matches_won: 39
  god_matches_played: 78
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Golden Blade,
    Runeforged Hammer, Lernaean Bow, Shield Splitter, Tyrfing, Eye of the Storm, Pharaoh''s
    Curse, Hydra''s Lament, Avenging Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance,
    Heartseeker, Deathbringer, Erosion, Daybreak Gavel, Eye of Providence, Shield
    of the Phoenix, Silverbranch Bow, Toxic Blade, Stone of Binding, Breastplate of
    Valor.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.24
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.75
      pick: 0.28
      fit: 0.44
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.59
      fit: 0.34
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Contagion
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, Runeforged Hammer, Golden Blade, Shield Splitter, Eye of the Storm, The
    Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean Bow, Erosion, Shogun''s Ofuda,
    Phoenix Feather, Eye of Providence, Tyrfing, Avenging Blade, Riptalon, Hydra''s
    Lament, Chandra''s Grace, Stone of Binding, Daybreak Gavel, Midgardian Mail, Breastplate
    of Valor.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.27
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.47
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.75
      pick: 0.28
      fit: 0.54
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.59
      fit: 0.44
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Amanita Charm
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
    for this god: Jotunn''s Revenge, Berserker''s Shield, Avenging Blade, Amanita
    Charm, Heartseeker, Tekko-Kagi, Stone of Binding, Silverbranch Bow, Screeching
    Gargoyle, Runeforged Hammer, Void Shield, Titan''s Bane, Golden Blade, The Crusher,
    Toxic Blade, Void Stone, Lernaean Bow, The Reaper, Shield Splitter, Tyrfing, Hydra''s
    Lament, Eye of the Storm, Riptalon, Pharaoh''s Curse, Avatar''s Parashu, Breastplate
    of Valor.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.2
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.75
      pick: 0.28
      fit: 0.35
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.25
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
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
    this god: Berserker''s Shield, Jotunn''s Revenge, Golden Blade, Amanita Charm,
    Tyrfing, Riptalon, Lernaean Bow, Runeforged Hammer, Silverbranch Bow, Pharaoh''s
    Curse, Toxic Blade, Shogun''s Ofuda, Shield Splitter, Tekko-Kagi, Hydra''s Lament,
    The Reaper, Eye of the Storm, Daybreak Gavel, Dominance, Avenging Blade, Erosion,
    Heartseeker, Shield of the Phoenix, Qin''s Blade, Stone of Binding, Breastplate
    of Valor.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.2
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.18
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.75
      pick: 0.28
      fit: 0.35
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Screeching Gargoyle, Runeforged
    Hammer, Breastplate of Valor, Golden Blade, Arondight, Lernaean Bow, Pharaoh''s
    Curse, Shield Splitter, Eye of Erebus, Tyrfing, Daybreak Gavel, Shogun''s Ofuda,
    Eye of the Storm, Prophetic Cloak, Chandra''s Grace, Erosion, Avenging Blade,
    Eye of Providence, Silverbranch Bow, Stone of Binding.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.2
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 0.36
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.75
      pick: 0.28
      fit: 0.34
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.28
      fit: 0.43
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Golden Blade, Runeforged Hammer, Lernaean Bow, Shield Splitter, Tyrfing, Eye of
    the Storm, Breastplate of Valor, Pharaoh''s Curse, Hydra''s Lament, Avenging Blade,
    Tekko-Kagi, Shogun''s Ofuda, Dominance, Heartseeker, Deathbringer, Erosion, Daybreak
    Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch Bow, Toxic Blade,
    Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.75
      pick: 0.28
      fit: 0.44
    Runeforged Hammer:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
  starter: *id001
---
