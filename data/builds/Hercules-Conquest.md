---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.48
    win_rate: 0.52
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.5
    - name: Daybreak Gavel
      pick_rate: 0.08
      win_rate: 0.4
  - name: Breastplate of Valor
    pick_rate: 0.26
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.39
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.45
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.16
      win_rate: 0.47
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.25
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.35
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.45
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.5
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.43
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.8
    alternates:
    - name: Glorious Pridwen
      pick_rate: 0.08
      win_rate: 0.25
    - name: Ring
      pick_rate: 0.08
      win_rate: 0.75
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.49
    win_rate: 0.41
  - name: Bumba's Hammer
    pick_rate: 0.38
    win_rate: 0.44
  - name: Bluestone Pendant
    pick_rate: 0.08
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-09-12'
  god_win_rate: 0.4375
  god_matches_won: 56
  god_matches_played: 128
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-12'
  god_matches_analyzed: 4284
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
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
    Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s
    Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle,
    Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile, Prophetic Cloak,
    Oni Hunter''s Garb.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.35
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.09
      fit: 0.4
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.52
      pick: 0.48
      fit: 0.6
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.52
      pick: 0.42
      fit: 0.54
    Hide of the Nemean Lion:
      total: 0.61
      efficiency: 0.52
      win: 0.8
      pick: 0.28
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion,
    The Reaper, Eye of Providence, Draconic Scale, Hydra''s Lament, Yogi''s Necklace,
    Avenging Blade, Phoenix Feather, Chandra''s Grace, Stone of Binding, Midgardian
    Mail, Magi''s Cloak, Leviathan''s Hide, Heartseeker, Void Shield, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.35
      fit: 0.3
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.09
      fit: 0.42
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.42
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.62
      efficiency: 0.52
      win: 0.8
      pick: 0.28
      fit: 0.4
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Avenging Blade,
    Kinetic Cuirass, Screeching Gargoyle, Heartseeker, Void Shield, Shield Splitter,
    Void Stone, Runeforged Hammer, Titan''s Bane, Berserker''s Shield, The Crusher,
    Eye of the Storm, The Reaper, Erosion, Hydra''s Lament, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Magi''s Cloak, Pendulum Blade, Avatar''s Parashu,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.35
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.09
      fit: 0.57
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.48
      fit: 0.43
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.52
      pick: 0.42
      fit: 0.39
    Hide of the Nemean Lion:
      total: 0.6
      efficiency: 0.52
      win: 0.8
      pick: 0.28
      fit: 0.28
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Tyrfing
  - Freya's Tears
  - Hide of the Nemean Lion
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
    Draconic Scale, Magi''s Cloak, Screeching Gargoyle, The Reaper, Tekko-Kagi, Daybreak
    Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.35
      fit: 0.21
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.51
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.42
      fit: 0.34
    Hide of the Nemean Lion:
      total: 0.59
      efficiency: 0.52
      win: 0.8
      pick: 0.28
      fit: 0.24
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Genji's Guard
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle,
    Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Runeforged Hammer,
    Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Eye
    of the Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle Of Discord, Midgardian
    Mail, Chandra''s Grace, Leviathan''s Hide, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.35
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.09
      fit: 0.46
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.45
      pick: 0.37
      fit: 0.48
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.52
      pick: 0.42
      fit: 0.64
    Hide of the Nemean Lion:
      total: 0.6
      efficiency: 0.52
      win: 0.8
      pick: 0.28
      fit: 0.29
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Genji's Guard
  - Freya's Tears
  - Hide of the Nemean Lion
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
    of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone of
    Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching
    Gargoyle, Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile, Prophetic
    Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.09
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.7
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.52
      pick: 0.48
      fit: 0.6
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.52
      pick: 0.42
      fit: 0.54
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.51
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
  - Shifter's Shield
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Erosion, Jotunn''s Revenge, Kinetic Cuirass, Shield of
    the Phoenix, Void Shield, Stampede, Runeforged Hammer, Void Stone, Spectral Armor,
    Shield Splitter, Eye of the Storm, Doublet of Binding, Berserker''s Shield, Eye
    of Providence, Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade,
    Mystical Mail, Hydra''s Lament, Midgardian Mail, Sanguine Lash, Stone of Binding,
    Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.09
      fit: 0.39
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.52
      pick: 0.48
      fit: 0.61
    Hide of the Nemean Lion:
      total: 0.62
      efficiency: 0.52
      win: 0.8
      pick: 0.28
      fit: 0.43
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.42
      fit: 0.48
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  - Erosion
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Erosion, Shield of the Phoenix, Kinetic
    Cuirass, Void Shield, Runeforged Hammer, Stampede, Shield Splitter, Void Stone,
    Spectral Armor, Eye of the Storm, Doublet of Binding, Berserker''s Shield, The
    Reaper, Eye of Providence, Draconic Scale, Hydra''s Lament, Yogi''s Necklace,
    Avenging Blade, Shogun''s Ofuda, Phoenix Feather, Pharaoh''s Curse, Chandra''s
    Grace, Mystical Mail, Sanguine Lash.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.35
      fit: 0.3
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.09
      fit: 0.42
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.42
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.62
      efficiency: 0.52
      win: 0.8
      pick: 0.28
      fit: 0.4
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Void Shield
  - Hide of the Nemean Lion
  - Void Stone
  - Amanita Charm
  flex_slots:
  - Void Stone
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, Void Shield, Void Stone, Erosion,
    Avenging Blade, Kinetic Cuirass, Stone of Binding, Shield of the Phoenix, The
    Reaper, Stampede, Screeching Gargoyle, Spectral Armor, Runeforged Hammer, Heartseeker,
    Doublet of Binding, Shield Splitter, Berserker''s Shield, Eye of the Storm, Titan''s
    Bane, The Crusher, Shogun''s Ofuda, Eye of Providence, Pharaoh''s Curse, Hydra''s
    Lament, Draconic Scale.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.35
      fit: 0.21
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.09
      fit: 0.55
    Void Shield:
      total: 0.54
      efficiency: 0.47
      win: 0.51
      pick: 0.0
      fit: 1.0
    Hide of the Nemean Lion:
      total: 0.6
      efficiency: 0.52
      win: 0.8
      pick: 0.28
      fit: 0.32
    Void Stone:
      total: 0.54
      efficiency: 0.45
      win: 0.51
      pick: 0.0
      fit: 1.0
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Amanita Charm
  - Hide of the Nemean Lion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Breastplate of Valor
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
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
      total: 0.54
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.35
      fit: 0.19
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.9
    Hide of the Nemean Lion:
      total: 0.6
      efficiency: 0.52
      win: 0.8
      pick: 0.28
      fit: 0.28
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.52
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Breastplate of Valor
  - Hide of the Nemean Lion
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  - Erosion
  flex_slots:
  - Jotunn's Revenge
  - Erosion
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
    Gargoyle, Berserker''s Shield, Runeforged Hammer, Gladiator''s Shield, Shield
    Splitter, Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Draconic Scale,
    Eye of the Storm, Mystical Mail, Prophetic Cloak, Eye of Erebus.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.35
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.09
      fit: 0.44
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.52
      pick: 0.42
      fit: 0.59
    Hide of the Nemean Lion:
      total: 0.6
      efficiency: 0.52
      win: 0.8
      pick: 0.28
      fit: 0.33
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.97
    Erosion:
      total: 0.52
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Hide of the Nemean Lion
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
    Eye of Providence, Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse, Avenging
    Blade, Mystical Mail, Hydra''s Lament, Midgardian Mail, Sanguine Lash, Stone of
    Binding, Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.09
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.74
    Void Shield:
      total: 0.52
      efficiency: 0.47
      win: 0.51
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
  aspect: Aspect of Preservation
---
