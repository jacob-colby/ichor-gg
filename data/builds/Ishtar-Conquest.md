---
type: smite-build
god: Ishtar
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Passionate Storm
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.43
  slot_order:
  - name: Tyrfing
    pick_rate: 0.87
    win_rate: 0.7
    alternates:
    - name: Avenging Blade
      pick_rate: 0.09
      win_rate: 0.5
    - name: Lernaean Bow
      pick_rate: 0.02
      win_rate: 0.0
  - name: Odysseus' Bow
    pick_rate: 0.37
    win_rate: 0.71
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.22
      win_rate: 0.6
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.83
  - name: The Executioner
    pick_rate: 0.22
    win_rate: 0.8
    alternates:
    - name: Riptalon
      pick_rate: 0.17
      win_rate: 0.38
    - name: Hastened Fatalis
      pick_rate: 0.17
      win_rate: 1.0
  - name: Silverbranch Bow
    pick_rate: 0.36
    win_rate: 0.94
    alternates:
    - name: The Executioner
      pick_rate: 0.22
      win_rate: 0.6
    - name: Riptalon
      pick_rate: 0.16
      win_rate: 0.57
  - name: Riptalon
    pick_rate: 0.16
    win_rate: 1.0
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.3
      win_rate: 0.69
    - name: The Executioner
      pick_rate: 0.09
      win_rate: 0.5
  - name: Hunter's Bow
    pick_rate: 0.17
    win_rate: 0.67
    alternates:
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.8
    - name: Qin's Blade
      pick_rate: 0.09
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.39
    win_rate: 0.72
  - name: Sharpshooter's Arrow
    pick_rate: 0.3
    win_rate: 0.64
  - name: Gilded Arrow
    pick_rate: 0.11
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/ishtar/
  last_verified: '2026-09-09'
  god_win_rate: 0.6521739130434783
  god_matches_won: 30
  god_matches_played: 46
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
  - Golden Blade
  - Tyrfing
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  - Demon Blade
  flex_slots:
  - Golden Blade
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Demon Blade, Deathbringer, Dominance, Musashi''s Dual
    Swords, Damaru, Rage, Jotunn''s Revenge, Tekko-Kagi, Hydra''s Lament, Transcendence,
    The Reaper, Runeforged Hammer, Sun Beam Bow, Barbed Carver, Berserker''s Shield,
    Bloodforge, Dagger of Frenzy, Toxic Blade, Vital Amplifier, Heartseeker, Shield
    Splitter, The Crusher, Avenging Blade, Lernaean Bow.'
  slot_scores:
    Golden Blade:
      total: 0.59
      efficiency: 0.47
      win: 0.7
      pick: 0.0
      fit: 0.72
    Tyrfing:
      total: 0.65
      efficiency: 0.48
      win: 0.7
      pick: 0.87
      fit: 0.82
    Riptalon:
      total: 0.7
      efficiency: 0.41
      win: 1.0
      pick: 0.35
      fit: 0.61
    Qin's Blade:
      total: 0.7
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.68
    Silverbranch Bow:
      total: 0.67
      efficiency: 0.42
      win: 0.94
      pick: 0.6
      fit: 0.48
    Demon Blade:
      total: 0.58
      efficiency: 0.38
      win: 0.7
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Tyrfing
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, Heartseeker, The Reaper, Tekko-Kagi, Dominance, Deathbringer,
    Golden Blade, Titan''s Bane, The Crusher, Transcendence, Arondight, Musashi''s
    Dual Swords, Runeforged Hammer, Demon Blade, Pendulum Blade, Toxic Blade, Avatar''s
    Parashu, Damaru, Rage, Barbed Carver, Breastplate of Valor, Berserker''s Shield,
    Genji''s Guard, Avenging Blade, Lernaean Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.7
      pick: 0.0
      fit: 0.45
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.7
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.35
      fit: 0.41
    Qin's Blade:
      total: 0.66
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.43
    Silverbranch Bow:
      total: 0.69
      efficiency: 0.53
      win: 0.94
      pick: 0.6
      fit: 0.35
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.7
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Musashi's Dual Swords
  - Qin's Blade
  - Riptalon
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
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
    this god: Demon Blade, Deathbringer, Golden Blade, Musashi''s Dual Swords, Dominance,
    Damaru, Rage, Jotunn''s Revenge, Hydra''s Lament, Tekko-Kagi, Transcendence, The
    Reaper, Runeforged Hammer, Sun Beam Bow, Berserker''s Shield, Barbed Carver, Dagger
    of Frenzy, Bloodforge, Vital Amplifier, Toxic Blade, Heartseeker, Shield Splitter,
    The Crusher, Avenging Blade, Lernaean Bow.'
  slot_scores:
    Musashi's Dual Swords:
      total: 0.57
      efficiency: 0.46
      win: 0.7
      pick: 0.0
      fit: 0.57
    Qin's Blade:
      total: 0.69
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.65
    Riptalon:
      total: 0.7
      efficiency: 0.41
      win: 1.0
      pick: 0.35
      fit: 0.58
    Silverbranch Bow:
      total: 0.67
      efficiency: 0.42
      win: 0.94
      pick: 0.6
      fit: 0.45
    Demon Blade:
      total: 0.58
      efficiency: 0.38
      win: 0.7
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.7
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Qin's Blade
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Tyrfing
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
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Golden Blade, Runeforged
    Hammer, Shield of the Phoenix, Shifter''s Shield, Shield Splitter, Yogi''s Necklace,
    Pharaoh''s Curse, Eye of the Storm, Shogun''s Ofuda, The Reaper, Erosion, Phoenix
    Feather, Eye of Providence, Draconic Scale, Daybreak Gavel, Stone of Binding,
    Midgardian Mail, Deathbringer, Umbral Link, Magi''s Cloak, Hide of the Nemean
    Lion, Bloodforge, Leviathan''s Hide, Avenging Blade, Lernaean Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.61
      efficiency: 0.48
      win: 0.7
      pick: 0.87
      fit: 0.53
    Riptalon:
      total: 0.71
      efficiency: 0.41
      win: 1.0
      pick: 0.35
      fit: 0.66
    Qin's Blade:
      total: 0.67
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.48
    Silverbranch Bow:
      total: 0.64
      efficiency: 0.42
      win: 0.94
      pick: 0.6
      fit: 0.28
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.7
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Tyrfing
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker, Titan''s
    Bane, The Crusher, Toxic Blade, Golden Blade, Avatar''s Parashu, Deathbringer,
    Dominance, Demon Blade, Musashi''s Dual Swords, Hydra''s Lament, Oath-Sworn Spear,
    Transcendence, Pendulum Blade, Runeforged Hammer, Damaru, Rage, Berserker''s Shield,
    Barbed Carver, Sun Beam Bow, Avenging Blade, Lernaean Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.59
      win: 0.7
      pick: 0.0
      fit: 0.51
    Tyrfing:
      total: 0.61
      efficiency: 0.48
      win: 0.7
      pick: 0.87
      fit: 0.57
    Riptalon:
      total: 0.76
      efficiency: 0.51
      win: 1.0
      pick: 0.35
      fit: 0.75
    Qin's Blade:
      total: 0.67
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.51
    Silverbranch Bow:
      total: 0.74
      efficiency: 0.53
      win: 0.94
      pick: 0.6
      fit: 0.66
    Tekko-Kagi:
      total: 0.59
      efficiency: 0.49
      win: 0.7
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Tyrfing
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Executioner
  - Qin's Blade
  flex_slots:
  - Golden Blade
  - The Executioner
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
    this god: Golden Blade, Dominance, Demon Blade, Deathbringer, Musashi''s Dual
    Swords, Sun Beam Bow, Jotunn''s Revenge, Tekko-Kagi, Hydra''s Lament, Transcendence,
    Damaru, Berserker''s Shield, Rage, Runeforged Hammer, Dagger of Frenzy, The Reaper,
    Toxic Blade, Barbed Carver, Vital Amplifier, Bloodforge, Heartseeker, Daybreak
    Gavel, Avenging Blade, Lernaean Bow.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.47
      win: 0.7
      pick: 0.0
      fit: 0.67
    Tyrfing:
      total: 0.64
      efficiency: 0.48
      win: 0.7
      pick: 0.87
      fit: 0.77
    Riptalon:
      total: 0.7
      efficiency: 0.41
      win: 1.0
      pick: 0.35
      fit: 0.6
    Silverbranch Bow:
      total: 0.68
      efficiency: 0.42
      win: 0.94
      pick: 0.6
      fit: 0.5
    The Executioner:
      total: 0.56
      efficiency: 0.35
      win: 0.8
      pick: 0.34
      fit: 0.4
    Qin's Blade:
      total: 0.7
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.7
  community_ordered:
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Executioner
  - Qin's Blade
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Riptalon
  - Qin's Blade
  - Arondight
  - Silverbranch Bow
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
    Arondight, Golden Blade, Deathbringer, Dominance, Breastplate of Valor, Genji''s
    Guard, Demon Blade, Musashi''s Dual Swords, Transcendence, Runeforged Hammer,
    Damaru, Rage, Berserker''s Shield, The Reaper, Sun Beam Bow, Tekko-Kagi, Eye of
    Erebus, Barbed Carver, Daybreak Gavel, Screeching Gargoyle, Chandra''s Grace,
    Vital Amplifier, Avenging Blade, Lernaean Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.67
      win: 0.7
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.7
      pick: 0.0
      fit: 0.53
    Riptalon:
      total: 0.67
      efficiency: 0.41
      win: 1.0
      pick: 0.35
      fit: 0.38
    Qin's Blade:
      total: 0.67
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.5
    Arondight:
      total: 0.56
      efficiency: 0.5
      win: 0.7
      pick: 0.0
      fit: 0.43
    Silverbranch Bow:
      total: 0.65
      efficiency: 0.42
      win: 0.94
      pick: 0.6
      fit: 0.3
  community_ordered:
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Dominance
  - Demon Blade
  - Deathbringer
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
    Underrated for this god: Lernaean Bow, Golden Blade, Demon Blade, Deathbringer,
    Dominance, Musashi''s Dual Swords, Damaru, Rage, Jotunn''s Revenge, Tekko-Kagi,
    Hydra''s Lament, Transcendence, The Reaper, Runeforged Hammer, Sun Beam Bow, Barbed
    Carver, Berserker''s Shield, Avenging Blade, Bloodforge, Dagger of Frenzy, Toxic
    Blade, Vital Amplifier, Heartseeker, Shield Splitter, The Crusher.'
  slot_scores:
    Golden Blade:
      total: 0.59
      efficiency: 0.47
      win: 0.7
      pick: 0.0
      fit: 0.72
    Tyrfing:
      total: 0.65
      efficiency: 0.48
      win: 0.7
      pick: 0.87
      fit: 0.82
    Lernaean Bow:
      total: 0.28
      efficiency: 0.52
      win: 0.0
      pick: 0.02
      fit: 0.66
    Dominance:
      total: 0.57
      efficiency: 0.45
      win: 0.7
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.58
      efficiency: 0.38
      win: 0.7
      pick: 0.0
      fit: 0.87
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.7
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Lernaean Bow
  starter: *id001
---
