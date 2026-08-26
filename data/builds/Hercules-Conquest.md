---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.51
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Runeforged Hammer
      pick_rate: 0.08
      win_rate: 1.0
  - name: Breastplate of Valor
    pick_rate: 0.32
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.67
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.0
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.22
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.71
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.67
    - name: Regrowth Striders
      pick_rate: 0.12
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.21
    win_rate: 0.5
    alternates:
    - name: Captain's Ring
      pick_rate: 0.07
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.5
  - name: Contagion
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Draconic Scale
      pick_rate: 0.17
      win_rate: 0.5
    - name: Glorious Pridwen
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.49
    win_rate: 0.56
  - name: Bumba's Cudgel
    pick_rate: 0.43
    win_rate: 0.56
  - name: Bluestone Brooch
    pick_rate: 0.03
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-08-26'
  god_win_rate: 0.5405405405405406
  god_matches_won: 20
  god_matches_played: 37
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Glorious Pridwen
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Eye of the Storm, Erosion, Berserker''s Shield, Eye of Providence, Shield of the
    Phoenix, Hydra''s Lament, Stone of Binding, Magi''s Cloak, Avenging Blade, Mantle
    Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker,
    Leviathan''s Hide, Void Shield, Stampede, Ancile, Prophetic Cloak, Oni Hunter''s
    Garb.'
  slot_scores:
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.65
      win: 0.75
      pick: 0.44
      fit: 0.33
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
    Glorious Pridwen:
      total: 0.68
      efficiency: 0.38
      win: 1.0
      pick: 0.25
      fit: 0.54
    Runeforged Hammer:
      total: 0.73
      efficiency: 0.57
      win: 1.0
      pick: 0.08
      fit: 0.51
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.71
      pick: 0.35
      fit: 0.54
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.53
      pick: 0.51
      fit: 0.6
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, The Reaper, Eye
    of Providence, Hydra''s Lament, Yogi''s Necklace, Avenging Blade, Phoenix Feather,
    Chandra''s Grace, Stone of Binding, Midgardian Mail, Hide of the Nemean Lion,
    Daybreak Gavel, Magi''s Cloak, Leviathan''s Hide, Heartseeker, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.44
      fit: 0.3
    Glorious Pridwen:
      total: 0.71
      efficiency: 0.38
      win: 1.0
      pick: 0.25
      fit: 0.77
    Runeforged Hammer:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.08
      fit: 0.57
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.71
      pick: 0.35
      fit: 0.47
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.53
      pick: 0.51
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Runeforged Hammer, Amanita Charm, Stone of Binding, Avenging Blade,
    Kinetic Cuirass, Screeching Gargoyle, Heartseeker, Void Shield, Shield Splitter,
    Void Stone, Titan''s Bane, Berserker''s Shield, The Crusher, Eye of the Storm,
    The Reaper, Erosion, Hydra''s Lament, Eye of Providence, Shield of the Phoenix,
    Magi''s Cloak, Pendulum Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian
    Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.44
      fit: 0.24
    Glorious Pridwen:
      total: 0.65
      efficiency: 0.38
      win: 1.0
      pick: 0.25
      fit: 0.39
    Runeforged Hammer:
      total: 0.71
      efficiency: 0.57
      win: 1.0
      pick: 0.08
      fit: 0.4
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.71
      pick: 0.35
      fit: 0.39
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.51
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Tyrfing
  - Glorious Pridwen
  - Runeforged Hammer
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
    this god: Runeforged Hammer, Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Tyrfing, Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Shogun''s Ofuda, Silverbranch Bow, Erosion, Eye of Providence, Stone of Binding,
    Toxic Blade, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Tekko-Kagi.'
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
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.44
      fit: 0.21
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.55
    Glorious Pridwen:
      total: 0.65
      efficiency: 0.38
      win: 1.0
      pick: 0.25
      fit: 0.34
    Runeforged Hammer:
      total: 0.7
      efficiency: 0.57
      win: 1.0
      pick: 0.08
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Runeforged Hammer, Amanita Charm,
    Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle,
    Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Eye of Providence,
    Gladiator''s Shield, Stone of Binding, Eye of the Storm, Arondight, Magi''s Cloak,
    Eye of Erebus, Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Chandra''s
    Grace, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.34
      fit: 0.48
    Breastplate of Valor:
      total: 0.66
      efficiency: 0.65
      win: 0.75
      pick: 0.44
      fit: 0.48
    Glorious Pridwen:
      total: 0.69
      efficiency: 0.38
      win: 1.0
      pick: 0.25
      fit: 0.64
    Runeforged Hammer:
      total: 0.7
      efficiency: 0.57
      win: 1.0
      pick: 0.08
      fit: 0.32
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.71
      pick: 0.35
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.51
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Eye of the Storm, Erosion, Berserker''s Shield, Eye of Providence, Shield
    of the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s Cloak, Avenging Blade,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion,
    Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile, Prophetic Cloak,
    Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.32
      efficiency: 0.72
      win: 0.0
      pick: 0.19
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.71
      pick: 0.35
      fit: 0.54
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.53
      pick: 0.51
      fit: 0.6
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
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
    this god: Runeforged Hammer, Amanita Charm, Erosion, Kinetic Cuirass, Shield of
    the Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Shield Splitter,
    Eye of the Storm, Doublet of Binding, Berserker''s Shield, Eye of Providence,
    Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, Mystical Mail, Hydra''s Lament,
    Midgardian Mail, Sanguine Lash, Stone of Binding, Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.44
      fit: 0.29
    Glorious Pridwen:
      total: 0.7
      efficiency: 0.38
      win: 1.0
      pick: 0.25
      fit: 0.68
    Runeforged Hammer:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.08
      fit: 0.58
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.71
      pick: 0.35
      fit: 0.48
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.53
      pick: 0.51
      fit: 0.61
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
    this god: Runeforged Hammer, Amanita Charm, Erosion, Shield of the Phoenix, Kinetic
    Cuirass, Void Shield, Stampede, Shield Splitter, Void Stone, Spectral Armor, Eye
    of the Storm, Doublet of Binding, Berserker''s Shield, The Reaper, Eye of Providence,
    Hydra''s Lament, Yogi''s Necklace, Avenging Blade, Shogun''s Ofuda, Phoenix Feather,
    Pharaoh''s Curse, Chandra''s Grace, Mystical Mail, Sanguine Lash.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.44
      fit: 0.3
    Glorious Pridwen:
      total: 0.71
      efficiency: 0.38
      win: 1.0
      pick: 0.25
      fit: 0.77
    Runeforged Hammer:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.08
      fit: 0.57
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.71
      pick: 0.35
      fit: 0.47
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.53
      pick: 0.51
      fit: 0.58
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
  - Void Shield
  - Void Stone
  - Freya's Tears
  flex_slots:
  - Void Shield
  - Void Stone
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
    for this god: Runeforged Hammer, Amanita Charm, Void Shield, Void Stone, Erosion,
    Avenging Blade, Kinetic Cuirass, Stone of Binding, Shield of the Phoenix, The
    Reaper, Stampede, Screeching Gargoyle, Spectral Armor, Heartseeker, Doublet of
    Binding, Shield Splitter, Berserker''s Shield, Eye of the Storm, Titan''s Bane,
    The Crusher, Shogun''s Ofuda, Eye of Providence, Pharaoh''s Curse, Hydra''s Lament.'
  slot_scores:
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.44
      fit: 0.21
    Glorious Pridwen:
      total: 0.68
      efficiency: 0.38
      win: 1.0
      pick: 0.25
      fit: 0.55
    Runeforged Hammer:
      total: 0.72
      efficiency: 0.57
      win: 1.0
      pick: 0.08
      fit: 0.45
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
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.71
      pick: 0.35
      fit: 0.35
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Amanita Charm, Berserker''s Shield, Pharaoh''s Curse,
    Shogun''s Ofuda, Erosion, Riptalon, Kinetic Cuirass, Golden Blade, Shield of the
    Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Doublet of Binding,
    Umbral Link, The Reaper, Tyrfing, Eros'' Bow, Shield Splitter, Sanguine Lash,
    Lernaean Bow, Toxic Blade, Eye of the Storm, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.44
      fit: 0.19
    Glorious Pridwen:
      total: 0.67
      efficiency: 0.38
      win: 1.0
      pick: 0.25
      fit: 0.51
    Runeforged Hammer:
      total: 0.71
      efficiency: 0.57
      win: 1.0
      pick: 0.08
      fit: 0.36
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
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Glorious Pridwen
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
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
    + fit + win/pick). Underrated for this god: Runeforged Hammer, Amanita Charm,
    Shield of the Phoenix, Erosion, Kinetic Cuirass, Void Shield, Stampede, Void Stone,
    Spectral Armor, Hydra''s Lament, Chandra''s Grace, Doublet of Binding, Screeching
    Gargoyle, Berserker''s Shield, Gladiator''s Shield, Shield Splitter, Eye of Providence,
    Shogun''s Ofuda, Pharaoh''s Curse, Eye of the Storm, Mystical Mail, Prophetic
    Cloak, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.34
      fit: 0.45
    Breastplate of Valor:
      total: 0.66
      efficiency: 0.65
      win: 0.75
      pick: 0.44
      fit: 0.45
    Glorious Pridwen:
      total: 0.71
      efficiency: 0.38
      win: 1.0
      pick: 0.25
      fit: 0.79
    Runeforged Hammer:
      total: 0.71
      efficiency: 0.57
      win: 1.0
      pick: 0.08
      fit: 0.38
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.71
      pick: 0.35
      fit: 0.59
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.51
      fit: 0.47
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
    Shield Splitter, Eye of the Storm, Doublet of Binding, Berserker''s Shield, Eye
    of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, Mystical Mail,
    Hydra''s Lament, Midgardian Mail, Sanguine Lash, Stone of Binding, Yogi''s Necklace,
    Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.32
      efficiency: 0.72
      win: 0.0
      pick: 0.19
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
  starter: *id001
  aspect: Aspect of Preservation
---
