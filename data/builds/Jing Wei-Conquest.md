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
    pick_rate: 0.59
    win_rate: 0.2
    alternates:
    - name: Tyrfing
      pick_rate: 0.18
      win_rate: 0.33
    - name: Dagger of Frenzy
      pick_rate: 0.06
      win_rate: 0.0
  - name: Dagger of Frenzy
    pick_rate: 0.35
    win_rate: 0.17
    alternates:
    - name: Transcendence
      pick_rate: 0.29
      win_rate: 0.4
    - name: Avenging Blade
      pick_rate: 0.18
      win_rate: 0.67
  - name: Toxic Blade
    pick_rate: 0.29
    win_rate: 0.4
    alternates:
    - name: Deathbringer
      pick_rate: 0.24
      win_rate: 0.25
    - name: Musashi's Dual Swords
      pick_rate: 0.18
      win_rate: 0.0
  - name: Deathbringer
    pick_rate: 0.53
    win_rate: 0.33
    alternates:
    - name: Riptalon
      pick_rate: 0.12
      win_rate: 0.0
    - name: Silverbranch Bow
      pick_rate: 0.12
      win_rate: 0.0
  - name: Dominance
    pick_rate: 0.18
    win_rate: 0.0
    alternates:
    - name: The Executioner
      pick_rate: 0.18
      win_rate: 0.0
    - name: Bow
      pick_rate: 0.12
      win_rate: 0.0
  - name: Skeggox
    pick_rate: 0.17
    win_rate: 0.0
    alternates:
    - name: Avatar's Parashu
      pick_rate: 0.17
      win_rate: 0.0
    - name: Dominance
      pick_rate: 0.17
      win_rate: 1.0
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.76
    win_rate: 0.31
  - name: Gilded Arrow
    pick_rate: 0.18
    win_rate: 0.33
  - name: Death's Toll
    pick_rate: 0.06
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/jing-wei/
  last_verified: '2026-08-26'
  god_win_rate: 0.29411764705882354
  god_matches_won: 5
  god_matches_played: 17
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Avenging Blade
  - Toxic Blade
  - Transcendence
  - Tyrfing
  - Dagger of Frenzy
  - Deathbringer
  flex_slots:
  - Toxic Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Demon Blade, Golden Blade, Damaru, Rage, Qin''s Blade,
    Tekko-Kagi, Jotunn''s Revenge, Hydra''s Lament, The Reaper, Berserker''s Shield,
    Runeforged Hammer, Sun Beam Bow, Barbed Carver, Vital Amplifier, Bloodforge, Heartseeker,
    Odysseus'' Bow, Shield Splitter.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.67
      pick: 0.25
      fit: 0.31
    Toxic Blade:
      total: 0.39
      efficiency: 0.35
      win: 0.4
      pick: 0.45
      fit: 0.44
    Transcendence:
      total: 0.41
      efficiency: 0.53
      win: 0.4
      pick: 0.4
      fit: 0.21
    Tyrfing:
      total: 0.44
      efficiency: 0.48
      win: 0.33
      pick: 0.18
      fit: 0.75
    Dagger of Frenzy:
      total: 0.3
      efficiency: 0.37
      win: 0.17
      pick: 0.48
      fit: 0.44
    Deathbringer:
      total: 0.45
      efficiency: 0.51
      win: 0.33
      pick: 0.88
      fit: 0.54
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Avenging Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Deathbringer
  flex_slots:
  - Jotunn's Revenge
  - Hydra's Lament
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Titan''s
    Bane, Golden Blade, The Crusher, Arondight, Demon Blade, Runeforged Hammer, Pendulum
    Blade, Damaru, Rage, Qin''s Blade, Barbed Carver, Berserker''s Shield, Breastplate
    of Valor, Genji''s Guard.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.67
      pick: 0.25
      fit: 0.28
    Toxic Blade:
      total: 0.4
      efficiency: 0.44
      win: 0.4
      pick: 0.45
      fit: 0.33
    Jotunn's Revenge:
      total: 0.32
      efficiency: 0.72
      win: 0.0
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.42
      efficiency: 0.53
      win: 0.4
      pick: 0.4
      fit: 0.24
    Hydra's Lament:
      total: 0.25
      efficiency: 0.54
      win: 0.0
      pick: 0.0
      fit: 0.42
    Deathbringer:
      total: 0.42
      efficiency: 0.51
      win: 0.33
      pick: 0.88
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Avenging Blade
  - Transcendence
  - Tyrfing
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
    this god: Lernaean Bow, Demon Blade, Golden Blade, Damaru, Rage, Qin''s Blade,
    Jotunn''s Revenge, Hydra''s Lament, Tekko-Kagi, The Reaper, Runeforged Hammer,
    Berserker''s Shield, Sun Beam Bow, Barbed Carver, Bloodforge, Vital Amplifier,
    Heartseeker, Shield Splitter, The Crusher.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.67
      pick: 0.25
      fit: 0.3
    Transcendence:
      total: 0.41
      efficiency: 0.53
      win: 0.4
      pick: 0.4
      fit: 0.2
    Tyrfing:
      total: 0.43
      efficiency: 0.48
      win: 0.33
      pick: 0.18
      fit: 0.71
    Musashi's Dual Swords:
      total: 0.26
      efficiency: 0.46
      win: 0.0
      pick: 0.28
      fit: 0.57
    Demon Blade:
      total: 0.26
      efficiency: 0.38
      win: 0.0
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.46
      efficiency: 0.51
      win: 0.33
      pick: 0.88
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Toxic Blade
  - Transcendence
  - Tyrfing
  - Deathbringer
  - Amanita Charm
  flex_slots:
  - Toxic Blade
  - Amanita Charm
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Golden Blade, Runeforged
    Hammer, Shield of the Phoenix, Shifter''s Shield, Pharaoh''s Curse, Yogi''s Necklace,
    Shield Splitter, Shogun''s Ofuda, Lernaean Bow, Eye of the Storm, Phoenix Feather,
    Erosion, The Reaper, Eye of Providence, Draconic Scale, Daybreak Gavel, Stone
    of Binding, Midgardian Mail, Umbral Link, Magi''s Cloak, Hide of the Nemean Lion,
    Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.67
      pick: 0.25
      fit: 0.38
    Toxic Blade:
      total: 0.4
      efficiency: 0.38
      win: 0.4
      pick: 0.45
      fit: 0.42
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.4
      pick: 0.4
      fit: 0.12
    Tyrfing:
      total: 0.4
      efficiency: 0.48
      win: 0.33
      pick: 0.18
      fit: 0.49
    Deathbringer:
      total: 0.42
      efficiency: 0.51
      win: 0.33
      pick: 0.88
      fit: 0.32
    Amanita Charm:
      total: 0.33
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Toxic Blade
  - Transcendence
  - Tyrfing
  - Riptalon
  - Deathbringer
  flex_slots:
  - Transcendence
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker, Titan''s
    Bane, The Crusher, Lernaean Bow, Golden Blade, Demon Blade, Hydra''s Lament, Oath-Sworn
    Spear, Qin''s Blade, Damaru, Runeforged Hammer, Rage, Pendulum Blade, Berserker''s
    Shield, Sun Beam Bow, Barbed Carver.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.44
      win: 0.67
      pick: 0.25
      fit: 0.54
    Toxic Blade:
      total: 0.45
      efficiency: 0.44
      win: 0.4
      pick: 0.45
      fit: 0.63
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.4
      pick: 0.4
      fit: 0.14
    Tyrfing:
      total: 0.41
      efficiency: 0.48
      win: 0.33
      pick: 0.18
      fit: 0.53
    Riptalon:
      total: 0.3
      efficiency: 0.51
      win: 0.0
      pick: 0.2
      fit: 0.72
    Deathbringer:
      total: 0.42
      efficiency: 0.51
      win: 0.33
      pick: 0.88
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Avenging Blade
  - Toxic Blade
  - Transcendence
  - Tyrfing
  - Dagger of Frenzy
  - Deathbringer
  flex_slots:
  - Toxic Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Golden Blade, Demon Blade, Qin''s Blade, Sun Beam Bow,
    Jotunn''s Revenge, Hydra''s Lament, Damaru, Tekko-Kagi, Rage, Berserker''s Shield,
    Runeforged Hammer, The Reaper, Barbed Carver, Vital Amplifier, Hastened Fatalis,
    Bloodforge, Heartseeker, Daybreak Gavel.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.67
      pick: 0.25
      fit: 0.26
    Toxic Blade:
      total: 0.4
      efficiency: 0.35
      win: 0.4
      pick: 0.45
      fit: 0.49
    Transcendence:
      total: 0.41
      efficiency: 0.53
      win: 0.4
      pick: 0.4
      fit: 0.16
    Tyrfing:
      total: 0.44
      efficiency: 0.48
      win: 0.33
      pick: 0.18
      fit: 0.75
    Dagger of Frenzy:
      total: 0.3
      efficiency: 0.37
      win: 0.17
      pick: 0.48
      fit: 0.49
    Deathbringer:
      total: 0.43
      efficiency: 0.51
      win: 0.33
      pick: 0.88
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Arondight
  - Deathbringer
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
    Lernaean Bow, Arondight, Golden Blade, Breastplate of Valor, Demon Blade, Genji''s
    Guard, Qin''s Blade, Runeforged Hammer, Damaru, Rage, Berserker''s Shield, The
    Reaper, Tekko-Kagi, Sun Beam Bow, Eye of Erebus, Daybreak Gavel, Barbed Carver,
    Vital Amplifier, Screeching Gargoyle, Chandra''s Grace.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.44
      win: 0.67
      pick: 0.25
      fit: 0.2
    Jotunn's Revenge:
      total: 0.3
      efficiency: 0.67
      win: 0.0
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.4
      pick: 0.4
      fit: 0.1
    Hydra's Lament:
      total: 0.27
      efficiency: 0.54
      win: 0.0
      pick: 0.0
      fit: 0.51
    Arondight:
      total: 0.24
      efficiency: 0.5
      win: 0.0
      pick: 0.0
      fit: 0.41
    Deathbringer:
      total: 0.41
      efficiency: 0.51
      win: 0.33
      pick: 0.88
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
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
    Underrated for this god: Lernaean Bow, Demon Blade, Golden Blade, Damaru, Rage,
    Qin''s Blade, Tekko-Kagi, Jotunn''s Revenge, Hydra''s Lament, The Reaper, Berserker''s
    Shield, Runeforged Hammer, Sun Beam Bow, Barbed Carver, Vital Amplifier, Bloodforge,
    Heartseeker, Odysseus'' Bow, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.26
      efficiency: 0.47
      win: 0.0
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.28
      efficiency: 0.52
      win: 0.0
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.44
      efficiency: 0.48
      win: 0.33
      pick: 0.18
      fit: 0.75
    Dominance:
      total: 0.27
      efficiency: 0.45
      win: 0.0
      pick: 0.39
      fit: 0.64
    Demon Blade:
      total: 0.26
      efficiency: 0.38
      win: 0.0
      pick: 0.0
      fit: 0.87
    Deathbringer:
      total: 0.45
      efficiency: 0.51
      win: 0.33
      pick: 0.88
      fit: 0.54
  starter: *id001
---
