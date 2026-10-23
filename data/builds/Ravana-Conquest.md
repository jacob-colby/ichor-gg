---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.05
  aspect_win_rate: 1.0
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.67
    win_rate: 0.53
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.19
      win_rate: 0.42
    - name: Tyrfing
      pick_rate: 0.02
      win_rate: 0.6
  - name: Sanguine Lash
    pick_rate: 0.43
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.5
    - name: Barbed Carver
      pick_rate: 0.05
      win_rate: 0.2
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.76
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.11
      win_rate: 0.52
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.54
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.6
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.14
      win_rate: 0.48
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.36
  - name: Heartseeker
    pick_rate: 0.07
    win_rate: 0.64
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.06
      win_rate: 0.78
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.67
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.43
    - name: Mote of Chaos
      pick_rate: 0.04
      win_rate: 0.2
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.27
    win_rate: 0.56
  - name: Leather Cowl
    pick_rate: 0.24
    win_rate: 0.51
  - name: Bumba's Hammer
    pick_rate: 0.16
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-10-23'
  god_win_rate: 0.5
  god_matches_won: 101
  god_matches_played: 202
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-23'
  god_matches_analyzed: 2743
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Runeforged Hammer, Shield Splitter,
    Eye of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament, Avenging
    Blade, Shield of the Phoenix, Titan''s Bane, The Crusher, The Reaper, Erosion,
    Shifter''s Shield, Eye of Providence, Draconic Scale, Daybreak Gavel, Pendulum
    Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone of
    Binding, Avatar''s Parashu.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.6
      win: 0.78
      pick: 0.13
      fit: 0.31
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.42
      pick: 0.19
      fit: 0.58
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.76
      pick: 0.2
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.35
      fit: 0.36
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.64
      pick: 0.15
      fit: 0.65
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Berserker''s
    Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Avenging Blade, Titan''s
    Bane, The Crusher, Shield of the Phoenix, The Reaper, Transcendence, Daybreak
    Gavel, Arondight, Screeching Gargoyle, Erosion, Shifter''s Shield, Eye of Providence,
    Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian
    Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.25
    Berserker's Shield:
      total: 0.6
      efficiency: 0.6
      win: 0.78
      pick: 0.13
      fit: 0.19
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.42
      pick: 0.19
      fit: 0.52
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.76
      pick: 0.2
      fit: 0.37
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.35
      fit: 0.25
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.64
      pick: 0.15
      fit: 0.62
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Berserker''s Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Hydra''s Lament, Shield of the Phoenix, Titan''s Bane, Shield
    Splitter, The Crusher, The Reaper, Eye of the Storm, Pendulum Blade, Avenging
    Blade, Screeching Gargoyle, Daybreak Gavel, Arondight, Erosion, Shifter''s Shield,
    Eye of Providence, Draconic Scale, Avatar''s Parashu, Stone of Binding, Midgardian
    Mail, Leviathan''s Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.6
      win: 0.78
      pick: 0.13
      fit: 0.21
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.42
      pick: 0.19
      fit: 0.56
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.76
      pick: 0.2
      fit: 0.39
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.35
      fit: 0.32
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.64
      pick: 0.15
      fit: 0.6
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Shield of the Phoenix
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Shield of the Phoenix, The Reaper,
    Runeforged Hammer, Shield Splitter, Genji''s Guard, Breastplate of Valor, Eye
    of the Storm, Erosion, Yogi''s Necklace, Shifter''s Shield, Eye of Providence,
    Hydra''s Lament, Draconic Scale, Phoenix Feather, Avenging Blade, Chandra''s Grace,
    Glorious Pridwen, Stone of Binding, Midgardian Mail, Titan''s Bane, Daybreak Gavel,
    The Crusher, Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.62
      efficiency: 0.6
      win: 0.78
      pick: 0.13
      fit: 0.36
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.56
      win: 0.76
      pick: 0.2
      fit: 0.61
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.35
      fit: 0.42
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.64
      pick: 0.15
      fit: 0.58
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  flex_slots:
  - Freya's Tears
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Berserker''s Shield, Avenging Blade, Amanita Charm, Screeching Gargoyle,
    Titan''s Bane, Runeforged Hammer, Stone of Binding, The Crusher, The Reaper, Void
    Shield, Genji''s Guard, Breastplate of Valor, Void Stone, Hydra''s Lament, Shield
    Splitter, Pendulum Blade, Eye of the Storm, Avatar''s Parashu, Shield of the Phoenix,
    Daybreak Gavel, Tekko-Kagi, Erosion, Shifter''s Shield, Eye of Providence, Draconic
    Scale, Arondight.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.75
    Berserker's Shield:
      total: 0.6
      efficiency: 0.6
      win: 0.78
      pick: 0.13
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.42
      pick: 0.19
      fit: 0.67
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.76
      pick: 0.2
      fit: 0.43
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.35
      fit: 0.28
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.64
      pick: 0.15
      fit: 0.77
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Freya's Tears
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Golden Blade
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
    this god: Berserker''s Shield, Tyrfing, Golden Blade, Amanita Charm, Riptalon,
    Silverbranch Bow, Genji''s Guard, Breastplate of Valor, Toxic Blade, Runeforged
    Hammer, Lernaean Bow, The Reaper, Pharaoh''s Curse, Tekko-Kagi, Shogun''s Ofuda,
    Hydra''s Lament, Shield Splitter, Eye of the Storm, Shield of the Phoenix, Daybreak
    Gavel, Avenging Blade, Dominance, Erosion, Shifter''s Shield, Eye of Providence,
    Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.66
      efficiency: 0.68
      win: 0.78
      pick: 0.13
      fit: 0.4
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.76
      pick: 0.2
      fit: 0.36
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.6
      pick: 0.02
      fit: 0.58
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.35
      fit: 0.22
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.64
      pick: 0.15
      fit: 0.43
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
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
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Screeching
    Gargoyle, Runeforged Hammer, Arondight, Gladiator''s Shield, Eye of Erebus, Pendulum
    Blade, Shield Splitter, Prophetic Cloak, Chandra''s Grace, Eye of the Storm, Daybreak
    Gavel, Erosion, Shifter''s Shield, Eye of Providence, Avenging Blade, Draconic
    Scale, Midgardian Mail, Stone of Binding, Titan''s Bane, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.43
    Berserker's Shield:
      total: 0.6
      efficiency: 0.6
      win: 0.78
      pick: 0.13
      fit: 0.22
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.42
      pick: 0.19
      fit: 0.59
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.76
      pick: 0.2
      fit: 0.41
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.35
      fit: 0.52
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    Underrated for this god: Amanita Charm, Runeforged Hammer, Shield Splitter, Eye
    of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament, Shifter''s
    Shield, Berserker''s Shield, Avenging Blade, Shield of the Phoenix, Titan''s Bane,
    The Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Daybreak
    Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle,
    Stone of Binding, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.42
      pick: 0.19
      fit: 0.58
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.76
      pick: 0.2
      fit: 0.52
    Shield Splitter:
      total: 0.51
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.35
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
