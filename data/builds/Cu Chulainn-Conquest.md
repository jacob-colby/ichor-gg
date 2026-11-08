---
type: smite-build
god: Cu Chulainn
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Warped
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.41
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.51
    win_rate: 0.51
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.16
      win_rate: 0.54
    - name: Mystical Mail
      pick_rate: 0.15
      win_rate: 0.56
  - name: Mystical Mail
    pick_rate: 0.14
    win_rate: 0.49
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.49
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.41
  - name: Freya's Tears
    pick_rate: 0.23
    win_rate: 0.46
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.17
      win_rate: 0.54
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.62
  - name: Kinetic Cuirass
    pick_rate: 0.11
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.18
      win_rate: 0.49
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.44
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.61
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.57
    alternates:
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 0.71
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.46
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.57
    win_rate: 0.56
  - name: Bluestone Pendant
    pick_rate: 0.31
    win_rate: 0.42
  - name: Sundering Axe
    pick_rate: 0.07
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/cu-chulainn/
  last_verified: '2026-11-08'
  god_win_rate: 0.5085910652920962
  god_matches_won: 148
  god_matches_played: 291
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Tyrfing, Shield Splitter, Golden Blade, Runeforged Hammer, The Reaper, Hydra''s
    Lament, Breastplate of Valor, Oni Hunter''s Garb, Lernaean Bow, Dominance, Shield
    of the Phoenix, Tekko-Kagi, Draconic Scale, Shogun''s Ofuda, The Crusher, Pharaoh''s
    Curse, Avenging Blade, Midgardian Mail, Heartseeker, Erosion, Eye of Providence,
    Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.62
      pick: 0.11
      fit: 0.12
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.18
      fit: 0.41
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Berserker''s Shield, Shield of the Phoenix,
    The Reaper, Shield Splitter, Phoenix Feather, Jotunn''s Revenge, Yogi''s Necklace,
    Tyrfing, Runeforged Hammer, Golden Blade, Oni Hunter''s Garb, Draconic Scale,
    Riptalon, Breastplate of Valor, Bloodforge, Chandra''s Grace, Erosion, Eye of
    Providence, Hydra''s Lament, Midgardian Mail, Shogun''s Ofuda, Pharaoh''s Curse,
    Leviathan''s Hide, Regrowth Striders, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.62
      pick: 0.11
      fit: 0.15
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.52
      pick: 0.18
      fit: 0.5
    Shield Splitter:
      total: 0.5
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Jotunn's Revenge
  - The Reaper
  flex_slots:
  - Kinetic Cuirass
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
    for this god: Genji''s Guard, Berserker''s Shield, Jotunn''s Revenge, The Reaper,
    Amanita Charm, Avenging Blade, Screeching Gargoyle, The Crusher, Tekko-Kagi, Stone
    of Binding, Heartseeker, Tyrfing, Void Stone, Titan''s Bane, Shield Splitter,
    Void Shield, Runeforged Hammer, Toxic Blade, Golden Blade, Breastplate of Valor,
    Silverbranch Bow, Hydra''s Lament, Riptalon, Oni Hunter''s Garb, Shield of the
    Phoenix, Lernaean Bow, Avatar''s Parashu, Dominance.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.62
      pick: 0.11
      fit: 0.09
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.52
      pick: 0.18
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.45
    The Reaper:
      total: 0.51
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Genji''s Guard, Amanita Charm, Tyrfing, Golden
    Blade, Jotunn''s Revenge, Shield Splitter, Runeforged Hammer, Toxic Blade, Breastplate
    of Valor, Oni Hunter''s Garb, The Reaper, Lernaean Bow, Dominance, Silverbranch
    Bow, Shogun''s Ofuda, Pharaoh''s Curse, Shield of the Phoenix, Hydra''s Lament,
    Riptalon, Tekko-Kagi, Draconic Scale, Qin''s Blade, Midgardian Mail, Erosion,
    Leviathan''s Hide, The Crusher, Eye of Providence.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.62
      pick: 0.11
      fit: 0.1
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.52
      pick: 0.18
      fit: 0.35
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.25
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Berserker''s Shield,
    Jotunn''s Revenge, Amanita Charm, Breastplate of Valor, Shield of the Phoenix,
    Hydra''s Lament, Screeching Gargoyle, Tyrfing, Arondight, Shield Splitter, Runeforged
    Hammer, Oni Hunter''s Garb, Gladiator''s Shield, Golden Blade, The Reaper, Chandra''s
    Grace, Draconic Scale, Damaru, Midgardian Mail, Eye of Erebus, Prophetic Cloak,
    Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Leviathan''s Hide, Erosion,
    Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.62
      pick: 0.11
      fit: 0.34
    Berserker's Shield:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.29
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.52
      pick: 0.18
      fit: 0.33
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.38
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.23
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Genji''s Guard, Tyrfing, Shield Splitter, Golden Blade, Runeforged Hammer, The
    Reaper, Hydra''s Lament, Breastplate of Valor, Oni Hunter''s Garb, Lernaean Bow,
    Dominance, Shield of the Phoenix, Tekko-Kagi, Draconic Scale, Shogun''s Ofuda,
    The Crusher, Pharaoh''s Curse, Avenging Blade, Midgardian Mail, Heartseeker, Erosion,
    Eye of Providence, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.62
      pick: 0.11
      fit: 0.12
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.18
      fit: 0.41
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-10-20'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of the Warped
    status: shown
    window: ob47
    window_rule: newest
    window_start: '2026-11-03'
    window_end: '2026-11-08'
    matches: 37
    wins: 17
    win_share: 0.46
    aggregate:
      aspect_matches: 49
      aspect_win_rate: 0.449
      no_aspect_matches: 258
      no_aspect_win_rate: 0.531
    roles:
    - role: Solo
      matches: 31
      share: 0.84
    - role: Jungle
      matches: 3
      share: 0.08
    - role: Support
      matches: 3
      share: 0.08
    base_role: Solo
    base_role_share: 0.84
    role_shift: null
    items:
    - name: Devourer's Gauntlet
      share: 0.54
    - name: Berserker's Shield
      share: 0.51
    - name: Kinetic Cuirass
      share: 0.46
    - name: Riptalon
      share: 0.43
    - name: Freya's Tears
      share: 0.32
    - name: Mystical Mail
      share: 0.24
    - name: Shifter's Shield
      share: 0.22
    - name: Contagion
      share: 0.16
    starters:
    - name: Bluestone Brooch
      share: 0.22
    - name: Death's Embrace
      share: 0.22
    - name: Bluestone Pendant
      share: 0.19
    relics:
    - name: agility-relic
      share: 0.3
    - name: purification-beads
      share: 0.27
    - name: sundering-arc
      share: 0.19
    matches_by_window:
      ob47: 37
      ob46: 112
    unmapped_slugs:
    - aegis-of-acceleration
    - agility-relic
    - brawlers-ruin
    - phantom-shell
    - purification-beads
    - sundering-arc
---
