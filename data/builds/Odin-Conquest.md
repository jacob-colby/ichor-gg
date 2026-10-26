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
    pick_rate: 0.6
    win_rate: 0.59
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.53
    - name: Devourer's Gauntlet
      pick_rate: 0.06
      win_rate: 0.45
  - name: Hydra's Lament
    pick_rate: 0.19
    win_rate: 0.7
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.19
      win_rate: 0.61
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.68
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Transcendence
      pick_rate: 0.15
      win_rate: 0.71
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.41
  - name: Heartseeker
    pick_rate: 0.14
    win_rate: 0.8
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.56
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.67
  - name: Brawler’s Beat Stick
    pick_rate: 0.08
    win_rate: 0.69
    alternates:
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.7
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.86
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.06
      win_rate: 0.71
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.31
    win_rate: 0.65
  - name: Bumba's Cudgel
    pick_rate: 0.18
    win_rate: 0.34
  - name: Bluestone Brooch
    pick_rate: 0.12
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/odin/
  last_verified: '2026-10-26'
  god_win_rate: 0.5751295336787565
  god_matches_won: 111
  god_matches_played: 193
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-26'
  god_matches_analyzed: 6194
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Transcendence
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer,
    Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Avenging Blade, Mantle
    Of Discord, The Crusher, Midgardian Mail, Screeching Gargoyle, Titan''s Bane,
    Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Daybreak Gavel,
    Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.59
      pick: 0.6
      fit: 0.46
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.64
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.23
      fit: 0.21
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.86
      pick: 0.18
      fit: 0.49
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.8
      pick: 0.23
      fit: 0.56
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Transcendence
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Berserker''s Shield,
    Eye of the Storm, Shield of the Phoenix, Erosion, Stone of Binding, Eye of Providence,
    Avenging Blade, Draconic Scale, The Crusher, Screeching Gargoyle, Magi''s Cloak,
    Titan''s Bane, Daybreak Gavel, Oni Hunter''s Garb, Midgardian Mail, Mantle Of
    Discord, The Reaper, Arondight, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.59
      pick: 0.6
      fit: 0.45
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.23
      fit: 0.25
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.7
      pick: 0.26
      fit: 0.44
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.86
      pick: 0.18
      fit: 0.35
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.8
      pick: 0.23
      fit: 0.56
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Transcendence
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Transcendence
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Runeforged Hammer,
    The Reaper, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s
    Necklace, Eye of Providence, Draconic Scale, Phoenix Feather, Avenging Blade,
    Chandra''s Grace, Glorious Pridwen, Stone of Binding, The Crusher, Midgardian
    Mail, Daybreak Gavel, Titan''s Bane, Hide of the Nemean Lion, Magi''s Cloak, Shifter''s
    Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.59
      pick: 0.6
      fit: 0.48
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.77
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.23
      fit: 0.21
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.86
      pick: 0.18
      fit: 0.43
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.8
      pick: 0.23
      fit: 0.57
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Transcendence
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Kinetic Cuirass, Avenging Blade,
    Screeching Gargoyle, Void Shield, Shield Splitter, Void Stone, Runeforged Hammer,
    The Crusher, Berserker''s Shield, Titan''s Bane, Eye of the Storm, The Reaper,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak,
    Pendulum Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail, Shifter''s
    Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.59
      pick: 0.6
      fit: 0.56
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.71
      pick: 0.23
      fit: 0.17
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.86
      pick: 0.18
      fit: 0.39
    Heartseeker:
      total: 0.64
      efficiency: 0.47
      win: 0.8
      pick: 0.23
      fit: 0.68
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Freya's Tears
  - Riptalon
  - Heartseeker
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Golden Blade, Riptalon,
    Tyrfing, Silverbranch Bow, Shield Splitter, Runeforged Hammer, Pharaoh''s Curse,
    Lernaean Bow, Toxic Blade, Shogun''s Ofuda, Erosion, The Reaper, Stone of Binding,
    Eye of Providence, Eye of the Storm, Shield of the Phoenix, Tekko-Kagi, Draconic
    Scale, Magi''s Cloak, Daybreak Gavel, Shifter''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.52
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.6
      fit: 0.27
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.86
      pick: 0.18
      fit: 0.32
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.48
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.8
      pick: 0.23
      fit: 0.4
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Transcendence
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield
    of the Phoenix, Screeching Gargoyle, Berserker''s Shield, Shield Splitter, Runeforged
    Hammer, Prophetic Cloak, Erosion, Eye of Providence, Stone of Binding, Gladiator''s
    Shield, Draconic Scale, Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus,
    Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Pendulum Blade, Glorious Pridwen,
    Hide of the Nemean Lion, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.59
      pick: 0.6
      fit: 0.5
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.71
      pick: 0.23
      fit: 0.09
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.7
      pick: 0.26
      fit: 0.48
    Freya's Tears:
      total: 0.7
      efficiency: 0.61
      win: 0.86
      pick: 0.18
      fit: 0.59
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.8
      pick: 0.23
      fit: 0.41
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Heartseeker
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Shifter''s
    Shield, Runeforged Hammer, Eye of the Storm, Berserker''s Shield, Erosion, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Magi''s
    Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle,
    Titan''s Bane, The Crusher, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield,
    Stampede, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.59
      pick: 0.6
      fit: 0.46
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.26
      fit: 0.29
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.86
      pick: 0.18
      fit: 0.49
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
