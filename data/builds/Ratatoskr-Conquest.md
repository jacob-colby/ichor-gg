---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.36
  aspect_win_rate: 0.54
  slot_order:
  - name: Briskberry Acorn
    pick_rate: 0.32
    win_rate: 0.43
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.3
      win_rate: 0.48
    - name: Ashwhorl Acorn
      pick_rate: 0.23
      win_rate: 0.55
  - name: Thistlethorn Acorn
    pick_rate: 0.19
    win_rate: 0.53
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.3
      win_rate: 0.49
    - name: Ashwhorl Acorn
      pick_rate: 0.14
      win_rate: 0.41
  - name: Jotunn's Revenge
    pick_rate: 0.22
    win_rate: 0.54
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.18
      win_rate: 0.51
    - name: Thistlethorn Acorn
      pick_rate: 0.13
      win_rate: 0.33
  - name: Heartseeker
    pick_rate: 0.14
    win_rate: 0.44
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.08
      win_rate: 0.44
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.28
  - name: Titan's Bane
    pick_rate: 0.1
    win_rate: 0.38
    alternates:
    - name: Heartseeker
      pick_rate: 0.18
      win_rate: 0.44
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.67
  - name: Lucerne Hammer
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.52
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.2
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.53
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.43
  - name: Bumba's Hammer
    pick_rate: 0.18
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-08-22'
  god_win_rate: 0.463519313304721
  god_matches_won: 108
  god_matches_played: 233
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
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  flex_slots:
  - The Crusher
  - Breastplate of Valor
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
    this god: The Crusher, The Reaper, Tekko-Kagi, Pendulum Blade, Hydra''s Lament,
    Avatar''s Parashu, Runeforged Hammer, Tyrfing, Golden Blade, Lernaean Bow, Shield
    Splitter, Arondight, Avenging Blade, Silverbranch Bow, Transcendence, Eye of the
    Storm, Riptalon, Deathbringer, Damaru, Dominance, Genji''s Guard, Toxic Blade,
    Musashi''s Dual Swords, Berserker''s Shield.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.66
      efficiency: 0.93
      win: 0.55
      pick: 0.23
      fit: 0.52
    Briskberry Acorn:
      total: 0.58
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.64
      efficiency: 0.86
      win: 0.53
      pick: 0.26
      fit: 0.61
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.67
      pick: 0.15
      fit: 0.09
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.54
      pick: 0.34
      fit: 1.0
    The Crusher:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  flex_slots:
  - Briskberry Acorn
  - Hydra's Lament
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Crusher, Hydra''s Lament, Genji''s Guard, The Reaper, Runeforged Hammer, Transcendence,
    Tekko-Kagi, Arondight, Pendulum Blade, Lernaean Bow, Berserker''s Shield, Freya''s
    Tears, Tyrfing, Shield Splitter, Golden Blade, Avenging Blade, Dominance, Amanita
    Charm, Avatar''s Parashu, Kinetic Cuirass, Eye of the Storm, Shield of the Phoenix,
    Deathbringer, Silverbranch Bow.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.63
      efficiency: 0.93
      win: 0.55
      pick: 0.23
      fit: 0.29
    Briskberry Acorn:
      total: 0.54
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.29
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.26
      fit: 0.43
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.15
      fit: 0.24
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.54
      pick: 0.34
      fit: 0.71
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  flex_slots:
  - Briskberry Acorn
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, The Reaper, Hydra''s Lament, Pendulum Blade, Genji''s Guard,
    Tekko-Kagi, Freya''s Tears, Runeforged Hammer, Silverbranch Bow, Arondight, Avatar''s
    Parashu, Berserker''s Shield, Riptalon, Shield of the Phoenix, Amanita Charm,
    Lernaean Bow, Screeching Gargoyle, Tyrfing, Kinetic Cuirass, Shield Splitter,
    Golden Blade, Avenging Blade, Toxic Blade, Transcendence.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.93
      win: 0.55
      pick: 0.23
      fit: 0.22
    Briskberry Acorn:
      total: 0.53
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.22
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.26
      fit: 0.44
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.15
      fit: 0.22
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.54
      pick: 0.34
      fit: 0.78
    The Crusher:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.66
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
  - Breastplate of Valor
  - Briskberry Acorn
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, The Reaper, Berserker''s
    Shield, Runeforged Hammer, Shield Splitter, Shifter''s Shield, The Crusher, Eye
    of the Storm, Freya''s Tears, Phoenix Feather, Erosion, Eye of Providence, Genji''s
    Guard, Draconic Scale, Spectral Armor, Yogi''s Necklace, Riptalon, Golden Blade,
    Mantle Of Discord, Stone of Binding, Chandra''s Grace, Avenging Blade, Leviathan''s
    Hide.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.93
      win: 0.55
      pick: 0.23
      fit: 0.44
    Briskberry Acorn:
      total: 0.57
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.26
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.15
      fit: 0.21
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.54
      pick: 0.34
      fit: 0.44
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.86
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
  - Briskberry Acorn
  - Breastplate of Valor
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
    for this god: The Crusher, The Reaper, Tekko-Kagi, Avatar''s Parashu, Pendulum
    Blade, Silverbranch Bow, Riptalon, Avenging Blade, Toxic Blade, Hydra''s Lament,
    Runeforged Hammer, Stone of Binding, Screeching Gargoyle, Tyrfing, Lernaean Bow,
    Golden Blade, Shield Splitter, Berserker''s Shield, Genji''s Guard, Oath-Sworn
    Spear, Transcendence, Arondight, Eye of the Storm, Amanita Charm.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.63
      efficiency: 0.93
      win: 0.55
      pick: 0.23
      fit: 0.33
    Briskberry Acorn:
      total: 0.55
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.33
    Thistlethorn Acorn:
      total: 0.61
      efficiency: 0.86
      win: 0.53
      pick: 0.26
      fit: 0.38
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.67
      pick: 0.15
      fit: 0.06
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.54
      pick: 0.34
      fit: 1.0
    The Crusher:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
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
    Tekko-Kagi, Lernaean Bow, Toxic Blade, The Crusher, The Reaper, Dominance, Pharaoh''s
    Curse, Qin''s Blade, Runeforged Hammer, Hydra''s Lament, Genji''s Guard, Shogun''s
    Ofuda, Amanita Charm, Kinetic Cuirass, Sun Beam Bow, Freya''s Tears, Shield Splitter,
    Eye of Providence, Avenging Blade.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.66
      efficiency: 0.93
      win: 0.55
      pick: 0.23
      fit: 0.48
    Thistlethorn Acorn:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.26
      fit: 0.31
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.67
      pick: 0.15
      fit: 0.04
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.34
      fit: 0.37
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Hydra''s Lament, Freya''s
    Tears, Pendulum Blade, Shield of the Phoenix, Arondight, Screeching Gargoyle,
    The Crusher, Chandra''s Grace, The Reaper, Eye of Erebus, Berserker''s Shield,
    Runeforged Hammer, Prophetic Cloak, Amanita Charm, Gladiator''s Shield, Kinetic
    Cuirass, Silverbranch Bow, Tekko-Kagi, Lernaean Bow, Riptalon, Tyrfing, Eye of
    Providence, Shield Splitter.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.61
      efficiency: 0.93
      win: 0.55
      pick: 0.23
      fit: 0.15
    Thistlethorn Acorn:
      total: 0.65
      efficiency: 0.86
      win: 0.53
      pick: 0.26
      fit: 0.65
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.15
      fit: 0.5
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.54
      pick: 0.34
      fit: 0.85
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Crusher
  - Titan's Bane
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
    Underrated for this god: The Crusher, The Reaper, Tekko-Kagi, Pendulum Blade,
    Hydra''s Lament, Avatar''s Parashu, Runeforged Hammer, Tyrfing, Golden Blade,
    Lernaean Bow, Shield Splitter, Arondight, Avenging Blade, Silverbranch Bow, Transcendence,
    Eye of the Storm, Riptalon, Deathbringer, Damaru, Dominance, Genji''s Guard, Toxic
    Blade, Musashi''s Dual Swords, Berserker''s Shield.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.66
      efficiency: 0.93
      win: 0.55
      pick: 0.23
      fit: 0.52
    Briskberry Acorn:
      total: 0.58
      efficiency: 0.83
      win: 0.43
      pick: 0.32
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.64
      efficiency: 0.86
      win: 0.53
      pick: 0.26
      fit: 0.61
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.54
      pick: 0.34
      fit: 1.0
    The Crusher:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.5
      efficiency: 0.47
      win: 0.38
      pick: 0.22
      fit: 1.0
  starter: *id001
---
