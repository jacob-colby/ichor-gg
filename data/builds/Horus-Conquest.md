---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.2
    win_rate: 0.58
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.18
      win_rate: 0.64
    - name: Stampede
      pick_rate: 0.18
      win_rate: 0.65
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.62
    alternates:
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.66
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.61
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.7
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.17
      win_rate: 0.69
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.51
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.61
  - name: Veve Charm
    pick_rate: 0.09
    win_rate: 0.73
    alternates:
    - name: Legionnaire Armor
      pick_rate: 0.08
      win_rate: 0.79
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.73
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.22
    win_rate: 0.6
  - name: Selflessness
    pick_rate: 0.21
    win_rate: 0.7
  - name: Bluestone Pendant
    pick_rate: 0.12
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-08-30'
  god_win_rate: 0.6422976501305483
  god_matches_won: 246
  god_matches_played: 383
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-30'
  god_matches_analyzed: 5563
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shield of the Phoenix,
    Erosion, Eye of Providence, Berserker''s Shield, Shield Splitter, Draconic Scale,
    Stone of Binding, Eye of the Storm, Runeforged Hammer, Screeching Gargoyle, Magi''s
    Cloak, Prophetic Cloak, Midgardian Mail, Mantle Of Discord, Hydra''s Lament, Hide
    of the Nemean Lion, Gladiator''s Shield, Leviathan''s Hide, Void Shield, Ancile,
    Oni Hunter''s Garb, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.62
      pick: 0.33
      fit: 0.42
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.16
      fit: 0.42
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.64
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.66
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Jotunn''s Revenge,
    Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale, Chandra''s Grace,
    Glorious Pridwen, Phoenix Feather, Shield Splitter, Runeforged Hammer, Yogi''s
    Necklace, Eye of the Storm, Midgardian Mail, Stone of Binding, Screeching Gargoyle,
    Hide of the Nemean Lion, Gladiator''s Shield, Leviathan''s Hide, Void Shield,
    Magi''s Cloak, Hydra''s Lament, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.16
      fit: 0.39
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.62
      efficiency: 0.53
      win: 0.66
      pick: 0.0
      fit: 0.94
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.59
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    Kinetic Cuirass, Void Shield, Void Stone, Avenging Blade, Heartseeker, Berserker''s
    Shield, Shield of the Phoenix, Shield Splitter, Erosion, Eye of Providence, Draconic
    Scale, Runeforged Hammer, Titan''s Bane, The Crusher, The Reaper, Eye of the Storm,
    Hydra''s Lament, Magi''s Cloak, Midgardian Mail, Pendulum Blade, Mantle Of Discord,
    Daybreak Gavel.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.58
      efficiency: 0.51
      win: 0.66
      pick: 0.0
      fit: 0.69
    Stone of Binding:
      total: 0.58
      efficiency: 0.51
      win: 0.66
      pick: 0.0
      fit: 0.72
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.16
      fit: 0.29
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.45
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Freya's Tears
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Tyrfing, Runeforged Hammer, Shield Splitter, Pharaoh''s Curse, Riptalon,
    Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the
    Phoenix, Toxic Blade, Erosion, Eye of the Storm, Eye of Providence, Stone of Binding,
    Draconic Scale, Screeching Gargoyle, Daybreak Gavel, Magi''s Cloak, The Reaper,
    Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.66
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.66
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.34
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Shield of the Phoenix, Kinetic Cuirass, Hydra''s Lament, Screeching Gargoyle,
    Berserker''s Shield, Shield Splitter, Prophetic Cloak, Runeforged Hammer, Gladiator''s
    Shield, Erosion, Eye of Providence, Arondight, Draconic Scale, Eye of the Storm,
    Stone of Binding, Eye of Erebus, Magi''s Cloak, Chandra''s Grace, Midgardian Mail,
    Glorious Pridwen, Daybreak Gavel, Mantle Of Discord, Hide of the Nemean Lion,
    Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.62
      pick: 0.33
      fit: 0.48
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.16
      fit: 0.48
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.63
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.43
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shield
    of the Phoenix, Erosion, Eye of Providence, Berserker''s Shield, Shield Splitter,
    Draconic Scale, Stone of Binding, Eye of the Storm, Runeforged Hammer, Screeching
    Gargoyle, Magi''s Cloak, Prophetic Cloak, Midgardian Mail, Mantle Of Discord,
    Hydra''s Lament, Hide of the Nemean Lion, Gladiator''s Shield, Leviathan''s Hide,
    Void Shield, Ancile, Oni Hunter''s Garb, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.62
      pick: 0.33
      fit: 0.42
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.7
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.2
      fit: 0.66
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.66
  starter: *id001
---
