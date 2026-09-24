---
type: smite-build
god: Pele
mode: Conquest
builds:
- source: community
  aspect: Aspect of Obsidian
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.67
  slot_order:
  - name: Barbed Carver
    pick_rate: 0.34
    win_rate: 0.62
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.23
      win_rate: 0.43
    - name: Jotunn's Revenge
      pick_rate: 0.18
      win_rate: 0.55
  - name: The Reaper
    pick_rate: 0.39
    win_rate: 0.63
    alternates:
    - name: Barbed Carver
      pick_rate: 0.18
      win_rate: 0.64
    - name: Jotunn's Revenge
      pick_rate: 0.15
      win_rate: 0.33
  - name: The Crusher
    pick_rate: 0.18
    win_rate: 0.82
    alternates:
    - name: The Reaper
      pick_rate: 0.2
      win_rate: 0.42
    - name: Barbed Carver
      pick_rate: 0.13
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.37
    win_rate: 0.62
    alternates:
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.8
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.2
  - name: Magi's Cloak
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Heartseeker
      pick_rate: 0.17
      win_rate: 0.5
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.5
  - name: Skeggox
    pick_rate: 0.21
    win_rate: 0.17
    alternates:
    - name: Titan's Bane
      pick_rate: 0.14
      win_rate: 0.75
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.37
    win_rate: 0.65
  - name: Leather Cowl
    pick_rate: 0.26
    win_rate: 0.56
  - name: Bumba's Cudgel
    pick_rate: 0.11
    win_rate: 0.29
  source_url: https://smitebrain.com/gods/pele/
  last_verified: '2026-09-24'
  god_win_rate: 0.5806451612903226
  god_matches_won: 36
  god_matches_played: 62
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Magi's Cloak — magical protection
    swap_item: Magi's Cloak
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Pendulum Blade, Tyrfing, Arondight, Avatar''s Parashu,
    Tekko-Kagi, Transcendence, Runeforged Hammer, Golden Blade, Avenging Blade, Silverbranch
    Bow, Riptalon, Lernaean Bow, Shield Splitter, Dominance, Toxic Blade, Oath-Sworn
    Spear, Breastplate of Valor, Bloodforge, Genji''s Guard, Deathbringer, Eye of
    the Storm, Damaru, Daybreak Gavel.'
  slot_scores:
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.77
    The Reaper:
      total: 0.6
      efficiency: 0.5
      win: 0.63
      pick: 0.53
      fit: 0.78
    The Crusher:
      total: 0.68
      efficiency: 0.47
      win: 0.82
      pick: 0.28
      fit: 0.88
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.62
      pick: 0.62
      fit: 0.98
    Titan's Bane:
      total: 0.66
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.88
  community_ordered:
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Transcendence, Arondight, Pendulum Blade, Tyrfing, Avatar''s Parashu,
    Runeforged Hammer, Tekko-Kagi, Avenging Blade, Dominance, Breastplate of Valor,
    Golden Blade, Lernaean Bow, Genji''s Guard, Shield Splitter, Silverbranch Bow,
    Oath-Sworn Spear, Daybreak Gavel, Riptalon, Toxic Blade, Bloodforge, Yogi''s Necklace,
    Deathbringer, Eye of the Storm.'
  slot_scores:
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.55
      efficiency: 0.5
      win: 0.63
      pick: 0.53
      fit: 0.47
    The Crusher:
      total: 0.63
      efficiency: 0.47
      win: 0.82
      pick: 0.28
      fit: 0.57
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.62
      pick: 0.62
      fit: 0.77
    Titan's Bane:
      total: 0.61
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.57
  community_ordered:
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Magi's Cloak
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Magi's Cloak
  - Hydra's Lament
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
    god: Hydra''s Lament, Pendulum Blade, Arondight, Avatar''s Parashu, Tekko-Kagi,
    Tyrfing, Transcendence, Runeforged Hammer, Silverbranch Bow, Riptalon, Avenging
    Blade, Breastplate of Valor, Toxic Blade, Genji''s Guard, Golden Blade, Lernaean
    Bow, Shield Splitter, Dominance, Daybreak Gavel, Oath-Sworn Spear, Eye of Erebus,
    Screeching Gargoyle, Bloodforge, Chandra''s Grace.'
  slot_scores:
    Magi's Cloak:
      total: 0.55
      efficiency: 0.26
      win: 1.0
      pick: 0.22
      fit: 0.0
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.63
      pick: 0.53
      fit: 0.56
    The Crusher:
      total: 0.65
      efficiency: 0.47
      win: 0.82
      pick: 0.28
      fit: 0.66
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.62
      pick: 0.62
      fit: 0.76
    Titan's Bane:
      total: 0.62
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.66
  community_ordered:
  - Magi's Cloak
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - The Reaper
  - Magi's Cloak
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - The Reaper
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Freya''s Tears,
    Runeforged Hammer, Shield Splitter, Shifter''s Shield, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye
    of Providence, Draconic Scale, Hydra''s Lament, Phoenix Feather, Chandra''s Grace,
    Avenging Blade, Glorious Pridwen, Stone of Binding, Midgardian Mail, Daybreak
    Gavel, Golden Blade, Hide of the Nemean Lion.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.62
    The Reaper:
      total: 0.58
      efficiency: 0.5
      win: 0.63
      pick: 0.53
      fit: 0.67
    Magi's Cloak:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.22
      fit: 0.32
    The Crusher:
      total: 0.62
      efficiency: 0.47
      win: 0.82
      pick: 0.28
      fit: 0.47
    Titan's Bane:
      total: 0.6
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.47
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.82
  community_ordered:
  - The Reaper
  - Magi's Cloak
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Pendulum Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Magi's Cloak — magical protection
    swap_item: Magi's Cloak
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Pendulum Blade, Avatar''s Parashu, Hydra''s Lament, Tekko-Kagi,
    Avenging Blade, Silverbranch Bow, Riptalon, Arondight, Tyrfing, Toxic Blade, Oath-Sworn
    Spear, Transcendence, Runeforged Hammer, Golden Blade, Lernaean Bow, Screeching
    Gargoyle, Shield Splitter, Dominance, Breastplate of Valor, Genji''s Guard, Daybreak
    Gavel, Bloodforge, Deathbringer, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.33
      pick: 0.2
      fit: 1.0
    The Reaper:
      total: 0.61
      efficiency: 0.5
      win: 0.63
      pick: 0.53
      fit: 0.85
    Pendulum Blade:
      total: 0.58
      efficiency: 0.42
      win: 0.62
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.69
      efficiency: 0.47
      win: 0.82
      pick: 0.28
      fit: 0.95
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.62
      pick: 0.62
      fit: 1.0
    Titan's Bane:
      total: 0.67
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.95
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Blade, Toxic Blade, Hydra''s Lament, Dominance, Qin''s Blade, Sun Beam Bow, Arondight,
    Pendulum Blade, Transcendence, Berserker''s Shield, Avatar''s Parashu, Runeforged
    Hammer, Dagger of Frenzy, Avenging Blade, Vital Amplifier, Hastened Fatalis, Bloodforge,
    The Executioner, Daybreak Gavel.'
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.62
      pick: 0.0
      fit: 0.74
    The Reaper:
      total: 0.56
      efficiency: 0.55
      win: 0.63
      pick: 0.53
      fit: 0.41
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.74
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.61
      efficiency: 0.47
      win: 0.82
      pick: 0.28
      fit: 0.41
    Titan's Bane:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.41
  community_ordered:
  - The Reaper
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Hydra's Lament
  - Arondight
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Pendulum Blade
  - Arondight
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Pendulum Blade, Arondight,
    Breastplate of Valor, Genji''s Guard, Tyrfing, Avatar''s Parashu, Eye of Erebus,
    Transcendence, Screeching Gargoyle, Runeforged Hammer, Chandra''s Grace, Freya''s
    Tears, Silverbranch Bow, Tekko-Kagi, Avenging Blade, Shield of the Phoenix, Riptalon,
    Golden Blade, Daybreak Gavel, Toxic Blade, Lernaean Bow, Gladiator''s Shield,
    Shield Splitter, Dominance.'
  slot_scores:
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.75
    Arondight:
      total: 0.55
      efficiency: 0.5
      win: 0.62
      pick: 0.0
      fit: 0.65
    Pendulum Blade:
      total: 0.55
      efficiency: 0.42
      win: 0.62
      pick: 0.0
      fit: 0.85
    The Crusher:
      total: 0.61
      efficiency: 0.47
      win: 0.82
      pick: 0.28
      fit: 0.45
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.62
      pick: 0.62
      fit: 0.55
    Titan's Bane:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.45
  community_ordered:
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
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
    Underrated for this god: Hydra''s Lament, Pendulum Blade, Tyrfing, Arondight,
    Avatar''s Parashu, Tekko-Kagi, Transcendence, Runeforged Hammer, Golden Blade,
    Avenging Blade, Silverbranch Bow, Riptalon, Lernaean Bow, Shield Splitter, Dominance,
    Toxic Blade, Oath-Sworn Spear, Breastplate of Valor, Bloodforge, Genji''s Guard,
    Deathbringer, Eye of the Storm, Damaru, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.33
      pick: 0.2
      fit: 1.0
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.77
    Pendulum Blade:
      total: 0.58
      efficiency: 0.42
      win: 0.62
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.62
      pick: 0.62
      fit: 0.98
    Titan's Bane:
      total: 0.66
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
