---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.33
  aspect_win_rate: 0.58
  slot_order:
  - name: Briskberry Acorn
    pick_rate: 0.45
    win_rate: 0.5
    alternates:
    - name: Ashwhorl Acorn
      pick_rate: 0.27
      win_rate: 0.59
    - name: Thistlethorn Acorn
      pick_rate: 0.22
      win_rate: 0.52
  - name: Thistlethorn Acorn
    pick_rate: 0.37
    win_rate: 0.52
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.33
      win_rate: 0.55
    - name: Ashwhorl Acorn
      pick_rate: 0.09
      win_rate: 0.47
  - name: Jotunn's Revenge
    pick_rate: 0.31
    win_rate: 0.5
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.17
      win_rate: 0.54
    - name: Briskberry Acorn
      pick_rate: 0.12
      win_rate: 0.56
  - name: The Crusher
    pick_rate: 0.16
    win_rate: 0.46
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.54
    - name: Jotunn's Revenge
      pick_rate: 0.13
      win_rate: 0.48
  - name: Heartseeker
    pick_rate: 0.29
    win_rate: 0.49
    alternates:
    - name: The Crusher
      pick_rate: 0.11
      win_rate: 0.47
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.68
  - name: Titan's Bane
    pick_rate: 0.07
    win_rate: 0.47
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.51
    - name: Avatar's Parashu
      pick_rate: 0.07
      win_rate: 0.65
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.26
    win_rate: 0.65
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.48
  - name: Bluestone Pendant
    pick_rate: 0.14
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-11-03'
  god_win_rate: 0.5266106442577031
  god_matches_won: 564
  god_matches_played: 1071
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Briskberry Acorn
  - Titan's Bane
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Tekko-Kagi, Hydra''s Lament, Pendulum Blade, Arondight,
    Tyrfing, Transcendence, Runeforged Hammer, Avenging Blade, Shield Splitter, Eye
    of the Storm, Golden Blade, Dominance, Bloodforge, Lernaean Bow, Silverbranch
    Bow, Oath-Sworn Spear, Barbed Carver, Toxic Blade, Rage, Musashi''s Dual Swords,
    Riptalon.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.6
      efficiency: 0.7
      win: 0.59
      pick: 0.27
      fit: 0.52
    Briskberry Acorn:
      total: 0.58
      efficiency: 0.74
      win: 0.5
      pick: 0.45
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.6
      efficiency: 0.72
      win: 0.52
      pick: 0.5
      fit: 0.61
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.67
      win: 0.5
      pick: 0.48
      fit: 1.0
    Titan's Bane:
      total: 0.56
      efficiency: 0.54
      win: 0.47
      pick: 0.22
      fit: 1.0
    Avatar's Parashu:
      total: 0.6
      efficiency: 0.44
      win: 0.65
      pick: 0.22
      fit: 0.91
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Titan's Bane
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Hydra''s Lament, Arondight, The Reaper, Transcendence, Tekko-Kagi, Pendulum
    Blade, Tyrfing, Runeforged Hammer, Dominance, Avenging Blade, Shield Splitter,
    Eye of the Storm, Bloodforge, Lernaean Bow, Damaru, Breastplate of Valor, Golden
    Blade, Chandra''s Grace, Oath-Sworn Spear, Barbed Carver, Silverbranch Bow.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.57
      efficiency: 0.7
      win: 0.59
      pick: 0.27
      fit: 0.29
    Briskberry Acorn:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.45
      fit: 0.29
    Thistlethorn Acorn:
      total: 0.57
      efficiency: 0.72
      win: 0.52
      pick: 0.5
      fit: 0.43
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.5
      pick: 0.48
      fit: 0.71
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.39
    Heartseeker:
      total: 0.52
      efficiency: 0.43
      win: 0.49
      pick: 0.63
      fit: 0.77
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Briskberry Acorn
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Genji''s Guard, Hydra''s Lament, The Reaper, Pendulum Blade, Arondight, Tekko-Kagi,
    Transcendence, Tyrfing, Runeforged Hammer, Damaru, Avenging Blade, Silverbranch
    Bow, Shield Splitter, Eye of the Storm, Toxic Blade, Dominance, Breastplate of
    Valor, Bloodforge, Lernaean Bow, Chandra''s Grace, Golden Blade, Riptalon.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.56
      efficiency: 0.7
      win: 0.59
      pick: 0.27
      fit: 0.22
    Briskberry Acorn:
      total: 0.54
      efficiency: 0.74
      win: 0.5
      pick: 0.45
      fit: 0.22
    Thistlethorn Acorn:
      total: 0.58
      efficiency: 0.72
      win: 0.52
      pick: 0.5
      fit: 0.44
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.67
      win: 0.5
      pick: 0.48
      fit: 0.78
    Heartseeker:
      total: 0.52
      efficiency: 0.43
      win: 0.49
      pick: 0.63
      fit: 0.76
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.44
      win: 0.65
      pick: 0.22
      fit: 0.56
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Genji's Guard
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, Kinetic Cuirass, Shield Splitter, Berserker''s
    Shield, Shield of the Phoenix, The Reaper, Runeforged Hammer, Phoenix Feather,
    Yogi''s Necklace, Erosion, Eye of Providence, Freya''s Tears, Oni Hunter''s Garb,
    Draconic Scale, Avenging Blade, Breastplate of Valor, Midgardian Mail, Hydra''s
    Lament, Wyrmskin Hide, Shifter''s Shield, Leviathan''s Hide, Chandra''s Grace,
    Stone of Binding.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.63
      efficiency: 0.8
      win: 0.59
      pick: 0.27
      fit: 0.44
    Briskberry Acorn:
      total: 0.61
      efficiency: 0.84
      win: 0.5
      pick: 0.45
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.82
      win: 0.52
      pick: 0.5
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.5
      pick: 0.48
      fit: 0.44
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.68
      pick: 0.11
      fit: 0.21
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
  - Briskberry Acorn
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Tekko-Kagi, Pendulum Blade, Hydra''s Lament, Avenging
    Blade, Silverbranch Bow, Arondight, Toxic Blade, Tyrfing, Oath-Sworn Spear, Transcendence,
    Runeforged Hammer, Riptalon, Shield Splitter, Eye of the Storm, Dominance, Bloodforge,
    Lernaean Bow, Golden Blade, Barbed Carver, Screeching Gargoyle, Damaru.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.57
      efficiency: 0.7
      win: 0.59
      pick: 0.27
      fit: 0.33
    Briskberry Acorn:
      total: 0.56
      efficiency: 0.74
      win: 0.5
      pick: 0.45
      fit: 0.33
    Thistlethorn Acorn:
      total: 0.57
      efficiency: 0.72
      win: 0.52
      pick: 0.5
      fit: 0.38
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.67
      win: 0.5
      pick: 0.48
      fit: 1.0
    Titan's Bane:
      total: 0.56
      efficiency: 0.54
      win: 0.47
      pick: 0.22
      fit: 1.0
    Avatar's Parashu:
      total: 0.6
      efficiency: 0.44
      win: 0.65
      pick: 0.22
      fit: 0.94
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Tyrfing
  - Tekko-Kagi
  flex_slots:
  - Tyrfing
  - Tekko-Kagi
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
    this god: Tyrfing, Tekko-Kagi, Silverbranch Bow, Riptalon, Golden Blade, Lernaean
    Bow, Toxic Blade, The Reaper, Dominance, Qin''s Blade, Hydra''s Lament, Sun Beam
    Bow, Arondight, Berserker''s Shield, Bloodforge, Transcendence, Dagger of Frenzy,
    Runeforged Hammer, Pendulum Blade, Avenging Blade, Barbed Carver, Vital Amplifier.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.76
      win: 0.59
      pick: 0.27
      fit: 0.48
    Briskberry Acorn:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.45
      fit: 0.17
    Thistlethorn Acorn:
      total: 0.57
      efficiency: 0.75
      win: 0.52
      pick: 0.5
      fit: 0.31
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.5
      pick: 0.48
      fit: 0.37
    Tyrfing:
      total: 0.52
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.79
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Genji's Guard
  - Hydra's Lament
  flex_slots:
  - Hydra's Lament
  - Briskberry Acorn
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Hydra''s Lament, Arondight,
    Pendulum Blade, Damaru, The Reaper, Breastplate of Valor, Chandra''s Grace, Tekko-Kagi,
    Transcendence, Tyrfing, Eye of Erebus, Screeching Gargoyle, Runeforged Hammer,
    Freya''s Tears, Avenging Blade, Shield Splitter, Shield of the Phoenix, Eye of
    the Storm, Silverbranch Bow, Dominance, Bloodforge.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.55
      efficiency: 0.7
      win: 0.59
      pick: 0.27
      fit: 0.15
    Briskberry Acorn:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.45
      fit: 0.15
    Thistlethorn Acorn:
      total: 0.61
      efficiency: 0.72
      win: 0.52
      pick: 0.5
      fit: 0.65
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.48
      fit: 0.85
    Genji's Guard:
      total: 0.55
      efficiency: 0.48
      win: 0.68
      pick: 0.11
      fit: 0.5
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.75
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Genji's Guard
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
  - Ashwhorl Acorn
  - The Crusher
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
    Underrated for this god: The Reaper, Tekko-Kagi, Hydra''s Lament, Pendulum Blade,
    Arondight, Tyrfing, Transcendence, Runeforged Hammer, Avenging Blade, Shield Splitter,
    Eye of the Storm, Golden Blade, Dominance, Bloodforge, Lernaean Bow, Silverbranch
    Bow, Oath-Sworn Spear, Barbed Carver, Toxic Blade, Rage, Musashi''s Dual Swords,
    Riptalon.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.6
      efficiency: 0.7
      win: 0.59
      pick: 0.27
      fit: 0.52
    Briskberry Acorn:
      total: 0.58
      efficiency: 0.74
      win: 0.5
      pick: 0.45
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.6
      efficiency: 0.72
      win: 0.52
      pick: 0.5
      fit: 0.61
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.67
      win: 0.5
      pick: 0.48
      fit: 1.0
    The Crusher:
      total: 0.54
      efficiency: 0.49
      win: 0.46
      pick: 0.27
      fit: 1.0
    Titan's Bane:
      total: 0.56
      efficiency: 0.54
      win: 0.47
      pick: 0.22
      fit: 1.0
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
---
