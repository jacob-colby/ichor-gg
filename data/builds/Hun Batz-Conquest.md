---
type: smite-build
god: Hun Batz
mode: Conquest
builds:
- source: community
  aspect: Aspect of Disruption
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.27
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.67
    win_rate: 0.42
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.21
      win_rate: 0.44
    - name: Transcendence
      pick_rate: 0.05
      win_rate: 0.5
  - name: Hydra's Lament
    pick_rate: 0.52
    win_rate: 0.39
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.18
      win_rate: 0.53
    - name: Transcendence
      pick_rate: 0.12
      win_rate: 0.6
  - name: The Reaper
    pick_rate: 0.21
    win_rate: 0.44
    alternates:
    - name: The Crusher
      pick_rate: 0.15
      win_rate: 0.38
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.36
  - name: Heartseeker
    pick_rate: 0.35
    win_rate: 0.52
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.14
      win_rate: 0.36
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.29
  - name: Titan's Bane
    pick_rate: 0.24
    win_rate: 0.71
    alternates:
    - name: Heartseeker
      pick_rate: 0.24
      win_rate: 0.59
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.33
  - name: Void Shard
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.1
      win_rate: 1.0
    - name: Titan's Bane
      pick_rate: 0.1
      win_rate: 0.2
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.54
    win_rate: 0.46
  - name: Bumba's Cudgel
    pick_rate: 0.35
    win_rate: 0.43
  - name: Hunter's Cowl
    pick_rate: 0.06
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/hun-batz/
  last_verified: '2026-08-14'
  god_win_rate: 0.43529411764705883
  god_matches_won: 37
  god_matches_played: 85
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
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
  - Transcendence
  - The Reaper
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
    this god: Pendulum Blade, Tekko-Kagi, Runeforged Hammer, Damaru, Lernaean Bow,
    Avatar''s Parashu, Golden Blade, Avenging Blade, Arondight, Shield Splitter, Genji''s
    Guard, Eye of the Storm, Tyrfing, Riptalon, Dominance, Silverbranch Bow, Breastplate
    of Valor, Deathbringer, Barbed Carver, Berserker''s Shield, Musashi''s Dual Swords,
    Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.42
      pick: 0.67
      fit: 1.0
    Transcendence:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.16
      fit: 0.52
    The Reaper:
      total: 0.53
      efficiency: 0.52
      win: 0.44
      pick: 0.33
      fit: 0.91
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.38
      pick: 0.23
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.41
      win: 0.52
      pick: 0.58
      fit: 1.0
    Titan's Bane:
      total: 0.64
      efficiency: 0.45
      win: 0.71
      pick: 0.52
      fit: 0.91
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
  - The Crusher
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
    Guard, Breastplate of Valor, Runeforged Hammer, Damaru, Pendulum Blade, Lernaean
    Bow, Arondight, Oni Hunter''s Garb, Berserker''s Shield, Golden Blade, Freya''s
    Tears, Tekko-Kagi, Avenging Blade, Dominance, Kinetic Cuirass, Shield Splitter,
    Amanita Charm, Shield of the Phoenix, Eye of the Storm, Tyrfing, Eye of Providence,
    Yogi''s Necklace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.42
      pick: 0.67
      fit: 0.71
    Transcendence:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.16
      fit: 0.39
    Hydra's Lament:
      total: 0.5
      efficiency: 0.56
      win: 0.39
      pick: 0.71
      fit: 0.63
    The Crusher:
      total: 0.49
      efficiency: 0.64
      win: 0.38
      pick: 0.23
      fit: 0.57
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.52
      pick: 0.58
      fit: 0.67
    Titan's Bane:
      total: 0.57
      efficiency: 0.45
      win: 0.71
      pick: 0.52
      fit: 0.47
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
  - Transcendence
  - Hydra's Lament
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
    god: Genji''s Guard, Pendulum Blade, Breastplate of Valor, Runeforged Hammer,
    Freya''s Tears, Tekko-Kagi, Riptalon, Arondight, Damaru, Silverbranch Bow, Shield
    of the Phoenix, Berserker''s Shield, Lernaean Bow, Kinetic Cuirass, Amanita Charm,
    Screeching Gargoyle, Golden Blade, Chandra''s Grace, Eye of Providence, Avenging
    Blade, Oni Hunter''s Garb, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.42
      pick: 0.67
      fit: 0.78
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.16
      fit: 0.22
    Hydra's Lament:
      total: 0.49
      efficiency: 0.56
      win: 0.39
      pick: 0.71
      fit: 0.54
    The Crusher:
      total: 0.5
      efficiency: 0.64
      win: 0.38
      pick: 0.23
      fit: 0.66
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.52
      pick: 0.58
      fit: 0.66
    Titan's Bane:
      total: 0.58
      efficiency: 0.45
      win: 0.71
      pick: 0.52
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Transcendence
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Transcendence
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
    Shield, Runeforged Hammer, Genji''s Guard, Oni Hunter''s Garb, Eye of the Storm,
    Chandra''s Grace, Erosion, Shifter''s Shield, Shield Splitter, Phoenix Feather,
    Freya''s Tears, Eye of Providence, Spectral Armor, Draconic Scale, Riptalon, Breastplate
    of Valor, Golden Blade, Pharaoh''s Curse, Avenging Blade, Leviathan''s Hide, Midgardian
    Mail, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.64
      win: 0.42
      pick: 0.67
      fit: 0.44
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.73
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.16
      fit: 0.23
    Titan's Bane:
      total: 0.56
      efficiency: 0.45
      win: 0.71
      pick: 0.52
      fit: 0.4
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Tekko-Kagi, Pendulum Blade, Riptalon, Avenging Blade, Silverbranch
    Bow, Avatar''s Parashu, Runeforged Hammer, Genji''s Guard, Damaru, Toxic Blade,
    Lernaean Bow, Screeching Gargoyle, Golden Blade, Breastplate of Valor, Berserker''s
    Shield, Shield Splitter, Eye of the Storm, Stone of Binding, Tyrfing, Oath-Sworn
    Spear, Arondight, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.42
      pick: 0.67
      fit: 1.0
    Transcendence:
      total: 0.51
      efficiency: 0.52
      win: 0.6
      pick: 0.16
      fit: 0.33
    The Reaper:
      total: 0.54
      efficiency: 0.52
      win: 0.44
      pick: 0.33
      fit: 0.94
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.38
      pick: 0.23
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.41
      win: 0.52
      pick: 0.58
      fit: 1.0
    Titan's Bane:
      total: 0.64
      efficiency: 0.45
      win: 0.71
      pick: 0.52
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Transcendence
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Transcendence
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
    Lernaean Bow, Toxic Blade, Tekko-Kagi, Genji''s Guard, Pharaoh''s Curse, Dominance,
    Runeforged Hammer, Breastplate of Valor, Damaru, Shogun''s Ofuda, Kinetic Cuirass,
    Amanita Charm, Qin''s Blade, Eye of Providence, Oni Hunter''s Garb, Eros'' Bow,
    Freya''s Tears, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.42
      pick: 0.67
      fit: 0.37
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.16
      fit: 0.17
    Riptalon:
      total: 0.52
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.69
    Titan's Bane:
      total: 0.55
      efficiency: 0.45
      win: 0.71
      pick: 0.52
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Titan's Bane
  flex_slots:
  - Breastplate of Valor
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Shield of the Phoenix, Pendulum Blade, Arondight, Screeching Gargoyle,
    Chandra''s Grace, Gladiator''s Shield, Runeforged Hammer, Berserker''s Shield,
    Prophetic Cloak, Kinetic Cuirass, Damaru, Amanita Charm, Riptalon, Eye of Providence,
    Oni Hunter''s Garb, Regrowth Striders, Lernaean Bow, Silverbranch Bow, Golden
    Blade, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.47
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.42
      pick: 0.67
      fit: 0.85
    Transcendence:
      total: 0.48
      efficiency: 0.52
      win: 0.6
      pick: 0.16
      fit: 0.15
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.39
      pick: 0.71
      fit: 0.75
    Titan's Bane:
      total: 0.55
      efficiency: 0.45
      win: 0.71
      pick: 0.52
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
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
    Underrated for this god: Pendulum Blade, Tekko-Kagi, Runeforged Hammer, Damaru,
    Lernaean Bow, Avatar''s Parashu, Golden Blade, Avenging Blade, Arondight, Shield
    Splitter, Genji''s Guard, Eye of the Storm, Tyrfing, Riptalon, Dominance, Silverbranch
    Bow, Breastplate of Valor, Deathbringer, Barbed Carver, Berserker''s Shield, Musashi''s
    Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.42
      pick: 0.67
      fit: 1.0
    Transcendence:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.16
      fit: 0.52
    Hydra's Lament:
      total: 0.51
      efficiency: 0.56
      win: 0.39
      pick: 0.71
      fit: 0.71
    The Reaper:
      total: 0.53
      efficiency: 0.52
      win: 0.44
      pick: 0.33
      fit: 0.91
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.38
      pick: 0.23
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.41
      win: 0.52
      pick: 0.58
      fit: 1.0
  starter: *id001
---
