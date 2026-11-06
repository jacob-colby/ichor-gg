---
type: smite-build
god: Pele
mode: Conquest
builds:
- source: community
  aspect: Aspect of Obsidian
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.6
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.35
    win_rate: 0.56
    alternates:
    - name: Barbed Carver
      pick_rate: 0.25
      win_rate: 0.4
    - name: Jotunn's Revenge
      pick_rate: 0.19
      win_rate: 0.53
  - name: Barbed Carver
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: The Reaper
      pick_rate: 0.17
      win_rate: 0.53
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.5
  - name: The Crusher
    pick_rate: 0.24
    win_rate: 0.5
    alternates:
    - name: The Reaper
      pick_rate: 0.15
      win_rate: 0.33
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.73
  - name: Heartseeker
    pick_rate: 0.28
    win_rate: 0.44
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.08
      win_rate: 0.63
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.54
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.5
  - name: Skeggox
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.2
    - name: Magi's Cloak
      pick_rate: 0.09
      win_rate: 0.6
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.46
    win_rate: 0.53
  - name: Leather Cowl
    pick_rate: 0.21
    win_rate: 0.43
  - name: Bluestone Brooch
    pick_rate: 0.08
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/pele/
  last_verified: '2026-11-06'
  god_win_rate: 0.5
  god_matches_won: 51
  god_matches_played: 102
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
  - Hydra's Lament
  - Arondight
  - The Crusher
  - Pendulum Blade
  flex_slots:
  - Arondight
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Pendulum Blade, Arondight, Tyrfing, Avatar''s Parashu,
    Tekko-Kagi, Transcendence, Runeforged Hammer, Dominance, Shield Splitter, Eye
    of the Storm, Avenging Blade, Golden Blade, Lernaean Bow, Damaru, Genji''s Guard,
    Silverbranch Bow, Bloodforge, Rage, Toxic Blade, Oath-Sworn Spear, Breastplate
    of Valor, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.5
      pick: 0.19
      fit: 1.0
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.56
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.77
    Arondight:
      total: 0.54
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.67
    The Crusher:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.37
      fit: 0.88
    Pendulum Blade:
      total: 0.54
      efficiency: 0.39
      win: 0.56
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Hydra's Lament
  - The Crusher
  - Arondight
  flex_slots:
  - Tyrfing
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Arondight, Tyrfing, Transcendence, Avatar''s Parashu, Pendulum Blade,
    Dominance, Tekko-Kagi, Runeforged Hammer, Genji''s Guard, Shield Splitter, Eye
    of the Storm, Avenging Blade, Damaru, Breastplate of Valor, Chandra''s Grace,
    Lernaean Bow, Golden Blade, Bloodforge, Rage, Yogi''s Necklace, Silverbranch Bow,
    Oath-Sworn Spear, Toxic Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.19
      fit: 0.71
    Transcendence:
      total: 0.48
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.5
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.46
    Hydra's Lament:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.37
      fit: 0.57
    Arondight:
      total: 0.5
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Arondight
  - The Crusher
  - Pendulum Blade
  flex_slots:
  - Arondight
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, Pendulum Blade, Arondight, Avatar''s Parashu, Tyrfing, Tekko-Kagi,
    Damaru, Genji''s Guard, Transcendence, Runeforged Hammer, Silverbranch Bow, Dominance,
    Shield Splitter, Eye of the Storm, Avenging Blade, Toxic Blade, Breastplate of
    Valor, Chandra''s Grace, Lernaean Bow, Golden Blade, Riptalon, Bloodforge, Rage,
    Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.19
      fit: 0.78
    Transcendence:
      total: 0.46
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.54
    Arondight:
      total: 0.5
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.37
      fit: 0.66
    Pendulum Blade:
      total: 0.51
      efficiency: 0.39
      win: 0.56
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Genji''s Guard,
    Berserker''s Shield, Shield Splitter, Phoenix Feather, Yogi''s Necklace, Runeforged
    Hammer, Draconic Scale, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s
    Garb, Erosion, Eye of Providence, Hydra''s Lament, Midgardian Mail, Regrowth Striders,
    Leviathan''s Hide, Glorious Pridwen, Hide of the Nemean Lion, Avenging Blade,
    Wyrmskin Hide, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.56
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.62
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.43
    Shifter's Shield:
      total: 0.59
      efficiency: 0.5
      win: 0.73
      pick: 0.17
      fit: 0.52
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tekko-Kagi
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Avatar''s Parashu, Pendulum Blade, Tekko-Kagi, Hydra''s Lament,
    Arondight, Tyrfing, Avenging Blade, Silverbranch Bow, Toxic Blade, Oath-Sworn
    Spear, Transcendence, Runeforged Hammer, Riptalon, Dominance, Shield Splitter,
    Eye of the Storm, Screeching Gargoyle, Damaru, Genji''s Guard, Golden Blade, Lernaean
    Bow, Bloodforge, Rage, Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.5
      pick: 0.19
      fit: 1.0
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.43
      win: 0.56
      pick: 0.0
      fit: 0.85
    Pendulum Blade:
      total: 0.54
      efficiency: 0.39
      win: 0.56
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.37
      fit: 0.95
    Heartseeker:
      total: 0.53
      efficiency: 0.45
      win: 0.44
      pick: 0.47
      fit: 1.0
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.46
      win: 0.56
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Tyrfing
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Tekko-Kagi
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Tyrfing, Riptalon, Silverbranch Bow, Tekko-Kagi, Golden Blade, Toxic
    Blade, Lernaean Bow, Dominance, Hydra''s Lament, Qin''s Blade, Arondight, Dagger
    of Frenzy, Avatar''s Parashu, Berserker''s Shield, Sun Beam Bow, Pendulum Blade,
    Bloodforge, Transcendence, Runeforged Hammer, Damaru, Genji''s Guard, Odysseus''
    Bow, Shield Splitter, Eye of the Storm.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.45
      win: 0.56
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.19
      fit: 0.42
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.74
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.6
    Riptalon:
      total: 0.52
      efficiency: 0.45
      win: 0.56
      pick: 0.0
      fit: 0.74
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Damaru
  - Arondight
  - Freya's Tears
  - Pendulum Blade
  flex_slots:
  - Freya's Tears
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Arondight, Pendulum
    Blade, Damaru, Genji''s Guard, Breastplate of Valor, Chandra''s Grace, Tyrfing,
    Avatar''s Parashu, Screeching Gargoyle, Eye of Erebus, Shield of the Phoenix,
    Tekko-Kagi, Transcendence, Runeforged Hammer, Dominance, Gladiator''s Shield,
    Shield Splitter, Eye of the Storm, Avenging Blade, Silverbranch Bow, Regrowth
    Striders, Toxic Blade, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.19
      fit: 0.85
    Hydra's Lament:
      total: 0.56
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.75
    Damaru:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.5
    Arondight:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.65
    Freya's Tears:
      total: 0.52
      efficiency: 0.38
      win: 0.67
      pick: 0.15
      fit: 0.5
    Pendulum Blade:
      total: 0.52
      efficiency: 0.39
      win: 0.56
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
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
    Underrated for this god: Hydra''s Lament, Pendulum Blade, Arondight, Tyrfing,
    Avatar''s Parashu, Tekko-Kagi, Transcendence, Runeforged Hammer, Dominance, Shield
    Splitter, Eye of the Storm, Avenging Blade, Golden Blade, Lernaean Bow, Damaru,
    Genji''s Guard, Silverbranch Bow, Bloodforge, Rage, Toxic Blade, Oath-Sworn Spear,
    Breastplate of Valor, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.5
      pick: 0.19
      fit: 1.0
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.56
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.77
    The Crusher:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.37
      fit: 0.88
    Heartseeker:
      total: 0.53
      efficiency: 0.45
      win: 0.44
      pick: 0.47
      fit: 0.98
    Titan's Bane:
      total: 0.4
      efficiency: 0.48
      win: 0.2
      pick: 0.28
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
