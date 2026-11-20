---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.45
  aspect_win_rate: 0.53
  slot_order:
  - name: Ancient Signet
    pick_rate: 0.27
    win_rate: 0.56
    alternates:
    - name: Golden Blade
      pick_rate: 0.12
      win_rate: 0.25
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.25
  - name: Berserker's Shield
    pick_rate: 0.18
    win_rate: 0.33
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.15
      win_rate: 0.6
    - name: Helm of Radiance
      pick_rate: 0.12
      win_rate: 1.0
  - name: Kinetic Cuirass
    pick_rate: 0.18
    win_rate: 0.67
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.15
      win_rate: 0.4
    - name: Sphere of Negation
      pick_rate: 0.09
      win_rate: 1.0
  - name: Rod of Tahuti
    pick_rate: 0.12
    win_rate: 1.0
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.12
      win_rate: 0.25
    - name: Contagion
      pick_rate: 0.12
      win_rate: 0.75
  - name: Medal of Disruption
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Soul Reaver
      pick_rate: 0.1
      win_rate: 0.33
    - name: Contagion
      pick_rate: 0.1
      win_rate: 0.33
  - name: Sundering Echo
    pick_rate: 0.11
    win_rate: 1.0
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 1.0
    - name: Medallion
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.21
    win_rate: 0.29
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.5
  - name: Sundering Axe
    pick_rate: 0.15
    win_rate: 0.8
  community_relics:
  - name: Aegis of Acceleration
    pick_rate: 0.36
    win_rate: 0.5
  - name: Sundering Arc
    pick_rate: 0.3
    win_rate: 0.5
  - name: Phantom Shell
    pick_rate: 0.15
    win_rate: 0.2
  starter_sightings:
  - name: Death's Embrace
    pick_rate: 0.21
    win_rate: 0.29
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.5
  - name: Sundering Axe
    pick_rate: 0.15
    win_rate: 0.8
  - name: Warrior's Axe
    pick_rate: 0.12
    win_rate: 0.5
  - name: Death's Toll
    pick_rate: 0.09
    win_rate: 0.33
  - name: Archmage's Gem
    pick_rate: 0.06
    win_rate: 0.0
  - name: Bluestone Pendant
    pick_rate: 0.06
    win_rate: 0.5
  - name: Hunter's Cowl
    pick_rate: 0.03
    win_rate: 0.0
  - name: Leather Cowl
    pick_rate: 0.03
    win_rate: 1.0
  - name: Pendulum of the Ages
    pick_rate: 0.03
    win_rate: 0.0
  - name: Sands Of Time
    pick_rate: 0.03
    win_rate: 1.0
  relic_sightings:
  - name: Aegis of Acceleration
    pick_rate: 0.36
    win_rate: 0.5
  - name: Sundering Arc
    pick_rate: 0.3
    win_rate: 0.5
  - name: Phantom Shell
    pick_rate: 0.15
    win_rate: 0.2
  - name: Purification Beads
    pick_rate: 0.12
    win_rate: 0.75
  - name: Agility Relic
    pick_rate: 0.06
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-11-20'
  god_win_rate: 0.45454545454545453
  god_matches_won: 15
  god_matches_played: 33
  god_division: obsidian
  god_window_start: '2026-11-17'
  god_window_end: '2026-11-20'
  god_matches_analyzed: 2341
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
    pick_rate: 0.3
    win_rate: 0.302
    matches: 10
    basis: community
  relic:
    name: Aegis of Acceleration
    pick_rate: 0.36
    win_rate: 0.5
    matches: 12
    basis: community
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Tyrfing, Genji''s Guard, Shield Splitter,
    Runeforged Hammer, The Reaper, Freya''s Tears, Hydra''s Lament, Oni Hunter''s
    Garb, Breastplate of Valor, Shield of the Phoenix, Lernaean Bow, Dominance, Tekko-Kagi,
    Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, The Crusher,
    Midgardian Mail, Erosion, Toxic Blade, Eye of Providence, Heartseeker, Leviathan''s
    Hide, Shifter''s Shield, Golden Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.12
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.28
      fit: 0.42
    Shield Splitter:
      total: 0.5
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Kinetic Cuirass
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
    pick_rate: 0.3
    win_rate: 0.302
    matches: 10
    basis: community
  relic: &id002
    name: Aegis of Acceleration
    pick_rate: 0.36
    win_rate: 0.5
    matches: 12
    basis: community
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, The Reaper, Genji''s Guard, Shield
    Splitter, Phoenix Feather, Jotunn''s Revenge, Yogi''s Necklace, Tyrfing, Runeforged
    Hammer, Freya''s Tears, Riptalon, Oni Hunter''s Garb, Draconic Scale, Breastplate
    of Valor, Bloodforge, Chandra''s Grace, Erosion, Eye of Providence, Hydra''s Lament,
    Midgardian Mail, Shogun''s Ofuda, Pharaoh''s Curse, Shifter''s Shield, Leviathan''s
    Hide, Regrowth Striders, Lernaean Bow, Golden Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.15
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.28
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
  - Kinetic Cuirass
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, The Reaper, Avenging Blade, Genji''s
    Guard, Screeching Gargoyle, The Crusher, Tekko-Kagi, Stone of Binding, Tyrfing,
    Heartseeker, Void Stone, Void Shield, Toxic Blade, Titan''s Bane, Runeforged Hammer,
    Shield Splitter, Silverbranch Bow, Freya''s Tears, Breastplate of Valor, Riptalon,
    Hydra''s Lament, Oni Hunter''s Garb, Shield of the Phoenix, Lernaean Bow, Dominance,
    Avatar''s Parashu, Golden Blade.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.49
    Avenging Blade:
      total: 0.5
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.09
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.28
      fit: 0.34
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Toxic Blade
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Tyrfing, Genji''s Guard, Jotunn''s Revenge, Shield Splitter,
    Runeforged Hammer, Toxic Blade, Freya''s Tears, Breastplate of Valor, Oni Hunter''s
    Garb, The Reaper, Shogun''s Ofuda, Shield of the Phoenix, Pharaoh''s Curse, Lernaean
    Bow, Dominance, Silverbranch Bow, Hydra''s Lament, Riptalon, Tekko-Kagi, Draconic
    Scale, Midgardian Mail, Qin''s Blade, Erosion, Leviathan''s Hide, Eye of Providence,
    Hide of the Nemean Lion, Golden Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.48
      efficiency: 0.46
      win: 0.53
      pick: 0.0
      fit: 0.52
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.1
    Berserker's Shield:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.25
      fit: 0.41
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.28
      fit: 0.36
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Amanita Charm, Freya''s Tears, Breastplate of Valor, Shield of the Phoenix, Hydra''s
    Lament, Screeching Gargoyle, Tyrfing, Arondight, Runeforged Hammer, Shield Splitter,
    Oni Hunter''s Garb, Gladiator''s Shield, The Reaper, Chandra''s Grace, Draconic
    Scale, Midgardian Mail, Eye of Erebus, Damaru, Shogun''s Ofuda, Pharaoh''s Curse,
    Leviathan''s Hide, Eye of Providence, Erosion, Hide of the Nemean Lion, Golden
    Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.33
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.28
      fit: 0.34
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.4
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
  relic: *id002
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
  - Tyrfing
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Tyrfing, Genji''s Guard,
    Golden Blade, Shield Splitter, Runeforged Hammer, The Reaper, Freya''s Tears,
    Hydra''s Lament, Oni Hunter''s Garb, Breastplate of Valor, Shield of the Phoenix,
    Lernaean Bow, Dominance, Tekko-Kagi, Draconic Scale, Shogun''s Ofuda, Pharaoh''s
    Curse, Avenging Blade, The Crusher, Midgardian Mail, Erosion, Toxic Blade, Eye
    of Providence, Heartseeker, Leviathan''s Hide, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.12
    Berserker's Shield:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.25
      fit: 0.41
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.28
      fit: 0.42
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
  relic: *id002
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-09-24'
  partial_windows:
    ob44: '2026-09-24'
  minimum_matches: 30
  window_rule: the newest patch window; else the last closed one; else the newest
    windows pooled, reaching back one closed window at a time, until they hold minimum_matches
    of the aspect's matches
  item_changes: an item is flagged when its cost, tier or stats moved at a patch after
    the oldest window read (data/Analysis/snapshots); a passive change is not recorded
    there and is never flagged
  aspects:
  - aspect: Aspect of the Fragmented
    status: shown
    windows:
    - ob47
    patches: OB47
    window_rule: newest
    window_start: '2026-11-03'
    window_end: '2026-11-17'
    matches: 61
    wins: 33
    win_share: 0.54
    aggregate:
      aspect_matches: 75
      aspect_win_rate: 0.493
      no_aspect_matches: 160
      no_aspect_win_rate: 0.425
    roles:
    - role: Solo
      matches: 44
      share: 0.72
    - role: Mid
      matches: 8
      share: 0.13
    - role: Jungle
      matches: 5
      share: 0.08
    - role: Carry
      matches: 3
      share: 0.05
    - role: Support
      matches: 1
      share: 0.02
    base_role: Solo
    base_role_share: 0.72
    role_shift: null
    items:
    - name: Ancient Signet
      share: 0.44
    - name: Helm of Radiance
      share: 0.33
    - name: Sphere of Negation
      share: 0.33
    - name: Shifter's Shield
      share: 0.3
    - name: Prophetic Cloak
      share: 0.28
    - name: Rod of Tahuti
      share: 0.28
    - name: Freya's Tears
      share: 0.26
    - name: Spear of Desolation
      share: 0.21
    starters:
    - name: Sundering Axe
      share: 0.25
    - name: Archmage's Gem
      share: 0.23
    - name: Bluestone Brooch
      share: 0.23
    - name: Conduit Gem
      share: 0.13
    - name: Bluestone Pendant
      share: 0.07
    - name: Warrior's Axe
      share: 0.05
    - name: Death's Toll
      share: 0.02
    - name: Pendulum of the Ages
      share: 0.02
    - name: War Flag
      share: 0.02
    relics:
    - name: Purification Beads
      share: 0.38
    - name: Aegis of Acceleration
      share: 0.33
    - name: Phantom Shell
      share: 0.18
    matches_by_window:
      ob47: 61
      ob46: 45
      ob45: 43
      ob44: 72
    unmapped_slugs:
    - brawlers-ruin
---
