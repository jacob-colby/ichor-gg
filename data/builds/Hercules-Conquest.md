---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.49
    win_rate: 0.48
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.25
  - name: Breastplate of Valor
    pick_rate: 0.23
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.36
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.36
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.19
      win_rate: 0.5
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.27
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.27
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.33
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.33
    - name: Hide of the Nemean Lion
      pick_rate: 0.1
      win_rate: 0.5
  - name: Glorious Pridwen
    pick_rate: 0.1
    win_rate: 0.33
    alternates:
    - name: Draconic Scale
      pick_rate: 0.1
      win_rate: 0.67
    - name: Ring
      pick_rate: 0.1
      win_rate: 0.67
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.55
    win_rate: 0.38
  - name: Bumba's Hammer
    pick_rate: 0.35
    win_rate: 0.41
  - name: Bluestone Brooch
    pick_rate: 0.02
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-09-11'
  god_win_rate: 0.4024390243902439
  god_matches_won: 33
  god_matches_played: 82
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter,
    Runeforged Hammer, Eye of the Storm, Erosion, Berserker''s Shield, Eye of Providence,
    Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Heartseeker, Leviathan''s
    Hide, Void Shield, Stampede, Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.4
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.31
      fit: 0.33
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.47
      pick: 0.45
      fit: 0.54
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.6
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion,
    The Reaper, Eye of Providence, Hydra''s Lament, Yogi''s Necklace, Avenging Blade,
    Phoenix Feather, Chandra''s Grace, Stone of Binding, Midgardian Mail, Daybreak
    Gavel, Magi''s Cloak, Leviathan''s Hide, Heartseeker, Void Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.42
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.31
      fit: 0.3
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Avenging Blade,
    Kinetic Cuirass, Screeching Gargoyle, Heartseeker, Void Shield, Shield Splitter,
    Void Stone, Runeforged Hammer, Titan''s Bane, Berserker''s Shield, The Crusher,
    Eye of the Storm, The Reaper, Erosion, Hydra''s Lament, Eye of Providence, Shield
    of the Phoenix, Magi''s Cloak, Pendulum Blade, Avatar''s Parashu, Mantle Of Discord,
    Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.31
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.57
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.47
      pick: 0.45
      fit: 0.39
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.43
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Draconic Scale
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Tyrfing, Shield Splitter, Pharaoh''s Curse, Runeforged Hammer, Riptalon,
    Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Eye of Providence, Stone
    of Binding, Toxic Blade, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament,
    Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.31
      fit: 0.21
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.21
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.55
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.38
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle,
    Shield Splitter, Berserker''s Shield, Prophetic Cloak, Gladiator''s Shield, Erosion,
    Runeforged Hammer, Eye of Providence, Stone of Binding, Eye of the Storm, Arondight,
    Magi''s Cloak, Eye of Erebus, Mantle Of Discord, Midgardian Mail, Daybreak Gavel,
    Chandra''s Grace, Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.46
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.58
      pick: 0.31
      fit: 0.48
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.47
      pick: 0.45
      fit: 0.64
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Runeforged Hammer, Eye of the Storm, Erosion, Berserker''s Shield, Eye
    of Providence, Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s
    Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle,
    Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile, Prophetic Cloak,
    Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.48
      pick: 0.49
      fit: 0.6
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.47
      pick: 0.45
      fit: 0.54
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Erosion, Jotunn''s Revenge, Kinetic Cuirass, Shield of
    the Phoenix, Void Shield, Stampede, Runeforged Hammer, Void Stone, Spectral Armor,
    Shield Splitter, Eye of the Storm, Doublet of Binding, Berserker''s Shield, Eye
    of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, Mystical Mail,
    Hydra''s Lament, Midgardian Mail, Sanguine Lash, Stone of Binding, Yogi''s Necklace,
    Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.39
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.31
      fit: 0.29
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.71
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.61
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Draconic Scale
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Erosion, Shield of the Phoenix, Kinetic
    Cuirass, Void Shield, Runeforged Hammer, Stampede, Shield Splitter, Void Stone,
    Spectral Armor, Eye of the Storm, Doublet of Binding, Berserker''s Shield, The
    Reaper, Eye of Providence, Hydra''s Lament, Yogi''s Necklace, Avenging Blade,
    Shogun''s Ofuda, Phoenix Feather, Pharaoh''s Curse, Chandra''s Grace, Mystical
    Mail, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.42
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.31
      fit: 0.3
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.58
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Draconic Scale
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Void Shield
  - Void Stone
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Void Stone
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, Void Shield, Void Stone, Erosion,
    Avenging Blade, Kinetic Cuirass, Stone of Binding, Shield of the Phoenix, The
    Reaper, Stampede, Screeching Gargoyle, Spectral Armor, Runeforged Hammer, Heartseeker,
    Doublet of Binding, Shield Splitter, Berserker''s Shield, Eye of the Storm, Titan''s
    Bane, The Crusher, Shogun''s Ofuda, Eye of Providence, Pharaoh''s Curse, Hydra''s
    Lament.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.55
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.31
      fit: 0.21
    Void Shield:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.45
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Draconic Scale
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Draconic Scale
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
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Pharaoh''s Curse, Shogun''s Ofuda,
    Jotunn''s Revenge, Erosion, Riptalon, Kinetic Cuirass, Golden Blade, Shield of
    the Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Doublet of Binding,
    Runeforged Hammer, Umbral Link, The Reaper, Tyrfing, Eros'' Bow, Shield Splitter,
    Sanguine Lash, Lernaean Bow, Toxic Blade, Eye of the Storm, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.58
      pick: 0.31
      fit: 0.19
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.4
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.52
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Breastplate of Valor
  - Draconic Scale
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Freya's Tears
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Jotunn''s Revenge,
    Shield of the Phoenix, Erosion, Kinetic Cuirass, Void Shield, Stampede, Void Stone,
    Spectral Armor, Hydra''s Lament, Chandra''s Grace, Doublet of Binding, Screeching
    Gargoyle, Berserker''s Shield, Gladiator''s Shield, Runeforged Hammer, Shield
    Splitter, Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Eye of the Storm,
    Mystical Mail, Prophetic Cloak, Eye of Erebus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.44
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.31
      fit: 0.45
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.47
      pick: 0.45
      fit: 0.59
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.31
      fit: 0.47
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.97
    Erosion:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Void Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shield of the Phoenix
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Erosion, Jotunn''s Revenge, Kinetic Cuirass,
    Shield of the Phoenix, Void Shield, Stampede, Runeforged Hammer, Void Stone, Spectral
    Armor, Shield Splitter, Eye of the Storm, Doublet of Binding, Berserker''s Shield,
    Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, Mystical
    Mail, Hydra''s Lament, Midgardian Mail, Sanguine Lash, Stone of Binding, Yogi''s
    Necklace, Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.1
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.74
    Void Shield:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
  aspect: Aspect of Preservation
---
