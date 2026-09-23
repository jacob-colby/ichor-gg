---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.0
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.32
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.91
    - name: Chandra's Grace
      pick_rate: 0.11
      win_rate: 0.86
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.8
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.17
      win_rate: 0.82
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.86
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.89
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.67
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.67
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 1.0
  - name: Medallion
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Circle of Protection
      pick_rate: 0.1
      win_rate: 1.0
    - name: Spirit Robe
      pick_rate: 0.1
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.32
    win_rate: 0.7
  - name: Heroism
    pick_rate: 0.14
    win_rate: 0.89
  - name: Warrior's Axe
    pick_rate: 0.13
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-09-23'
  god_win_rate: 0.6666666666666666
  god_matches_won: 42
  god_matches_played: 63
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spirit Robe
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shifter''s Shield,
    Shield of the Phoenix, Erosion, Eye of Providence, Berserker''s Shield, Shield
    Splitter, Draconic Scale, Stone of Binding, Eye of the Storm, Runeforged Hammer,
    Screeching Gargoyle, Magi''s Cloak, Prophetic Cloak, Midgardian Mail, Mantle Of
    Discord, Hydra''s Lament, Gladiator''s Shield, Leviathan''s Hide, Void Shield,
    Ancile, Oni Hunter''s Garb, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.8
      pick: 0.33
      fit: 0.42
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.76
    Spirit Robe:
      total: 0.65
      efficiency: 0.34
      win: 1.0
      pick: 0.31
      fit: 0.46
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.64
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Genji's Guard
  - Spirit Robe
  - Freya's Tears
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spirit Robe
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Chandra''s Grace, Shield of the Phoenix, Kinetic Cuirass,
    Jotunn''s Revenge, Shifter''s Shield, Berserker''s Shield, Erosion, Eye of Providence,
    Draconic Scale, Glorious Pridwen, Phoenix Feather, Shield Splitter, Runeforged
    Hammer, Yogi''s Necklace, Eye of the Storm, Midgardian Mail, Stone of Binding,
    Screeching Gargoyle, Gladiator''s Shield, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Hydra''s Lament, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.66
      efficiency: 0.66
      win: 0.8
      pick: 0.33
      fit: 0.39
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.76
    Spirit Robe:
      total: 0.69
      efficiency: 0.34
      win: 1.0
      pick: 0.31
      fit: 0.71
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.59
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Genji's Guard
  - Spirit Robe
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Spirit Robe
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    Kinetic Cuirass, Void Shield, Void Stone, Avenging Blade, Shifter''s Shield, Heartseeker,
    Berserker''s Shield, Shield of the Phoenix, Shield Splitter, Erosion, Eye of Providence,
    Draconic Scale, Runeforged Hammer, Titan''s Bane, The Crusher, The Reaper, Eye
    of the Storm, Hydra''s Lament, Magi''s Cloak, Midgardian Mail, Pendulum Blade,
    Mantle Of Discord, Daybreak Gavel.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.58
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.69
    Stone of Binding:
      total: 0.59
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.8
      pick: 0.33
      fit: 0.29
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.45
    Spirit Robe:
      total: 0.63
      efficiency: 0.34
      win: 1.0
      pick: 0.31
      fit: 0.32
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spirit Robe
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Spirit Robe
  flex_slots:
  - Golden Blade
  - Tyrfing
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
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Tyrfing, Shifter''s Shield, Runeforged Hammer, Shield Splitter,
    Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Hydra''s
    Lament, Shield of the Phoenix, Toxic Blade, Erosion, Eye of the Storm, Eye of
    Providence, Stone of Binding, Draconic Scale, Screeching Gargoyle, Daybreak Gavel,
    Magi''s Cloak, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.33
      fit: 0.22
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.67
      pick: 0.0
      fit: 0.55
    Spirit Robe:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.31
      fit: 0.24
  community_ordered:
  - Genji's Guard
  - Spirit Robe
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Freya's Tears
  - Spirit Robe
  flex_slots:
  - Kinetic Cuirass
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Chandra''s Grace,
    Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Hydra''s Lament, Screeching
    Gargoyle, Shifter''s Shield, Berserker''s Shield, Shield Splitter, Prophetic Cloak,
    Runeforged Hammer, Gladiator''s Shield, Erosion, Eye of Providence, Arondight,
    Draconic Scale, Eye of the Storm, Stone of Binding, Eye of Erebus, Magi''s Cloak,
    Midgardian Mail, Glorious Pridwen, Daybreak Gavel, Mantle Of Discord, Avenging
    Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.68
      efficiency: 0.66
      win: 0.8
      pick: 0.33
      fit: 0.48
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.53
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.63
    Spirit Robe:
      total: 0.63
      efficiency: 0.34
      win: 1.0
      pick: 0.31
      fit: 0.3
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spirit Robe
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shifter''s
    Shield, Shield of the Phoenix, Erosion, Eye of Providence, Berserker''s Shield,
    Shield Splitter, Draconic Scale, Stone of Binding, Eye of the Storm, Runeforged
    Hammer, Screeching Gargoyle, Magi''s Cloak, Prophetic Cloak, Midgardian Mail,
    Mantle Of Discord, Hydra''s Lament, Gladiator''s Shield, Leviathan''s Hide, Void
    Shield, Ancile, Oni Hunter''s Garb, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.8
      pick: 0.33
      fit: 0.42
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.64
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
