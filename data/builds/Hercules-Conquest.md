---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.25
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.33
    win_rate: 0.47
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.15
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.41
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.45
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.45
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.64
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.48
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.58
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.44
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.48
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.58
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.46
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.73
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.67
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.44
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.43
    win_rate: 0.63
  - name: Bumba's Cudgel
    pick_rate: 0.35
    win_rate: 0.32
  - name: Archmage's Gem
    pick_rate: 0.07
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-10-03'
  god_win_rate: 0.5068493150684932
  god_matches_won: 148
  god_matches_played: 292
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-10-03'
  god_matches_analyzed: 12830
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
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
    this god: Jotunn''s Revenge, Hydra''s Lament, Amanita Charm, Kinetic Cuirass,
    Shield Splitter, Runeforged Hammer, Eye of the Storm, Erosion, Berserker''s Shield,
    Eye of Providence, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Heartseeker, Hide
    of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Ancile, Prophetic
    Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.4
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.34
      fit: 0.33
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.7
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.12
      fit: 0.45
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.47
      pick: 0.27
      fit: 0.54
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Hydra's Lament
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Hydra''s Lament, Shield of the Phoenix,
    Kinetic Cuirass, Runeforged Hammer, Shield Splitter, Eye of the Storm, Berserker''s
    Shield, Erosion, The Reaper, Eye of Providence, Yogi''s Necklace, Avenging Blade,
    Phoenix Feather, Chandra''s Grace, Glorious Pridwen, Stone of Binding, Midgardian
    Mail, Daybreak Gavel, Hide of the Nemean Lion, Magi''s Cloak, Leviathan''s Hide,
    Heartseeker, Void Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.42
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.82
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.12
      fit: 0.47
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.47
      pick: 0.27
      fit: 0.47
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Transcendence
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
    for this god: Jotunn''s Revenge, Hydra''s Lament, Amanita Charm, Stone of Binding,
    Avenging Blade, Kinetic Cuirass, Screeching Gargoyle, Heartseeker, Void Shield,
    Shield Splitter, Void Stone, Runeforged Hammer, Titan''s Bane, Berserker''s Shield,
    The Crusher, Eye of the Storm, The Reaper, Erosion, Eye of Providence, Shield
    of the Phoenix, Magi''s Cloak, Pendulum Blade, Avatar''s Parashu, Mantle Of Discord,
    Midgardian Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.57
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.48
      pick: 0.34
      fit: 0.24
    Transcendence:
      total: 0.42
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.17
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.64
      pick: 0.12
      fit: 0.36
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.47
      pick: 0.27
      fit: 0.39
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Hydra''s Lament, Berserker''s Shield, Amanita Charm,
    Kinetic Cuirass, Golden Blade, Tyrfing, Shield Splitter, Pharaoh''s Curse, Runeforged
    Hammer, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Eye
    of Providence, Stone of Binding, Toxic Blade, Eye of the Storm, Shield of the
    Phoenix, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.21
    Tyrfing:
      total: 0.47
      efficiency: 0.48
      win: 0.47
      pick: 0.0
      fit: 0.55
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.64
      pick: 0.12
      fit: 0.28
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Shield
    Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Runeforged Hammer, Eye
    of Providence, Gladiator''s Shield, Stone of Binding, Eye of the Storm, Arondight,
    Magi''s Cloak, Eye of Erebus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel, Chandra''s Grace, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.45
      pick: 0.26
      fit: 0.48
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.48
      pick: 0.34
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.46
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.64
      pick: 0.12
      fit: 0.52
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.47
      pick: 0.27
      fit: 0.64
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
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
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Runeforged Hammer, Eye of the Storm, Erosion, Berserker''s Shield, Eye
    of Providence, Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s
    Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle,
    Hide of the Nemean Lion, Heartseeker, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.4
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.51
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.67
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.47
      pick: 0.33
      fit: 0.6
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.47
      pick: 0.27
      fit: 0.54
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.47
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
  - Kinetic Cuirass
  - Hydra's Lament
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Hydra''s Lament, Erosion, Kinetic
    Cuirass, Shield of the Phoenix, Void Shield, Stampede, Runeforged Hammer, Void
    Stone, Spectral Armor, Shield Splitter, Eye of the Storm, Doublet of Binding,
    Berserker''s Shield, Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Avenging
    Blade, Mystical Mail, Midgardian Mail, Sanguine Lash, Stone of Binding, Yogi''s
    Necklace, Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.39
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.71
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.12
      fit: 0.44
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.47
      pick: 0.33
      fit: 0.61
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hydra's Lament
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Hydra''s Lament, Erosion, Shield of
    the Phoenix, Kinetic Cuirass, Void Shield, Runeforged Hammer, Stampede, Shield
    Splitter, Void Stone, Spectral Armor, Eye of the Storm, Doublet of Binding, Berserker''s
    Shield, The Reaper, Eye of Providence, Yogi''s Necklace, Avenging Blade, Shogun''s
    Ofuda, Phoenix Feather, Pharaoh''s Curse, Chandra''s Grace, Mystical Mail, Sanguine
    Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.42
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.82
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.12
      fit: 0.47
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.52
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Void Stone
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Hydra''s Lament, Void Shield,
    Void Stone, Erosion, Avenging Blade, Kinetic Cuirass, Stone of Binding, Shield
    of the Phoenix, The Reaper, Stampede, Screeching Gargoyle, Spectral Armor, Runeforged
    Hammer, Heartseeker, Doublet of Binding, Shield Splitter, Berserker''s Shield,
    Eye of the Storm, Titan''s Bane, The Crusher, Shogun''s Ofuda, Eye of Providence,
    Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.55
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.64
      pick: 0.12
      fit: 0.35
    Void Shield:
      total: 0.53
      efficiency: 0.47
      win: 0.47
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.52
      efficiency: 0.45
      win: 0.47
      pick: 0.0
      fit: 1.0
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.95
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.75
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Berserker''s Shield, Pharaoh''s Curse,
    Shogun''s Ofuda, Erosion, Riptalon, Kinetic Cuirass, Golden Blade, Shield of the
    Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Doublet of Binding,
    Runeforged Hammer, Umbral Link, The Reaper, Tyrfing, Eros'' Bow, Shield Splitter,
    Sanguine Lash, Lernaean Bow, Toxic Blade, Eye of the Storm, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.21
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.64
      pick: 0.12
      fit: 0.28
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.5
      efficiency: 0.5
      win: 0.47
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Hydra''s Lament, Shield of the Phoenix, Erosion, Kinetic Cuirass, Void Shield,
    Stampede, Void Stone, Spectral Armor, Chandra''s Grace, Doublet of Binding, Screeching
    Gargoyle, Berserker''s Shield, Runeforged Hammer, Glorious Pridwen, Gladiator''s
    Shield, Shield Splitter, Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse,
    Eye of the Storm, Mystical Mail, Prophetic Cloak, Eye of Erebus.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.45
      pick: 0.26
      fit: 0.45
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.48
      pick: 0.34
      fit: 0.45
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.44
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.64
      pick: 0.12
      fit: 0.5
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.47
      pick: 0.27
      fit: 0.59
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.97
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
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
    Underrated for this god: Amanita Charm, Erosion, Jotunn''s Revenge, Kinetic Cuirass,
    Shield of the Phoenix, Void Shield, Stampede, Runeforged Hammer, Void Stone, Spectral
    Armor, Shield Splitter, Eye of the Storm, Doublet of Binding, Berserker''s Shield,
    Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, Mystical
    Mail, Hydra''s Lament, Midgardian Mail, Sanguine Lash, Stone of Binding, Yogi''s
    Necklace, Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.15
      fit: 0.39
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.74
    Void Shield:
      total: 0.5
      efficiency: 0.47
      win: 0.47
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
  aspect: Aspect of Preservation
---
