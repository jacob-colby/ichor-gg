---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.78
    win_rate: 0.57
    alternates:
    - name: Vital Amplifier
      pick_rate: 0.08
      win_rate: 0.56
    - name: Berserker's Shield
      pick_rate: 0.03
      win_rate: 0.2
  - name: Berserker's Shield
    pick_rate: 0.46
    win_rate: 0.55
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.26
      win_rate: 0.55
    - name: Shogun's Ofuda
      pick_rate: 0.05
      win_rate: 0.44
  - name: Sanguine Lash
    pick_rate: 0.21
    win_rate: 0.65
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.24
      win_rate: 0.59
    - name: Shogun's Ofuda
      pick_rate: 0.09
      win_rate: 0.67
  - name: Kinetic Cuirass
    pick_rate: 0.2
    win_rate: 0.54
    alternates:
    - name: Hussar's Wings
      pick_rate: 0.1
      win_rate: 0.56
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.53
  - name: Hussar's Wings
    pick_rate: 0.08
    win_rate: 0.79
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.52
    - name: Shogun's Ofuda
      pick_rate: 0.06
      win_rate: 0.4
  - name: Veve Charm
    pick_rate: 0.08
    win_rate: 0.73
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.4
    - name: Olmec Blue
      pick_rate: 0.06
      win_rate: 0.63
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.46
    win_rate: 0.67
  - name: Leather Cowl
    pick_rate: 0.18
    win_rate: 0.42
  - name: Death's Embrace
    pick_rate: 0.17
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-10-24'
  god_win_rate: 0.5384615384615384
  god_matches_won: 105
  god_matches_played: 195
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-24'
  god_matches_analyzed: 3785
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
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
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
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.67
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.54
      pick: 0.33
      fit: 0.7
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.54
    Hussar's Wings:
      total: 0.59
      efficiency: 0.39
      win: 0.79
      pick: 0.17
      fit: 0.6
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  - Hussar's Wings
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
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Freya''s Tears,
    Runeforged Hammer, Shield Splitter, Shifter''s Shield, Eye of the Storm, Genji''s
    Guard, Breastplate of Valor, Erosion, The Reaper, Eye of Providence, Draconic
    Scale, Hydra''s Lament, Yogi''s Necklace, Avenging Blade, Phoenix Feather, Chandra''s
    Grace, Glorious Pridwen, Stone of Binding, Midgardian Mail, Hide of the Nemean
    Lion, Golden Blade, Daybreak Gavel, Magi''s Cloak, Leviathan''s Hide, Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.82
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.54
      pick: 0.33
      fit: 0.68
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.47
    Hussar's Wings:
      total: 0.59
      efficiency: 0.39
      win: 0.79
      pick: 0.17
      fit: 0.58
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Kinetic Cuirass
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Hussar's Wings
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
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
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.71
    Avenging Blade:
      total: 0.55
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.57
    Hussar's Wings:
      total: 0.57
      efficiency: 0.39
      win: 0.79
      pick: 0.17
      fit: 0.43
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Hussar's Wings
  - Shogun's Ofuda
  - Amanita Charm
  flex_slots:
  - Shogun's Ofuda
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
    this god: Amanita Charm, Jotunn''s Revenge, Shogun''s Ofuda, Freya''s Tears, Golden
    Blade, Genji''s Guard, Breastplate of Valor, Tyrfing, Shifter''s Shield, Shield
    Splitter, Pharaoh''s Curse, Runeforged Hammer, Riptalon, Lernaean Bow, Silverbranch
    Bow, Erosion, Eye of Providence, Stone of Binding, Toxic Blade, Eye of the Storm,
    Shield of the Phoenix, Hydra''s Lament, Draconic Scale, Magi''s Cloak, Screeching
    Gargoyle, Daybreak Gavel, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.55
      pick: 0.63
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.21
    Hussar's Wings:
      total: 0.56
      efficiency: 0.39
      win: 0.79
      pick: 0.17
      fit: 0.38
    Shogun's Ofuda:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.14
      fit: 0.45
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Berserker's Shield
  - Hussar's Wings
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Hussar's Wings
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Hydra''s
    Lament, Screeching Gargoyle, Shifter''s Shield, Shield Splitter, Prophetic Cloak,
    Erosion, Runeforged Hammer, Eye of Providence, Gladiator''s Shield, Draconic Scale,
    Stone of Binding, Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle
    Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace,
    Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.64
    Hussar's Wings:
      total: 0.57
      efficiency: 0.39
      win: 0.79
      pick: 0.17
      fit: 0.45
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Hussar's Wings
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
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.67
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.54
      pick: 0.33
      fit: 0.7
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
