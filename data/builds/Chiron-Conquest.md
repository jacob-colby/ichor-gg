---
type: smite-build
god: Chiron
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Heroic Tutor
  aspect_pick_rate: 0.34
  aspect_win_rate: 0.4
  slot_order:
  - name: Transcendence
    pick_rate: 0.45
    win_rate: 0.55
    alternates:
    - name: Tyrfing
      pick_rate: 0.16
      win_rate: 0.57
    - name: Daybreak Gavel
      pick_rate: 0.14
      win_rate: 0.5
  - name: Jotunn's Revenge
    pick_rate: 0.43
    win_rate: 0.58
    alternates:
    - name: Avenging Blade
      pick_rate: 0.09
      win_rate: 0.5
    - name: Toxic Blade
      pick_rate: 0.07
      win_rate: 1.0
  - name: The Crusher
    pick_rate: 0.23
    win_rate: 0.7
    alternates:
    - name: Oath-Sworn Spear
      pick_rate: 0.11
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.75
  - name: Heartseeker
    pick_rate: 0.17
    win_rate: 0.43
    alternates:
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.4
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.25
  - name: Titan's Bane
    pick_rate: 0.29
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 1.0
    - name: Survivor's Sash
      pick_rate: 0.09
      win_rate: 1.0
  - name: Hunter's Bow
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Axe
      pick_rate: 0.12
      win_rate: 0.67
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.25
    win_rate: 0.64
  - name: Hunter's Cowl
    pick_rate: 0.2
    win_rate: 0.44
  - name: Bluestone Pendant
    pick_rate: 0.14
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/chiron/
  last_verified: '2026-08-26'
  god_win_rate: 0.5454545454545454
  god_matches_won: 24
  god_matches_played: 44
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
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tyrfing
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, Tekko-Kagi, Lernaean Bow, The Reaper, Silverbranch
    Bow, Hydra''s Lament, Deathbringer, Golden Blade, Dominance, Demon Blade, Musashi''s
    Dual Swords, Arondight, Pendulum Blade, Avatar''s Parashu, Damaru, Rage, Runeforged
    Hammer, Qin''s Blade, Berserker''s Shield, Barbed Carver, Sun Beam Bow, Bloodforge,
    Avenging Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.47
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.44
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.57
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.56
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.44
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Tyrfing
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Toxic
    Blade, Hydra''s Lament, Lernaean Bow, The Reaper, Tekko-Kagi, Riptalon, Silverbranch
    Bow, Dominance, Deathbringer, Golden Blade, Arondight, Musashi''s Dual Swords,
    Demon Blade, Runeforged Hammer, Pendulum Blade, Avatar''s Parashu, Damaru, Rage,
    Qin''s Blade, Barbed Carver, Berserker''s Shield, Breastplate of Valor, Genji''s
    Guard, Avenging Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.32
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.44
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.55
      pick: 0.45
      fit: 0.24
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.48
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Demon Blade
  - The Crusher
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, The Reaper, Silverbranch Bow, Tekko-Kagi, Lernaean
    Bow, Hydra''s Lament, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s
    Dual Swords, Arondight, Damaru, Rage, Pendulum Blade, Avatar''s Parashu, Qin''s
    Blade, Runeforged Hammer, Berserker''s Shield, Barbed Carver, Sun Beam Bow, Bloodforge,
    Avenging Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.46
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.48
      efficiency: 0.46
      win: 0.57
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.49
      efficiency: 0.38
      win: 0.57
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.42
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Silverbranch Bow
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Toxic Blade, The Reaper, Riptalon, Silverbranch Bow, Tekko-Kagi, Hydra''s
    Lament, Lernaean Bow, Deathbringer, Pendulum Blade, Dominance, Golden Blade, Arondight,
    Avatar''s Parashu, Musashi''s Dual Swords, Demon Blade, Runeforged Hammer, Damaru,
    Rage, Qin''s Blade, Berserker''s Shield, Breastplate of Valor, Barbed Carver,
    Avenging Blade, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.42
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.46
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.39
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.42
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - The Crusher
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Shifter''s Shield, Amanita Charm, Berserker''s Shield,
    Riptalon, The Reaper, Shield of the Phoenix, Kinetic Cuirass, Genji''s Guard,
    Freya''s Tears, Breastplate of Valor, Runeforged Hammer, Golden Blade, Yogi''s
    Necklace, Shield Splitter, Lernaean Bow, Pharaoh''s Curse, Hydra''s Lament, Chandra''s
    Grace, Silverbranch Bow, Shogun''s Ofuda, Phoenix Feather, Eye of the Storm, Tekko-Kagi,
    Erosion, Eye of Providence, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.1
      fit: 0.44
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.3
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.75
      pick: 0.14
      fit: 0.32
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - Silverbranch Bow
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Toxic Blade, Riptalon, The Reaper, Tekko-Kagi, Silverbranch Bow,
    Lernaean Bow, Hydra''s Lament, Deathbringer, Pendulum Blade, Avatar''s Parashu,
    Golden Blade, Dominance, Demon Blade, Musashi''s Dual Swords, Avenging Blade,
    Arondight, Runeforged Hammer, Damaru, Rage, Qin''s Blade, Berserker''s Shield,
    Screeching Gargoyle.'
  slot_scores:
    Toxic Blade:
      total: 0.69
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.56
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.53
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.63
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.56
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, Silverbranch Bow, Lernaean Bow, Tekko-Kagi, The
    Reaper, Golden Blade, Hydra''s Lament, Deathbringer, Dominance, Qin''s Blade,
    Demon Blade, Musashi''s Dual Swords, Arondight, Sun Beam Bow, Pendulum Blade,
    Runeforged Hammer, Avatar''s Parashu, Berserker''s Shield, Damaru, Rage, Dagger
    of Frenzy, Barbed Carver, Avenging Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.69
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.52
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.35
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.6
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.52
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Riptalon
  - The Crusher
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Toxic Blade, Hydra''s Lament, Riptalon,
    Silverbranch Bow, Lernaean Bow, The Reaper, Tekko-Kagi, Arondight, Pendulum Blade,
    Deathbringer, Dominance, Golden Blade, Breastplate of Valor, Musashi''s Dual Swords,
    Genji''s Guard, Demon Blade, Qin''s Blade, Runeforged Hammer, Avatar''s Parashu,
    Berserker''s Shield, Damaru, Rage, Avenging Blade, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.36
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.49
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.46
    Arondight:
      total: 0.49
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.43
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.31
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
    Bow, Hydra''s Lament, Deathbringer, Golden Blade, Dominance, Demon Blade, Toxic
    Blade, Musashi''s Dual Swords, Arondight, Pendulum Blade, Avatar''s Parashu, Damaru,
    Rage, Runeforged Hammer, Qin''s Blade, Berserker''s Shield, Avenging Blade, Barbed
    Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.44
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.56
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.47
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, The Reaper, Hydra''s Lament, Deathbringer, Riptalon, Tekko-Kagi,
    Silverbranch Bow, Lernaean Bow, Musashi''s Dual Swords, Pendulum Blade, Arondight,
    Damaru, Rage, Avatar''s Parashu, Demon Blade, Golden Blade, Dominance, Runeforged
    Hammer, Barbed Carver, Bloodforge, Qin''s Blade, Shield Splitter, Breastplate
    of Valor, Avenging Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.36
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.53
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.55
      pick: 0.45
      fit: 0.2
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.51
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: mana-stack
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  flex_slots:
  - The Reaper
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Toxic
    Blade, Hydra''s Lament, The Reaper, Deathbringer, Lernaean Bow, Tekko-Kagi, Riptalon,
    Arondight, Musashi''s Dual Swords, Dominance, Silverbranch Bow, Pendulum Blade,
    Runeforged Hammer, Golden Blade, Avatar''s Parashu, Damaru, Rage, Demon Blade,
    Barbed Carver, Breastplate of Valor, Bloodforge, Genji''s Guard, Shield Splitter,
    Avenging Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.64
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.22
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.5
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.55
      pick: 0.45
      fit: 0.27
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.47
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.4
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.43
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Demon Blade
  - The Crusher
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, The Reaper, Silverbranch Bow, Tekko-Kagi, Lernaean
    Bow, Hydra''s Lament, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s
    Dual Swords, Arondight, Damaru, Rage, Pendulum Blade, Avatar''s Parashu, Qin''s
    Blade, Runeforged Hammer, Berserker''s Shield, Barbed Carver, Sun Beam Bow, Bloodforge,
    Avenging Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.46
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.48
      efficiency: 0.46
      win: 0.57
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.49
      efficiency: 0.38
      win: 0.57
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.42
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.42
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Toxic Blade, The Reaper, Hydra''s Lament, Riptalon, Tekko-Kagi, Silverbranch
    Bow, Deathbringer, Pendulum Blade, Lernaean Bow, Arondight, Avatar''s Parashu,
    Musashi''s Dual Swords, Runeforged Hammer, Golden Blade, Dominance, Damaru, Rage,
    Demon Blade, Barbed Carver, Breastplate of Valor, Genji''s Guard, Bloodforge,
    Avenging Blade, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.33
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.53
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.55
      pick: 0.45
      fit: 0.15
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.4
    The Reaper:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.48
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shifter''s Shield, The Reaper, Berserker''s Shield, Shield
    of the Phoenix, Riptalon, Kinetic Cuirass, Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Erosion, Yogi''s Necklace, Shield Splitter, Pharaoh''s
    Curse, Eye of the Storm, Umbral Link, Golden Blade, Phoenix Feather, Chandra''s
    Grace, Hydra''s Lament, Shogun''s Ofuda, Eye of Providence, Void Shield, Stampede,
    Draconic Scale, Daybreak Gavel, Avenging Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.1
      fit: 0.37
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.34
    The Reaper:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.75
      pick: 0.14
      fit: 0.37
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.36
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Toxic Blade, The Reaper, Riptalon, Tekko-Kagi, Silverbranch Bow,
    Hydra''s Lament, Pendulum Blade, Avatar''s Parashu, Deathbringer, Lernaean Bow,
    Musashi''s Dual Swords, Arondight, Avenging Blade, Damaru, Rage, Golden Blade,
    Runeforged Hammer, Dominance, Demon Blade, Barbed Carver, Screeching Gargoyle,
    Bloodforge.'
  slot_scores:
    Toxic Blade:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.48
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.62
    The Reaper:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.62
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.59
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.63
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.63
      fit: 0.63
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, Silverbranch Bow, Lernaean Bow, Tekko-Kagi, The
    Reaper, Golden Blade, Hydra''s Lament, Deathbringer, Dominance, Qin''s Blade,
    Demon Blade, Musashi''s Dual Swords, Arondight, Sun Beam Bow, Pendulum Blade,
    Runeforged Hammer, Avatar''s Parashu, Berserker''s Shield, Damaru, Rage, Dagger
    of Frenzy, Barbed Carver, Avenging Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.69
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.52
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.35
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.6
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.52
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.36
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Arondight
  - The Crusher
  flex_slots:
  - The Reaper
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Toxic Blade, Hydra''s Lament, The
    Reaper, Arondight, Pendulum Blade, Riptalon, Deathbringer, Silverbranch Bow, Lernaean
    Bow, Tekko-Kagi, Breastplate of Valor, Musashi''s Dual Swords, Genji''s Guard,
    Runeforged Hammer, Avatar''s Parashu, Golden Blade, Damaru, Rage, Dominance, Demon
    Blade, Eye of Erebus, Barbed Carver, Avenging Blade, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.65
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.26
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.57
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.52
    The Reaper:
      total: 0.5
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.33
    Arondight:
      total: 0.49
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.7
      pick: 0.36
      fit: 0.35
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Deathbringer
  - Heartseeker
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
    Tekko-Kagi, Silverbranch Bow, Lernaean Bow, Musashi''s Dual Swords, Pendulum Blade,
    Arondight, Damaru, Rage, Avatar''s Parashu, Demon Blade, Golden Blade, Dominance,
    Runeforged Hammer, Toxic Blade, Barbed Carver, Avenging Blade, Bloodforge, Qin''s
    Blade, Shield Splitter, Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.58
      pick: 0.59
      fit: 0.53
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.55
      pick: 0.45
      fit: 0.2
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.53
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.49
    Heartseeker:
      total: 0.46
      efficiency: 0.47
      win: 0.43
      pick: 0.28
      fit: 0.61
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
