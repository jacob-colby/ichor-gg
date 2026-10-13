---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.71
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.81
    win_rate: 0.56
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.47
    - name: Transcendence
      pick_rate: 0.02
      win_rate: 0.71
  - name: Sanguine Lash
    pick_rate: 0.53
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.56
    - name: Berserker's Shield
      pick_rate: 0.05
      win_rate: 0.45
  - name: Umbral Link
    pick_rate: 0.14
    win_rate: 0.55
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.21
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.2
    win_rate: 0.51
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.58
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.42
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.54
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.56
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.56
  - name: Veve Charm
    pick_rate: 0.05
    win_rate: 0.54
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.52
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.63
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.35
    win_rate: 0.59
  - name: Bumba's Hammer
    pick_rate: 0.21
    win_rate: 0.63
  - name: Leather Cowl
    pick_rate: 0.2
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-10-13'
  god_win_rate: 0.5428893905191874
  god_matches_won: 481
  god_matches_played: 886
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-13'
  god_matches_analyzed: 7865
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
  - Shifter's Shield
  - Runeforged Hammer
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
    this god: Jotunn''s Revenge, Amanita Charm, Shifter''s Shield, Runeforged Hammer,
    Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s
    Lament, Heartseeker, Avenging Blade, Shield of the Phoenix, Titan''s Bane, The
    Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Daybreak Gavel,
    Pendulum Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle,
    Stone of Binding, Avatar''s Parashu, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.1
      fit: 0.58
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.15
      fit: 0.52
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.71
      pick: 0.02
      fit: 0.27
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.61
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Transcendence,
    Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Shifter''s Shield, Breastplate
    of Valor, Hydra''s Lament, Runeforged Hammer, Heartseeker, Shield Splitter, Eye
    of the Storm, Avenging Blade, Titan''s Bane, The Crusher, Shield of the Phoenix,
    Daybreak Gavel, The Reaper, Arondight, Screeching Gargoyle, Erosion, Eye of Providence,
    Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian
    Mail, Berserker''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.1
      fit: 0.52
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.58
      pick: 0.15
      fit: 0.37
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.02
      fit: 0.28
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.61
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
  - Kinetic Cuirass
  - Transcendence
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
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
    god: Jotunn''s Revenge, Amanita Charm, Shifter''s Shield, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Heartseeker, Hydra''s Lament, Shield of the Phoenix,
    Titan''s Bane, Shield Splitter, The Crusher, Eye of the Storm, The Reaper, Pendulum
    Blade, Avenging Blade, Screeching Gargoyle, Daybreak Gavel, Arondight, Erosion,
    Eye of Providence, Draconic Scale, Avatar''s Parashu, Stone of Binding, Midgardian
    Mail, Leviathan''s Hide, Berserker''s Shield.'
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
      pick: 0.1
      fit: 0.56
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.58
      pick: 0.15
      fit: 0.39
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.71
      pick: 0.02
      fit: 0.16
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.61
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
  - Kinetic Cuirass
  - Transcendence
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
  - Jotunn's Revenge
  - Transcendence
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
    Valor, Eye of the Storm, Erosion, Yogi''s Necklace, Eye of Providence, Hydra''s
    Lament, Draconic Scale, Phoenix Feather, Avenging Blade, Heartseeker, Chandra''s
    Grace, Glorious Pridwen, Stone of Binding, Midgardian Mail, Titan''s Bane, Daybreak
    Gavel, The Crusher, Magi''s Cloak, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.47
      pick: 0.1
      fit: 0.49
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.58
      pick: 0.15
      fit: 0.61
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.76
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.71
      pick: 0.02
      fit: 0.22
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
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
  - Kinetic Cuirass
  - Transcendence
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Heartseeker, Amanita Charm, Shifter''s
    Shield, Screeching Gargoyle, Titan''s Bane, Runeforged Hammer, Stone of Binding,
    The Crusher, Void Shield, The Reaper, Genji''s Guard, Breastplate of Valor, Void
    Stone, Hydra''s Lament, Shield Splitter, Pendulum Blade, Eye of the Storm, Avatar''s
    Parashu, Shield of the Phoenix, Daybreak Gavel, Tekko-Kagi, Erosion, Eye of Providence,
    Draconic Scale, Arondight, Berserker''s Shield.'
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
      pick: 0.1
      fit: 0.67
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.15
      fit: 0.43
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.71
      pick: 0.02
      fit: 0.21
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
  - Kinetic Cuirass
  - Transcendence
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Riptalon
  - Berserker's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Amanita Charm, Shifter''s Shield, Jotunn''s Revenge, Riptalon,
    Berserker''s Shield, Tyrfing, Silverbranch Bow, Genji''s Guard, Breastplate of
    Valor, Toxic Blade, Runeforged Hammer, Lernaean Bow, Pharaoh''s Curse, Tekko-Kagi,
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
      total: 0.5
      efficiency: 0.68
      win: 0.45
      pick: 0.07
      fit: 0.4
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.58
      pick: 0.15
      fit: 0.36
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.61
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Freya's Tears
  flex_slots:
  - Kinetic Cuirass
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Shifter''s Shield, Hydra''s Lament, Shield
    of the Phoenix, Screeching Gargoyle, Runeforged Hammer, Arondight, Gladiator''s
    Shield, Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic Cloak, Chandra''s
    Grace, Heartseeker, Eye of the Storm, Daybreak Gavel, Erosion, Eye of Providence,
    Avenging Blade, Draconic Scale, Midgardian Mail, Stone of Binding, Titan''s Bane,
    The Crusher, Berserker''s Shield.'
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
      pick: 0.1
      fit: 0.59
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.15
      fit: 0.41
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.71
      pick: 0.02
      fit: 0.1
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.51
      pick: 0.33
      fit: 0.52
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
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
      pick: 0.1
      fit: 0.58
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
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
      total: 0.51
      efficiency: 0.61
      win: 0.51
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
