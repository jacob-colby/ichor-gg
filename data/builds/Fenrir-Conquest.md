---
type: smite-build
god: Fenrir
mode: Conquest
builds:
- source: community
  aspect: Aspect of Loyalty
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.8
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.37
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.88
    - name: The Reaper
      pick_rate: 0.14
      win_rate: 0.5
  - name: Shifter's Shield
    pick_rate: 0.16
    win_rate: 0.57
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.12
      win_rate: 0.6
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.75
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Deathbringer
      pick_rate: 0.1
      win_rate: 0.5
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.67
  - name: Heartseeker
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.67
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.5
  - name: Hunter's Bow
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Medallion
      pick_rate: 0.09
      win_rate: 0.5
    - name: Mantle Of Discord
      pick_rate: 0.09
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.23
    win_rate: 0.8
  - name: Bumba's Cudgel
    pick_rate: 0.19
    win_rate: 0.38
  - name: Death's Embrace
    pick_rate: 0.09
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/fenrir/
  last_verified: '2026-08-13'
  god_win_rate: 0.6511627906976745
  god_matches_won: 28
  god_matches_played: 43
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Mantle Of Discord
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - The Reaper
  - Hydra's Lament
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Hydra''s Lament, Titan''s Bane, Pendulum Blade, Tekko-Kagi,
    Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s Parashu, Golden Blade, Avenging
    Blade, Shield Splitter, Arondight, Riptalon, Dominance, Eye of the Storm, Tyrfing,
    Silverbranch Bow, Breastplate of Valor, Berserker''s Shield, Barbed Carver, Transcendence,
    Bloodforge, Musashi''s Dual Swords.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.66
      win: 0.56
      pick: 0.37
      fit: 1.0
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.12
      fit: 0.71
    Mantle Of Discord:
      total: 0.65
      efficiency: 0.53
      win: 1.0
      pick: 0.28
      fit: 0.0
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.14
      fit: 0.91
    The Crusher:
      total: 0.68
      efficiency: 0.63
      win: 0.67
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.66
      efficiency: 0.45
      win: 0.75
      pick: 0.24
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Mantle Of Discord
  - The Crusher
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, Breastplate of Valor, Pendulum Blade, The Reaper, Riptalon,
    Titan''s Bane, Runeforged Hammer, Silverbranch Bow, Tekko-Kagi, Berserker''s Shield,
    Damaru, Lernaean Bow, Arondight, Shield of the Phoenix, Kinetic Cuirass, Golden
    Blade, Amanita Charm, Screeching Gargoyle, Oni Hunter''s Garb, Chandra''s Grace,
    Avatar''s Parashu, Eye of Providence, Avenging Blade, Shield Splitter.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.16
      fit: 0.22
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.56
      pick: 0.37
      fit: 0.78
    Hydra's Lament:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.12
      fit: 0.54
    Mantle Of Discord:
      total: 0.65
      efficiency: 0.53
      win: 1.0
      pick: 0.28
      fit: 0.0
    The Crusher:
      total: 0.63
      efficiency: 0.63
      win: 0.67
      pick: 0.19
      fit: 0.66
    Heartseeker:
      total: 0.6
      efficiency: 0.45
      win: 0.75
      pick: 0.24
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Mantle Of Discord
  - The Crusher
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, The Reaper, Oni Hunter''s Garb, Runeforged Hammer, Eye of the Storm, Riptalon,
    Chandra''s Grace, Shield Splitter, Erosion, Phoenix Feather, Breastplate of Valor,
    Eye of Providence, Spectral Armor, Pharaoh''s Curse, Draconic Scale, Golden Blade,
    Hydra''s Lament, Leviathan''s Hide, Avenging Blade, Midgardian Mail, Shogun''s
    Ofuda.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.56
      pick: 0.37
      fit: 0.44
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.73
    Mantle Of Discord:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.28
      fit: 0.34
    The Crusher:
      total: 0.61
      efficiency: 0.63
      win: 0.67
      pick: 0.19
      fit: 0.5
    Heartseeker:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.24
      fit: 0.5
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Mantle Of Discord
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Titan''s Bane, Tekko-Kagi, Pendulum Blade, Riptalon,
    Silverbranch Bow, Avenging Blade, Avatar''s Parashu, Hydra''s Lament, Runeforged
    Hammer, Damaru, Lernaean Bow, Screeching Gargoyle, Breastplate of Valor, Toxic
    Blade, Berserker''s Shield, Golden Blade, Shield Splitter, Stone of Binding, Dominance,
    Eye of the Storm, Oath-Sworn Spear, Tyrfing, Arondight, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.66
      win: 0.56
      pick: 0.37
      fit: 1.0
    Mantle Of Discord:
      total: 0.65
      efficiency: 0.53
      win: 1.0
      pick: 0.28
      fit: 0.0
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.14
      fit: 0.94
    The Crusher:
      total: 0.68
      efficiency: 0.63
      win: 0.67
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.66
      efficiency: 0.45
      win: 0.75
      pick: 0.24
      fit: 1.0
    Titan's Bane:
      total: 0.54
      efficiency: 0.45
      win: 0.53
      pick: 0.0
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Mantle Of Discord
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Heartseeker
  flex_slots:
  - Silverbranch Bow
  - Golden Blade
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
    this god: Riptalon, Silverbranch Bow, Golden Blade, Berserker''s Shield, Tyrfing,
    Lernaean Bow, Tekko-Kagi, Toxic Blade, Dominance, Pharaoh''s Curse, Hydra''s Lament,
    The Reaper, Breastplate of Valor, Runeforged Hammer, Shogun''s Ofuda, Damaru,
    Eros'' Bow, Qin''s Blade, Kinetic Cuirass, Amanita Charm, Oni Hunter''s Garb,
    Eye of Providence, Dagger of Frenzy, Titan''s Bane.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.69
    Mantle Of Discord:
      total: 0.65
      efficiency: 0.53
      win: 1.0
      pick: 0.28
      fit: 0.0
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.67
      pick: 0.19
      fit: 0.43
    Heartseeker:
      total: 0.57
      efficiency: 0.45
      win: 0.75
      pick: 0.24
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Mantle Of Discord
  - The Crusher
  - Heartseeker
  flex_slots:
  - Genji's Guard
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Breastplate of Valor,
    Shield of the Phoenix, Pendulum Blade, Arondight, Screeching Gargoyle, Chandra''s
    Grace, Berserker''s Shield, Gladiator''s Shield, Runeforged Hammer, The Reaper,
    Riptalon, Damaru, Lernaean Bow, Prophetic Cloak, Kinetic Cuirass, Amanita Charm,
    Silverbranch Bow, Oni Hunter''s Garb, Eye of Providence, Regrowth Striders, Golden
    Blade, Titan''s Bane, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.16
      fit: 0.5
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.66
      win: 0.56
      pick: 0.37
      fit: 0.85
    Hydra's Lament:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.12
      fit: 0.75
    Mantle Of Discord:
      total: 0.65
      efficiency: 0.53
      win: 1.0
      pick: 0.28
      fit: 0.0
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.67
      pick: 0.19
      fit: 0.45
    Heartseeker:
      total: 0.57
      efficiency: 0.45
      win: 0.75
      pick: 0.24
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
    Underrated for this god: The Reaper, Hydra''s Lament, Titan''s Bane, Pendulum
    Blade, Tekko-Kagi, Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s Parashu,
    Golden Blade, Avenging Blade, Shield Splitter, Arondight, Riptalon, Dominance,
    Eye of the Storm, Tyrfing, Silverbranch Bow, Breastplate of Valor, Berserker''s
    Shield, Barbed Carver, Transcendence, Bloodforge, Musashi''s Dual Swords.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.66
      win: 0.56
      pick: 0.37
      fit: 1.0
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.12
      fit: 0.71
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.14
      fit: 0.91
    The Crusher:
      total: 0.68
      efficiency: 0.63
      win: 0.67
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.66
      efficiency: 0.45
      win: 0.75
      pick: 0.24
      fit: 1.0
    Titan's Bane:
      total: 0.53
      efficiency: 0.45
      win: 0.53
      pick: 0.0
      fit: 0.91
  starter: *id001
---
