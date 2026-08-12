---
type: smite-build
god: Loki
mode: Conquest
builds:
- source: community
  aspect: Aspect of Agony
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.57
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.39
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.22
      win_rate: 0.56
    - name: Hydra's Lament
      pick_rate: 0.15
      win_rate: 0.57
  - name: Hydra's Lament
    pick_rate: 0.31
    win_rate: 0.57
    alternates:
    - name: Transcendence
      pick_rate: 0.12
      win_rate: 0.52
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.55
  - name: Barbed Carver
    pick_rate: 0.16
    win_rate: 0.55
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.14
      win_rate: 0.57
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.28
    win_rate: 0.59
    alternates:
    - name: Titan's Bane
      pick_rate: 0.13
      win_rate: 0.59
    - name: The Crusher
      pick_rate: 0.07
      win_rate: 0.57
  - name: Titan's Bane
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.61
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.53
  - name: Lucerne Hammer
    pick_rate: 0.06
    win_rate: 0.64
    alternates:
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.69
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.62
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.41
    win_rate: 0.62
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.63
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/loki/
  last_verified: '2026-08-11'
  god_win_rate: 0.5647581989994441
  god_matches_won: 1016
  god_matches_played: 1799
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Titan's Bane
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Pendulum Blade, Tekko-Kagi, Runeforged Hammer,
    Lernaean Bow, Damaru, Avatar''s Parashu, Golden Blade, Genji''s Guard, Avenging
    Blade, Shield Splitter, Arondight, Riptalon, Dominance, Eye of the Storm, Tyrfing,
    Silverbranch Bow, Breastplate of Valor, Berserker''s Shield, Deathbringer, Bloodforge,
    Musashi''s Dual Swords.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.66
      win: 0.56
      pick: 0.39
      fit: 1.0
    Hydra's Lament:
      total: 0.59
      efficiency: 0.58
      win: 0.57
      pick: 0.42
      fit: 0.71
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.63
      efficiency: 0.63
      win: 0.57
      pick: 0.12
      fit: 1.0
    Heartseeker:
      total: 0.6
      efficiency: 0.45
      win: 0.59
      pick: 0.47
      fit: 1.0
    Titan's Bane:
      total: 0.57
      efficiency: 0.45
      win: 0.58
      pick: 0.32
      fit: 0.91
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Genji''s Guard, Breastplate of Valor, The Reaper, Pendulum Blade,
    Riptalon, Runeforged Hammer, Silverbranch Bow, Tekko-Kagi, Freya''s Tears, Berserker''s
    Shield, Lernaean Bow, Damaru, Arondight, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Amanita Charm, Screeching Gargoyle, Oni Hunter''s Garb, Chandra''s
    Grace, Avatar''s Parashu, Eye of Providence, Avenging Blade, Shield Splitter.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.22
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.56
      pick: 0.39
      fit: 0.78
    Hydra's Lament:
      total: 0.56
      efficiency: 0.58
      win: 0.57
      pick: 0.42
      fit: 0.54
    The Crusher:
      total: 0.58
      efficiency: 0.63
      win: 0.57
      pick: 0.12
      fit: 0.66
    Heartseeker:
      total: 0.54
      efficiency: 0.45
      win: 0.59
      pick: 0.47
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, The Crusher,
    Berserker''s Shield, The Reaper, Genji''s Guard, Oni Hunter''s Garb, Runeforged
    Hammer, Eye of the Storm, Riptalon, Chandra''s Grace, Shield Splitter, Erosion,
    Phoenix Feather, Freya''s Tears, Breastplate of Valor, Eye of Providence, Spectral
    Armor, Pharaoh''s Curse, Draconic Scale, Golden Blade, Leviathan''s Hide, Avenging
    Blade, Midgardian Mail, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.56
      pick: 0.39
      fit: 0.44
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.73
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.57
      pick: 0.12
      fit: 0.5
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Tekko-Kagi
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, The Reaper, Tekko-Kagi, Pendulum Blade, Riptalon, Silverbranch
    Bow, Avenging Blade, Avatar''s Parashu, Genji''s Guard, Runeforged Hammer, Lernaean
    Bow, Damaru, Screeching Gargoyle, Toxic Blade, Breastplate of Valor, Berserker''s
    Shield, Golden Blade, Shield Splitter, Stone of Binding, Dominance, Eye of the
    Storm, Oath-Sworn Spear, Tyrfing, Arondight, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.66
      win: 0.56
      pick: 0.39
      fit: 1.0
    The Reaper:
      total: 0.58
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.94
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.45
      win: 0.57
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.63
      efficiency: 0.63
      win: 0.57
      pick: 0.12
      fit: 1.0
    Heartseeker:
      total: 0.6
      efficiency: 0.45
      win: 0.59
      pick: 0.47
      fit: 1.0
    Titan's Bane:
      total: 0.58
      efficiency: 0.45
      win: 0.58
      pick: 0.32
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Silverbranch Bow, Golden Blade, The Crusher, Berserker''s
    Shield, Tyrfing, Lernaean Bow, Genji''s Guard, Tekko-Kagi, Toxic Blade, Dominance,
    Pharaoh''s Curse, The Reaper, Breastplate of Valor, Runeforged Hammer, Shogun''s
    Ofuda, Damaru, Eros'' Bow, Qin''s Blade, Kinetic Cuirass, Amanita Charm, Oni Hunter''s
    Garb, Eye of Providence, Freya''s Tears, Dagger of Frenzy.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.69
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.39
      fit: 0.37
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.12
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  flex_slots:
  - The Crusher
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    The Crusher, Freya''s Tears, Shield of the Phoenix, Pendulum Blade, Arondight,
    Screeching Gargoyle, Chandra''s Grace, Berserker''s Shield, Gladiator''s Shield,
    The Reaper, Runeforged Hammer, Riptalon, Lernaean Bow, Damaru, Prophetic Cloak,
    Kinetic Cuirass, Amanita Charm, Silverbranch Bow, Oni Hunter''s Garb, Eye of Providence,
    Regrowth Striders, Golden Blade, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.66
      win: 0.56
      pick: 0.39
      fit: 0.85
    Hydra's Lament:
      total: 0.59
      efficiency: 0.58
      win: 0.57
      pick: 0.42
      fit: 0.75
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.12
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Titan's Bane
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, The Reaper, Pendulum Blade, Tekko-Kagi,
    Runeforged Hammer, Lernaean Bow, Damaru, Avatar''s Parashu, Golden Blade, Genji''s
    Guard, Avenging Blade, Shield Splitter, Arondight, Riptalon, Dominance, Eye of
    the Storm, Tyrfing, Silverbranch Bow, Breastplate of Valor, Berserker''s Shield,
    Deathbringer, Bloodforge, Musashi''s Dual Swords.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.66
      win: 0.56
      pick: 0.39
      fit: 1.0
    Hydra's Lament:
      total: 0.59
      efficiency: 0.58
      win: 0.57
      pick: 0.42
      fit: 0.71
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.63
      efficiency: 0.63
      win: 0.57
      pick: 0.12
      fit: 1.0
    Heartseeker:
      total: 0.6
      efficiency: 0.45
      win: 0.59
      pick: 0.47
      fit: 1.0
    Titan's Bane:
      total: 0.57
      efficiency: 0.45
      win: 0.58
      pick: 0.32
      fit: 0.91
  starter: *id001
---
