---
type: smite-build
god: Loki
mode: Conquest
builds:
- source: community
  aspect: Aspect of Agony
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.52
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.33
    win_rate: 0.5
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.21
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.5
  - name: Hydra's Lament
    pick_rate: 0.28
    win_rate: 0.48
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.6
    - name: Barbed Carver
      pick_rate: 0.14
      win_rate: 0.58
  - name: Barbed Carver
    pick_rate: 0.12
    win_rate: 0.51
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.14
      win_rate: 0.58
    - name: The Crusher
      pick_rate: 0.12
      win_rate: 0.59
  - name: Heartseeker
    pick_rate: 0.33
    win_rate: 0.55
    alternates:
    - name: Titan's Bane
      pick_rate: 0.1
      win_rate: 0.58
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.54
  - name: Titan's Bane
    pick_rate: 0.15
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.58
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.51
  - name: Lucerne Hammer
    pick_rate: 0.08
    win_rate: 0.49
    alternates:
    - name: Skeggox
      pick_rate: 0.08
      win_rate: 0.55
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.65
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.38
    win_rate: 0.58
  - name: Bumba's Cudgel
    pick_rate: 0.22
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/loki/
  last_verified: '2026-08-21'
  god_win_rate: 0.5275229357798165
  god_matches_won: 690
  god_matches_played: 1308
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
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
    this god: The Reaper, Pendulum Blade, Tekko-Kagi, Runeforged Hammer, Damaru, Lernaean
    Bow, Avatar''s Parashu, Golden Blade, Transcendence, Avenging Blade, Dominance,
    Arondight, Shield Splitter, Genji''s Guard, Eye of the Storm, Tyrfing, Riptalon,
    Silverbranch Bow, Breastplate of Valor, Deathbringer, Berserker''s Shield, Sanguine
    Lash, Musashi''s Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.5
      pick: 0.33
      fit: 1.0
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.52
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.65
      efficiency: 0.64
      win: 0.59
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.57
      efficiency: 0.41
      win: 0.55
      pick: 0.55
      fit: 1.0
    Titan's Bane:
      total: 0.59
      efficiency: 0.45
      win: 0.6
      pick: 0.32
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
  - Hydra's Lament
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Breastplate of Valor, The Reaper, Runeforged Hammer, Damaru, Transcendence,
    Dominance, Pendulum Blade, Lernaean Bow, Arondight, Oni Hunter''s Garb, Berserker''s
    Shield, Golden Blade, Freya''s Tears, Tekko-Kagi, Avenging Blade, Kinetic Cuirass,
    Shield Splitter, Amanita Charm, Shield of the Phoenix, Eye of the Storm, Tyrfing,
    Eye of Providence, Yogi''s Necklace, Riptalon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.33
      fit: 0.71
    Transcendence:
      total: 0.47
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.48
      pick: 0.38
      fit: 0.63
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.59
      pick: 0.19
      fit: 0.57
    Heartseeker:
      total: 0.54
      efficiency: 0.41
      win: 0.55
      pick: 0.55
      fit: 0.77
    Titan's Bane:
      total: 0.53
      efficiency: 0.45
      win: 0.6
      pick: 0.32
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Genji''s Guard, The Reaper, Pendulum Blade, Breastplate of Valor, Runeforged
    Hammer, Freya''s Tears, Tekko-Kagi, Riptalon, Arondight, Damaru, Silverbranch
    Bow, Shield of the Phoenix, Berserker''s Shield, Lernaean Bow, Kinetic Cuirass,
    Amanita Charm, Screeching Gargoyle, Golden Blade, Chandra''s Grace, Eye of Providence,
    Transcendence, Avenging Blade, Oni Hunter''s Garb, Dominance, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.5
      pick: 0.33
      fit: 0.78
    Transcendence:
      total: 0.45
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.51
      efficiency: 0.56
      win: 0.48
      pick: 0.38
      fit: 0.54
    The Crusher:
      total: 0.6
      efficiency: 0.64
      win: 0.59
      pick: 0.19
      fit: 0.66
    Heartseeker:
      total: 0.53
      efficiency: 0.41
      win: 0.55
      pick: 0.55
      fit: 0.76
    Titan's Bane:
      total: 0.54
      efficiency: 0.45
      win: 0.6
      pick: 0.32
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, The Reaper, Yogi''s Necklace, Runeforged Hammer, Genji''s Guard, Oni Hunter''s
    Garb, Eye of the Storm, Chandra''s Grace, Erosion, Shield Splitter, Phoenix Feather,
    Freya''s Tears, Eye of Providence, Spectral Armor, Draconic Scale, Riptalon, Breastplate
    of Valor, Golden Blade, Pharaoh''s Curse, Avenging Blade, Leviathan''s Hide, Midgardian
    Mail, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.33
      fit: 0.44
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.51
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.73
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.59
      pick: 0.19
      fit: 0.5
    Titan's Bane:
      total: 0.52
      efficiency: 0.45
      win: 0.6
      pick: 0.32
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.51
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Tekko-Kagi, Pendulum Blade, Riptalon, Avenging Blade,
    Silverbranch Bow, Avatar''s Parashu, Runeforged Hammer, Genji''s Guard, Damaru,
    Toxic Blade, Lernaean Bow, Screeching Gargoyle, Golden Blade, Transcendence, Breastplate
    of Valor, Berserker''s Shield, Dominance, Shield Splitter, Eye of the Storm, Stone
    of Binding, Tyrfing, Oath-Sworn Spear, Arondight, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.5
      pick: 0.33
      fit: 1.0
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.94
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.44
      win: 0.51
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.65
      efficiency: 0.64
      win: 0.59
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.57
      efficiency: 0.41
      win: 0.55
      pick: 0.55
      fit: 1.0
    Titan's Bane:
      total: 0.59
      efficiency: 0.45
      win: 0.6
      pick: 0.32
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
  - The Crusher
  flex_slots:
  - Silverbranch Bow
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Riptalon, Golden Blade, Silverbranch Bow, Tyrfing, Berserker''s Shield,
    Lernaean Bow, Toxic Blade, Dominance, Tekko-Kagi, The Reaper, Genji''s Guard,
    Pharaoh''s Curse, Qin''s Blade, Runeforged Hammer, Breastplate of Valor, Damaru,
    Shogun''s Ofuda, Kinetic Cuirass, Amanita Charm, Eye of Providence, Oni Hunter''s
    Garb, Eros'' Bow, Freya''s Tears, Transcendence, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.33
      fit: 0.37
    Tyrfing:
      total: 0.51
      efficiency: 0.46
      win: 0.51
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.54
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.59
      pick: 0.19
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
  - Breastplate of Valor
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
    Freya''s Tears, Shield of the Phoenix, Pendulum Blade, Arondight, Screeching Gargoyle,
    Chandra''s Grace, The Reaper, Gladiator''s Shield, Runeforged Hammer, Berserker''s
    Shield, Prophetic Cloak, Kinetic Cuirass, Damaru, Amanita Charm, Riptalon, Eye
    of Providence, Oni Hunter''s Garb, Regrowth Striders, Lernaean Bow, Silverbranch
    Bow, Golden Blade, Tekko-Kagi, Transcendence.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.33
      fit: 0.85
    Hydra's Lament:
      total: 0.54
      efficiency: 0.56
      win: 0.48
      pick: 0.38
      fit: 0.75
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.51
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.59
      pick: 0.19
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
  - Hydra's Lament
  - Heartseeker
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
    Underrated for this god: The Reaper, Pendulum Blade, Tekko-Kagi, Runeforged Hammer,
    Damaru, Lernaean Bow, Avatar''s Parashu, Golden Blade, Transcendence, Avenging
    Blade, Dominance, Arondight, Shield Splitter, Genji''s Guard, Eye of the Storm,
    Tyrfing, Riptalon, Silverbranch Bow, Breastplate of Valor, Deathbringer, Berserker''s
    Shield, Sanguine Lash, Musashi''s Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.5
      pick: 0.33
      fit: 1.0
    Hydra's Lament:
      total: 0.54
      efficiency: 0.56
      win: 0.48
      pick: 0.38
      fit: 0.71
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.65
      efficiency: 0.64
      win: 0.59
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.57
      efficiency: 0.41
      win: 0.55
      pick: 0.55
      fit: 1.0
    Titan's Bane:
      total: 0.59
      efficiency: 0.45
      win: 0.6
      pick: 0.32
      fit: 1.0
  starter: *id001
---
