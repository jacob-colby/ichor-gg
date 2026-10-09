---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.41
  slot_order:
  - name: Briskberry Acorn
    pick_rate: 0.52
    win_rate: 0.51
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.25
      win_rate: 0.62
    - name: Ashwhorl Acorn
      pick_rate: 0.11
      win_rate: 0.45
  - name: Thistlethorn Acorn
    pick_rate: 0.38
    win_rate: 0.49
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.29
      win_rate: 0.67
    - name: Ashwhorl Acorn
      pick_rate: 0.1
      win_rate: 0.4
  - name: Ashwhorl Acorn
    pick_rate: 0.2
    win_rate: 0.7
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.16
      win_rate: 0.56
    - name: Hydra's Lament
      pick_rate: 0.14
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.26
    win_rate: 0.6
    alternates:
    - name: Arondight
      pick_rate: 0.1
      win_rate: 0.9
    - name: Thistlethorn Acorn
      pick_rate: 0.09
      win_rate: 0.67
  - name: Titan's Bane
    pick_rate: 0.07
    win_rate: 0.83
    alternates:
    - name: Heartseeker
      pick_rate: 0.32
      win_rate: 0.66
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 1.0
  - name: Avatar's Parashu
    pick_rate: 0.18
    win_rate: 0.85
    alternates:
    - name: Titan's Bane
      pick_rate: 0.15
      win_rate: 0.36
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.43
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.22
    win_rate: 0.68
  - name: Bluestone Brooch
    pick_rate: 0.2
    win_rate: 0.45
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-10-09'
  god_win_rate: 0.5392156862745098
  god_matches_won: 55
  god_matches_played: 102
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-09'
  god_matches_analyzed: 2961
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Ashwhorl Acorn
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Jotunn's Revenge
  - Ashwhorl Acorn
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
    this god: The Crusher, The Reaper, Pendulum Blade, Tekko-Kagi, Tyrfing, Transcendence,
    Runeforged Hammer, Avenging Blade, Golden Blade, Lernaean Bow, Shield Splitter,
    Dominance, Silverbranch Bow, Oath-Sworn Spear, Barbed Carver, Riptalon, Bloodforge,
    Toxic Blade, Deathbringer, Eye of the Storm, Damaru, Rage.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.7
      win: 0.7
      pick: 0.31
      fit: 0.52
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.56
      pick: 0.25
      fit: 1.0
    Arondight:
      total: 0.68
      efficiency: 0.5
      win: 0.9
      pick: 0.17
      fit: 0.61
    The Crusher:
      total: 0.77
      efficiency: 0.47
      win: 1.0
      pick: 0.11
      fit: 1.0
    Titan's Bane:
      total: 0.7
      efficiency: 0.47
      win: 0.83
      pick: 0.15
      fit: 1.0
    Avatar's Parashu:
      total: 0.71
      efficiency: 0.45
      win: 0.85
      pick: 0.55
      fit: 0.91
  community_ordered:
  - Ashwhorl Acorn
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Arondight
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Crusher, The Reaper, Transcendence, Pendulum Blade, Runeforged Hammer, Tyrfing,
    Tekko-Kagi, Avenging Blade, Dominance, Breastplate of Valor, Lernaean Bow, Genji''s
    Guard, Shield Splitter, Golden Blade, Oath-Sworn Spear, Daybreak Gavel, Silverbranch
    Bow, Barbed Carver, Bloodforge, Riptalon, Yogi''s Necklace, Deathbringer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.56
      pick: 0.25
      fit: 0.71
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.65
      pick: 0.0
      fit: 0.39
    Arondight:
      total: 0.65
      efficiency: 0.5
      win: 0.9
      pick: 0.17
      fit: 0.43
    The Crusher:
      total: 0.7
      efficiency: 0.47
      win: 1.0
      pick: 0.11
      fit: 0.57
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.6
      pick: 0.43
      fit: 0.77
    Avatar's Parashu:
      total: 0.64
      efficiency: 0.45
      win: 0.85
      pick: 0.55
      fit: 0.47
  community_ordered:
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Jotunn's Revenge
  - Ashwhorl Acorn
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    god: The Crusher, Pendulum Blade, The Reaper, Tekko-Kagi, Transcendence, Runeforged
    Hammer, Tyrfing, Avenging Blade, Silverbranch Bow, Breastplate of Valor, Genji''s
    Guard, Riptalon, Lernaean Bow, Shield Splitter, Dominance, Toxic Blade, Daybreak
    Gavel, Golden Blade, Oath-Sworn Spear, Barbed Carver, Eye of Erebus, Screeching
    Gargoyle.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.61
      efficiency: 0.7
      win: 0.7
      pick: 0.31
      fit: 0.22
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.56
      pick: 0.25
      fit: 0.78
    Arondight:
      total: 0.66
      efficiency: 0.5
      win: 0.9
      pick: 0.17
      fit: 0.44
    The Crusher:
      total: 0.72
      efficiency: 0.47
      win: 1.0
      pick: 0.11
      fit: 0.66
    Titan's Bane:
      total: 0.64
      efficiency: 0.47
      win: 0.83
      pick: 0.15
      fit: 0.66
    Avatar's Parashu:
      total: 0.65
      efficiency: 0.45
      win: 0.85
      pick: 0.55
      fit: 0.56
  community_ordered:
  - Ashwhorl Acorn
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Arondight
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Avatar's Parashu
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix,
    Runeforged Hammer, The Reaper, Shield Splitter, Shifter''s Shield, Eye of the
    Storm, Freya''s Tears, Berserker''s Shield, Erosion, Eye of Providence, Genji''s
    Guard, Breastplate of Valor, Draconic Scale, Yogi''s Necklace, Phoenix Feather,
    Avenging Blade, Stone of Binding, Midgardian Mail, Chandra''s Grace, Daybreak
    Gavel, Hide of the Nemean Lion.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.68
      efficiency: 0.8
      win: 0.7
      pick: 0.31
      fit: 0.44
    Arondight:
      total: 0.63
      efficiency: 0.5
      win: 0.9
      pick: 0.17
      fit: 0.27
    The Crusher:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.11
      fit: 0.5
    Titan's Bane:
      total: 0.62
      efficiency: 0.47
      win: 0.83
      pick: 0.15
      fit: 0.5
    Avatar's Parashu:
      total: 0.63
      efficiency: 0.45
      win: 0.85
      pick: 0.55
      fit: 0.4
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Ashwhorl Acorn
  - Arondight
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ashwhorl Acorn
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Arondight
  - Ashwhorl Acorn
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
    for this god: The Crusher, The Reaper, Pendulum Blade, Tekko-Kagi, Avenging Blade,
    Silverbranch Bow, Riptalon, Oath-Sworn Spear, Transcendence, Tyrfing, Runeforged
    Hammer, Toxic Blade, Lernaean Bow, Shield Splitter, Dominance, Golden Blade, Barbed
    Carver, Screeching Gargoyle, Daybreak Gavel, Bloodforge, Breastplate of Valor,
    Genji''s Guard.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.7
      win: 0.7
      pick: 0.31
      fit: 0.33
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.56
      pick: 0.25
      fit: 1.0
    Arondight:
      total: 0.65
      efficiency: 0.5
      win: 0.9
      pick: 0.17
      fit: 0.38
    The Crusher:
      total: 0.77
      efficiency: 0.47
      win: 1.0
      pick: 0.11
      fit: 1.0
    Titan's Bane:
      total: 0.7
      efficiency: 0.47
      win: 0.83
      pick: 0.15
      fit: 1.0
    Avatar's Parashu:
      total: 0.71
      efficiency: 0.45
      win: 0.85
      pick: 0.55
      fit: 0.94
  community_ordered:
  - Ashwhorl Acorn
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Ashwhorl Acorn
  - Tyrfing
  - Arondight
  - Riptalon
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: The Crusher, Riptalon, Tyrfing, Silverbranch Bow, Tekko-Kagi, Lernaean
    Bow, Golden Blade, The Reaper, Toxic Blade, Dominance, Qin''s Blade, Sun Beam
    Bow, Transcendence, Berserker''s Shield, Dagger of Frenzy, Runeforged Hammer,
    Pendulum Blade, Avenging Blade, Barbed Carver, Vital Amplifier, Hastened Fatalis,
    Bloodforge.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.67
      efficiency: 0.76
      win: 0.7
      pick: 0.31
      fit: 0.48
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.65
      pick: 0.0
      fit: 0.79
    Arondight:
      total: 0.62
      efficiency: 0.5
      win: 0.9
      pick: 0.17
      fit: 0.21
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.65
      pick: 0.0
      fit: 0.79
    The Crusher:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.11
      fit: 0.43
    Avatar's Parashu:
      total: 0.62
      efficiency: 0.45
      win: 0.85
      pick: 0.55
      fit: 0.33
  community_ordered:
  - Ashwhorl Acorn
  - Arondight
  - The Crusher
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
  - Thistlethorn Acorn
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
    + fit + win/pick). Underrated for this god: The Crusher, Pendulum Blade, Breastplate
    of Valor, Genji''s Guard, The Reaper, Eye of Erebus, Transcendence, Screeching
    Gargoyle, Runeforged Hammer, Tyrfing, Chandra''s Grace, Freya''s Tears, Tekko-Kagi,
    Avenging Blade, Shield of the Phoenix, Silverbranch Bow, Daybreak Gavel, Lernaean
    Bow, Gladiator''s Shield, Shield Splitter, Dominance, Riptalon.'
  slot_scores:
    Thistlethorn Acorn:
      total: 0.59
      efficiency: 0.72
      win: 0.49
      pick: 0.52
      fit: 0.65
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.56
      pick: 0.25
      fit: 0.85
    Arondight:
      total: 0.69
      efficiency: 0.5
      win: 0.9
      pick: 0.17
      fit: 0.65
    The Crusher:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.11
      fit: 0.45
    Titan's Bane:
      total: 0.61
      efficiency: 0.47
      win: 0.83
      pick: 0.15
      fit: 0.45
    Avatar's Parashu:
      total: 0.62
      efficiency: 0.45
      win: 0.85
      pick: 0.55
      fit: 0.35
  community_ordered:
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Briskberry Acorn
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
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
    Underrated for this god: The Crusher, The Reaper, Pendulum Blade, Tekko-Kagi,
    Tyrfing, Transcendence, Runeforged Hammer, Avenging Blade, Golden Blade, Lernaean
    Bow, Shield Splitter, Dominance, Silverbranch Bow, Oath-Sworn Spear, Barbed Carver,
    Riptalon, Bloodforge, Toxic Blade, Deathbringer, Eye of the Storm, Damaru, Rage.'
  slot_scores:
    Briskberry Acorn:
      total: 0.58
      efficiency: 0.71
      win: 0.51
      pick: 0.52
      fit: 0.52
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.7
      win: 0.7
      pick: 0.31
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.59
      efficiency: 0.72
      win: 0.49
      pick: 0.52
      fit: 0.61
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.56
      pick: 0.25
      fit: 1.0
    The Crusher:
      total: 0.77
      efficiency: 0.47
      win: 1.0
      pick: 0.11
      fit: 1.0
    Titan's Bane:
      total: 0.7
      efficiency: 0.47
      win: 0.83
      pick: 0.15
      fit: 1.0
  community_ordered:
  - Briskberry Acorn
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
---
