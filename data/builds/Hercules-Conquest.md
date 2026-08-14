---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.23
  aspect_win_rate: 0.25
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.43
    win_rate: 0.45
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.13
      win_rate: 0.54
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 0.22
  - name: Breastplate of Valor
    pick_rate: 0.27
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.36
  - name: Genji's Guard
    pick_rate: 0.35
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.28
      win_rate: 0.45
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.15
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.25
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.67
  - name: Sage's Ring
    pick_rate: 0.06
    win_rate: 0.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.5
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.6
  - name: Hide of the Nemean Lion
    pick_rate: 0.13
    win_rate: 0.33
    alternates:
    - name: Contagion
      pick_rate: 0.07
      win_rate: 0.67
    - name: Captain's Ring
      pick_rate: 0.07
      win_rate: 0.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.46
    win_rate: 0.64
  - name: Bumba's Cudgel
    pick_rate: 0.32
    win_rate: 0.33
  - name: Bluestone Pendant
    pick_rate: 0.05
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-08-14'
  god_win_rate: 0.46601941747572817
  god_matches_won: 48
  god_matches_played: 103
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
  - Breastplate of Valor
  - Kinetic Cuirass
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Jotunn''s Revenge,
    The Crusher, Shield Splitter, Shield of the Phoenix, Oni Hunter''s Garb, Erosion,
    Eye of the Storm, Runeforged Hammer, Eye of Providence, Draconic Scale, Hydra''s
    Lament, Spectral Armor, Pharaoh''s Curse, Leviathan''s Hide, Golden Blade, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Avenging Blade, Magi''s Cloak, Ancile,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.55
      fit: 0.33
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.38
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.37
      fit: 0.33
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.54
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Jotunn''s Revenge, The Crusher, Chandra''s Grace, Runeforged Hammer, Oni
    Hunter''s Garb, Eye of the Storm, The Reaper, Shield Splitter, Erosion, Hydra''s
    Lament, Phoenix Feather, Eye of Providence, Spectral Armor, Draconic Scale, Golden
    Blade, Avenging Blade, Pharaoh''s Curse, Leviathan''s Hide, Midgardian Mail, Glorious
    Pridwen, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.55
      fit: 0.3
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.37
      fit: 0.3
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.47
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
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm,
    Avenging Blade, Stone of Binding, Berserker''s Shield, Screeching Gargoyle, Void
    Shield, Oni Hunter''s Garb, The Reaper, Void Stone, Runeforged Hammer, Shield
    of the Phoenix, Shield Splitter, Hydra''s Lament, Erosion, Spectral Armor, Eye
    of the Storm, Eye of Providence, Draconic Scale, Pharaoh''s Curse, Riptalon, Heartseeker,
    Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.55
      fit: 0.24
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.61
      pick: 0.37
      fit: 0.24
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.57
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.39
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Freya's Tears
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Golden Blade, The
    Crusher, Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, Oni Hunter''s Garb, Shield
    of the Phoenix, Shogun''s Ofuda, Tyrfing, Runeforged Hammer, Spectral Armor, Erosion,
    Silverbranch Bow, Lernaean Bow, Hydra''s Lament, Shield Splitter, Eye of Providence,
    Draconic Scale, Eye of the Storm, Leviathan''s Hide, Midgardian Mail, Toxic Blade.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.55
      fit: 0.21
    Berserker's Shield:
      total: 0.51
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.61
      pick: 0.37
      fit: 0.21
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.34
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
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Kinetic Cuirass,
    Shield of the Phoenix, Amanita Charm, Hydra''s Lament, Berserker''s Shield, The
    Crusher, Screeching Gargoyle, Oni Hunter''s Garb, Chandra''s Grace, Gladiator''s
    Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic Cloak, Shield Splitter,
    Draconic Scale, Runeforged Hammer, Pharaoh''s Curse, Eye of the Storm, Leviathan''s
    Hide, Midgardian Mail, Mantle Of Discord, Stone of Binding, Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.5
      pick: 0.55
      fit: 0.48
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.64
      win: 0.61
      pick: 0.37
      fit: 0.48
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.15
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Jotunn''s Revenge, The Crusher, Shield Splitter, Shield of the Phoenix, Oni Hunter''s
    Garb, Erosion, Eye of the Storm, Runeforged Hammer, Eye of Providence, Draconic
    Scale, Hydra''s Lament, Spectral Armor, Pharaoh''s Curse, Leviathan''s Hide, Golden
    Blade, Midgardian Mail, Mantle Of Discord, Stone of Binding, Avenging Blade, Magi''s
    Cloak, Ancile, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.55
      fit: 0.33
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.54
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Erosion, Kinetic Cuirass, Spectral Armor, Shield of the
    Phoenix, Pharaoh''s Curse, Berserker''s Shield, Shogun''s Ofuda, Void Shield,
    Doublet of Binding, The Crusher, Jotunn''s Revenge, Runeforged Hammer, Oni Hunter''s
    Garb, Stampede, Void Stone, Eye of the Storm, Eye of Providence, Shield Splitter,
    Chandra''s Grace, Draconic Scale, Mystical Mail, Hydra''s Lament, Umbral Link,
    Golden Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.55
      fit: 0.29
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.37
      fit: 0.29
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.71
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.48
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.53
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.91
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shield of the Phoenix
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Erosion, Kinetic Cuirass, Spectral
    Armor, Pharaoh''s Curse, Berserker''s Shield, Jotunn''s Revenge, The Crusher,
    Shogun''s Ofuda, Chandra''s Grace, Void Shield, Doublet of Binding, Runeforged
    Hammer, Oni Hunter''s Garb, Eye of the Storm, Stampede, The Reaper, Umbral Link,
    Void Stone, Shield Splitter, Hydra''s Lament, Phoenix Feather, Eye of Providence,
    Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.55
      fit: 0.3
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.37
      fit: 0.3
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.47
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.52
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.88
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Void Shield
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Void Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Void Shield, The Crusher, Jotunn''s Revenge, Void
    Stone, Spectral Armor, Erosion, Kinetic Cuirass, Shield of the Phoenix, Pharaoh''s
    Curse, The Reaper, Avenging Blade, Berserker''s Shield, Shogun''s Ofuda, Doublet
    of Binding, Stone of Binding, Screeching Gargoyle, Oni Hunter''s Garb, Riptalon,
    Stampede, Runeforged Hammer, Chandra''s Grace, Umbral Link, Eye of the Storm,
    Hydra''s Lament.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.55
      fit: 0.21
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.61
      pick: 0.37
      fit: 0.21
    Void Shield:
      total: 0.52
      efficiency: 0.46
      win: 0.47
      pick: 0.0
      fit: 1.0
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.35
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.95
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Freya's Tears
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Berserker's Shield
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Pharaoh''s Curse, Berserker''s Shield, Shogun''s Ofuda,
    Spectral Armor, Erosion, Kinetic Cuirass, Riptalon, Shield of the Phoenix, Golden
    Blade, Eros'' Bow, Void Shield, Doublet of Binding, The Crusher, Umbral Link,
    Oni Hunter''s Garb, Stampede, Void Stone, Jotunn''s Revenge, Chandra''s Grace,
    Runeforged Hammer, The Reaper, Mystical Mail, Tyrfing, Eye of Providence.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.61
      pick: 0.37
      fit: 0.19
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.31
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.5
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.78
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield of the Phoenix,
    Spectral Armor, Erosion, Kinetic Cuirass, Chandra''s Grace, Jotunn''s Revenge,
    Pharaoh''s Curse, Berserker''s Shield, Shogun''s Ofuda, Hydra''s Lament, Void
    Shield, Doublet of Binding, Oni Hunter''s Garb, Stampede, Void Stone, The Crusher,
    Gladiator''s Shield, Screeching Gargoyle, Umbral Link, Runeforged Hammer, Mystical
    Mail, Eye of Providence, Glorious Pridwen, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.5
      pick: 0.55
      fit: 0.45
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.61
      pick: 0.37
      fit: 0.45
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.59
    Spectral Armor:
      total: 0.51
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.97
    Erosion:
      total: 0.51
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Shield of the Phoenix
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Erosion, Kinetic Cuirass, Spectral Armor,
    Shield of the Phoenix, Pharaoh''s Curse, Berserker''s Shield, Shogun''s Ofuda,
    Void Shield, Doublet of Binding, The Crusher, Jotunn''s Revenge, Runeforged Hammer,
    Oni Hunter''s Garb, Stampede, Void Stone, Eye of the Storm, Eye of Providence,
    Shield Splitter, Chandra''s Grace, Draconic Scale, Mystical Mail, Hydra''s Lament,
    Umbral Link, Golden Blade.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.74
    Spectral Armor:
      total: 0.52
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.53
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.91
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.73
  starter: *id001
  aspect: Aspect of Preservation
---
