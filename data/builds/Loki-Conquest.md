---
type: smite-build
god: Loki
mode: Conquest
builds:
- source: community
  aspect: Aspect of Agony
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.54
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.37
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.35
      win_rate: 0.56
    - name: Transcendence
      pick_rate: 0.07
      win_rate: 0.88
  - name: Barbed Carver
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.34
      win_rate: 0.58
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.57
  - name: The Crusher
    pick_rate: 0.17
    win_rate: 0.62
    alternates:
    - name: Barbed Carver
      pick_rate: 0.18
      win_rate: 0.5
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.59
  - name: Heartseeker
    pick_rate: 0.37
    win_rate: 0.58
    alternates:
    - name: The Crusher
      pick_rate: 0.12
      win_rate: 0.5
    - name: Barbed Carver
      pick_rate: 0.09
      win_rate: 0.6
  - name: Avatar's Parashu
    pick_rate: 0.11
    win_rate: 0.71
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.53
    - name: The Crusher
      pick_rate: 0.11
      win_rate: 0.5
  - name: Titan's Bane
    pick_rate: 0.1
    win_rate: 0.79
    alternates:
    - name: The Crusher
      pick_rate: 0.11
      win_rate: 0.81
    - name: Avatar's Parashu
      pick_rate: 0.1
      win_rate: 0.53
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.48
    win_rate: 0.6
  - name: Bumba's Cudgel
    pick_rate: 0.25
    win_rate: 0.35
  - name: Bluestone Brooch
    pick_rate: 0.12
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/loki/
  last_verified: '2026-11-06'
  god_win_rate: 0.5311203319502075
  god_matches_won: 128
  god_matches_played: 241
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
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - The Crusher
  - Heartseeker
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
    this god: Transcendence, The Reaper, Tyrfing, Pendulum Blade, Tekko-Kagi, Arondight,
    Runeforged Hammer, Golden Blade, Dominance, Shield Splitter, Eye of the Storm,
    Avenging Blade, Silverbranch Bow, Lernaean Bow, Toxic Blade, Bloodforge, Rage,
    Riptalon, Oath-Sworn Spear, Devourer''s Gauntlet, Deathbringer, Damaru, Genji''s
    Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.65
      win: 0.56
      pick: 0.35
      fit: 1.0
    Transcendence:
      total: 0.65
      efficiency: 0.5
      win: 0.88
      pick: 0.07
      fit: 0.52
    Heartseeker:
      total: 0.6
      efficiency: 0.45
      win: 0.58
      pick: 0.62
      fit: 1.0
    Titan's Bane:
      total: 0.69
      efficiency: 0.48
      win: 0.79
      pick: 0.31
      fit: 1.0
    The Crusher:
      total: 0.62
      efficiency: 0.51
      win: 0.62
      pick: 0.26
      fit: 1.0
    Avatar's Parashu:
      total: 0.63
      efficiency: 0.46
      win: 0.71
      pick: 0.24
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - The Crusher
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - The Crusher
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Transcendence,
    The Reaper, Tyrfing, Arondight, Pendulum Blade, Dominance, Tekko-Kagi, Runeforged
    Hammer, Genji''s Guard, Shield Splitter, Eye of the Storm, Avenging Blade, Damaru,
    Breastplate of Valor, Golden Blade, Chandra''s Grace, Lernaean Bow, Bloodforge,
    Rage, Silverbranch Bow, Yogi''s Necklace, Toxic Blade, Oath-Sworn Spear.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.56
      pick: 0.35
      fit: 0.71
    Transcendence:
      total: 0.63
      efficiency: 0.5
      win: 0.88
      pick: 0.07
      fit: 0.39
    Heartseeker:
      total: 0.57
      efficiency: 0.45
      win: 0.58
      pick: 0.62
      fit: 0.77
    Titan's Bane:
      total: 0.62
      efficiency: 0.48
      win: 0.79
      pick: 0.31
      fit: 0.57
    The Crusher:
      total: 0.56
      efficiency: 0.51
      win: 0.62
      pick: 0.26
      fit: 0.57
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.46
      win: 0.71
      pick: 0.24
      fit: 0.47
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - The Crusher
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - The Crusher
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
    god: Transcendence, The Reaper, Pendulum Blade, Arondight, Tyrfing, Tekko-Kagi,
    Damaru, Genji''s Guard, Runeforged Hammer, Silverbranch Bow, Dominance, Toxic
    Blade, Shield Splitter, Eye of the Storm, Avenging Blade, Breastplate of Valor,
    Chandra''s Grace, Golden Blade, Lernaean Bow, Riptalon, Bloodforge, Rage, Screeching
    Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.56
      pick: 0.35
      fit: 0.78
    Transcendence:
      total: 0.61
      efficiency: 0.5
      win: 0.88
      pick: 0.07
      fit: 0.22
    Heartseeker:
      total: 0.56
      efficiency: 0.45
      win: 0.58
      pick: 0.62
      fit: 0.76
    Titan's Bane:
      total: 0.64
      efficiency: 0.48
      win: 0.79
      pick: 0.31
      fit: 0.66
    The Crusher:
      total: 0.57
      efficiency: 0.51
      win: 0.62
      pick: 0.26
      fit: 0.66
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.46
      win: 0.71
      pick: 0.24
      fit: 0.56
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - The Crusher
  - Avatar's Parashu
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
  - Shield of the Phoenix
  - Jotunn's Revenge
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Shield Splitter, The Reaper, Phoenix Feather, Genji''s Guard, Runeforged
    Hammer, Yogi''s Necklace, Draconic Scale, Freya''s Tears, Oni Hunter''s Garb,
    Erosion, Eye of Providence, Shifter''s Shield, Breastplate of Valor, Chandra''s
    Grace, Midgardian Mail, Leviathan''s Hide, Wyrmskin Hide, Avenging Blade, Hide
    of the Nemean Lion, Tyrfing, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.35
      fit: 0.44
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.73
    Transcendence:
      total: 0.61
      efficiency: 0.5
      win: 0.88
      pick: 0.07
      fit: 0.23
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.79
      pick: 0.31
      fit: 0.5
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - The Crusher
  - Heartseeker
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
    for this god: Transcendence, The Reaper, Tekko-Kagi, Pendulum Blade, Tyrfing,
    Avenging Blade, Silverbranch Bow, Toxic Blade, Arondight, Riptalon, Oath-Sworn
    Spear, Runeforged Hammer, Dominance, Shield Splitter, Eye of the Storm, Golden
    Blade, Lernaean Bow, Bloodforge, Rage, Screeching Gargoyle, Damaru, Genji''s Guard,
    Devourer''s Gauntlet.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.65
      win: 0.56
      pick: 0.35
      fit: 1.0
    Transcendence:
      total: 0.62
      efficiency: 0.5
      win: 0.88
      pick: 0.07
      fit: 0.33
    Heartseeker:
      total: 0.6
      efficiency: 0.45
      win: 0.58
      pick: 0.62
      fit: 1.0
    Titan's Bane:
      total: 0.69
      efficiency: 0.48
      win: 0.79
      pick: 0.31
      fit: 1.0
    The Crusher:
      total: 0.62
      efficiency: 0.51
      win: 0.62
      pick: 0.26
      fit: 1.0
    Avatar's Parashu:
      total: 0.63
      efficiency: 0.46
      win: 0.71
      pick: 0.24
      fit: 0.94
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - The Crusher
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Riptalon
  - Silverbranch Bow
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
    this god: Transcendence, Tyrfing, Riptalon, Silverbranch Bow, Tekko-Kagi, The
    Reaper, Golden Blade, Toxic Blade, Lernaean Bow, Dominance, Qin''s Blade, Dagger
    of Frenzy, Arondight, Berserker''s Shield, Sun Beam Bow, Bloodforge, Runeforged
    Hammer, Odysseus'' Bow, Pendulum Blade, Shield Splitter, Eye of the Storm, Avenging
    Blade, Damaru.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.35
      fit: 0.37
    Transcendence:
      total: 0.6
      efficiency: 0.5
      win: 0.88
      pick: 0.07
      fit: 0.17
    Tyrfing:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.55
      efficiency: 0.45
      win: 0.6
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.69
    Titan's Bane:
      total: 0.6
      efficiency: 0.48
      win: 0.79
      pick: 0.31
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Transcendence
  - Arondight
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Hydra's Lament
  - Avatar's Parashu
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
    + fit + win/pick). Underrated for this god: Transcendence, Arondight, Pendulum
    Blade, Damaru, Genji''s Guard, Breastplate of Valor, The Reaper, Tyrfing, Chandra''s
    Grace, Screeching Gargoyle, Freya''s Tears, Eye of Erebus, Shield of the Phoenix,
    Tekko-Kagi, Runeforged Hammer, Dominance, Silverbranch Bow, Gladiator''s Shield,
    Shield Splitter, Eye of the Storm, Avenging Blade, Toxic Blade, Golden Blade,
    Regrowth Striders.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.65
      win: 0.56
      pick: 0.35
      fit: 0.85
    Hydra's Lament:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.37
      fit: 0.75
    Transcendence:
      total: 0.6
      efficiency: 0.5
      win: 0.88
      pick: 0.07
      fit: 0.15
    Arondight:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.65
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.79
      pick: 0.31
      fit: 0.45
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.46
      win: 0.71
      pick: 0.24
      fit: 0.35
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Transcendence
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Heartseeker
  - The Crusher
  - Titan's Bane
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
    Underrated for this god: The Reaper, Tyrfing, Pendulum Blade, Tekko-Kagi, Arondight,
    Transcendence, Runeforged Hammer, Golden Blade, Dominance, Shield Splitter, Eye
    of the Storm, Avenging Blade, Silverbranch Bow, Lernaean Bow, Toxic Blade, Bloodforge,
    Rage, Riptalon, Oath-Sworn Spear, Devourer''s Gauntlet, Deathbringer, Damaru,
    Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.65
      win: 0.56
      pick: 0.35
      fit: 1.0
    Transcendence:
      total: 0.65
      efficiency: 0.5
      win: 0.88
      pick: 0.07
      fit: 0.52
    The Reaper:
      total: 0.59
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.91
    Heartseeker:
      total: 0.6
      efficiency: 0.45
      win: 0.58
      pick: 0.62
      fit: 1.0
    The Crusher:
      total: 0.62
      efficiency: 0.51
      win: 0.62
      pick: 0.26
      fit: 1.0
    Titan's Bane:
      total: 0.69
      efficiency: 0.48
      win: 0.79
      pick: 0.31
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - The Crusher
  - Titan's Bane
  starter: *id001
---
