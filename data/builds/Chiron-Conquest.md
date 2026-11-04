---
type: smite-build
god: Chiron
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Transcendence
    pick_rate: 1.0
    win_rate: 0.75
  - name: Jotunn's Revenge
    pick_rate: 1.0
    win_rate: 0.75
  - name: The Crusher
    pick_rate: 0.67
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.33
      win_rate: 1.0
  - name: Heartseeker
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: The Crusher
      pick_rate: 0.33
      win_rate: 1.0
    - name: Avatar's Parashu
      pick_rate: 0.33
      win_rate: 0.0
  - name: Titan's Bane
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Avatar's Parashu
      pick_rate: 0.33
      win_rate: 1.0
    - name: Heartseeker
      pick_rate: 0.33
      win_rate: 0.0
  - name: Lucerne Hammer
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Titan's Bane
      pick_rate: 0.5
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.5
    win_rate: 1.0
  - name: Bluestone Pendant
    pick_rate: 0.25
    win_rate: 1.0
  - name: Pendulum of the Ages
    pick_rate: 0.25
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/chiron/
  last_verified: '2026-11-04'
  god_win_rate: 0.75
  god_matches_won: 3
  god_matches_played: 4
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Tyrfing
  - Lernaean Bow
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
    this god: Tekko-Kagi, The Reaper, Tyrfing, Lernaean Bow, Silverbranch Bow, Hydra''s
    Lament, Riptalon, Dominance, Golden Blade, Toxic Blade, Arondight, Deathbringer,
    Musashi''s Dual Swords, Demon Blade, Rage, Bloodforge, Pendulum Blade, Qin''s
    Blade, Runeforged Hammer, Berserker''s Shield, Avenging Blade, Barbed Carver,
    Sun Beam Bow, Shield Splitter.'
  slot_scores:
    Lernaean Bow:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.0
      fit: 0.57
    The Reaper:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.58
    Heartseeker:
      total: 0.71
      efficiency: 0.43
      win: 1.0
      pick: 0.55
      fit: 0.54
    Titan's Bane:
      total: 0.74
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.44
  community_ordered:
  - Heartseeker
  - Titan's Bane
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Tekko-Kagi,
    Hydra''s Lament, The Reaper, Tyrfing, Lernaean Bow, Dominance, Silverbranch Bow,
    Arondight, Golden Blade, Riptalon, Deathbringer, Musashi''s Dual Swords, Runeforged
    Hammer, Toxic Blade, Bloodforge, Rage, Demon Blade, Pendulum Blade, Avenging Blade,
    Berserker''s Shield, Qin''s Blade, Shield Splitter, Eye of the Storm, Genji''s
    Guard.'
  slot_scores:
    Transcendence:
      total: 0.61
      efficiency: 0.53
      win: 0.75
      pick: 1.0
      fit: 0.24
    Hydra's Lament:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.7
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.35
    Tekko-Kagi:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.45
    Heartseeker:
      total: 0.71
      efficiency: 0.43
      win: 1.0
      pick: 0.55
      fit: 0.55
    Titan's Bane:
      total: 0.73
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.39
  community_ordered:
  - Transcendence
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Musashi's Dual Swords
  - The Reaper
  - Tekko-Kagi
  - Demon Blade
  - Titan's Bane
  - Deathbringer
  flex_slots:
  - Musashi's Dual Swords
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Tekko-Kagi, The Reaper, Tyrfing, Silverbranch Bow, Lernaean Bow, Hydra''s
    Lament, Riptalon, Dominance, Golden Blade, Deathbringer, Toxic Blade, Musashi''s
    Dual Swords, Arondight, Demon Blade, Rage, Bloodforge, Pendulum Blade, Qin''s
    Blade, Berserker''s Shield, Runeforged Hammer, Avenging Blade, Sun Beam Bow, Barbed
    Carver, Damaru.'
  slot_scores:
    Musashi's Dual Swords:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.41
    Tekko-Kagi:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.54
    Demon Blade:
      total: 0.67
      efficiency: 0.36
      win: 1.0
      pick: 0.0
      fit: 0.64
    Titan's Bane:
      total: 0.74
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.42
    Deathbringer:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - Silverbranch Bow
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Silverbranch Bow
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
    god: Tekko-Kagi, The Reaper, Hydra''s Lament, Silverbranch Bow, Tyrfing, Lernaean
    Bow, Riptalon, Arondight, Dominance, Toxic Blade, Golden Blade, Pendulum Blade,
    Deathbringer, Musashi''s Dual Swords, Runeforged Hammer, Bloodforge, Rage, Demon
    Blade, Berserker''s Shield, Qin''s Blade, Damaru, Avenging Blade, Genji''s Guard,
    Shield Splitter.'
  slot_scores:
    Hydra's Lament:
      total: 0.7
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.36
    The Reaper:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.39
    Tekko-Kagi:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.5
    Silverbranch Bow:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.71
      efficiency: 0.43
      win: 1.0
      pick: 0.55
      fit: 0.53
    Titan's Bane:
      total: 0.74
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.43
  community_ordered:
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - The Reaper
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, The Reaper, Shield of the Phoenix,
    Genji''s Guard, Riptalon, Kinetic Cuirass, Shield Splitter, Yogi''s Necklace,
    Tekko-Kagi, Golden Blade, Runeforged Hammer, Phoenix Feather, Breastplate of Valor,
    Bloodforge, Freya''s Tears, Hydra''s Lament, Chandra''s Grace, Tyrfing, Toxic
    Blade, Oni Hunter''s Garb, Lernaean Bow, Pharaoh''s Curse, Silverbranch Bow, Regrowth
    Striders, Shogun''s Ofuda, Midgardian Mail, Erosion.'
  slot_scores:
    Genji's Guard:
      total: 0.72
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.16
    Berserker's Shield:
      total: 0.77
      efficiency: 0.74
      win: 1.0
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.59
    Titan's Bane:
      total: 0.72
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.33
    Amanita Charm:
      total: 0.77
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - Silverbranch Bow
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Jotunn's Revenge
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
    for this god: Tekko-Kagi, The Reaper, Silverbranch Bow, Riptalon, Tyrfing, Lernaean
    Bow, Toxic Blade, Hydra''s Lament, Avenging Blade, Dominance, Golden Blade, Pendulum
    Blade, Arondight, Deathbringer, Musashi''s Dual Swords, The Executioner, Demon
    Blade, Oath-Sworn Spear, Rage, Bloodforge, Runeforged Hammer, Qin''s Blade, Berserker''s
    Shield, Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.67
      win: 0.75
      pick: 1.0
      fit: 0.53
    The Reaper:
      total: 0.72
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.52
    Tekko-Kagi:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.64
    Silverbranch Bow:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.56
    Heartseeker:
      total: 0.73
      efficiency: 0.43
      win: 1.0
      pick: 0.55
      fit: 0.65
    Titan's Bane:
      total: 0.76
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.55
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Riptalon
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Tekko-Kagi, Tyrfing, Silverbranch Bow, Riptalon, The Reaper, Lernaean
    Bow, Golden Blade, Hydra''s Lament, Toxic Blade, Dominance, Qin''s Blade, Arondight,
    Deathbringer, Musashi''s Dual Swords, Demon Blade, Berserker''s Shield, Sun Beam
    Bow, Rage, Bloodforge, Runeforged Hammer, Pendulum Blade, Avenging Blade, Dagger
    of Frenzy, Damaru.'
  slot_scores:
    Tyrfing:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.7
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.34
    Tekko-Kagi:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.49
    Riptalon:
      total: 0.7
      efficiency: 0.46
      win: 1.0
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.52
    Titan's Bane:
      total: 0.73
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.36
  community_ordered:
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Tekko-Kagi
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Arondight
  - Heartseeker
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Tekko-Kagi, Arondight,
    The Reaper, Silverbranch Bow, Tyrfing, Lernaean Bow, Riptalon, Pendulum Blade,
    Dominance, Damaru, Toxic Blade, Golden Blade, Genji''s Guard, Deathbringer, Musashi''s
    Dual Swords, Berserker''s Shield, Breastplate of Valor, Qin''s Blade, Bloodforge,
    Runeforged Hammer, Demon Blade, Rage, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.67
      win: 0.75
      pick: 1.0
      fit: 0.49
    Hydra's Lament:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.46
    Arondight:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.0
      fit: 0.36
    Tekko-Kagi:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.39
    Heartseeker:
      total: 0.69
      efficiency: 0.43
      win: 1.0
      pick: 0.55
      fit: 0.41
    Titan's Bane:
      total: 0.72
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.31
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Lernaean Bow
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
    Underrated for this god: Tekko-Kagi, The Reaper, Tyrfing, Lernaean Bow, Silverbranch
    Bow, Hydra''s Lament, Riptalon, Dominance, Golden Blade, Toxic Blade, Arondight,
    Deathbringer, Musashi''s Dual Swords, Demon Blade, Rage, Bloodforge, Pendulum
    Blade, Qin''s Blade, Runeforged Hammer, Berserker''s Shield, Avenging Blade, Barbed
    Carver, Sun Beam Bow, Shield Splitter.'
  slot_scores:
    Lernaean Bow:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.67
      win: 0.75
      pick: 1.0
      fit: 0.44
    Tyrfing:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.0
      fit: 0.57
    The Reaper:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.58
    Titan's Bane:
      total: 0.74
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.44
  community_ordered:
  - Jotunn's Revenge
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Avatar's Parashu
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
    this god: The Reaper, Tekko-Kagi, Hydra''s Lament, Tyrfing, Deathbringer, Musashi''s
    Dual Swords, Arondight, Silverbranch Bow, Lernaean Bow, Riptalon, Rage, Pendulum
    Blade, Bloodforge, Dominance, Golden Blade, Toxic Blade, Runeforged Hammer, Demon
    Blade, Avenging Blade, Barbed Carver, Shield Splitter, Eye of the Storm, Damaru,
    Genji''s Guard.'
  slot_scores:
    Hydra's Lament:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.53
    Tekko-Kagi:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.48
    Heartseeker:
      total: 0.72
      efficiency: 0.43
      win: 1.0
      pick: 0.55
      fit: 0.61
    Avatar's Parashu:
      total: 0.7
      efficiency: 0.44
      win: 1.0
      pick: 0.71
      fit: 0.41
    Titan's Bane:
      total: 0.75
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.51
  community_ordered:
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: mana-stack
  slot_order:
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - Heartseeker
  - Titan's Bane
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, The Reaper, Tekko-Kagi, Arondight, Tyrfing, Lernaean Bow, Dominance, Deathbringer,
    Musashi''s Dual Swords, Silverbranch Bow, Bloodforge, Rage, Runeforged Hammer,
    Golden Blade, Pendulum Blade, Riptalon, Avenging Blade, Shield Splitter, Eye of
    the Storm, Genji''s Guard, Barbed Carver, Toxic Blade, Demon Blade, Damaru.'
  slot_scores:
    Transcendence:
      total: 0.61
      efficiency: 0.53
      win: 0.75
      pick: 1.0
      fit: 0.27
    Hydra's Lament:
      total: 0.72
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.47
    The Reaper:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.4
    Tekko-Kagi:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.37
    Heartseeker:
      total: 0.72
      efficiency: 0.43
      win: 1.0
      pick: 0.55
      fit: 0.6
    Titan's Bane:
      total: 0.74
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.43
  community_ordered:
  - Transcendence
  - Heartseeker
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: crit
  slot_order:
  - Musashi's Dual Swords
  - The Reaper
  - Tekko-Kagi
  - Demon Blade
  - Titan's Bane
  - Deathbringer
  flex_slots:
  - Musashi's Dual Swords
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Tekko-Kagi, The Reaper, Tyrfing, Silverbranch Bow, Lernaean Bow, Hydra''s
    Lament, Riptalon, Dominance, Golden Blade, Deathbringer, Toxic Blade, Musashi''s
    Dual Swords, Arondight, Demon Blade, Rage, Bloodforge, Pendulum Blade, Qin''s
    Blade, Berserker''s Shield, Runeforged Hammer, Avenging Blade, Sun Beam Bow, Barbed
    Carver, Damaru.'
  slot_scores:
    Musashi's Dual Swords:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.41
    Tekko-Kagi:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.54
    Demon Blade:
      total: 0.67
      efficiency: 0.36
      win: 1.0
      pick: 0.0
      fit: 0.64
    Titan's Bane:
      total: 0.74
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.42
    Deathbringer:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Jotunn's Revenge
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Reaper, Tekko-Kagi, Hydra''s Lament, Arondight, Silverbranch Bow, Tyrfing,
    Pendulum Blade, Lernaean Bow, Riptalon, Deathbringer, Musashi''s Dual Swords,
    Toxic Blade, Dominance, Rage, Bloodforge, Runeforged Hammer, Golden Blade, Damaru,
    Avenging Blade, Genji''s Guard, Shield Splitter, Eye of the Storm, Barbed Carver,
    Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.67
      win: 0.75
      pick: 1.0
      fit: 0.53
    Hydra's Lament:
      total: 0.7
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.4
    The Reaper:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.45
    Tekko-Kagi:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.72
      efficiency: 0.43
      win: 1.0
      pick: 0.55
      fit: 0.58
    Titan's Bane:
      total: 0.75
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.48
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - The Reaper
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, The Reaper, Shield of the Phoenix,
    Genji''s Guard, Kinetic Cuirass, Shield Splitter, Yogi''s Necklace, Runeforged
    Hammer, Phoenix Feather, Riptalon, Breastplate of Valor, Erosion, Freya''s Tears,
    Bloodforge, Hydra''s Lament, Chandra''s Grace, Oni Hunter''s Garb, Tekko-Kagi,
    Golden Blade, Pharaoh''s Curse, Umbral Link, Regrowth Striders, Eye of Providence,
    Midgardian Mail, Shogun''s Ofuda, Stampede, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.72
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.19
    Berserker's Shield:
      total: 0.75
      efficiency: 0.74
      win: 1.0
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.72
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.47
    The Reaper:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.63
    Titan's Bane:
      total: 0.73
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.36
    Amanita Charm:
      total: 0.79
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - Avatar's Parashu
  - Jotunn's Revenge
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Tekko-Kagi, Silverbranch Bow, Hydra''s Lament, Riptalon,
    Avenging Blade, Pendulum Blade, Toxic Blade, Tyrfing, Arondight, Lernaean Bow,
    Deathbringer, Musashi''s Dual Swords, Rage, Oath-Sworn Spear, Dominance, Bloodforge,
    Golden Blade, Runeforged Hammer, Demon Blade, Barbed Carver, Shield Splitter,
    The Executioner, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.67
      win: 0.75
      pick: 1.0
      fit: 0.62
    The Reaper:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.62
    Tekko-Kagi:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.58
    Heartseeker:
      total: 0.74
      efficiency: 0.43
      win: 1.0
      pick: 0.55
      fit: 0.73
    Avatar's Parashu:
      total: 0.72
      efficiency: 0.44
      win: 1.0
      pick: 0.71
      fit: 0.53
    Titan's Bane:
      total: 0.77
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.63
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Riptalon
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Tekko-Kagi, Tyrfing, Silverbranch Bow, Riptalon, The Reaper, Lernaean
    Bow, Golden Blade, Hydra''s Lament, Toxic Blade, Dominance, Qin''s Blade, Arondight,
    Deathbringer, Musashi''s Dual Swords, Demon Blade, Berserker''s Shield, Sun Beam
    Bow, Rage, Bloodforge, Runeforged Hammer, Pendulum Blade, Avenging Blade, Dagger
    of Frenzy, Damaru.'
  slot_scores:
    Tyrfing:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.7
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.34
    Tekko-Kagi:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.49
    Riptalon:
      total: 0.7
      efficiency: 0.46
      win: 1.0
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.52
    Titan's Bane:
      total: 0.73
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.36
  community_ordered:
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - The Reaper
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - The Reaper
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Arondight, The Reaper,
    Tekko-Kagi, Pendulum Blade, Damaru, Silverbranch Bow, Tyrfing, Genji''s Guard,
    Lernaean Bow, Deathbringer, Riptalon, Musashi''s Dual Swords, Breastplate of Valor,
    Dominance, Rage, Bloodforge, Chandra''s Grace, Toxic Blade, Runeforged Hammer,
    Golden Blade, Avenging Blade, Demon Blade, Shield Splitter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.67
      win: 0.75
      pick: 1.0
      fit: 0.57
    Hydra's Lament:
      total: 0.72
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.52
    Arondight:
      total: 0.7
      efficiency: 0.54
      win: 1.0
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.7
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.33
    Heartseeker:
      total: 0.7
      efficiency: 0.43
      win: 1.0
      pick: 0.55
      fit: 0.45
    Titan's Bane:
      total: 0.73
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.35
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: model
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Reaper, Tekko-Kagi, Hydra''s Lament, Tyrfing, Deathbringer,
    Musashi''s Dual Swords, Arondight, Silverbranch Bow, Lernaean Bow, Riptalon, Rage,
    Pendulum Blade, Bloodforge, Dominance, Golden Blade, Toxic Blade, Runeforged Hammer,
    Demon Blade, Avenging Blade, Barbed Carver, Shield Splitter, Eye of the Storm,
    Damaru, Genji''s Guard.'
  slot_scores:
    Transcendence:
      total: 0.6
      efficiency: 0.53
      win: 0.75
      pick: 1.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.67
      win: 0.75
      pick: 1.0
      fit: 0.53
    Hydra's Lament:
      total: 0.71
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.53
    Tekko-Kagi:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.48
    Titan's Bane:
      total: 0.75
      efficiency: 0.54
      win: 1.0
      pick: 0.71
      fit: 0.51
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
