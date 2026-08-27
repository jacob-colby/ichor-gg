---
type: smite-build
god: Ullr
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Transcendence
    pick_rate: 0.91
    win_rate: 0.49
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.04
      win_rate: 0.5
    - name: Jotunn's Revenge
      pick_rate: 0.03
      win_rate: 0.8
  - name: Hydra's Lament
    pick_rate: 0.57
    win_rate: 0.48
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.33
      win_rate: 0.52
    - name: Transcendence
      pick_rate: 0.07
      win_rate: 0.6
  - name: Jotunn's Revenge
    pick_rate: 0.51
    win_rate: 0.45
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.28
      win_rate: 0.54
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.7
    win_rate: 0.48
    alternates:
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.45
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.36
  - name: Titan's Bane
    pick_rate: 0.36
    win_rate: 0.48
    alternates:
    - name: Avatar's Parashu
      pick_rate: 0.11
      win_rate: 0.6
    - name: Void Shard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Lucerne Hammer
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Barbed Carver
      pick_rate: 0.1
      win_rate: 0.75
    - name: Skeggox
      pick_rate: 0.08
      win_rate: 0.57
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.56
    win_rate: 0.57
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.5
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/ullr/
  last_verified: '2026-08-27'
  god_win_rate: 0.5
  god_matches_won: 75
  god_matches_played: 150
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Barbed Carver
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
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
    this god: Riptalon, Lernaean Bow, Tekko-Kagi, Tyrfing, The Reaper, Silverbranch
    Bow, Deathbringer, Golden Blade, Dominance, Demon Blade, Musashi''s Dual Swords,
    Toxic Blade, Arondight, The Crusher, Pendulum Blade, Damaru, Rage, Runeforged
    Hammer, Qin''s Blade, Berserker''s Shield, Avenging Blade, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.45
      pick: 0.79
      fit: 0.42
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.49
      pick: 0.91
      fit: 0.17
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.48
      pick: 0.78
      fit: 0.37
    Barbed Carver:
      total: 0.55
      efficiency: 0.39
      win: 0.75
      pick: 0.31
      fit: 0.37
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.48
      pick: 1.0
      fit: 0.52
    Avatar's Parashu:
      total: 0.49
      efficiency: 0.45
      win: 0.6
      pick: 0.24
      fit: 0.32
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Barbed Carver
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Transcendence
  - Avatar's Parashu
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Lernaean
    Bow, The Reaper, Tyrfing, Tekko-Kagi, Riptalon, Dominance, Silverbranch Bow, Deathbringer,
    Golden Blade, Arondight, Musashi''s Dual Swords, The Crusher, Demon Blade, Runeforged
    Hammer, Pendulum Blade, Toxic Blade, Damaru, Rage, Avenging Blade, Qin''s Blade,
    Berserker''s Shield, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.45
      pick: 0.79
      fit: 0.44
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.49
      pick: 0.91
      fit: 0.24
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.48
      pick: 0.78
      fit: 0.42
    Barbed Carver:
      total: 0.54
      efficiency: 0.39
      win: 0.75
      pick: 0.31
      fit: 0.34
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.48
      pick: 1.0
      fit: 0.55
    Avatar's Parashu:
      total: 0.48
      efficiency: 0.45
      win: 0.6
      pick: 0.24
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Barbed Carver
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Lernaean Bow, The Reaper, Tekko-Kagi, Tyrfing, Silverbranch
    Bow, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s Dual Swords,
    Toxic Blade, Arondight, Damaru, The Crusher, Rage, Pendulum Blade, Runeforged
    Hammer, Qin''s Blade, Berserker''s Shield, Avenging Blade, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.45
      pick: 0.79
      fit: 0.4
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.49
      pick: 0.91
      fit: 0.15
    Barbed Carver:
      total: 0.54
      efficiency: 0.39
      win: 0.75
      pick: 0.31
      fit: 0.34
    Musashi's Dual Swords:
      total: 0.45
      efficiency: 0.46
      win: 0.49
      pick: 0.0
      fit: 0.43
    Demon Blade:
      total: 0.45
      efficiency: 0.38
      win: 0.49
      pick: 0.0
      fit: 0.66
    Deathbringer:
      total: 0.46
      efficiency: 0.51
      win: 0.49
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Barbed Carver
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
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
    god: The Reaper, Riptalon, Tekko-Kagi, Silverbranch Bow, Lernaean Bow, Tyrfing,
    Deathbringer, The Crusher, Pendulum Blade, Dominance, Golden Blade, Arondight,
    Toxic Blade, Musashi''s Dual Swords, Demon Blade, Runeforged Hammer, Damaru, Rage,
    Qin''s Blade, Avenging Blade, Berserker''s Shield, Breastplate of Valor, Daybreak
    Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.45
      pick: 0.79
      fit: 0.46
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.49
      pick: 0.91
      fit: 0.13
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.48
      pick: 0.78
      fit: 0.36
    Barbed Carver:
      total: 0.54
      efficiency: 0.39
      win: 0.75
      pick: 0.31
      fit: 0.3
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.48
      pick: 1.0
      fit: 0.53
    Avatar's Parashu:
      total: 0.49
      efficiency: 0.45
      win: 0.6
      pick: 0.24
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Barbed Carver
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Amanita Charm, Berserker''s Shield, The Reaper, Riptalon, Shield of
    the Phoenix, Kinetic Cuirass, Freya''s Tears, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Golden Blade, Yogi''s Necklace, Shifter''s Shield, Shield Splitter,
    Lernaean Bow, Pharaoh''s Curse, Shogun''s Ofuda, Chandra''s Grace, Tyrfing, Phoenix
    Feather, Eye of the Storm, Silverbranch Bow, Erosion, Tekko-Kagi, Eye of Providence,
    Daybreak Gavel, Toxic Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.49
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.45
      pick: 0.79
      fit: 0.28
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.49
      pick: 0.91
      fit: 0.12
    Barbed Carver:
      total: 0.53
      efficiency: 0.39
      win: 0.75
      pick: 0.31
      fit: 0.28
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.48
      pick: 1.0
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Barbed Carver
  - Heartseeker
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
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
    for this god: Riptalon, The Reaper, Tekko-Kagi, Silverbranch Bow, Lernaean Bow,
    Tyrfing, Avenging Blade, Toxic Blade, The Crusher, Deathbringer, Pendulum Blade,
    Dominance, Golden Blade, Demon Blade, The Executioner, Musashi''s Dual Swords,
    Arondight, Oath-Sworn Spear, Runeforged Hammer, Damaru, Rage, Qin''s Blade, Berserker''s
    Shield, Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.45
      pick: 0.79
      fit: 0.53
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.49
      pick: 0.91
      fit: 0.14
    Barbed Carver:
      total: 0.54
      efficiency: 0.39
      win: 0.75
      pick: 0.31
      fit: 0.32
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.48
      pick: 1.0
      fit: 0.65
    Titan's Bane:
      total: 0.5
      efficiency: 0.47
      win: 0.48
      pick: 0.78
      fit: 0.55
    Avatar's Parashu:
      total: 0.51
      efficiency: 0.45
      win: 0.6
      pick: 0.24
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Barbed Carver
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Tyrfing, Silverbranch Bow, Lernaean Bow, Tekko-Kagi, The Reaper,
    Golden Blade, Toxic Blade, Deathbringer, Dominance, Qin''s Blade, Demon Blade,
    Musashi''s Dual Swords, Arondight, The Crusher, Sun Beam Bow, Runeforged Hammer,
    Pendulum Blade, Damaru, Berserker''s Shield, Rage, Avenging Blade, Dagger of Frenzy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.45
      pick: 0.79
      fit: 0.33
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.49
      pick: 0.91
      fit: 0.12
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.49
      pick: 0.0
      fit: 0.61
    Barbed Carver:
      total: 0.54
      efficiency: 0.39
      win: 0.75
      pick: 0.31
      fit: 0.3
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.49
      pick: 0.0
      fit: 0.59
    Silverbranch Bow:
      total: 0.48
      efficiency: 0.53
      win: 0.49
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Barbed Carver
  - Arondight
  - Heartseeker
  flex_slots:
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Riptalon, Lernaean Bow, Silverbranch
    Bow, The Reaper, Tyrfing, Arondight, Tekko-Kagi, Pendulum Blade, Deathbringer,
    Dominance, Golden Blade, Breastplate of Valor, Toxic Blade, Musashi''s Dual Swords,
    Demon Blade, Genji''s Guard, The Crusher, Qin''s Blade, Runeforged Hammer, Berserker''s
    Shield, Damaru, Rage, Avenging Blade, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.45
      pick: 0.79
      fit: 0.48
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.49
      pick: 0.91
      fit: 0.08
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.48
      pick: 0.78
      fit: 0.47
    Barbed Carver:
      total: 0.53
      efficiency: 0.39
      win: 0.75
      pick: 0.31
      fit: 0.25
    Arondight:
      total: 0.45
      efficiency: 0.5
      win: 0.49
      pick: 0.0
      fit: 0.37
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.48
      pick: 1.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  - Tekko-Kagi
  flex_slots:
  - Tyrfing
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
    Underrated for this god: Riptalon, Lernaean Bow, Tekko-Kagi, Tyrfing, The Reaper,
    Silverbranch Bow, Deathbringer, Golden Blade, Dominance, Demon Blade, The Crusher,
    Musashi''s Dual Swords, Toxic Blade, Arondight, Pendulum Blade, Damaru, Rage,
    Runeforged Hammer, Qin''s Blade, Berserker''s Shield, Avenging Blade, Sun Beam
    Bow, Bloodforge.'
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.52
      win: 0.49
      pick: 0.0
      fit: 0.51
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.45
      pick: 0.79
      fit: 0.42
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.49
      pick: 0.0
      fit: 0.58
    The Reaper:
      total: 0.47
      efficiency: 0.55
      win: 0.49
      pick: 0.0
      fit: 0.41
    Riptalon:
      total: 0.48
      efficiency: 0.51
      win: 0.49
      pick: 0.0
      fit: 0.55
    Tekko-Kagi:
      total: 0.48
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.56
  starter: *id001
---
