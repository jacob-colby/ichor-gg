---
type: smite-build
god: Pele
mode: Conquest
builds:
- source: community
  aspect: Aspect of Obsidian
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.51
  slot_order:
  - name: Barbed Carver
    pick_rate: 0.34
    win_rate: 0.59
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.26
      win_rate: 0.5
    - name: The Reaper
      pick_rate: 0.12
      win_rate: 0.48
  - name: The Reaper
    pick_rate: 0.32
    win_rate: 0.57
    alternates:
    - name: Barbed Carver
      pick_rate: 0.22
      win_rate: 0.52
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.56
  - name: The Crusher
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: The Reaper
      pick_rate: 0.26
      win_rate: 0.56
    - name: Barbed Carver
      pick_rate: 0.1
      win_rate: 0.47
  - name: Heartseeker
    pick_rate: 0.4
    win_rate: 0.57
    alternates:
    - name: The Crusher
      pick_rate: 0.07
      win_rate: 0.65
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.38
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.61
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.58
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.55
  - name: Avatar's Parashu
    pick_rate: 0.11
    win_rate: 0.66
    alternates:
    - name: Skeggox
      pick_rate: 0.09
      win_rate: 0.39
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.55
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.41
    win_rate: 0.64
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.45
  - name: Bumba's Hammer
    pick_rate: 0.13
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/pele/
  last_verified: '2026-09-21'
  god_win_rate: 0.5403587443946188
  god_matches_won: 241
  god_matches_played: 446
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-21'
  god_matches_analyzed: 15551
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Hydra's Lament
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
      total: 0.64
      efficiency: 0.72
      win: 0.5
      pick: 0.26
      fit: 1.0
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.57
      pick: 0.44
      fit: 0.78
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.77
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.57
      pick: 0.67
      fit: 0.98
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.45
      win: 0.66
      pick: 0.34
      fit: 0.78
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Hydra's Lament
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
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.26
      fit: 0.71
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.39
    The Reaper:
      total: 0.52
      efficiency: 0.5
      win: 0.57
      pick: 0.44
      fit: 0.47
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.63
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.57
      pick: 0.67
      fit: 0.77
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.45
      win: 0.66
      pick: 0.34
      fit: 0.47
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Hydra's Lament
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
      total: 0.61
      efficiency: 0.72
      win: 0.5
      pick: 0.26
      fit: 0.78
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.22
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.57
      pick: 0.44
      fit: 0.56
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.57
      pick: 0.67
      fit: 0.76
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.66
      pick: 0.34
      fit: 0.56
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Freya's Tears
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
    Runeforged Hammer, Shield Splitter, Genji''s Guard, Breastplate of Valor, Eye
    of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye of Providence,
    Draconic Scale, Hydra''s Lament, Phoenix Feather, Chandra''s Grace, Avenging Blade,
    Glorious Pridwen, Stone of Binding, Midgardian Mail, Daybreak Gavel, Golden Blade,
    Hide of the Nemean Lion, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.26
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.62
    The Reaper:
      total: 0.55
      efficiency: 0.5
      win: 0.57
      pick: 0.44
      fit: 0.67
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.43
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.57
      pick: 0.67
      fit: 0.57
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
  - The Crusher
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
      total: 0.64
      efficiency: 0.72
      win: 0.5
      pick: 0.26
      fit: 1.0
    The Reaper:
      total: 0.58
      efficiency: 0.5
      win: 0.57
      pick: 0.44
      fit: 0.85
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.22
      fit: 0.95
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.57
      pick: 0.67
      fit: 1.0
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.55
      pick: 0.17
      fit: 0.95
    Avatar's Parashu:
      total: 0.6
      efficiency: 0.45
      win: 0.66
      pick: 0.34
      fit: 0.85
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  - Heartseeker
  - Silverbranch Bow
  flex_slots:
  - The Reaper
  - Heartseeker
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
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.26
      fit: 0.42
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.74
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.44
      fit: 0.41
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.74
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.57
      pick: 0.67
      fit: 0.51
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
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
  - Arondight
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Pendulum Blade, Arondight,
    Breastplate of Valor, Genji''s Guard, Tyrfing, Eye of Erebus, Transcendence, Screeching
    Gargoyle, Runeforged Hammer, Chandra''s Grace, Freya''s Tears, Silverbranch Bow,
    Tekko-Kagi, Avenging Blade, Shield of the Phoenix, Riptalon, Golden Blade, Daybreak
    Gavel, Toxic Blade, Lernaean Bow, Gladiator''s Shield, Shield Splitter, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.5
      pick: 0.26
      fit: 0.85
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.75
    Arondight:
      total: 0.53
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.65
    Pendulum Blade:
      total: 0.53
      efficiency: 0.42
      win: 0.56
      pick: 0.0
      fit: 0.85
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.57
      pick: 0.67
      fit: 0.55
    Avatar's Parashu:
      total: 0.52
      efficiency: 0.45
      win: 0.66
      pick: 0.34
      fit: 0.35
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
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
      total: 0.64
      efficiency: 0.72
      win: 0.5
      pick: 0.26
      fit: 1.0
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.77
    Pendulum Blade:
      total: 0.55
      efficiency: 0.42
      win: 0.56
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.57
      pick: 0.67
      fit: 0.98
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.55
      pick: 0.17
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
