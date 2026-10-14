---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.82
    win_rate: 0.56
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.48
    - name: Transcendence
      pick_rate: 0.01
      win_rate: 0.71
  - name: Sanguine Lash
    pick_rate: 0.55
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.56
    - name: Berserker's Shield
      pick_rate: 0.05
      win_rate: 0.43
  - name: Umbral Link
    pick_rate: 0.14
    win_rate: 0.55
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.2
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.63
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.52
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.56
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.41
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.57
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.59
  - name: Veve Charm
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.53
    - name: Sage's Ring
      pick_rate: 0.04
      win_rate: 0.63
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.35
    win_rate: 0.59
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.62
  - name: Leather Cowl
    pick_rate: 0.2
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-10-14'
  god_win_rate: 0.5405960945529291
  god_matches_won: 526
  god_matches_played: 973
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-14'
  god_matches_analyzed: 8861
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
  - Kinetic Cuirass
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
    this god: Jotunn''s Revenge, Shifter''s Shield, Amanita Charm, Runeforged Hammer,
    Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s
    Lament, Heartseeker, Avenging Blade, Shield of the Phoenix, Titan''s Bane, The
    Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Daybreak Gavel,
    Pendulum Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle,
    Stone of Binding, Avatar''s Parashu, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.48
      pick: 0.1
      fit: 0.58
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.15
      fit: 0.52
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.71
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
      win: 0.63
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Transcendence, Shifter''s Shield, Amanita Charm, Genji''s Guard, Breastplate
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
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.1
      fit: 0.52
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.01
      fit: 0.28
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.63
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
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
    god: Jotunn''s Revenge, Shifter''s Shield, Amanita Charm, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Heartseeker, Hydra''s Lament, Shield of the Phoenix,
    Titan''s Bane, Shield Splitter, The Crusher, Eye of the Storm, The Reaper, Pendulum
    Blade, Avenging Blade, Screeching Gargoyle, Daybreak Gavel, Arondight, Erosion,
    Eye of Providence, Draconic Scale, Avatar''s Parashu, Stone of Binding, Midgardian
    Mail, Leviathan''s Hide, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.1
      fit: 0.56
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.56
      pick: 0.15
      fit: 0.39
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.71
      pick: 0.01
      fit: 0.16
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.52
      pick: 0.35
      fit: 0.32
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.63
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
      win: 0.48
      pick: 0.1
      fit: 0.49
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
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
      pick: 0.01
      fit: 0.22
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.63
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Shifter''s Shield, Heartseeker,
    Amanita Charm, Screeching Gargoyle, Titan''s Bane, Runeforged Hammer, Stone of
    Binding, The Crusher, Void Shield, The Reaper, Genji''s Guard, Breastplate of
    Valor, Void Stone, Hydra''s Lament, Shield Splitter, Pendulum Blade, Eye of the
    Storm, Avatar''s Parashu, Shield of the Phoenix, Daybreak Gavel, Tekko-Kagi, Erosion,
    Eye of Providence, Draconic Scale, Arondight, Berserker''s Shield.'
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
      win: 0.48
      pick: 0.1
      fit: 0.67
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.71
      pick: 0.01
      fit: 0.21
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.63
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
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Shifter's Shield
  - Riptalon
  flex_slots:
  - Riptalon
  - Tyrfing
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
    this god: Shifter''s Shield, Golden Blade, Jotunn''s Revenge, Amanita Charm, Riptalon,
    Tyrfing, Silverbranch Bow, Genji''s Guard, Breastplate of Valor, Toxic Blade,
    Berserker''s Shield, Runeforged Hammer, Lernaean Bow, Pharaoh''s Curse, Tekko-Kagi,
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
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.48
      pick: 0.1
      fit: 0.31
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.71
      pick: 0.01
      fit: 0.12
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.55
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.63
      pick: 0.14
      fit: 0.26
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Jotunn's Revenge
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
      total: 0.56
      efficiency: 0.72
      win: 0.48
      pick: 0.1
      fit: 0.59
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.71
      pick: 0.01
      fit: 0.1
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.35
      fit: 0.52
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.63
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
      total: 0.56
      efficiency: 0.72
      win: 0.48
      pick: 0.1
      fit: 0.58
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
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
      win: 0.52
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
