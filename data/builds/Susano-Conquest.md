---
type: smite-build
god: Susano
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Storm Front
  aspect_pick_rate: 0.31
  aspect_win_rate: 0.5
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.27
    win_rate: 0.5
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.21
      win_rate: 0.51
    - name: Barbed Carver
      pick_rate: 0.2
      win_rate: 0.52
  - name: Barbed Carver
    pick_rate: 0.18
    win_rate: 0.47
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.28
      win_rate: 0.52
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.54
  - name: Jotunn's Revenge
    pick_rate: 0.11
    win_rate: 0.48
    alternates:
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.52
    - name: Barbed Carver
      pick_rate: 0.09
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.31
    win_rate: 0.51
    alternates:
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.53
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.47
  - name: Blinking Abyss
    pick_rate: 0.1
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.61
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.48
  - name: Skeggox
    pick_rate: 0.09
    win_rate: 0.47
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.11
      win_rate: 0.56
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.62
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.43
    win_rate: 0.55
  - name: Bumba's Cudgel
    pick_rate: 0.22
    win_rate: 0.38
  - name: Bluestone Pendant
    pick_rate: 0.14
    win_rate: 0.41
  source_url: https://smitebrain.com/gods/susano/
  last_verified: '2026-11-02'
  god_win_rate: 0.5033301617507137
  god_matches_won: 529
  god_matches_played: 1051
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
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
    this god: The Reaper, Tekko-Kagi, Pendulum Blade, Avatar''s Parashu, Tyrfing,
    Arondight, Transcendence, Golden Blade, Avenging Blade, Eye of the Storm, Shield
    Splitter, Dominance, Silverbranch Bow, Lernaean Bow, Bloodforge, Toxic Blade,
    Oath-Sworn Spear, Riptalon, Rage, Musashi''s Dual Swords, Deathbringer, Sanguine
    Lash, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.48
      pick: 0.17
      fit: 1.0
    Transcendence:
      total: 0.48
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.52
    The Reaper:
      total: 0.53
      efficiency: 0.47
      win: 0.51
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.55
      efficiency: 0.45
      win: 0.52
      pick: 0.16
      fit: 1.0
    Heartseeker:
      total: 0.55
      efficiency: 0.41
      win: 0.51
      pick: 0.52
      fit: 1.0
    Titan's Bane:
      total: 0.62
      efficiency: 0.51
      win: 0.62
      pick: 0.22
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
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
  - The Crusher
  - Heartseeker
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Reaper, Arondight, Transcendence, Pendulum Blade, Tekko-Kagi, Tyrfing, Avatar''s
    Parashu, Dominance, Genji''s Guard, Avenging Blade, Eye of the Storm, Shield Splitter,
    Breastplate of Valor, Lernaean Bow, Chandra''s Grace, Bloodforge, Golden Blade,
    Damaru, Silverbranch Bow, Oath-Sworn Spear, Yogi''s Necklace, Toxic Blade, Rage.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.48
      pick: 0.17
      fit: 0.71
    Transcendence:
      total: 0.46
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.27
      fit: 0.63
    The Crusher:
      total: 0.49
      efficiency: 0.45
      win: 0.52
      pick: 0.16
      fit: 0.57
    Heartseeker:
      total: 0.52
      efficiency: 0.41
      win: 0.51
      pick: 0.52
      fit: 0.77
    Titan's Bane:
      total: 0.55
      efficiency: 0.51
      win: 0.62
      pick: 0.22
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Pendulum Blade, The Reaper, Arondight, Tekko-Kagi, Avatar''s Parashu, Tyrfing,
    Transcendence, Silverbranch Bow, Genji''s Guard, Damaru, Toxic Blade, Avenging
    Blade, Eye of the Storm, Breastplate of Valor, Shield Splitter, Chandra''s Grace,
    Dominance, Riptalon, Lernaean Bow, Golden Blade, Bloodforge, Oath-Sworn Spear,
    Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.48
      pick: 0.17
      fit: 0.78
    Transcendence:
      total: 0.43
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.27
      fit: 0.54
    The Crusher:
      total: 0.5
      efficiency: 0.45
      win: 0.52
      pick: 0.16
      fit: 0.66
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.51
      pick: 0.52
      fit: 0.76
    Titan's Bane:
      total: 0.57
      efficiency: 0.51
      win: 0.62
      pick: 0.22
      fit: 0.66
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Shield Splitter, The Reaper, Phoenix Feather, Genji''s Guard, Yogi''s
    Necklace, Erosion, Freya''s Tears, Eye of Providence, Draconic Scale, Oni Hunter''s
    Garb, Breastplate of Valor, Chandra''s Grace, Midgardian Mail, Shifter''s Shield,
    Wyrmskin Hide, Avenging Blade, Leviathan''s Hide, Stone of Binding, Ancile, Glorious
    Pridwen.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.48
      pick: 0.17
      fit: 0.44
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.73
    Titan's Bane:
      total: 0.54
      efficiency: 0.51
      win: 0.62
      pick: 0.22
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.62
      win: 0.51
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Jotunn's Revenge
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Tekko-Kagi
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
    for this god: The Reaper, Tekko-Kagi, Pendulum Blade, Avatar''s Parashu, Avenging
    Blade, Silverbranch Bow, Toxic Blade, Arondight, Tyrfing, Riptalon, Oath-Sworn
    Spear, Transcendence, Eye of the Storm, Shield Splitter, Dominance, Golden Blade,
    Lernaean Bow, Bloodforge, Screeching Gargoyle, Genji''s Guard, Damaru, Rage, Breastplate
    of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.48
      pick: 0.17
      fit: 1.0
    The Reaper:
      total: 0.54
      efficiency: 0.47
      win: 0.51
      pick: 0.0
      fit: 0.94
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.44
      win: 0.51
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.55
      efficiency: 0.45
      win: 0.52
      pick: 0.16
      fit: 1.0
    Heartseeker:
      total: 0.55
      efficiency: 0.41
      win: 0.51
      pick: 0.52
      fit: 1.0
    Titan's Bane:
      total: 0.62
      efficiency: 0.51
      win: 0.62
      pick: 0.22
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Riptalon
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
    this god: Tyrfing, Tekko-Kagi, Silverbranch Bow, Riptalon, Golden Blade, Toxic
    Blade, Lernaean Bow, The Reaper, Dominance, Qin''s Blade, Sun Beam Bow, Berserker''s
    Shield, Arondight, Dagger of Frenzy, Bloodforge, Transcendence, Pendulum Blade,
    Avatar''s Parashu, Hastened Fatalis, Vital Amplifier, Avenging Blade, Eye of the
    Storm, Shield Splitter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.48
      pick: 0.17
      fit: 0.37
    Tyrfing:
      total: 0.51
      efficiency: 0.46
      win: 0.51
      pick: 0.0
      fit: 0.79
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.65
    Riptalon:
      total: 0.51
      efficiency: 0.45
      win: 0.51
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.69
    Titan's Bane:
      total: 0.53
      efficiency: 0.51
      win: 0.62
      pick: 0.22
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
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
    + fit + win/pick). Underrated for this god: Arondight, Pendulum Blade, Genji''s
    Guard, Damaru, Breastplate of Valor, Chandra''s Grace, The Reaper, Tekko-Kagi,
    Screeching Gargoyle, Tyrfing, Eye of Erebus, Transcendence, Avatar''s Parashu,
    Freya''s Tears, Shield of the Phoenix, Silverbranch Bow, Avenging Blade, Eye of
    the Storm, Shield Splitter, Toxic Blade, Gladiator''s Shield, Dominance, Golden
    Blade, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.48
      pick: 0.17
      fit: 0.85
    Hydra's Lament:
      total: 0.53
      efficiency: 0.52
      win: 0.5
      pick: 0.27
      fit: 0.75
    Arondight:
      total: 0.5
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.65
    Pendulum Blade:
      total: 0.49
      efficiency: 0.39
      win: 0.51
      pick: 0.0
      fit: 0.85
    Heartseeker:
      total: 0.48
      efficiency: 0.41
      win: 0.51
      pick: 0.52
      fit: 0.55
    Titan's Bane:
      total: 0.54
      efficiency: 0.51
      win: 0.62
      pick: 0.22
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
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Tekko-Kagi
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
    Underrated for this god: The Reaper, Tekko-Kagi, Pendulum Blade, Avatar''s Parashu,
    Tyrfing, Arondight, Transcendence, Golden Blade, Avenging Blade, Eye of the Storm,
    Shield Splitter, Dominance, Silverbranch Bow, Lernaean Bow, Bloodforge, Toxic
    Blade, Oath-Sworn Spear, Riptalon, Rage, Musashi''s Dual Swords, Deathbringer,
    Sanguine Lash, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.48
      pick: 0.17
      fit: 1.0
    The Reaper:
      total: 0.53
      efficiency: 0.47
      win: 0.51
      pick: 0.0
      fit: 0.91
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.44
      win: 0.51
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.55
      efficiency: 0.45
      win: 0.52
      pick: 0.16
      fit: 1.0
    Heartseeker:
      total: 0.55
      efficiency: 0.41
      win: 0.51
      pick: 0.52
      fit: 1.0
    Titan's Bane:
      total: 0.62
      efficiency: 0.51
      win: 0.62
      pick: 0.22
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
