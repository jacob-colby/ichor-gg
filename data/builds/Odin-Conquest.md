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
    pick_rate: 0.41
    win_rate: 0.67
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.55
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.41
  - name: Breastplate of Valor
    pick_rate: 0.2
    win_rate: 0.67
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.15
      win_rate: 0.75
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.46
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.65
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.59
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.42
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.66
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.58
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.46
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.68
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.62
  - name: Shield
    pick_rate: 0.06
    win_rate: 0.2
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.83
    - name: Captain's Ring
      pick_rate: 0.03
      win_rate: 0.6
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.29
    win_rate: 0.7
  - name: Bumba's Cudgel
    pick_rate: 0.23
    win_rate: 0.57
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/odin/
  last_verified: '2026-09-21'
  god_win_rate: 0.5946843853820598
  god_matches_won: 179
  god_matches_played: 301
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-21'
  god_matches_analyzed: 15551
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Transcendence
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer,
    Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Stone of Binding, Heartseeker, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Titan''s Bane,
    The Crusher, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede,
    Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.67
      pick: 0.41
      fit: 0.46
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.29
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.21
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.75
      pick: 0.2
      fit: 0.41
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.49
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Hydra's Lament
  - Freya's Tears
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Transcendence
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Heartseeker, Berserker''s
    Shield, Eye of the Storm, Shield of the Phoenix, Erosion, Stone of Binding, Eye
    of Providence, Avenging Blade, Draconic Scale, Screeching Gargoyle, Magi''s Cloak,
    Titan''s Bane, The Crusher, Daybreak Gavel, Oni Hunter''s Garb, Transcendence,
    Midgardian Mail, Mantle Of Discord, The Reaper, Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.65
      pick: 0.3
      fit: 0.29
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.29
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.67
      pick: 0.41
      fit: 0.45
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.25
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.75
      pick: 0.2
      fit: 0.44
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Shield of the Phoenix
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Runeforged Hammer,
    The Reaper, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s
    Necklace, Eye of Providence, Draconic Scale, Phoenix Feather, Avenging Blade,
    Heartseeker, Chandra''s Grace, Glorious Pridwen, Stone of Binding, Midgardian
    Mail, Daybreak Gavel, Titan''s Bane, The Crusher, Magi''s Cloak, Hide of the Nemean
    Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.67
      pick: 0.41
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.27
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.77
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.75
      pick: 0.2
      fit: 0.42
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.43
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Kinetic Cuirass, Avenging Blade,
    Screeching Gargoyle, Void Shield, Heartseeker, Shield Splitter, Void Stone, Runeforged
    Hammer, Berserker''s Shield, Titan''s Bane, The Crusher, Eye of the Storm, The
    Reaper, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Magi''s
    Cloak, Pendulum Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.67
      pick: 0.41
      fit: 0.56
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.24
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.17
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.75
      pick: 0.2
      fit: 0.35
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Jotunn's Revenge
  - Breastplate of Valor
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Riptalon
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Golden Blade, Riptalon,
    Tyrfing, Silverbranch Bow, Shield Splitter, Runeforged Hammer, Pharaoh''s Curse,
    Lernaean Bow, Toxic Blade, Shogun''s Ofuda, Erosion, The Reaper, Stone of Binding,
    Eye of Providence, Eye of the Storm, Shield of the Phoenix, Tekko-Kagi, Draconic
    Scale, Magi''s Cloak, Heartseeker, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.42
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.19
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.41
      fit: 0.27
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.75
      pick: 0.2
      fit: 0.27
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.64
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
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
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield
    of the Phoenix, Screeching Gargoyle, Berserker''s Shield, Shield Splitter, Runeforged
    Hammer, Prophetic Cloak, Erosion, Eye of Providence, Stone of Binding, Gladiator''s
    Shield, Draconic Scale, Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus,
    Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Heartseeker, Pendulum Blade,
    Glorious Pridwen, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.65
      pick: 0.3
      fit: 0.44
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.44
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.67
      pick: 0.41
      fit: 0.5
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.75
      pick: 0.2
      fit: 0.48
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.59
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Stone of Binding, Heartseeker, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Titan''s Bane,
    The Crusher, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede,
    Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.67
      pick: 0.41
      fit: 0.46
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.65
      pick: 0.3
      fit: 0.29
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.57
      efficiency: 0.55
      win: 0.64
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.18
      fit: 0.49
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
