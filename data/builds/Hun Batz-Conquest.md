---
type: smite-build
god: Hun Batz
mode: Conquest
builds:
- source: community
  aspect: Aspect of Disruption
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.41
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.61
    win_rate: 0.45
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.21
      win_rate: 0.49
    - name: Transcendence
      pick_rate: 0.1
      win_rate: 0.41
  - name: Hydra's Lament
    pick_rate: 0.48
    win_rate: 0.47
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.19
      win_rate: 0.46
    - name: Transcendence
      pick_rate: 0.12
      win_rate: 0.5
  - name: The Reaper
    pick_rate: 0.13
    win_rate: 0.48
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.16
      win_rate: 0.38
    - name: The Crusher
      pick_rate: 0.12
      win_rate: 0.49
  - name: Heartseeker
    pick_rate: 0.37
    win_rate: 0.48
    alternates:
    - name: Titan's Bane
      pick_rate: 0.13
      win_rate: 0.49
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.41
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.21
      win_rate: 0.52
    - name: Blinking Abyss
      pick_rate: 0.1
      win_rate: 0.39
  - name: Blinking Abyss
    pick_rate: 0.12
    win_rate: 0.41
    alternates:
    - name: Skeggox
      pick_rate: 0.08
      win_rate: 0.71
    - name: Avatar's Parashu
      pick_rate: 0.08
      win_rate: 0.36
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.55
    win_rate: 0.51
  - name: Bumba's Cudgel
    pick_rate: 0.31
    win_rate: 0.39
  - name: Gilded Arrow
    pick_rate: 0.09
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/hun-batz/
  last_verified: '2026-08-22'
  god_win_rate: 0.45209580838323354
  god_matches_won: 151
  god_matches_played: 334
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Tekko-Kagi, Pendulum Blade, Runeforged Hammer, Tyrfing, Golden Blade,
    Lernaean Bow, Shield Splitter, Silverbranch Bow, Arondight, Avenging Blade, Riptalon,
    Eye of the Storm, Deathbringer, Damaru, Dominance, Toxic Blade, Genji''s Guard,
    Breastplate of Valor, Musashi''s Dual Swords, Berserker''s Shield, Sanguine Lash,
    Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.45
      pick: 0.61
      fit: 1.0
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.16
      fit: 0.52
    The Reaper:
      total: 0.55
      efficiency: 0.55
      win: 0.48
      pick: 0.2
      fit: 0.91
    The Crusher:
      total: 0.58
      efficiency: 0.57
      win: 0.49
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.48
      pick: 0.62
      fit: 1.0
    Titan's Bane:
      total: 0.63
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Crusher
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Breastplate of Valor, Runeforged Hammer, Tekko-Kagi, Arondight, Pendulum
    Blade, Lernaean Bow, Tyrfing, Berserker''s Shield, Freya''s Tears, Golden Blade,
    Shield Splitter, Avenging Blade, Dominance, Amanita Charm, Kinetic Cuirass, Eye
    of the Storm, Silverbranch Bow, Shield of the Phoenix, Deathbringer, Damaru, Riptalon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.45
      pick: 0.61
      fit: 0.71
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.16
      fit: 0.39
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.47
      pick: 0.65
      fit: 0.63
    The Crusher:
      total: 0.52
      efficiency: 0.57
      win: 0.49
      pick: 0.19
      fit: 0.57
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.48
      pick: 0.62
      fit: 0.77
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Transcendence
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Pendulum Blade, Genji''s Guard, Breastplate of Valor, Tekko-Kagi, Freya''s
    Tears, Runeforged Hammer, Silverbranch Bow, Arondight, Riptalon, Berserker''s
    Shield, Shield of the Phoenix, Tyrfing, Amanita Charm, Lernaean Bow, Golden Blade,
    Screeching Gargoyle, Kinetic Cuirass, Shield Splitter, Toxic Blade, Avenging Blade,
    Eye of Providence, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.45
      pick: 0.61
      fit: 0.78
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.5
      pick: 0.16
      fit: 0.22
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.47
      pick: 0.65
      fit: 0.54
    The Crusher:
      total: 0.53
      efficiency: 0.57
      win: 0.49
      pick: 0.19
      fit: 0.66
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.48
      pick: 0.62
      fit: 0.76
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Runeforged Hammer, Shield Splitter, Shifter''s Shield, Eye of the Storm,
    Freya''s Tears, Phoenix Feather, Erosion, Eye of Providence, Genji''s Guard, Riptalon,
    Golden Blade, Breastplate of Valor, Draconic Scale, Spectral Armor, Yogi''s Necklace,
    Mantle Of Discord, Stone of Binding, Chandra''s Grace, Avenging Blade, Leviathan''s
    Hide, Pharaoh''s Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.48
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.45
      pick: 0.61
      fit: 0.44
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.73
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.5
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.48
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
  - The Reaper
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Tekko-Kagi, Pendulum Blade, Silverbranch Bow, Riptalon, Avenging
    Blade, Toxic Blade, Runeforged Hammer, Tyrfing, Stone of Binding, Golden Blade,
    Screeching Gargoyle, Lernaean Bow, Shield Splitter, Berserker''s Shield, Genji''s
    Guard, Breastplate of Valor, Oath-Sworn Spear, Arondight, Eye of the Storm, Amanita
    Charm, Kinetic Cuirass, Deathbringer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.45
      pick: 0.61
      fit: 1.0
    The Reaper:
      total: 0.56
      efficiency: 0.55
      win: 0.48
      pick: 0.2
      fit: 0.94
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.48
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.58
      efficiency: 0.57
      win: 0.49
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.48
      pick: 0.62
      fit: 1.0
    Titan's Bane:
      total: 0.63
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Tyrfing, Silverbranch Bow, Golden Blade, Berserker''s Shield,
    Tekko-Kagi, Lernaean Bow, Toxic Blade, Dominance, Pharaoh''s Curse, Qin''s Blade,
    Runeforged Hammer, Genji''s Guard, Breastplate of Valor, Shogun''s Ofuda, Amanita
    Charm, Kinetic Cuirass, Sun Beam Bow, Freya''s Tears, Shield Splitter, Eye of
    Providence, Avenging Blade, Vital Amplifier.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.45
      pick: 0.61
      fit: 0.37
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.48
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.48
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.69
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.35
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
  - Titan's Bane
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Freya''s Tears, Pendulum Blade, Shield of the Phoenix, Arondight, Screeching Gargoyle,
    Chandra''s Grace, Eye of Erebus, Berserker''s Shield, Runeforged Hammer, Prophetic
    Cloak, Amanita Charm, Gladiator''s Shield, Silverbranch Bow, Kinetic Cuirass,
    Tekko-Kagi, Riptalon, Tyrfing, Lernaean Bow, Golden Blade, Eye of Providence,
    Shield Splitter.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.45
      pick: 0.61
      fit: 0.85
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.47
      pick: 0.65
      fit: 0.75
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.48
      pick: 0.0
      fit: 0.5
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Tekko-Kagi
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
    Underrated for this god: Tekko-Kagi, Pendulum Blade, Runeforged Hammer, Tyrfing,
    Golden Blade, Lernaean Bow, Shield Splitter, Silverbranch Bow, Arondight, Avenging
    Blade, Riptalon, Eye of the Storm, Deathbringer, Damaru, Dominance, Toxic Blade,
    Genji''s Guard, Breastplate of Valor, Musashi''s Dual Swords, Berserker''s Shield,
    Sanguine Lash, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.45
      pick: 0.61
      fit: 1.0
    The Reaper:
      total: 0.55
      efficiency: 0.55
      win: 0.48
      pick: 0.2
      fit: 0.91
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.48
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.58
      efficiency: 0.57
      win: 0.49
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.48
      pick: 0.62
      fit: 1.0
    Titan's Bane:
      total: 0.63
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 1.0
  starter: *id001
---
