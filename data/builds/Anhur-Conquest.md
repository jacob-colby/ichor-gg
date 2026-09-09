---
type: smite-build
god: Anhur
mode: Conquest
builds:
- source: community
  aspect: Aspect of Pride
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.14
  slot_order:
  - name: Tyrfing
    pick_rate: 0.61
    win_rate: 0.45
    alternates:
    - name: Avenging Blade
      pick_rate: 0.22
      win_rate: 0.88
    - name: Devourer's Gauntlet
      pick_rate: 0.08
      win_rate: 1.0
  - name: Dagger of Frenzy
    pick_rate: 0.33
    win_rate: 0.67
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.5
    - name: Hastened Fatalis
      pick_rate: 0.11
      win_rate: 0.25
  - name: Odysseus' Bow
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Riptalon
      pick_rate: 0.19
      win_rate: 0.57
    - name: The Executioner
      pick_rate: 0.17
      win_rate: 1.0
  - name: The Executioner
    pick_rate: 0.36
    win_rate: 0.5
    alternates:
    - name: Riptalon
      pick_rate: 0.15
      win_rate: 0.8
    - name: Hastened Fatalis
      pick_rate: 0.09
      win_rate: 0.67
  - name: Silverbranch Bow
    pick_rate: 0.19
    win_rate: 0.5
    alternates:
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.25
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.33
  - name: Qin's Blade
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Bow
      pick_rate: 0.08
      win_rate: 0.0
    - name: Manchu Bow
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.31
    win_rate: 0.91
  - name: Gilded Arrow
    pick_rate: 0.28
    win_rate: 0.5
  - name: Hunter's Cowl
    pick_rate: 0.19
    win_rate: 0.29
  source_url: https://smitebrain.com/gods/anhur/
  last_verified: '2026-09-09'
  god_win_rate: 0.5833333333333334
  god_matches_won: 21
  god_matches_played: 36
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Dagger of Frenzy
  - Devourer's Gauntlet
  - Riptalon
  - Qin's Blade
  flex_slots:
  - Jotunn's Revenge
  - Dagger of Frenzy
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
    this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, Tekko-Kagi, Demon Blade,
    Deathbringer, The Reaper, Dominance, Hydra''s Lament, Musashi''s Dual Swords,
    Heartseeker, Damaru, Rage, Toxic Blade, Titan''s Bane, The Crusher, Transcendence,
    Arondight, Runeforged Hammer, Sun Beam Bow, Barbed Carver, Avatar''s Parashu,
    Bloodforge, Pendulum Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.61
      efficiency: 0.44
      win: 0.88
      pick: 0.22
      fit: 0.31
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.3
    Dagger of Frenzy:
      total: 0.51
      efficiency: 0.37
      win: 0.67
      pick: 0.45
      fit: 0.4
    Devourer's Gauntlet:
      total: 0.62
      efficiency: 0.33
      win: 1.0
      pick: 0.08
      fit: 0.32
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.3
      fit: 0.57
    Qin's Blade:
      total: 0.54
      efficiency: 0.37
      win: 0.67
      pick: 0.4
      fit: 0.6
  community_ordered:
  - Avenging Blade
  - Dagger of Frenzy
  - Devourer's Gauntlet
  - Riptalon
  - Qin's Blade
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Devourer's Gauntlet
  - Qin's Blade
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Heartseeker
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
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Dominance,
    Deathbringer, Golden Blade, Titan''s Bane, The Crusher, Transcendence, Arondight,
    Musashi''s Dual Swords, Demon Blade, Runeforged Hammer, Pendulum Blade, Toxic
    Blade, Avatar''s Parashu, Damaru, Rage, Barbed Carver, Breastplate of Valor, Genji''s
    Guard.'
  slot_scores:
    Avenging Blade:
      total: 0.6
      efficiency: 0.44
      win: 0.88
      pick: 0.22
      fit: 0.28
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.42
    Devourer's Gauntlet:
      total: 0.6
      efficiency: 0.33
      win: 1.0
      pick: 0.08
      fit: 0.24
    Qin's Blade:
      total: 0.52
      efficiency: 0.37
      win: 0.67
      pick: 0.4
      fit: 0.42
    Heartseeker:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Avenging Blade
  - Devourer's Gauntlet
  - Qin's Blade
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Avenging Blade
  - Devourer's Gauntlet
  - Musashi's Dual Swords
  - Qin's Blade
  - Demon Blade
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
    this god: Jotunn''s Revenge, Lernaean Bow, Deathbringer, Demon Blade, Golden Blade,
    Tekko-Kagi, The Reaper, Musashi''s Dual Swords, Dominance, Hydra''s Lament, Heartseeker,
    Damaru, Rage, Toxic Blade, Titan''s Bane, The Crusher, Transcendence, Arondight,
    Runeforged Hammer, Sun Beam Bow, Barbed Carver, Avatar''s Parashu, Bloodforge,
    Pendulum Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.6
      efficiency: 0.44
      win: 0.88
      pick: 0.22
      fit: 0.28
    Devourer's Gauntlet:
      total: 0.61
      efficiency: 0.33
      win: 1.0
      pick: 0.08
      fit: 0.29
    Musashi's Dual Swords:
      total: 0.47
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.52
    Qin's Blade:
      total: 0.54
      efficiency: 0.37
      win: 0.67
      pick: 0.4
      fit: 0.58
    Demon Blade:
      total: 0.48
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.79
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Avenging Blade
  - Devourer's Gauntlet
  - Qin's Blade
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Devourer's Gauntlet
  - Qin's Blade
  - Amanita Charm
  flex_slots:
  - Qin's Blade
  - Jotunn's Revenge
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
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, The Reaper,
    Kinetic Cuirass, Golden Blade, Runeforged Hammer, Freya''s Tears, Genji''s Guard,
    Breastplate of Valor, Shifter''s Shield, Yogi''s Necklace, Shield Splitter, Pharaoh''s
    Curse, Lernaean Bow, Shogun''s Ofuda, Eye of the Storm, Phoenix Feather, Erosion,
    Eye of Providence, Draconic Scale, Chandra''s Grace, Hydra''s Lament, Daybreak
    Gavel, Stone of Binding.'
  slot_scores:
    Avenging Blade:
      total: 0.64
      efficiency: 0.49
      win: 0.88
      pick: 0.22
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.15
      fit: 0.44
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.19
    Devourer's Gauntlet:
      total: 0.64
      efficiency: 0.33
      win: 1.0
      pick: 0.08
      fit: 0.5
    Qin's Blade:
      total: 0.52
      efficiency: 0.37
      win: 0.67
      pick: 0.4
      fit: 0.45
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  - Devourer's Gauntlet
  - Qin's Blade
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Devourer's Gauntlet
  - Qin's Blade
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - Silverbranch Bow
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker, Titan''s
    Bane, The Crusher, Lernaean Bow, Toxic Blade, Hydra''s Lament, Deathbringer, Golden
    Blade, Avatar''s Parashu, Dominance, Pendulum Blade, Demon Blade, Musashi''s Dual
    Swords, Oath-Sworn Spear, Transcendence, Runeforged Hammer, Arondight, Damaru,
    Rage, Barbed Carver.'
  slot_scores:
    Avenging Blade:
      total: 0.64
      efficiency: 0.44
      win: 0.88
      pick: 0.22
      fit: 0.55
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.5
    Devourer's Gauntlet:
      total: 0.6
      efficiency: 0.33
      win: 1.0
      pick: 0.08
      fit: 0.23
    Qin's Blade:
      total: 0.53
      efficiency: 0.37
      win: 0.67
      pick: 0.4
      fit: 0.49
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.41
      fit: 0.61
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Avenging Blade
  - Devourer's Gauntlet
  - Qin's Blade
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Dagger of Frenzy
  - Devourer's Gauntlet
  - Riptalon
  - Qin's Blade
  flex_slots:
  - Dagger of Frenzy
  - Jotunn's Revenge
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
    this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, Tekko-Kagi, Dominance,
    Deathbringer, The Reaper, Hydra''s Lament, Demon Blade, Toxic Blade, Heartseeker,
    Musashi''s Dual Swords, Sun Beam Bow, Titan''s Bane, The Crusher, Transcendence,
    Damaru, Rage, Runeforged Hammer, Arondight, Barbed Carver, Vital Amplifier, Avatar''s
    Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.6
      efficiency: 0.44
      win: 0.88
      pick: 0.22
      fit: 0.24
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.22
    Dagger of Frenzy:
      total: 0.52
      efficiency: 0.37
      win: 0.67
      pick: 0.45
      fit: 0.45
    Devourer's Gauntlet:
      total: 0.6
      efficiency: 0.33
      win: 1.0
      pick: 0.08
      fit: 0.24
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.57
      pick: 0.3
      fit: 0.59
    Qin's Blade:
      total: 0.55
      efficiency: 0.37
      win: 0.67
      pick: 0.4
      fit: 0.65
  community_ordered:
  - Avenging Blade
  - Dagger of Frenzy
  - Devourer's Gauntlet
  - Riptalon
  - Qin's Blade
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Devourer's Gauntlet
  - Qin's Blade
  - Arondight
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
    Lernaean Bow, Arondight, The Reaper, Deathbringer, Tekko-Kagi, Golden Blade, Dominance,
    Heartseeker, Pendulum Blade, Breastplate of Valor, Demon Blade, Musashi''s Dual
    Swords, Genji''s Guard, Titan''s Bane, Toxic Blade, The Crusher, Transcendence,
    Runeforged Hammer, Damaru, Rage, Sun Beam Bow, Daybreak Gavel.'
  slot_scores:
    Avenging Blade:
      total: 0.59
      efficiency: 0.44
      win: 0.88
      pick: 0.22
      fit: 0.19
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.5
    Devourer's Gauntlet:
      total: 0.59
      efficiency: 0.33
      win: 1.0
      pick: 0.08
      fit: 0.17
    Qin's Blade:
      total: 0.52
      efficiency: 0.37
      win: 0.67
      pick: 0.4
      fit: 0.47
    Arondight:
      total: 0.46
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Avenging Blade
  - Devourer's Gauntlet
  - Qin's Blade
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
    Demon Blade, Deathbringer, The Reaper, Dominance, Hydra''s Lament, Musashi''s
    Dual Swords, Heartseeker, Damaru, Rage, Toxic Blade, Titan''s Bane, The Crusher,
    Transcendence, Arondight, Runeforged Hammer, Sun Beam Bow, Barbed Carver, Avatar''s
    Parashu, Bloodforge, Pendulum Blade.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.61
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.45
      pick: 0.61
      fit: 0.71
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.3
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.3
      fit: 0.57
    Tekko-Kagi:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Riptalon
  starter: *id001
---
