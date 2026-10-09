---
type: smite-build
god: Artemis
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Wild
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.56
    win_rate: 0.62
    alternates:
    - name: Tyrfing
      pick_rate: 0.35
      win_rate: 0.48
    - name: Avenging Blade
      pick_rate: 0.04
      win_rate: 0.43
  - name: Dagger of Frenzy
    pick_rate: 0.36
    win_rate: 0.63
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.31
      win_rate: 0.59
    - name: Tyrfing
      pick_rate: 0.07
      win_rate: 0.54
  - name: Riptalon
    pick_rate: 0.17
    win_rate: 0.53
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.15
      win_rate: 0.5
    - name: Dominance
      pick_rate: 0.15
      win_rate: 0.65
  - name: Silverbranch Bow
    pick_rate: 0.23
    win_rate: 0.62
    alternates:
    - name: Riptalon
      pick_rate: 0.19
      win_rate: 0.58
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.62
  - name: The Executioner
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.47
    - name: Deathbringer
      pick_rate: 0.08
      win_rate: 0.77
  - name: Manchu Bow
    pick_rate: 0.13
    win_rate: 0.53
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.6
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.78
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.32
    win_rate: 0.59
  - name: Sharpshooter's Arrow
    pick_rate: 0.26
    win_rate: 0.66
  - name: Gilded Arrow
    pick_rate: 0.17
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/artemis/
  last_verified: '2026-10-09'
  god_win_rate: 0.5586592178770949
  god_matches_won: 100
  god_matches_played: 179
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-09'
  god_matches_analyzed: 2961
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, Demon Blade, The Reaper,
    Hydra''s Lament, Musashi''s Dual Swords, Heartseeker, Damaru, Rage, Titan''s Bane,
    The Crusher, Transcendence, Arondight, Runeforged Hammer, Golden Blade, Berserker''s
    Shield, Barbed Carver, Avatar''s Parashu, Bloodforge, Pendulum Blade, Vital Amplifier,
    Shield Splitter, Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.3
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.21
    Dominance:
      total: 0.55
      efficiency: 0.45
      win: 0.65
      pick: 0.23
      fit: 0.6
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.62
      pick: 0.0
      fit: 0.55
    Deathbringer:
      total: 0.61
      efficiency: 0.51
      win: 0.77
      pick: 0.17
      fit: 0.5
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
    Bane, The Crusher, Transcendence, Arondight, Musashi''s Dual Swords, Demon Blade,
    Runeforged Hammer, Pendulum Blade, Avatar''s Parashu, Damaru, Rage, Barbed Carver,
    Berserker''s Shield, Breastplate of Valor, Golden Blade, Genji''s Guard, Bloodforge,
    Daybreak Gavel, Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.42
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.65
      pick: 0.23
      fit: 0.5
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.77
      pick: 0.17
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
    this god: Jotunn''s Revenge, Lernaean Bow, Demon Blade, Tekko-Kagi, The Reaper,
    Musashi''s Dual Swords, Hydra''s Lament, Heartseeker, Damaru, Rage, Titan''s Bane,
    The Crusher, Transcendence, Arondight, Runeforged Hammer, Berserker''s Shield,
    Golden Blade, Barbed Carver, Avatar''s Parashu, Bloodforge, Pendulum Blade, Vital
    Amplifier, Daybreak Gavel, Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.28
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.65
      pick: 0.23
      fit: 0.55
    Musashi's Dual Swords:
      total: 0.52
      efficiency: 0.46
      win: 0.62
      pick: 0.0
      fit: 0.52
    Demon Blade:
      total: 0.53
      efficiency: 0.38
      win: 0.62
      pick: 0.0
      fit: 0.79
    Deathbringer:
      total: 0.61
      efficiency: 0.51
      win: 0.77
      pick: 0.17
      fit: 0.52
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
  - Shield of the Phoenix
  - Deathbringer
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, The Reaper, Kinetic Cuirass, Runeforged Hammer, Freya''s Tears, Genji''s
    Guard, Breastplate of Valor, Shifter''s Shield, Yogi''s Necklace, Shield Splitter,
    Pharaoh''s Curse, Lernaean Bow, Shogun''s Ofuda, Eye of the Storm, Phoenix Feather,
    Erosion, Eye of Providence, Draconic Scale, Chandra''s Grace, Hydra''s Lament,
    Daybreak Gavel, Stone of Binding, Midgardian Mail, Tekko-Kagi, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.19
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.47
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.58
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.77
      pick: 0.17
      fit: 0.32
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.67
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
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker, Titan''s
    Bane, The Crusher, Lernaean Bow, Hydra''s Lament, Avatar''s Parashu, Pendulum
    Blade, Demon Blade, Musashi''s Dual Swords, Oath-Sworn Spear, Transcendence, Runeforged
    Hammer, Arondight, Damaru, Rage, Toxic Blade, Berserker''s Shield, Golden Blade,
    Barbed Carver, Daybreak Gavel, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.5
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.15
    The Reaper:
      total: 0.55
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.55
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.62
      pick: 0.0
      fit: 0.68
    Deathbringer:
      total: 0.59
      efficiency: 0.51
      win: 0.77
      pick: 0.17
      fit: 0.36
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.62
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Dominance
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Lernaean Bow
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
    this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, Tekko-Kagi, The Reaper,
    Hydra''s Lament, Demon Blade, Qin''s Blade, Toxic Blade, Heartseeker, Musashi''s
    Dual Swords, Sun Beam Bow, Titan''s Bane, The Crusher, Transcendence, Damaru,
    Rage, Runeforged Hammer, Berserker''s Shield, Arondight, Barbed Carver, Vital
    Amplifier, Avatar''s Parashu, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.47
      win: 0.62
      pick: 0.0
      fit: 0.6
    Lernaean Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.52
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.22
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.65
      pick: 0.23
      fit: 0.52
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.62
      pick: 0.38
      fit: 0.5
    Deathbringer:
      total: 0.59
      efficiency: 0.51
      win: 0.77
      pick: 0.17
      fit: 0.38
  community_ordered:
  - Dominance
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Dominance
  - Arondight
  - Deathbringer
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
    Lernaean Bow, Arondight, The Reaper, Tekko-Kagi, Heartseeker, Pendulum Blade,
    Breastplate of Valor, Demon Blade, Musashi''s Dual Swords, Genji''s Guard, Titan''s
    Bane, The Crusher, Transcendence, Runeforged Hammer, Damaru, Berserker''s Shield,
    Rage, Daybreak Gavel, Eye of Erebus, Barbed Carver, Golden Blade, Avatar''s Parashu,
    Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.5
    Dominance:
      total: 0.52
      efficiency: 0.45
      win: 0.65
      pick: 0.23
      fit: 0.39
    Arondight:
      total: 0.51
      efficiency: 0.5
      win: 0.62
      pick: 0.0
      fit: 0.4
    Deathbringer:
      total: 0.58
      efficiency: 0.51
      win: 0.77
      pick: 0.17
      fit: 0.29
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
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Lernaean Bow, Tekko-Kagi, Demon Blade,
    The Reaper, Hydra''s Lament, Musashi''s Dual Swords, Heartseeker, Damaru, Rage,
    Titan''s Bane, The Crusher, Transcendence, Arondight, Runeforged Hammer, Golden
    Blade, Berserker''s Shield, Barbed Carver, Avenging Blade, Avatar''s Parashu,
    Bloodforge, Pendulum Blade, Vital Amplifier, Shield Splitter.'
  slot_scores:
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.3
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.37
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.62
      pick: 0.0
      fit: 0.55
    Demon Blade:
      total: 0.53
      efficiency: 0.38
      win: 0.62
      pick: 0.0
      fit: 0.79
    Deathbringer:
      total: 0.61
      efficiency: 0.51
      win: 0.77
      pick: 0.17
      fit: 0.5
  community_ordered:
  - Deathbringer
  starter: *id001
---
