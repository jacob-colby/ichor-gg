---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.73
  slot_order:
  - name: Golden Blade
    pick_rate: 0.22
    win_rate: 0.46
    alternates:
    - name: Tyrfing
      pick_rate: 0.14
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.59
  - name: Berserker's Shield
    pick_rate: 0.38
    win_rate: 0.6
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.16
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.67
  - name: Kinetic Cuirass
    pick_rate: 0.14
    win_rate: 0.56
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.18
      win_rate: 0.45
    - name: Hastened Fatalis
      pick_rate: 0.12
      win_rate: 0.73
  - name: Shogun's Ofuda
    pick_rate: 0.16
    win_rate: 0.42
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.5
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.73
  - name: Hastened Fatalis
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Demon Blade
      pick_rate: 0.08
      win_rate: 0.67
    - name: Shogun's Ofuda
      pick_rate: 0.06
      win_rate: 0.71
  - name: Riptalon
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.67
    - name: Hunter's Bow
      pick_rate: 0.06
      win_rate: 0.6
  community_starters:
  - name: Death's Toll
    pick_rate: 0.32
    win_rate: 0.37
  - name: Death's Embrace
    pick_rate: 0.26
    win_rate: 0.67
  - name: Sharpshooter's Arrow
    pick_rate: 0.09
    win_rate: 0.73
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-08-31'
  god_win_rate: 0.5748031496062992
  god_matches_won: 73
  god_matches_played: 127
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-31'
  god_matches_analyzed: 7103
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
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
    Berserker's Shield:
      total: 0.56
      efficiency: 0.6
      win: 0.6
      pick: 0.52
      fit: 0.38
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.22
      fit: 0.7
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.6
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
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Freya''s Tears,
    Shifter''s Shield, Runeforged Hammer, Shield Splitter, Eye of the Storm, Genji''s
    Guard, Breastplate of Valor, Erosion, The Reaper, Eye of Providence, Draconic
    Scale, Hydra''s Lament, Yogi''s Necklace, Avenging Blade, Phoenix Feather, Chandra''s
    Grace, Glorious Pridwen, Stone of Binding, Midgardian Mail, Hide of the Nemean
    Lion, Daybreak Gavel, Magi''s Cloak, Leviathan''s Hide, Heartseeker.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.6
      win: 0.6
      pick: 0.52
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.22
      fit: 0.68
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
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
    Shield Splitter, Breastplate of Valor, Shifter''s Shield, Void Stone, Runeforged
    Hammer, Titan''s Bane, The Crusher, Eye of the Storm, The Reaper, Erosion, Hydra''s
    Lament, Eye of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak,
    Pendulum Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.71
    Avenging Blade:
      total: 0.55
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.7
    Berserker's Shield:
      total: 0.55
      efficiency: 0.6
      win: 0.6
      pick: 0.52
      fit: 0.28
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Riptalon
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Freya's Tears
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Shifter''s Shield, Shield Splitter, Pharaoh''s Curse, Runeforged Hammer,
    Lernaean Bow, Tyrfing, Silverbranch Bow, Erosion, Eye of Providence, Stone of
    Binding, Toxic Blade, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament,
    Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper,
    Tekko-Kagi.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.6
      pick: 0.52
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.21
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.34
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.34
      fit: 0.44
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.38
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.45
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
  - Amanita Charm
  - Berserker's Shield
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
      win: 0.59
      pick: 0.0
      fit: 0.48
    Berserker's Shield:
      total: 0.55
      efficiency: 0.6
      win: 0.6
      pick: 0.52
      fit: 0.29
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.45
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
      win: 0.59
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.22
      fit: 0.7
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.59
      pick: 0.13
      fit: 0.6
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.6
  starter: *id001
---
