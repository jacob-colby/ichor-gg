---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.39
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.45
    win_rate: 0.53
    alternates:
    - name: Pendulum Blade
      pick_rate: 0.08
      win_rate: 0.55
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.42
  - name: Breastplate of Valor
    pick_rate: 0.32
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.22
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.52
  - name: Genji's Guard
    pick_rate: 0.31
    win_rate: 0.53
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.21
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.49
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.59
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.66
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.67
    - name: Glorious Pridwen
      pick_rate: 0.05
      win_rate: 0.73
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.57
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.6
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.47
    win_rate: 0.63
  - name: Bumba's Cudgel
    pick_rate: 0.32
    win_rate: 0.43
  - name: Bumba's Golden Dagger
    pick_rate: 0.06
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-08-24'
  god_win_rate: 0.5276073619631901
  god_matches_won: 344
  god_matches_played: 652
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-24'
  god_matches_analyzed: 17273
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter,
    Eye of the Storm, Erosion, Berserker''s Shield, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Heartseeker, Leviathan''s
    Hide, Void Shield, Stampede, Ancile, Prophetic Cloak, Oni Hunter''s Garb, Runeforged
    Hammer.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.44
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.54
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.53
      pick: 0.45
      fit: 0.6
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.6
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Glorious Pridwen
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Glorious Pridwen, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion,
    The Reaper, Eye of Providence, Draconic Scale, Hydra''s Lament, Yogi''s Necklace,
    Avenging Blade, Phoenix Feather, Chandra''s Grace, Stone of Binding, Midgardian
    Mail, Daybreak Gavel, Magi''s Cloak, Leviathan''s Hide, Heartseeker, Void Shield,
    Runeforged Hammer.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.44
      fit: 0.3
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.68
    Glorious Pridwen:
      total: 0.58
      efficiency: 0.38
      win: 0.73
      pick: 0.11
      fit: 0.77
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.47
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Avenging Blade,
    Kinetic Cuirass, Screeching Gargoyle, Heartseeker, Void Shield, Shield Splitter,
    Void Stone, Titan''s Bane, Berserker''s Shield, The Crusher, Eye of the Storm,
    The Reaper, Erosion, Hydra''s Lament, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Pendulum Blade, Magi''s Cloak, Avatar''s Parashu, Mantle Of Discord,
    Midgardian Mail, Runeforged Hammer.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.48
      fit: 0.24
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.44
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.39
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Amanita Charm
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass,
    Golden Blade, Tyrfing, Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Shogun''s Ofuda, Silverbranch Bow, Erosion, Eye of Providence, Stone of Binding,
    Toxic Blade, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Tekko-Kagi,
    Runeforged Hammer.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.44
      fit: 0.21
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.21
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Glorious Pridwen
  - Freya's Tears
  flex_slots:
  - Glorious Pridwen
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Glorious Pridwen,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Eye
    of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Eye of the
    Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle Of Discord, Midgardian
    Mail, Daybreak Gavel, Chandra''s Grace, Leviathan''s Hide, Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.48
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.44
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.55
    Glorious Pridwen:
      total: 0.56
      efficiency: 0.38
      win: 0.73
      pick: 0.11
      fit: 0.64
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.64
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
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Runeforged Hammer, Eye of the Storm, Erosion, Berserker''s Shield, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone of
    Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching
    Gargoyle, Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile, Prophetic
    Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.54
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.53
      pick: 0.45
      fit: 0.6
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Glorious Pridwen
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Erosion, Jotunn''s Revenge, Kinetic Cuirass, Shield of
    the Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Shield Splitter,
    Eye of the Storm, Doublet of Binding, Berserker''s Shield, Eye of Providence,
    Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, Mystical Mail,
    Hydra''s Lament, Midgardian Mail, Sanguine Lash, Stone of Binding, Yogi''s Necklace,
    Phoenix Feather, Runeforged Hammer.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.44
      fit: 0.29
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.71
    Glorious Pridwen:
      total: 0.57
      efficiency: 0.38
      win: 0.73
      pick: 0.11
      fit: 0.68
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.57
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.91
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Glorious Pridwen
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Erosion, Shield of the Phoenix, Kinetic
    Cuirass, Void Shield, Stampede, Shield Splitter, Void Stone, Spectral Armor, Eye
    of the Storm, Doublet of Binding, Berserker''s Shield, The Reaper, Eye of Providence,
    Draconic Scale, Hydra''s Lament, Yogi''s Necklace, Avenging Blade, Shogun''s Ofuda,
    Phoenix Feather, Pharaoh''s Curse, Chandra''s Grace, Mystical Mail, Sanguine Lash,
    Runeforged Hammer.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.44
      fit: 0.3
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.68
    Glorious Pridwen:
      total: 0.58
      efficiency: 0.38
      win: 0.73
      pick: 0.11
      fit: 0.77
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.88
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, Void Shield, Void Stone, Erosion,
    Avenging Blade, Kinetic Cuirass, Stone of Binding, Shield of the Phoenix, The
    Reaper, Stampede, Screeching Gargoyle, Spectral Armor, Heartseeker, Doublet of
    Binding, Shield Splitter, Berserker''s Shield, Eye of the Storm, Titan''s Bane,
    The Crusher, Shogun''s Ofuda, Eye of Providence, Pharaoh''s Curse, Hydra''s Lament,
    Draconic Scale, Runeforged Hammer.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.55
    Void Shield:
      total: 0.56
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.56
      efficiency: 0.45
      win: 0.56
      pick: 0.0
      fit: 1.0
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.95
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.75
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Glorious Pridwen
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Erosion
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Pharaoh''s Curse, Shogun''s Ofuda,
    Erosion, Jotunn''s Revenge, Riptalon, Kinetic Cuirass, Golden Blade, Shield of
    the Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Doublet of Binding,
    Umbral Link, The Reaper, Tyrfing, Eros'' Bow, Shield Splitter, Sanguine Lash,
    Lernaean Bow, Toxic Blade, Eye of the Storm, Silverbranch Bow, Runeforged Hammer.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.48
    Glorious Pridwen:
      total: 0.54
      efficiency: 0.38
      win: 0.73
      pick: 0.11
      fit: 0.51
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.9
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.7
    Pharaoh's Curse:
      total: 0.55
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.54
      efficiency: 0.5
      win: 0.56
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
  - Freya's Tears
  - Erosion
  flex_slots:
  - Genji's Guard
  - Erosion
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Glorious Pridwen, Jotunn''s
    Revenge, Shield of the Phoenix, Erosion, Kinetic Cuirass, Void Shield, Stampede,
    Void Stone, Spectral Armor, Hydra''s Lament, Chandra''s Grace, Doublet of Binding,
    Screeching Gargoyle, Berserker''s Shield, Gladiator''s Shield, Shield Splitter,
    Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Draconic Scale, Eye of the
    Storm, Mystical Mail, Prophetic Cloak, Eye of Erebus, Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.48
      fit: 0.45
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.44
      fit: 0.45
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.44
    Glorious Pridwen:
      total: 0.59
      efficiency: 0.38
      win: 0.73
      pick: 0.11
      fit: 0.79
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.56
      pick: 0.15
      fit: 0.59
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.77
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
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.74
    Void Shield:
      total: 0.54
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.57
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.91
  starter: *id001
  aspect: Aspect of Preservation
---
