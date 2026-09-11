---
type: smite-build
god: Chiron
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Heroic Tutor
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.69
  slot_order:
  - name: Transcendence
    pick_rate: 0.39
    win_rate: 0.56
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.28
      win_rate: 0.67
    - name: Tyrfing
      pick_rate: 0.13
      win_rate: 0.72
  - name: Jotunn's Revenge
    pick_rate: 0.34
    win_rate: 0.55
    alternates:
    - name: Transcendence
      pick_rate: 0.16
      win_rate: 0.59
    - name: Daybreak Gavel
      pick_rate: 0.11
      win_rate: 0.53
  - name: The Crusher
    pick_rate: 0.15
    win_rate: 0.47
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.17
      win_rate: 0.59
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.56
  - name: Heartseeker
    pick_rate: 0.3
    win_rate: 0.55
    alternates:
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.67
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.8
  - name: Titan's Bane
    pick_rate: 0.2
    win_rate: 0.41
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.6
    - name: The Executioner
      pick_rate: 0.09
      win_rate: 0.8
  - name: Skeggox
    pick_rate: 0.15
    win_rate: 0.08
    alternates:
    - name: Titan's Bane
      pick_rate: 0.1
      win_rate: 0.88
    - name: Avatar's Parashu
      pick_rate: 0.1
      win_rate: 0.75
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.34
    win_rate: 0.62
  - name: Bluestone Pendant
    pick_rate: 0.24
    win_rate: 0.52
  - name: Hunter's Cowl
    pick_rate: 0.18
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/chiron/
  last_verified: '2026-09-11'
  god_win_rate: 0.6204379562043796
  god_matches_won: 85
  god_matches_played: 137
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Transcendence
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Tyrfing, Riptalon, Tekko-Kagi, Lernaean Bow, The Reaper, Silverbranch
    Bow, Hydra''s Lament, Deathbringer, Golden Blade, Dominance, Demon Blade, Toxic
    Blade, Musashi''s Dual Swords, Arondight, Pendulum Blade, Damaru, Rage, Runeforged
    Hammer, Qin''s Blade, Berserker''s Shield, Avenging Blade, Barbed Carver, Sun
    Beam Bow, Bloodforge.'
  slot_scores:
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.56
      pick: 0.39
      fit: 0.17
    The Executioner:
      total: 0.54
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.34
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.44
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.57
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.55
      pick: 0.5
      fit: 0.54
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.34
  community_ordered:
  - Transcendence
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Tyrfing,
    Hydra''s Lament, Lernaean Bow, The Reaper, Tekko-Kagi, Riptalon, Silverbranch
    Bow, Dominance, Deathbringer, Golden Blade, Arondight, Musashi''s Dual Swords,
    Demon Blade, Runeforged Hammer, Pendulum Blade, Toxic Blade, Damaru, Rage, Avenging
    Blade, Qin''s Blade, Barbed Carver, Berserker''s Shield, Breastplate of Valor,
    Genji''s Guard.'
  slot_scores:
    The Executioner:
      total: 0.53
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.26
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.44
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.48
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.55
      pick: 0.5
      fit: 0.55
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.29
  community_ordered:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Demon Blade
  - Deathbringer
  - Avatar's Parashu
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, Riptalon, The Reaper, Silverbranch Bow, Tekko-Kagi, Lernaean
    Bow, Hydra''s Lament, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s
    Dual Swords, Toxic Blade, Arondight, Damaru, Rage, Pendulum Blade, Qin''s Blade,
    Runeforged Hammer, Berserker''s Shield, Avenging Blade, Barbed Carver, Sun Beam
    Bow, Bloodforge.'
  slot_scores:
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.53
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.47
      efficiency: 0.46
      win: 0.56
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.48
      efficiency: 0.38
      win: 0.56
      pick: 0.0
      fit: 0.64
    Deathbringer:
      total: 0.49
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.32
  community_ordered:
  - Tyrfing
  - Jotunn's Revenge
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Transcendence
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    god: Tyrfing, The Reaper, Riptalon, Silverbranch Bow, Tekko-Kagi, Hydra''s Lament,
    Lernaean Bow, Deathbringer, Pendulum Blade, Dominance, Golden Blade, Arondight,
    Toxic Blade, Musashi''s Dual Swords, Demon Blade, Runeforged Hammer, Damaru, Rage,
    Qin''s Blade, Avenging Blade, Berserker''s Shield, Breastplate of Valor, Barbed
    Carver.'
  slot_scores:
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.56
      pick: 0.39
      fit: 0.13
    The Executioner:
      total: 0.53
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.27
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.46
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.45
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.55
      pick: 0.5
      fit: 0.53
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.33
  community_ordered:
  - Transcendence
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Daybreak Gavel
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Daybreak Gavel
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
    this god: Amanita Charm, Tyrfing, Berserker''s Shield, Riptalon, The Reaper, Shield
    of the Phoenix, Kinetic Cuirass, Genji''s Guard, Freya''s Tears, Breastplate of
    Valor, Runeforged Hammer, Golden Blade, Yogi''s Necklace, Shifter''s Shield, Shield
    Splitter, Lernaean Bow, Pharaoh''s Curse, Hydra''s Lament, Chandra''s Grace, Silverbranch
    Bow, Shogun''s Ofuda, Phoenix Feather, Eye of the Storm, Tekko-Kagi, Toxic Blade,
    Erosion, Eye of Providence.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.3
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.42
    Daybreak Gavel:
      total: 0.54
      efficiency: 0.59
      win: 0.67
      pick: 0.28
      fit: 0.12
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.23
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Daybreak Gavel
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Transcendence
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Tyrfing, Riptalon, The Reaper, Tekko-Kagi, Silverbranch Bow, Lernaean
    Bow, Hydra''s Lament, Toxic Blade, Avenging Blade, Deathbringer, Pendulum Blade,
    Golden Blade, Dominance, Demon Blade, Musashi''s Dual Swords, Arondight, Oath-Sworn
    Spear, Runeforged Hammer, Damaru, Rage, Qin''s Blade, Berserker''s Shield, Screeching
    Gargoyle.'
  slot_scores:
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.56
      pick: 0.39
      fit: 0.14
    The Executioner:
      total: 0.58
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.6
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.53
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.49
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.55
      pick: 0.5
      fit: 0.65
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.45
  community_ordered:
  - Transcendence
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Riptalon
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Tyrfing, Riptalon, Silverbranch Bow, Lernaean Bow, Tekko-Kagi, The Reaper,
    Golden Blade, Hydra''s Lament, Toxic Blade, Deathbringer, Dominance, Qin''s Blade,
    Demon Blade, Musashi''s Dual Swords, Arondight, Sun Beam Bow, Pendulum Blade,
    Runeforged Hammer, Berserker''s Shield, Damaru, Rage, Avenging Blade, Dagger of
    Frenzy, Barbed Carver.'
  slot_scores:
    The Executioner:
      total: 0.54
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.35
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.6
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.52
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.26
  community_ordered:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Arondight
  - Avatar's Parashu
  flex_slots:
  - Hydra's Lament
  - Arondight
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Tyrfing, Hydra''s Lament, Riptalon,
    Silverbranch Bow, Lernaean Bow, The Reaper, Tekko-Kagi, Arondight, Pendulum Blade,
    Deathbringer, Dominance, Golden Blade, Toxic Blade, Breastplate of Valor, Musashi''s
    Dual Swords, Genji''s Guard, Demon Blade, Qin''s Blade, Runeforged Hammer, Berserker''s
    Shield, Damaru, Rage, Avenging Blade.'
  slot_scores:
    The Executioner:
      total: 0.53
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.28
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.49
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.41
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.46
    Arondight:
      total: 0.48
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.36
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.21
  community_ordered:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - The Reaper
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
    Underrated for this god: Riptalon, Tekko-Kagi, Lernaean Bow, The Reaper, Silverbranch
    Bow, Tyrfing, Hydra''s Lament, Deathbringer, Golden Blade, Dominance, Demon Blade,
    Toxic Blade, Musashi''s Dual Swords, Arondight, Pendulum Blade, Damaru, Rage,
    Runeforged Hammer, Qin''s Blade, Berserker''s Shield, Avenging Blade, Barbed Carver,
    Sun Beam Bow, Bloodforge.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.44
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.56
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.47
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - The Reaper
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, The Reaper, Hydra''s Lament, Deathbringer, Riptalon, Tekko-Kagi,
    Silverbranch Bow, Lernaean Bow, Musashi''s Dual Swords, Pendulum Blade, Arondight,
    Damaru, Rage, Demon Blade, Golden Blade, Dominance, Runeforged Hammer, Toxic Blade,
    Barbed Carver, Avenging Blade, Bloodforge, Qin''s Blade, Shield Splitter, Breastplate
    of Valor.'
  slot_scores:
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.56
      pick: 0.39
      fit: 0.2
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.53
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.45
    The Reaper:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.53
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.55
      pick: 0.5
      fit: 0.61
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.41
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: mana-stack
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Tyrfing,
    Hydra''s Lament, The Reaper, Deathbringer, Lernaean Bow, Tekko-Kagi, Riptalon,
    Arondight, Musashi''s Dual Swords, Dominance, Silverbranch Bow, Pendulum Blade,
    Runeforged Hammer, Golden Blade, Damaru, Rage, Avenging Blade, Demon Blade, Barbed
    Carver, Breastplate of Valor, Toxic Blade, Bloodforge, Genji''s Guard, Shield
    Splitter.'
  slot_scores:
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.56
      pick: 0.39
      fit: 0.27
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.5
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.39
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.47
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.55
      pick: 0.5
      fit: 0.6
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.33
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Demon Blade
  - Deathbringer
  - Avatar's Parashu
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, Riptalon, The Reaper, Silverbranch Bow, Tekko-Kagi, Lernaean
    Bow, Hydra''s Lament, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s
    Dual Swords, Toxic Blade, Arondight, Damaru, Rage, Pendulum Blade, Qin''s Blade,
    Runeforged Hammer, Berserker''s Shield, Avenging Blade, Barbed Carver, Sun Beam
    Bow, Bloodforge.'
  slot_scores:
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.53
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.47
      efficiency: 0.46
      win: 0.56
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.48
      efficiency: 0.38
      win: 0.56
      pick: 0.0
      fit: 0.64
    Deathbringer:
      total: 0.49
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.32
  community_ordered:
  - Tyrfing
  - Jotunn's Revenge
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: burst
  slot_order:
  - Transcendence
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - The Executioner
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Tyrfing, The Reaper, Hydra''s Lament, Riptalon, Tekko-Kagi, Silverbranch
    Bow, Deathbringer, Pendulum Blade, Lernaean Bow, Arondight, Musashi''s Dual Swords,
    Runeforged Hammer, Toxic Blade, Golden Blade, Dominance, Damaru, Rage, Demon Blade,
    Avenging Blade, Barbed Carver, Breastplate of Valor, Genji''s Guard, Bloodforge.'
  slot_scores:
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.56
      pick: 0.39
      fit: 0.15
    The Executioner:
      total: 0.51
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.15
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.53
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.35
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.55
      pick: 0.5
      fit: 0.58
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.38
  community_ordered:
  - Transcendence
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Tyrfing
  - Jotunn's Revenge
  - Daybreak Gavel
  - The Reaper
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Daybreak Gavel
  - The Reaper
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, The Reaper, Berserker''s Shield, Shield of the Phoenix,
    Riptalon, Kinetic Cuirass, Freya''s Tears, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Erosion, Shifter''s Shield, Yogi''s Necklace, Shield Splitter,
    Pharaoh''s Curse, Eye of the Storm, Umbral Link, Golden Blade, Phoenix Feather,
    Chandra''s Grace, Hydra''s Lament, Shogun''s Ofuda, Eye of Providence, Void Shield,
    Stampede, Draconic Scale, Avenging Blade.'
  slot_scores:
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.32
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.34
    Daybreak Gavel:
      total: 0.54
      efficiency: 0.59
      win: 0.67
      pick: 0.28
      fit: 0.14
    The Reaper:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.63
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.26
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Tyrfing
  - Jotunn's Revenge
  - Daybreak Gavel
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: anti-tank
  slot_order:
  - Transcendence
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Tyrfing, The Reaper, Riptalon, Tekko-Kagi, Silverbranch Bow, Hydra''s
    Lament, Pendulum Blade, Avenging Blade, Deathbringer, Lernaean Bow, Toxic Blade,
    Musashi''s Dual Swords, Arondight, Oath-Sworn Spear, Damaru, Rage, Golden Blade,
    Runeforged Hammer, Dominance, Demon Blade, Barbed Carver, Screeching Gargoyle,
    Bloodforge.'
  slot_scores:
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.56
      pick: 0.39
      fit: 0.17
    The Executioner:
      total: 0.56
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.45
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.62
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.38
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.55
      pick: 0.5
      fit: 0.73
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.53
  community_ordered:
  - Transcendence
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: attack-speed
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Riptalon
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Tyrfing, Riptalon, Silverbranch Bow, Lernaean Bow, Tekko-Kagi, The Reaper,
    Golden Blade, Hydra''s Lament, Toxic Blade, Deathbringer, Dominance, Qin''s Blade,
    Demon Blade, Musashi''s Dual Swords, Arondight, Sun Beam Bow, Pendulum Blade,
    Runeforged Hammer, Berserker''s Shield, Damaru, Rage, Avenging Blade, Dagger of
    Frenzy, Barbed Carver.'
  slot_scores:
    The Executioner:
      total: 0.54
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.35
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.6
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.52
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.26
  community_ordered:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: cooldown
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Arondight
  - Avatar's Parashu
  flex_slots:
  - The Executioner
  - Arondight
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Tyrfing, Hydra''s Lament, The Reaper,
    Arondight, Pendulum Blade, Riptalon, Deathbringer, Silverbranch Bow, Lernaean
    Bow, Tekko-Kagi, Breastplate of Valor, Musashi''s Dual Swords, Genji''s Guard,
    Runeforged Hammer, Golden Blade, Damaru, Rage, Dominance, Toxic Blade, Demon Blade,
    Avenging Blade, Eye of Erebus, Barbed Carver.'
  slot_scores:
    The Executioner:
      total: 0.52
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.15
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.57
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.72
      pick: 0.13
      fit: 0.3
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.52
    Arondight:
      total: 0.49
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.25
  community_ordered:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: model
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Reaper, Hydra''s Lament, Deathbringer, Riptalon,
    Tekko-Kagi, Silverbranch Bow, Tyrfing, Lernaean Bow, Musashi''s Dual Swords, Pendulum
    Blade, Arondight, Damaru, Rage, Demon Blade, Golden Blade, Dominance, Runeforged
    Hammer, Toxic Blade, Barbed Carver, Avenging Blade, Bloodforge, Qin''s Blade,
    Shield Splitter, Breastplate of Valor.'
  slot_scores:
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.56
      pick: 0.39
      fit: 0.2
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.55
      pick: 0.46
      fit: 0.53
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.53
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.55
      pick: 0.5
      fit: 0.61
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
