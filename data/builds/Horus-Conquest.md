---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.1
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.35
    win_rate: 0.59
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.17
      win_rate: 0.62
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.57
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.52
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.68
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.58
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.62
  - name: Dwarven Plate
    pick_rate: 0.05
    win_rate: 0.64
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.61
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.6
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Legionnaire Armor
      pick_rate: 0.06
      win_rate: 0.69
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.39
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.26
    win_rate: 0.55
  - name: Selflessness
    pick_rate: 0.19
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-08-10'
  god_win_rate: 0.5846917080085046
  god_matches_won: 825
  god_matches_played: 1411
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
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
    this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Freya''s Tears,
    Shield of the Phoenix, Oni Hunter''s Garb, Jotunn''s Revenge, Erosion, Eye of
    Providence, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Shield Splitter,
    Hydra''s Lament, The Crusher, Leviathan''s Hide, Eye of the Storm, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Gladiator''s Shield, Screeching Gargoyle,
    Shogun''s Ofuda, Prophetic Cloak, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.42
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.59
      pick: 0.35
      fit: 0.66
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.66
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Freya''s Tears, Chandra''s Grace, Oni Hunter''s Garb, Jotunn''s Revenge,
    Erosion, Eye of Providence, Phoenix Feather, Draconic Scale, Spectral Armor, Pharaoh''s
    Curse, Glorious Pridwen, Leviathan''s Hide, Hydra''s Lament, Eye of the Storm,
    The Crusher, Midgardian Mail, Gladiator''s Shield, Shield Splitter, Shogun''s
    Ofuda, Riptalon, The Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.39
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.94
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.59
      pick: 0.35
      fit: 0.66
    Amanita Charm:
      total: 0.63
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Amanita Charm,
    Berserker''s Shield, Stone of Binding, Screeching Gargoyle, Freya''s Tears, Void
    Shield, Oni Hunter''s Garb, Shield of the Phoenix, Avenging Blade, Void Stone,
    Erosion, Riptalon, Spectral Armor, Eye of Providence, Hydra''s Lament, Pharaoh''s
    Curse, The Reaper, Silverbranch Bow, Draconic Scale, Shield Splitter, Leviathan''s
    Hide, Heartseeker.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.29
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Golden Blade, Jotunn''s
    Revenge, Pharaoh''s Curse, Riptalon, Freya''s Tears, The Crusher, Oni Hunter''s
    Garb, Lernaean Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Silverbranch
    Bow, Tyrfing, Spectral Armor, Erosion, Shield Splitter, Eye of Providence, Eye
    of the Storm, Draconic Scale, Leviathan''s Hide, Eros'' Bow, Yogi''s Necklace.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.54
      win: 0.59
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.22
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.35
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Shield of the Phoenix, Kinetic Cuirass, Amanita Charm, Hydra''s Lament, Berserker''s
    Shield, Oni Hunter''s Garb, Screeching Gargoyle, The Crusher, Chandra''s Grace,
    Gladiator''s Shield, Erosion, Spectral Armor, Prophetic Cloak, Eye of Providence,
    Pharaoh''s Curse, Shield Splitter, Draconic Scale, Leviathan''s Hide, Eye of the
    Storm, Midgardian Mail, Arondight, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.2
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.53
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
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
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Freya''s Tears, Shield of the Phoenix, Oni Hunter''s Garb, Jotunn''s Revenge,
    Erosion, Eye of Providence, Draconic Scale, Spectral Armor, Pharaoh''s Curse,
    Shield Splitter, Hydra''s Lament, The Crusher, Leviathan''s Hide, Eye of the Storm,
    Midgardian Mail, Mantle Of Discord, Stone of Binding, Gladiator''s Shield, Screeching
    Gargoyle, Shogun''s Ofuda, Prophetic Cloak, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.42
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.2
      fit: 0.42
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.66
  starter: *id001
---
