---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.33
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.45
    win_rate: 0.49
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.13
      win_rate: 0.45
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.54
  - name: Breastplate of Valor
    pick_rate: 0.27
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.25
      win_rate: 0.48
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.27
    win_rate: 0.49
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.25
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.56
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.51
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.54
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.54
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.39
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.59
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.39
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.28
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.46
    win_rate: 0.56
  - name: Bumba's Cudgel
    pick_rate: 0.34
    win_rate: 0.43
  - name: Bumba's Golden Dagger
    pick_rate: 0.08
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-08-10'
  god_win_rate: 0.5053272450532724
  god_matches_won: 332
  god_matches_played: 657
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Freya''s Tears, Shield Splitter, The Crusher, Oni Hunter''s Garb, Shield of the
    Phoenix, Hydra''s Lament, Erosion, Eye of the Storm, Eye of Providence, Draconic
    Scale, Spectral Armor, Pharaoh''s Curse, Runeforged Hammer, Golden Blade, Leviathan''s
    Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail, Avenging Blade, Damaru,
    Shogun''s Ofuda, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.49
      pick: 0.42
      fit: 0.33
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.38
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.11
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.5
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
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Kinetic Cuirass,
    Berserker''s Shield, The Crusher, Oni Hunter''s Garb, Chandra''s Grace, Freya''s
    Tears, Eye of the Storm, Hydra''s Lament, The Reaper, Shield Splitter, Erosion,
    Phoenix Feather, Eye of Providence, Runeforged Hammer, Spectral Armor, Draconic
    Scale, Pharaoh''s Curse, Golden Blade, Avenging Blade, Leviathan''s Hide, Midgardian
    Mail, Riptalon, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.49
      pick: 0.42
      fit: 0.3
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.11
      fit: 0.42
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.82
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
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
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
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
    for this god: Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Amanita Charm,
    Berserker''s Shield, Stone of Binding, Avenging Blade, Screeching Gargoyle, Freya''s
    Tears, Void Shield, Oni Hunter''s Garb, Hydra''s Lament, The Reaper, Void Stone,
    Shield Splitter, Shield of the Phoenix, Erosion, Spectral Armor, Eye of the Storm,
    Heartseeker, Eye of Providence, Riptalon, Pharaoh''s Curse, Draconic Scale, Runeforged
    Hammer, Silverbranch Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.49
      pick: 0.42
      fit: 0.24
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 0.24
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.11
      fit: 0.57
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
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
    this god: Berserker''s Shield, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm,
    Golden Blade, Pharaoh''s Curse, Riptalon, Freya''s Tears, The Crusher, Oni Hunter''s
    Garb, Lernaean Bow, Shogun''s Ofuda, Shield of the Phoenix, Hydra''s Lament, Silverbranch
    Bow, Tyrfing, Spectral Armor, Erosion, Shield Splitter, Eye of Providence, Draconic
    Scale, Eye of the Storm, Leviathan''s Hide, Midgardian Mail, Runeforged Hammer,
    Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.49
      pick: 0.42
      fit: 0.21
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 0.21
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.54
      pick: 0.11
      fit: 0.21
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.57
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Kinetic Cuirass, Shield of the Phoenix, Amanita Charm, Berserker''s Shield, Hydra''s
    Lament, Oni Hunter''s Garb, Screeching Gargoyle, The Crusher, Chandra''s Grace,
    Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic Cloak,
    Shield Splitter, Pharaoh''s Curse, Draconic Scale, Leviathan''s Hide, Eye of the
    Storm, Midgardian Mail, Mantle Of Discord, Stone of Binding, Arondight, Runeforged
    Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.49
      pick: 0.42
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.11
      fit: 0.46
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Jotunn''s Revenge, Freya''s Tears, Shield Splitter, The Crusher, Oni Hunter''s
    Garb, Shield of the Phoenix, Hydra''s Lament, Erosion, Eye of the Storm, Runeforged
    Hammer, Eye of Providence, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Golden
    Blade, Leviathan''s Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail,
    Avenging Blade, Damaru, Shogun''s Ofuda, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.49
      pick: 0.42
      fit: 0.33
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.11
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Jotunn's Revenge
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Erosion, Kinetic Cuirass, Spectral Armor, Jotunn''s Revenge,
    Pharaoh''s Curse, Shield of the Phoenix, Berserker''s Shield, Shogun''s Ofuda,
    Void Shield, Doublet of Binding, Oni Hunter''s Garb, Stampede, The Crusher, Void
    Stone, Freya''s Tears, Eye of the Storm, Shield Splitter, Eye of Providence, Hydra''s
    Lament, Umbral Link, Draconic Scale, Chandra''s Grace, Runeforged Hammer, Mystical
    Mail, Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.11
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.71
    Spectral Armor:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
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
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Erosion, Kinetic
    Cuirass, Spectral Armor, Pharaoh''s Curse, Berserker''s Shield, Shogun''s Ofuda,
    Void Shield, The Crusher, Umbral Link, Doublet of Binding, Oni Hunter''s Garb,
    Chandra''s Grace, Freya''s Tears, Eye of the Storm, Stampede, Hydra''s Lament,
    Void Stone, The Reaper, Shield Splitter, Phoenix Feather, Eye of Providence, Runeforged
    Hammer, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.49
      pick: 0.42
      fit: 0.3
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.11
      fit: 0.42
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.82
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Void Stone
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, Void Shield, The Crusher, Void
    Stone, Spectral Armor, Erosion, Pharaoh''s Curse, Kinetic Cuirass, Shield of the
    Phoenix, Berserker''s Shield, The Reaper, Avenging Blade, Shogun''s Ofuda, Riptalon,
    Stone of Binding, Doublet of Binding, Oni Hunter''s Garb, Screeching Gargoyle,
    Stampede, Umbral Link, Freya''s Tears, Hydra''s Lament, Chandra''s Grace, Eye
    of the Storm, Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.49
      pick: 0.42
      fit: 0.21
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.11
      fit: 0.55
    Void Shield:
      total: 0.54
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.53
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Spectral Armor
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Genji's Guard
  - Spectral Armor
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Pharaoh''s Curse, Berserker''s Shield, Shogun''s Ofuda,
    Spectral Armor, Riptalon, Erosion, Jotunn''s Revenge, Kinetic Cuirass, Shield
    of the Phoenix, Golden Blade, Eros'' Bow, Umbral Link, Void Shield, Doublet of
    Binding, Oni Hunter''s Garb, Stampede, The Crusher, Void Stone, Freya''s Tears,
    Lernaean Bow, Chandra''s Grace, Hydra''s Lament, Silverbranch Bow, The Reaper,
    Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.49
      pick: 0.42
      fit: 0.19
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spectral Armor:
      total: 0.51
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.52
      efficiency: 0.52
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
  - Shield of the Phoenix
  - Spectral Armor
  - Erosion
  flex_slots:
  - Spectral Armor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield of the Phoenix,
    Jotunn''s Revenge, Spectral Armor, Erosion, Freya''s Tears, Pharaoh''s Curse,
    Kinetic Cuirass, Berserker''s Shield, Chandra''s Grace, Hydra''s Lament, Shogun''s
    Ofuda, Void Shield, Doublet of Binding, Oni Hunter''s Garb, Stampede, Void Stone,
    Umbral Link, The Crusher, Gladiator''s Shield, Screeching Gargoyle, Eros'' Bow,
    Eye of Providence, Mystical Mail, Glorious Pridwen, Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.49
      pick: 0.42
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 0.45
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.11
      fit: 0.44
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.84
    Spectral Armor:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.52
      efficiency: 0.52
      win: 0.5
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
  - Pharaoh's Curse
  - Shield of the Phoenix
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
    Pharaoh''s Curse, Shield of the Phoenix, Berserker''s Shield, Shogun''s Ofuda,
    Jotunn''s Revenge, Void Shield, Doublet of Binding, Oni Hunter''s Garb, Runeforged
    Hammer, Stampede, The Crusher, Void Stone, Freya''s Tears, Eye of the Storm, Shield
    Splitter, Eye of Providence, Hydra''s Lament, Umbral Link, Draconic Scale, Chandra''s
    Grace, Mystical Mail, Golden Blade.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.74
    Spectral Armor:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
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
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
  aspect: Aspect of Preservation
---
