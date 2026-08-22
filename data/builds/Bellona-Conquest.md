---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.31
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.28
    win_rate: 0.51
    alternates:
    - name: Golden Blade
      pick_rate: 0.23
      win_rate: 0.46
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.51
  - name: Berserker's Shield
    pick_rate: 0.32
    win_rate: 0.53
    alternates:
    - name: Golden Blade
      pick_rate: 0.16
      win_rate: 0.56
    - name: Shogun's Ofuda
      pick_rate: 0.14
      win_rate: 0.4
  - name: Shogun's Ofuda
    pick_rate: 0.18
    win_rate: 0.59
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.41
    - name: Kinetic Cuirass
      pick_rate: 0.15
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.16
    win_rate: 0.36
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.13
      win_rate: 0.57
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 0.65
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.7
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.63
  - name: Manchu Bow
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.43
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.44
    win_rate: 0.58
  - name: Death's Toll
    pick_rate: 0.36
    win_rate: 0.4
  - name: Hunter's Cowl
    pick_rate: 0.06
    win_rate: 0.71
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-08-22'
  god_win_rate: 0.4852459016393443
  god_matches_won: 148
  god_matches_played: 305
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm, Shield of the
    Phoenix, Mantle Of Discord, Erosion, Stone of Binding, Eye of Providence, Draconic
    Scale, The Crusher, Spectral Armor, Hydra''s Lament, Leviathan''s Hide, Magi''s
    Cloak, Pharaoh''s Curse, Avenging Blade, Midgardian Mail, Screeching Gargoyle,
    Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.44
      fit: 0.38
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.67
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.63
      pick: 0.15
      fit: 0.38
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
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
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Hide of the Nemean Lion
  - Shogun's Ofuda
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
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Freya''s Tears,
    Runeforged Hammer, Shield Splitter, The Reaper, Eye of the Storm, Genji''s Guard,
    Breastplate of Valor, Phoenix Feather, Chandra''s Grace, Erosion, Eye of Providence,
    Draconic Scale, Spectral Armor, Hydra''s Lament, The Crusher, Yogi''s Necklace,
    Avenging Blade, Mantle Of Discord, Stone of Binding, Leviathan''s Hide, Pharaoh''s
    Curse, Glorious Pridwen, Riptalon.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.44
      fit: 0.4
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.82
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.63
      pick: 0.15
      fit: 0.4
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.88
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.53
      win: 0.59
      pick: 0.28
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Stone of Binding, Amanita Charm, The Crusher,
    Avenging Blade, Screeching Gargoyle, Freya''s Tears, Heartseeker, Void Shield,
    Genji''s Guard, Shield Splitter, The Reaper, Breastplate of Valor, Void Stone,
    Runeforged Hammer, Shield of the Phoenix, Titan''s Bane, Mantle Of Discord, Eye
    of the Storm, Erosion, Hydra''s Lament, Tekko-Kagi, Spectral Armor, Eye of Providence,
    Silverbranch Bow, Draconic Scale.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.71
    Avenging Blade:
      total: 0.52
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.7
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.44
      fit: 0.28
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.57
    The Crusher:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Hide of the Nemean Lion
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Genji''s Guard, Pharaoh''s
    Curse, Breastplate of Valor, Tyrfing, Shield Splitter, Shield of the Phoenix,
    Mantle Of Discord, Stone of Binding, Runeforged Hammer, Riptalon, Lernaean Bow,
    Silverbranch Bow, Spectral Armor, Erosion, The Crusher, Eye of Providence, Toxic
    Blade, Eye of the Storm, Hydra''s Lament, Draconic Scale, Leviathan''s Hide, Magi''s
    Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.53
      pick: 0.44
      fit: 0.45
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.21
    Hide of the Nemean Lion:
      total: 0.51
      efficiency: 0.52
      win: 0.63
      pick: 0.15
      fit: 0.24
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.38
    Pharaoh's Curse:
      total: 0.5
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.45
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.53
      win: 0.59
      pick: 0.28
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
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Lament, Screeching Gargoyle, Shield Splitter, Mantle Of Discord, Stone of Binding,
    Prophetic Cloak, Erosion, Runeforged Hammer, Eye of Providence, Gladiator''s Shield,
    Spectral Armor, Draconic Scale, Chandra''s Grace, Eye of the Storm, Arondight,
    Leviathan''s Hide, Pharaoh''s Curse, The Crusher, Magi''s Cloak, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.48
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.44
      fit: 0.29
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Shield
    Splitter, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye of the
    Storm, Shield of the Phoenix, Mantle Of Discord, Erosion, Stone of Binding, Eye
    of Providence, Draconic Scale, The Crusher, Spectral Armor, Hydra''s Lament, Leviathan''s
    Hide, Magi''s Cloak, Pharaoh''s Curse, Avenging Blade, Midgardian Mail, Screeching
    Gargoyle, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.44
      fit: 0.38
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.6
      win: 0.36
      pick: 0.27
      fit: 0.7
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.6
  starter: *id001
---
