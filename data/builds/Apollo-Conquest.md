---
type: smite-build
god: Apollo
mode: Conquest
builds:
- source: community
  aspect: Aspect of Harmony
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.63
    win_rate: 0.56
    alternates:
    - name: Tyrfing
      pick_rate: 0.23
      win_rate: 0.4
    - name: Toxic Blade
      pick_rate: 0.05
      win_rate: 0.67
  - name: Dagger of Frenzy
    pick_rate: 0.4
    win_rate: 0.58
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.25
      win_rate: 0.44
    - name: Tyrfing
      pick_rate: 0.12
      win_rate: 0.88
  - name: Dominance
    pick_rate: 0.22
    win_rate: 0.64
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.22
      win_rate: 0.57
    - name: Silverbranch Bow
      pick_rate: 0.13
      win_rate: 0.38
  - name: Silverbranch Bow
    pick_rate: 0.22
    win_rate: 0.64
    alternates:
    - name: Riptalon
      pick_rate: 0.17
      win_rate: 0.64
    - name: Dominance
      pick_rate: 0.13
      win_rate: 0.75
  - name: Riptalon
    pick_rate: 0.28
    win_rate: 0.6
    alternates:
    - name: The Executioner
      pick_rate: 0.11
      win_rate: 0.33
    - name: Deathbringer
      pick_rate: 0.09
      win_rate: 1.0
  - name: Hunter's Bow
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.75
    - name: The Executioner
      pick_rate: 0.11
      win_rate: 0.5
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.29
    win_rate: 0.74
  - name: Gilded Arrow
    pick_rate: 0.25
    win_rate: 0.44
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/apollo/
  last_verified: '2026-10-07'
  god_win_rate: 0.5384615384615384
  god_matches_won: 35
  god_matches_played: 65
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Dominance
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  flex_slots:
  - Dominance
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Lernaean Bow, Toxic Blade, Golden Blade, Tekko-Kagi,
    Demon Blade, The Reaper, Hydra''s Lament, Musashi''s Dual Swords, Heartseeker,
    Damaru, Rage, Qin''s Blade, Titan''s Bane, The Crusher, Transcendence, Arondight,
    Runeforged Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver, Avenging
    Blade, Avatar''s Parashu, Bloodforge, Pendulum Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.3
    Dominance:
      total: 0.55
      efficiency: 0.45
      win: 0.64
      pick: 0.34
      fit: 0.6
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.64
      pick: 0.37
      fit: 0.45
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.61
      fit: 0.56
    Deathbringer:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.19
      fit: 0.5
  community_ordered:
  - Dominance
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Dominance
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  flex_slots:
  - Dominance
  - Hydra's Lament
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, Toxic Blade, The Reaper,
    Tekko-Kagi, Titan''s Bane, Golden Blade, The Crusher, Transcendence, Arondight,
    Musashi''s Dual Swords, Demon Blade, Runeforged Hammer, Pendulum Blade, Avatar''s
    Parashu, Damaru, Rage, Avenging Blade, Qin''s Blade, Barbed Carver, Berserker''s
    Shield, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.42
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.64
      pick: 0.34
      fit: 0.5
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.64
      pick: 0.37
      fit: 0.33
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.61
      fit: 0.39
    Deathbringer:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.19
      fit: 0.34
  community_ordered:
  - Dominance
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Silverbranch Bow
  - Demon Blade
  - Riptalon
  - Deathbringer
  flex_slots:
  - Demon Blade
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
    this god: Jotunn''s Revenge, Lernaean Bow, Toxic Blade, Demon Blade, Golden Blade,
    Tekko-Kagi, The Reaper, Musashi''s Dual Swords, Hydra''s Lament, Heartseeker,
    Damaru, Rage, Qin''s Blade, Titan''s Bane, The Crusher, Transcendence, Arondight,
    Runeforged Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver, Avenging
    Blade, Avatar''s Parashu, Bloodforge, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.28
    Musashi's Dual Swords:
      total: 0.5
      efficiency: 0.46
      win: 0.58
      pick: 0.0
      fit: 0.52
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.64
      pick: 0.37
      fit: 0.43
    Demon Blade:
      total: 0.51
      efficiency: 0.38
      win: 0.58
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.61
      fit: 0.54
    Deathbringer:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.19
      fit: 0.52
  community_ordered:
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Silverbranch Bow
  - Deathbringer
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, The Reaper, Kinetic Cuirass, Golden Blade, Runeforged Hammer, Freya''s
    Tears, Genji''s Guard, Breastplate of Valor, Shifter''s Shield, Yogi''s Necklace,
    Shield Splitter, Pharaoh''s Curse, Lernaean Bow, Shogun''s Ofuda, Eye of the Storm,
    Phoenix Feather, Erosion, Eye of Providence, Draconic Scale, Chandra''s Grace,
    Hydra''s Lament, Daybreak Gavel, Avenging Blade, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.19
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.64
      pick: 0.37
      fit: 0.28
    Deathbringer:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.19
      fit: 0.32
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.6
      pick: 0.61
      fit: 0.65
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Silverbranch Bow
  - Deathbringer
  - Riptalon
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Silverbranch Bow
  - Tekko-Kagi
  - Riptalon
  - Deathbringer
  flex_slots:
  - Toxic Blade
  - Tekko-Kagi
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Toxic Blade, The Reaper, Tekko-Kagi, Heartseeker,
    Titan''s Bane, The Crusher, Lernaean Bow, Avenging Blade, Hydra''s Lament, Avatar''s
    Parashu, Golden Blade, Pendulum Blade, Demon Blade, Musashi''s Dual Swords, Oath-Sworn
    Spear, Transcendence, Runeforged Hammer, Qin''s Blade, Arondight, Damaru, Rage,
    Berserker''s Shield, Barbed Carver.'
  slot_scores:
    Toxic Blade:
      total: 0.55
      efficiency: 0.44
      win: 0.67
      pick: 0.05
      fit: 0.61
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.5
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.64
      pick: 0.37
      fit: 0.61
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.68
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.6
      pick: 0.61
      fit: 0.69
    Deathbringer:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.19
      fit: 0.36
  community_ordered:
  - Toxic Blade
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Dominance
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  flex_slots:
  - Dominance
  - Toxic Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Toxic Blade, Lernaean Bow, Golden Blade, Tekko-Kagi,
    The Reaper, Hydra''s Lament, Demon Blade, Qin''s Blade, Heartseeker, Musashi''s
    Dual Swords, Sun Beam Bow, Titan''s Bane, The Crusher, Transcendence, Damaru,
    Rage, Runeforged Hammer, Berserker''s Shield, Arondight, Avenging Blade, Barbed
    Carver, Vital Amplifier, Avatar''s Parashu.'
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.05
      fit: 0.5
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.22
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.64
      pick: 0.34
      fit: 0.52
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.64
      pick: 0.37
      fit: 0.5
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.6
      pick: 0.61
      fit: 0.59
    Deathbringer:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.19
      fit: 0.38
  community_ordered:
  - Toxic Blade
  - Dominance
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  flex_slots:
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Toxic Blade, Lernaean Bow, Arondight, The Reaper, Tekko-Kagi, Golden Blade, Heartseeker,
    Pendulum Blade, Breastplate of Valor, Demon Blade, Musashi''s Dual Swords, Genji''s
    Guard, Qin''s Blade, Titan''s Bane, The Crusher, Transcendence, Runeforged Hammer,
    Damaru, Berserker''s Shield, Rage, Avenging Blade, Sun Beam Bow, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.5
    Arondight:
      total: 0.5
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.4
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.64
      pick: 0.37
      fit: 0.31
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.61
      fit: 0.38
    Deathbringer:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.19
      fit: 0.29
  community_ordered:
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Jotunn's Revenge
  - Riptalon
  - Tekko-Kagi
  flex_slots:
  - Golden Blade
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
    Underrated for this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, Tekko-Kagi,
    Demon Blade, The Reaper, Hydra''s Lament, Musashi''s Dual Swords, Heartseeker,
    Damaru, Rage, Toxic Blade, Qin''s Blade, Titan''s Bane, The Crusher, Transcendence,
    Arondight, Runeforged Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver,
    Avenging Blade, Avatar''s Parashu, Bloodforge, Pendulum Blade.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.47
      win: 0.58
      pick: 0.0
      fit: 0.6
    Lernaean Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.6
    Tyrfing:
      total: 0.47
      efficiency: 0.48
      win: 0.4
      pick: 0.23
      fit: 0.7
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.3
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.61
      fit: 0.56
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Riptalon
  starter: *id001
---
