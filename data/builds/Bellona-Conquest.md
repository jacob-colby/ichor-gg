---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.26
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.33
    win_rate: 0.52
    alternates:
    - name: Golden Blade
      pick_rate: 0.25
      win_rate: 0.47
    - name: Berserker's Shield
      pick_rate: 0.14
      win_rate: 0.42
  - name: Berserker's Shield
    pick_rate: 0.36
    win_rate: 0.53
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.17
      win_rate: 0.35
    - name: Golden Blade
      pick_rate: 0.16
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.19
    win_rate: 0.38
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.19
      win_rate: 0.64
    - name: Berserker's Shield
      pick_rate: 0.16
      win_rate: 0.27
  - name: Shogun's Ofuda
    pick_rate: 0.16
    win_rate: 0.45
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.17
      win_rate: 0.36
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.64
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 0.54
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.43
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.2
    alternates:
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.2
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.8
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.46
    win_rate: 0.52
  - name: Death's Toll
    pick_rate: 0.37
    win_rate: 0.43
  - name: Bumba's Spear
    pick_rate: 0.07
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-08-16'
  god_win_rate: 0.47101449275362317
  god_matches_won: 65
  god_matches_played: 138
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
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
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Freya''s Tears, Jotunn''s Revenge, The
    Crusher, Shield Splitter, Shield of the Phoenix, Oni Hunter''s Garb, Breastplate
    of Valor, Erosion, Eye of the Storm, Runeforged Hammer, Eye of Providence, Draconic
    Scale, Hydra''s Lament, Spectral Armor, Pharaoh''s Curse, Leviathan''s Hide, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Avenging Blade, Magi''s Cloak, Ancile,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.47
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.49
      fit: 0.38
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.38
      pick: 0.3
      fit: 0.7
    Freya's Tears:
      total: 0.5
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.33
      fit: 0.6
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.47
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
  - Genji's Guard
  - Jotunn's Revenge
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Genji''s Guard, Jotunn''s Revenge,
    The Crusher, Chandra''s Grace, Runeforged Hammer, Freya''s Tears, Oni Hunter''s
    Garb, Eye of the Storm, The Reaper, Shield Splitter, Erosion, Breastplate of Valor,
    Hydra''s Lament, Phoenix Feather, Eye of Providence, Spectral Armor, Draconic
    Scale, Avenging Blade, Pharaoh''s Curse, Leviathan''s Hide, Midgardian Mail, Glorious
    Pridwen, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.47
      pick: 0.0
      fit: 0.3
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.49
      fit: 0.4
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.33
      fit: 0.58
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
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
    for this god: The Crusher, Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Avenging
    Blade, Stone of Binding, Screeching Gargoyle, Freya''s Tears, Void Shield, Breastplate
    of Valor, Oni Hunter''s Garb, The Reaper, Void Stone, Runeforged Hammer, Shield
    of the Phoenix, Shield Splitter, Hydra''s Lament, Erosion, Spectral Armor, Eye
    of the Storm, Eye of Providence, Draconic Scale, Pharaoh''s Curse, Riptalon, Heartseeker,
    Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.47
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.49
      fit: 0.28
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.57
    Shifter's Shield:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.33
      fit: 0.43
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.5
      efficiency: 0.63
      win: 0.47
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
  - Genji's Guard
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
    this god: Amanita Charm, Genji''s Guard, The Crusher, Pharaoh''s Curse, Freya''s
    Tears, Jotunn''s Revenge, Breastplate of Valor, Riptalon, Oni Hunter''s Garb,
    Shield of the Phoenix, Tyrfing, Runeforged Hammer, Spectral Armor, Erosion, Silverbranch
    Bow, Lernaean Bow, Hydra''s Lament, Shield Splitter, Eye of Providence, Draconic
    Scale, Eye of the Storm, Leviathan''s Hide, Midgardian Mail, Toxic Blade.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.53
      win: 0.47
      pick: 0.25
      fit: 0.56
    Genji's Guard:
      total: 0.48
      efficiency: 0.69
      win: 0.47
      pick: 0.0
      fit: 0.21
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.49
      fit: 0.45
    Shifter's Shield:
      total: 0.49
      efficiency: 0.52
      win: 0.52
      pick: 0.33
      fit: 0.38
    Amanita Charm:
      total: 0.49
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.38
    Pharaoh's Curse:
      total: 0.47
      efficiency: 0.55
      win: 0.47
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Freya''s Tears, Breastplate
    of Valor, Jotunn''s Revenge, Shield of the Phoenix, Amanita Charm, Hydra''s Lament,
    The Crusher, Screeching Gargoyle, Oni Hunter''s Garb, Chandra''s Grace, Gladiator''s
    Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic Cloak, Shield Splitter,
    Draconic Scale, Runeforged Hammer, Pharaoh''s Curse, Eye of the Storm, Leviathan''s
    Hide, Midgardian Mail, Mantle Of Discord, Stone of Binding, Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.47
      pick: 0.0
      fit: 0.48
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.49
      fit: 0.29
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.46
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.47
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
  - Freya's Tears
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Genji''s Guard, Freya''s Tears, Jotunn''s
    Revenge, The Crusher, Shield Splitter, Shield of the Phoenix, Oni Hunter''s Garb,
    Breastplate of Valor, Erosion, Eye of the Storm, Runeforged Hammer, Eye of Providence,
    Draconic Scale, Hydra''s Lament, Spectral Armor, Pharaoh''s Curse, Leviathan''s
    Hide, Midgardian Mail, Mantle Of Discord, Stone of Binding, Avenging Blade, Magi''s
    Cloak, Ancile, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.47
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.49
      fit: 0.38
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.38
      pick: 0.3
      fit: 0.7
    Freya's Tears:
      total: 0.5
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.6
  starter: *id001
---
