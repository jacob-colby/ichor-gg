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
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Eye of Providence
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Eye of Providence,
    Berserker''s Shield, Shield Splitter, Oni Hunter''s Garb, Freya''s Tears, The
    Crusher, Hydra''s Lament, Eye of the Storm, Shield of the Phoenix, Erosion, Runeforged
    Hammer, Draconic Scale, Hide of the Nemean Lion, Spectral Armor, Pharaoh''s Curse,
    Avenging Blade, Golden Blade, Yogi''s Necklace, Leviathan''s Hide, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Lernaean Bow.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.49
      pick: 0.27
      fit: 0.33
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.11
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
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Kinetic Cuirass,
    Berserker''s Shield, Eye of Providence, Oni Hunter''s Garb, The Crusher, Hydra''s
    Lament, Chandra''s Grace, Eye of the Storm, Runeforged Hammer, Shield Splitter,
    The Reaper, Freya''s Tears, Erosion, Phoenix Feather, Spectral Armor, Avenging
    Blade, Golden Blade, Draconic Scale, Pharaoh''s Curse, Yogi''s Necklace, Leviathan''s
    Hide, Midgardian Mail, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.49
      pick: 0.27
      fit: 0.3
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.11
      fit: 0.42
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
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
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Amanita Charm, Kinetic Cuirass,
    Berserker''s Shield, Avenging Blade, Eye of Providence, Stone of Binding, Oni
    Hunter''s Garb, Screeching Gargoyle, Hydra''s Lament, Freya''s Tears, Void Shield,
    Shield Splitter, The Reaper, Void Stone, Shield of the Phoenix, Runeforged Hammer,
    Eye of the Storm, Spectral Armor, Heartseeker, Erosion, Yogi''s Necklace, Pharaoh''s
    Curse, Draconic Scale, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.49
      pick: 0.27
      fit: 0.24
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.54
      pick: 0.11
      fit: 0.57
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
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
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass,
    Golden Blade, Eye of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher,
    Riptalon, Freya''s Tears, Lernaean Bow, Hydra''s Lament, Shogun''s Ofuda, Tyrfing,
    Shield of the Phoenix, Silverbranch Bow, Spectral Armor, Shield Splitter, Yogi''s
    Necklace, Runeforged Hammer, Erosion, Eye of the Storm, Draconic Scale, Dominance,
    Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.49
      pick: 0.27
      fit: 0.21
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.54
      pick: 0.11
      fit: 0.21
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
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
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s Shield, Hydra''s
    Lament, Eye of Providence, Oni Hunter''s Garb, The Crusher, Screeching Gargoyle,
    Chandra''s Grace, Gladiator''s Shield, Spectral Armor, Erosion, Shield Splitter,
    Yogi''s Necklace, Pharaoh''s Curse, Prophetic Cloak, Draconic Scale, Runeforged
    Hammer, Eye of the Storm, Arondight, Leviathan''s Hide, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.27
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.27
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.11
      fit: 0.46
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
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
    Shield, Jotunn''s Revenge, Shield Splitter, Runeforged Hammer, Oni Hunter''s Garb,
    Freya''s Tears, The Crusher, Hydra''s Lament, Eye of the Storm, Shield of the
    Phoenix, Erosion, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Avenging Blade,
    Golden Blade, Yogi''s Necklace, Leviathan''s Hide, Midgardian Mail, Mantle Of
    Discord, Stone of Binding, Lernaean Bow, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.49
      pick: 0.27
      fit: 0.33
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.11
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Erosion, Kinetic Cuirass, Spectral Armor, Berserker''s
    Shield, Pharaoh''s Curse, Jotunn''s Revenge, Shield of the Phoenix, Eye of Providence,
    Shogun''s Ofuda, Oni Hunter''s Garb, Stampede, Doublet of Binding, Void Shield,
    The Crusher, Eye of the Storm, Runeforged Hammer, Void Stone, Hydra''s Lament,
    Freya''s Tears, Shield Splitter, Chandra''s Grace, Draconic Scale, Avenging Blade,
    Mystical Mail, Umbral Link.'
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
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Erosion, Spectral
    Armor, Kinetic Cuirass, Berserker''s Shield, Pharaoh''s Curse, Eye of Providence,
    Shogun''s Ofuda, Oni Hunter''s Garb, The Crusher, Stampede, Doublet of Binding,
    Hydra''s Lament, Void Shield, Chandra''s Grace, Eye of the Storm, Runeforged Hammer,
    Umbral Link, Shield Splitter, The Reaper, Freya''s Tears, Void Stone, Phoenix
    Feather, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.11
      fit: 0.42
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.82
    Spectral Armor:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.7
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
      fit: 0.88
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - The Crusher
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Void Stone
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, Void Shield, The Crusher, Void
    Stone, Spectral Armor, Erosion, Berserker''s Shield, Pharaoh''s Curse, Kinetic
    Cuirass, Avenging Blade, Shield of the Phoenix, The Reaper, Eye of Providence,
    Shogun''s Ofuda, Oni Hunter''s Garb, Stampede, Doublet of Binding, Riptalon, Stone
    of Binding, Hydra''s Lament, Screeching Gargoyle, Runeforged Hammer, Umbral Link,
    Freya''s Tears, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
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
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spectral Armor:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Riptalon
  - Spectral Armor
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Spectral Armor
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Pharaoh''s Curse, Shogun''s Ofuda,
    Spectral Armor, Riptalon, Erosion, Kinetic Cuirass, Jotunn''s Revenge, Golden
    Blade, Shield of the Phoenix, Eros'' Bow, Eye of Providence, Oni Hunter''s Garb,
    Stampede, Umbral Link, Doublet of Binding, Void Shield, The Crusher, Void Stone,
    Lernaean Bow, Hydra''s Lament, Freya''s Tears, Chandra''s Grace, Yogi''s Necklace,
    Runeforged Hammer.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Riptalon:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spectral Armor:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.58
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield of the Phoenix,
    Jotunn''s Revenge, Spectral Armor, Erosion, Berserker''s Shield, Pharaoh''s Curse,
    Kinetic Cuirass, Freya''s Tears, Chandra''s Grace, Hydra''s Lament, Eye of Providence,
    Shogun''s Ofuda, Oni Hunter''s Garb, Stampede, Doublet of Binding, Void Shield,
    Void Stone, The Crusher, Umbral Link, Gladiator''s Shield, Yogi''s Necklace, Screeching
    Gargoyle, Eros'' Bow, Runeforged Hammer, Mystical Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.49
      pick: 0.27
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.27
      fit: 0.45
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
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
      total: 0.53
      efficiency: 0.59
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
    Runeforged Hammer, Shogun''s Ofuda, Oni Hunter''s Garb, Stampede, Jotunn''s Revenge,
    Doublet of Binding, Void Shield, The Crusher, Eye of the Storm, Void Stone, Hydra''s
    Lament, Freya''s Tears, Shield Splitter, Chandra''s Grace, Draconic Scale, Avenging
    Blade, Mystical Mail, Umbral Link.'
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
