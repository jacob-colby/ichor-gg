---
type: smite-build
god: Apollo
mode: Conquest
builds:
- source: community
  aspect: Aspect of Harmony
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.33
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.74
    win_rate: 0.48
    alternates:
    - name: Tyrfing
      pick_rate: 0.14
      win_rate: 0.58
    - name: Avenging Blade
      pick_rate: 0.04
      win_rate: 0.43
  - name: Dagger of Frenzy
    pick_rate: 0.57
    win_rate: 0.43
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.18
      win_rate: 0.43
    - name: Tyrfing
      pick_rate: 0.08
      win_rate: 0.62
  - name: Dominance
    pick_rate: 0.34
    win_rate: 0.39
    alternates:
    - name: The Executioner
      pick_rate: 0.2
      win_rate: 0.52
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.61
  - name: Silverbranch Bow
    pick_rate: 0.36
    win_rate: 0.49
    alternates:
    - name: The Executioner
      pick_rate: 0.16
      win_rate: 0.38
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.52
  - name: Riptalon
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.5
    - name: Deathbringer
      pick_rate: 0.11
      win_rate: 0.18
  - name: Manchu Bow
    pick_rate: 0.1
    win_rate: 0.55
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.7
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.63
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.44
    win_rate: 0.48
  - name: Gilded Arrow
    pick_rate: 0.18
    win_rate: 0.37
  - name: Hunter's Cowl
    pick_rate: 0.18
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/apollo/
  last_verified: '2026-11-06'
  god_win_rate: 0.46987951807228917
  god_matches_won: 78
  god_matches_played: 166
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Silverbranch Bow
  - Riptalon
  flex_slots:
  - Lernaean Bow
  - The Reaper
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
    this god: Tyrfing, Jotunn''s Revenge, Lernaean Bow, The Reaper, Tekko-Kagi, Golden
    Blade, Demon Blade, Hydra''s Lament, Rage, The Crusher, Heartseeker, Qin''s Blade,
    Arondight, Titan''s Bane, Toxic Blade, Bloodforge, Musashi''s Dual Swords, Barbed
    Carver, Berserker''s Shield, Transcendence, Runeforged Hammer, Avatar''s Parashu,
    Shield Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.47
      efficiency: 0.47
      win: 0.48
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.58
      pick: 0.14
      fit: 0.7
    The Reaper:
      total: 0.47
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.37
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.49
      win: 0.49
      pick: 0.6
      fit: 0.45
    Riptalon:
      total: 0.54
      efficiency: 0.45
      win: 0.63
      pick: 0.39
      fit: 0.56
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Hydra's Lament
  - Silverbranch Bow
  - Riptalon
  flex_slots:
  - Silverbranch Bow
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Tyrfing,
    Jotunn''s Revenge, Hydra''s Lament, The Reaper, Heartseeker, Tekko-Kagi, The Crusher,
    Lernaean Bow, Titan''s Bane, Arondight, Golden Blade, Rage, Transcendence, Avatar''s
    Parashu, Demon Blade, Toxic Blade, Qin''s Blade, Genji''s Guard, Runeforged Hammer,
    Bloodforge, Barbed Carver, Pendulum Blade, Damaru, Shield Splitter, Eye of the
    Storm, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.43
      efficiency: 0.5
      win: 0.48
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.14
      fit: 0.49
    Hydra's Lament:
      total: 0.47
      efficiency: 0.55
      win: 0.48
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.47
      efficiency: 0.49
      win: 0.49
      pick: 0.6
      fit: 0.33
    Riptalon:
      total: 0.52
      efficiency: 0.45
      win: 0.63
      pick: 0.39
      fit: 0.39
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Rage
  - Jotunn's Revenge
  - Tyrfing
  - Musashi's Dual Swords
  - Riptalon
  - Demon Blade
  flex_slots:
  - Rage
  - Musashi's Dual Swords
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, Jotunn''s Revenge, The Reaper, Lernaean Bow, Tekko-Kagi, Demon
    Blade, Golden Blade, Hydra''s Lament, Rage, The Crusher, Heartseeker, Qin''s Blade,
    Arondight, Titan''s Bane, Toxic Blade, Musashi''s Dual Swords, Bloodforge, Berserker''s
    Shield, Barbed Carver, Transcendence, Runeforged Hammer, Avatar''s Parashu, Shield
    Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Rage:
      total: 0.46
      efficiency: 0.46
      win: 0.48
      pick: 0.0
      fit: 0.52
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.28
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.14
      fit: 0.66
    Musashi's Dual Swords:
      total: 0.43
      efficiency: 0.38
      win: 0.48
      pick: 0.0
      fit: 0.52
    Riptalon:
      total: 0.54
      efficiency: 0.45
      win: 0.63
      pick: 0.39
      fit: 0.54
    Demon Blade:
      total: 0.46
      efficiency: 0.36
      win: 0.48
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Tyrfing
  - Riptalon
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Tyrfing, Shield of the Phoenix,
    Kinetic Cuirass, The Reaper, Genji''s Guard, Phoenix Feather, Yogi''s Necklace,
    Jotunn''s Revenge, Shield Splitter, Golden Blade, Freya''s Tears, Runeforged Hammer,
    Oni Hunter''s Garb, Breastplate of Valor, Draconic Scale, Chandra''s Grace, Shogun''s
    Ofuda, Pharaoh''s Curse, Bloodforge, Erosion, Eye of Providence, Midgardian Mail,
    Hydra''s Lament, Shifter''s Shield, Regrowth Striders, Lernaean Bow, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.48
      pick: 0.0
      fit: 0.14
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.48
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.48
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.14
      fit: 0.48
    Riptalon:
      total: 0.56
      efficiency: 0.45
      win: 0.63
      pick: 0.39
      fit: 0.65
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.48
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Tyrfing
  - Riptalon
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Tekko-Kagi
  - Silverbranch Bow
  - Riptalon
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Tyrfing, Jotunn''s Revenge, The Reaper, Tekko-Kagi, The Crusher,
    Heartseeker, Titan''s Bane, Toxic Blade, Lernaean Bow, Hydra''s Lament, Avatar''s
    Parashu, Golden Blade, Rage, Pendulum Blade, Demon Blade, Arondight, Qin''s Blade,
    Avenging Blade, Oath-Sworn Spear, Transcendence, Bloodforge, Runeforged Hammer,
    Berserker''s Shield, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.14
      fit: 0.53
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.48
      pick: 0.0
      fit: 0.68
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.49
      win: 0.49
      pick: 0.6
      fit: 0.61
    Riptalon:
      total: 0.56
      efficiency: 0.45
      win: 0.63
      pick: 0.39
      fit: 0.69
    The Crusher:
      total: 0.48
      efficiency: 0.51
      win: 0.48
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  flex_slots:
  - Golden Blade
  - Lernaean Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, Jotunn''s Revenge, Golden Blade, Lernaean Bow, The Reaper,
    Tekko-Kagi, Qin''s Blade, Hydra''s Lament, Toxic Blade, Demon Blade, The Crusher,
    Rage, Heartseeker, Arondight, Titan''s Bane, Berserker''s Shield, Sun Beam Bow,
    Bloodforge, Transcendence, Runeforged Hammer, Barbed Carver, Musashi''s Dual Swords,
    Avatar''s Parashu, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.45
      win: 0.48
      pick: 0.0
      fit: 0.6
    Lernaean Bow:
      total: 0.46
      efficiency: 0.47
      win: 0.48
      pick: 0.0
      fit: 0.52
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.22
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.58
      pick: 0.14
      fit: 0.7
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.49
      win: 0.49
      pick: 0.6
      fit: 0.5
    Riptalon:
      total: 0.55
      efficiency: 0.45
      win: 0.63
      pick: 0.39
      fit: 0.59
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Arondight
  - Silverbranch Bow
  - Riptalon
  flex_slots:
  - Silverbranch Bow
  - Arondight
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Tyrfing, Jotunn''s Revenge, Hydra''s
    Lament, Arondight, The Reaper, Lernaean Bow, Damaru, Genji''s Guard, Tekko-Kagi,
    The Crusher, Golden Blade, Qin''s Blade, Heartseeker, Rage, Breastplate of Valor,
    Pendulum Blade, Chandra''s Grace, Titan''s Bane, Demon Blade, Toxic Blade, Berserker''s
    Shield, Transcendence, Runeforged Hammer, Bloodforge, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.58
      pick: 0.14
      fit: 0.46
    Hydra's Lament:
      total: 0.49
      efficiency: 0.55
      win: 0.48
      pick: 0.0
      fit: 0.5
    Arondight:
      total: 0.46
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.4
    Silverbranch Bow:
      total: 0.47
      efficiency: 0.49
      win: 0.49
      pick: 0.6
      fit: 0.31
    Riptalon:
      total: 0.52
      efficiency: 0.45
      win: 0.63
      pick: 0.39
      fit: 0.38
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - The Reaper
  - Tekko-Kagi
  flex_slots:
  - The Reaper
  - Tekko-Kagi
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Tyrfing, Jotunn''s Revenge, Lernaean Bow, The Reaper,
    Tekko-Kagi, Golden Blade, Demon Blade, Hydra''s Lament, Rage, The Crusher, Heartseeker,
    Qin''s Blade, Arondight, Titan''s Bane, Toxic Blade, Bloodforge, Musashi''s Dual
    Swords, Barbed Carver, Berserker''s Shield, Transcendence, Runeforged Hammer,
    Avatar''s Parashu, Shield Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.47
      efficiency: 0.47
      win: 0.48
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.58
      pick: 0.14
      fit: 0.7
    Dominance:
      total: 0.46
      efficiency: 0.47
      win: 0.39
      pick: 0.53
      fit: 0.6
    The Reaper:
      total: 0.47
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.37
    Tekko-Kagi:
      total: 0.47
      efficiency: 0.49
      win: 0.48
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Dominance
  starter: *id001
---
