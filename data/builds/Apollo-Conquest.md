---
type: smite-build
god: Apollo
mode: Conquest
builds:
- source: community
  aspect: Aspect of Harmony
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.75
  slot_order:
  - name: Tyrfing
    pick_rate: 0.75
    win_rate: 0.56
    alternates:
    - name: Avenging Blade
      pick_rate: 0.11
      win_rate: 0.57
    - name: Gauntlet of Thebes
      pick_rate: 0.06
      win_rate: 0.75
  - name: Odysseus' Bow
    pick_rate: 0.25
    win_rate: 0.63
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.2
      win_rate: 0.54
    - name: Dagger of Frenzy
      pick_rate: 0.13
      win_rate: 0.63
  - name: Silverbranch Bow
    pick_rate: 0.18
    win_rate: 0.82
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.15
      win_rate: 0.67
    - name: Odysseus' Bow
      pick_rate: 0.15
      win_rate: 0.67
  - name: Riptalon
    pick_rate: 0.16
    win_rate: 0.44
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.35
      win_rate: 0.6
    - name: Dominance
      pick_rate: 0.07
      win_rate: 0.25
  - name: The Executioner
    pick_rate: 0.19
    win_rate: 0.6
    alternates:
    - name: Riptalon
      pick_rate: 0.17
      win_rate: 0.67
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.17
  - name: Manchu Bow
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 1.0
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.67
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.38
    win_rate: 0.63
  - name: Leather Cowl
    pick_rate: 0.23
    win_rate: 0.27
  - name: Death's Embrace
    pick_rate: 0.11
    win_rate: 0.71
  source_url: https://smitebrain.com/gods/apollo/
  last_verified: '2026-09-10'
  god_win_rate: 0.5625
  god_matches_won: 36
  god_matches_played: 64
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Jotunn's Revenge
  - Silverbranch Bow
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, Tekko-Kagi, Demon Blade,
    Deathbringer, The Reaper, Hydra''s Lament, Musashi''s Dual Swords, Heartseeker,
    Damaru, Rage, Toxic Blade, Qin''s Blade, Titan''s Bane, The Crusher, Transcendence,
    Arondight, Runeforged Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver,
    Avatar''s Parashu, Bloodforge, Pendulum Blade, Avenging Blade, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.6
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.56
      pick: 0.75
      fit: 0.7
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.3
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.82
      pick: 0.28
      fit: 0.45
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Transcendence
  - Silverbranch Bow
  - Hydra's Lament
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
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Deathbringer,
    Titan''s Bane, Golden Blade, The Crusher, Transcendence, Arondight, Musashi''s
    Dual Swords, Demon Blade, Runeforged Hammer, Pendulum Blade, Toxic Blade, Avatar''s
    Parashu, Damaru, Rage, Qin''s Blade, Barbed Carver, Berserker''s Shield, Breastplate
    of Valor, Genji''s Guard, Avenging Blade, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.56
      pick: 0.75
      fit: 0.49
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.24
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.82
      pick: 0.28
      fit: 0.33
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Musashi's Dual Swords
  - Silverbranch Bow
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
    Tekko-Kagi, The Reaper, Musashi''s Dual Swords, Hydra''s Lament, Heartseeker,
    Damaru, Rage, Toxic Blade, Qin''s Blade, Titan''s Bane, The Crusher, Transcendence,
    Arondight, Runeforged Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver,
    Avatar''s Parashu, Bloodforge, Pendulum Blade, Avenging Blade, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.28
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.56
      pick: 0.75
      fit: 0.66
    Musashi's Dual Swords:
      total: 0.52
      efficiency: 0.46
      win: 0.61
      pick: 0.0
      fit: 0.52
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.82
      pick: 0.28
      fit: 0.43
    Demon Blade:
      total: 0.53
      efficiency: 0.38
      win: 0.61
      pick: 0.0
      fit: 0.79
    Deathbringer:
      total: 0.53
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Silverbranch Bow
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, The Reaper, Kinetic Cuirass, Golden Blade, Runeforged Hammer, Freya''s
    Tears, Genji''s Guard, Breastplate of Valor, Shifter''s Shield, Yogi''s Necklace,
    Shield Splitter, Pharaoh''s Curse, Lernaean Bow, Shogun''s Ofuda, Eye of the Storm,
    Phoenix Feather, Erosion, Eye of Providence, Draconic Scale, Chandra''s Grace,
    Hydra''s Lament, Daybreak Gavel, Stone of Binding, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.19
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.47
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.82
      pick: 0.28
      fit: 0.28
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Silverbranch Bow
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
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker, Titan''s
    Bane, The Crusher, Lernaean Bow, Toxic Blade, Hydra''s Lament, Deathbringer, Avatar''s
    Parashu, Golden Blade, Pendulum Blade, Avenging Blade, Demon Blade, Musashi''s
    Dual Swords, Oath-Sworn Spear, Transcendence, Runeforged Hammer, Qin''s Blade,
    Arondight, Damaru, Rage, Berserker''s Shield, Barbed Carver, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.5
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.15
    The Reaper:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.55
    Silverbranch Bow:
      total: 0.66
      efficiency: 0.53
      win: 0.82
      pick: 0.28
      fit: 0.61
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.68
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Jotunn's Revenge
  - Silverbranch Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, Tekko-Kagi, Deathbringer,
    The Reaper, Hydra''s Lament, Demon Blade, Qin''s Blade, Toxic Blade, Heartseeker,
    Musashi''s Dual Swords, Sun Beam Bow, Titan''s Bane, The Crusher, Transcendence,
    Damaru, Rage, Runeforged Hammer, Berserker''s Shield, Arondight, Barbed Carver,
    Vital Amplifier, Avatar''s Parashu, Avenging Blade, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.6
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.56
      pick: 0.75
      fit: 0.7
    Lernaean Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.52
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.22
    Silverbranch Bow:
      total: 0.64
      efficiency: 0.53
      win: 0.82
      pick: 0.28
      fit: 0.5
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - Jotunn's Revenge
  - Silverbranch Bow
  - Hydra's Lament
  - Arondight
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
    Lernaean Bow, Arondight, The Reaper, Deathbringer, Tekko-Kagi, Golden Blade, Heartseeker,
    Pendulum Blade, Breastplate of Valor, Demon Blade, Musashi''s Dual Swords, Genji''s
    Guard, Qin''s Blade, Titan''s Bane, The Crusher, Toxic Blade, Transcendence, Runeforged
    Hammer, Damaru, Berserker''s Shield, Rage, Sun Beam Bow, Daybreak Gavel, Avenging
    Blade, Dominance.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.56
      pick: 0.75
      fit: 0.46
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.43
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.82
      pick: 0.28
      fit: 0.31
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.5
    Arondight:
      total: 0.51
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
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
    Dual Swords, Heartseeker, Damaru, Rage, Toxic Blade, Qin''s Blade, Titan''s Bane,
    The Crusher, Transcendence, Arondight, Runeforged Hammer, Berserker''s Shield,
    Sun Beam Bow, Barbed Carver, Avenging Blade, Avatar''s Parashu, Bloodforge, Pendulum
    Blade.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.6
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.56
      pick: 0.75
      fit: 0.7
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.3
    Riptalon:
      total: 0.47
      efficiency: 0.51
      win: 0.44
      pick: 0.27
      fit: 0.56
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Riptalon
  starter: *id001
---
