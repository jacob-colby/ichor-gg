---
type: smite-build
god: Hun Batz
mode: Conquest
builds:
- source: community
  aspect: Aspect of Disruption
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.5
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.51
    win_rate: 0.45
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.38
      win_rate: 0.5
    - name: Axe
      pick_rate: 0.03
      win_rate: 0.5
  - name: Hydra's Lament
    pick_rate: 0.37
    win_rate: 0.52
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.27
      win_rate: 0.48
    - name: Transcendence
      pick_rate: 0.1
      win_rate: 0.13
  - name: The Crusher
    pick_rate: 0.22
    win_rate: 0.35
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.56
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.51
    win_rate: 0.43
    alternates:
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.29
    - name: Pendulum Blade
      pick_rate: 0.08
      win_rate: 0.67
  - name: Avatar's Parashu
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: The Crusher
      pick_rate: 0.15
      win_rate: 0.7
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.44
  - name: Skeggox
    pick_rate: 0.25
    win_rate: 0.36
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.09
      win_rate: 0.5
    - name: Axe
      pick_rate: 0.09
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.59
    win_rate: 0.54
  - name: Bumba's Cudgel
    pick_rate: 0.26
    win_rate: 0.25
  - name: Bumba's Spear
    pick_rate: 0.04
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/hun-batz/
  last_verified: '2026-11-06'
  god_win_rate: 0.46153846153846156
  god_matches_won: 36
  god_matches_played: 78
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
  - Hydra's Lament
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - The Reaper
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
    this god: Pendulum Blade, The Reaper, Titan''s Bane, Tyrfing, Tekko-Kagi, Arondight,
    Runeforged Hammer, Dominance, Golden Blade, Shield Splitter, Eye of the Storm,
    Avenging Blade, Lernaean Bow, Silverbranch Bow, Bloodforge, Rage, Barbed Carver,
    Toxic Blade, Oath-Sworn Spear, Devourer''s Gauntlet, Riptalon, Deathbringer, Damaru,
    Genji''s Guard, Transcendence.'
  slot_scores:
    Hydra's Lament:
      total: 0.56
      efficiency: 0.55
      win: 0.52
      pick: 0.5
      fit: 0.71
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.45
      pick: 0.51
      fit: 1.0
    The Reaper:
      total: 0.53
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.91
    Pendulum Blade:
      total: 0.6
      efficiency: 0.39
      win: 0.67
      pick: 0.13
      fit: 1.0
    Heartseeker:
      total: 0.54
      efficiency: 0.45
      win: 0.43
      pick: 0.85
      fit: 1.0
    Avatar's Parashu:
      total: 0.53
      efficiency: 0.46
      win: 0.5
      pick: 0.19
      fit: 0.91
  community_ordered:
  - Hydra's Lament
  - Jotunn's Revenge
  - Pendulum Blade
  - Heartseeker
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Transcendence
  - Pendulum Blade
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Titan's Bane
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Pendulum
    Blade, Titan''s Bane, The Reaper, Arondight, Tyrfing, Dominance, Tekko-Kagi, Runeforged
    Hammer, Genji''s Guard, Shield Splitter, Eye of the Storm, Avenging Blade, Damaru,
    Breastplate of Valor, Chandra''s Grace, Lernaean Bow, Golden Blade, Bloodforge,
    Rage, Barbed Carver, Yogi''s Necklace, Silverbranch Bow, Oath-Sworn Spear, Devourer''s
    Gauntlet, Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.45
      pick: 0.51
      fit: 0.71
    Hydra's Lament:
      total: 0.55
      efficiency: 0.55
      win: 0.52
      pick: 0.5
      fit: 0.63
    Transcendence:
      total: 0.3
      efficiency: 0.5
      win: 0.13
      pick: 0.14
      fit: 0.39
    Pendulum Blade:
      total: 0.54
      efficiency: 0.39
      win: 0.67
      pick: 0.13
      fit: 0.61
    Heartseeker:
      total: 0.51
      efficiency: 0.45
      win: 0.43
      pick: 0.85
      fit: 0.77
    Titan's Bane:
      total: 0.47
      efficiency: 0.48
      win: 0.47
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Transcendence
  - Pendulum Blade
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Hydra's Lament
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - The Reaper
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Pendulum Blade, Titan''s Bane, The Reaper, Arondight, Tyrfing, Tekko-Kagi,
    Damaru, Genji''s Guard, Runeforged Hammer, Silverbranch Bow, Dominance, Shield
    Splitter, Eye of the Storm, Avenging Blade, Toxic Blade, Breastplate of Valor,
    Chandra''s Grace, Lernaean Bow, Golden Blade, Riptalon, Bloodforge, Rage, Barbed
    Carver, Screeching Gargoyle, Transcendence.'
  slot_scores:
    Hydra's Lament:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.5
      fit: 0.54
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.45
      pick: 0.51
      fit: 0.78
    The Reaper:
      total: 0.48
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.56
    Pendulum Blade:
      total: 0.56
      efficiency: 0.39
      win: 0.67
      pick: 0.13
      fit: 0.78
    Heartseeker:
      total: 0.51
      efficiency: 0.45
      win: 0.43
      pick: 0.85
      fit: 0.76
    Titan's Bane:
      total: 0.48
      efficiency: 0.48
      win: 0.47
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Hydra's Lament
  - Jotunn's Revenge
  - Pendulum Blade
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Pendulum Blade
  - Amanita Charm
  flex_slots:
  - Pendulum Blade
  - Hydra's Lament
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
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Shield Splitter, The Reaper, Phoenix Feather, Genji''s Guard, Runeforged
    Hammer, Yogi''s Necklace, Draconic Scale, Freya''s Tears, Oni Hunter''s Garb,
    Erosion, Eye of Providence, Shifter''s Shield, Breastplate of Valor, Chandra''s
    Grace, Midgardian Mail, Leviathan''s Hide, Wyrmskin Hide, Avenging Blade, Hide
    of the Nemean Lion, Titan''s Bane, Ancile, Stone of Binding.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.45
      pick: 0.51
      fit: 0.44
    Hydra's Lament:
      total: 0.51
      efficiency: 0.55
      win: 0.52
      pick: 0.5
      fit: 0.37
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.73
    Pendulum Blade:
      total: 0.51
      efficiency: 0.39
      win: 0.67
      pick: 0.13
      fit: 0.44
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Pendulum Blade
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Hydra's Lament
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - The Reaper
  - Hydra's Lament
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
    for this god: Pendulum Blade, The Reaper, Titan''s Bane, Tekko-Kagi, Tyrfing,
    Avenging Blade, Silverbranch Bow, Arondight, Toxic Blade, Riptalon, Oath-Sworn
    Spear, Runeforged Hammer, Dominance, Shield Splitter, Eye of the Storm, Golden
    Blade, Lernaean Bow, Bloodforge, Rage, Barbed Carver, Screeching Gargoyle, Damaru,
    Genji''s Guard, Devourer''s Gauntlet, Transcendence.'
  slot_scores:
    Hydra's Lament:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.5
      fit: 0.48
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.45
      pick: 0.51
      fit: 1.0
    The Reaper:
      total: 0.54
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.94
    Pendulum Blade:
      total: 0.6
      efficiency: 0.39
      win: 0.67
      pick: 0.13
      fit: 1.0
    Heartseeker:
      total: 0.54
      efficiency: 0.45
      win: 0.43
      pick: 0.85
      fit: 1.0
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.46
      win: 0.5
      pick: 0.19
      fit: 0.94
  community_ordered:
  - Hydra's Lament
  - Jotunn's Revenge
  - Pendulum Blade
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Pendulum Blade
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
    this god: Tyrfing, Pendulum Blade, Riptalon, Silverbranch Bow, Tekko-Kagi, The
    Reaper, Golden Blade, Toxic Blade, Lernaean Bow, Dominance, Qin''s Blade, Titan''s
    Bane, Dagger of Frenzy, Arondight, Berserker''s Shield, Sun Beam Bow, Bloodforge,
    Barbed Carver, Runeforged Hammer, Odysseus'' Bow, Shield Splitter, Eye of the
    Storm, Avenging Blade, Damaru, Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.45
      pick: 0.51
      fit: 0.37
    Hydra's Lament:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.5
      fit: 0.31
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.49
      efficiency: 0.45
      win: 0.47
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.49
      win: 0.47
      pick: 0.0
      fit: 0.69
    Pendulum Blade:
      total: 0.5
      efficiency: 0.39
      win: 0.67
      pick: 0.13
      fit: 0.37
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Pendulum Blade
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Hydra's Lament
  - Jotunn's Revenge
  - Damaru
  - Arondight
  - Heartseeker
  - Pendulum Blade
  flex_slots:
  - Heartseeker
  - Damaru
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
    + fit + win/pick). Underrated for this god: Pendulum Blade, Arondight, Damaru,
    Genji''s Guard, Titan''s Bane, Breastplate of Valor, The Reaper, Chandra''s Grace,
    Tyrfing, Screeching Gargoyle, Freya''s Tears, Eye of Erebus, Shield of the Phoenix,
    Tekko-Kagi, Runeforged Hammer, Dominance, Gladiator''s Shield, Shield Splitter,
    Eye of the Storm, Avenging Blade, Silverbranch Bow, Regrowth Striders, Toxic Blade,
    Prophetic Cloak, Transcendence.'
  slot_scores:
    Hydra's Lament:
      total: 0.56
      efficiency: 0.55
      win: 0.52
      pick: 0.5
      fit: 0.75
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.45
      pick: 0.51
      fit: 0.85
    Damaru:
      total: 0.47
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.5
    Arondight:
      total: 0.5
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.65
    Heartseeker:
      total: 0.48
      efficiency: 0.45
      win: 0.43
      pick: 0.85
      fit: 0.55
    Pendulum Blade:
      total: 0.57
      efficiency: 0.39
      win: 0.67
      pick: 0.13
      fit: 0.85
  community_ordered:
  - Hydra's Lament
  - Jotunn's Revenge
  - Heartseeker
  - Pendulum Blade
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Heartseeker
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
    Underrated for this god: The Reaper, Titan''s Bane, Tyrfing, Pendulum Blade, Tekko-Kagi,
    Arondight, Transcendence, Runeforged Hammer, Dominance, Golden Blade, Shield Splitter,
    Eye of the Storm, Avenging Blade, Lernaean Bow, Silverbranch Bow, Bloodforge,
    Rage, Barbed Carver, Toxic Blade, Oath-Sworn Spear, Devourer''s Gauntlet, Riptalon,
    Deathbringer, Damaru, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.45
      pick: 0.51
      fit: 1.0
    Transcendence:
      total: 0.32
      efficiency: 0.5
      win: 0.13
      pick: 0.14
      fit: 0.52
    The Reaper:
      total: 0.53
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.5
      efficiency: 0.51
      win: 0.35
      pick: 0.34
      fit: 1.0
    Heartseeker:
      total: 0.54
      efficiency: 0.45
      win: 0.43
      pick: 0.85
      fit: 1.0
    Titan's Bane:
      total: 0.53
      efficiency: 0.48
      win: 0.47
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Heartseeker
  starter: *id001
---
