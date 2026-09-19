---
type: smite-build
god: Jing Wei
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Tyrfing
    pick_rate: 0.33
    win_rate: 0.32
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.31
      win_rate: 0.47
    - name: Avenging Blade
      pick_rate: 0.24
      win_rate: 0.62
  - name: Dagger of Frenzy
    pick_rate: 0.51
    win_rate: 0.48
    alternates:
    - name: Dominance
      pick_rate: 0.09
      win_rate: 0.46
    - name: Odysseus' Bow
      pick_rate: 0.09
      win_rate: 0.15
  - name: Musashi's Dual Swords
    pick_rate: 0.25
    win_rate: 0.43
    alternates:
    - name: Deathbringer
      pick_rate: 0.13
      win_rate: 0.53
    - name: Dominance
      pick_rate: 0.1
      win_rate: 0.64
  - name: Deathbringer
    pick_rate: 0.31
    win_rate: 0.43
    alternates:
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.47
    - name: Dominance
      pick_rate: 0.11
      win_rate: 0.53
  - name: Riptalon
    pick_rate: 0.19
    win_rate: 0.68
    alternates:
    - name: Deathbringer
      pick_rate: 0.18
      win_rate: 0.52
    - name: Dominance
      pick_rate: 0.11
      win_rate: 0.2
  - name: Bow
    pick_rate: 0.09
    win_rate: 0.56
    alternates:
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.55
    - name: Manchu Bow
      pick_rate: 0.09
      win_rate: 0.56
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.59
    win_rate: 0.48
  - name: Gilded Arrow
    pick_rate: 0.22
    win_rate: 0.39
  - name: Hunter's Cowl
    pick_rate: 0.1
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/jing-wei/
  last_verified: '2026-09-19'
  god_win_rate: 0.4375
  god_matches_won: 63
  god_matches_played: 144
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-19'
  god_matches_analyzed: 12806
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Avenging Blade
  - Deathbringer
  - Demon Blade
  - Riptalon
  flex_slots:
  - Demon Blade
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Demon Blade, Golden Blade, Damaru, Rage, Qin''s Blade,
    Tekko-Kagi, Jotunn''s Revenge, Hydra''s Lament, Transcendence, Silverbranch Bow,
    The Reaper, Berserker''s Shield, Runeforged Hammer, Sun Beam Bow, Barbed Carver,
    Vital Amplifier, Bloodforge, Toxic Blade, The Executioner, Heartseeker, Shield
    Splitter, Odysseus'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.47
      win: 0.47
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.49
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.64
    Avenging Blade:
      total: 0.49
      efficiency: 0.44
      win: 0.62
      pick: 0.24
      fit: 0.31
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.43
      pick: 0.52
      fit: 0.54
    Demon Blade:
      total: 0.48
      efficiency: 0.38
      win: 0.47
      pick: 0.0
      fit: 0.87
    Riptalon:
      total: 0.55
      efficiency: 0.41
      win: 0.68
      pick: 0.41
      fit: 0.57
  community_ordered:
  - Avenging Blade
  - Deathbringer
  - Riptalon
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Riptalon
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
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Silverbranch
    Bow, Titan''s Bane, Golden Blade, The Crusher, Transcendence, Arondight, Demon
    Blade, Runeforged Hammer, Pendulum Blade, Toxic Blade, Avatar''s Parashu, Damaru,
    Rage, Qin''s Blade, Barbed Carver, Berserker''s Shield, Breastplate of Valor,
    Genji''s Guard.'
  slot_scores:
    Avenging Blade:
      total: 0.49
      efficiency: 0.44
      win: 0.62
      pick: 0.24
      fit: 0.28
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.47
      efficiency: 0.54
      win: 0.47
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.68
      pick: 0.41
      fit: 0.39
    Heartseeker:
      total: 0.46
      efficiency: 0.47
      win: 0.47
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Avenging Blade
  - Riptalon
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Avenging Blade
  - Musashi's Dual Swords
  - Deathbringer
  - Demon Blade
  - Riptalon
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
    this god: Lernaean Bow, Demon Blade, Golden Blade, Damaru, Rage, Qin''s Blade,
    Jotunn''s Revenge, Hydra''s Lament, Tekko-Kagi, Transcendence, The Reaper, Runeforged
    Hammer, Silverbranch Bow, Berserker''s Shield, Sun Beam Bow, Barbed Carver, Bloodforge,
    Vital Amplifier, Heartseeker, Toxic Blade, The Executioner, Shield Splitter, The
    Crusher.'
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.6
    Avenging Blade:
      total: 0.49
      efficiency: 0.44
      win: 0.62
      pick: 0.24
      fit: 0.3
    Musashi's Dual Swords:
      total: 0.46
      efficiency: 0.46
      win: 0.43
      pick: 0.39
      fit: 0.57
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.43
      pick: 0.52
      fit: 0.57
    Demon Blade:
      total: 0.48
      efficiency: 0.38
      win: 0.47
      pick: 0.0
      fit: 0.88
    Riptalon:
      total: 0.55
      efficiency: 0.41
      win: 0.68
      pick: 0.41
      fit: 0.53
  community_ordered:
  - Avenging Blade
  - Musashi's Dual Swords
  - Deathbringer
  - Riptalon
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Avenging Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Golden Blade, Runeforged
    Hammer, Shield of the Phoenix, Shifter''s Shield, Pharaoh''s Curse, Yogi''s Necklace,
    Shield Splitter, Shogun''s Ofuda, Lernaean Bow, Eye of the Storm, Phoenix Feather,
    Erosion, The Reaper, Eye of Providence, Draconic Scale, Daybreak Gavel, Stone
    of Binding, Midgardian Mail, Umbral Link, Magi''s Cloak, Hide of the Nemean Lion,
    Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.54
    Avenging Blade:
      total: 0.52
      efficiency: 0.49
      win: 0.62
      pick: 0.24
      fit: 0.38
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.5
    Riptalon:
      total: 0.56
      efficiency: 0.41
      win: 0.68
      pick: 0.41
      fit: 0.64
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Avenging Blade
  - Riptalon
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Silverbranch Bow
  - Tekko-Kagi
  - Riptalon
  - Heartseeker
  flex_slots:
  - Tekko-Kagi
  - Heartseeker
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Silverbranch Bow, Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker,
    Titan''s Bane, The Crusher, Lernaean Bow, Toxic Blade, Avatar''s Parashu, Golden
    Blade, Demon Blade, The Executioner, Hydra''s Lament, Oath-Sworn Spear, Transcendence,
    Qin''s Blade, Damaru, Runeforged Hammer, Rage, Pendulum Blade, Berserker''s Shield,
    Sun Beam Bow, Barbed Carver.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.44
      win: 0.62
      pick: 0.24
      fit: 0.54
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.47
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.63
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.47
      pick: 0.0
      fit: 0.69
    Riptalon:
      total: 0.61
      efficiency: 0.51
      win: 0.68
      pick: 0.41
      fit: 0.72
    Heartseeker:
      total: 0.48
      efficiency: 0.47
      win: 0.47
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Avenging Blade
  - Riptalon
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Avenging Blade
  - Dagger of Frenzy
  - Deathbringer
  - Riptalon
  flex_slots:
  - Deathbringer
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Golden Blade, Demon Blade, Qin''s Blade, Silverbranch
    Bow, Sun Beam Bow, Jotunn''s Revenge, Hydra''s Lament, Damaru, Tekko-Kagi, Rage,
    Transcendence, Berserker''s Shield, Runeforged Hammer, The Reaper, Toxic Blade,
    Barbed Carver, Vital Amplifier, Hastened Fatalis, Bloodforge, The Executioner,
    Heartseeker, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.47
      win: 0.47
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.47
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.55
    Avenging Blade:
      total: 0.48
      efficiency: 0.44
      win: 0.62
      pick: 0.24
      fit: 0.26
    Dagger of Frenzy:
      total: 0.45
      efficiency: 0.37
      win: 0.48
      pick: 0.7
      fit: 0.49
    Deathbringer:
      total: 0.46
      efficiency: 0.51
      win: 0.43
      pick: 0.52
      fit: 0.41
    Riptalon:
      total: 0.56
      efficiency: 0.41
      win: 0.68
      pick: 0.41
      fit: 0.59
  community_ordered:
  - Avenging Blade
  - Dagger of Frenzy
  - Deathbringer
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
  - Lernaean Bow
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
    Lernaean Bow, Arondight, Golden Blade, Breastplate of Valor, Demon Blade, Genji''s
    Guard, Qin''s Blade, Transcendence, Runeforged Hammer, Damaru, Rage, Berserker''s
    Shield, The Reaper, Silverbranch Bow, Tekko-Kagi, Sun Beam Bow, Eye of Erebus,
    Daybreak Gavel, Barbed Carver, Vital Amplifier, Screeching Gargoyle, Chandra''s
    Grace.'
  slot_scores:
    Lernaean Bow:
      total: 0.45
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.4
    Avenging Blade:
      total: 0.47
      efficiency: 0.44
      win: 0.62
      pick: 0.24
      fit: 0.2
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.67
      win: 0.47
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.47
      pick: 0.0
      fit: 0.51
    Arondight:
      total: 0.45
      efficiency: 0.5
      win: 0.47
      pick: 0.0
      fit: 0.41
    Riptalon:
      total: 0.52
      efficiency: 0.41
      win: 0.68
      pick: 0.41
      fit: 0.35
  community_ordered:
  - Avenging Blade
  - Riptalon
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Dominance
  - Deathbringer
  - Demon Blade
  flex_slots:
  - Deathbringer
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Lernaean Bow, Demon Blade, Golden Blade, Damaru, Rage,
    Qin''s Blade, Tekko-Kagi, Jotunn''s Revenge, Hydra''s Lament, Transcendence, Silverbranch
    Bow, The Reaper, Berserker''s Shield, Runeforged Hammer, Sun Beam Bow, Barbed
    Carver, Vital Amplifier, Bloodforge, Toxic Blade, The Executioner, Heartseeker,
    Odysseus'' Bow, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.47
      win: 0.47
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.49
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.44
      efficiency: 0.48
      win: 0.32
      pick: 0.33
      fit: 0.75
    Dominance:
      total: 0.35
      efficiency: 0.45
      win: 0.2
      pick: 0.24
      fit: 0.64
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.43
      pick: 0.52
      fit: 0.54
    Demon Blade:
      total: 0.48
      efficiency: 0.38
      win: 0.47
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Tyrfing
  - Dominance
  - Deathbringer
  starter: *id001
---
