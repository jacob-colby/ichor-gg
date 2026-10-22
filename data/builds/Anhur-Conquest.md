---
type: smite-build
god: Anhur
mode: Conquest
builds:
- source: community
  aspect: Aspect of Pride
  aspect_pick_rate: 0.18
  aspect_win_rate: 0.36
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.75
    win_rate: 0.59
    alternates:
    - name: Tyrfing
      pick_rate: 0.13
      win_rate: 0.39
    - name: Avenging Blade
      pick_rate: 0.11
      win_rate: 0.56
  - name: Dagger of Frenzy
    pick_rate: 0.65
    win_rate: 0.57
    alternates:
    - name: The Executioner
      pick_rate: 0.06
      win_rate: 0.63
    - name: Odysseus' Bow
      pick_rate: 0.06
      win_rate: 0.5
  - name: Dominance
    pick_rate: 0.36
    win_rate: 0.6
    alternates:
    - name: The Executioner
      pick_rate: 0.16
      win_rate: 0.57
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.44
  - name: Riptalon
    pick_rate: 0.17
    win_rate: 0.65
    alternates:
    - name: The Executioner
      pick_rate: 0.16
      win_rate: 0.68
    - name: Dominance
      pick_rate: 0.13
      win_rate: 0.44
  - name: Silverbranch Bow
    pick_rate: 0.16
    win_rate: 0.55
    alternates:
    - name: Riptalon
      pick_rate: 0.19
      win_rate: 0.63
    - name: Deathbringer
      pick_rate: 0.15
      win_rate: 0.74
  - name: Hunter's Bow
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Bow
      pick_rate: 0.09
      win_rate: 0.78
    - name: Silverbranch Bow
      pick_rate: 0.07
      win_rate: 0.43
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.42
    win_rate: 0.63
  - name: Gilded Arrow
    pick_rate: 0.18
    win_rate: 0.44
  - name: Hunter's Cowl
    pick_rate: 0.18
    win_rate: 0.69
  source_url: https://smitebrain.com/gods/anhur/
  last_verified: '2026-10-22'
  god_win_rate: 0.5673758865248227
  god_matches_won: 80
  god_matches_played: 141
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-22'
  god_matches_analyzed: 1760
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Transcendence
  - Dominance
  - Riptalon
  - Deathbringer
  flex_slots:
  - Lernaean Bow
  - Transcendence
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
    The Reaper, Hydra''s Lament, Musashi''s Dual Swords, Heartseeker, Damaru, Rage,
    Toxic Blade, Qin''s Blade, Titan''s Bane, The Crusher, Transcendence, Arondight,
    Runeforged Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver, Avatar''s
    Parashu, Avenging Blade, Tyrfing, Bloodforge, Pendulum Blade.'
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
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.21
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.6
      pick: 0.56
      fit: 0.6
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.65
      pick: 0.28
      fit: 0.57
    Deathbringer:
      total: 0.6
      efficiency: 0.51
      win: 0.74
      pick: 0.32
      fit: 0.5
  community_ordered:
  - Dominance
  - Riptalon
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Dominance
  - Riptalon
  - Deathbringer
  flex_slots:
  - Hydra's Lament
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
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Golden
    Blade, Titan''s Bane, The Crusher, Transcendence, Arondight, Musashi''s Dual Swords,
    Demon Blade, Runeforged Hammer, Pendulum Blade, Toxic Blade, Avatar''s Parashu,
    Damaru, Rage, Qin''s Blade, Avenging Blade, Barbed Carver, Berserker''s Shield,
    Breastplate of Valor, Genji''s Guard, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.42
    Dominance:
      total: 0.53
      efficiency: 0.45
      win: 0.6
      pick: 0.56
      fit: 0.5
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.65
      pick: 0.28
      fit: 0.4
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.74
      pick: 0.32
      fit: 0.34
  community_ordered:
  - Dominance
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Dominance
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
    this god: Jotunn''s Revenge, Lernaean Bow, Demon Blade, Golden Blade, Tekko-Kagi,
    The Reaper, Musashi''s Dual Swords, Hydra''s Lament, Heartseeker, Damaru, Rage,
    Toxic Blade, Qin''s Blade, Titan''s Bane, The Crusher, Transcendence, Arondight,
    Runeforged Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver, Avatar''s
    Parashu, Avenging Blade, Tyrfing, Bloodforge, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.28
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.6
      pick: 0.56
      fit: 0.55
    Musashi's Dual Swords:
      total: 0.5
      efficiency: 0.46
      win: 0.58
      pick: 0.0
      fit: 0.52
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.65
      pick: 0.28
      fit: 0.55
    Demon Blade:
      total: 0.51
      efficiency: 0.38
      win: 0.58
      pick: 0.0
      fit: 0.79
    Deathbringer:
      total: 0.6
      efficiency: 0.51
      win: 0.74
      pick: 0.32
      fit: 0.52
  community_ordered:
  - Dominance
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Riptalon
  - Deathbringer
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, The Reaper, Kinetic Cuirass, Golden Blade, Runeforged Hammer, Freya''s
    Tears, Genji''s Guard, Breastplate of Valor, Shifter''s Shield, Yogi''s Necklace,
    Shield Splitter, Pharaoh''s Curse, Lernaean Bow, Shogun''s Ofuda, Eye of the Storm,
    Phoenix Feather, Erosion, Eye of Providence, Draconic Scale, Chandra''s Grace,
    Hydra''s Lament, Daybreak Gavel, Stone of Binding, Avenging Blade, Tyrfing.'
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
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.47
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.65
      pick: 0.28
      fit: 0.66
    Deathbringer:
      total: 0.57
      efficiency: 0.51
      win: 0.74
      pick: 0.32
      fit: 0.32
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Executioner
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  - Deathbringer
  flex_slots:
  - The Executioner
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
    Bane, The Crusher, Lernaean Bow, Toxic Blade, Avenging Blade, Hydra''s Lament,
    Golden Blade, Avatar''s Parashu, Pendulum Blade, Demon Blade, Musashi''s Dual
    Swords, Oath-Sworn Spear, Transcendence, Qin''s Blade, Runeforged Hammer, Arondight,
    Damaru, Rage, Berserker''s Shield, Barbed Carver, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.5
    The Executioner:
      total: 0.53
      efficiency: 0.35
      win: 0.68
      pick: 0.27
      fit: 0.61
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.65
      pick: 0.28
      fit: 0.69
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.35
      fit: 0.61
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.68
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.74
      pick: 0.32
      fit: 0.36
  community_ordered:
  - The Executioner
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Dominance
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Silverbranch Bow
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
    this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, Tekko-Kagi, The Reaper,
    Hydra''s Lament, Demon Blade, Qin''s Blade, Toxic Blade, Heartseeker, Musashi''s
    Dual Swords, Sun Beam Bow, Titan''s Bane, The Crusher, Transcendence, Damaru,
    Rage, Runeforged Hammer, Berserker''s Shield, Arondight, Tyrfing, Barbed Carver,
    Avenging Blade, Vital Amplifier, Avatar''s Parashu.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.52
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.22
    Dominance:
      total: 0.53
      efficiency: 0.45
      win: 0.6
      pick: 0.56
      fit: 0.52
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.65
      pick: 0.28
      fit: 0.59
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.55
      pick: 0.35
      fit: 0.5
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.74
      pick: 0.32
      fit: 0.38
  community_ordered:
  - Dominance
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Dominance
  - Arondight
  - Riptalon
  - Deathbringer
  flex_slots:
  - Dominance
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
    Lernaean Bow, Arondight, The Reaper, Tekko-Kagi, Golden Blade, Heartseeker, Pendulum
    Blade, Breastplate of Valor, Demon Blade, Musashi''s Dual Swords, Genji''s Guard,
    Qin''s Blade, Titan''s Bane, Toxic Blade, The Crusher, Transcendence, Runeforged
    Hammer, Damaru, Berserker''s Shield, Rage, Sun Beam Bow, Daybreak Gavel, Avenging
    Blade, Tyrfing.'
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
    Dominance:
      total: 0.51
      efficiency: 0.45
      win: 0.6
      pick: 0.56
      fit: 0.39
    Arondight:
      total: 0.5
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.4
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.65
      pick: 0.28
      fit: 0.39
    Deathbringer:
      total: 0.57
      efficiency: 0.51
      win: 0.74
      pick: 0.32
      fit: 0.29
  community_ordered:
  - Dominance
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
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
    Underrated for this god: Jotunn''s Revenge, Tyrfing, Lernaean Bow, Golden Blade,
    Tekko-Kagi, Demon Blade, The Reaper, Hydra''s Lament, Musashi''s Dual Swords,
    Heartseeker, Damaru, Rage, Toxic Blade, Qin''s Blade, Titan''s Bane, The Crusher,
    Transcendence, Arondight, Runeforged Hammer, Berserker''s Shield, Sun Beam Bow,
    Barbed Carver, Avenging Blade, Avatar''s Parashu, Bloodforge, Pendulum Blade.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.47
      win: 0.58
      pick: 0.0
      fit: 0.61
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
    Tyrfing:
      total: 0.46
      efficiency: 0.48
      win: 0.39
      pick: 0.13
      fit: 0.71
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.65
      pick: 0.28
      fit: 0.57
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
