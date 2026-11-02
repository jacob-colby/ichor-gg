---
type: smite-build
god: Pele
mode: Conquest
builds:
- source: community
  aspect: Aspect of Obsidian
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.59
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.43
    win_rate: 0.6
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.24
      win_rate: 0.5
    - name: Barbed Carver
      pick_rate: 0.16
      win_rate: 0.62
  - name: Barbed Carver
    pick_rate: 0.26
    win_rate: 0.53
    alternates:
    - name: The Reaper
      pick_rate: 0.2
      win_rate: 0.58
    - name: Jotunn's Revenge
      pick_rate: 0.15
      win_rate: 0.58
  - name: The Reaper
    pick_rate: 0.17
    win_rate: 0.65
    alternates:
    - name: The Crusher
      pick_rate: 0.15
      win_rate: 0.49
    - name: Barbed Carver
      pick_rate: 0.15
      win_rate: 0.52
  - name: Heartseeker
    pick_rate: 0.25
    win_rate: 0.55
    alternates:
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.59
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.5
  - name: Titan's Bane
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.19
      win_rate: 0.61
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.63
  - name: Skeggox
    pick_rate: 0.08
    win_rate: 0.59
    alternates:
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.72
    - name: Avatar's Parashu
      pick_rate: 0.07
      win_rate: 0.71
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.48
    win_rate: 0.64
  - name: Leather Cowl
    pick_rate: 0.21
    win_rate: 0.41
  - name: Bluestone Brooch
    pick_rate: 0.08
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/pele/
  last_verified: '2026-11-02'
  god_win_rate: 0.5789473684210527
  god_matches_won: 341
  god_matches_played: 589
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Hydra's Lament
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
    this god: Hydra''s Lament, Pendulum Blade, Arondight, Tekko-Kagi, Tyrfing, Transcendence,
    Golden Blade, Runeforged Hammer, Silverbranch Bow, Avenging Blade, Eye of the
    Storm, Shield Splitter, Toxic Blade, Dominance, Lernaean Bow, Bloodforge, Riptalon,
    Oath-Sworn Spear, Genji''s Guard, Damaru, Breastplate of Valor, Rage, Chandra''s
    Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.5
      pick: 0.24
      fit: 1.0
    Transcendence:
      total: 0.51
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.56
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.77
    The Reaper:
      total: 0.59
      efficiency: 0.47
      win: 0.65
      pick: 0.26
      fit: 0.78
    Titan's Bane:
      total: 0.59
      efficiency: 0.51
      win: 0.6
      pick: 0.17
      fit: 0.88
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.39
      win: 0.71
      pick: 0.22
      fit: 0.78
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Titan's Bane
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Titan's Bane
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Arondight, Transcendence, Pendulum Blade, Tekko-Kagi, Tyrfing, Runeforged
    Hammer, Dominance, Genji''s Guard, Avenging Blade, Eye of the Storm, Shield Splitter,
    Golden Blade, Breastplate of Valor, Lernaean Bow, Chandra''s Grace, Silverbranch
    Bow, Bloodforge, Damaru, Toxic Blade, Oath-Sworn Spear, Yogi''s Necklace, Riptalon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.24
      fit: 0.71
    Hydra's Lament:
      total: 0.54
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.54
      efficiency: 0.47
      win: 0.65
      pick: 0.26
      fit: 0.47
    Titan's Bane:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.17
      fit: 0.57
    Heartseeker:
      total: 0.53
      efficiency: 0.41
      win: 0.55
      pick: 0.42
      fit: 0.77
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.39
      win: 0.71
      pick: 0.22
      fit: 0.47
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Titan's Bane
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Titan's Bane
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, Pendulum Blade, Arondight, Tekko-Kagi, Tyrfing, Silverbranch
    Bow, Transcendence, Runeforged Hammer, Toxic Blade, Genji''s Guard, Damaru, Avenging
    Blade, Eye of the Storm, Breastplate of Valor, Riptalon, Shield Splitter, Golden
    Blade, Chandra''s Grace, Dominance, Lernaean Bow, Bloodforge, Oath-Sworn Spear,
    Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.24
      fit: 0.78
    Transcendence:
      total: 0.47
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.56
      efficiency: 0.47
      win: 0.65
      pick: 0.26
      fit: 0.56
    Titan's Bane:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.17
      fit: 0.66
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.39
      win: 0.71
      pick: 0.22
      fit: 0.56
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - The Reaper
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Genji''s Guard, Shield Splitter, Phoenix Feather, Runeforged Hammer, Yogi''s
    Necklace, Freya''s Tears, Breastplate of Valor, Chandra''s Grace, Erosion, Hydra''s
    Lament, Eye of Providence, Oni Hunter''s Garb, Draconic Scale, Midgardian Mail,
    Glorious Pridwen, Shifter''s Shield, Avenging Blade, Regrowth Striders, Leviathan''s
    Hide, Wyrmskin Hide, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.27
    Berserker's Shield:
      total: 0.54
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.62
    The Reaper:
      total: 0.57
      efficiency: 0.47
      win: 0.65
      pick: 0.26
      fit: 0.67
    Shield Splitter:
      total: 0.54
      efficiency: 0.54
      win: 0.59
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.61
      efficiency: 0.62
      win: 0.59
      pick: 0.0
      fit: 0.82
  community_ordered:
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - Titan's Bane
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Tekko-Kagi
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Pendulum Blade, Tekko-Kagi, Hydra''s Lament, Silverbranch Bow, Avenging
    Blade, Arondight, Toxic Blade, Tyrfing, Riptalon, Oath-Sworn Spear, Transcendence,
    Runeforged Hammer, Golden Blade, Eye of the Storm, Shield Splitter, Screeching
    Gargoyle, Dominance, Lernaean Bow, Bloodforge, Genji''s Guard, Damaru, Breastplate
    of Valor, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.5
      pick: 0.24
      fit: 1.0
    The Reaper:
      total: 0.6
      efficiency: 0.47
      win: 0.65
      pick: 0.26
      fit: 0.85
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.44
      win: 0.59
      pick: 0.0
      fit: 0.85
    Titan's Bane:
      total: 0.6
      efficiency: 0.51
      win: 0.6
      pick: 0.17
      fit: 0.95
    Heartseeker:
      total: 0.56
      efficiency: 0.41
      win: 0.55
      pick: 0.42
      fit: 1.0
    Avatar's Parashu:
      total: 0.6
      efficiency: 0.39
      win: 0.71
      pick: 0.22
      fit: 0.85
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Titan's Bane
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Riptalon
  - Jotunn's Revenge
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
    this god: Tyrfing, Tekko-Kagi, Silverbranch Bow, Riptalon, Golden Blade, Toxic
    Blade, Lernaean Bow, Hydra''s Lament, Dominance, Qin''s Blade, Arondight, Sun
    Beam Bow, Berserker''s Shield, Pendulum Blade, Dagger of Frenzy, Bloodforge, Transcendence,
    Runeforged Hammer, Hastened Fatalis, Vital Amplifier, Avenging Blade, Eye of the
    Storm, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.24
      fit: 0.42
    Tyrfing:
      total: 0.54
      efficiency: 0.46
      win: 0.59
      pick: 0.0
      fit: 0.74
    The Reaper:
      total: 0.55
      efficiency: 0.53
      win: 0.65
      pick: 0.26
      fit: 0.41
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.6
    Riptalon:
      total: 0.54
      efficiency: 0.45
      win: 0.59
      pick: 0.0
      fit: 0.74
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.5
      win: 0.59
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - The Reaper
  - Pendulum Blade
  - Titan's Bane
  flex_slots:
  - Titan's Bane
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Arondight, Pendulum
    Blade, Genji''s Guard, Damaru, Breastplate of Valor, Chandra''s Grace, Tyrfing,
    Tekko-Kagi, Screeching Gargoyle, Eye of Erebus, Transcendence, Freya''s Tears,
    Runeforged Hammer, Silverbranch Bow, Shield of the Phoenix, Toxic Blade, Avenging
    Blade, Eye of the Storm, Golden Blade, Shield Splitter, Gladiator''s Shield, Dominance,
    Riptalon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.24
      fit: 0.85
    Hydra's Lament:
      total: 0.56
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.75
    Arondight:
      total: 0.54
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.65
    The Reaper:
      total: 0.52
      efficiency: 0.47
      win: 0.65
      pick: 0.26
      fit: 0.35
    Pendulum Blade:
      total: 0.53
      efficiency: 0.39
      win: 0.59
      pick: 0.0
      fit: 0.85
    Titan's Bane:
      total: 0.52
      efficiency: 0.51
      win: 0.6
      pick: 0.17
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Crusher
  - Pendulum Blade
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
    Underrated for this god: Hydra''s Lament, Pendulum Blade, Arondight, Tekko-Kagi,
    Tyrfing, Transcendence, Golden Blade, Runeforged Hammer, Silverbranch Bow, Avenging
    Blade, Eye of the Storm, Shield Splitter, Toxic Blade, Dominance, Lernaean Bow,
    Bloodforge, Riptalon, Oath-Sworn Spear, Genji''s Guard, Damaru, Breastplate of
    Valor, Rage, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.5
      pick: 0.24
      fit: 1.0
    Hydra's Lament:
      total: 0.56
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.77
    Pendulum Blade:
      total: 0.55
      efficiency: 0.39
      win: 0.59
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.52
      efficiency: 0.45
      win: 0.49
      pick: 0.23
      fit: 0.88
    Heartseeker:
      total: 0.56
      efficiency: 0.41
      win: 0.55
      pick: 0.42
      fit: 0.98
    Titan's Bane:
      total: 0.59
      efficiency: 0.51
      win: 0.6
      pick: 0.17
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
