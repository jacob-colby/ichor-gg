---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.33
  slot_order:
  - name: Vital Amplifier
    pick_rate: 0.24
    win_rate: 0.67
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.22
      win_rate: 0.26
    - name: Berserker's Shield
      pick_rate: 0.16
      win_rate: 0.71
  - name: Berserker's Shield
    pick_rate: 0.35
    win_rate: 0.43
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.67
    - name: Vital Amplifier
      pick_rate: 0.12
      win_rate: 0.5
  - name: Shogun's Ofuda
    pick_rate: 0.22
    win_rate: 0.67
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.44
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.11
    win_rate: 0.22
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.13
      win_rate: 0.6
    - name: Berserker's Shield
      pick_rate: 0.13
      win_rate: 0.6
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.29
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.11
      win_rate: 0.2
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.5
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.45
    win_rate: 0.56
  - name: Death's Toll
    pick_rate: 0.29
    win_rate: 0.48
  - name: Hunter's Cowl
    pick_rate: 0.08
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-09-11'
  god_win_rate: 0.5465116279069767
  god_matches_won: 47
  god_matches_played: 86
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Shogun's Ofuda
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm, Erosion, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone of
    Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching
    Gargoyle, Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile, Prophetic
    Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.46
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.46
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.46
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.19
      fit: 0.6
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.34
      fit: 0.38
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Shifter's Shield
  - Shogun's Ofuda
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Vital Amplifier
  - Shifter's Shield
  - Shogun's Ofuda
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Vital Amplifier
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Freya''s Tears,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate
    of Valor, Erosion, The Reaper, Eye of Providence, Draconic Scale, Hydra''s Lament,
    Yogi''s Necklace, Avenging Blade, Phoenix Feather, Chandra''s Grace, Glorious
    Pridwen, Stone of Binding, Midgardian Mail, Golden Blade, Magi''s Cloak, Leviathan''s
    Hide, Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.46
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.46
      pick: 0.0
      fit: 0.82
    Vital Amplifier:
      total: 0.5
      efficiency: 0.43
      win: 0.67
      pick: 0.24
      fit: 0.22
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.19
      fit: 0.58
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.34
      fit: 0.4
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Vital Amplifier
  - Shifter's Shield
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Shifter's Shield
  - Shogun's Ofuda
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
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
    Stone of Binding:
      total: 0.49
      efficiency: 0.51
      win: 0.46
      pick: 0.0
      fit: 0.71
    Avenging Blade:
      total: 0.49
      efficiency: 0.49
      win: 0.46
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.46
      pick: 0.0
      fit: 0.57
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.67
      pick: 0.19
      fit: 0.43
    Shogun's Ofuda:
      total: 0.51
      efficiency: 0.44
      win: 0.67
      pick: 0.34
      fit: 0.28
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Shifter's Shield
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Vital Amplifier
  - Berserker's Shield
  - Shifter's Shield
  - Shogun's Ofuda
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Golden Blade, Genji''s
    Guard, Breastplate of Valor, Tyrfing, Shield Splitter, Pharaoh''s Curse, Runeforged
    Hammer, Riptalon, Lernaean Bow, Silverbranch Bow, Erosion, Eye of Providence,
    Stone of Binding, Toxic Blade, Eye of the Storm, Shield of the Phoenix, Hydra''s
    Lament, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, The Reaper, Tekko-Kagi.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.46
      pick: 0.0
      fit: 0.21
    Vital Amplifier:
      total: 0.53
      efficiency: 0.47
      win: 0.67
      pick: 0.24
      fit: 0.31
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.43
      pick: 0.48
      fit: 0.45
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.19
      fit: 0.38
    Shogun's Ofuda:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.34
      fit: 0.45
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Vital Amplifier
  - Berserker's Shield
  - Shifter's Shield
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Shogun's Ofuda
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Hydra''s
    Lament, Screeching Gargoyle, Shield Splitter, Prophetic Cloak, Erosion, Runeforged
    Hammer, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Chandra''s Grace, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.46
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.46
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.46
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.67
      pick: 0.19
      fit: 0.45
    Shogun's Ofuda:
      total: 0.52
      efficiency: 0.44
      win: 0.67
      pick: 0.34
      fit: 0.29
  community_ordered:
  - Shifter's Shield
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Kinetic Cuirass
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
    Mail, Screeching Gargoyle, Heartseeker, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.46
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.46
      pick: 0.0
      fit: 0.67
    Kinetic Cuirass:
      total: 0.41
      efficiency: 0.56
      win: 0.22
      pick: 0.18
      fit: 0.7
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.46
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.19
      fit: 0.6
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
---
