---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.46
    win_rate: 0.55
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.17
      win_rate: 0.55
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.52
  - name: Breastplate of Valor
    pick_rate: 0.29
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.52
  - name: Genji's Guard
    pick_rate: 0.31
    win_rate: 0.55
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.2
      win_rate: 0.53
    - name: Regrowth Striders
      pick_rate: 0.05
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.13
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.65
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.62
  - name: Hide of the Nemean Lion
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.46
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.57
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.86
    - name: Glorious Pridwen
      pick_rate: 0.06
      win_rate: 1.0
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-08-01'
  god_win_rate: 0.5470588235294118
  god_matches_won: 93
  god_matches_played: 170
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Glorious Pridwen
  - Runeforged Hammer
  - Shifter's Shield
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Jotunn''s Revenge,
    Berserker''s Shield, Shield Splitter, Oni Hunter''s Garb, Freya''s Tears, The
    Crusher, Hydra''s Lament, Hide of the Nemean Lion, Eye of the Storm, Shield of
    the Phoenix, Erosion, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Avenging
    Blade, Golden Blade, Yogi''s Necklace, Leviathan''s Hide, Midgardian Mail, Mantle
    Of Discord, Stone of Binding, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.31
      fit: 0.33
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.29
      fit: 0.33
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.7
    Glorious Pridwen:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.06
      fit: 0.54
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.6
      win: 0.55
      pick: 0.17
      fit: 0.51
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.46
      fit: 0.6
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Shifter's Shield
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Jotunn''s Revenge,
    Berserker''s Shield, Eye of Providence, Oni Hunter''s Garb, The Crusher, Hydra''s
    Lament, Chandra''s Grace, Eye of the Storm, Shield Splitter, The Reaper, Freya''s
    Tears, Erosion, Phoenix Feather, Spectral Armor, Avenging Blade, Golden Blade,
    Draconic Scale, Pharaoh''s Curse, Yogi''s Necklace, Leviathan''s Hide, Midgardian
    Mail, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.31
      fit: 0.3
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.29
      fit: 0.3
    Glorious Pridwen:
      total: 0.7
      efficiency: 0.36
      win: 1.0
      pick: 0.06
      fit: 0.77
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.55
      pick: 0.17
      fit: 0.57
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.46
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Glorious Pridwen
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - The Crusher
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Amanita Charm, Kinetic Cuirass,
    Berserker''s Shield, Avenging Blade, Eye of Providence, Stone of Binding, Oni
    Hunter''s Garb, Screeching Gargoyle, Hydra''s Lament, Freya''s Tears, Void Shield,
    Shield Splitter, The Reaper, Void Stone, Shield of the Phoenix, Eye of the Storm,
    Spectral Armor, Heartseeker, Erosion, Yogi''s Necklace, Pharaoh''s Curse, Draconic
    Scale, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.31
      fit: 0.24
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.29
      fit: 0.24
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.14
      fit: 0.57
    Glorious Pridwen:
      total: 0.64
      efficiency: 0.36
      win: 1.0
      pick: 0.06
      fit: 0.39
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.46
      fit: 0.43
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
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
  - Glorious Pridwen
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Golden Blade, Jotunn''s
    Revenge, Eye of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher,
    Riptalon, Freya''s Tears, Lernaean Bow, Hydra''s Lament, Shogun''s Ofuda, Tyrfing,
    Shield of the Phoenix, Silverbranch Bow, Spectral Armor, Shield Splitter, Yogi''s
    Necklace, Erosion, Eye of the Storm, Draconic Scale, Dominance, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.31
      fit: 0.21
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.29
      fit: 0.21
    Glorious Pridwen:
      total: 0.63
      efficiency: 0.36
      win: 1.0
      pick: 0.06
      fit: 0.34
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Glorious Pridwen
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s Shield, Hydra''s
    Lament, Eye of Providence, Oni Hunter''s Garb, The Crusher, Screeching Gargoyle,
    Chandra''s Grace, Gladiator''s Shield, Spectral Armor, Erosion, Shield Splitter,
    Yogi''s Necklace, Pharaoh''s Curse, Prophetic Cloak, Draconic Scale, Eye of the
    Storm, Arondight, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.55
      pick: 0.31
      fit: 0.48
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.61
      pick: 0.29
      fit: 0.48
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.14
      fit: 0.46
    Glorious Pridwen:
      total: 0.68
      efficiency: 0.36
      win: 1.0
      pick: 0.06
      fit: 0.64
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.46
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Jotunn''s Revenge, Shield Splitter, Oni Hunter''s Garb, Freya''s Tears,
    The Crusher, Hydra''s Lament, Eye of the Storm, Shield of the Phoenix, Erosion,
    Draconic Scale, Spectral Armor, Pharaoh''s Curse, Avenging Blade, Golden Blade,
    Yogi''s Necklace, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Stone
    of Binding, Lernaean Bow, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.31
      fit: 0.33
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.14
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Erosion, Kinetic Cuirass, Spectral Armor, Berserker''s
    Shield, Pharaoh''s Curse, Shield of the Phoenix, Eye of Providence, Jotunn''s
    Revenge, Shogun''s Ofuda, Oni Hunter''s Garb, Stampede, Doublet of Binding, Void
    Shield, The Crusher, Eye of the Storm, Void Stone, Hydra''s Lament, Freya''s Tears,
    Shield Splitter, Chandra''s Grace, Draconic Scale, Avenging Blade, Mystical Mail,
    Umbral Link.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.31
      fit: 0.29
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.29
      fit: 0.29
    Glorious Pridwen:
      total: 0.68
      efficiency: 0.36
      win: 1.0
      pick: 0.06
      fit: 0.68
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.55
      pick: 0.17
      fit: 0.58
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.55
      pick: 0.46
      fit: 0.61
    Amanita Charm:
      total: 0.61
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Erosion, Spectral Armor, Kinetic
    Cuirass, Jotunn''s Revenge, Berserker''s Shield, Pharaoh''s Curse, Eye of Providence,
    Shogun''s Ofuda, Oni Hunter''s Garb, The Crusher, Stampede, Doublet of Binding,
    Hydra''s Lament, Void Shield, Chandra''s Grace, Eye of the Storm, Umbral Link,
    Shield Splitter, The Reaper, Freya''s Tears, Void Stone, Phoenix Feather, Avenging
    Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.31
      fit: 0.3
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.29
      fit: 0.3
    Glorious Pridwen:
      total: 0.7
      efficiency: 0.36
      win: 1.0
      pick: 0.06
      fit: 0.77
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.55
      pick: 0.17
      fit: 0.57
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.46
      fit: 0.58
    Amanita Charm:
      total: 0.61
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Glorious Pridwen
  - Void Shield
  - The Crusher
  flex_slots:
  - Void Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, Void Shield, The Crusher, Void
    Stone, Spectral Armor, Erosion, Berserker''s Shield, Pharaoh''s Curse, Kinetic
    Cuirass, Avenging Blade, Shield of the Phoenix, The Reaper, Eye of Providence,
    Shogun''s Ofuda, Oni Hunter''s Garb, Stampede, Doublet of Binding, Riptalon, Stone
    of Binding, Hydra''s Lament, Screeching Gargoyle, Umbral Link, Freya''s Tears,
    Eye of the Storm.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.31
      fit: 0.21
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.29
      fit: 0.21
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.52
      pick: 0.14
      fit: 0.55
    Glorious Pridwen:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.06
      fit: 0.55
    Void Shield:
      total: 0.54
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Glorious Pridwen
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Pharaoh's Curse
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Pharaoh''s Curse, Shogun''s Ofuda,
    Spectral Armor, Riptalon, Erosion, Kinetic Cuirass, Golden Blade, Shield of the
    Phoenix, Eros'' Bow, Eye of Providence, Jotunn''s Revenge, Oni Hunter''s Garb,
    Stampede, Umbral Link, Doublet of Binding, Void Shield, The Crusher, Void Stone,
    Lernaean Bow, Hydra''s Lament, Freya''s Tears, Chandra''s Grace, Yogi''s Necklace.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.29
      fit: 0.19
    Glorious Pridwen:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.06
      fit: 0.51
    Amanita Charm:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Glorious Pridwen
  - Shifter's Shield
  - Spectral Armor
  flex_slots:
  - Shifter's Shield
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield of the Phoenix,
    Jotunn''s Revenge, Spectral Armor, Erosion, Berserker''s Shield, Pharaoh''s Curse,
    Kinetic Cuirass, Freya''s Tears, Chandra''s Grace, Hydra''s Lament, Eye of Providence,
    Shogun''s Ofuda, Oni Hunter''s Garb, Stampede, Doublet of Binding, Void Shield,
    Void Stone, The Crusher, Umbral Link, Gladiator''s Shield, Yogi''s Necklace, Screeching
    Gargoyle, Eros'' Bow, Mystical Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.31
      fit: 0.45
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.61
      pick: 0.29
      fit: 0.45
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.14
      fit: 0.44
    Glorious Pridwen:
      total: 0.7
      efficiency: 0.36
      win: 1.0
      pick: 0.06
      fit: 0.79
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.46
      fit: 0.47
    Spectral Armor:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Berserker's Shield
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Erosion, Kinetic Cuirass, Spectral Armor,
    Berserker''s Shield, Pharaoh''s Curse, Shield of the Phoenix, Eye of Providence,
    Shogun''s Ofuda, Oni Hunter''s Garb, Stampede, Jotunn''s Revenge, Doublet of Binding,
    Void Shield, The Crusher, Eye of the Storm, Void Stone, Hydra''s Lament, Freya''s
    Tears, Shield Splitter, Chandra''s Grace, Draconic Scale, Avenging Blade, Mystical
    Mail, Umbral Link.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.71
    Spectral Armor:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.61
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.91
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
  aspect: Aspect of Preservation
---
