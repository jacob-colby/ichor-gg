---
type: smite-build
god: Pele
mode: Conquest
builds:
- source: community
  aspect: Aspect of Obsidian
  aspect_pick_rate: 0.03
  aspect_win_rate: 1.0
  slot_order:
  - name: Barbed Carver
    pick_rate: 0.4
    win_rate: 0.71
    alternates:
    - name: The Reaper
      pick_rate: 0.2
      win_rate: 0.71
    - name: Jotunn's Revenge
      pick_rate: 0.17
      win_rate: 0.33
  - name: The Reaper
    pick_rate: 0.43
    win_rate: 0.67
    alternates:
    - name: Barbed Carver
      pick_rate: 0.26
      win_rate: 0.11
    - name: Jotunn's Revenge
      pick_rate: 0.2
      win_rate: 0.71
  - name: The Crusher
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: The Reaper
      pick_rate: 0.31
      win_rate: 0.27
    - name: Barbed Carver
      pick_rate: 0.26
      win_rate: 0.67
  - name: Heartseeker
    pick_rate: 0.39
    win_rate: 0.62
    alternates:
    - name: Titan's Bane
      pick_rate: 0.18
      win_rate: 0.17
    - name: The Crusher
      pick_rate: 0.15
      win_rate: 0.8
  - name: Avatar's Parashu
    pick_rate: 0.14
    win_rate: 0.75
    alternates:
    - name: Heartseeker
      pick_rate: 0.24
      win_rate: 0.29
    - name: Blinking Abyss
      pick_rate: 0.1
      win_rate: 0.67
  - name: Blinking Abyss
    pick_rate: 0.19
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.67
    - name: Magi's Cloak
      pick_rate: 0.14
      win_rate: 0.67
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.4
    win_rate: 0.57
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.29
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.8
  source_url: https://smitebrain.com/gods/pele/
  last_verified: '2026-08-26'
  god_win_rate: 0.5428571428571428
  god_matches_won: 19
  god_matches_played: 35
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Hydra's Lament
  - Transcendence
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
    this god: Hydra''s Lament, Pendulum Blade, Tyrfing, Arondight, Tekko-Kagi, Transcendence,
    Runeforged Hammer, Golden Blade, Avenging Blade, Silverbranch Bow, Riptalon, Lernaean
    Bow, Shield Splitter, Dominance, Toxic Blade, Oath-Sworn Spear, Breastplate of
    Valor, Bloodforge, Genji''s Guard, Deathbringer, Eye of the Storm, Damaru, Daybreak
    Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.73
      efficiency: 0.72
      win: 0.71
      pick: 0.27
      fit: 1.0
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.77
    The Reaper:
      total: 0.62
      efficiency: 0.5
      win: 0.67
      pick: 0.59
      fit: 0.78
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.62
      pick: 0.65
      fit: 0.98
    Avatar's Parashu:
      total: 0.63
      efficiency: 0.45
      win: 0.75
      pick: 0.3
      fit: 0.78
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - The Reaper
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Transcendence, Arondight, Pendulum Blade, Tyrfing, Runeforged Hammer,
    Tekko-Kagi, Avenging Blade, Dominance, Breastplate of Valor, Golden Blade, Lernaean
    Bow, Genji''s Guard, Shield Splitter, Silverbranch Bow, Oath-Sworn Spear, Daybreak
    Gavel, Riptalon, Toxic Blade, Bloodforge, Yogi''s Necklace, Deathbringer, Eye
    of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.71
      pick: 0.27
      fit: 0.71
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.59
      fit: 0.47
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.62
      pick: 0.65
      fit: 0.77
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.3
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Hydra's Lament
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, Pendulum Blade, Arondight, Tekko-Kagi, Tyrfing, Transcendence,
    Runeforged Hammer, Silverbranch Bow, Riptalon, Avenging Blade, Breastplate of
    Valor, Toxic Blade, Genji''s Guard, Golden Blade, Lernaean Bow, Shield Splitter,
    Dominance, Daybreak Gavel, Oath-Sworn Spear, Eye of Erebus, Screeching Gargoyle,
    Bloodforge, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.72
      win: 0.71
      pick: 0.27
      fit: 0.78
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.59
      efficiency: 0.5
      win: 0.67
      pick: 0.59
      fit: 0.56
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.62
      pick: 0.65
      fit: 0.76
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.45
      win: 0.75
      pick: 0.3
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Freya''s Tears,
    Runeforged Hammer, Shield Splitter, Shifter''s Shield, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye
    of Providence, Draconic Scale, Hydra''s Lament, Phoenix Feather, Chandra''s Grace,
    Avenging Blade, Glorious Pridwen, Stone of Binding, Midgardian Mail, Daybreak
    Gavel, Golden Blade, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.71
      pick: 0.27
      fit: 0.48
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.62
    Runeforged Hammer:
      total: 0.58
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.43
    The Reaper:
      total: 0.61
      efficiency: 0.5
      win: 0.67
      pick: 0.59
      fit: 0.67
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Pendulum Blade
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Pendulum Blade, Hydra''s Lament, Tekko-Kagi, Avenging Blade, Silverbranch
    Bow, Riptalon, Arondight, Tyrfing, Toxic Blade, Oath-Sworn Spear, Transcendence,
    Runeforged Hammer, Golden Blade, Lernaean Bow, Screeching Gargoyle, Shield Splitter,
    Dominance, Breastplate of Valor, Genji''s Guard, Daybreak Gavel, Bloodforge, Deathbringer,
    Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.73
      efficiency: 0.72
      win: 0.71
      pick: 0.27
      fit: 1.0
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.3
    The Reaper:
      total: 0.63
      efficiency: 0.5
      win: 0.67
      pick: 0.59
      fit: 0.85
    Pendulum Blade:
      total: 0.6
      efficiency: 0.42
      win: 0.67
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.63
      efficiency: 0.47
      win: 0.62
      pick: 0.65
      fit: 1.0
    Avatar's Parashu:
      total: 0.64
      efficiency: 0.45
      win: 0.75
      pick: 0.3
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Lernaean Bow
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
    Blade, Toxic Blade, Hydra''s Lament, Dominance, Qin''s Blade, Sun Beam Bow, Arondight,
    Pendulum Blade, Transcendence, Berserker''s Shield, Runeforged Hammer, Dagger
    of Frenzy, Avenging Blade, Vital Amplifier, Hastened Fatalis, Bloodforge, The
    Executioner, Daybreak Gavel.'
  slot_scores:
    Lernaean Bow:
      total: 0.56
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.71
      pick: 0.27
      fit: 0.42
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.67
      pick: 0.0
      fit: 0.74
    The Reaper:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.59
      fit: 0.41
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.74
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Pendulum Blade
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - Heartseeker
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Pendulum Blade, Arondight,
    Breastplate of Valor, Genji''s Guard, Tyrfing, Eye of Erebus, Transcendence, Screeching
    Gargoyle, Runeforged Hammer, Chandra''s Grace, Freya''s Tears, Silverbranch Bow,
    Tekko-Kagi, Avenging Blade, Shield of the Phoenix, Riptalon, Golden Blade, Daybreak
    Gavel, Toxic Blade, Lernaean Bow, Gladiator''s Shield, Shield Splitter, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.72
      win: 0.71
      pick: 0.27
      fit: 0.85
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.75
    Arondight:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.0
      fit: 0.65
    Pendulum Blade:
      total: 0.58
      efficiency: 0.42
      win: 0.67
      pick: 0.0
      fit: 0.85
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.62
      pick: 0.65
      fit: 0.55
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.3
      fit: 0.35
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
    Tekko-Kagi, Transcendence, Runeforged Hammer, Golden Blade, Avenging Blade, Silverbranch
    Bow, Riptalon, Lernaean Bow, Shield Splitter, Dominance, Toxic Blade, Oath-Sworn
    Spear, Breastplate of Valor, Bloodforge, Genji''s Guard, Deathbringer, Eye of
    the Storm, Damaru, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.73
      efficiency: 0.72
      win: 0.71
      pick: 0.27
      fit: 1.0
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.77
    Pendulum Blade:
      total: 0.6
      efficiency: 0.42
      win: 0.67
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.62
      pick: 0.65
      fit: 0.98
    Titan's Bane:
      total: 0.39
      efficiency: 0.47
      win: 0.17
      pick: 0.3
      fit: 0.88
  starter: *id001
---
