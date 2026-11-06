---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.37
  aspect_win_rate: 0.64
  slot_order:
  - name: Briskberry Acorn
    pick_rate: 0.49
    win_rate: 0.57
    alternates:
    - name: Ashwhorl Acorn
      pick_rate: 0.29
      win_rate: 0.65
    - name: Thistlethorn Acorn
      pick_rate: 0.15
      win_rate: 0.45
  - name: Thistlethorn Acorn
    pick_rate: 0.36
    win_rate: 0.57
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.34
      win_rate: 0.62
    - name: Ashwhorl Acorn
      pick_rate: 0.09
      win_rate: 0.73
  - name: Jotunn's Revenge
    pick_rate: 0.31
    win_rate: 0.57
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.25
      win_rate: 0.66
    - name: Briskberry Acorn
      pick_rate: 0.11
      win_rate: 0.55
  - name: Heartseeker
    pick_rate: 0.15
    win_rate: 0.38
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.15
      win_rate: 0.59
    - name: The Crusher
      pick_rate: 0.11
      win_rate: 0.73
  - name: The Crusher
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.29
      win_rate: 0.63
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.83
  - name: Avatar's Parashu
    pick_rate: 0.09
    win_rate: 0.8
    alternates:
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.5
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.4
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.28
    win_rate: 0.59
  - name: Bluestone Brooch
    pick_rate: 0.25
    win_rate: 0.72
  - name: Bluestone Pendant
    pick_rate: 0.12
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-11-06'
  god_win_rate: 0.5833333333333334
  god_matches_won: 161
  god_matches_played: 276
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Titan''s Bane, Hydra''s Lament, Tyrfing, Pendulum Blade,
    Tekko-Kagi, Arondight, Transcendence, Runeforged Hammer, Dominance, Shield Splitter,
    Eye of the Storm, Avenging Blade, Golden Blade, Lernaean Bow, Bloodforge, Rage,
    Barbed Carver, Silverbranch Bow, Toxic Blade, Oath-Sworn Spear, Devourer''s Gauntlet,
    Deathbringer.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.68
      win: 0.65
      pick: 0.29
      fit: 0.52
    Briskberry Acorn:
      total: 0.62
      efficiency: 0.73
      win: 0.57
      pick: 0.49
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.7
      win: 0.57
      pick: 0.49
      fit: 0.61
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.65
      win: 0.57
      pick: 0.48
      fit: 1.0
    Titan's Bane:
      total: 0.57
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 1.0
    Avatar's Parashu:
      total: 0.67
      efficiency: 0.46
      win: 0.8
      pick: 0.28
      fit: 0.91
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Avatar's Parashu
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Titan''s Bane, The Reaper, Arondight, Tyrfing, Transcendence, Pendulum
    Blade, Dominance, Tekko-Kagi, Runeforged Hammer, Genji''s Guard, Shield Splitter,
    Eye of the Storm, Avenging Blade, Damaru, Breastplate of Valor, Chandra''s Grace,
    Lernaean Bow, Golden Blade, Bloodforge, Rage, Barbed Carver, Yogi''s Necklace.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.59
      efficiency: 0.68
      win: 0.65
      pick: 0.29
      fit: 0.29
    Thistlethorn Acorn:
      total: 0.59
      efficiency: 0.7
      win: 0.57
      pick: 0.49
      fit: 0.43
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.65
      win: 0.57
      pick: 0.48
      fit: 0.71
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.63
    Avatar's Parashu:
      total: 0.6
      efficiency: 0.46
      win: 0.8
      pick: 0.28
      fit: 0.47
  community_ordered:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Freya's Tears
  - Avatar's Parashu
  flex_slots:
  - Briskberry Acorn
  - Freya's Tears
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
    god: Hydra''s Lament, Titan''s Bane, The Reaper, Pendulum Blade, Arondight, Tyrfing,
    Tekko-Kagi, Damaru, Genji''s Guard, Transcendence, Runeforged Hammer, Dominance,
    Silverbranch Bow, Shield Splitter, Eye of the Storm, Avenging Blade, Breastplate
    of Valor, Toxic Blade, Chandra''s Grace, Lernaean Bow, Golden Blade, Bloodforge,
    Riptalon.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.58
      efficiency: 0.68
      win: 0.65
      pick: 0.29
      fit: 0.22
    Briskberry Acorn:
      total: 0.57
      efficiency: 0.73
      win: 0.57
      pick: 0.49
      fit: 0.22
    Thistlethorn Acorn:
      total: 0.59
      efficiency: 0.7
      win: 0.57
      pick: 0.49
      fit: 0.44
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.65
      win: 0.57
      pick: 0.48
      fit: 0.78
    Freya's Tears:
      total: 0.55
      efficiency: 0.38
      win: 0.83
      pick: 0.15
      fit: 0.22
    Avatar's Parashu:
      total: 0.62
      efficiency: 0.46
      win: 0.8
      pick: 0.28
      fit: 0.56
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Freya's Tears
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Freya's Tears
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Avatar's Parashu
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Shield Splitter, The Reaper, Phoenix Feather, Genji''s Guard, Runeforged
    Hammer, Yogi''s Necklace, Draconic Scale, Oni Hunter''s Garb, Erosion, Eye of
    Providence, Shifter''s Shield, Breastplate of Valor, Chandra''s Grace, Midgardian
    Mail, Leviathan''s Hide, Hydra''s Lament, Wyrmskin Hide, Avenging Blade, Hide
    of the Nemean Lion.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.79
      win: 0.65
      pick: 0.29
      fit: 0.44
    Briskberry Acorn:
      total: 0.64
      efficiency: 0.84
      win: 0.57
      pick: 0.49
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.64
      efficiency: 0.81
      win: 0.57
      pick: 0.49
      fit: 0.48
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.83
      pick: 0.15
      fit: 0.38
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.46
      win: 0.8
      pick: 0.28
      fit: 0.4
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Freya's Tears
  - Avatar's Parashu
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
  - Thistlethorn Acorn
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Titan''s Bane, Tekko-Kagi, Pendulum Blade, Hydra''s
    Lament, Avenging Blade, Tyrfing, Silverbranch Bow, Arondight, Toxic Blade, Oath-Sworn
    Spear, Transcendence, Runeforged Hammer, Riptalon, Dominance, Shield Splitter,
    Eye of the Storm, Lernaean Bow, Golden Blade, Bloodforge, Rage, Barbed Carver,
    Screeching Gargoyle.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.6
      efficiency: 0.68
      win: 0.65
      pick: 0.29
      fit: 0.33
    Briskberry Acorn:
      total: 0.59
      efficiency: 0.73
      win: 0.57
      pick: 0.49
      fit: 0.33
    Thistlethorn Acorn:
      total: 0.58
      efficiency: 0.7
      win: 0.57
      pick: 0.49
      fit: 0.38
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.65
      win: 0.57
      pick: 0.48
      fit: 1.0
    Titan's Bane:
      total: 0.57
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 1.0
    Avatar's Parashu:
      total: 0.68
      efficiency: 0.46
      win: 0.8
      pick: 0.28
      fit: 0.94
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Avatar's Parashu
  flex_slots:
  - Tyrfing
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, Riptalon, Silverbranch Bow, Tekko-Kagi, The Reaper, Golden
    Blade, Toxic Blade, Lernaean Bow, Dominance, Qin''s Blade, Hydra''s Lament, Titan''s
    Bane, Dagger of Frenzy, Arondight, Berserker''s Shield, Sun Beam Bow, Bloodforge,
    Barbed Carver, Transcendence, Runeforged Hammer, Odysseus'' Bow, Pendulum Blade,
    Shield Splitter.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.63
      efficiency: 0.73
      win: 0.65
      pick: 0.29
      fit: 0.48
    Thistlethorn Acorn:
      total: 0.59
      efficiency: 0.74
      win: 0.57
      pick: 0.49
      fit: 0.31
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.48
      fit: 0.37
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.53
      efficiency: 0.45
      win: 0.57
      pick: 0.0
      fit: 0.79
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.46
      win: 0.8
      pick: 0.28
      fit: 0.33
  community_ordered:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Avatar's Parashu
  flex_slots:
  - Ashwhorl Acorn
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Arondight, Pendulum
    Blade, Damaru, Genji''s Guard, Titan''s Bane, Breastplate of Valor, The Reaper,
    Chandra''s Grace, Tyrfing, Screeching Gargoyle, Eye of Erebus, Shield of the Phoenix,
    Tekko-Kagi, Transcendence, Runeforged Hammer, Dominance, Gladiator''s Shield,
    Shield Splitter, Eye of the Storm, Avenging Blade, Silverbranch Bow.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.57
      efficiency: 0.68
      win: 0.65
      pick: 0.29
      fit: 0.15
    Thistlethorn Acorn:
      total: 0.63
      efficiency: 0.7
      win: 0.57
      pick: 0.49
      fit: 0.65
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.65
      win: 0.57
      pick: 0.48
      fit: 0.85
    Hydra's Lament:
      total: 0.56
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.75
    Freya's Tears:
      total: 0.59
      efficiency: 0.38
      win: 0.83
      pick: 0.15
      fit: 0.5
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.46
      win: 0.8
      pick: 0.28
      fit: 0.35
  community_ordered:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Freya's Tears
  - Avatar's Parashu
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
  - Titan's Bane
  - Ashwhorl Acorn
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
    Underrated for this god: The Reaper, Titan''s Bane, Hydra''s Lament, Tyrfing,
    Pendulum Blade, Tekko-Kagi, Arondight, Transcendence, Runeforged Hammer, Dominance,
    Shield Splitter, Eye of the Storm, Avenging Blade, Golden Blade, Lernaean Bow,
    Bloodforge, Rage, Barbed Carver, Silverbranch Bow, Toxic Blade, Oath-Sworn Spear,
    Devourer''s Gauntlet, Deathbringer.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.68
      win: 0.65
      pick: 0.29
      fit: 0.52
    Briskberry Acorn:
      total: 0.62
      efficiency: 0.73
      win: 0.57
      pick: 0.49
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.7
      win: 0.57
      pick: 0.49
      fit: 0.61
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.65
      win: 0.57
      pick: 0.48
      fit: 1.0
    The Crusher:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.22
      fit: 1.0
    Titan's Bane:
      total: 0.57
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
---
