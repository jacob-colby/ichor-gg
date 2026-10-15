---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.25
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.15
    win_rate: 0.41
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.4
    - name: Devourer's Gauntlet
      pick_rate: 0.1
      win_rate: 0.68
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.43
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.35
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.53
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.42
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.41
  - name: Genji's Guard
    pick_rate: 0.1
    win_rate: 0.58
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.55
    - name: Contagion
      pick_rate: 0.06
      win_rate: 0.2
  - name: Shifter's Shield
    pick_rate: 0.05
    win_rate: 0.75
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.47
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.5
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.6
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.46
    win_rate: 0.56
  - name: Bumba's Cudgel
    pick_rate: 0.3
    win_rate: 0.27
  - name: Warrior's Axe
    pick_rate: 0.07
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-10-15'
  god_win_rate: 0.4497354497354497
  god_matches_won: 85
  god_matches_played: 189
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-15'
  god_matches_analyzed: 9899
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Jotunn''s Revenge, Hydra''s Lament, Runeforged Hammer, Eye of the Storm, Erosion,
    Berserker''s Shield, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s
    Hide, Void Shield, Stampede, Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.58
      pick: 0.17
      fit: 0.33
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.47
      pick: 0.25
      fit: 0.54
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.75
      pick: 0.11
      fit: 0.6
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, Shield Splitter, Jotunn''s Revenge, Hydra''s Lament, Eye of
    the Storm, Berserker''s Shield, Erosion, The Reaper, Eye of Providence, Draconic
    Scale, Yogi''s Necklace, Avenging Blade, Phoenix Feather, Chandra''s Grace, Glorious
    Pridwen, Stone of Binding, Midgardian Mail, Hide of the Nemean Lion, Daybreak
    Gavel, Magi''s Cloak, Leviathan''s Hide, Heartseeker, Void Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.17
      fit: 0.3
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.47
      pick: 0.25
      fit: 0.47
    Shifter's Shield:
      total: 0.62
      efficiency: 0.55
      win: 0.75
      pick: 0.11
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Shifter''s Shield, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Avenging Blade, Kinetic Cuirass, Screeching Gargoyle, Heartseeker, Void Shield,
    Shield Splitter, Hydra''s Lament, Void Stone, Runeforged Hammer, Titan''s Bane,
    Berserker''s Shield, The Crusher, Eye of the Storm, The Reaper, Erosion, Eye of
    Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak, Pendulum Blade,
    Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.17
      fit: 0.24
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.41
      pick: 0.15
      fit: 0.57
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.11
      fit: 0.43
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Shifter's Shield
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Hydra''s Lament, Tyrfing, Jotunn''s Revenge, Shield Splitter, Pharaoh''s
    Curse, Runeforged Hammer, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch
    Bow, Erosion, Eye of Providence, Stone of Binding, Toxic Blade, Eye of the Storm,
    Shield of the Phoenix, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak
    Gavel, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.17
      fit: 0.21
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.75
      pick: 0.11
      fit: 0.38
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Hydra's Lament
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Amanita Charm,
    Hydra''s Lament, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix, Screeching
    Gargoyle, Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Runeforged
    Hammer, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Hide of the
    Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.41
      pick: 0.15
      fit: 0.46
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.58
      pick: 0.17
      fit: 0.48
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.53
      pick: 0.12
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.47
      pick: 0.25
      fit: 0.64
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.11
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Hydra's Lament
  - Freya's Tears
  - Shifter's Shield
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
    Splitter, Shifter''s Shield, Runeforged Hammer, Eye of the Storm, Erosion, Berserker''s
    Shield, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament,
    Stone of Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s
    Hide, Void Shield, Stampede, Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.41
      pick: 0.15
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
      total: 0.52
      efficiency: 0.61
      win: 0.47
      pick: 0.25
      fit: 0.54
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.75
      pick: 0.11
      fit: 0.6
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Erosion, Kinetic Cuirass, Shield of
    the Phoenix, Void Shield, Stampede, Runeforged Hammer, Void Stone, Spectral Armor,
    Shield Splitter, Eye of the Storm, Doublet of Binding, Hydra''s Lament, Jotunn''s
    Revenge, Berserker''s Shield, Eye of Providence, Draconic Scale, Shogun''s Ofuda,
    Pharaoh''s Curse, Avenging Blade, Mystical Mail, Midgardian Mail, Sanguine Lash,
    Stone of Binding, Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.17
      fit: 0.29
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.74
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.75
      pick: 0.11
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
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Shifter's Shield
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
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Erosion, Shield of the Phoenix, Kinetic
    Cuirass, Void Shield, Runeforged Hammer, Stampede, Shield Splitter, Jotunn''s
    Revenge, Hydra''s Lament, Void Stone, Spectral Armor, Eye of the Storm, Doublet
    of Binding, Berserker''s Shield, The Reaper, Eye of Providence, Draconic Scale,
    Yogi''s Necklace, Avenging Blade, Shogun''s Ofuda, Phoenix Feather, Pharaoh''s
    Curse, Chandra''s Grace, Mystical Mail, Sanguine Lash.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.17
      fit: 0.3
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.62
      efficiency: 0.55
      win: 0.75
      pick: 0.11
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
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Void Shield
  - Shifter's Shield
  - Void Stone
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
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
    for this god: Shifter''s Shield, Amanita Charm, Void Shield, Void Stone, Jotunn''s
    Revenge, Erosion, Avenging Blade, Kinetic Cuirass, Stone of Binding, Shield of
    the Phoenix, The Reaper, Stampede, Screeching Gargoyle, Spectral Armor, Runeforged
    Hammer, Heartseeker, Hydra''s Lament, Doublet of Binding, Shield Splitter, Berserker''s
    Shield, Eye of the Storm, Titan''s Bane, The Crusher, Shogun''s Ofuda, Eye of
    Providence, Pharaoh''s Curse, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.41
      pick: 0.15
      fit: 0.55
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.17
      fit: 0.21
    Void Shield:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 1.0
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.11
      fit: 0.45
    Void Stone:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Shifter's Shield
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
    this god: Shifter''s Shield, Amanita Charm, Berserker''s Shield, Pharaoh''s Curse,
    Shogun''s Ofuda, Erosion, Riptalon, Kinetic Cuirass, Golden Blade, Shield of the
    Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Doublet of Binding,
    Runeforged Hammer, Umbral Link, The Reaper, Tyrfing, Jotunn''s Revenge, Eros''
    Bow, Shield Splitter, Sanguine Lash, Lernaean Bow, Toxic Blade, Eye of the Storm,
    Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.17
      fit: 0.19
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.11
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
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Shield of the Phoenix
  - Genji's Guard
  - Hydra's Lament
  - Freya's Tears
  - Shifter's Shield
  - Erosion
  flex_slots:
  - Erosion
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Amanita Charm,
    Shield of the Phoenix, Erosion, Hydra''s Lament, Jotunn''s Revenge, Kinetic Cuirass,
    Void Shield, Stampede, Void Stone, Spectral Armor, Chandra''s Grace, Doublet of
    Binding, Screeching Gargoyle, Berserker''s Shield, Runeforged Hammer, Glorious
    Pridwen, Gladiator''s Shield, Shield Splitter, Eye of Providence, Shogun''s Ofuda,
    Pharaoh''s Curse, Draconic Scale, Eye of the Storm, Mystical Mail, Prophetic Cloak,
    Eye of Erebus.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.84
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.58
      pick: 0.17
      fit: 0.45
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.53
      pick: 0.12
      fit: 0.5
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.47
      pick: 0.25
      fit: 0.59
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.75
      pick: 0.11
      fit: 0.47
    Erosion:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Genji's Guard
  - Hydra's Lament
  - Freya's Tears
  - Shifter's Shield
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
    Shield of the Phoenix, Void Shield, Stampede, Shifter''s Shield, Runeforged Hammer,
    Void Stone, Spectral Armor, Shield Splitter, Eye of the Storm, Doublet of Binding,
    Berserker''s Shield, Eye of Providence, Draconic Scale, Shogun''s Ofuda, Pharaoh''s
    Curse, Avenging Blade, Mystical Mail, Hydra''s Lament, Midgardian Mail, Sanguine
    Lash, Stone of Binding, Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.41
      pick: 0.15
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
