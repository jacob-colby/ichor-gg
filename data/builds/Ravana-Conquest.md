---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.46
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.83
    win_rate: 0.56
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.47
    - name: Transcendence
      pick_rate: 0.01
      win_rate: 0.73
  - name: Sanguine Lash
    pick_rate: 0.56
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.55
    - name: Jotunn's Revenge
      pick_rate: 0.04
      win_rate: 0.48
  - name: Umbral Link
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.19
      win_rate: 0.52
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.64
  - name: Freya's Tears
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.54
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.43
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.54
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.56
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.62
  - name: Veve Charm
    pick_rate: 0.05
    win_rate: 0.52
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.54
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.62
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.35
    win_rate: 0.6
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.62
  - name: Leather Cowl
    pick_rate: 0.2
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-10-15'
  god_win_rate: 0.5406392694063927
  god_matches_won: 592
  god_matches_played: 1095
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-15'
  god_matches_analyzed: 9899
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
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
    this god: Jotunn''s Revenge, Shifter''s Shield, Amanita Charm, Runeforged Hammer,
    Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s
    Lament, Heartseeker, Berserker''s Shield, Avenging Blade, Shield of the Phoenix,
    Titan''s Bane, The Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale,
    Daybreak Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden Blade, Screeching
    Gargoyle, Stone of Binding, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.09
      fit: 0.58
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.15
      fit: 0.52
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.73
      pick: 0.01
      fit: 0.27
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Shifter's Shield
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Transcendence,
    Jotunn''s Revenge, Shifter''s Shield, Amanita Charm, Genji''s Guard, Breastplate
    of Valor, Hydra''s Lament, Runeforged Hammer, Heartseeker, Shield Splitter, Eye
    of the Storm, Berserker''s Shield, Avenging Blade, Titan''s Bane, The Crusher,
    Shield of the Phoenix, Daybreak Gavel, The Reaper, Arondight, Screeching Gargoyle,
    Erosion, Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Draconic Scale,
    Pendulum Blade, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.47
      pick: 0.09
      fit: 0.52
    Transcendence:
      total: 0.56
      efficiency: 0.53
      win: 0.73
      pick: 0.01
      fit: 0.28
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.27
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Shifter''s Shield, Amanita Charm, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Heartseeker, Hydra''s Lament, Berserker''s Shield,
    Shield of the Phoenix, Titan''s Bane, Shield Splitter, The Crusher, Eye of the
    Storm, The Reaper, Pendulum Blade, Avenging Blade, Screeching Gargoyle, Daybreak
    Gavel, Arondight, Erosion, Eye of Providence, Draconic Scale, Avatar''s Parashu,
    Stone of Binding, Midgardian Mail, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.09
      fit: 0.56
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.73
      pick: 0.01
      fit: 0.16
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.33
      fit: 0.32
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.29
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Transcendence
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shifter''s Shield, Shield of the Phoenix, Jotunn''s Revenge,
    Runeforged Hammer, The Reaper, Shield Splitter, Genji''s Guard, Breastplate of
    Valor, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye of
    Providence, Hydra''s Lament, Draconic Scale, Phoenix Feather, Avenging Blade,
    Heartseeker, Chandra''s Grace, Glorious Pridwen, Stone of Binding, Midgardian
    Mail, Titan''s Bane, Daybreak Gavel, The Crusher, Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.47
      pick: 0.09
      fit: 0.49
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.15
      fit: 0.61
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.76
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.73
      pick: 0.01
      fit: 0.22
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.51
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Amanita Charm
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
    for this god: Jotunn''s Revenge, Shifter''s Shield, Avenging Blade, Heartseeker,
    Amanita Charm, Screeching Gargoyle, Titan''s Bane, Runeforged Hammer, Stone of
    Binding, The Crusher, Void Shield, The Reaper, Genji''s Guard, Breastplate of
    Valor, Void Stone, Hydra''s Lament, Shield Splitter, Pendulum Blade, Eye of the
    Storm, Berserker''s Shield, Avatar''s Parashu, Shield of the Phoenix, Daybreak
    Gavel, Tekko-Kagi, Erosion, Eye of Providence, Draconic Scale, Arondight.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.47
      pick: 0.09
      fit: 0.67
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.73
      pick: 0.01
      fit: 0.21
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.33
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.55
      pick: 0.0
      fit: 0.77
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Transcendence
  - Shifter's Shield
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Shifter''s Shield, Golden Blade, Amanita Charm,
    Jotunn''s Revenge, Riptalon, Tyrfing, Silverbranch Bow, Genji''s Guard, Breastplate
    of Valor, Toxic Blade, Runeforged Hammer, Lernaean Bow, Pharaoh''s Curse, Tekko-Kagi,
    The Reaper, Shogun''s Ofuda, Hydra''s Lament, Shield Splitter, Heartseeker, Eye
    of the Storm, Shield of the Phoenix, Daybreak Gavel, Avenging Blade, Dominance,
    Erosion, Eye of Providence, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.4
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.73
      pick: 0.01
      fit: 0.12
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.26
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Transcendence
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Shifter''s Shield, Amanita Charm, Hydra''s Lament, Shield
    of the Phoenix, Screeching Gargoyle, Runeforged Hammer, Berserker''s Shield, Arondight,
    Gladiator''s Shield, Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic
    Cloak, Chandra''s Grace, Heartseeker, Eye of the Storm, Daybreak Gavel, Erosion,
    Eye of Providence, Avenging Blade, Draconic Scale, Midgardian Mail, Stone of Binding,
    Titan''s Bane, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.09
      fit: 0.59
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.73
      pick: 0.01
      fit: 0.1
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.33
      fit: 0.52
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.31
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer,
    Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s
    Lament, Heartseeker, Shifter''s Shield, Berserker''s Shield, Avenging Blade, Shield
    of the Phoenix, Titan''s Bane, The Crusher, Erosion, The Reaper, Eye of Providence,
    Draconic Scale, Daybreak Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden
    Blade, Screeching Gargoyle, Stone of Binding, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.09
      fit: 0.58
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.15
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
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.33
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
