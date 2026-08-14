---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.17
  slot_order:
  - name: Golden Blade
    pick_rate: 0.31
    win_rate: 0.48
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.26
      win_rate: 0.52
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.5
  - name: Berserker's Shield
    pick_rate: 0.4
    win_rate: 0.53
    alternates:
    - name: Golden Blade
      pick_rate: 0.16
      win_rate: 0.38
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.19
    win_rate: 0.33
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.18
      win_rate: 0.71
    - name: Berserker's Shield
      pick_rate: 0.17
      win_rate: 0.31
  - name: Shogun's Ofuda
    pick_rate: 0.14
    win_rate: 0.36
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.16
      win_rate: 0.42
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.56
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.2
    alternates:
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.33
    - name: Manchu Bow
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.42
    win_rate: 0.5
  - name: Death's Toll
    pick_rate: 0.4
    win_rate: 0.38
  - name: Hunter's Cowl
    pick_rate: 0.06
    win_rate: 0.8
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-08-14'
  god_win_rate: 0.4691358024691358
  god_matches_won: 38
  god_matches_played: 81
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Jotunn''s Revenge, Freya''s Tears, Shield
    Splitter, Breastplate of Valor, The Crusher, Oni Hunter''s Garb, Shield of the
    Phoenix, Erosion, Hydra''s Lament, Eye of the Storm, Runeforged Hammer, Eye of
    Providence, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Leviathan''s Hide,
    Mantle Of Discord, Stone of Binding, Midgardian Mail, Avenging Blade, Magi''s
    Cloak, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.55
      fit: 0.38
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.49
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.26
      fit: 0.6
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.6
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Genji''s Guard,
    The Crusher, Oni Hunter''s Garb, Chandra''s Grace, Runeforged Hammer, Freya''s
    Tears, Breastplate of Valor, Eye of the Storm, Hydra''s Lament, The Reaper, Shield
    Splitter, Erosion, Phoenix Feather, Eye of Providence, Spectral Armor, Draconic
    Scale, Pharaoh''s Curse, Avenging Blade, Leviathan''s Hide, Riptalon, Midgardian
    Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.3
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.55
      fit: 0.4
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.26
      fit: 0.58
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Stone of Binding
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Amanita Charm, Genji''s Guard, Stone
    of Binding, Avenging Blade, Screeching Gargoyle, Breastplate of Valor, Freya''s
    Tears, Void Shield, Oni Hunter''s Garb, Hydra''s Lament, Void Stone, The Reaper,
    Shield Splitter, Shield of the Phoenix, Runeforged Hammer, Erosion, Spectral Armor,
    Heartseeker, Eye of the Storm, Eye of Providence, Riptalon, Pharaoh''s Curse,
    Draconic Scale, Silverbranch Bow.'
  slot_scores:
    Stone of Binding:
      total: 0.5
      efficiency: 0.48
      win: 0.49
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.55
      fit: 0.28
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.57
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.51
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Shifter's Shield
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Shifter's Shield
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
    this god: Genji''s Guard, Amanita Charm, Pharaoh''s Curse, Riptalon, Breastplate
    of Valor, Jotunn''s Revenge, Freya''s Tears, The Crusher, Oni Hunter''s Garb,
    Lernaean Bow, Shield of the Phoenix, Silverbranch Bow, Hydra''s Lament, Tyrfing,
    Spectral Armor, Runeforged Hammer, Erosion, Shield Splitter, Eye of Providence,
    Draconic Scale, Eye of the Storm, Leviathan''s Hide, Midgardian Mail, Mantle Of
    Discord.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.54
      win: 0.48
      pick: 0.31
      fit: 0.56
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.21
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.53
      pick: 0.55
      fit: 0.45
    Shifter's Shield:
      total: 0.49
      efficiency: 0.52
      win: 0.52
      pick: 0.26
      fit: 0.38
    Amanita Charm:
      total: 0.5
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.38
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.57
      win: 0.49
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
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Jotunn''s Revenge, Shield of the Phoenix, Amanita Charm, Hydra''s
    Lament, Oni Hunter''s Garb, Screeching Gargoyle, The Crusher, Chandra''s Grace,
    Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic Cloak,
    Pharaoh''s Curse, Shield Splitter, Draconic Scale, Runeforged Hammer, Leviathan''s
    Hide, Eye of the Storm, Mantle Of Discord, Midgardian Mail, Stone of Binding,
    Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.48
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.55
      fit: 0.29
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.46
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.49
      pick: 0.0
      fit: 0.64
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Genji''s Guard, Jotunn''s Revenge, Freya''s
    Tears, Shield Splitter, Breastplate of Valor, The Crusher, Oni Hunter''s Garb,
    Shield of the Phoenix, Erosion, Hydra''s Lament, Eye of the Storm, Runeforged
    Hammer, Eye of Providence, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Leviathan''s
    Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail, Avenging Blade, Magi''s
    Cloak, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.55
      fit: 0.38
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.59
      win: 0.33
      pick: 0.3
      fit: 0.7
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.49
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.6
  starter: *id001
---
