---
type: smite-build
god: Da Ji
mode: Conquest
builds:
- source: community
  aspect: Aspect of Ferocity
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.33
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.47
    win_rate: 0.6
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.34
      win_rate: 0.45
    - name: Barbed Carver
      pick_rate: 0.06
      win_rate: 0.5
  - name: Hydra's Lament
    pick_rate: 0.31
    win_rate: 0.7
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.25
      win_rate: 0.5
    - name: The Reaper
      pick_rate: 0.19
      win_rate: 0.33
  - name: Barbed Carver
    pick_rate: 0.35
    win_rate: 0.55
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.16
      win_rate: 0.6
    - name: The Reaper
      pick_rate: 0.13
      win_rate: 0.25
  - name: Heartseeker
    pick_rate: 0.45
    win_rate: 0.64
    alternates:
    - name: The Crusher
      pick_rate: 0.16
      win_rate: 0.2
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.67
  - name: Titan's Bane
    pick_rate: 0.15
    win_rate: 0.75
    alternates:
    - name: Heartseeker
      pick_rate: 0.19
      win_rate: 0.4
    - name: Avatar's Parashu
      pick_rate: 0.15
      win_rate: 0.5
  - name: Skeggox
    pick_rate: 0.29
    win_rate: 0.67
    alternates:
    - name: Magi's Cloak
      pick_rate: 0.14
      win_rate: 0.67
    - name: Lucerne Hammer
      pick_rate: 0.1
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.5
    win_rate: 0.69
  - name: Bumba's Cudgel
    pick_rate: 0.19
    win_rate: 0.17
  - name: Leather Cowl
    pick_rate: 0.13
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/da-ji/
  last_verified: '2026-09-09'
  god_win_rate: 0.53125
  god_matches_won: 17
  god_matches_played: 32
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Transcendence
  - Pendulum Blade
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Pendulum Blade
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Pendulum Blade, Arondight, Tekko-Kagi, Tyrfing, Transcendence, Runeforged
    Hammer, Avenging Blade, Golden Blade, Lernaean Bow, Shield Splitter, Dominance,
    Silverbranch Bow, Oath-Sworn Spear, Riptalon, Toxic Blade, Breastplate of Valor,
    Bloodforge, Genji''s Guard, Deathbringer, Eye of the Storm, Damaru, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.6
      pick: 0.47
      fit: 1.0
    Hydra's Lament:
      total: 0.64
      efficiency: 0.54
      win: 0.7
      pick: 0.42
      fit: 0.77
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.44
    Pendulum Blade:
      total: 0.57
      efficiency: 0.42
      win: 0.6
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.64
      efficiency: 0.47
      win: 0.64
      pick: 0.75
      fit: 0.98
    Titan's Bane:
      total: 0.65
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Transcendence
  - Arondight
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Transcendence,
    Arondight, Pendulum Blade, Tyrfing, Runeforged Hammer, Tekko-Kagi, Avenging Blade,
    Dominance, Breastplate of Valor, Lernaean Bow, Genji''s Guard, Shield Splitter,
    Golden Blade, Oath-Sworn Spear, Silverbranch Bow, Daybreak Gavel, Riptalon, Bloodforge,
    Yogi''s Necklace, Toxic Blade, Deathbringer, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.6
      pick: 0.47
      fit: 0.71
    Hydra's Lament:
      total: 0.62
      efficiency: 0.54
      win: 0.7
      pick: 0.42
      fit: 0.63
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.39
    Arondight:
      total: 0.51
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.43
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.64
      pick: 0.75
      fit: 0.77
    Titan's Bane:
      total: 0.6
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Transcendence
  - Pendulum Blade
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Pendulum Blade
  - Transcendence
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Pendulum Blade, Arondight, Tekko-Kagi, Transcendence, Tyrfing, Runeforged
    Hammer, Silverbranch Bow, Avenging Blade, Breastplate of Valor, Riptalon, Genji''s
    Guard, Lernaean Bow, Toxic Blade, Shield Splitter, Dominance, Golden Blade, Daybreak
    Gavel, Oath-Sworn Spear, Eye of Erebus, Screeching Gargoyle, Bloodforge, Chandra''s
    Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.6
      pick: 0.47
      fit: 0.78
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.7
      pick: 0.42
      fit: 0.54
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.22
    Pendulum Blade:
      total: 0.53
      efficiency: 0.42
      win: 0.6
      pick: 0.0
      fit: 0.78
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.64
      pick: 0.75
      fit: 0.76
    Titan's Bane:
      total: 0.62
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.66
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Freya''s Tears,
    Runeforged Hammer, Shield Splitter, Shifter''s Shield, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye
    of Providence, Draconic Scale, Phoenix Feather, Chandra''s Grace, Avenging Blade,
    Glorious Pridwen, Stone of Binding, Midgardian Mail, Daybreak Gavel, Hide of the
    Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.6
      pick: 0.47
      fit: 0.48
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.7
      pick: 0.42
      fit: 0.42
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.21
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.64
      pick: 0.75
      fit: 0.57
    Titan's Bane:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.47
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Transcendence
  - Pendulum Blade
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Pendulum Blade
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Pendulum Blade, Tekko-Kagi, Avenging Blade, Arondight, Silverbranch
    Bow, Riptalon, Tyrfing, Oath-Sworn Spear, Transcendence, Runeforged Hammer, Toxic
    Blade, Lernaean Bow, Screeching Gargoyle, Golden Blade, Shield Splitter, Dominance,
    Breastplate of Valor, Genji''s Guard, Daybreak Gavel, Bloodforge, Deathbringer,
    Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.6
      pick: 0.47
      fit: 1.0
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.7
      pick: 0.42
      fit: 0.54
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.3
    Pendulum Blade:
      total: 0.57
      efficiency: 0.42
      win: 0.6
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.64
      efficiency: 0.47
      win: 0.64
      pick: 0.75
      fit: 1.0
    Titan's Bane:
      total: 0.66
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.95
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
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
    this god: Riptalon, Tyrfing, Silverbranch Bow, Lernaean Bow, Tekko-Kagi, Golden
    Blade, Toxic Blade, Dominance, Qin''s Blade, Sun Beam Bow, Arondight, Pendulum
    Blade, Transcendence, Berserker''s Shield, Runeforged Hammer, Dagger of Frenzy,
    Avenging Blade, Vital Amplifier, Hastened Fatalis, Bloodforge, The Executioner,
    Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.47
      fit: 0.42
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.7
      pick: 0.42
      fit: 0.36
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.74
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.74
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.64
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.41
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Pendulum Blade
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Pendulum Blade
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
    + fit + win/pick). Underrated for this god: Pendulum Blade, Arondight, Breastplate
    of Valor, Genji''s Guard, Eye of Erebus, Transcendence, Tyrfing, Screeching Gargoyle,
    Runeforged Hammer, Chandra''s Grace, Freya''s Tears, Tekko-Kagi, Avenging Blade,
    Shield of the Phoenix, Silverbranch Bow, Daybreak Gavel, Lernaean Bow, Riptalon,
    Gladiator''s Shield, Shield Splitter, Dominance, Golden Blade, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.6
      pick: 0.47
      fit: 0.85
    Hydra's Lament:
      total: 0.64
      efficiency: 0.54
      win: 0.7
      pick: 0.42
      fit: 0.75
    Arondight:
      total: 0.54
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.65
    Pendulum Blade:
      total: 0.55
      efficiency: 0.42
      win: 0.6
      pick: 0.0
      fit: 0.85
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.64
      pick: 0.75
      fit: 0.55
    Titan's Bane:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: model
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Pendulum Blade, Arondight, Tekko-Kagi, Tyrfing, Transcendence,
    Runeforged Hammer, Avenging Blade, Golden Blade, Lernaean Bow, Shield Splitter,
    Dominance, Silverbranch Bow, Oath-Sworn Spear, Riptalon, Toxic Blade, Breastplate
    of Valor, Bloodforge, Genji''s Guard, Deathbringer, Eye of the Storm, Damaru,
    Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.6
      pick: 0.47
      fit: 1.0
    Hydra's Lament:
      total: 0.64
      efficiency: 0.54
      win: 0.7
      pick: 0.42
      fit: 0.77
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.44
    Pendulum Blade:
      total: 0.57
      efficiency: 0.42
      win: 0.6
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.64
      efficiency: 0.47
      win: 0.64
      pick: 0.75
      fit: 0.98
    Titan's Bane:
      total: 0.65
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
