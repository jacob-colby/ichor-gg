---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.43
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.37
    win_rate: 0.57
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.48
    - name: Runeforged Hammer
      pick_rate: 0.12
      win_rate: 0.59
  - name: Stampede
    pick_rate: 0.22
    win_rate: 0.45
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.54
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 0.48
  - name: Shell of Rebuke
    pick_rate: 0.19
    win_rate: 0.61
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.58
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.54
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.65
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.56
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.43
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.47
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 0.9
    - name: Olmec Blue
      pick_rate: 0.07
      win_rate: 0.56
  community_starters:
  - name: Selflessness
    pick_rate: 0.32
    win_rate: 0.57
  - name: Warrior's Axe
    pick_rate: 0.16
    win_rate: 0.51
  - name: Heroism
    pick_rate: 0.12
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-10-26'
  god_win_rate: 0.5274390243902439
  god_matches_won: 173
  god_matches_played: 328
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-26'
  god_matches_analyzed: 6194
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shifter''s Shield,
    Breastplate of Valor, Shield of the Phoenix, Erosion, Runeforged Hammer, Eye of
    Providence, Berserker''s Shield, Shield Splitter, Stone of Binding, Eye of the
    Storm, Screeching Gargoyle, Magi''s Cloak, Midgardian Mail, Mantle Of Discord,
    Hydra''s Lament, Hide of the Nemean Lion, Gladiator''s Shield, Leviathan''s Hide,
    Void Shield, Ancile, Oni Hunter''s Garb, Void Stone, Draconic Scale, Prophetic
    Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.23
      fit: 0.42
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.54
      pick: 0.32
      fit: 0.64
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Jotunn''s Revenge,
    Shifter''s Shield, Breastplate of Valor, Runeforged Hammer, Berserker''s Shield,
    Erosion, Eye of Providence, Chandra''s Grace, Glorious Pridwen, Phoenix Feather,
    Shield Splitter, Yogi''s Necklace, Eye of the Storm, Midgardian Mail, Stone of
    Binding, Screeching Gargoyle, Hide of the Nemean Lion, Gladiator''s Shield, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Hydra''s Lament, Ancile, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.94
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.32
      fit: 0.59
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Kinetic Cuirass
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    Kinetic Cuirass, Breastplate of Valor, Void Shield, Void Stone, Avenging Blade,
    Runeforged Hammer, Shifter''s Shield, Heartseeker, Berserker''s Shield, Shield
    of the Phoenix, Shield Splitter, Erosion, Eye of Providence, Titan''s Bane, The
    Crusher, The Reaper, Eye of the Storm, Hydra''s Lament, Magi''s Cloak, Midgardian
    Mail, Pendulum Blade, Mantle Of Discord, Daybreak Gavel, Draconic Scale.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.69
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.72
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.32
      fit: 0.45
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Freya's Tears
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Breastplate of Valor, Tyrfing, Shifter''s Shield,
    Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s
    Ofuda, Hydra''s Lament, Shield of the Phoenix, Toxic Blade, Erosion, Eye of the
    Storm, Eye of Providence, Stone of Binding, Screeching Gargoyle, Daybreak Gavel,
    Magi''s Cloak, The Reaper, Tekko-Kagi, Draconic Scale.'
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
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.32
      fit: 0.34
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Freya's Tears
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Hydra''s Lament,
    Runeforged Hammer, Screeching Gargoyle, Shifter''s Shield, Berserker''s Shield,
    Shield Splitter, Gladiator''s Shield, Erosion, Eye of Providence, Arondight, Eye
    of the Storm, Stone of Binding, Eye of Erebus, Magi''s Cloak, Chandra''s Grace,
    Midgardian Mail, Glorious Pridwen, Daybreak Gavel, Mantle Of Discord, Hide of
    the Nemean Lion, Avenging Blade, Prophetic Cloak, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.23
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.54
      pick: 0.32
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Freya's Tears
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
    Shield, Breastplate of Valor, Shield of the Phoenix, Erosion, Eye of Providence,
    Berserker''s Shield, Shield Splitter, Draconic Scale, Stone of Binding, Eye of
    the Storm, Runeforged Hammer, Screeching Gargoyle, Magi''s Cloak, Prophetic Cloak,
    Midgardian Mail, Mantle Of Discord, Hydra''s Lament, Hide of the Nemean Lion,
    Gladiator''s Shield, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb,
    Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.23
      fit: 0.42
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.54
      pick: 0.32
      fit: 0.64
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
