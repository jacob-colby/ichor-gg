---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.63
  aspect_win_rate: 0.69
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.2
    win_rate: 0.6
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.16
      win_rate: 0.38
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.43
  - name: Breastplate of Valor
    pick_rate: 0.25
    win_rate: 0.77
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.78
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.24
      win_rate: 0.92
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.25
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.73
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.75
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.75
    alternates:
    - name: Veve Charm
      pick_rate: 0.09
      win_rate: 0.5
    - name: Draconic Scale
      pick_rate: 0.09
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.11
    win_rate: 1.0
    alternates:
    - name: Olmec Blue
      pick_rate: 0.11
      win_rate: 0.67
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Sands Of Time
    pick_rate: 0.22
    win_rate: 0.64
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.5
  - name: Pendulum of the Ages
    pick_rate: 0.2
    win_rate: 0.8
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-08-13'
  god_win_rate: 0.6078431372549019
  god_matches_won: 31
  god_matches_played: 51
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Jotunn''s Revenge,
    The Crusher, Hydra''s Lament, Shield of the Phoenix, Oni Hunter''s Garb, Pharaoh''s
    Curse, Shield Splitter, Runeforged Hammer, Golden Blade, Eye of the Storm, Erosion,
    Eye of Providence, Spectral Armor, Lernaean Bow, Shogun''s Ofuda, Leviathan''s
    Hide, Midgardian Mail, Avenging Blade, Mantle Of Discord, Stone of Binding, Damaru.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.66
      win: 0.77
      pick: 0.34
      fit: 0.32
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.64
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.75
      pick: 0.19
      fit: 0.49
    Draconic Scale:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.64
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
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Berserker''s Shield, Kinetic Cuirass,
    Jotunn''s Revenge, Chandra''s Grace, The Crusher, Oni Hunter''s Garb, Hydra''s
    Lament, Runeforged Hammer, Pharaoh''s Curse, The Reaper, Golden Blade, Riptalon,
    Eye of the Storm, Phoenix Feather, Shield Splitter, Erosion, Spectral Armor, Eye
    of Providence, Shogun''s Ofuda, Lernaean Bow, Leviathan''s Hide, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.66
      win: 0.77
      pick: 0.34
      fit: 0.3
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.79
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.75
      pick: 0.19
      fit: 0.45
    Draconic Scale:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.5
    Amanita Charm:
      total: 0.63
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Berserker''s Shield, Kinetic Cuirass,
    Amanita Charm, Avenging Blade, Screeching Gargoyle, Stone of Binding, Void Shield,
    Hydra''s Lament, Oni Hunter''s Garb, Shield of the Phoenix, Riptalon, Void Stone,
    Runeforged Hammer, Pharaoh''s Curse, The Reaper, Silverbranch Bow, Shield Splitter,
    Golden Blade, Spectral Armor, Heartseeker, Erosion, Lernaean Bow, Eye of the Storm.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.77
      pick: 0.34
      fit: 0.24
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.64
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.75
      pick: 0.19
      fit: 0.37
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.38
    The Crusher:
      total: 0.59
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
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
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Golden Blade, Jotunn''s
    Revenge, Pharaoh''s Curse, Riptalon, The Crusher, Oni Hunter''s Garb, Lernaean
    Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Silverbranch Bow,
    Tyrfing, Runeforged Hammer, Spectral Armor, Erosion, Shield Splitter, Eye of Providence,
    Eye of the Storm, Leviathan''s Hide, Eros'' Bow, Yogi''s Necklace.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.54
      win: 0.64
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.77
      pick: 0.34
      fit: 0.22
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.75
      pick: 0.19
      fit: 0.34
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.35
    Pharaoh's Curse:
      total: 0.55
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Berserker's Shield
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield,
    Shield of the Phoenix, Kinetic Cuirass, Amanita Charm, Hydra''s Lament, Oni Hunter''s
    Garb, The Crusher, Screeching Gargoyle, Pharaoh''s Curse, Chandra''s Grace, Gladiator''s
    Shield, Spectral Armor, Erosion, Runeforged Hammer, Eye of Providence, Prophetic
    Cloak, Shield Splitter, Shogun''s Ofuda, Golden Blade, Leviathan''s Hide, Eye
    of the Storm, Lernaean Bow, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.66
      efficiency: 0.66
      win: 0.77
      pick: 0.34
      fit: 0.44
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.0
      fit: 0.43
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.64
      efficiency: 0.59
      win: 0.75
      pick: 0.19
      fit: 0.58
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.34
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
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm,
    Jotunn''s Revenge, The Crusher, Hydra''s Lament, Shield of the Phoenix, Oni Hunter''s
    Garb, Pharaoh''s Curse, Shield Splitter, Runeforged Hammer, Golden Blade, Eye
    of the Storm, Erosion, Eye of Providence, Spectral Armor, Lernaean Bow, Shogun''s
    Ofuda, Leviathan''s Hide, Midgardian Mail, Avenging Blade, Mantle Of Discord,
    Stone of Binding, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.19
      fit: 0.32
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.64
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.75
      pick: 0.19
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.5
  starter: *id001
---
