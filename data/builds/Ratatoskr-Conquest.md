---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.34
  aspect_win_rate: 0.58
  slot_order:
  - name: Briskberry Acorn
    pick_rate: 0.33
    win_rate: 0.43
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.3
      win_rate: 0.47
    - name: Ashwhorl Acorn
      pick_rate: 0.24
      win_rate: 0.57
  - name: Thistlethorn Acorn
    pick_rate: 0.19
    win_rate: 0.49
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.3
      win_rate: 0.51
    - name: Ashwhorl Acorn
      pick_rate: 0.12
      win_rate: 0.43
  - name: Jotunn's Revenge
    pick_rate: 0.22
    win_rate: 0.55
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.17
      win_rate: 0.45
    - name: Thistlethorn Acorn
      pick_rate: 0.12
      win_rate: 0.39
  - name: Heartseeker
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.24
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.56
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.19
      win_rate: 0.39
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.27
  - name: Lucerne Hammer
    pick_rate: 0.07
    win_rate: 0.33
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.52
    - name: The Reaper
      pick_rate: 0.05
      win_rate: 0.57
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.41
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.53
  - name: Bumba's Hammer
    pick_rate: 0.18
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-08-20'
  god_win_rate: 0.4717948717948718
  god_matches_won: 92
  god_matches_played: 195
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-20'
  god_matches_analyzed: 11556
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Hydra''s Lament, Pendulum Blade, Tekko-Kagi, Runeforged
    Hammer, Damaru, Lernaean Bow, Avatar''s Parashu, Golden Blade, Transcendence,
    Avenging Blade, Dominance, Arondight, Shield Splitter, Eye of the Storm, Tyrfing,
    Riptalon, Silverbranch Bow, Deathbringer, Barbed Carver, Berserker''s Shield,
    Sanguine Lash.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.68
      efficiency: 0.94
      win: 0.57
      pick: 0.24
      fit: 0.52
    Briskberry Acorn:
      total: 0.61
      efficiency: 0.93
      win: 0.43
      pick: 0.33
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.65
      efficiency: 0.92
      win: 0.49
      pick: 0.26
      fit: 0.61
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.67
      pick: 0.19
      fit: 0.09
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.64
      win: 0.55
      pick: 0.34
      fit: 1.0
    The Crusher:
      total: 0.61
      efficiency: 0.64
      win: 0.52
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
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Crusher, Hydra''s Lament, Runeforged Hammer, Damaru, Transcendence, Dominance,
    Pendulum Blade, Lernaean Bow, Arondight, Oni Hunter''s Garb, Berserker''s Shield,
    Golden Blade, Freya''s Tears, Tekko-Kagi, Avenging Blade, Kinetic Cuirass, Shield
    Splitter, Amanita Charm, Shield of the Phoenix, Eye of the Storm, Tyrfing, Eye
    of Providence.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.64
      efficiency: 0.94
      win: 0.57
      pick: 0.24
      fit: 0.29
    Briskberry Acorn:
      total: 0.58
      efficiency: 0.93
      win: 0.43
      pick: 0.33
      fit: 0.29
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.92
      win: 0.49
      pick: 0.26
      fit: 0.43
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.56
      pick: 0.15
      fit: 0.24
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.67
      pick: 0.19
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.55
      pick: 0.34
      fit: 0.71
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Hydra''s Lament, Pendulum Blade, Runeforged Hammer, Freya''s
    Tears, Tekko-Kagi, Riptalon, Arondight, Damaru, Silverbranch Bow, Shield of the
    Phoenix, Berserker''s Shield, Lernaean Bow, Kinetic Cuirass, Amanita Charm, Screeching
    Gargoyle, Golden Blade, Chandra''s Grace, Eye of Providence, Transcendence, Avenging
    Blade, Oni Hunter''s Garb.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.63
      efficiency: 0.94
      win: 0.57
      pick: 0.24
      fit: 0.22
    Briskberry Acorn:
      total: 0.57
      efficiency: 0.93
      win: 0.43
      pick: 0.33
      fit: 0.22
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.92
      win: 0.49
      pick: 0.26
      fit: 0.44
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.67
      pick: 0.19
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.55
      pick: 0.34
      fit: 0.78
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.52
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
  - Jotunn's Revenge
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, The Crusher,
    Berserker''s Shield, Yogi''s Necklace, Runeforged Hammer, Oni Hunter''s Garb,
    Eye of the Storm, Chandra''s Grace, Erosion, Shifter''s Shield, Shield Splitter,
    Phoenix Feather, Freya''s Tears, Eye of Providence, Spectral Armor, Draconic Scale,
    Riptalon, Golden Blade, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Leviathan''s
    Hide.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.67
      efficiency: 0.94
      win: 0.57
      pick: 0.24
      fit: 0.44
    Briskberry Acorn:
      total: 0.6
      efficiency: 0.93
      win: 0.43
      pick: 0.33
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.63
      efficiency: 0.92
      win: 0.49
      pick: 0.26
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.67
      pick: 0.19
      fit: 0.21
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.55
      pick: 0.34
      fit: 0.44
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.52
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Tekko-Kagi, Pendulum Blade, Riptalon, Avenging Blade,
    Silverbranch Bow, Avatar''s Parashu, Hydra''s Lament, Runeforged Hammer, Damaru,
    Toxic Blade, Lernaean Bow, Screeching Gargoyle, Golden Blade, Transcendence, Berserker''s
    Shield, Dominance, Shield Splitter, Eye of the Storm, Stone of Binding, Tyrfing,
    Oath-Sworn Spear.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.94
      win: 0.57
      pick: 0.24
      fit: 0.33
    Briskberry Acorn:
      total: 0.59
      efficiency: 0.93
      win: 0.43
      pick: 0.33
      fit: 0.33
    Thistlethorn Acorn:
      total: 0.61
      efficiency: 0.92
      win: 0.49
      pick: 0.26
      fit: 0.38
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.67
      pick: 0.19
      fit: 0.06
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.64
      win: 0.55
      pick: 0.34
      fit: 1.0
    The Crusher:
      total: 0.61
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Riptalon
  flex_slots:
  - Riptalon
  - Golden Blade
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
    this god: Riptalon, The Crusher, Golden Blade, Silverbranch Bow, Tyrfing, Berserker''s
    Shield, Lernaean Bow, Toxic Blade, Dominance, Tekko-Kagi, Hydra''s Lament, Pharaoh''s
    Curse, Qin''s Blade, Runeforged Hammer, Damaru, Shogun''s Ofuda, Kinetic Cuirass,
    Amanita Charm, Eye of Providence, Oni Hunter''s Garb, Eros'' Bow, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.69
    Ashwhorl Acorn:
      total: 0.67
      efficiency: 0.94
      win: 0.57
      pick: 0.24
      fit: 0.48
    Briskberry Acorn:
      total: 0.56
      efficiency: 0.93
      win: 0.43
      pick: 0.33
      fit: 0.17
    Thistlethorn Acorn:
      total: 0.6
      efficiency: 0.92
      win: 0.49
      pick: 0.26
      fit: 0.31
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.55
      pick: 0.34
      fit: 0.37
    Riptalon:
      total: 0.54
      efficiency: 0.53
      win: 0.52
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, The Crusher, Freya''s
    Tears, Shield of the Phoenix, Pendulum Blade, Arondight, Screeching Gargoyle,
    Chandra''s Grace, Gladiator''s Shield, Runeforged Hammer, Berserker''s Shield,
    Prophetic Cloak, Kinetic Cuirass, Damaru, Amanita Charm, Riptalon, Eye of Providence,
    Oni Hunter''s Garb, Regrowth Striders, Lernaean Bow, Silverbranch Bow, Golden
    Blade.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.94
      win: 0.57
      pick: 0.24
      fit: 0.15
    Briskberry Acorn:
      total: 0.56
      efficiency: 0.93
      win: 0.43
      pick: 0.33
      fit: 0.15
    Thistlethorn Acorn:
      total: 0.65
      efficiency: 0.92
      win: 0.49
      pick: 0.26
      fit: 0.65
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.56
      pick: 0.15
      fit: 0.5
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.64
      win: 0.67
      pick: 0.19
      fit: 0.5
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.55
      pick: 0.34
      fit: 0.85
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
  - Jotunn's Revenge
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
    Underrated for this god: The Crusher, Hydra''s Lament, Pendulum Blade, Tekko-Kagi,
    Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s Parashu, Golden Blade, Transcendence,
    Avenging Blade, Dominance, Arondight, Shield Splitter, Eye of the Storm, Tyrfing,
    Riptalon, Silverbranch Bow, Deathbringer, Barbed Carver, Berserker''s Shield,
    Sanguine Lash.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.68
      efficiency: 0.94
      win: 0.57
      pick: 0.24
      fit: 0.52
    Briskberry Acorn:
      total: 0.61
      efficiency: 0.93
      win: 0.43
      pick: 0.33
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.65
      efficiency: 0.92
      win: 0.49
      pick: 0.26
      fit: 0.61
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.64
      win: 0.55
      pick: 0.34
      fit: 1.0
    The Crusher:
      total: 0.61
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.44
      efficiency: 0.45
      win: 0.27
      pick: 0.19
      fit: 1.0
  starter: *id001
---
