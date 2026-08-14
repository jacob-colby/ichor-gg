---
type: smite-build
god: Mercury
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Rage
    pick_rate: 0.63
    win_rate: 0.63
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.4
    - name: Avenging Blade
      pick_rate: 0.07
      win_rate: 1.0
  - name: Dagger of Frenzy
    pick_rate: 0.23
    win_rate: 0.79
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.18
      win_rate: 0.73
    - name: Rage
      pick_rate: 0.13
      win_rate: 0.75
  - name: Deathbringer
    pick_rate: 0.32
    win_rate: 0.58
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.22
      win_rate: 0.69
    - name: Musashi's Dual Swords
      pick_rate: 0.14
      win_rate: 0.88
  - name: Silverbranch Bow
    pick_rate: 0.16
    win_rate: 0.89
    alternates:
    - name: Deathbringer
      pick_rate: 0.26
      win_rate: 0.53
    - name: Musashi's Dual Swords
      pick_rate: 0.09
      win_rate: 0.4
  - name: Riptalon
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Deathbringer
      pick_rate: 0.2
      win_rate: 0.91
    - name: Silverbranch Bow
      pick_rate: 0.07
      win_rate: 1.0
  - name: Void Shard
    pick_rate: 0.1
    win_rate: 0.75
    alternates:
    - name: Infused Axe
      pick_rate: 0.07
      win_rate: 0.33
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Bumba's Spear
    pick_rate: 0.3
    win_rate: 0.72
  - name: Sharpshooter's Arrow
    pick_rate: 0.25
    win_rate: 0.8
  - name: Hunter's Cowl
    pick_rate: 0.18
    win_rate: 0.91
  source_url: https://smitebrain.com/gods/mercury/
  last_verified: '2026-08-14'
  god_win_rate: 0.7
  god_matches_won: 42
  god_matches_played: 60
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
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Musashi's Dual Swords
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Musashi's Dual Swords
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Avenging Blade, Jotunn''s Revenge, The Crusher, The Reaper, Genji''s
    Guard, Lernaean Bow, Heartseeker, Pendulum Blade, Damaru, Tekko-Kagi, Runeforged
    Hammer, Golden Blade, Breastplate of Valor, Titan''s Bane, Berserker''s Shield,
    Arondight, Dominance, Tyrfing, Shield Splitter, Eye of the Storm, Avatar''s Parashu,
    Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass, Amanita Charm.'
  slot_scores:
    Avenging Blade:
      total: 0.69
      efficiency: 0.48
      win: 1.0
      pick: 0.07
      fit: 0.48
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.66
      win: 0.74
      pick: 0.0
      fit: 0.84
    Hydra's Lament:
      total: 0.64
      efficiency: 0.58
      win: 0.73
      pick: 0.25
      fit: 0.66
    Musashi's Dual Swords:
      total: 0.62
      efficiency: 0.42
      win: 0.88
      pick: 0.22
      fit: 0.45
    Silverbranch Bow:
      total: 0.66
      efficiency: 0.54
      win: 0.89
      pick: 0.27
      fit: 0.37
    The Crusher:
      total: 0.67
      efficiency: 0.63
      win: 0.74
      pick: 0.0
      fit: 0.77
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Silverbranch Bow
  - The Crusher
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
    god: Jotunn''s Revenge, Avenging Blade, The Crusher, Genji''s Guard, Breastplate
    of Valor, The Reaper, Pendulum Blade, Heartseeker, Berserker''s Shield, Lernaean
    Bow, Tekko-Kagi, Damaru, Runeforged Hammer, Freya''s Tears, Titan''s Bane, Shield
    of the Phoenix, Arondight, Golden Blade, Kinetic Cuirass, Amanita Charm, Oni Hunter''s
    Garb, Screeching Gargoyle, Eye of Providence, Dominance, Chandra''s Grace, Tyrfing.'
  slot_scores:
    Avenging Blade:
      total: 0.67
      efficiency: 0.48
      win: 1.0
      pick: 0.07
      fit: 0.3
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.74
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.66
      win: 0.74
      pick: 0.0
      fit: 0.71
    Hydra's Lament:
      total: 0.62
      efficiency: 0.58
      win: 0.73
      pick: 0.25
      fit: 0.51
    Silverbranch Bow:
      total: 0.66
      efficiency: 0.54
      win: 0.89
      pick: 0.27
      fit: 0.35
    The Crusher:
      total: 0.64
      efficiency: 0.63
      win: 0.74
      pick: 0.0
      fit: 0.61
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Avenging Blade, Amanita Charm, Shield of the Phoenix, Berserker''s Shield,
    Jotunn''s Revenge, Kinetic Cuirass, The Crusher, Genji''s Guard, The Reaper, Chandra''s
    Grace, Oni Hunter''s Garb, Breastplate of Valor, Runeforged Hammer, Freya''s Tears,
    Pharaoh''s Curse, Eye of the Storm, Phoenix Feather, Shifter''s Shield, Shield
    Splitter, Erosion, Spectral Armor, Golden Blade, Eye of Providence, Draconic Scale,
    Leviathan''s Hide, Shogun''s Ofuda, Lernaean Bow.'
  slot_scores:
    Avenging Blade:
      total: 0.69
      efficiency: 0.48
      win: 1.0
      pick: 0.07
      fit: 0.48
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.74
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.66
      win: 0.74
      pick: 0.0
      fit: 0.44
    Shield of the Phoenix:
      total: 0.64
      efficiency: 0.57
      win: 0.74
      pick: 0.0
      fit: 0.73
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.54
      win: 0.89
      pick: 0.27
      fit: 0.19
    Amanita Charm:
      total: 0.67
      efficiency: 0.63
      win: 0.74
      pick: 0.0
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - Silverbranch Bow
  - The Crusher
  - Heartseeker
  flex_slots:
  - The Reaper
  - Heartseeker
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
    for this god: Avenging Blade, Jotunn''s Revenge, The Crusher, The Reaper, Heartseeker,
    Tekko-Kagi, Pendulum Blade, Titan''s Bane, Genji''s Guard, Lernaean Bow, Screeching
    Gargoyle, Damaru, Breastplate of Valor, Avatar''s Parashu, Berserker''s Shield,
    Runeforged Hammer, Golden Blade, Toxic Blade, Stone of Binding, Dominance, Arondight,
    Freya''s Tears, Tyrfing, Kinetic Cuirass, Void Shield, Amanita Charm.'
  slot_scores:
    Avenging Blade:
      total: 0.72
      efficiency: 0.48
      win: 1.0
      pick: 0.07
      fit: 0.67
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.66
      win: 0.74
      pick: 0.0
      fit: 0.89
    The Reaper:
      total: 0.63
      efficiency: 0.52
      win: 0.74
      pick: 0.0
      fit: 0.77
    Silverbranch Bow:
      total: 0.69
      efficiency: 0.54
      win: 0.89
      pick: 0.27
      fit: 0.56
    The Crusher:
      total: 0.68
      efficiency: 0.63
      win: 0.74
      pick: 0.0
      fit: 0.87
    Heartseeker:
      total: 0.62
      efficiency: 0.45
      win: 0.74
      pick: 0.0
      fit: 0.87
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - The Crusher
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
    this god: Jotunn''s Revenge, Golden Blade, Berserker''s Shield, The Crusher, Lernaean
    Bow, Tyrfing, Genji''s Guard, Breastplate of Valor, Tekko-Kagi, Pharaoh''s Curse,
    Dominance, Toxic Blade, The Reaper, Damaru, Runeforged Hammer, Shogun''s Ofuda,
    Kinetic Cuirass, Amanita Charm, Eros'' Bow, Freya''s Tears, Oni Hunter''s Garb,
    Heartseeker, Eye of Providence, Qin''s Blade, Shield of the Phoenix, Yogi''s Necklace.'
  slot_scores:
    Golden Blade:
      total: 0.61
      efficiency: 0.54
      win: 0.74
      pick: 0.0
      fit: 0.62
    Avenging Blade:
      total: 0.66
      efficiency: 0.48
      win: 1.0
      pick: 0.07
      fit: 0.25
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.74
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.74
      pick: 0.0
      fit: 0.4
    Silverbranch Bow:
      total: 0.7
      efficiency: 0.54
      win: 0.89
      pick: 0.27
      fit: 0.62
    The Crusher:
      total: 0.61
      efficiency: 0.63
      win: 0.74
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, The Crusher, Freya''s Tears, Shield of the Phoenix, Pendulum
    Blade, Screeching Gargoyle, Arondight, Chandra''s Grace, Berserker''s Shield,
    Lernaean Bow, Damaru, The Reaper, Runeforged Hammer, Gladiator''s Shield, Kinetic
    Cuirass, Amanita Charm, Oni Hunter''s Garb, Heartseeker, Prophetic Cloak, Golden
    Blade, Eye of Providence, Tekko-Kagi, Pharaoh''s Curse, Yogi''s Necklace.'
  slot_scores:
    Avenging Blade:
      total: 0.66
      efficiency: 0.48
      win: 1.0
      pick: 0.07
      fit: 0.24
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.74
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.74
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.66
      win: 0.74
      pick: 0.0
      fit: 0.77
    Hydra's Lament:
      total: 0.65
      efficiency: 0.58
      win: 0.73
      pick: 0.25
      fit: 0.69
    Silverbranch Bow:
      total: 0.64
      efficiency: 0.54
      win: 0.89
      pick: 0.27
      fit: 0.23
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Lernaean Bow
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
    Underrated for this god: Jotunn''s Revenge, The Crusher, The Reaper, Genji''s
    Guard, Lernaean Bow, Heartseeker, Pendulum Blade, Damaru, Tekko-Kagi, Runeforged
    Hammer, Golden Blade, Breastplate of Valor, Titan''s Bane, Berserker''s Shield,
    Arondight, Dominance, Tyrfing, Avenging Blade, Shield Splitter, Eye of the Storm,
    Avatar''s Parashu, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass, Amanita
    Charm.'
  slot_scores:
    Lernaean Bow:
      total: 0.61
      efficiency: 0.54
      win: 0.74
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.74
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.66
      win: 0.74
      pick: 0.0
      fit: 0.84
    Hydra's Lament:
      total: 0.64
      efficiency: 0.58
      win: 0.73
      pick: 0.25
      fit: 0.66
    The Reaper:
      total: 0.61
      efficiency: 0.52
      win: 0.74
      pick: 0.0
      fit: 0.67
    The Crusher:
      total: 0.67
      efficiency: 0.63
      win: 0.74
      pick: 0.0
      fit: 0.77
  starter: *id001
---
