---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.02
  aspect_win_rate: 1.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.2
    win_rate: 0.23
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.44
    - name: Leviathan's Hide
      pick_rate: 0.09
      win_rate: 0.17
  - name: Breastplate of Valor
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.11
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.29
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.36
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.29
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.43
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.38
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.33
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.25
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.44
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.67
  - name: Veve Charm
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 0.0
    - name: Spirit Robe
      pick_rate: 0.08
      win_rate: 0.67
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.52
    win_rate: 0.5
  - name: Bumba's Cudgel
    pick_rate: 0.26
    win_rate: 0.18
  - name: Warrior's Axe
    pick_rate: 0.09
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-10-10'
  god_win_rate: 0.3939393939393939
  god_matches_won: 26
  god_matches_played: 66
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-10'
  god_matches_analyzed: 4063
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield Splitter
  - Transcendence
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Shield Splitter, Runeforged Hammer,
    Eye of the Storm, Erosion, Berserker''s Shield, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean
    Lion, Heartseeker, Void Shield, Stampede, Ancile, Prophetic Cloak, Oni Hunter''s
    Garb, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.32
      fit: 0.33
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.33
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.4
    Shield Splitter:
      total: 0.47
      efficiency: 0.55
      win: 0.4
      pick: 0.0
      fit: 0.67
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.4
      pick: 0.0
      fit: 0.24
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Spirit Robe
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Runeforged
    Hammer, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, The Reaper,
    Eye of Providence, Draconic Scale, Hydra''s Lament, Yogi''s Necklace, Avenging
    Blade, Phoenix Feather, Chandra''s Grace, Glorious Pridwen, Stone of Binding,
    Midgardian Mail, Hide of the Nemean Lion, Daybreak Gavel, Magi''s Cloak, Heartseeker,
    Void Shield, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.32
      fit: 0.3
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.3
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.42
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.4
      pick: 0.0
      fit: 0.25
    Spirit Robe:
      total: 0.53
      efficiency: 0.34
      win: 0.67
      pick: 0.25
      fit: 0.66
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Spirit Robe
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Spirit Robe
  flex_slots:
  - Stone of Binding
  - Transcendence
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Heartseeker, Void Shield, Shield Splitter, Void Stone, Runeforged
    Hammer, Titan''s Bane, Berserker''s Shield, The Crusher, Eye of the Storm, The
    Reaper, Erosion, Hydra''s Lament, Eye of Providence, Draconic Scale, Shield of
    the Phoenix, Magi''s Cloak, Pendulum Blade, Avatar''s Parashu, Mantle Of Discord,
    Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.46
      efficiency: 0.51
      win: 0.4
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.32
      fit: 0.24
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.57
    Transcendence:
      total: 0.39
      efficiency: 0.53
      win: 0.4
      pick: 0.0
      fit: 0.17
    Spirit Robe:
      total: 0.48
      efficiency: 0.34
      win: 0.67
      pick: 0.25
      fit: 0.31
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Spirit Robe
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Berserker''s Shield, Amanita Charm, Golden Blade,
    Tyrfing, Shield Splitter, Pharaoh''s Curse, Runeforged Hammer, Riptalon, Lernaean
    Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Eye of Providence, Stone of Binding,
    Toxic Blade, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.45
      efficiency: 0.52
      win: 0.4
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.32
      fit: 0.21
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.4
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.21
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.21
    Tyrfing:
      total: 0.43
      efficiency: 0.48
      win: 0.4
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Spirit Robe
  flex_slots:
  - Spirit Robe
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle, Shield Splitter,
    Berserker''s Shield, Prophetic Cloak, Erosion, Runeforged Hammer, Eye of Providence,
    Gladiator''s Shield, Draconic Scale, Stone of Binding, Eye of the Storm, Arondight,
    Magi''s Cloak, Eye of Erebus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel, Chandra''s Grace, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.32
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.48
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.46
    Hydra's Lament:
      total: 0.45
      efficiency: 0.54
      win: 0.4
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.36
      pick: 0.26
      fit: 0.64
    Spirit Robe:
      total: 0.48
      efficiency: 0.34
      win: 0.67
      pick: 0.25
      fit: 0.32
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Spirit Robe
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
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Shield Splitter, Runeforged
    Hammer, Eye of the Storm, Erosion, Berserker''s Shield, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s Cloak,
    Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide
    of the Nemean Lion, Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile,
    Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.4
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.56
      win: 0.25
      pick: 0.15
      fit: 0.7
    Shield Splitter:
      total: 0.47
      efficiency: 0.55
      win: 0.4
      pick: 0.0
      fit: 0.67
    Shifter's Shield:
      total: 0.4
      efficiency: 0.55
      win: 0.23
      pick: 0.2
      fit: 0.6
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.36
      pick: 0.26
      fit: 0.54
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Spirit Robe
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Jotunn''s Revenge, Erosion, Shield of the Phoenix, Void
    Shield, Stampede, Runeforged Hammer, Void Stone, Spectral Armor, Shield Splitter,
    Eye of the Storm, Doublet of Binding, Berserker''s Shield, Eye of Providence,
    Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, Mystical Mail,
    Hydra''s Lament, Midgardian Mail, Sanguine Lash, Stone of Binding, Yogi''s Necklace,
    Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.32
      fit: 0.29
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.29
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.39
    Spirit Robe:
      total: 0.52
      efficiency: 0.34
      win: 0.67
      pick: 0.25
      fit: 0.57
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.5
      efficiency: 0.51
      win: 0.4
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Spirit Robe
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Spirit Robe
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Erosion, Shield of the Phoenix, Void
    Shield, Runeforged Hammer, Stampede, Shield Splitter, Void Stone, Spectral Armor,
    Eye of the Storm, Doublet of Binding, Berserker''s Shield, The Reaper, Eye of
    Providence, Draconic Scale, Hydra''s Lament, Yogi''s Necklace, Avenging Blade,
    Shogun''s Ofuda, Phoenix Feather, Pharaoh''s Curse, Chandra''s Grace, Mystical
    Mail, Sanguine Lash.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.32
      fit: 0.3
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.3
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.42
    Spirit Robe:
      total: 0.53
      efficiency: 0.34
      win: 0.67
      pick: 0.25
      fit: 0.66
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.49
      efficiency: 0.51
      win: 0.4
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Spirit Robe
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, Void Shield, Void Stone, Erosion,
    Avenging Blade, Stone of Binding, Shield of the Phoenix, The Reaper, Stampede,
    Screeching Gargoyle, Spectral Armor, Runeforged Hammer, Heartseeker, Doublet of
    Binding, Shield Splitter, Berserker''s Shield, Eye of the Storm, Titan''s Bane,
    The Crusher, Shogun''s Ofuda, Eye of Providence, Pharaoh''s Curse, Hydra''s Lament,
    Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.32
      fit: 0.21
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.21
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.55
    Void Shield:
      total: 0.49
      efficiency: 0.47
      win: 0.4
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.49
      efficiency: 0.45
      win: 0.4
      pick: 0.0
      fit: 1.0
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Spirit Robe
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Pharaoh''s Curse,
    Shogun''s Ofuda, Erosion, Riptalon, Golden Blade, Shield of the Phoenix, Void
    Shield, Stampede, Void Stone, Spectral Armor, Doublet of Binding, Runeforged Hammer,
    Umbral Link, The Reaper, Tyrfing, Eros'' Bow, Shield Splitter, Sanguine Lash,
    Lernaean Bow, Toxic Blade, Eye of the Storm, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.4
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.32
      fit: 0.19
    Spirit Robe:
      total: 0.5
      efficiency: 0.34
      win: 0.67
      pick: 0.25
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.48
      efficiency: 0.51
      win: 0.4
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.47
      efficiency: 0.5
      win: 0.4
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Genji's Guard
  - Spirit Robe
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
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
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Jotunn''s Revenge,
    Shield of the Phoenix, Erosion, Void Shield, Stampede, Void Stone, Spectral Armor,
    Hydra''s Lament, Chandra''s Grace, Doublet of Binding, Screeching Gargoyle, Berserker''s
    Shield, Runeforged Hammer, Glorious Pridwen, Gladiator''s Shield, Shield Splitter,
    Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Draconic Scale, Eye of the
    Storm, Mystical Mail, Prophetic Cloak, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.32
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.16
      fit: 0.45
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.44
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.36
      pick: 0.26
      fit: 0.59
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.97
    Erosion:
      total: 0.47
      efficiency: 0.51
      win: 0.4
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
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
    Underrated for this god: Amanita Charm, Erosion, Jotunn''s Revenge, Shield of
    the Phoenix, Void Shield, Stampede, Runeforged Hammer, Void Stone, Spectral Armor,
    Shield Splitter, Eye of the Storm, Doublet of Binding, Berserker''s Shield, Eye
    of Providence, Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade,
    Mystical Mail, Hydra''s Lament, Midgardian Mail, Sanguine Lash, Stone of Binding,
    Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.44
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.56
      win: 0.25
      pick: 0.15
      fit: 0.71
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.53
      win: 0.4
      pick: 0.0
      fit: 0.74
    Void Shield:
      total: 0.47
      efficiency: 0.47
      win: 0.4
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.5
      efficiency: 0.51
      win: 0.4
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  starter: *id001
  aspect: Aspect of Preservation
---
