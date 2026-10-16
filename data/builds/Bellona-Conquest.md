---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.55
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.89
    win_rate: 0.6
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.02
      win_rate: 0.62
    - name: Vital Amplifier
      pick_rate: 0.02
      win_rate: 0.38
  - name: Sanguine Lash
    pick_rate: 0.52
    win_rate: 0.64
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.25
      win_rate: 0.57
    - name: Vital Amplifier
      pick_rate: 0.06
      win_rate: 0.55
  - name: Berserker's Shield
    pick_rate: 0.26
    win_rate: 0.59
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.23
      win_rate: 0.54
    - name: Umbral Link
      pick_rate: 0.15
      win_rate: 0.61
  - name: Kinetic Cuirass
    pick_rate: 0.17
    win_rate: 0.61
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.6
    - name: Hussar's Wings
      pick_rate: 0.11
      win_rate: 0.57
  - name: Shogun's Ofuda
    pick_rate: 0.09
    win_rate: 0.75
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.68
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 0.66
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.77
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.06
      win_rate: 0.52
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.58
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.43
    win_rate: 0.64
  - name: Death's Embrace
    pick_rate: 0.2
    win_rate: 0.67
  - name: Leather Cowl
    pick_rate: 0.19
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-10-16'
  god_win_rate: 0.5816993464052288
  god_matches_won: 445
  god_matches_played: 765
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-16'
  god_matches_analyzed: 10934
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Shield Splitter
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Shield Splitter, Shifter''s
    Shield, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament,
    Stone of Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s
    Hide, Void Shield, Stampede, Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.67
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.28
      fit: 0.7
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.6
    Shogun's Ofuda:
      total: 0.56
      efficiency: 0.44
      win: 0.75
      pick: 0.19
      fit: 0.38
  community_ordered:
  - Kinetic Cuirass
  - Shogun's Ofuda
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Freya''s Tears,
    Runeforged Hammer, Shield Splitter, Shifter''s Shield, Eye of the Storm, Genji''s
    Guard, Breastplate of Valor, Erosion, The Reaper, Eye of Providence, Draconic
    Scale, Hydra''s Lament, Yogi''s Necklace, Avenging Blade, Phoenix Feather, Chandra''s
    Grace, Glorious Pridwen, Stone of Binding, Daybreak Gavel, Midgardian Mail, Hide
    of the Nemean Lion, Golden Blade, Magi''s Cloak, Leviathan''s Hide, Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.82
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.28
      fit: 0.68
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.88
    Shogun's Ofuda:
      total: 0.56
      efficiency: 0.44
      win: 0.75
      pick: 0.19
      fit: 0.4
  community_ordered:
  - Kinetic Cuirass
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Freya''s Tears, Heartseeker, Void Shield, Genji''s Guard,
    Shield Splitter, Breastplate of Valor, Void Stone, Shifter''s Shield, Runeforged
    Hammer, Titan''s Bane, The Crusher, Eye of the Storm, The Reaper, Erosion, Hydra''s
    Lament, Eye of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak,
    Pendulum Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.71
    Avenging Blade:
      total: 0.55
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.57
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.61
      pick: 0.28
      fit: 0.53
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
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
    Guard, Breastplate of Valor, Tyrfing, Shifter''s Shield, Shield Splitter, Pharaoh''s
    Curse, Runeforged Hammer, Riptalon, Lernaean Bow, Silverbranch Bow, Erosion, Eye
    of Providence, Stone of Binding, Toxic Blade, Eye of the Storm, Shield of the
    Phoenix, Hydra''s Lament, Draconic Scale, Daybreak Gavel, Magi''s Cloak, Screeching
    Gargoyle, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.21
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.59
      pick: 0.4
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.28
      fit: 0.48
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.38
    Shogun's Ofuda:
      total: 0.59
      efficiency: 0.5
      win: 0.75
      pick: 0.19
      fit: 0.45
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Hydra''s
    Lament, Screeching Gargoyle, Shifter''s Shield, Shield Splitter, Prophetic Cloak,
    Erosion, Runeforged Hammer, Eye of Providence, Gladiator''s Shield, Draconic Scale,
    Stone of Binding, Eye of the Storm, Arondight, Magi''s Cloak, Daybreak Gavel,
    Eye of Erebus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Chandra''s
    Grace, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.61
      pick: 0.28
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Kinetic Cuirass
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
    Splitter, Shifter''s Shield, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Eye of the Storm, Erosion, Eye of Providence, Draconic Scale, Shield of
    the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s Cloak, Avenging Blade,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion,
    Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile, Prophetic Cloak,
    Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.67
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.28
      fit: 0.7
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Sanguine Lash
  - Kinetic Cuirass
  - Shell of Rebuke
  - Shogun's Ofuda
  flex_slots:
  - Sanguine Lash
  - Shell of Rebuke
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Jotunn''s Revenge,
    Freya''s Tears, Shield Splitter, Shifter''s Shield, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Eye of the Storm, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s Cloak,
    Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide
    of the Nemean Lion, Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile,
    Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.4
    Sanguine Lash:
      total: 0.53
      efficiency: 0.36
      win: 0.64
      pick: 0.71
      fit: 0.55
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.28
      fit: 0.7
    Shell of Rebuke:
      total: 0.52
      efficiency: 0.28
      win: 0.77
      pick: 0.15
      fit: 0.43
    Shogun's Ofuda:
      total: 0.56
      efficiency: 0.44
      win: 0.75
      pick: 0.19
      fit: 0.38
  community_ordered:
  - Sanguine Lash
  - Kinetic Cuirass
  - Shell of Rebuke
  - Shogun's Ofuda
  swaps:
  - added: Shogun's Ofuda
    removed: Shifter's Shield
    reason: community 75% win over 69 matches (vs 58% on this god), taking the model's
      weakest slot from Shifter's Shield
  - added: Shell of Rebuke
    removed: Shield Splitter
    reason: community 77% win over 38 matches (vs 58% on this god), taking the model's
      weakest slot from Shield Splitter
  - added: Sanguine Lash
    removed: Freya's Tears
    reason: community 64% win over 398 matches (vs 58% on this god), taking the model's
      weakest slot from Freya's Tears
  starter: *id001
---
