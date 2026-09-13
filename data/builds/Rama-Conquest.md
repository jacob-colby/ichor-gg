---
type: smite-build
god: Rama
mode: Conquest
builds:
- source: community
  aspect: Aspect of Precision
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.36
  slot_order:
  - name: Tyrfing
    pick_rate: 0.61
    win_rate: 0.62
    alternates:
    - name: The Reaper
      pick_rate: 0.12
      win_rate: 0.43
    - name: Devourer's Gauntlet
      pick_rate: 0.11
      win_rate: 0.5
  - name: Odysseus' Bow
    pick_rate: 0.32
    win_rate: 0.62
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.16
      win_rate: 0.4
    - name: Dominance
      pick_rate: 0.15
      win_rate: 0.41
  - name: Silverbranch Bow
    pick_rate: 0.2
    win_rate: 0.42
    alternates:
    - name: Riptalon
      pick_rate: 0.18
      win_rate: 0.58
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.65
  - name: The Executioner
    pick_rate: 0.18
    win_rate: 0.64
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.17
      win_rate: 0.73
    - name: Demon Blade
      pick_rate: 0.12
      win_rate: 0.43
  - name: Riptalon
    pick_rate: 0.2
    win_rate: 0.56
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.22
      win_rate: 0.83
    - name: Manchu Bow
      pick_rate: 0.08
      win_rate: 0.46
  - name: Hunter's Bow
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Deathbringer
      pick_rate: 0.12
      win_rate: 0.57
    - name: Bow
      pick_rate: 0.07
      win_rate: 0.78
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.42
    win_rate: 0.58
  - name: Gilded Arrow
    pick_rate: 0.2
    win_rate: 0.35
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/rama/
  last_verified: '2026-09-13'
  god_win_rate: 0.5343915343915344
  god_matches_won: 101
  god_matches_played: 189
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-13'
  god_matches_analyzed: 5560
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - Jotunn's Revenge
  - Riptalon
  - Tekko-Kagi
  - Deathbringer
  flex_slots:
  - Lernaean Bow
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, Heartseeker, Hydra''s Lament,
    The Reaper, Titan''s Bane, The Crusher, Musashi''s Dual Swords, Damaru, Rage,
    Transcendence, Avatar''s Parashu, Arondight, Runeforged Hammer, Pendulum Blade,
    Golden Blade, Berserker''s Shield, Avenging Blade, Barbed Carver, Bloodforge,
    Vital Amplifier, Daybreak Gavel, Toxic Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.54
    Tyrfing:
      total: 0.52
      efficiency: 0.38
      win: 0.62
      pick: 0.61
      fit: 0.54
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.5
      efficiency: 0.43
      win: 0.56
      pick: 0.43
      fit: 0.52
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.6
    Deathbringer:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.37
      fit: 0.44
  community_ordered:
  - Tyrfing
  - Riptalon
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Transcendence
  - Hydra's Lament
  - Deathbringer
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
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
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, Tekko-Kagi, Titan''s Bane,
    The Crusher, Transcendence, The Reaper, Arondight, Musashi''s Dual Swords, Runeforged
    Hammer, Pendulum Blade, Avatar''s Parashu, Damaru, Rage, Avenging Blade, Barbed
    Carver, Berserker''s Shield, Breastplate of Valor, Golden Blade, Genji''s Guard,
    Bloodforge, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.51
      efficiency: 0.38
      win: 0.62
      pick: 0.61
      fit: 0.44
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.42
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.37
      fit: 0.34
    Heartseeker:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Musashi's Dual Swords
  - Riptalon
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Musashi's Dual Swords
  - Demon Blade
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
    this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, Heartseeker, Hydra''s Lament,
    Musashi''s Dual Swords, The Reaper, Titan''s Bane, The Crusher, Damaru, Rage,
    Transcendence, Avatar''s Parashu, Arondight, Runeforged Hammer, Pendulum Blade,
    Berserker''s Shield, Golden Blade, Avenging Blade, Barbed Carver, Bloodforge,
    Vital Amplifier, Daybreak Gavel, Toxic Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.52
      efficiency: 0.38
      win: 0.62
      pick: 0.61
      fit: 0.5
    Musashi's Dual Swords:
      total: 0.46
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.46
    Riptalon:
      total: 0.5
      efficiency: 0.43
      win: 0.56
      pick: 0.43
      fit: 0.5
    Demon Blade:
      total: 0.44
      efficiency: 0.38
      win: 0.43
      pick: 0.2
      fit: 0.7
    Deathbringer:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.37
      fit: 0.46
  community_ordered:
  - Tyrfing
  - Riptalon
  - Demon Blade
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Riptalon
  - Tekko-Kagi
  - Deathbringer
  flex_slots:
  - Tekko-Kagi
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Tekko-Kagi, Hydra''s Lament, Heartseeker, Lernaean Bow,
    Titan''s Bane, The Crusher, The Reaper, Pendulum Blade, Arondight, Avatar''s Parashu,
    Musashi''s Dual Swords, Transcendence, Runeforged Hammer, Damaru, Rage, Avenging
    Blade, Berserker''s Shield, Breastplate of Valor, Barbed Carver, Daybreak Gavel,
    Golden Blade, Genji''s Guard, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.5
      efficiency: 0.38
      win: 0.62
      pick: 0.61
      fit: 0.4
    Hydra's Lament:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.49
      efficiency: 0.43
      win: 0.56
      pick: 0.43
      fit: 0.43
    Tekko-Kagi:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.5
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.37
      fit: 0.3
  community_ordered:
  - Tyrfing
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Jotunn's Revenge
  - Riptalon
  - Deathbringer
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Deathbringer
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, Kinetic Cuirass, The Reaper, Runeforged Hammer, Freya''s Tears, Genji''s
    Guard, Breastplate of Valor, Yogi''s Necklace, Shifter''s Shield, Shield Splitter,
    Pharaoh''s Curse, Lernaean Bow, Shogun''s Ofuda, Eye of the Storm, Phoenix Feather,
    Erosion, Tekko-Kagi, Eye of Providence, Heartseeker, Daybreak Gavel, Chandra''s
    Grace, Hydra''s Lament, Draconic Scale, Avenging Blade, Stone of Binding, Midgardian
    Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.5
      efficiency: 0.38
      win: 0.62
      pick: 0.61
      fit: 0.39
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.25
    Riptalon:
      total: 0.52
      efficiency: 0.43
      win: 0.56
      pick: 0.43
      fit: 0.64
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.37
      fit: 0.29
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Tyrfing
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Tyrfing
  - The Executioner
  - Jotunn's Revenge
  - Riptalon
  - Tekko-Kagi
  - Deathbringer
  flex_slots:
  - Deathbringer
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
    for this god: Jotunn''s Revenge, Tekko-Kagi, Heartseeker, Titan''s Bane, The Crusher,
    Lernaean Bow, The Reaper, Avenging Blade, Hydra''s Lament, Avatar''s Parashu,
    Pendulum Blade, Musashi''s Dual Swords, Oath-Sworn Spear, Transcendence, Runeforged
    Hammer, Arondight, Damaru, Rage, Toxic Blade, Berserker''s Shield, Golden Blade,
    Barbed Carver, Daybreak Gavel.'
  slot_scores:
    Tyrfing:
      total: 0.51
      efficiency: 0.38
      win: 0.62
      pick: 0.61
      fit: 0.46
    The Executioner:
      total: 0.52
      efficiency: 0.35
      win: 0.64
      pick: 0.3
      fit: 0.61
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.5
    Riptalon:
      total: 0.51
      efficiency: 0.43
      win: 0.56
      pick: 0.43
      fit: 0.61
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.68
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.37
      fit: 0.36
  community_ordered:
  - Tyrfing
  - The Executioner
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - The Executioner
  - Jotunn's Revenge
  - Riptalon
  - Deathbringer
  flex_slots:
  - The Executioner
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
    this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, Golden Blade, Toxic Blade,
    Heartseeker, Hydra''s Lament, Qin''s Blade, Titan''s Bane, The Crusher, The Reaper,
    Musashi''s Dual Swords, Sun Beam Bow, Transcendence, Runeforged Hammer, Arondight,
    Damaru, Rage, Berserker''s Shield, Avatar''s Parashu, Pendulum Blade, Avenging
    Blade, Barbed Carver.'
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.62
      pick: 0.61
      fit: 0.64
    The Executioner:
      total: 0.48
      efficiency: 0.35
      win: 0.64
      pick: 0.3
      fit: 0.35
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.29
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.56
      pick: 0.43
      fit: 0.62
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.37
      fit: 0.35
  community_ordered:
  - Tyrfing
  - The Executioner
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Arondight
  - Riptalon
  - Deathbringer
  flex_slots:
  - Riptalon
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
    Lernaean Bow, Arondight, Tekko-Kagi, Heartseeker, Pendulum Blade, Titan''s Bane,
    The Crusher, The Reaper, Breastplate of Valor, Musashi''s Dual Swords, Genji''s
    Guard, Transcendence, Runeforged Hammer, Berserker''s Shield, Damaru, Rage, Avatar''s
    Parashu, Avenging Blade, Daybreak Gavel, Barbed Carver, Eye of Erebus, Golden
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.5
      efficiency: 0.38
      win: 0.62
      pick: 0.61
      fit: 0.37
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.47
    Arondight:
      total: 0.46
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.48
      efficiency: 0.43
      win: 0.56
      pick: 0.43
      fit: 0.37
    Deathbringer:
      total: 0.49
      efficiency: 0.51
      win: 0.57
      pick: 0.37
      fit: 0.27
  community_ordered:
  - Tyrfing
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - Deathbringer
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Deathbringer
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
    Underrated for this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, The Reaper,
    Heartseeker, Hydra''s Lament, Titan''s Bane, The Crusher, Musashi''s Dual Swords,
    Damaru, Rage, Transcendence, Avatar''s Parashu, Arondight, Runeforged Hammer,
    Pendulum Blade, Golden Blade, Berserker''s Shield, Avenging Blade, Barbed Carver,
    Bloodforge, Vital Amplifier, Daybreak Gavel, Toxic Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.46
      efficiency: 0.55
      win: 0.43
      pick: 0.12
      fit: 0.44
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.6
    Deathbringer:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.37
      fit: 0.44
    Heartseeker:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.54
  community_ordered:
  - The Reaper
  - Deathbringer
  starter: *id001
---
