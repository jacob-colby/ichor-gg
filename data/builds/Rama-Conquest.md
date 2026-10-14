---
type: smite-build
god: Rama
mode: Conquest
builds:
- source: community
  aspect: Aspect of Precision
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.75
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.76
    win_rate: 0.54
    alternates:
    - name: Tyrfing
      pick_rate: 0.2
      win_rate: 0.57
    - name: Avenging Blade
      pick_rate: 0.02
      win_rate: 0.6
  - name: Dagger of Frenzy
    pick_rate: 0.43
    win_rate: 0.52
    alternates:
    - name: Tyrfing
      pick_rate: 0.13
      win_rate: 0.54
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.55
  - name: Dominance
    pick_rate: 0.3
    win_rate: 0.57
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.13
      win_rate: 0.59
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.6
  - name: Riptalon
    pick_rate: 0.23
    win_rate: 0.52
    alternates:
    - name: The Executioner
      pick_rate: 0.16
      win_rate: 0.47
    - name: Silverbranch Bow
      pick_rate: 0.12
      win_rate: 0.49
  - name: Silverbranch Bow
    pick_rate: 0.15
    win_rate: 0.6
    alternates:
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.6
    - name: Deathbringer
      pick_rate: 0.11
      win_rate: 0.68
  - name: Deathbringer
    pick_rate: 0.12
    win_rate: 0.74
    alternates:
    - name: Manchu Bow
      pick_rate: 0.1
      win_rate: 0.53
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.27
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.4
    win_rate: 0.61
  - name: Gilded Arrow
    pick_rate: 0.24
    win_rate: 0.48
  - name: Hunter's Cowl
    pick_rate: 0.14
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/rama/
  last_verified: '2026-10-14'
  god_win_rate: 0.5392491467576792
  god_matches_won: 158
  god_matches_played: 293
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-14'
  god_matches_analyzed: 8861
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Dominance
  - The Reaper
  - Tekko-Kagi
  - Deathbringer
  flex_slots:
  - Tekko-Kagi
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
    this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, The Reaper, Heartseeker,
    Demon Blade, Hydra''s Lament, Titan''s Bane, The Crusher, Musashi''s Dual Swords,
    Avenging Blade, Damaru, Rage, Transcendence, Avatar''s Parashu, Arondight, Runeforged
    Hammer, Pendulum Blade, Golden Blade, Berserker''s Shield, Barbed Carver, Bloodforge,
    Vital Amplifier, Daybreak Gavel, Toxic Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.38
    Dominance:
      total: 0.52
      efficiency: 0.45
      win: 0.57
      pick: 0.47
      fit: 0.54
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.44
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.6
    Deathbringer:
      total: 0.59
      efficiency: 0.51
      win: 0.74
      pick: 0.37
      fit: 0.44
  community_ordered:
  - Dominance
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Dominance
  - Deathbringer
  flex_slots:
  - Lernaean Bow
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
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Titan''s
    Bane, The Crusher, Transcendence, Avenging Blade, Arondight, Musashi''s Dual Swords,
    Demon Blade, Runeforged Hammer, Pendulum Blade, Avatar''s Parashu, Damaru, Rage,
    Barbed Carver, Berserker''s Shield, Breastplate of Valor, Golden Blade, Genji''s
    Guard, Bloodforge, Daybreak Gavel.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.42
    Dominance:
      total: 0.51
      efficiency: 0.45
      win: 0.57
      pick: 0.47
      fit: 0.5
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.74
      pick: 0.37
      fit: 0.34
  community_ordered:
  - Dominance
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Dominance
  - Musashi's Dual Swords
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
    this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, The Reaper, Heartseeker,
    Demon Blade, Hydra''s Lament, Musashi''s Dual Swords, Titan''s Bane, The Crusher,
    Damaru, Rage, Avenging Blade, Transcendence, Avatar''s Parashu, Arondight, Runeforged
    Hammer, Pendulum Blade, Berserker''s Shield, Golden Blade, Barbed Carver, Bloodforge,
    Vital Amplifier, Daybreak Gavel, Toxic Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.36
    Dominance:
      total: 0.51
      efficiency: 0.45
      win: 0.57
      pick: 0.47
      fit: 0.5
    Musashi's Dual Swords:
      total: 0.48
      efficiency: 0.46
      win: 0.55
      pick: 0.0
      fit: 0.46
    Demon Blade:
      total: 0.49
      efficiency: 0.38
      win: 0.55
      pick: 0.0
      fit: 0.7
    Deathbringer:
      total: 0.6
      efficiency: 0.51
      win: 0.74
      pick: 0.37
      fit: 0.46
  community_ordered:
  - Dominance
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Dominance
  - The Reaper
  - Tekko-Kagi
  - Deathbringer
  flex_slots:
  - Tekko-Kagi
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
    Lernaean Bow, Titan''s Bane, The Crusher, Pendulum Blade, Arondight, Avenging
    Blade, Avatar''s Parashu, Musashi''s Dual Swords, Demon Blade, Transcendence,
    Runeforged Hammer, Damaru, Rage, Berserker''s Shield, Breastplate of Valor, Barbed
    Carver, Daybreak Gavel, Golden Blade, Genji''s Guard, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.46
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.13
    Dominance:
      total: 0.5
      efficiency: 0.45
      win: 0.57
      pick: 0.47
      fit: 0.4
    The Reaper:
      total: 0.5
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.39
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.5
    Deathbringer:
      total: 0.57
      efficiency: 0.51
      win: 0.74
      pick: 0.37
      fit: 0.3
  community_ordered:
  - Dominance
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - Deathbringer
  - Amanita Charm
  flex_slots:
  - The Reaper
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
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, The Reaper, Shield
    of the Phoenix, Kinetic Cuirass, Runeforged Hammer, Freya''s Tears, Genji''s Guard,
    Breastplate of Valor, Avenging Blade, Yogi''s Necklace, Shifter''s Shield, Shield
    Splitter, Pharaoh''s Curse, Lernaean Bow, Shogun''s Ofuda, Eye of the Storm, Phoenix
    Feather, Erosion, Tekko-Kagi, Eye of Providence, Heartseeker, Daybreak Gavel,
    Chandra''s Grace, Hydra''s Lament, Draconic Scale, Stone of Binding, Midgardian
    Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.59
    Deathbringer:
      total: 0.57
      efficiency: 0.51
      win: 0.74
      pick: 0.37
      fit: 0.29
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Tekko-Kagi
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker, Avenging
    Blade, Titan''s Bane, The Crusher, Lernaean Bow, Hydra''s Lament, Avatar''s Parashu,
    Pendulum Blade, Demon Blade, Musashi''s Dual Swords, Oath-Sworn Spear, Transcendence,
    Runeforged Hammer, Arondight, Damaru, Rage, Toxic Blade, Berserker''s Shield,
    Golden Blade, Barbed Carver, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.5
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.15
    The Reaper:
      total: 0.52
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.55
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.68
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.74
      pick: 0.37
      fit: 0.36
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.55
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Riptalon
  - Dominance
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
    Toxic Blade, Heartseeker, Hydra''s Lament, Demon Blade, Qin''s Blade, Titan''s
    Bane, The Crusher, Musashi''s Dual Swords, Avenging Blade, Sun Beam Bow, Transcendence,
    Runeforged Hammer, Arondight, Damaru, Rage, Berserker''s Shield, Avatar''s Parashu,
    Pendulum Blade, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.29
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.57
      pick: 0.2
      fit: 0.64
    Dominance:
      total: 0.51
      efficiency: 0.45
      win: 0.57
      pick: 0.47
      fit: 0.48
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.52
      pick: 0.38
      fit: 0.62
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.32
      fit: 0.54
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.74
      pick: 0.37
      fit: 0.35
  community_ordered:
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Dominance
  - Arondight
  - Deathbringer
  flex_slots:
  - Arondight
  - Transcendence
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
    Lernaean Bow, The Reaper, Arondight, Tekko-Kagi, Heartseeker, Pendulum Blade,
    Titan''s Bane, The Crusher, Breastplate of Valor, Avenging Blade, Musashi''s Dual
    Swords, Demon Blade, Genji''s Guard, Transcendence, Runeforged Hammer, Berserker''s
    Shield, Damaru, Rage, Avatar''s Parashu, Daybreak Gavel, Barbed Carver, Eye of
    Erebus, Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.08
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.47
    Dominance:
      total: 0.49
      efficiency: 0.45
      win: 0.57
      pick: 0.47
      fit: 0.37
    Arondight:
      total: 0.48
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.37
    Deathbringer:
      total: 0.57
      efficiency: 0.51
      win: 0.74
      pick: 0.37
      fit: 0.27
  community_ordered:
  - Dominance
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
    Heartseeker, Demon Blade, Hydra''s Lament, Titan''s Bane, The Crusher, Musashi''s
    Dual Swords, Damaru, Rage, Transcendence, Avatar''s Parashu, Arondight, Runeforged
    Hammer, Pendulum Blade, Golden Blade, Berserker''s Shield, Avenging Blade, Barbed
    Carver, Bloodforge, Vital Amplifier, Daybreak Gavel, Toxic Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.44
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.6
    Deathbringer:
      total: 0.59
      efficiency: 0.51
      win: 0.74
      pick: 0.37
      fit: 0.44
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.55
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Deathbringer
  starter: *id001
---
