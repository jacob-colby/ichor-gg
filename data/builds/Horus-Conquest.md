---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.75
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.57
    - name: Runeforged Hammer
      pick_rate: 0.15
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.83
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.57
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.76
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.65
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.61
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.55
  - name: Veve Charm
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Medallion
      pick_rate: 0.07
      win_rate: 0.56
    - name: Shield
      pick_rate: 0.07
      win_rate: 0.88
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.24
    win_rate: 0.57
  - name: Selflessness
    pick_rate: 0.18
    win_rate: 0.51
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-08-14'
  god_win_rate: 0.6045627376425855
  god_matches_won: 159
  god_matches_played: 263
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Runeforged Hammer, Berserker''s Shield,
    Freya''s Tears, Shield of the Phoenix, Oni Hunter''s Garb, Jotunn''s Revenge,
    Erosion, Eye of Providence, Draconic Scale, Spectral Armor, Pharaoh''s Curse,
    Shield Splitter, Hydra''s Lament, The Crusher, Leviathan''s Hide, Eye of the Storm,
    Midgardian Mail, Mantle Of Discord, Stone of Binding, Gladiator''s Shield, Screeching
    Gargoyle, Shogun''s Ofuda, Prophetic Cloak, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.58
      pick: 0.3
      fit: 0.42
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.76
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.15
      fit: 0.39
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.57
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
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Berserker's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Runeforged Hammer,
    Berserker''s Shield, Freya''s Tears, Chandra''s Grace, Oni Hunter''s Garb, Jotunn''s
    Revenge, Erosion, Eye of Providence, Phoenix Feather, Spectral Armor, Draconic
    Scale, Pharaoh''s Curse, Glorious Pridwen, Leviathan''s Hide, Hydra''s Lament,
    Eye of the Storm, The Crusher, Midgardian Mail, Gladiator''s Shield, Shield Splitter,
    Shogun''s Ofuda, Riptalon, The Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.58
      pick: 0.3
      fit: 0.39
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.94
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.55
      win: 0.67
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Runeforged Hammer,
    Amanita Charm, Berserker''s Shield, Stone of Binding, Screeching Gargoyle, Freya''s
    Tears, Void Shield, Oni Hunter''s Garb, Shield of the Phoenix, Avenging Blade,
    Void Stone, Erosion, Riptalon, Spectral Armor, Eye of Providence, Hydra''s Lament,
    Pharaoh''s Curse, The Reaper, Silverbranch Bow, Draconic Scale, Shield Splitter,
    Leviathan''s Hide, Heartseeker.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.58
      pick: 0.3
      fit: 0.29
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.15
      fit: 0.3
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.57
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
  - Runeforged Hammer
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Berserker''s Shield, Runeforged Hammer, Kinetic Cuirass, Amanita Charm,
    Golden Blade, Jotunn''s Revenge, Pharaoh''s Curse, Riptalon, Freya''s Tears, The
    Crusher, Oni Hunter''s Garb, Lernaean Bow, Shogun''s Ofuda, Hydra''s Lament, Shield
    of the Phoenix, Silverbranch Bow, Tyrfing, Spectral Armor, Erosion, Shield Splitter,
    Eye of Providence, Eye of the Storm, Leviathan''s Hide, Eros'' Bow, Yogi''s Necklace,
    Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.58
      pick: 0.3
      fit: 0.22
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.15
      fit: 0.32
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Runeforged Hammer
  - Freya's Tears
  flex_slots:
  - Runeforged Hammer
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Runeforged Hammer, Shield of the Phoenix, Kinetic Cuirass, Amanita Charm, Hydra''s
    Lament, Berserker''s Shield, Oni Hunter''s Garb, Screeching Gargoyle, The Crusher,
    Chandra''s Grace, Gladiator''s Shield, Erosion, Spectral Armor, Prophetic Cloak,
    Eye of Providence, Pharaoh''s Curse, Shield Splitter, Draconic Scale, Leviathan''s
    Hide, Eye of the Storm, Midgardian Mail, Arondight, Mantle Of Discord, Stone of
    Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.58
      pick: 0.3
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.2
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.47
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.61
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.15
      fit: 0.33
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.57
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
    Midgardian Mail, Mantle Of Discord, Stone of Binding, Gladiator''s Shield, Runeforged
    Hammer, Screeching Gargoyle, Shogun''s Ofuda, Prophetic Cloak, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.58
      pick: 0.3
      fit: 0.42
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.2
      fit: 0.42
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.66
  starter: *id001
---
