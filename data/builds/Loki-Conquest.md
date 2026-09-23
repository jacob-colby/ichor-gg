---
type: smite-build
god: Loki
mode: Conquest
builds:
- source: community
  aspect: Aspect of Agony
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.52
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.35
    win_rate: 0.54
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.22
      win_rate: 0.41
    - name: Barbed Carver
      pick_rate: 0.13
      win_rate: 0.54
  - name: Hydra's Lament
    pick_rate: 0.38
    win_rate: 0.61
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.18
      win_rate: 0.39
    - name: Barbed Carver
      pick_rate: 0.13
      win_rate: 0.46
  - name: Barbed Carver
    pick_rate: 0.24
    win_rate: 0.65
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.42
    - name: The Crusher
      pick_rate: 0.12
      win_rate: 0.42
  - name: Heartseeker
    pick_rate: 0.44
    win_rate: 0.5
    alternates:
    - name: The Reaper
      pick_rate: 0.06
      win_rate: 0.83
    - name: Hide of the Nemean Lion
      pick_rate: 0.04
      win_rate: 1.0
  - name: Titan's Bane
    pick_rate: 0.12
    win_rate: 0.45
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.57
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.33
  - name: Avatar's Parashu
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Skeggox
      pick_rate: 0.08
      win_rate: 0.2
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.48
    win_rate: 0.58
  - name: Bumba's Cudgel
    pick_rate: 0.22
    win_rate: 0.41
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/loki/
  last_verified: '2026-09-23'
  god_win_rate: 0.51
  god_matches_won: 51
  god_matches_played: 100
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Heartseeker
  - The Reaper
  flex_slots:
  - Hide of the Nemean Lion
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
    this god: The Reaper, Tyrfing, Pendulum Blade, Tekko-Kagi, Arondight, Golden Blade,
    Transcendence, Runeforged Hammer, Silverbranch Bow, Avenging Blade, Riptalon,
    Toxic Blade, Lernaean Bow, Shield Splitter, Dominance, Oath-Sworn Spear, Bloodforge,
    Deathbringer, Eye of the Storm, Damaru, Rage, Musashi''s Dual Swords, Sanguine
    Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.54
      pick: 0.35
      fit: 1.0
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.61
      pick: 0.52
      fit: 0.71
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.07
      fit: 0.0
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.73
      fit: 1.0
    The Reaper:
      total: 0.69
      efficiency: 0.5
      win: 0.83
      pick: 0.1
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Heartseeker
  - The Reaper
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Heartseeker
  - The Reaper
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Reaper, Transcendence, Arondight, Pendulum Blade, Tyrfing, Runeforged Hammer,
    Tekko-Kagi, Avenging Blade, Dominance, Golden Blade, Breastplate of Valor, Lernaean
    Bow, Genji''s Guard, Shield Splitter, Silverbranch Bow, Oath-Sworn Spear, Riptalon,
    Daybreak Gavel, Toxic Blade, Bloodforge, Yogi''s Necklace, Deathbringer, Eye of
    the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.54
      pick: 0.35
      fit: 0.71
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.61
      pick: 0.52
      fit: 0.63
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.07
      fit: 0.0
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.73
      fit: 0.77
    The Reaper:
      total: 0.62
      efficiency: 0.5
      win: 0.83
      pick: 0.1
      fit: 0.47
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Heartseeker
  - The Reaper
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Heartseeker
  - The Reaper
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Reaper, Pendulum Blade, Arondight, Tyrfing, Tekko-Kagi, Transcendence,
    Silverbranch Bow, Runeforged Hammer, Riptalon, Avenging Blade, Toxic Blade, Breastplate
    of Valor, Golden Blade, Genji''s Guard, Lernaean Bow, Shield Splitter, Dominance,
    Daybreak Gavel, Oath-Sworn Spear, Eye of Erebus, Screeching Gargoyle, Bloodforge,
    Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.54
      pick: 0.35
      fit: 0.78
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.61
      pick: 0.52
      fit: 0.54
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.07
      fit: 0.0
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.73
      fit: 0.76
    The Reaper:
      total: 0.64
      efficiency: 0.5
      win: 0.83
      pick: 0.1
      fit: 0.56
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Heartseeker
  - The Reaper
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Hide of the Nemean Lion
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Hide of the Nemean Lion, The Reaper, Amanita Charm, Kinetic Cuirass,
    Shield of the Phoenix, Runeforged Hammer, Shield Splitter, Shifter''s Shield,
    Eye of the Storm, Freya''s Tears, Berserker''s Shield, Erosion, Eye of Providence,
    Genji''s Guard, Breastplate of Valor, Draconic Scale, Yogi''s Necklace, Phoenix
    Feather, Avenging Blade, Stone of Binding, Midgardian Mail, Golden Blade, Chandra''s
    Grace, Daybreak Gavel, Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.54
      pick: 0.35
      fit: 0.44
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.66
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.61
      pick: 0.52
      fit: 0.37
    Hide of the Nemean Lion:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.07
      fit: 0.39
    The Reaper:
      total: 0.66
      efficiency: 0.5
      win: 0.83
      pick: 0.1
      fit: 0.7
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Heartseeker
  - The Reaper
  flex_slots:
  - Hide of the Nemean Lion
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Pendulum Blade, Tekko-Kagi, Silverbranch Bow, Avenging
    Blade, Riptalon, Tyrfing, Toxic Blade, Oath-Sworn Spear, Transcendence, Arondight,
    Runeforged Hammer, Golden Blade, Lernaean Bow, Shield Splitter, Dominance, Screeching
    Gargoyle, Daybreak Gavel, Bloodforge, Breastplate of Valor, Genji''s Guard, Deathbringer,
    Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.54
      pick: 0.35
      fit: 1.0
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.33
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.61
      pick: 0.52
      fit: 0.48
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.07
      fit: 0.0
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.73
      fit: 1.0
    The Reaper:
      total: 0.69
      efficiency: 0.5
      win: 0.83
      pick: 0.1
      fit: 0.94
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Heartseeker
  - The Reaper
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hide of the Nemean Lion
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
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
    this god: The Reaper, Riptalon, Tyrfing, Silverbranch Bow, Tekko-Kagi, Lernaean
    Bow, Golden Blade, Toxic Blade, Dominance, Qin''s Blade, Sun Beam Bow, Transcendence,
    Berserker''s Shield, Dagger of Frenzy, Arondight, Runeforged Hammer, Pendulum
    Blade, Avenging Blade, Vital Amplifier, Hastened Fatalis, Bloodforge, The Executioner,
    Odysseus'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.35
      fit: 0.37
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.52
      pick: 0.0
      fit: 0.79
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.07
      fit: 0.0
    The Reaper:
      total: 0.64
      efficiency: 0.55
      win: 0.83
      pick: 0.1
      fit: 0.44
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - The Reaper
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  - The Reaper
  - Heartseeker
  - Pendulum Blade
  flex_slots:
  - Pendulum Blade
  - Heartseeker
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
    + fit + win/pick). Underrated for this god: The Reaper, Pendulum Blade, Arondight,
    Breastplate of Valor, Genji''s Guard, Tyrfing, Eye of Erebus, Transcendence, Screeching
    Gargoyle, Runeforged Hammer, Chandra''s Grace, Freya''s Tears, Silverbranch Bow,
    Tekko-Kagi, Avenging Blade, Shield of the Phoenix, Riptalon, Golden Blade, Toxic
    Blade, Daybreak Gavel, Lernaean Bow, Gladiator''s Shield, Shield Splitter, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.54
      pick: 0.35
      fit: 0.85
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.61
      pick: 0.52
      fit: 0.75
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.07
      fit: 0.0
    The Reaper:
      total: 0.6
      efficiency: 0.5
      win: 0.83
      pick: 0.1
      fit: 0.35
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.73
      fit: 0.55
    Pendulum Blade:
      total: 0.51
      efficiency: 0.42
      win: 0.52
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Tyrfing
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
    Golden Blade, Transcendence, Runeforged Hammer, Silverbranch Bow, Avenging Blade,
    Riptalon, Toxic Blade, Lernaean Bow, Shield Splitter, Dominance, Oath-Sworn Spear,
    Bloodforge, Deathbringer, Eye of the Storm, Damaru, Rage, Musashi''s Dual Swords,
    Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.54
      pick: 0.35
      fit: 1.0
    Tyrfing:
      total: 0.53
      efficiency: 0.44
      win: 0.52
      pick: 0.0
      fit: 0.97
    The Reaper:
      total: 0.69
      efficiency: 0.5
      win: 0.83
      pick: 0.1
      fit: 0.91
    The Crusher:
      total: 0.47
      efficiency: 0.47
      win: 0.33
      pick: 0.22
      fit: 1.0
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.73
      fit: 1.0
    Titan's Bane:
      total: 0.53
      efficiency: 0.47
      win: 0.45
      pick: 0.26
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
