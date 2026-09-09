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
    pick_rate: 0.43
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.0
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.0
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.25
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.19
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.14
      win_rate: 0.0
  - name: Breastplate of Valor
    pick_rate: 0.24
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.33
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.0
  - name: Freya's Tears
    pick_rate: 0.2
    win_rate: 0.33
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.2
      win_rate: 0.33
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.0
  - name: Hide of the Nemean Lion
    pick_rate: 0.2
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.0
    - name: Regrowth Striders
      pick_rate: 0.1
      win_rate: 0.0
  - name: Draconic Scale
    pick_rate: 0.29
    win_rate: 1.0
    alternates:
    - name: Olmec Blue
      pick_rate: 0.14
      win_rate: 0.0
    - name: Medal of Defense
      pick_rate: 0.14
      win_rate: 0.0
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.52
    win_rate: 0.18
  - name: Bumba's Hammer
    pick_rate: 0.33
    win_rate: 0.29
  - name: Bluestone Brooch
    pick_rate: 0.05
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-09-09'
  god_win_rate: 0.3333333333333333
  god_matches_won: 7
  god_matches_played: 21
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Shifter's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
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
    Hide, Void Shield, Stampede, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.33
      pick: 0.43
      fit: 0.6
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.37
      fit: 0.33
    Hide of the Nemean Lion:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.43
      fit: 0.38
    Freya's Tears:
      total: 0.46
      efficiency: 0.61
      win: 0.33
      pick: 0.33
      fit: 0.54
    Draconic Scale:
      total: 0.76
      efficiency: 0.5
      win: 1.0
      pick: 0.89
      fit: 0.6
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.29
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Shifter's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Shifter's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion,
    The Reaper, Eye of Providence, Hydra''s Lament, Yogi''s Necklace, Avenging Blade,
    Phoenix Feather, Chandra''s Grace, Glorious Pridwen, Stone of Binding, Midgardian
    Mail, Daybreak Gavel, Magi''s Cloak, Leviathan''s Hide, Heartseeker, Void Shield.'
  slot_scores:
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.33
      pick: 0.43
      fit: 0.58
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.37
      fit: 0.3
    Hide of the Nemean Lion:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.43
      fit: 0.4
    Freya's Tears:
      total: 0.45
      efficiency: 0.61
      win: 0.33
      pick: 0.33
      fit: 0.47
    Draconic Scale:
      total: 0.76
      efficiency: 0.5
      win: 1.0
      pick: 0.89
      fit: 0.58
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.29
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Shifter's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Shifter's Shield
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
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
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.29
      pick: 0.0
      fit: 0.57
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.37
      fit: 0.24
    Shifter's Shield:
      total: 0.43
      efficiency: 0.55
      win: 0.33
      pick: 0.43
      fit: 0.43
    Hide of the Nemean Lion:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.43
      fit: 0.28
    Freya's Tears:
      total: 0.44
      efficiency: 0.61
      win: 0.33
      pick: 0.33
      fit: 0.39
    Draconic Scale:
      total: 0.73
      efficiency: 0.5
      win: 1.0
      pick: 0.89
      fit: 0.43
  community_ordered:
  - Breastplate of Valor
  - Shifter's Shield
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Tyrfing
  - Hide of the Nemean Lion
  - Draconic Scale
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Berserker''s Shield, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass,
    Golden Blade, Tyrfing, Shield Splitter, Pharaoh''s Curse, Runeforged Hammer, Riptalon,
    Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Eye of Providence, Stone
    of Binding, Toxic Blade, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament,
    Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.4
      efficiency: 0.52
      win: 0.29
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.44
      efficiency: 0.68
      win: 0.29
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.37
      fit: 0.21
    Tyrfing:
      total: 0.38
      efficiency: 0.48
      win: 0.29
      pick: 0.0
      fit: 0.55
    Hide of the Nemean Lion:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.43
      fit: 0.24
    Draconic Scale:
      total: 0.73
      efficiency: 0.5
      win: 1.0
      pick: 0.89
      fit: 0.38
  community_ordered:
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Shifter's Shield
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle,
    Shield Splitter, Berserker''s Shield, Erosion, Runeforged Hammer, Eye of Providence,
    Gladiator''s Shield, Stone of Binding, Eye of the Storm, Arondight, Magi''s Cloak,
    Eye of Erebus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak
    Gavel, Chandra''s Grace, Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.72
      win: 0.29
      pick: 0.0
      fit: 0.46
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.37
      fit: 0.48
    Shifter's Shield:
      total: 0.43
      efficiency: 0.55
      win: 0.33
      pick: 0.43
      fit: 0.45
    Hide of the Nemean Lion:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.43
      fit: 0.29
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.33
      pick: 0.33
      fit: 0.64
    Draconic Scale:
      total: 0.74
      efficiency: 0.5
      win: 1.0
      pick: 0.89
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Shifter's Shield
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
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
    Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.72
      win: 0.29
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.29
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.42
      efficiency: 0.55
      win: 0.29
      pick: 0.0
      fit: 0.67
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.33
      pick: 0.43
      fit: 0.6
    Freya's Tears:
      total: 0.46
      efficiency: 0.61
      win: 0.33
      pick: 0.33
      fit: 0.54
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.29
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Shifter's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
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
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.33
      pick: 0.43
      fit: 0.61
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.37
      fit: 0.29
    Hide of the Nemean Lion:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.43
      fit: 0.43
    Freya's Tears:
      total: 0.45
      efficiency: 0.61
      win: 0.33
      pick: 0.33
      fit: 0.48
    Draconic Scale:
      total: 0.76
      efficiency: 0.5
      win: 1.0
      pick: 0.89
      fit: 0.61
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.29
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Shifter's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Shifter's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.33
      pick: 0.43
      fit: 0.58
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.37
      fit: 0.3
    Hide of the Nemean Lion:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.43
      fit: 0.4
    Freya's Tears:
      total: 0.45
      efficiency: 0.61
      win: 0.33
      pick: 0.33
      fit: 0.47
    Draconic Scale:
      total: 0.76
      efficiency: 0.5
      win: 1.0
      pick: 0.89
      fit: 0.58
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.29
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Shifter's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Void Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
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
      total: 0.46
      efficiency: 0.72
      win: 0.29
      pick: 0.0
      fit: 0.55
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.37
      fit: 0.21
    Hide of the Nemean Lion:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.43
      fit: 0.32
    Void Shield:
      total: 0.44
      efficiency: 0.47
      win: 0.29
      pick: 0.0
      fit: 1.0
    Draconic Scale:
      total: 0.74
      efficiency: 0.5
      win: 1.0
      pick: 0.89
      fit: 0.45
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.29
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Draconic Scale
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Pharaoh's Curse
  - Draconic Scale
  - Shogun's Ofuda
  flex_slots:
  - Pharaoh's Curse
  - Shogun's Ofuda
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Pharaoh''s Curse, Shogun''s Ofuda,
    Erosion, Jotunn''s Revenge, Riptalon, Kinetic Cuirass, Golden Blade, Shield of
    the Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Doublet of Binding,
    Runeforged Hammer, Umbral Link, The Reaper, Tyrfing, Eros'' Bow, Shield Splitter,
    Sanguine Lash, Lernaean Bow, Toxic Blade, Eye of the Storm, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.44
      efficiency: 0.68
      win: 0.29
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.37
      fit: 0.19
    Hide of the Nemean Lion:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.43
      fit: 0.28
    Pharaoh's Curse:
      total: 0.43
      efficiency: 0.51
      win: 0.29
      pick: 0.0
      fit: 0.78
    Draconic Scale:
      total: 0.73
      efficiency: 0.5
      win: 1.0
      pick: 0.89
      fit: 0.4
    Shogun's Ofuda:
      total: 0.42
      efficiency: 0.5
      win: 0.29
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Draconic Scale
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Jotunn''s Revenge,
    Shield of the Phoenix, Erosion, Kinetic Cuirass, Void Shield, Stampede, Void Stone,
    Spectral Armor, Hydra''s Lament, Chandra''s Grace, Doublet of Binding, Screeching
    Gargoyle, Berserker''s Shield, Runeforged Hammer, Glorious Pridwen, Gladiator''s
    Shield, Shield Splitter, Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse,
    Eye of the Storm, Mystical Mail, Eye of Erebus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.72
      win: 0.29
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.37
      fit: 0.45
    Hide of the Nemean Lion:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.43
      fit: 0.33
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.33
      pick: 0.33
      fit: 0.59
    Draconic Scale:
      total: 0.74
      efficiency: 0.5
      win: 1.0
      pick: 0.89
      fit: 0.47
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.29
      pick: 0.0
      fit: 0.97
  community_ordered:
  - Breastplate of Valor
  - Hide of the Nemean Lion
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
      total: 0.44
      efficiency: 0.72
      win: 0.29
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.29
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.43
      efficiency: 0.53
      win: 0.29
      pick: 0.0
      fit: 0.74
    Void Shield:
      total: 0.42
      efficiency: 0.47
      win: 0.29
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.29
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.45
      efficiency: 0.51
      win: 0.29
      pick: 0.0
      fit: 0.91
  starter: *id001
  aspect: Aspect of Preservation
---
