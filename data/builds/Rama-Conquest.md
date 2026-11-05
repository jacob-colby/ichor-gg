---
type: smite-build
god: Rama
mode: Conquest
builds:
- source: community
  aspect: Aspect of Precision
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.29
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.77
    win_rate: 0.57
    alternates:
    - name: Tyrfing
      pick_rate: 0.19
      win_rate: 0.55
    - name: Avenging Blade
      pick_rate: 0.02
      win_rate: 0.6
  - name: Dagger of Frenzy
    pick_rate: 0.56
    win_rate: 0.6
    alternates:
    - name: Tyrfing
      pick_rate: 0.11
      win_rate: 0.51
    - name: Odysseus' Bow
      pick_rate: 0.08
      win_rate: 0.55
  - name: Dominance
    pick_rate: 0.34
    win_rate: 0.6
    alternates:
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.62
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.54
  - name: Riptalon
    pick_rate: 0.24
    win_rate: 0.6
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.2
      win_rate: 0.61
    - name: The Executioner
      pick_rate: 0.17
      win_rate: 0.59
  - name: Silverbranch Bow
    pick_rate: 0.16
    win_rate: 0.64
    alternates:
    - name: Deathbringer
      pick_rate: 0.16
      win_rate: 0.56
    - name: Riptalon
      pick_rate: 0.16
      win_rate: 0.62
  - name: Hunter's Bow
    pick_rate: 0.11
    win_rate: 0.54
    alternates:
    - name: Deathbringer
      pick_rate: 0.11
      win_rate: 0.72
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.67
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.46
    win_rate: 0.63
  - name: Gilded Arrow
    pick_rate: 0.18
    win_rate: 0.49
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/rama/
  last_verified: '2026-11-04'
  god_win_rate: 0.5653543307086614
  god_matches_won: 359
  god_matches_played: 635
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Riptalon
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
    this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Lernaean Bow, The Crusher,
    Hydra''s Lament, Heartseeker, Golden Blade, Titan''s Bane, Demon Blade, Toxic
    Blade, Rage, Qin''s Blade, Arondight, Avatar''s Parashu, Bloodforge, Transcendence,
    Berserker''s Shield, Barbed Carver, Runeforged Hammer, Musashi''s Dual Swords,
    Pendulum Blade, Shield Splitter, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.19
      fit: 0.65
    Dominance:
      total: 0.54
      efficiency: 0.47
      win: 0.6
      pick: 0.53
      fit: 0.54
    The Reaper:
      total: 0.53
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.54
      efficiency: 0.45
      win: 0.6
      pick: 0.4
      fit: 0.62
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.49
      win: 0.64
      pick: 0.35
      fit: 0.52
  community_ordered:
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Dominance
  - Hydra's Lament
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, The Reaper, Heartseeker, Tekko-Kagi, The Crusher, Lernaean
    Bow, Titan''s Bane, Arondight, Golden Blade, Rage, Transcendence, Avatar''s Parashu,
    Toxic Blade, Demon Blade, Qin''s Blade, Genji''s Guard, Runeforged Hammer, Bloodforge,
    Barbed Carver, Pendulum Blade, Avenging Blade, Damaru, Shield Splitter, Eye of
    the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.48
      efficiency: 0.5
      win: 0.59
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.55
      pick: 0.19
      fit: 0.5
    Dominance:
      total: 0.54
      efficiency: 0.47
      win: 0.6
      pick: 0.53
      fit: 0.5
    Hydra's Lament:
      total: 0.52
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.49
      win: 0.64
      pick: 0.35
      fit: 0.34
  community_ordered:
  - Tyrfing
  - Dominance
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Rage
  - Jotunn's Revenge
  - Dominance
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Rage
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Lernaean Bow, The Crusher,
    Hydra''s Lament, Heartseeker, Golden Blade, Demon Blade, Rage, Titan''s Bane,
    Toxic Blade, Qin''s Blade, Arondight, Avatar''s Parashu, Musashi''s Dual Swords,
    Bloodforge, Berserker''s Shield, Transcendence, Barbed Carver, Runeforged Hammer,
    Pendulum Blade, Shield Splitter, Eye of the Storm.'
  slot_scores:
    Rage:
      total: 0.5
      efficiency: 0.46
      win: 0.59
      pick: 0.0
      fit: 0.46
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.36
    Dominance:
      total: 0.54
      efficiency: 0.47
      win: 0.6
      pick: 0.53
      fit: 0.5
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.49
      win: 0.64
      pick: 0.35
      fit: 0.51
    Demon Blade:
      total: 0.5
      efficiency: 0.36
      win: 0.59
      pick: 0.0
      fit: 0.7
    Deathbringer:
      total: 0.49
      efficiency: 0.44
      win: 0.56
      pick: 0.35
      fit: 0.46
  community_ordered:
  - Dominance
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Dominance
  - Silverbranch Bow
  - The Reaper
  flex_slots:
  - Tyrfing
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
    god: Jotunn''s Revenge, The Reaper, Hydra''s Lament, Tekko-Kagi, The Crusher,
    Heartseeker, Titan''s Bane, Lernaean Bow, Arondight, Toxic Blade, Golden Blade,
    Avatar''s Parashu, Rage, Pendulum Blade, Qin''s Blade, Demon Blade, Damaru, Genji''s
    Guard, Transcendence, Runeforged Hammer, Bloodforge, Barbed Carver, Berserker''s
    Shield, Shield Splitter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.46
    Transcendence:
      total: 0.46
      efficiency: 0.5
      win: 0.59
      pick: 0.0
      fit: 0.13
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.55
      pick: 0.19
      fit: 0.47
    Dominance:
      total: 0.52
      efficiency: 0.47
      win: 0.6
      pick: 0.53
      fit: 0.4
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.49
      win: 0.64
      pick: 0.35
      fit: 0.44
    The Reaper:
      total: 0.52
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Tyrfing
  - Dominance
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
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
    this god: Amanita Charm, Berserker''s Shield, The Reaper, Shield of the Phoenix,
    Kinetic Cuirass, Genji''s Guard, Jotunn''s Revenge, Yogi''s Necklace, Phoenix
    Feather, Shield Splitter, Golden Blade, Freya''s Tears, Runeforged Hammer, Oni
    Hunter''s Garb, Breastplate of Valor, Chandra''s Grace, Draconic Scale, Bloodforge,
    Toxic Blade, Shogun''s Ofuda, Pharaoh''s Curse, Erosion, Tekko-Kagi, Midgardian
    Mail, Hydra''s Lament, Eye of Providence, Regrowth Striders, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.59
      pick: 0.0
      fit: 0.13
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Dominance
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Dominance
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
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, The Crusher, Heartseeker,
    Titan''s Bane, Toxic Blade, Lernaean Bow, Hydra''s Lament, Avenging Blade, Avatar''s
    Parashu, Golden Blade, Rage, Pendulum Blade, Demon Blade, Qin''s Blade, Arondight,
    Oath-Sworn Spear, Transcendence, Bloodforge, Runeforged Hammer, Berserker''s Shield,
    Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.5
    Dominance:
      total: 0.53
      efficiency: 0.47
      win: 0.6
      pick: 0.53
      fit: 0.46
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.68
    Riptalon:
      total: 0.55
      efficiency: 0.45
      win: 0.6
      pick: 0.4
      fit: 0.7
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.49
      win: 0.64
      pick: 0.35
      fit: 0.62
    The Crusher:
      total: 0.53
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Dominance
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dagger of Frenzy
  - Dominance
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Dominance
  - Dagger of Frenzy
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Golden Blade, Lernaean Bow,
    Toxic Blade, The Crusher, Hydra''s Lament, Qin''s Blade, Heartseeker, Titan''s
    Bane, Demon Blade, Rage, Arondight, Avatar''s Parashu, Berserker''s Shield, Transcendence,
    Bloodforge, Runeforged Hammer, Sun Beam Bow, Barbed Carver, Musashi''s Dual Swords,
    Damaru.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.29
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.19
      fit: 0.64
    Dagger of Frenzy:
      total: 0.52
      efficiency: 0.42
      win: 0.6
      pick: 0.76
      fit: 0.41
    Dominance:
      total: 0.53
      efficiency: 0.47
      win: 0.6
      pick: 0.53
      fit: 0.48
    Riptalon:
      total: 0.54
      efficiency: 0.45
      win: 0.6
      pick: 0.4
      fit: 0.62
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.49
      win: 0.64
      pick: 0.35
      fit: 0.54
  community_ordered:
  - Tyrfing
  - Dagger of Frenzy
  - Dominance
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Dominance
  - Riptalon
  - Silverbranch Bow
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
    Arondight, The Reaper, Tekko-Kagi, The Crusher, Lernaean Bow, Damaru, Genji''s
    Guard, Heartseeker, Titan''s Bane, Pendulum Blade, Golden Blade, Toxic Blade,
    Qin''s Blade, Rage, Breastplate of Valor, Chandra''s Grace, Demon Blade, Avatar''s
    Parashu, Berserker''s Shield, Transcendence, Runeforged Hammer, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.48
    Hydra's Lament:
      total: 0.53
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.47
    Arondight:
      total: 0.51
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.37
    Dominance:
      total: 0.52
      efficiency: 0.47
      win: 0.6
      pick: 0.53
      fit: 0.37
    Riptalon:
      total: 0.51
      efficiency: 0.45
      win: 0.6
      pick: 0.4
      fit: 0.44
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.49
      win: 0.64
      pick: 0.35
      fit: 0.37
  community_ordered:
  - Dominance
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Riptalon
  - Silverbranch Bow
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
    Underrated for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Lernaean Bow,
    The Crusher, Hydra''s Lament, Heartseeker, Golden Blade, Titan''s Bane, Demon
    Blade, Toxic Blade, Rage, Qin''s Blade, Arondight, Avatar''s Parashu, Bloodforge,
    Transcendence, Berserker''s Shield, Barbed Carver, Runeforged Hammer, Musashi''s
    Dual Swords, Pendulum Blade, Shield Splitter, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.19
      fit: 0.65
    The Reaper:
      total: 0.53
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.44
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.6
    Riptalon:
      total: 0.54
      efficiency: 0.45
      win: 0.6
      pick: 0.4
      fit: 0.62
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.49
      win: 0.64
      pick: 0.35
      fit: 0.52
  community_ordered:
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  starter: *id001
---
