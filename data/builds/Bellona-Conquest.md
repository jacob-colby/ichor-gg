---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.5
  slot_order:
  - name: Vital Amplifier
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: Golden Blade
      pick_rate: 0.23
      win_rate: 0.33
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 1.0
  - name: Berserker's Shield
    pick_rate: 0.46
    win_rate: 0.67
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.15
      win_rate: 0.5
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.16
    win_rate: 1.0
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.24
      win_rate: 0.33
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 1.0
  - name: Shogun's Ofuda
    pick_rate: 0.33
    win_rate: 0.88
    alternates:
    - name: Riptalon
      pick_rate: 0.08
      win_rate: 0.0
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.5
  - name: Contagion
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Veve Charm
      pick_rate: 0.1
      win_rate: 0.5
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 1.0
  - name: Olmec Blue
    pick_rate: 0.13
    win_rate: 0.0
    alternates:
    - name: Agility Greaves
      pick_rate: 0.07
      win_rate: 0.0
    - name: Medal of Disruption
      pick_rate: 0.07
      win_rate: 0.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.5
    win_rate: 0.54
  - name: Death's Toll
    pick_rate: 0.35
    win_rate: 0.78
  - name: Warrior's Axe
    pick_rate: 0.12
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-09-23'
  god_win_rate: 0.5384615384615384
  god_matches_won: 14
  god_matches_played: 26
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Shogun's Ofuda
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm, Erosion, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone of
    Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching
    Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s Hide, Void Shield,
    Stampede, Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.27
    Berserker's Shield:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.63
      fit: 0.38
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.7
    Shifter's Shield:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.6
    Shogun's Ofuda:
      total: 0.63
      efficiency: 0.44
      win: 0.88
      pick: 0.55
      fit: 0.38
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Contagion
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Shogun's Ofuda
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Contagion
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Shogun's Ofuda
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Freya''s Tears,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate
    of Valor, Erosion, The Reaper, Eye of Providence, Draconic Scale, Hydra''s Lament,
    Yogi''s Necklace, Avenging Blade, Phoenix Feather, Chandra''s Grace, Glorious
    Pridwen, Stone of Binding, Midgardian Mail, Hide of the Nemean Lion, Daybreak
    Gavel, Magi''s Cloak, Leviathan''s Hide, Heartseeker.'
  slot_scores:
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.32
    Berserker's Shield:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.63
      fit: 0.4
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.68
    Shifter's Shield:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.58
    Shogun's Ofuda:
      total: 0.64
      efficiency: 0.44
      win: 0.88
      pick: 0.55
      fit: 0.4
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Contagion
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Berserker's Shield
  - Jotunn's Revenge
  - Shogun's Ofuda
  - Kinetic Cuirass
  - Shifter's Shield
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Freya''s Tears, Heartseeker, Void Shield, Genji''s Guard,
    Shield Splitter, Breastplate of Valor, Void Stone, Runeforged Hammer, Titan''s
    Bane, The Crusher, Eye of the Storm, The Reaper, Erosion, Hydra''s Lament, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak, Pendulum
    Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.22
    Berserker's Shield:
      total: 0.59
      efficiency: 0.6
      win: 0.67
      pick: 0.63
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.57
    Shogun's Ofuda:
      total: 0.62
      efficiency: 0.44
      win: 0.88
      pick: 0.55
      fit: 0.28
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.53
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.43
  community_ordered:
  - Contagion
  - Berserker's Shield
  - Shogun's Ofuda
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Berserker's Shield
  - Kinetic Cuirass
  - Shogun's Ofuda
  - Tyrfing
  - Shifter's Shield
  flex_slots:
  - Contagion
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Tyrfing, Shield Splitter, Pharaoh''s Curse, Runeforged Hammer, Lernaean
    Bow, Silverbranch Bow, Erosion, Eye of Providence, Stone of Binding, Toxic Blade,
    Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Tekko-Kagi, Riptalon.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.21
    Berserker's Shield:
      total: 0.64
      efficiency: 0.68
      win: 0.67
      pick: 0.63
      fit: 0.45
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.48
    Shogun's Ofuda:
      total: 0.66
      efficiency: 0.5
      win: 0.88
      pick: 0.55
      fit: 0.45
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.53
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.38
  community_ordered:
  - Contagion
  - Berserker's Shield
  - Kinetic Cuirass
  - Shogun's Ofuda
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Hydra''s
    Lament, Screeching Gargoyle, Shield Splitter, Prophetic Cloak, Erosion, Runeforged
    Hammer, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Hide of the
    Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.23
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.45
  community_ordered:
  - Contagion
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Shield
    Splitter, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye of the
    Storm, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s
    Lament, Stone of Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s
    Hide, Void Shield, Stampede, Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.7
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.6
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
---
