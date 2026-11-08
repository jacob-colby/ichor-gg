---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.76
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.25
    win_rate: 0.39
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.18
      win_rate: 0.75
    - name: Avenging Blade
      pick_rate: 0.15
      win_rate: 0.53
  - name: Gladiator's Shield
    pick_rate: 0.11
    win_rate: 0.53
    alternates:
    - name: Avenging Blade
      pick_rate: 0.1
      win_rate: 0.77
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.14
    win_rate: 0.33
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.67
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.41
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.56
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.38
    - name: Sundering Echo
      pick_rate: 0.08
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.56
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.63
  - name: Veve Charm
    pick_rate: 0.07
    win_rate: 0.8
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.07
      win_rate: 0.6
    - name: Brawler’s Beat Stick
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.18
    win_rate: 0.63
  - name: Sundering Axe
    pick_rate: 0.15
    win_rate: 0.47
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-11-08'
  god_win_rate: 0.5114503816793893
  god_matches_won: 67
  god_matches_played: 131
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Shield Splitter
  - Hydra's Lament
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, The Reaper, Shield Splitter, Berserker''s
    Shield, Genji''s Guard, Runeforged Hammer, The Crusher, Heartseeker, Avenging
    Blade, Oni Hunter''s Garb, Shield of the Phoenix, Titan''s Bane, Draconic Scale,
    Breastplate of Valor, Tyrfing, Erosion, Eye of Providence, Midgardian Mail, Wyrmskin
    Hide, Leviathan''s Hide, Golden Blade, Arondight, Sanguine Lash, Ancile, Hide
    of the Nemean Lion.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.48
    Shield Splitter:
      total: 0.51
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.48
    Hydra's Lament:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.18
      fit: 0.4
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.22
      fit: 0.27
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Brawler’s Beat Stick
  - Hydra's Lament
  - Freya's Tears
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Genji''s Guard, Amanita Charm, The Reaper, Berserker''s Shield, Breastplate
    of Valor, Shield Splitter, Runeforged Hammer, Heartseeker, Oni Hunter''s Garb,
    Shield of the Phoenix, The Crusher, Avenging Blade, Titan''s Bane, Arondight,
    Tyrfing, Screeching Gargoyle, Draconic Scale, Yogi''s Necklace, Midgardian Mail,
    Leviathan''s Hide, Erosion, Eye of Providence, Transcendence, Chandra''s Grace,
    Hide of the Nemean Lion.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.14
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.45
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.26
    Hydra's Lament:
      total: 0.61
      efficiency: 0.55
      win: 0.75
      pick: 0.18
      fit: 0.46
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.25
  community_ordered:
  - Brawler’s Beat Stick
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
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
    Berserker''s Shield, Shield Splitter, Genji''s Guard, Phoenix Feather, Yogi''s
    Necklace, Runeforged Hammer, Draconic Scale, Oni Hunter''s Garb, Erosion, Bloodforge,
    Eye of Providence, Breastplate of Valor, Chandra''s Grace, Avenging Blade, The
    Crusher, Midgardian Mail, Heartseeker, Leviathan''s Hide, Wyrmskin Hide, Titan''s
    Bane, Regrowth Striders, Hide of the Nemean Lion.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.31
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.4
    Hydra's Lament:
      total: 0.59
      efficiency: 0.55
      win: 0.75
      pick: 0.18
      fit: 0.35
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.22
      fit: 0.34
    The Reaper:
      total: 0.55
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.77
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Brawler’s Beat Stick
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  flex_slots:
  - Avenging Blade
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, Amanita Charm, Avenging Blade, The
    Crusher, Heartseeker, Genji''s Guard, Titan''s Bane, Berserker''s Shield, Screeching
    Gargoyle, Stone of Binding, Shield Splitter, Void Stone, Runeforged Hammer, Void
    Shield, Avatar''s Parashu, Oni Hunter''s Garb, Breastplate of Valor, Shield of
    the Phoenix, Draconic Scale, Tekko-Kagi, Tyrfing, Midgardian Mail, Erosion, Pendulum
    Blade, Eye of Providence, Leviathan''s Hide.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.18
    Avenging Blade:
      total: 0.52
      efficiency: 0.47
      win: 0.53
      pick: 0.15
      fit: 0.74
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.59
      efficiency: 0.55
      win: 0.75
      pick: 0.18
      fit: 0.33
    The Reaper:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.51
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Brawler’s Beat Stick
  - Avenging Blade
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Tyrfing
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Tyrfing, Golden Blade, Jotunn''s
    Revenge, Genji''s Guard, Toxic Blade, The Reaper, Silverbranch Bow, Shield Splitter,
    Runeforged Hammer, Riptalon, Tekko-Kagi, Breastplate of Valor, Oni Hunter''s Garb,
    Shogun''s Ofuda, Pharaoh''s Curse, Lernaean Bow, Dominance, Shield of the Phoenix,
    The Crusher, Draconic Scale, Heartseeker, Qin''s Blade, Midgardian Mail, Erosion,
    Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.62
    Brawler’s Beat Stick:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.15
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.6
    Hydra's Lament:
      total: 0.58
      efficiency: 0.55
      win: 0.75
      pick: 0.18
      fit: 0.25
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Brawler’s Beat Stick
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Freya's Tears
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Berserker''s Shield,
    Screeching Gargoyle, Arondight, The Reaper, Shield Splitter, Runeforged Hammer,
    Oni Hunter''s Garb, Chandra''s Grace, Eye of Erebus, Draconic Scale, Prophetic
    Cloak, The Crusher, Damaru, Midgardian Mail, Erosion, Regrowth Striders, Heartseeker,
    Leviathan''s Hide, Eye of Providence, Pendulum Blade, Hide of the Nemean Lion.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.16
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.4
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.54
    Hydra's Lament:
      total: 0.62
      efficiency: 0.55
      win: 0.75
      pick: 0.18
      fit: 0.51
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.22
      fit: 0.47
  community_ordered:
  - Brawler’s Beat Stick
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
    Scale, Avenging Blade, Breastplate of Valor, Tyrfing, Erosion, Eye of Providence,
    Midgardian Mail, Wyrmskin Hide, Leviathan''s Hide, Golden Blade, Hide of the Nemean
    Lion, Arondight, Sanguine Lash, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.51
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.61
      win: 0.33
      pick: 0.22
      fit: 0.51
    Shield Splitter:
      total: 0.51
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-10-20'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of Prowess
    status: shown
    window: ob46
    window_rule: last closed
    window_start: '2026-10-20'
    window_end: '2026-11-03'
    matches: 48
    wins: 31
    win_share: 0.65
    aggregate:
      aspect_matches: 61
      aspect_win_rate: 0.574
      no_aspect_matches: 401
      no_aspect_win_rate: 0.509
    roles:
    - role: Jungle
      matches: 45
      share: 0.94
    - role: Solo
      matches: 3
      share: 0.06
    base_role: Solo Jungle
    base_role_share: 1.0
    role_shift: null
    items:
    - name: Hydra's Lament
      share: 0.75
    - name: Jotunn's Revenge
      share: 0.6
    - name: Heartseeker
      share: 0.56
    - name: The Reaper
      share: 0.31
    - name: Shifter's Shield
      share: 0.29
    - name: Blinking Abyss
      share: 0.25
    - name: brawlers-ruin
      share: 0.25
    - name: Avenging Blade
      share: 0.23
    starters:
    - name: Bumba's Hammer
      share: 0.46
    - name: Hunter's Cowl
      share: 0.31
    - name: Bumba's Cudgel
      share: 0.08
    relics:
    - name: purification-beads
      share: 0.42
    - name: Blink Rune
      share: 0.4
    - name: aegis-of-acceleration
      share: 0.12
    matches_by_window:
      ob47: 26
      ob46: 48
    unmapped_slugs:
    - aegis-of-acceleration
    - brawlers-ruin
    - phantom-shell
    - purification-beads
    - sundering-arc
---
