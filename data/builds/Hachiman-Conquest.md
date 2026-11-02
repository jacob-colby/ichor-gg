---
type: smite-build
god: Hachiman
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Steel Wind
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.42
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.66
    win_rate: 0.49
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.37
    - name: Tyrfing
      pick_rate: 0.09
      win_rate: 0.49
  - name: Dagger of Frenzy
    pick_rate: 0.55
    win_rate: 0.46
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.49
    - name: Tyrfing
      pick_rate: 0.07
      win_rate: 0.48
  - name: Dominance
    pick_rate: 0.32
    win_rate: 0.47
    alternates:
    - name: The Executioner
      pick_rate: 0.15
      win_rate: 0.47
    - name: Odysseus' Bow
      pick_rate: 0.09
      win_rate: 0.57
  - name: Riptalon
    pick_rate: 0.25
    win_rate: 0.45
    alternates:
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.47
    - name: Dominance
      pick_rate: 0.12
      win_rate: 0.53
  - name: Deathbringer
    pick_rate: 0.19
    win_rate: 0.51
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.13
      win_rate: 0.53
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.49
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.58
    alternates:
    - name: Deathbringer
      pick_rate: 0.09
      win_rate: 0.58
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 0.55
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.44
    win_rate: 0.52
  - name: Gilded Arrow
    pick_rate: 0.2
    win_rate: 0.36
  - name: Hunter's Cowl
    pick_rate: 0.1
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/hachiman/
  last_verified: '2026-11-02'
  god_win_rate: 0.4666666666666667
  god_matches_won: 385
  god_matches_played: 825
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  - Tekko-Kagi
  - Deathbringer
  flex_slots:
  - Tyrfing
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
    this god: Jotunn''s Revenge, Tyrfing, Tekko-Kagi, The Reaper, Lernaean Bow, Heartseeker,
    Golden Blade, Demon Blade, Titan''s Bane, The Crusher, Toxic Blade, Musashi''s
    Dual Swords, Hydra''s Lament, Damaru, Rage, Avatar''s Parashu, Transcendence,
    Qin''s Blade, Runeforged Hammer, Barbed Carver, Avenging Blade, Berserker''s Shield,
    Sun Beam Bow, Bloodforge, Pendulum Blade, Vital Amplifier.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.59
      win: 0.49
      pick: 0.11
      fit: 0.38
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.48
      pick: 0.1
      fit: 0.66
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.53
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.45
      pick: 0.42
      fit: 0.64
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.64
    Deathbringer:
      total: 0.49
      efficiency: 0.51
      win: 0.51
      pick: 0.41
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
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
  - Transcendence
  - Hydra's Lament
  - Silverbranch Bow
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, Heartseeker, The Reaper, Lernaean Bow, Tyrfing, Tekko-Kagi,
    Titan''s Bane, The Crusher, Golden Blade, Transcendence, Arondight, Musashi''s
    Dual Swords, Runeforged Hammer, Pendulum Blade, Demon Blade, Avatar''s Parashu,
    Toxic Blade, Damaru, Rage, Avenging Blade, Qin''s Blade, Barbed Carver, Breastplate
    of Valor, Berserker''s Shield, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.49
      pick: 0.11
      fit: 0.46
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.49
      pick: 0.0
      fit: 0.25
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.49
      pick: 0.0
      fit: 0.44
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.32
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.51
      pick: 0.41
      fit: 0.33
    Heartseeker:
      total: 0.47
      efficiency: 0.47
      win: 0.49
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Jotunn's Revenge
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Silverbranch Bow
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
    this god: Jotunn''s Revenge, Tyrfing, Tekko-Kagi, Lernaean Bow, The Reaper, Heartseeker,
    Demon Blade, Golden Blade, Musashi''s Dual Swords, Titan''s Bane, The Crusher,
    Toxic Blade, Damaru, Rage, Hydra''s Lament, Qin''s Blade, Transcendence, Avatar''s
    Parashu, Runeforged Hammer, Berserker''s Shield, Avenging Blade, Sun Beam Bow,
    Barbed Carver, Bloodforge, Vital Amplifier.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.59
      win: 0.49
      pick: 0.11
      fit: 0.33
    Musashi's Dual Swords:
      total: 0.45
      efficiency: 0.46
      win: 0.49
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.51
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.45
      pick: 0.42
      fit: 0.61
    Demon Blade:
      total: 0.46
      efficiency: 0.38
      win: 0.49
      pick: 0.0
      fit: 0.73
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.51
      pick: 0.41
      fit: 0.48
  community_ordered:
  - Jotunn's Revenge
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Riptalon
  - Silverbranch Bow
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Reaper, Hydra''s Lament, Tekko-Kagi, Heartseeker,
    Lernaean Bow, Tyrfing, Titan''s Bane, The Crusher, Pendulum Blade, Golden Blade,
    Arondight, Toxic Blade, Avatar''s Parashu, Musashi''s Dual Swords, Transcendence,
    Runeforged Hammer, Demon Blade, Qin''s Blade, Damaru, Rage, Avenging Blade, Berserker''s
    Shield, Barbed Carver, Breastplate of Valor, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.49
      pick: 0.11
      fit: 0.48
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.49
      pick: 0.0
      fit: 0.14
    Hydra's Lament:
      total: 0.47
      efficiency: 0.54
      win: 0.49
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.48
      efficiency: 0.51
      win: 0.45
      pick: 0.42
      fit: 0.49
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.42
    Deathbringer:
      total: 0.47
      efficiency: 0.51
      win: 0.51
      pick: 0.41
      fit: 0.29
  community_ordered:
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Riptalon
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Silverbranch Bow
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
    this god: Amanita Charm, Berserker''s Shield, The Reaper, Kinetic Cuirass, Golden
    Blade, Runeforged Hammer, Shield of the Phoenix, Shifter''s Shield, Yogi''s Necklace,
    Jotunn''s Revenge, Shield Splitter, Pharaoh''s Curse, Lernaean Bow, Eye of the
    Storm, Tyrfing, Shogun''s Ofuda, Phoenix Feather, Erosion, Toxic Blade, Eye of
    Providence, Tekko-Kagi, Heartseeker, Draconic Scale, Daybreak Gavel, Avenging
    Blade, Stone of Binding, Midgardian Mail, Umbral Link.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.49
      pick: 0.0
      fit: 0.49
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.49
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.49
      pick: 0.0
      fit: 0.47
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.45
      pick: 0.42
      fit: 0.71
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Silverbranch Bow
  - Riptalon
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
    Bane, The Crusher, Tyrfing, Lernaean Bow, Toxic Blade, Avenging Blade, Avatar''s
    Parashu, Golden Blade, Demon Blade, Musashi''s Dual Swords, Hydra''s Lament, Oath-Sworn
    Spear, Transcendence, Pendulum Blade, Runeforged Hammer, Qin''s Blade, Damaru,
    Rage, Berserker''s Shield, Barbed Carver, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.59
      win: 0.49
      pick: 0.11
      fit: 0.51
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.49
      pick: 0.0
      fit: 0.16
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.63
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.45
      pick: 0.42
      fit: 0.72
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.72
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.49
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Jotunn's Revenge
  - Silverbranch Bow
  - Riptalon
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Lernaean Bow
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
    this god: Tyrfing, Lernaean Bow, Jotunn''s Revenge, Tekko-Kagi, Golden Blade,
    The Reaper, Toxic Blade, Heartseeker, Qin''s Blade, Demon Blade, Titan''s Bane,
    The Crusher, Musashi''s Dual Swords, Sun Beam Bow, Hydra''s Lament, Transcendence,
    Runeforged Hammer, Berserker''s Shield, Avatar''s Parashu, Damaru, Rage, Avenging
    Blade, Barbed Carver, Vital Amplifier, Daybreak Gavel.'
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.52
      win: 0.49
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.59
      win: 0.49
      pick: 0.11
      fit: 0.28
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.48
      pick: 0.1
      fit: 0.68
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.45
      pick: 0.42
      fit: 0.66
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.58
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.51
      pick: 0.41
      fit: 0.34
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Deathbringer
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
    Lernaean Bow, The Reaper, Arondight, Tyrfing, Tekko-Kagi, Heartseeker, Pendulum
    Blade, Golden Blade, Titan''s Bane, The Crusher, Breastplate of Valor, Toxic Blade,
    Genji''s Guard, Musashi''s Dual Swords, Transcendence, Demon Blade, Qin''s Blade,
    Runeforged Hammer, Avatar''s Parashu, Berserker''s Shield, Damaru, Rage, Avenging
    Blade, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.49
      pick: 0.11
      fit: 0.5
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.49
      pick: 0.0
      fit: 0.48
    Arondight:
      total: 0.45
      efficiency: 0.5
      win: 0.49
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.47
      efficiency: 0.51
      win: 0.45
      pick: 0.42
      fit: 0.43
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.35
    Deathbringer:
      total: 0.46
      efficiency: 0.51
      win: 0.51
      pick: 0.41
      fit: 0.25
  community_ordered:
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - Lernaean Bow
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
    Underrated for this god: Tyrfing, Tekko-Kagi, The Reaper, Lernaean Bow, Jotunn''s
    Revenge, Heartseeker, Golden Blade, Demon Blade, Titan''s Bane, The Crusher, Toxic
    Blade, Musashi''s Dual Swords, Hydra''s Lament, Damaru, Rage, Avatar''s Parashu,
    Transcendence, Qin''s Blade, Runeforged Hammer, Barbed Carver, Avenging Blade,
    Berserker''s Shield, Sun Beam Bow, Bloodforge, Pendulum Blade, Vital Amplifier.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.52
      win: 0.49
      pick: 0.0
      fit: 0.56
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.48
      pick: 0.1
      fit: 0.66
    The Reaper:
      total: 0.49
      efficiency: 0.55
      win: 0.49
      pick: 0.0
      fit: 0.49
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.45
      pick: 0.42
      fit: 0.64
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.53
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  starter: *id001
---
