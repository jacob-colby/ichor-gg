---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.33
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.31
    win_rate: 0.48
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.16
      win_rate: 0.45
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.86
  - name: Shifter's Shield
    pick_rate: 0.27
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.5
    - name: Barbed Carver
      pick_rate: 0.09
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.67
    - name: Daybreak Gavel
      pick_rate: 0.06
      win_rate: 0.75
  - name: Heartseeker
    pick_rate: 0.13
    win_rate: 0.25
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.2
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.75
  - name: Sundering Echo
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 1.0
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.33
  - name: Lucerne Hammer
    pick_rate: 0.13
    win_rate: 0.4
    alternates:
    - name: Engraved Guard
      pick_rate: 0.1
      win_rate: 0.75
    - name: Olmec Blue
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.81
  - name: Bumba's Cudgel
    pick_rate: 0.22
    win_rate: 0.2
  - name: Bluestone Pendant
    pick_rate: 0.12
    win_rate: 0.13
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-09-23'
  god_win_rate: 0.47761194029850745
  god_matches_won: 32
  god_matches_played: 67
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, The Crusher, Amanita Charm, Runeforged Hammer, Freya''s
    Tears, Shield Splitter, Eye of the Storm, Breastplate of Valor, Hydra''s Lament,
    Berserker''s Shield, Avenging Blade, Shield of the Phoenix, Titan''s Bane, Erosion,
    The Reaper, Eye of Providence, Draconic Scale, Pendulum Blade, Arondight, Midgardian
    Mail, Golden Blade, Screeching Gargoyle, Stone of Binding, Hide of the Nemean
    Lion, Avatar''s Parashu.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.1
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.48
      pick: 0.31
      fit: 0.58
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.19
      fit: 0.52
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.14
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
  - The Crusher
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
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, The Crusher, Amanita Charm, Breastplate of Valor, Hydra''s Lament, Runeforged
    Hammer, Freya''s Tears, Shield Splitter, Eye of the Storm, Berserker''s Shield,
    Avenging Blade, Titan''s Bane, Shield of the Phoenix, Transcendence, The Reaper,
    Arondight, Screeching Gargoyle, Erosion, Eye of Providence, Oni Hunter''s Garb,
    Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian Mail, Hide of the
    Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.1
      fit: 0.25
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.48
      pick: 0.31
      fit: 0.52
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.28
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.14
      fit: 0.44
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Genji''s Guard, The Crusher, Amanita Charm, Breastplate of Valor, Freya''s
    Tears, Runeforged Hammer, Hydra''s Lament, Berserker''s Shield, Shield of the
    Phoenix, Titan''s Bane, Shield Splitter, Eye of the Storm, The Reaper, Pendulum
    Blade, Avenging Blade, Screeching Gargoyle, Arondight, Erosion, Eye of Providence,
    Draconic Scale, Avatar''s Parashu, Stone of Binding, Midgardian Mail, Hide of
    the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.1
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.48
      pick: 0.31
      fit: 0.56
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.19
      fit: 0.39
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.16
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.14
      fit: 0.5
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
  - The Crusher
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, The Crusher, Shield of the Phoenix, Freya''s
    Tears, Runeforged Hammer, The Reaper, Shield Splitter, Breastplate of Valor, Eye
    of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye of Providence,
    Hydra''s Lament, Draconic Scale, Phoenix Feather, Avenging Blade, Chandra''s Grace,
    Glorious Pridwen, Stone of Binding, Midgardian Mail, Titan''s Bane, Hide of the
    Nemean Lion, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.1
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.31
      fit: 0.49
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.19
      fit: 0.61
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.14
      fit: 0.48
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Genji''s Guard, The Crusher, Avenging Blade, Amanita Charm, Screeching
    Gargoyle, Titan''s Bane, Runeforged Hammer, Stone of Binding, Void Shield, The
    Reaper, Freya''s Tears, Breastplate of Valor, Void Stone, Hydra''s Lament, Shield
    Splitter, Pendulum Blade, Eye of the Storm, Berserker''s Shield, Avatar''s Parashu,
    Shield of the Phoenix, Tekko-Kagi, Erosion, Eye of Providence, Draconic Scale,
    Arondight.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.75
      pick: 0.1
      fit: 0.19
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.48
      pick: 0.31
      fit: 0.67
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.19
      fit: 0.43
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.14
      fit: 0.67
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Berserker's Shield
  - Riptalon
  - The Crusher
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
    this god: Genji''s Guard, Berserker''s Shield, Golden Blade, Amanita Charm, Riptalon,
    Tyrfing, Silverbranch Bow, Breastplate of Valor, Toxic Blade, Freya''s Tears,
    Runeforged Hammer, Lernaean Bow, Pharaoh''s Curse, Tekko-Kagi, The Reaper, Shogun''s
    Ofuda, Hydra''s Lament, Shield Splitter, Eye of the Storm, Shield of the Phoenix,
    Avenging Blade, Dominance, Erosion, Eye of Providence, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.75
      pick: 0.1
      fit: 0.15
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.48
      pick: 0.31
      fit: 0.31
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.52
      efficiency: 0.47
      win: 0.67
      pick: 0.14
      fit: 0.33
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, The Crusher, Breastplate
    of Valor, Freya''s Tears, Amanita Charm, Hydra''s Lament, Shield of the Phoenix,
    Screeching Gargoyle, Runeforged Hammer, Berserker''s Shield, Arondight, Gladiator''s
    Shield, Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic Cloak, Chandra''s
    Grace, Eye of the Storm, Erosion, Eye of Providence, Avenging Blade, Draconic
    Scale, Midgardian Mail, Stone of Binding, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.75
      pick: 0.1
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.48
      pick: 0.31
      fit: 0.59
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    The Crusher:
      total: 0.52
      efficiency: 0.47
      win: 0.67
      pick: 0.14
      fit: 0.34
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - The Crusher
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
    Underrated for this god: Amanita Charm, Runeforged Hammer, Freya''s Tears, Shield
    Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament,
    Berserker''s Shield, Avenging Blade, Shield of the Phoenix, Titan''s Bane, The
    Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Pendulum Blade,
    Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone of Binding,
    Hide of the Nemean Lion, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.48
      pick: 0.31
      fit: 0.58
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.19
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
      total: 0.49
      efficiency: 0.61
      win: 0.5
      pick: 0.0
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
  starter: *id001
---
