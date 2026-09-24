---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.2
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.26
    win_rate: 0.44
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.16
      win_rate: 0.33
    - name: Devourer's Gauntlet
      pick_rate: 0.16
      win_rate: 0.43
  - name: Shifter's Shield
    pick_rate: 0.21
    win_rate: 0.43
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.36
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.5
  - name: The Crusher
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.6
    - name: The Reaper
      pick_rate: 0.08
      win_rate: 0.4
  - name: Heartseeker
    pick_rate: 0.12
    win_rate: 0.2
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.86
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.6
  - name: Lucerne Hammer
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Olmec Blue
      pick_rate: 0.07
      win_rate: 0.2
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.75
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.26
    win_rate: 0.56
  - name: Bumba's Cudgel
    pick_rate: 0.21
    win_rate: 0.22
  - name: Hunter's Cowl
    pick_rate: 0.11
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-09-24'
  god_win_rate: 0.45038167938931295
  god_matches_won: 59
  god_matches_played: 131
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Hide of the Nemean Lion, Amanita Charm, Runeforged
    Hammer, Freya''s Tears, Shield Splitter, Eye of the Storm, Breastplate of Valor,
    Hydra''s Lament, Berserker''s Shield, Avenging Blade, The Crusher, Shield of the
    Phoenix, Titan''s Bane, Erosion, Eye of Providence, Draconic Scale, Pendulum Blade,
    Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone of Binding,
    Avatar''s Parashu, The Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.26
      fit: 0.58
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.12
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.31
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Kinetic
    Cuirass, Hide of the Nemean Lion, Amanita Charm, Breastplate of Valor, Hydra''s
    Lament, Runeforged Hammer, Freya''s Tears, Shield Splitter, Eye of the Storm,
    Berserker''s Shield, The Crusher, Avenging Blade, Titan''s Bane, Shield of the
    Phoenix, Transcendence, Arondight, Screeching Gargoyle, Erosion, Eye of Providence,
    Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian
    Mail, The Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.25
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.26
      fit: 0.52
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.12
      fit: 0.37
    Hide of the Nemean Lion:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.19
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Kinetic Cuirass, Hide of the Nemean Lion, Amanita Charm, Freya''s Tears,
    Breastplate of Valor, Runeforged Hammer, Hydra''s Lament, The Crusher, Berserker''s
    Shield, Shield of the Phoenix, Titan''s Bane, Shield Splitter, Eye of the Storm,
    Pendulum Blade, Avenging Blade, Screeching Gargoyle, Arondight, Erosion, Eye of
    Providence, Draconic Scale, Avatar''s Parashu, Stone of Binding, Midgardian Mail,
    Leviathan''s Hide, The Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.26
      fit: 0.56
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.12
      fit: 0.39
    Hide of the Nemean Lion:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.21
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.5
      pick: 0.12
      fit: 0.32
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Hide of the Nemean Lion, Shield of the
    Phoenix, Freya''s Tears, Runeforged Hammer, Shield Splitter, Breastplate of Valor,
    Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye of Providence,
    Hydra''s Lament, Draconic Scale, Phoenix Feather, Avenging Blade, Chandra''s Grace,
    The Crusher, Glorious Pridwen, Stone of Binding, Midgardian Mail, Titan''s Bane,
    The Reaper, Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.26
      fit: 0.49
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.6
      pick: 0.12
      fit: 0.61
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.76
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.36
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.12
      fit: 0.42
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    for this god: Kinetic Cuirass, Avenging Blade, Amanita Charm, The Crusher, Screeching
    Gargoyle, Titan''s Bane, Runeforged Hammer, Stone of Binding, Freya''s Tears,
    Void Shield, Breastplate of Valor, Void Stone, Hydra''s Lament, Shield Splitter,
    Pendulum Blade, Eye of the Storm, Berserker''s Shield, Avatar''s Parashu, Shield
    of the Phoenix, Tekko-Kagi, Erosion, Eye of Providence, Draconic Scale, Arondight,
    The Reaper.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.44
      pick: 0.26
      fit: 0.67
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.12
      fit: 0.43
    Hide of the Nemean Lion:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.24
    The Crusher:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.14
      fit: 0.67
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - The Crusher
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Berserker''s Shield, Golden Blade, Amanita Charm, Riptalon,
    Tyrfing, Silverbranch Bow, Freya''s Tears, Breastplate of Valor, Toxic Blade,
    Runeforged Hammer, Lernaean Bow, Pharaoh''s Curse, Tekko-Kagi, Shogun''s Ofuda,
    Hydra''s Lament, Shield Splitter, Eye of the Storm, Shield of the Phoenix, Avenging
    Blade, Dominance, Erosion, Eye of Providence, Screeching Gargoyle, The Reaper.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.44
      pick: 0.26
      fit: 0.31
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.12
      fit: 0.36
    Hide of the Nemean Lion:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.19
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  flex_slots:
  - Hide of the Nemean Lion
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Freya''s Tears, Breastplate
    of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Screeching Gargoyle,
    Runeforged Hammer, Berserker''s Shield, Arondight, Gladiator''s Shield, Eye of
    Erebus, Pendulum Blade, Shield Splitter, Prophetic Cloak, Chandra''s Grace, Eye
    of the Storm, Erosion, Eye of Providence, Avenging Blade, The Crusher, Draconic
    Scale, Midgardian Mail, Stone of Binding, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.26
      fit: 0.59
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.12
      fit: 0.41
    Hide of the Nemean Lion:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.22
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.12
      fit: 0.52
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Freya''s
    Tears, Shield Splitter, Eye of the Storm, Breastplate of Valor, Hydra''s Lament,
    Berserker''s Shield, Avenging Blade, Shield of the Phoenix, Titan''s Bane, The
    Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Pendulum Blade,
    Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone of Binding,
    Hide of the Nemean Lion, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.26
      fit: 0.58
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.12
      fit: 0.52
    Shield Splitter:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.12
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
