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
  - name: Devourer's Gauntlet
    pick_rate: 0.87
    win_rate: 0.23
    alternates:
    - name: Deathbringer
      pick_rate: 0.07
      win_rate: 1.0
    - name: Qin's Blade
      pick_rate: 0.07
      win_rate: 0.0
  - name: Dagger of Frenzy
    pick_rate: 0.6
    win_rate: 0.22
    alternates:
    - name: Tyrfing
      pick_rate: 0.13
      win_rate: 0.0
    - name: Demon Blade
      pick_rate: 0.13
      win_rate: 1.0
  - name: Riptalon
    pick_rate: 0.21
    win_rate: 0.33
    alternates:
    - name: Dominance
      pick_rate: 0.21
      win_rate: 0.0
    - name: Hydra's Lament
      pick_rate: 0.14
      win_rate: 0.5
  - name: Dominance
    pick_rate: 0.29
    win_rate: 0.5
    alternates:
    - name: Deathbringer
      pick_rate: 0.14
      win_rate: 0.0
    - name: Silverbranch Bow
      pick_rate: 0.14
      win_rate: 0.0
  - name: Deathbringer
    pick_rate: 0.21
    win_rate: 1.0
    alternates:
    - name: Bow
      pick_rate: 0.14
      win_rate: 0.0
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.5
  - name: Musashi's Dual Swords
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Dominance
      pick_rate: 0.17
      win_rate: 0.5
    - name: The Executioner
      pick_rate: 0.17
      win_rate: 0.0
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.73
    win_rate: 0.36
  - name: Gilded Arrow
    pick_rate: 0.27
    win_rate: 0.0
  community_relics:
  - name: Purification Beads
    pick_rate: 0.6
    win_rate: 0.22
  - name: Aegis of Acceleration
    pick_rate: 0.4
    win_rate: 0.33
  starter_sightings:
  - name: Sharpshooter's Arrow
    pick_rate: 0.73
    win_rate: 0.36
  - name: Gilded Arrow
    pick_rate: 0.27
    win_rate: 0.0
  relic_sightings:
  - name: Purification Beads
    pick_rate: 0.6
    win_rate: 0.22
  - name: Aegis of Acceleration
    pick_rate: 0.4
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/jing-wei/
  last_verified: '2026-11-19'
  god_win_rate: 0.26666666666666666
  god_matches_won: 4
  god_matches_played: 15
  god_division: obsidian
  god_window_start: '2026-11-17'
  god_window_end: '2026-11-19'
  god_matches_analyzed: 1578
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
    pick_rate: 1.0
    win_rate: 0.2628
    matches: 15
    basis: community
  relic:
    name: Purification Beads
    pick_rate: 0.6
    win_rate: 0.22
    matches: 9
    basis: community
- source: suggested
  archetype: core
  slot_order:
  - Hydra's Lament
  - Riptalon
  - Demon Blade
  - Dominance
  - Musashi's Dual Swords
  - Deathbringer
  flex_slots:
  - Hydra's Lament
  - Riptalon
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
    this god: Lernaean Bow, Golden Blade, Rage, Tekko-Kagi, The Reaper, Berserker''s
    Shield, Bloodforge, Barbed Carver, Transcendence, Runeforged Hammer, Odysseus''
    Bow, Jotunn''s Revenge, Sun Beam Bow, The Crusher, Shield Splitter, Eye of the
    Storm, Avenging Blade, Toxic Blade, Heartseeker, Qin''s Blade.'
  slot_scores:
    Hydra's Lament:
      total: 0.45
      efficiency: 0.5
      win: 0.5
      pick: 0.22
      fit: 0.31
    Riptalon:
      total: 0.38
      efficiency: 0.36
      win: 0.33
      pick: 0.33
      fit: 0.57
    Demon Blade:
      total: 0.72
      efficiency: 0.36
      win: 1.0
      pick: 0.18
      fit: 0.87
    Dominance:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.48
      fit: 0.64
    Musashi's Dual Swords:
      total: 0.46
      efficiency: 0.38
      win: 0.5
      pick: 0.52
      fit: 0.54
    Deathbringer:
      total: 0.71
      efficiency: 0.44
      win: 1.0
      pick: 0.45
      fit: 0.54
  community_ordered:
  - Hydra's Lament
  - Riptalon
  - Demon Blade
  - Dominance
  - Musashi's Dual Swords
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
    pick_rate: 1.0
    win_rate: 0.2628
    matches: 15
    basis: community
  relic: &id002
    name: Purification Beads
    pick_rate: 0.6
    win_rate: 0.22
    matches: 9
    basis: community
- source: suggested
  archetype: mana-stack
  slot_order:
  - Transcendence
  - Hydra's Lament
  - Demon Blade
  - Dominance
  - Deathbringer
  - Musashi's Dual Swords
  flex_slots:
  - Musashi's Dual Swords
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
    Revenge, The Reaper, Heartseeker, Tekko-Kagi, The Crusher, Lernaean Bow, Titan''s
    Bane, Arondight, Golden Blade, Rage, Transcendence, Avatar''s Parashu, Toxic Blade,
    Genji''s Guard, Runeforged Hammer, Bloodforge, Barbed Carver, Pendulum Blade,
    Damaru, Shield Splitter, Eye of the Storm, Avenging Blade, Qin''s Blade.'
  slot_scores:
    Transcendence:
      total: 0.31
      efficiency: 0.5
      win: 0.23
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.22
      fit: 0.42
    Demon Blade:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.18
      fit: 0.5
    Dominance:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.48
      fit: 0.5
    Deathbringer:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.45
      fit: 0.34
    Musashi's Dual Swords:
      total: 0.43
      efficiency: 0.38
      win: 0.5
      pick: 0.52
      fit: 0.34
  community_ordered:
  - Hydra's Lament
  - Demon Blade
  - Dominance
  - Deathbringer
  - Musashi's Dual Swords
  starter: *id001
  relic: *id002
- source: suggested
  archetype: crit
  slot_order:
  - Hydra's Lament
  - Riptalon
  - Demon Blade
  - Dominance
  - Musashi's Dual Swords
  - Deathbringer
  flex_slots:
  - Hydra's Lament
  - Riptalon
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
    this god: Lernaean Bow, Golden Blade, Rage, The Reaper, Tekko-Kagi, Bloodforge,
    Berserker''s Shield, Barbed Carver, Transcendence, Runeforged Hammer, Jotunn''s
    Revenge, The Crusher, Odysseus'' Bow, Shield Splitter, Eye of the Storm, Sun Beam
    Bow, Avenging Blade, Heartseeker, Arondight, Qin''s Blade.'
  slot_scores:
    Hydra's Lament:
      total: 0.45
      efficiency: 0.5
      win: 0.5
      pick: 0.22
      fit: 0.3
    Riptalon:
      total: 0.37
      efficiency: 0.36
      win: 0.33
      pick: 0.33
      fit: 0.53
    Demon Blade:
      total: 0.72
      efficiency: 0.36
      win: 1.0
      pick: 0.18
      fit: 0.88
    Dominance:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.48
      fit: 0.6
    Musashi's Dual Swords:
      total: 0.47
      efficiency: 0.38
      win: 0.5
      pick: 0.52
      fit: 0.57
    Deathbringer:
      total: 0.71
      efficiency: 0.44
      win: 1.0
      pick: 0.45
      fit: 0.57
  community_ordered:
  - Hydra's Lament
  - Riptalon
  - Demon Blade
  - Dominance
  - Musashi's Dual Swords
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - Hydra's Lament
  - Demon Blade
  - Deathbringer
  - Dominance
  - Musashi's Dual Swords
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Shield of the Phoenix,
    Phoenix Feather, Yogi''s Necklace, Golden Blade, Shield Splitter, Oni Hunter''s
    Garb, Runeforged Hammer, Draconic Scale, The Reaper, Shogun''s Ofuda, Pharaoh''s
    Curse, Erosion, Genji''s Guard, Eye of Providence, Bloodforge, Midgardian Mail,
    Shifter''s Shield, Leviathan''s Hide, Lernaean Bow, Hide of the Nemean Lion, Stone
    of Binding, Ancile, Umbral Link, Avenging Blade.'
  slot_scores:
    Hydra's Lament:
      total: 0.44
      efficiency: 0.5
      win: 0.5
      pick: 0.22
      fit: 0.22
    Demon Blade:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.18
      fit: 0.52
    Deathbringer:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.45
      fit: 0.32
    Dominance:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.48
      fit: 0.42
    Musashi's Dual Swords:
      total: 0.43
      efficiency: 0.38
      win: 0.5
      pick: 0.52
      fit: 0.32
    Amanita Charm:
      total: 0.45
      efficiency: 0.68
      win: 0.23
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Hydra's Lament
  - Demon Blade
  - Deathbringer
  - Dominance
  - Musashi's Dual Swords
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Hydra's Lament
  - Riptalon
  - Demon Blade
  - Dominance
  - Musashi's Dual Swords
  - Deathbringer
  flex_slots:
  - Musashi's Dual Swords
  - Riptalon
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
    for this god: The Reaper, Tekko-Kagi, The Crusher, Heartseeker, Titan''s Bane,
    Jotunn''s Revenge, Toxic Blade, Lernaean Bow, Avatar''s Parashu, Avenging Blade,
    Golden Blade, Rage, Berserker''s Shield, Oath-Sworn Spear, Transcendence, Bloodforge,
    Runeforged Hammer, Barbed Carver, Pendulum Blade, Qin''s Blade.'
  slot_scores:
    Hydra's Lament:
      total: 0.44
      efficiency: 0.5
      win: 0.5
      pick: 0.22
      fit: 0.24
    Riptalon:
      total: 0.43
      efficiency: 0.45
      win: 0.33
      pick: 0.33
      fit: 0.72
    Demon Blade:
      total: 0.67
      efficiency: 0.36
      win: 1.0
      pick: 0.18
      fit: 0.58
    Dominance:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.48
      fit: 0.46
    Musashi's Dual Swords:
      total: 0.44
      efficiency: 0.38
      win: 0.5
      pick: 0.52
      fit: 0.36
    Deathbringer:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.45
      fit: 0.36
  community_ordered:
  - Hydra's Lament
  - Riptalon
  - Demon Blade
  - Dominance
  - Musashi's Dual Swords
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Hydra's Lament
  - Riptalon
  - Demon Blade
  - Dominance
  - Musashi's Dual Swords
  - Deathbringer
  flex_slots:
  - Musashi's Dual Swords
  - Riptalon
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
    this god: Golden Blade, Lernaean Bow, Rage, Tekko-Kagi, The Reaper, Berserker''s
    Shield, Sun Beam Bow, Bloodforge, Transcendence, Barbed Carver, Toxic Blade, Runeforged
    Hammer, Odysseus'' Bow, Jotunn''s Revenge, The Crusher, Shield Splitter, Eye of
    the Storm, Avenging Blade, Heartseeker, Vital Amplifier, Qin''s Blade.'
  slot_scores:
    Hydra's Lament:
      total: 0.45
      efficiency: 0.5
      win: 0.5
      pick: 0.22
      fit: 0.26
    Riptalon:
      total: 0.38
      efficiency: 0.36
      win: 0.33
      pick: 0.33
      fit: 0.59
    Demon Blade:
      total: 0.69
      efficiency: 0.36
      win: 1.0
      pick: 0.18
      fit: 0.71
    Dominance:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.48
      fit: 0.55
    Musashi's Dual Swords:
      total: 0.45
      efficiency: 0.38
      win: 0.5
      pick: 0.52
      fit: 0.41
    Deathbringer:
      total: 0.69
      efficiency: 0.44
      win: 1.0
      pick: 0.45
      fit: 0.41
  community_ordered:
  - Hydra's Lament
  - Riptalon
  - Demon Blade
  - Dominance
  - Musashi's Dual Swords
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Demon Blade
  - Dominance
  - Deathbringer
  flex_slots:
  - Jotunn's Revenge
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Arondight, Lernaean
    Bow, Damaru, Genji''s Guard, Golden Blade, Rage, Breastplate of Valor, Chandra''s
    Grace, The Reaper, Berserker''s Shield, Transcendence, Runeforged Hammer, Bloodforge,
    Tekko-Kagi, Barbed Carver, Screeching Gargoyle, Freya''s Tears, Odysseus'' Bow,
    The Crusher, Eye of Erebus, Qin''s Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.38
      efficiency: 0.61
      win: 0.23
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.22
      fit: 0.51
    Arondight:
      total: 0.35
      efficiency: 0.53
      win: 0.23
      pick: 0.0
      fit: 0.41
    Demon Blade:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.18
      fit: 0.51
    Dominance:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.48
      fit: 0.4
    Deathbringer:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.45
      fit: 0.3
  community_ordered:
  - Hydra's Lament
  - Demon Blade
  - Dominance
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Rage
  - Tyrfing
  - Dominance
  - Demon Blade
  flex_slots:
  - Golden Blade
  - Rage
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
    Underrated for this god: Lernaean Bow, Golden Blade, Rage, Qin''s Blade, Tekko-Kagi,
    The Reaper, Berserker''s Shield, Bloodforge, Barbed Carver, Transcendence, Runeforged
    Hammer, Odysseus'' Bow, Jotunn''s Revenge, Sun Beam Bow, The Crusher, Shield Splitter,
    Eye of the Storm, Avenging Blade, Toxic Blade, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.36
      efficiency: 0.45
      win: 0.23
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.37
      efficiency: 0.47
      win: 0.23
      pick: 0.0
      fit: 0.64
    Rage:
      total: 0.35
      efficiency: 0.46
      win: 0.23
      pick: 0.0
      fit: 0.54
    Tyrfing:
      total: 0.31
      efficiency: 0.53
      win: 0.0
      pick: 0.18
      fit: 0.75
    Dominance:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.48
      fit: 0.64
    Demon Blade:
      total: 0.72
      efficiency: 0.36
      win: 1.0
      pick: 0.18
      fit: 0.87
  community_ordered:
  - Tyrfing
  - Dominance
  - Demon Blade
  starter: *id001
  relic: *id002
---
