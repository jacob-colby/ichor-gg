---
type: smite-build
god: Rama
mode: Conquest
builds:
- source: community
  aspect: Aspect of Precision
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.8
    win_rate: 0.61
    alternates:
    - name: Tyrfing
      pick_rate: 0.14
      win_rate: 0.45
    - name: Avenging Blade
      pick_rate: 0.04
      win_rate: 0.67
  - name: Dagger of Frenzy
    pick_rate: 0.37
    win_rate: 0.62
    alternates:
    - name: Tyrfing
      pick_rate: 0.18
      win_rate: 0.58
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.39
  - name: Dominance
    pick_rate: 0.2
    win_rate: 0.48
    alternates:
    - name: The Executioner
      pick_rate: 0.18
      win_rate: 0.56
    - name: Odysseus' Bow
      pick_rate: 0.16
      win_rate: 0.57
  - name: Silverbranch Bow
    pick_rate: 0.21
    win_rate: 0.48
    alternates:
    - name: Riptalon
      pick_rate: 0.15
      win_rate: 0.57
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.59
  - name: Deathbringer
    pick_rate: 0.18
    win_rate: 0.54
    alternates:
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.71
    - name: Silverbranch Bow
      pick_rate: 0.13
      win_rate: 0.71
  - name: Manchu Bow
    pick_rate: 0.13
    win_rate: 0.54
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.11
      win_rate: 0.55
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.6
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.44
    win_rate: 0.68
  - name: Gilded Arrow
    pick_rate: 0.19
    win_rate: 0.54
  - name: Hunter's Cowl
    pick_rate: 0.14
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/rama/
  last_verified: '2026-09-25'
  god_win_rate: 0.5850340136054422
  god_matches_won: 86
  god_matches_played: 147
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-25'
  god_matches_analyzed: 2996
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - Tekko-Kagi
  - Deathbringer
  flex_slots:
  - Riptalon
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, The Reaper, Avenging Blade,
    Heartseeker, Demon Blade, Hydra''s Lament, Titan''s Bane, The Crusher, Musashi''s
    Dual Swords, Damaru, Rage, Transcendence, Avatar''s Parashu, Arondight, Runeforged
    Hammer, Pendulum Blade, Golden Blade, Berserker''s Shield, Barbed Carver, Bloodforge,
    Vital Amplifier, Daybreak Gavel, Toxic Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.51
      efficiency: 0.43
      win: 0.6
      pick: 0.31
      fit: 0.52
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.6
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.54
      pick: 0.39
      fit: 0.44
  community_ordered:
  - Riptalon
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Lernaean Bow
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Heartseeker
  flex_slots:
  - Avenging Blade
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
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, Avenging Blade, The Reaper,
    Tekko-Kagi, Titan''s Bane, The Crusher, Transcendence, Arondight, Musashi''s Dual
    Swords, Demon Blade, Runeforged Hammer, Pendulum Blade, Avatar''s Parashu, Damaru,
    Rage, Barbed Carver, Berserker''s Shield, Breastplate of Valor, Golden Blade,
    Genji''s Guard, Bloodforge, Daybreak Gavel.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.44
    Avenging Blade:
      total: 0.5
      efficiency: 0.44
      win: 0.67
      pick: 0.04
      fit: 0.28
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Avenging Blade
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Riptalon
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
    this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, The Reaper, Avenging Blade,
    Heartseeker, Demon Blade, Hydra''s Lament, Musashi''s Dual Swords, Titan''s Bane,
    The Crusher, Damaru, Rage, Transcendence, Avatar''s Parashu, Arondight, Runeforged
    Hammer, Pendulum Blade, Berserker''s Shield, Golden Blade, Barbed Carver, Bloodforge,
    Vital Amplifier, Daybreak Gavel, Toxic Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.36
    Musashi's Dual Swords:
      total: 0.49
      efficiency: 0.46
      win: 0.56
      pick: 0.0
      fit: 0.46
    Riptalon:
      total: 0.51
      efficiency: 0.43
      win: 0.6
      pick: 0.31
      fit: 0.5
    Demon Blade:
      total: 0.49
      efficiency: 0.38
      win: 0.56
      pick: 0.0
      fit: 0.7
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.54
      pick: 0.39
      fit: 0.46
  community_ordered:
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Hydra''s Lament, Heartseeker,
    Lernaean Bow, Avenging Blade, Titan''s Bane, The Crusher, Pendulum Blade, Arondight,
    Avatar''s Parashu, Musashi''s Dual Swords, Demon Blade, Transcendence, Runeforged
    Hammer, Damaru, Rage, Berserker''s Shield, Breastplate of Valor, Barbed Carver,
    Daybreak Gavel, Golden Blade, Genji''s Guard, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.46
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.13
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.36
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.39
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.5
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Avenging Blade
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, The Reaper, Avenging
    Blade, Shield of the Phoenix, Kinetic Cuirass, Runeforged Hammer, Freya''s Tears,
    Genji''s Guard, Breastplate of Valor, Yogi''s Necklace, Shifter''s Shield, Shield
    Splitter, Pharaoh''s Curse, Lernaean Bow, Shogun''s Ofuda, Eye of the Storm, Phoenix
    Feather, Erosion, Tekko-Kagi, Eye of Providence, Heartseeker, Daybreak Gavel,
    Chandra''s Grace, Hydra''s Lament, Draconic Scale, Stone of Binding, Midgardian
    Mail.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.67
      pick: 0.04
      fit: 0.35
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Avenging Blade
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Tekko-Kagi
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
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
    for this god: Jotunn''s Revenge, Avenging Blade, The Reaper, Tekko-Kagi, Heartseeker,
    Titan''s Bane, The Crusher, Lernaean Bow, Hydra''s Lament, Avatar''s Parashu,
    Pendulum Blade, Demon Blade, Musashi''s Dual Swords, Oath-Sworn Spear, Transcendence,
    Runeforged Hammer, Arondight, Damaru, Rage, Toxic Blade, Berserker''s Shield,
    Golden Blade, Barbed Carver, Daybreak Gavel.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.44
      win: 0.67
      pick: 0.04
      fit: 0.55
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.5
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.15
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.55
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.68
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Avenging Blade
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Tekko-Kagi
  flex_slots:
  - Tekko-Kagi
  - Golden Blade
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
    this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, Golden Blade, The Reaper,
    Avenging Blade, Toxic Blade, Heartseeker, Hydra''s Lament, Demon Blade, Qin''s
    Blade, Titan''s Bane, The Crusher, Musashi''s Dual Swords, Sun Beam Bow, Transcendence,
    Runeforged Hammer, Arondight, Damaru, Rage, Berserker''s Shield, Avatar''s Parashu,
    Pendulum Blade, Barbed Carver.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.29
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.58
      pick: 0.25
      fit: 0.64
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.31
      fit: 0.62
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Tyrfing
  - Riptalon
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Lernaean Bow
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Riptalon
  flex_slots:
  - Avenging Blade
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
    Lernaean Bow, The Reaper, Avenging Blade, Arondight, Tekko-Kagi, Heartseeker,
    Pendulum Blade, Titan''s Bane, The Crusher, Breastplate of Valor, Musashi''s Dual
    Swords, Demon Blade, Genji''s Guard, Transcendence, Runeforged Hammer, Berserker''s
    Shield, Damaru, Rage, Avatar''s Parashu, Daybreak Gavel, Barbed Carver, Eye of
    Erebus, Golden Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.37
    Avenging Blade:
      total: 0.49
      efficiency: 0.44
      win: 0.67
      pick: 0.04
      fit: 0.18
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.48
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.47
    Arondight:
      total: 0.48
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.49
      efficiency: 0.43
      win: 0.6
      pick: 0.31
      fit: 0.37
  community_ordered:
  - Avenging Blade
  - Riptalon
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
    Heartseeker, Demon Blade, Hydra''s Lament, Titan''s Bane, The Crusher, Musashi''s
    Dual Swords, Damaru, Rage, Transcendence, Avatar''s Parashu, Arondight, Runeforged
    Hammer, Pendulum Blade, Golden Blade, Berserker''s Shield, Avenging Blade, Barbed
    Carver, Bloodforge, Vital Amplifier, Daybreak Gavel, Toxic Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.44
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.6
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.54
      pick: 0.39
      fit: 0.44
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Deathbringer
  starter: *id001
---
