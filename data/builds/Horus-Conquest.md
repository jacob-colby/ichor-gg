---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.0
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.38
    win_rate: 0.56
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.31
    - name: Runeforged Hammer
      pick_rate: 0.14
      win_rate: 0.62
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.4
    alternates:
    - name: Stampede
      pick_rate: 0.2
      win_rate: 0.53
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.29
  - name: Shell of Rebuke
    pick_rate: 0.19
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.38
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.38
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.43
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.64
    - name: Amanita Charm
      pick_rate: 0.06
      win_rate: 0.4
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.25
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.4
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.8
  - name: Veve Charm
    pick_rate: 0.15
    win_rate: 0.2
    alternates:
    - name: Engraved Guard
      pick_rate: 0.09
      win_rate: 0.33
    - name: Sage's Ring
      pick_rate: 0.09
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.31
    win_rate: 0.47
  - name: Warrior's Axe
    pick_rate: 0.2
    win_rate: 0.53
  - name: Heroism
    pick_rate: 0.15
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-10-22'
  god_win_rate: 0.4791666666666667
  god_matches_won: 46
  god_matches_played: 96
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-22'
  god_matches_analyzed: 1760
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Stampede
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Stampede
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge,
    Shifter''s Shield, Breastplate of Valor, Shield of the Phoenix, Erosion, Eye of
    Providence, Berserker''s Shield, Shield Splitter, Stone of Binding, Eye of the
    Storm, Screeching Gargoyle, Magi''s Cloak, Prophetic Cloak, Midgardian Mail, Mantle
    Of Discord, Hydra''s Lament, Hide of the Nemean Lion, Gladiator''s Shield, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Void Stone, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.43
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.43
      pick: 0.0
      fit: 0.76
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.14
      fit: 0.39
    Stampede:
      total: 0.5
      efficiency: 0.51
      win: 0.53
      pick: 0.27
      fit: 0.43
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.43
      pick: 0.28
      fit: 0.64
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.4
      pick: 0.1
      fit: 0.66
  community_ordered:
  - Runeforged Hammer
  - Stampede
  - Freya's Tears
  - Amanita Charm
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Stampede
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield of the Phoenix, Kinetic Cuirass,
    Jotunn''s Revenge, Shifter''s Shield, Breastplate of Valor, Berserker''s Shield,
    Erosion, Eye of Providence, Chandra''s Grace, Glorious Pridwen, Phoenix Feather,
    Shield Splitter, Yogi''s Necklace, Eye of the Storm, Midgardian Mail, Stone of
    Binding, Screeching Gargoyle, Hide of the Nemean Lion, Gladiator''s Shield, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Hydra''s Lament, Ancile, Draconic Scale.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.43
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.43
      pick: 0.0
      fit: 0.94
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.14
      fit: 0.45
    Stampede:
      total: 0.5
      efficiency: 0.51
      win: 0.53
      pick: 0.27
      fit: 0.46
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.43
      pick: 0.28
      fit: 0.59
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.4
      pick: 0.1
      fit: 0.96
  community_ordered:
  - Runeforged Hammer
  - Stampede
  - Freya's Tears
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Runeforged Hammer
  - Stampede
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Runeforged Hammer, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Screeching Gargoyle, Kinetic Cuirass, Breastplate of Valor, Void Shield, Void
    Stone, Avenging Blade, Shifter''s Shield, Heartseeker, Berserker''s Shield, Shield
    of the Phoenix, Shield Splitter, Erosion, Eye of Providence, Titan''s Bane, The
    Crusher, The Reaper, Eye of the Storm, Hydra''s Lament, Magi''s Cloak, Midgardian
    Mail, Pendulum Blade, Mantle Of Discord, Daybreak Gavel, Draconic Scale.'
  slot_scores:
    Stone of Binding:
      total: 0.48
      efficiency: 0.51
      win: 0.43
      pick: 0.0
      fit: 0.72
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.43
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.62
      pick: 0.14
      fit: 0.3
    Stampede:
      total: 0.48
      efficiency: 0.51
      win: 0.53
      pick: 0.27
      fit: 0.3
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.43
      pick: 0.28
      fit: 0.45
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.4
      pick: 0.1
      fit: 0.46
  community_ordered:
  - Runeforged Hammer
  - Stampede
  - Freya's Tears
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Runeforged Hammer
  - Freya's Tears
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Golden Blade, Breastplate of Valor, Tyrfing, Shifter''s Shield,
    Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s
    Ofuda, Hydra''s Lament, Shield of the Phoenix, Toxic Blade, Erosion, Eye of the
    Storm, Eye of Providence, Stone of Binding, Screeching Gargoyle, Daybreak Gavel,
    Magi''s Cloak, The Reaper, Tekko-Kagi, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.46
      efficiency: 0.52
      win: 0.43
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.43
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.43
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.44
      efficiency: 0.48
      win: 0.43
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.62
      pick: 0.14
      fit: 0.32
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.43
      pick: 0.28
      fit: 0.34
  community_ordered:
  - Runeforged Hammer
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Runeforged Hammer, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Hydra''s
    Lament, Screeching Gargoyle, Shifter''s Shield, Berserker''s Shield, Shield Splitter,
    Prophetic Cloak, Gladiator''s Shield, Erosion, Eye of Providence, Arondight, Eye
    of the Storm, Stone of Binding, Eye of Erebus, Magi''s Cloak, Chandra''s Grace,
    Midgardian Mail, Glorious Pridwen, Daybreak Gavel, Mantle Of Discord, Hide of
    the Nemean Lion, Avenging Blade, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.4
      pick: 0.29
      fit: 0.48
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.43
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.43
      pick: 0.0
      fit: 0.47
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.62
      pick: 0.14
      fit: 0.33
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.43
      pick: 0.28
      fit: 0.63
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.4
      pick: 0.1
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
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
      total: 0.49
      efficiency: 0.66
      win: 0.4
      pick: 0.29
      fit: 0.42
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.43
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.43
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.43
      pick: 0.28
      fit: 0.64
    Shifter's Shield:
      total: 0.49
      efficiency: 0.55
      win: 0.43
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.4
      pick: 0.1
      fit: 0.66
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Amanita Charm
  starter: *id001
---
