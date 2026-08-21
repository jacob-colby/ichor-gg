---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.35
  aspect_win_rate: 0.57
  slot_order:
  - name: Briskberry Acorn
    pick_rate: 0.32
    win_rate: 0.43
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.3
      win_rate: 0.47
    - name: Ashwhorl Acorn
      pick_rate: 0.24
      win_rate: 0.55
  - name: Thistlethorn Acorn
    pick_rate: 0.18
    win_rate: 0.51
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.3
      win_rate: 0.49
    - name: Ashwhorl Acorn
      pick_rate: 0.13
      win_rate: 0.45
  - name: Jotunn's Revenge
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.18
      win_rate: 0.5
    - name: Thistlethorn Acorn
      pick_rate: 0.13
      win_rate: 0.34
  - name: Heartseeker
    pick_rate: 0.14
    win_rate: 0.43
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.28
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.56
  - name: Titan's Bane
    pick_rate: 0.1
    win_rate: 0.32
    alternates:
    - name: Heartseeker
      pick_rate: 0.18
      win_rate: 0.42
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.67
  - name: Void Shard
    pick_rate: 0.07
    win_rate: 0.2
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.5
    - name: Lucerne Hammer
      pick_rate: 0.07
      win_rate: 0.4
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.45
  - name: Bumba's Hammer
    pick_rate: 0.17
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-08-21'
  god_win_rate: 0.46543778801843316
  god_matches_won: 101
  god_matches_played: 217
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
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - The Crusher
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
    this god: The Crusher, The Reaper, Tekko-Kagi, Genji''s Guard, Hydra''s Lament,
    Runeforged Hammer, Pendulum Blade, Avatar''s Parashu, Tyrfing, Golden Blade, Lernaean
    Bow, Shield Splitter, Avenging Blade, Arondight, Silverbranch Bow, Transcendence,
    Eye of the Storm, Riptalon, Deathbringer, Damaru, Dominance, Berserker''s Shield,
    Toxic Blade, Musashi''s Dual Swords.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.93
      win: 0.55
      pick: 0.24
      fit: 0.46
    Briskberry Acorn:
      total: 0.57
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.46
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.86
      win: 0.51
      pick: 0.25
      fit: 0.54
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.67
      pick: 0.17
      fit: 0.08
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.53
      pick: 0.31
      fit: 0.88
    The Crusher:
      total: 0.55
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.91
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  flex_slots:
  - Briskberry Acorn
  - Genji's Guard
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, The Crusher, Hydra''s Lament, The Reaper, Runeforged Hammer, Transcendence,
    Berserker''s Shield, Tekko-Kagi, Arondight, Lernaean Bow, Freya''s Tears, Pendulum
    Blade, Shield Splitter, Tyrfing, Golden Blade, Amanita Charm, Avenging Blade,
    Dominance, Kinetic Cuirass, Avatar''s Parashu, Eye of the Storm, Shield of the
    Phoenix, Silverbranch Bow, Deathbringer.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.63
      efficiency: 0.93
      win: 0.55
      pick: 0.24
      fit: 0.27
    Briskberry Acorn:
      total: 0.54
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.27
    Thistlethorn Acorn:
      total: 0.6
      efficiency: 0.86
      win: 0.51
      pick: 0.25
      fit: 0.41
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.56
      pick: 0.13
      fit: 0.23
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.17
      fit: 0.23
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.53
      pick: 0.31
      fit: 0.68
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  flex_slots:
  - Briskberry Acorn
  - Genji's Guard
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
    god: Genji''s Guard, The Crusher, The Reaper, Hydra''s Lament, Pendulum Blade,
    Tekko-Kagi, Freya''s Tears, Runeforged Hammer, Silverbranch Bow, Arondight, Berserker''s
    Shield, Avatar''s Parashu, Riptalon, Shield of the Phoenix, Amanita Charm, Lernaean
    Bow, Kinetic Cuirass, Screeching Gargoyle, Tyrfing, Shield Splitter, Golden Blade,
    Avenging Blade, Toxic Blade, Transcendence.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.93
      win: 0.55
      pick: 0.24
      fit: 0.21
    Briskberry Acorn:
      total: 0.53
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.21
    Thistlethorn Acorn:
      total: 0.6
      efficiency: 0.86
      win: 0.51
      pick: 0.25
      fit: 0.42
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.56
      pick: 0.13
      fit: 0.21
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.17
      fit: 0.21
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.53
      pick: 0.31
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Briskberry Acorn
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Kinetic Cuirass, Shield of the Phoenix,
    The Reaper, Berserker''s Shield, Runeforged Hammer, Shield Splitter, Shifter''s
    Shield, The Crusher, Freya''s Tears, Eye of the Storm, Phoenix Feather, Erosion,
    Eye of Providence, Yogi''s Necklace, Spectral Armor, Riptalon, Draconic Scale,
    Mantle Of Discord, Stone of Binding, Chandra''s Grace, Golden Blade, Avenging
    Blade, Leviathan''s Hide.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.93
      win: 0.55
      pick: 0.24
      fit: 0.42
    Briskberry Acorn:
      total: 0.56
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.42
    Thistlethorn Acorn:
      total: 0.61
      efficiency: 0.86
      win: 0.51
      pick: 0.25
      fit: 0.46
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.17
      fit: 0.2
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.53
      pick: 0.31
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.83
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - Briskberry Acorn
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, The Reaper, Tekko-Kagi, Avatar''s Parashu, Pendulum
    Blade, Genji''s Guard, Silverbranch Bow, Avenging Blade, Riptalon, Toxic Blade,
    Hydra''s Lament, Runeforged Hammer, Stone of Binding, Screeching Gargoyle, Lernaean
    Bow, Tyrfing, Golden Blade, Berserker''s Shield, Shield Splitter, Oath-Sworn Spear,
    Transcendence, Amanita Charm, Arondight, Eye of the Storm.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.63
      efficiency: 0.93
      win: 0.55
      pick: 0.24
      fit: 0.3
    Briskberry Acorn:
      total: 0.54
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.3
    Thistlethorn Acorn:
      total: 0.59
      efficiency: 0.86
      win: 0.51
      pick: 0.25
      fit: 0.35
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.67
      pick: 0.17
      fit: 0.05
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.53
      pick: 0.31
      fit: 0.92
    The Crusher:
      total: 0.56
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.97
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  flex_slots:
  - Riptalon
  - Tyrfing
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
    this god: Riptalon, Tyrfing, Silverbranch Bow, Golden Blade, Berserker''s Shield,
    Genji''s Guard, Tekko-Kagi, Lernaean Bow, Toxic Blade, The Crusher, The Reaper,
    Dominance, Pharaoh''s Curse, Qin''s Blade, Runeforged Hammer, Hydra''s Lament,
    Shogun''s Ofuda, Amanita Charm, Kinetic Cuirass, Sun Beam Bow, Freya''s Tears,
    Shield Splitter, Eye of Providence, Avenging Blade.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.66
      efficiency: 0.93
      win: 0.55
      pick: 0.24
      fit: 0.48
    Thistlethorn Acorn:
      total: 0.59
      efficiency: 0.86
      win: 0.51
      pick: 0.25
      fit: 0.31
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.67
      pick: 0.17
      fit: 0.04
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.31
      fit: 0.37
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.47
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  flex_slots:
  - Genji's Guard
  - Briskberry Acorn
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Hydra''s Lament, Freya''s
    Tears, Shield of the Phoenix, Pendulum Blade, Arondight, The Crusher, Screeching
    Gargoyle, Chandra''s Grace, The Reaper, Berserker''s Shield, Eye of Erebus, Runeforged
    Hammer, Amanita Charm, Kinetic Cuirass, Prophetic Cloak, Gladiator''s Shield,
    Silverbranch Bow, Tekko-Kagi, Lernaean Bow, Riptalon, Eye of Providence, Tyrfing,
    Shield Splitter.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.61
      efficiency: 0.93
      win: 0.55
      pick: 0.24
      fit: 0.14
    Briskberry Acorn:
      total: 0.52
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.14
    Thistlethorn Acorn:
      total: 0.63
      efficiency: 0.86
      win: 0.51
      pick: 0.25
      fit: 0.61
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.13
      fit: 0.47
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.17
      fit: 0.47
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.53
      pick: 0.31
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  flex_slots:
  - The Crusher
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
    Underrated for this god: The Crusher, The Reaper, Tekko-Kagi, Hydra''s Lament,
    Runeforged Hammer, Pendulum Blade, Avatar''s Parashu, Tyrfing, Golden Blade, Lernaean
    Bow, Shield Splitter, Avenging Blade, Arondight, Silverbranch Bow, Transcendence,
    Eye of the Storm, Riptalon, Deathbringer, Damaru, Genji''s Guard, Dominance, Berserker''s
    Shield, Toxic Blade, Musashi''s Dual Swords.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.93
      win: 0.55
      pick: 0.24
      fit: 0.46
    Briskberry Acorn:
      total: 0.57
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.46
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.86
      win: 0.51
      pick: 0.25
      fit: 0.54
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.53
      pick: 0.31
      fit: 0.88
    The Crusher:
      total: 0.55
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.91
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.43
      pick: 0.23
      fit: 1.0
  starter: *id001
---
