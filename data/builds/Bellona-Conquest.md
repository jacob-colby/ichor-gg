---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.43
  slot_order:
  - name: Berserker's Shield
    pick_rate: 0.26
    win_rate: 0.73
    alternates:
    - name: Vital Amplifier
      pick_rate: 0.26
      win_rate: 0.55
    - name: Daybreak Gavel
      pick_rate: 0.23
      win_rate: 0.2
  - name: Shifter's Shield
    pick_rate: 0.21
    win_rate: 0.56
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.33
      win_rate: 0.36
    - name: Daybreak Gavel
      pick_rate: 0.09
      win_rate: 0.5
  - name: Shogun's Ofuda
    pick_rate: 0.15
    win_rate: 0.83
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.43
    - name: Kinetic Cuirass
      pick_rate: 0.15
      win_rate: 0.33
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.2
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.16
      win_rate: 0.33
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.25
    alternates:
    - name: Veve Charm
      pick_rate: 0.08
      win_rate: 0.33
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.67
  - name: Hide of the Nemean Lion
    pick_rate: 0.14
    win_rate: 0.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.5
    - name: Shield
      pick_rate: 0.1
      win_rate: 1.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.47
    win_rate: 0.5
  - name: Death's Toll
    pick_rate: 0.33
    win_rate: 0.57
  - name: Sundering Axe
    pick_rate: 0.07
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-09-10'
  god_win_rate: 0.5348837209302325
  god_matches_won: 23
  god_matches_played: 43
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Amanita Charm
  - Shogun's Ofuda
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Shield
    Splitter, Breastplate of Valor, Runeforged Hammer, Eye of the Storm, Erosion,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone
    of Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail,
    Screeching Gargoyle, Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile,
    Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.74
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.33
    Berserker's Shield:
      total: 0.61
      efficiency: 0.6
      win: 0.73
      pick: 0.26
      fit: 0.38
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.4
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.29
      fit: 0.6
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.6
    Shogun's Ofuda:
      total: 0.6
      efficiency: 0.44
      win: 0.83
      pick: 0.23
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Shifter's Shield
  - Shogun's Ofuda
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix,
    Freya''s Tears, Runeforged Hammer, Shield Splitter, Eye of the Storm, Breastplate
    of Valor, Erosion, The Reaper, Eye of Providence, Draconic Scale, Hydra''s Lament,
    Yogi''s Necklace, Avenging Blade, Phoenix Feather, Chandra''s Grace, Glorious
    Pridwen, Stone of Binding, Midgardian Mail, Golden Blade, Magi''s Cloak, Leviathan''s
    Hide, Heartseeker.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.3
    Berserker's Shield:
      total: 0.61
      efficiency: 0.6
      win: 0.73
      pick: 0.26
      fit: 0.4
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.82
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.88
    Shogun's Ofuda:
      total: 0.6
      efficiency: 0.44
      win: 0.83
      pick: 0.23
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Genji''s Guard, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Avenging Blade, Screeching Gargoyle, Freya''s Tears, Heartseeker, Void Shield,
    Shield Splitter, Breastplate of Valor, Void Stone, Runeforged Hammer, Titan''s
    Bane, The Crusher, Eye of the Storm, The Reaper, Erosion, Hydra''s Lament, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak, Pendulum
    Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.24
    Berserker's Shield:
      total: 0.59
      efficiency: 0.6
      win: 0.73
      pick: 0.26
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.43
    Shogun's Ofuda:
      total: 0.58
      efficiency: 0.44
      win: 0.83
      pick: 0.23
      fit: 0.28
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Golden
    Blade, Breastplate of Valor, Tyrfing, Shield Splitter, Pharaoh''s Curse, Runeforged
    Hammer, Riptalon, Lernaean Bow, Silverbranch Bow, Erosion, Eye of Providence,
    Stone of Binding, Toxic Blade, Eye of the Storm, Shield of the Phoenix, Hydra''s
    Lament, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.21
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.73
      pick: 0.26
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.21
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.38
    Shogun's Ofuda:
      total: 0.63
      efficiency: 0.5
      win: 0.83
      pick: 0.23
      fit: 0.45
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
  - Shogun's Ofuda
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Freya''s Tears, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Hydra''s
    Lament, Screeching Gargoyle, Shield Splitter, Prophetic Cloak, Erosion, Runeforged
    Hammer, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Chandra''s Grace, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.76
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.48
    Berserker's Shield:
      total: 0.6
      efficiency: 0.6
      win: 0.73
      pick: 0.26
      fit: 0.29
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.64
    Shogun's Ofuda:
      total: 0.58
      efficiency: 0.44
      win: 0.83
      pick: 0.23
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
  - Freya's Tears
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
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.4
      efficiency: 0.56
      win: 0.2
      pick: 0.22
      fit: 0.7
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.67
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.29
      fit: 0.6
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
---
