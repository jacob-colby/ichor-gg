---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Briskberry Acorn
    pick_rate: 1.0
    win_rate: 0.25
  - name: Thistlethorn Acorn
    pick_rate: 0.5
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.25
      win_rate: 0.0
    - name: Magic Acorn
      pick_rate: 0.25
      win_rate: 0.0
  - name: Jotunn's Revenge
    pick_rate: 0.25
    win_rate: 0.0
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.5
      win_rate: 0.0
    - name: The Crusher
      pick_rate: 0.25
      win_rate: 1.0
  - name: Heartseeker
    pick_rate: 0.25
    win_rate: 0.0
    alternates:
    - name: Transcendence
      pick_rate: 0.25
      win_rate: 0.0
    - name: The Crusher
      pick_rate: 0.25
      win_rate: 0.0
  - name: Pendulum Blade
    pick_rate: 0.33
    win_rate: 0.0
    alternates:
    - name: Heartseeker
      pick_rate: 0.33
      win_rate: 0.0
    - name: Axe
      pick_rate: 0.33
      win_rate: 1.0
  - name: Avatar's Parashu
    pick_rate: 1.0
    win_rate: 0.0
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.5
    win_rate: 0.5
  - name: Bumba's Hammer
    pick_rate: 0.5
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-11-04'
  god_win_rate: 0.25
  god_matches_won: 1
  god_matches_played: 4
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Titan''s Bane, Ashwhorl Acorn, The Reaper, Tekko-Kagi, Hydra''s Lament,
    Arondight, Tyrfing, Runeforged Hammer, Avenging Blade, Shield Splitter, Eye of
    the Storm, Golden Blade, Dominance, Bloodforge, Lernaean Bow, Silverbranch Bow,
    Oath-Sworn Spear, Barbed Carver, Toxic Blade, Rage, Musashi''s Dual Swords, Riptalon.'
  slot_scores:
    Briskberry Acorn:
      total: 0.5
      efficiency: 0.74
      win: 0.25
      pick: 1.0
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.68
      fit: 0.61
    Jotunn's Revenge:
      total: 0.4
      efficiency: 0.67
      win: 0.0
      pick: 0.39
      fit: 1.0
    The Crusher:
      total: 0.34
      efficiency: 0.49
      win: 0.0
      pick: 0.42
      fit: 1.0
    Titan's Bane:
      total: 0.34
      efficiency: 0.54
      win: 0.0
      pick: 0.0
      fit: 1.0
    Avatar's Parashu:
      total: 0.34
      efficiency: 0.44
      win: 0.0
      pick: 1.0
      fit: 0.91
  community_ordered:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
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
  - Hydra's Lament
  flex_slots:
  - Ashwhorl Acorn
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Ashwhorl Acorn, Titan''s Bane, Arondight, The Reaper, Tekko-Kagi, Tyrfing,
    Runeforged Hammer, Dominance, Avenging Blade, Shield Splitter, Eye of the Storm,
    Genji''s Guard, Bloodforge, Lernaean Bow, Damaru, Breastplate of Valor, Golden
    Blade, Chandra''s Grace, Oath-Sworn Spear, Barbed Carver, Silverbranch Bow.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.29
      efficiency: 0.7
      win: 0.0
      pick: 0.0
      fit: 0.29
    Briskberry Acorn:
      total: 0.46
      efficiency: 0.74
      win: 0.25
      pick: 1.0
      fit: 0.29
    Thistlethorn Acorn:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.68
      fit: 0.43
    Jotunn's Revenge:
      total: 0.36
      efficiency: 0.67
      win: 0.0
      pick: 0.39
      fit: 0.71
    Transcendence:
      total: 0.26
      efficiency: 0.53
      win: 0.0
      pick: 0.42
      fit: 0.39
    Hydra's Lament:
      total: 0.29
      efficiency: 0.56
      win: 0.0
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Transcendence
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Pendulum Blade
  - Avatar's Parashu
  flex_slots:
  - The Crusher
  - Avatar's Parashu
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
    god: Titan''s Bane, Ashwhorl Acorn, Hydra''s Lament, The Reaper, Arondight, Tekko-Kagi,
    Tyrfing, Runeforged Hammer, Damaru, Avenging Blade, Genji''s Guard, Silverbranch
    Bow, Shield Splitter, Eye of the Storm, Toxic Blade, Dominance, Breastplate of
    Valor, Bloodforge, Lernaean Bow, Chandra''s Grace, Golden Blade, Riptalon.'
  slot_scores:
    Briskberry Acorn:
      total: 0.45
      efficiency: 0.74
      win: 0.25
      pick: 1.0
      fit: 0.22
    Thistlethorn Acorn:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.68
      fit: 0.44
    Jotunn's Revenge:
      total: 0.37
      efficiency: 0.67
      win: 0.0
      pick: 0.39
      fit: 0.78
    The Crusher:
      total: 0.29
      efficiency: 0.49
      win: 0.0
      pick: 0.42
      fit: 0.66
    Pendulum Blade:
      total: 0.3
      efficiency: 0.41
      win: 0.0
      pick: 0.71
      fit: 0.78
    Avatar's Parashu:
      total: 0.29
      efficiency: 0.44
      win: 0.0
      pick: 1.0
      fit: 0.56
  community_ordered:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Pendulum Blade
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Ashwhorl Acorn, Kinetic Cuirass, Shield Splitter, Berserker''s
    Shield, Shield of the Phoenix, The Reaper, Runeforged Hammer, Genji''s Guard,
    Phoenix Feather, Yogi''s Necklace, Titan''s Bane, Erosion, Eye of Providence,
    Freya''s Tears, Oni Hunter''s Garb, Draconic Scale, Avenging Blade, Breastplate
    of Valor, Midgardian Mail, Hydra''s Lament, Wyrmskin Hide, Shifter''s Shield,
    Leviathan''s Hide, Chandra''s Grace, Stone of Binding.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.35
      efficiency: 0.8
      win: 0.0
      pick: 0.0
      fit: 0.44
    Briskberry Acorn:
      total: 0.52
      efficiency: 0.84
      win: 0.25
      pick: 1.0
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.82
      win: 0.5
      pick: 0.68
      fit: 0.48
    Jotunn's Revenge:
      total: 0.32
      efficiency: 0.67
      win: 0.0
      pick: 0.39
      fit: 0.44
    Kinetic Cuirass:
      total: 0.29
      efficiency: 0.56
      win: 0.0
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.36
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - The Crusher
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Titan''s Bane, The Reaper, Tekko-Kagi, Ashwhorl Acorn, Hydra''s
    Lament, Avenging Blade, Silverbranch Bow, Arondight, Toxic Blade, Tyrfing, Oath-Sworn
    Spear, Runeforged Hammer, Riptalon, Shield Splitter, Eye of the Storm, Dominance,
    Bloodforge, Lernaean Bow, Golden Blade, Barbed Carver, Screeching Gargoyle, Damaru.'
  slot_scores:
    Briskberry Acorn:
      total: 0.47
      efficiency: 0.74
      win: 0.25
      pick: 1.0
      fit: 0.33
    Thistlethorn Acorn:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.68
      fit: 0.38
    Jotunn's Revenge:
      total: 0.4
      efficiency: 0.67
      win: 0.0
      pick: 0.39
      fit: 1.0
    The Crusher:
      total: 0.34
      efficiency: 0.49
      win: 0.0
      pick: 0.42
      fit: 1.0
    Titan's Bane:
      total: 0.34
      efficiency: 0.54
      win: 0.0
      pick: 0.0
      fit: 1.0
    Avatar's Parashu:
      total: 0.35
      efficiency: 0.44
      win: 0.0
      pick: 1.0
      fit: 0.94
  community_ordered:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Ashwhorl Acorn, Tyrfing, Tekko-Kagi, Silverbranch Bow, Riptalon, Golden
    Blade, Lernaean Bow, Toxic Blade, The Reaper, Titan''s Bane, Dominance, Qin''s
    Blade, Hydra''s Lament, Sun Beam Bow, Arondight, Berserker''s Shield, Bloodforge,
    Dagger of Frenzy, Runeforged Hammer, Avenging Blade, Barbed Carver, Vital Amplifier.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.34
      efficiency: 0.76
      win: 0.0
      pick: 0.0
      fit: 0.48
    Briskberry Acorn:
      total: 0.45
      efficiency: 0.74
      win: 0.25
      pick: 1.0
      fit: 0.17
    Thistlethorn Acorn:
      total: 0.57
      efficiency: 0.75
      win: 0.5
      pick: 0.68
      fit: 0.31
    Jotunn's Revenge:
      total: 0.31
      efficiency: 0.67
      win: 0.0
      pick: 0.39
      fit: 0.37
    Tyrfing:
      total: 0.29
      efficiency: 0.5
      win: 0.0
      pick: 0.0
      fit: 0.79
    Tekko-Kagi:
      total: 0.29
      efficiency: 0.55
      win: 0.0
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Pendulum Blade
  flex_slots:
  - Hydra's Lament
  - Arondight
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Arondight, Ashwhorl
    Acorn, Titan''s Bane, Damaru, Genji''s Guard, The Reaper, Breastplate of Valor,
    Chandra''s Grace, Tekko-Kagi, Tyrfing, Eye of Erebus, Screeching Gargoyle, Runeforged
    Hammer, Freya''s Tears, Avenging Blade, Shield Splitter, Shield of the Phoenix,
    Eye of the Storm, Silverbranch Bow, Dominance, Bloodforge.'
  slot_scores:
    Briskberry Acorn:
      total: 0.44
      efficiency: 0.74
      win: 0.25
      pick: 1.0
      fit: 0.15
    Thistlethorn Acorn:
      total: 0.61
      efficiency: 0.72
      win: 0.5
      pick: 0.68
      fit: 0.65
    Jotunn's Revenge:
      total: 0.38
      efficiency: 0.67
      win: 0.0
      pick: 0.39
      fit: 0.85
    Hydra's Lament:
      total: 0.31
      efficiency: 0.56
      win: 0.0
      pick: 0.0
      fit: 0.75
    Arondight:
      total: 0.29
      efficiency: 0.54
      win: 0.0
      pick: 0.0
      fit: 0.65
    Pendulum Blade:
      total: 0.31
      efficiency: 0.41
      win: 0.0
      pick: 0.71
      fit: 0.85
  community_ordered:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Pendulum Blade
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
    Underrated for this god: Titan''s Bane, Ashwhorl Acorn, The Reaper, Tekko-Kagi,
    Hydra''s Lament, Arondight, Tyrfing, Runeforged Hammer, Avenging Blade, Shield
    Splitter, Eye of the Storm, Golden Blade, Dominance, Bloodforge, Lernaean Bow,
    Silverbranch Bow, Oath-Sworn Spear, Barbed Carver, Toxic Blade, Rage, Musashi''s
    Dual Swords, Riptalon.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.32
      efficiency: 0.7
      win: 0.0
      pick: 0.0
      fit: 0.52
    Briskberry Acorn:
      total: 0.5
      efficiency: 0.74
      win: 0.25
      pick: 1.0
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.68
      fit: 0.61
    Jotunn's Revenge:
      total: 0.4
      efficiency: 0.67
      win: 0.0
      pick: 0.39
      fit: 1.0
    The Crusher:
      total: 0.34
      efficiency: 0.49
      win: 0.0
      pick: 0.42
      fit: 1.0
    Titan's Bane:
      total: 0.34
      efficiency: 0.54
      win: 0.0
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
---
