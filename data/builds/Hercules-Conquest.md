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
  - name: Jotunn's Revenge
    pick_rate: 0.5
    win_rate: 0.5
    alternates:
    - name: Golden Blade
      pick_rate: 0.17
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.0
  - name: Hydra's Lament
    pick_rate: 0.25
    win_rate: 0.67
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.17
      win_rate: 0.0
    - name: Regrowth Striders
      pick_rate: 0.08
      win_rate: 1.0
  - name: Heartseeker
    pick_rate: 0.25
    win_rate: 0.33
    alternates:
    - name: Regrowth Striders
      pick_rate: 0.08
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 1.0
  - name: Hussar's Wings
    pick_rate: 0.17
    win_rate: 1.0
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 1.0
  - name: Brawler’s Beat Stick
    pick_rate: 0.33
    win_rate: 0.75
    alternates:
    - name: Regrowth Striders
      pick_rate: 0.08
      win_rate: 1.0
    - name: Glorious Pridwen
      pick_rate: 0.08
      win_rate: 0.0
  - name: Freya's Tears
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Stone of Binding
      pick_rate: 0.17
      win_rate: 0.0
    - name: Sage's Ring
      pick_rate: 0.17
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.33
    win_rate: 0.5
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.5
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-10-21'
  god_win_rate: 0.5
  god_matches_won: 6
  god_matches_played: 12
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Hussar's Wings
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Hussar's Wings
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Genji''s Guard, Amanita Charm, Kinetic Cuirass, Shield Splitter, Breastplate
    of Valor, Runeforged Hammer, Eye of the Storm, Erosion, Berserker''s Shield, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean
    Lion, Leviathan''s Hide, Void Shield, Stampede, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.74
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.33
    Kinetic Cuirass:
      total: 0.7
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.7
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.6
    Hussar's Wings:
      total: 0.69
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.6
    Freya's Tears:
      total: 0.8
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.54
    Amanita Charm:
      total: 0.71
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Hussar's Wings
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Shield of the Phoenix
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Breastplate of Valor, Berserker''s
    Shield, Erosion, The Reaper, Eye of Providence, Draconic Scale, Yogi''s Necklace,
    Avenging Blade, Phoenix Feather, Chandra''s Grace, Midgardian Mail, Hide of the
    Nemean Lion, Daybreak Gavel, Magi''s Cloak, Leviathan''s Hide, Void Shield.'
  slot_scores:
    Golden Blade:
      total: 0.7
      efficiency: 0.44
      win: 1.0
      pick: 0.17
      fit: 0.55
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.3
    Shield of the Phoenix:
      total: 0.7
      efficiency: 0.53
      win: 0.88
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.58
    Freya's Tears:
      total: 0.79
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.47
    Amanita Charm:
      total: 0.75
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Golden Blade
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Genji''s Guard, Amanita Charm, Avenging Blade, Kinetic Cuirass,
    Screeching Gargoyle, Void Shield, Shield Splitter, Breastplate of Valor, Void
    Stone, Runeforged Hammer, Titan''s Bane, Berserker''s Shield, The Crusher, Eye
    of the Storm, The Reaper, Erosion, Eye of Providence, Draconic Scale, Shield of
    the Phoenix, Magi''s Cloak, Pendulum Blade, Avatar''s Parashu, Mantle Of Discord,
    Midgardian Mail.'
  slot_scores:
    Avenging Blade:
      total: 0.67
      efficiency: 0.49
      win: 0.88
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.24
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.53
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.43
    Freya's Tears:
      total: 0.77
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.39
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Tyrfing
  - Shifter's Shield
  - Freya's Tears
  flex_slots:
  - Berserker's Shield
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Breastplate of Valor, Tyrfing, Shield Splitter, Pharaoh''s Curse, Runeforged Hammer,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Eye of Providence,
    Toxic Blade, Eye of the Storm, Shield of the Phoenix, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.17
      fit: 0.56
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.21
    Berserker's Shield:
      total: 0.7
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.65
      efficiency: 0.48
      win: 0.88
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.38
    Freya's Tears:
      total: 0.77
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.34
  community_ordered:
  - Golden Blade
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Shield
    Splitter, Berserker''s Shield, Erosion, Runeforged Hammer, Eye of Providence,
    Gladiator''s Shield, Draconic Scale, Eye of the Storm, Arondight, Magi''s Cloak,
    Eye of Erebus, Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Chandra''s
    Grace, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.76
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.48
    Breastplate of Valor:
      total: 0.69
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.45
    Freya's Tears:
      total: 0.81
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.64
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm, Erosion, Berserker''s
    Shield, Eye of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak,
    Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide
    of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Ancile, Oni Hunter''s
    Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.5
      fit: 0.4
    Kinetic Cuirass:
      total: 0.7
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.69
      efficiency: 0.55
      win: 0.88
      pick: 0.0
      fit: 0.67
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.6
    Freya's Tears:
      total: 0.8
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.54
    Amanita Charm:
      total: 0.71
      efficiency: 0.65
      win: 0.88
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
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  - Freya's Tears
  - Erosion
  flex_slots:
  - Erosion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Erosion, Kinetic Cuirass, Shield of the
    Phoenix, Void Shield, Stampede, Runeforged Hammer, Void Stone, Spectral Armor,
    Shield Splitter, Eye of the Storm, Doublet of Binding, Berserker''s Shield, Breastplate
    of Valor, Eye of Providence, Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse,
    Avenging Blade, Mystical Mail, Midgardian Mail, Sanguine Lash, Yogi''s Necklace,
    Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.29
    Kinetic Cuirass:
      total: 0.7
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.71
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.61
    Amanita Charm:
      total: 0.77
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 1.0
    Freya's Tears:
      total: 0.79
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.48
    Erosion:
      total: 0.71
      efficiency: 0.51
      win: 0.88
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  - Freya's Tears
  - Erosion
  flex_slots:
  - Erosion
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Erosion, Shield of the Phoenix, Kinetic
    Cuirass, Void Shield, Runeforged Hammer, Stampede, Shield Splitter, Void Stone,
    Spectral Armor, Eye of the Storm, Doublet of Binding, Breastplate of Valor, Berserker''s
    Shield, The Reaper, Eye of Providence, Draconic Scale, Yogi''s Necklace, Avenging
    Blade, Shogun''s Ofuda, Phoenix Feather, Pharaoh''s Curse, Chandra''s Grace, Mystical
    Mail, Sanguine Lash.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.3
    Shield of the Phoenix:
      total: 0.7
      efficiency: 0.53
      win: 0.88
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.58
    Amanita Charm:
      total: 0.77
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 1.0
    Freya's Tears:
      total: 0.79
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.47
    Erosion:
      total: 0.7
      efficiency: 0.51
      win: 0.88
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Void Shield
  - Void Stone
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Void Shield
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    for this god: Amanita Charm, Genji''s Guard, Void Shield, Void Stone, Erosion,
    Avenging Blade, Kinetic Cuirass, Shield of the Phoenix, The Reaper, Stampede,
    Screeching Gargoyle, Spectral Armor, Runeforged Hammer, Doublet of Binding, Breastplate
    of Valor, Shield Splitter, Berserker''s Shield, Eye of the Storm, Titan''s Bane,
    The Crusher, Shogun''s Ofuda, Eye of Providence, Pharaoh''s Curse, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.21
    Void Shield:
      total: 0.71
      efficiency: 0.47
      win: 0.88
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.7
      efficiency: 0.45
      win: 0.88
      pick: 0.0
      fit: 1.0
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.45
    Freya's Tears:
      total: 0.77
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.35
    Amanita Charm:
      total: 0.77
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Shifter's Shield
  - Amanita Charm
  - Freya's Tears
  - Pharaoh's Curse
  flex_slots:
  - Berserker's Shield
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    this god: Amanita Charm, Genji''s Guard, Berserker''s Shield, Pharaoh''s Curse,
    Shogun''s Ofuda, Erosion, Riptalon, Kinetic Cuirass, Shield of the Phoenix, Void
    Shield, Stampede, Void Stone, Spectral Armor, Breastplate of Valor, Doublet of
    Binding, Runeforged Hammer, Umbral Link, The Reaper, Tyrfing, Eros'' Bow, Shield
    Splitter, Sanguine Lash, Lernaean Bow, Toxic Blade, Eye of the Storm, Silverbranch
    Bow.'
  slot_scores:
    Golden Blade:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 0.17
      fit: 0.59
    Berserker's Shield:
      total: 0.7
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.4
    Amanita Charm:
      total: 0.76
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.31
    Pharaoh's Curse:
      total: 0.69
      efficiency: 0.51
      win: 0.88
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Golden Blade
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Shield of the Phoenix
  - Shifter's Shield
  - Freya's Tears
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Genji''s Guard, Shield
    of the Phoenix, Breastplate of Valor, Erosion, Kinetic Cuirass, Void Shield, Stampede,
    Void Stone, Spectral Armor, Chandra''s Grace, Doublet of Binding, Screeching Gargoyle,
    Berserker''s Shield, Runeforged Hammer, Gladiator''s Shield, Shield Splitter,
    Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Draconic Scale, Eye of the
    Storm, Mystical Mail, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.75
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.45
    Breastplate of Valor:
      total: 0.69
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.45
    Shield of the Phoenix:
      total: 0.7
      efficiency: 0.53
      win: 0.88
      pick: 0.0
      fit: 0.84
    Shifter's Shield:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.28
      fit: 0.47
    Freya's Tears:
      total: 0.8
      efficiency: 0.61
      win: 1.0
      pick: 1.0
      fit: 0.59
    Erosion:
      total: 0.69
      efficiency: 0.51
      win: 0.88
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Erosion, Kinetic Cuirass, Shield of the
    Phoenix, Void Shield, Stampede, Runeforged Hammer, Void Stone, Spectral Armor,
    Shield Splitter, Eye of the Storm, Doublet of Binding, Berserker''s Shield, Genji''s
    Guard, Breastplate of Valor, Eye of Providence, Draconic Scale, Shogun''s Ofuda,
    Pharaoh''s Curse, Avenging Blade, Mystical Mail, Midgardian Mail, Sanguine Lash,
    Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.5
      fit: 0.39
    Kinetic Cuirass:
      total: 0.7
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.69
      efficiency: 0.53
      win: 0.88
      pick: 0.0
      fit: 0.74
    Void Shield:
      total: 0.68
      efficiency: 0.47
      win: 0.88
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.77
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.71
      efficiency: 0.51
      win: 0.88
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
  aspect: Aspect of Preservation
---
