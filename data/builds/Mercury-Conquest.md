---
type: smite-build
god: Mercury
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Rage
    pick_rate: 0.68
    win_rate: 0.5
    alternates:
    - name: Golden Blade
      pick_rate: 0.07
      win_rate: 0.5
    - name: Hydra's Lament
      pick_rate: 0.05
      win_rate: 0.25
  - name: Dagger of Frenzy
    pick_rate: 0.48
    win_rate: 0.49
    alternates:
    - name: Rage
      pick_rate: 0.13
      win_rate: 0.64
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.44
  - name: Deathbringer
    pick_rate: 0.59
    win_rate: 0.53
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.2
      win_rate: 0.44
    - name: Musashi's Dual Swords
      pick_rate: 0.03
      win_rate: 0.5
  - name: Riptalon
    pick_rate: 0.14
    win_rate: 0.45
    alternates:
    - name: Deathbringer
      pick_rate: 0.14
      win_rate: 0.55
    - name: Musashi's Dual Swords
      pick_rate: 0.11
      win_rate: 0.56
  - name: Hydra's Lament
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.44
    - name: Musashi's Dual Swords
      pick_rate: 0.07
      win_rate: 0.8
  - name: Hunter's Bow
    pick_rate: 0.08
    win_rate: 0.75
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.75
    - name: Dominance
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.38
    win_rate: 0.58
  - name: Leather Cowl
    pick_rate: 0.27
    win_rate: 0.41
  - name: Sharpshooter's Arrow
    pick_rate: 0.2
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/mercury/
  last_verified: '2026-11-06'
  god_win_rate: 0.5
  god_matches_won: 41
  god_matches_played: 82
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
  - Tyrfing
  - Hydra's Lament
  - Dominance
  - Titan's Bane
  flex_slots:
  - Tyrfing
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
    this god: Jotunn''s Revenge, Tyrfing, The Crusher, Heartseeker, Tekko-Kagi, The
    Reaper, Arondight, Pendulum Blade, Avatar''s Parashu, Silverbranch Bow, Lernaean
    Bow, Golden Blade, Toxic Blade, Transcendence, Runeforged Hammer, Shield Splitter,
    Eye of the Storm, Avenging Blade, Demon Blade, Qin''s Blade, Damaru, Genji''s
    Guard, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.84
    Transcendence:
      total: 0.48
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.73
    Hydra's Lament:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.66
    Dominance:
      total: 0.71
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.56
    Titan's Bane:
      total: 0.63
      efficiency: 0.48
      win: 0.75
      pick: 0.25
      fit: 0.77
  community_ordered:
  - Hydra's Lament
  - Dominance
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Dominance
  - Titan's Bane
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Heartseeker, Tyrfing, The Crusher, The Reaper, Arondight, Tekko-Kagi,
    Transcendence, Lernaean Bow, Avatar''s Parashu, Pendulum Blade, Silverbranch Bow,
    Runeforged Hammer, Genji''s Guard, Shield Splitter, Eye of the Storm, Golden Blade,
    Avenging Blade, Toxic Blade, Damaru, Breastplate of Valor, Chandra''s Grace, Qin''s
    Blade, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.66
    Transcendence:
      total: 0.47
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.36
    Hydra's Lament:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.59
    Dominance:
      total: 0.7
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.5
    Titan's Bane:
      total: 0.6
      efficiency: 0.48
      win: 0.75
      pick: 0.25
      fit: 0.53
    Heartseeker:
      total: 0.51
      efficiency: 0.45
      win: 0.55
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Hydra's Lament
  - Dominance
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Dominance
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Crusher
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Crusher, Heartseeker, The Reaper, Tyrfing, Tekko-Kagi,
    Arondight, Pendulum Blade, Silverbranch Bow, Avatar''s Parashu, Toxic Blade, Lernaean
    Bow, Damaru, Genji''s Guard, Transcendence, Runeforged Hammer, Golden Blade, Shield
    Splitter, Eye of the Storm, Avenging Blade, Qin''s Blade, Breastplate of Valor,
    Chandra''s Grace, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.71
    Transcendence:
      total: 0.45
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.2
    Hydra's Lament:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.51
    Dominance:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.35
    The Crusher:
      total: 0.51
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.61
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.75
      pick: 0.25
      fit: 0.61
  community_ordered:
  - Hydra's Lament
  - Dominance
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Shield of the Phoenix
  - Hydra's Lament
  - Dominance
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Jotunn''s Revenge, Genji''s Guard, The Reaper, Shield Splitter, Phoenix Feather,
    Freya''s Tears, Yogi''s Necklace, Runeforged Hammer, Draconic Scale, Breastplate
    of Valor, Oni Hunter''s Garb, Chandra''s Grace, Erosion, Tyrfing, Eye of Providence,
    Shifter''s Shield, The Crusher, Midgardian Mail, Regrowth Striders, Heartseeker,
    Leviathan''s Hide, Hide of the Nemean Lion, Glorious Pridwen, Golden Blade, Avenging
    Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.38
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.73
    Hydra's Lament:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.39
    Dominance:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.34
    Titan's Bane:
      total: 0.58
      efficiency: 0.48
      win: 0.75
      pick: 0.25
      fit: 0.44
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Hydra's Lament
  - Dominance
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Dominance
  - The Crusher
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - The Crusher
  - Heartseeker
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
    for this god: Jotunn''s Revenge, The Crusher, Heartseeker, The Reaper, Tekko-Kagi,
    Avatar''s Parashu, Silverbranch Bow, Pendulum Blade, Tyrfing, Toxic Blade, Avenging
    Blade, Arondight, Lernaean Bow, Oath-Sworn Spear, Transcendence, Runeforged Hammer,
    Golden Blade, Shield Splitter, Eye of the Storm, Screeching Gargoyle, Damaru,
    Genji''s Guard, Qin''s Blade, Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.89
    Hydra's Lament:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.49
    Dominance:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.42
    The Crusher:
      total: 0.55
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.87
    Titan's Bane:
      total: 0.65
      efficiency: 0.48
      win: 0.75
      pick: 0.25
      fit: 0.87
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.55
      pick: 0.0
      fit: 0.97
  community_ordered:
  - Hydra's Lament
  - Dominance
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Dominance
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Jotunn's Revenge
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
    this god: Tyrfing, Jotunn''s Revenge, Silverbranch Bow, Tekko-Kagi, The Reaper,
    Lernaean Bow, Toxic Blade, Qin''s Blade, The Crusher, Golden Blade, Heartseeker,
    Arondight, Avatar''s Parashu, Berserker''s Shield, Sun Beam Bow, Demon Blade,
    Bloodforge, Pendulum Blade, Transcendence, Runeforged Hammer, Barbed Carver, Damaru,
    Genji''s Guard, Odysseus'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.4
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.72
    Hydra's Lament:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.35
    Dominance:
      total: 0.71
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.53
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.62
    Titan's Bane:
      total: 0.58
      efficiency: 0.48
      win: 0.75
      pick: 0.25
      fit: 0.4
  community_ordered:
  - Hydra's Lament
  - Dominance
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Dominance
  - Pendulum Blade
  - Titan's Bane
  flex_slots:
  - Arondight
  - Pendulum Blade
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Arondight, Pendulum
    Blade, Tyrfing, Damaru, Genji''s Guard, The Crusher, Heartseeker, The Reaper,
    Breastplate of Valor, Tekko-Kagi, Chandra''s Grace, Silverbranch Bow, Lernaean
    Bow, Avatar''s Parashu, Toxic Blade, Screeching Gargoyle, Freya''s Tears, Eye
    of Erebus, Shield of the Phoenix, Transcendence, Runeforged Hammer, Qin''s Blade,
    Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.77
    Hydra's Lament:
      total: 0.76
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.69
    Arondight:
      total: 0.52
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.59
    Dominance:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.29
    Pendulum Blade:
      total: 0.5
      efficiency: 0.39
      win: 0.55
      pick: 0.0
      fit: 0.77
    Titan's Bane:
      total: 0.58
      efficiency: 0.48
      win: 0.75
      pick: 0.25
      fit: 0.42
  community_ordered:
  - Hydra's Lament
  - Dominance
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Hydra's Lament
  - The Crusher
  - Heartseeker
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
    Underrated for this god: Jotunn''s Revenge, Tyrfing, The Crusher, Heartseeker,
    Tekko-Kagi, The Reaper, Arondight, Pendulum Blade, Avatar''s Parashu, Golden Blade,
    Silverbranch Bow, Lernaean Bow, Toxic Blade, Transcendence, Runeforged Hammer,
    Shield Splitter, Eye of the Storm, Avenging Blade, Demon Blade, Qin''s Blade,
    Damaru, Genji''s Guard, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.84
    Transcendence:
      total: 0.48
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.73
    Hydra's Lament:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.19
      fit: 0.66
    The Crusher:
      total: 0.54
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.77
    Heartseeker:
      total: 0.53
      efficiency: 0.45
      win: 0.55
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Hydra's Lament
  starter: *id001
---
