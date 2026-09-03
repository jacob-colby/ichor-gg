---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.33
  slot_order:
  - name: Stampede
    pick_rate: 0.2
    win_rate: 0.63
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.2
      win_rate: 0.62
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.65
    alternates:
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.61
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.2
      win_rate: 0.58
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.73
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.66
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.18
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.58
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.82
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.73
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.64
  - name: Legionnaire Armor
    pick_rate: 0.08
    win_rate: 0.82
    alternates:
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.75
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.74
  community_starters:
  - name: Selflessness
    pick_rate: 0.24
    win_rate: 0.62
  - name: Warrior's Axe
    pick_rate: 0.19
    win_rate: 0.55
  - name: Heroism
    pick_rate: 0.14
    win_rate: 0.77
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-09-02'
  god_win_rate: 0.6311188811188811
  god_matches_won: 361
  god_matches_played: 572
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-01'
  god_matches_analyzed: 8200
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
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
    this god: Draconic Scale, Breastplate of Valor, Amanita Charm, Kinetic Cuirass,
    Jotunn''s Revenge, Shield of the Phoenix, Erosion, Eye of Providence, Berserker''s
    Shield, Shield Splitter, Stone of Binding, Eye of the Storm, Runeforged Hammer,
    Screeching Gargoyle, Magi''s Cloak, Prophetic Cloak, Midgardian Mail, Mantle Of
    Discord, Hydra''s Lament, Hide of the Nemean Lion, Gladiator''s Shield, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Void Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.73
      pick: 0.14
      fit: 0.42
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.65
      pick: 0.33
      fit: 0.42
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.64
    Draconic Scale:
      total: 0.65
      efficiency: 0.5
      win: 0.82
      pick: 0.11
      fit: 0.66
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Draconic Scale, Shield of the Phoenix, Breastplate of
    Valor, Kinetic Cuirass, Jotunn''s Revenge, Berserker''s Shield, Erosion, Eye of
    Providence, Chandra''s Grace, Glorious Pridwen, Phoenix Feather, Shield Splitter,
    Runeforged Hammer, Yogi''s Necklace, Eye of the Storm, Midgardian Mail, Stone
    of Binding, Screeching Gargoyle, Hide of the Nemean Lion, Gladiator''s Shield,
    Leviathan''s Hide, Void Shield, Magi''s Cloak, Hydra''s Lament, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.73
      pick: 0.14
      fit: 0.39
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
      total: 0.61
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.59
    Draconic Scale:
      total: 0.65
      efficiency: 0.5
      win: 0.82
      pick: 0.11
      fit: 0.66
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Stone of Binding
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Draconic Scale, Breastplate of Valor, Amanita
    Charm, Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Void Shield, Void
    Stone, Avenging Blade, Heartseeker, Berserker''s Shield, Shield of the Phoenix,
    Shield Splitter, Erosion, Eye of Providence, Runeforged Hammer, Titan''s Bane,
    The Crusher, The Reaper, Eye of the Storm, Hydra''s Lament, Magi''s Cloak, Midgardian
    Mail, Pendulum Blade, Mantle Of Discord, Daybreak Gavel.'
  slot_scores:
    Stone of Binding:
      total: 0.58
      efficiency: 0.51
      win: 0.66
      pick: 0.0
      fit: 0.72
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.73
      pick: 0.14
      fit: 0.29
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.45
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.82
      pick: 0.11
      fit: 0.46
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Draconic Scale
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Berserker''s Shield, Breastplate of Valor, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Golden Blade, Tyrfing, Runeforged Hammer,
    Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s
    Ofuda, Hydra''s Lament, Shield of the Phoenix, Toxic Blade, Erosion, Eye of the
    Storm, Eye of Providence, Stone of Binding, Screeching Gargoyle, Daybreak Gavel,
    Magi''s Cloak, The Reaper, Tekko-Kagi.'
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
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.73
      pick: 0.14
      fit: 0.22
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
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.82
      pick: 0.11
      fit: 0.35
  community_ordered:
  - Breastplate of Valor
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Jotunn''s Revenge,
    Draconic Scale, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Hydra''s
    Lament, Screeching Gargoyle, Berserker''s Shield, Shield Splitter, Prophetic Cloak,
    Runeforged Hammer, Gladiator''s Shield, Erosion, Eye of Providence, Arondight,
    Eye of the Storm, Stone of Binding, Eye of Erebus, Magi''s Cloak, Chandra''s Grace,
    Midgardian Mail, Glorious Pridwen, Daybreak Gavel, Mantle Of Discord, Hide of
    the Nemean Lion, Avenging Blade.'
  slot_scores:
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.65
      win: 0.73
      pick: 0.14
      fit: 0.48
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.65
      pick: 0.33
      fit: 0.48
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.63
    Draconic Scale:
      total: 0.61
      efficiency: 0.5
      win: 0.82
      pick: 0.11
      fit: 0.43
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Breastplate
    of Valor, Shield of the Phoenix, Erosion, Eye of Providence, Berserker''s Shield,
    Shield Splitter, Draconic Scale, Stone of Binding, Eye of the Storm, Runeforged
    Hammer, Screeching Gargoyle, Magi''s Cloak, Prophetic Cloak, Midgardian Mail,
    Mantle Of Discord, Hydra''s Lament, Hide of the Nemean Lion, Gladiator''s Shield,
    Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Void Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.34
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.65
      pick: 0.33
      fit: 0.42
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.76
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.59
      pick: 0.19
      fit: 0.66
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.64
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
---
