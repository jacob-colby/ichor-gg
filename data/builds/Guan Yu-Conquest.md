---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.69
  aspect_win_rate: 0.62
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.2
    win_rate: 0.62
    alternates:
    - name: Heartwood Charm
      pick_rate: 0.14
      win_rate: 0.61
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.57
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.23
      win_rate: 0.62
    - name: Chronos' Pendant
      pick_rate: 0.11
      win_rate: 0.65
  - name: Breastplate of Valor
    pick_rate: 0.23
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.65
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.48
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.74
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.57
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.77
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.48
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.53
    alternates:
    - name: Sage's Ring
      pick_rate: 0.04
      win_rate: 0.82
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.8
  community_starters:
  - name: Sands Of Time
    pick_rate: 0.3
    win_rate: 0.53
  - name: Pendulum of the Ages
    pick_rate: 0.19
    win_rate: 0.7
  - name: Bluestone Pendant
    pick_rate: 0.1
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-08-21'
  god_win_rate: 0.5725338491295938
  god_matches_won: 296
  god_matches_played: 517
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Berserker''s Shield, Kinetic Cuirass,
    Shield Splitter, Shield of the Phoenix, Runeforged Hammer, Eye of the Storm, Hydra''s
    Lament, Mantle Of Discord, Stone of Binding, Pharaoh''s Curse, Erosion, The Crusher,
    Eye of Providence, Golden Blade, Spectral Armor, Shogun''s Ofuda, Leviathan''s
    Hide, Avenging Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak, Midgardian
    Mail, Heartseeker.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.36
      fit: 0.32
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.18
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.5
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Berserker''s
    Shield, Kinetic Cuirass, The Reaper, Runeforged Hammer, Shield Splitter, Chandra''s
    Grace, Eye of the Storm, Phoenix Feather, Pharaoh''s Curse, Hydra''s Lament, Golden
    Blade, Yogi''s Necklace, Erosion, Spectral Armor, The Crusher, Eye of Providence,
    Shogun''s Ofuda, Mantle Of Discord, Stone of Binding, Avenging Blade, Glorious
    Pridwen, Leviathan''s Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.36
      fit: 0.3
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.79
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Stone of Binding, Berserker''s Shield, Amanita
    Charm, Kinetic Cuirass, The Crusher, Screeching Gargoyle, Avenging Blade, Void
    Shield, Heartseeker, The Reaper, Void Stone, Shield Splitter, Runeforged Hammer,
    Shield of the Phoenix, Tekko-Kagi, Titan''s Bane, Hydra''s Lament, Mantle Of Discord,
    Eye of the Storm, Pharaoh''s Curse, Silverbranch Bow, Spectral Armor, Erosion,
    Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.69
      pick: 0.36
      fit: 0.24
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.55
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Pharaoh''s Curse, Tyrfing, Shogun''s Ofuda, Shield of the Phoenix,
    Runeforged Hammer, Shield Splitter, Riptalon, Lernaean Bow, Mantle Of Discord,
    Stone of Binding, Silverbranch Bow, Hydra''s Lament, The Crusher, Spectral Armor,
    Toxic Blade, Erosion, Eye of the Storm, Eye of Providence, Leviathan''s Hide,
    Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.69
      pick: 0.36
      fit: 0.22
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.24
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.35
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.43
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Berserker''s Shield, Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament,
    Screeching Gargoyle, Shield Splitter, Mantle Of Discord, Stone of Binding, Runeforged
    Hammer, Pharaoh''s Curse, Prophetic Cloak, Spectral Armor, Erosion, Gladiator''s
    Shield, Eye of Providence, Chandra''s Grace, Shogun''s Ofuda, Arondight, The Crusher,
    Eye of the Storm, Leviathan''s Hide, Eye of Erebus, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.33
      fit: 0.44
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.69
      pick: 0.36
      fit: 0.44
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.18
      fit: 0.58
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Berserker''s Shield,
    Kinetic Cuirass, Shield Splitter, Shield of the Phoenix, Runeforged Hammer, Eye
    of the Storm, Hydra''s Lament, Mantle Of Discord, Stone of Binding, Pharaoh''s
    Curse, Erosion, The Crusher, Eye of Providence, Golden Blade, Spectral Armor,
    Shogun''s Ofuda, Leviathan''s Hide, Avenging Blade, Lernaean Bow, Screeching Gargoyle,
    Magi''s Cloak, Midgardian Mail, Heartseeker.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.33
      fit: 0.32
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.18
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Berserker''s Shield, Kinetic Cuirass, Shield Splitter, Shield of the Phoenix,
    Runeforged Hammer, Eye of the Storm, Hydra''s Lament, Mantle Of Discord, Stone
    of Binding, Pharaoh''s Curse, Erosion, The Crusher, Eye of Providence, Golden
    Blade, Spectral Armor, Shogun''s Ofuda, Leviathan''s Hide, Avenging Blade, Lernaean
    Bow, Screeching Gargoyle, Magi''s Cloak, Midgardian Mail, Heartseeker.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.36
      fit: 0.32
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.18
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.5
  swaps:
  - added: Breastplate of Valor
    removed: Genji's Guard
    reason: community 69% win over 119 matches (vs 57% on this god), taking the model's
      weakest slot from Genji's Guard
  starter: *id001
---
