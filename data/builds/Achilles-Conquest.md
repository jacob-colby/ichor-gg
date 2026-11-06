---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.24
  aspect_win_rate: 0.89
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.23
    win_rate: 0.35
    alternates:
    - name: Avenging Blade
      pick_rate: 0.2
      win_rate: 0.53
    - name: Hydra's Lament
      pick_rate: 0.2
      win_rate: 0.93
  - name: Gladiator's Shield
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.63
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.43
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.44
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.69
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 0.38
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.44
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.78
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.67
    - name: Contagion
      pick_rate: 0.06
      win_rate: 0.25
  - name: Veve Charm
    pick_rate: 0.1
    win_rate: 0.75
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.1
      win_rate: 1.0
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.33
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.22
    win_rate: 0.69
  - name: Bumba's Cudgel
    pick_rate: 0.14
    win_rate: 0.6
  - name: Hunter's Cowl
    pick_rate: 0.14
    win_rate: 0.7
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-11-06'
  god_win_rate: 0.527027027027027
  god_matches_won: 39
  god_matches_played: 74
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Avenging Blade
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, The Reaper, Berserker''s Shield, Shield
    Splitter, Runeforged Hammer, Genji''s Guard, The Crusher, Heartseeker, Oni Hunter''s
    Garb, Shield of the Phoenix, Titan''s Bane, Draconic Scale, Breastplate of Valor,
    Tyrfing, Erosion, Eye of Providence, Midgardian Mail, Wyrmskin Hide, Leviathan''s
    Hide, Golden Blade, Hide of the Nemean Lion, Arondight, Sanguine Lash, Ancile.'
  slot_scores:
    Avenging Blade:
      total: 0.49
      efficiency: 0.47
      win: 0.53
      pick: 0.2
      fit: 0.54
    Brawler’s Beat Stick:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.23
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.51
    Hydra's Lament:
      total: 0.68
      efficiency: 0.55
      win: 0.93
      pick: 0.2
      fit: 0.4
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Avenging Blade
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Hydra's Lament
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Avenging Blade
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Hydra's Lament
  flex_slots:
  - Avenging Blade
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Amanita Charm, Genji''s Guard, Berserker''s Shield, The Reaper, Breastplate
    of Valor, Shield Splitter, Runeforged Hammer, Heartseeker, Oni Hunter''s Garb,
    Shield of the Phoenix, The Crusher, Titan''s Bane, Arondight, Tyrfing, Screeching
    Gargoyle, Draconic Scale, Yogi''s Necklace, Midgardian Mail, Leviathan''s Hide,
    Erosion, Eye of Providence, Hide of the Nemean Lion, Transcendence, Chandra''s
    Grace.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.47
      win: 0.53
      pick: 0.2
      fit: 0.4
    Brawler’s Beat Stick:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.14
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.35
    Transcendence:
      total: 0.41
      efficiency: 0.5
      win: 0.44
      pick: 0.0
      fit: 0.26
    Hydra's Lament:
      total: 0.69
      efficiency: 0.55
      win: 0.93
      pick: 0.2
      fit: 0.46
  community_ordered:
  - Avenging Blade
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Brawler’s Beat Stick
  - Hydra's Lament
  - Kinetic Cuirass
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Shield of the Phoenix, Jotunn''s Revenge,
    Berserker''s Shield, Shield Splitter, Phoenix Feather, Yogi''s Necklace, Runeforged
    Hammer, Genji''s Guard, Draconic Scale, Oni Hunter''s Garb, Erosion, Bloodforge,
    Eye of Providence, Breastplate of Valor, Chandra''s Grace, The Crusher, Midgardian
    Mail, Heartseeker, Leviathan''s Hide, Hide of the Nemean Lion, Wyrmskin Hide,
    Titan''s Bane, Regrowth Striders.'
  slot_scores:
    Avenging Blade:
      total: 0.49
      efficiency: 0.47
      win: 0.53
      pick: 0.2
      fit: 0.51
    Brawler’s Beat Stick:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.31
    Hydra's Lament:
      total: 0.67
      efficiency: 0.55
      win: 0.93
      pick: 0.2
      fit: 0.35
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.6
    The Reaper:
      total: 0.51
      efficiency: 0.57
      win: 0.44
      pick: 0.0
      fit: 0.77
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Avenging Blade
  - Brawler’s Beat Stick
  - Hydra's Lament
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - The Reaper
  flex_slots:
  - The Reaper
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, Amanita Charm, The Crusher, Heartseeker,
    Berserker''s Shield, Titan''s Bane, Screeching Gargoyle, Stone of Binding, Shield
    Splitter, Void Stone, Runeforged Hammer, Void Shield, Genji''s Guard, Avatar''s
    Parashu, Oni Hunter''s Garb, Breastplate of Valor, Shield of the Phoenix, Draconic
    Scale, Tekko-Kagi, Tyrfing, Midgardian Mail, Erosion, Pendulum Blade, Eye of Providence,
    Leviathan''s Hide.'
  slot_scores:
    Avenging Blade:
      total: 0.52
      efficiency: 0.47
      win: 0.53
      pick: 0.2
      fit: 0.74
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.18
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.59
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.42
    Hydra's Lament:
      total: 0.67
      efficiency: 0.55
      win: 0.93
      pick: 0.2
      fit: 0.33
    The Reaper:
      total: 0.49
      efficiency: 0.57
      win: 0.44
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Avenging Blade
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Tyrfing
  - Hydra's Lament
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Berserker''s Shield, Amanita Charm, Tyrfing, Golden Blade, Jotunn''s
    Revenge, Toxic Blade, Genji''s Guard, The Reaper, Silverbranch Bow, Shield Splitter,
    Runeforged Hammer, Riptalon, Tekko-Kagi, Breastplate of Valor, Oni Hunter''s Garb,
    Shogun''s Ofuda, Pharaoh''s Curse, Lernaean Bow, Dominance, Shield of the Phoenix,
    The Crusher, Draconic Scale, Heartseeker, Qin''s Blade, Midgardian Mail, Erosion,
    Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.51
      win: 0.44
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.52
      efficiency: 0.72
      win: 0.43
      pick: 0.12
      fit: 0.43
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.15
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.37
    Tyrfing:
      total: 0.48
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.6
    Hydra's Lament:
      total: 0.66
      efficiency: 0.55
      win: 0.93
      pick: 0.2
      fit: 0.25
  community_ordered:
  - Berserker's Shield
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Berserker''s Shield,
    Screeching Gargoyle, Arondight, The Reaper, Shield Splitter, Runeforged Hammer,
    Oni Hunter''s Garb, Chandra''s Grace, Eye of Erebus, Draconic Scale, Prophetic
    Cloak, The Crusher, Damaru, Midgardian Mail, Erosion, Regrowth Striders, Heartseeker,
    Leviathan''s Hide, Eye of Providence, Hide of the Nemean Lion, Pendulum Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.4
      pick: 0.12
      fit: 0.4
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.16
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.38
    Hydra's Lament:
      total: 0.7
      efficiency: 0.55
      win: 0.93
      pick: 0.2
      fit: 0.51
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.44
      pick: 0.19
      fit: 0.47
  community_ordered:
  - Genji's Guard
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, The Reaper, Shield
    Splitter, Berserker''s Shield, Genji''s Guard, Runeforged Hammer, The Crusher,
    Heartseeker, Oni Hunter''s Garb, Shield of the Phoenix, Titan''s Bane, Draconic
    Scale, Breastplate of Valor, Tyrfing, Erosion, Eye of Providence, Midgardian Mail,
    Wyrmskin Hide, Leviathan''s Hide, Golden Blade, Hide of the Nemean Lion, Arondight,
    Sanguine Lash, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.46
      efficiency: 0.71
      win: 0.4
      pick: 0.12
      fit: 0.15
    Berserker's Shield:
      total: 0.47
      efficiency: 0.66
      win: 0.43
      pick: 0.12
      fit: 0.29
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.51
    Shield Splitter:
      total: 0.47
      efficiency: 0.58
      win: 0.44
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
