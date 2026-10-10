---
type: smite-build
god: Odin
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.4
    win_rate: 0.44
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.16
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.4
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.42
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.86
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.29
  - name: Genji's Guard
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.2
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.42
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.83
  - name: Brawler’s Beat Stick
    pick_rate: 0.06
    win_rate: 0.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.33
  - name: Sage's Ring
    pick_rate: 0.1
    win_rate: 0.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.0
    - name: Mote of Chaos
      pick_rate: 0.07
      win_rate: 0.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.26
    win_rate: 0.44
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.44
  - name: Bumba's Cudgel
    pick_rate: 0.15
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/odin/
  last_verified: '2026-10-10'
  god_win_rate: 0.5
  god_matches_won: 31
  god_matches_played: 62
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-10'
  god_matches_analyzed: 4063
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Genji''s Guard, Amanita Charm, Kinetic Cuirass, Shield
    Splitter, Runeforged Hammer, Eye of the Storm, Berserker''s Shield, Erosion, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Heartseeker,
    Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching
    Gargoyle, Titan''s Bane, The Crusher, Hide of the Nemean Lion, Leviathan''s Hide,
    Void Shield, Stampede, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.4
      fit: 0.46
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.29
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.43
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.67
      efficiency: 0.55
      win: 0.86
      pick: 0.15
      fit: 0.54
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.75
      pick: 0.12
      fit: 0.49
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.43
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Freya''s
    Tears, Genji''s Guard, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Heartseeker, Berserker''s Shield, Eye of the Storm, Shield of the Phoenix,
    Erosion, Stone of Binding, Eye of Providence, Avenging Blade, Draconic Scale,
    Screeching Gargoyle, Magi''s Cloak, Titan''s Bane, The Crusher, Daybreak Gavel,
    Oni Hunter''s Garb, Transcendence, Midgardian Mail, Mantle Of Discord, The Reaper,
    Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.4
      fit: 0.45
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.65
      win: 0.42
      pick: 0.26
      fit: 0.29
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.29
    Shifter's Shield:
      total: 0.64
      efficiency: 0.55
      win: 0.86
      pick: 0.15
      fit: 0.36
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.75
      pick: 0.12
      fit: 0.35
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.43
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Shield of the Phoenix
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Genji''s Guard, Amanita Charm, Shield of the Phoenix,
    Kinetic Cuirass, Runeforged Hammer, The Reaper, Shield Splitter, Eye of the Storm,
    Berserker''s Shield, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale,
    Phoenix Feather, Avenging Blade, Heartseeker, Chandra''s Grace, Glorious Pridwen,
    Stone of Binding, Midgardian Mail, Daybreak Gavel, Titan''s Bane, The Crusher,
    Hide of the Nemean Lion, Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.4
      fit: 0.48
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.27
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.53
      win: 0.43
      pick: 0.0
      fit: 0.77
    Shifter's Shield:
      total: 0.67
      efficiency: 0.55
      win: 0.86
      pick: 0.15
      fit: 0.52
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.12
      fit: 0.43
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.43
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Genji''s Guard, Amanita Charm, Stone of Binding,
    Kinetic Cuirass, Avenging Blade, Screeching Gargoyle, Void Shield, Heartseeker,
    Shield Splitter, Void Stone, Runeforged Hammer, Berserker''s Shield, Titan''s
    Bane, The Crusher, Eye of the Storm, The Reaper, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Magi''s Cloak, Pendulum Blade, Avatar''s Parashu,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.48
      efficiency: 0.51
      win: 0.43
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.4
      fit: 0.56
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.24
    Shifter's Shield:
      total: 0.65
      efficiency: 0.55
      win: 0.86
      pick: 0.15
      fit: 0.44
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.12
      fit: 0.39
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.43
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  - Riptalon
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Genji''s Guard, Berserker''s Shield, Amanita Charm,
    Kinetic Cuirass, Golden Blade, Riptalon, Tyrfing, Silverbranch Bow, Shield Splitter,
    Runeforged Hammer, Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Shogun''s Ofuda,
    Erosion, The Reaper, Stone of Binding, Eye of Providence, Eye of the Storm, Shield
    of the Phoenix, Tekko-Kagi, Draconic Scale, Magi''s Cloak, Heartseeker, Daybreak
    Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.45
      efficiency: 0.52
      win: 0.43
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.43
      pick: 0.0
      fit: 0.42
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.19
    Shifter's Shield:
      total: 0.64
      efficiency: 0.55
      win: 0.86
      pick: 0.15
      fit: 0.35
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.75
      pick: 0.12
      fit: 0.32
    Riptalon:
      total: 0.44
      efficiency: 0.51
      win: 0.43
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Genji's Guard
  - Shifter's Shield
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Amanita
    Charm, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Berserker''s
    Shield, Shield Splitter, Runeforged Hammer, Prophetic Cloak, Erosion, Eye of Providence,
    Stone of Binding, Gladiator''s Shield, Draconic Scale, Eye of the Storm, Arondight,
    Magi''s Cloak, Eye of Erebus, Mantle Of Discord, Midgardian Mail, Daybreak Gavel,
    Heartseeker, Pendulum Blade, Glorious Pridwen, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.4
      fit: 0.5
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.42
      pick: 0.26
      fit: 0.44
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.44
    Shifter's Shield:
      total: 0.65
      efficiency: 0.55
      win: 0.86
      pick: 0.15
      fit: 0.41
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.12
      fit: 0.59
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.43
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Freya''s Tears, Shield
    Splitter, Genji''s Guard, Runeforged Hammer, Eye of the Storm, Berserker''s Shield,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding,
    Heartseeker, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail,
    Screeching Gargoyle, Titan''s Bane, The Crusher, Hide of the Nemean Lion, Leviathan''s
    Hide, Void Shield, Stampede, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.4
      fit: 0.46
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.29
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.43
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.47
      efficiency: 0.55
      win: 0.43
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.75
      pick: 0.12
      fit: 0.49
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.43
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
