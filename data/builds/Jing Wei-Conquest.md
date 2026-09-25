---
type: smite-build
god: Jing Wei
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.81
    win_rate: 0.49
    alternates:
    - name: Tyrfing
      pick_rate: 0.09
      win_rate: 0.33
    - name: Avenging Blade
      pick_rate: 0.04
      win_rate: 0.67
  - name: Dagger of Frenzy
    pick_rate: 0.63
    win_rate: 0.48
    alternates:
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 0.5
    - name: Hastened Fatalis
      pick_rate: 0.04
      win_rate: 1.0
  - name: Musashi's Dual Swords
    pick_rate: 0.24
    win_rate: 0.38
    alternates:
    - name: Dominance
      pick_rate: 0.24
      win_rate: 0.56
    - name: The Executioner
      pick_rate: 0.15
      win_rate: 0.6
  - name: Deathbringer
    pick_rate: 0.32
    win_rate: 0.55
    alternates:
    - name: Musashi's Dual Swords
      pick_rate: 0.19
      win_rate: 0.67
    - name: Silverbranch Bow
      pick_rate: 0.13
      win_rate: 0.63
  - name: Dominance
    pick_rate: 0.11
    win_rate: 0.57
    alternates:
    - name: Deathbringer
      pick_rate: 0.39
      win_rate: 0.54
    - name: Odysseus' Bow
      pick_rate: 0.08
      win_rate: 0.6
  - name: Blinking Abyss
    pick_rate: 0.15
    win_rate: 0.57
    alternates:
    - name: Dominance
      pick_rate: 0.15
      win_rate: 0.57
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 0.5
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.67
    win_rate: 0.62
  - name: Gilded Arrow
    pick_rate: 0.23
    win_rate: 0.19
  - name: Hunter's Cowl
    pick_rate: 0.06
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/jing-wei/
  last_verified: '2026-09-25'
  god_win_rate: 0.5
  god_matches_won: 35
  god_matches_played: 70
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-25'
  god_matches_analyzed: 2996
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Hastened Fatalis
  - Deathbringer
  - Dominance
  - Demon Blade
  flex_slots:
  - Dominance
  - Golden Blade
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Demon Blade, Golden Blade, Avenging Blade, Damaru, Rage,
    Qin''s Blade, Tekko-Kagi, Jotunn''s Revenge, Hydra''s Lament, Transcendence, The
    Reaper, Berserker''s Shield, Runeforged Hammer, Sun Beam Bow, Barbed Carver, Vital
    Amplifier, Bloodforge, Toxic Blade, Heartseeker, Shield Splitter, Tyrfing.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.64
    Hastened Fatalis:
      total: 0.63
      efficiency: 0.32
      win: 1.0
      pick: 0.05
      fit: 0.44
    Deathbringer:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.53
      fit: 0.54
    Dominance:
      total: 0.52
      efficiency: 0.45
      win: 0.57
      pick: 0.24
      fit: 0.64
    Demon Blade:
      total: 0.52
      efficiency: 0.38
      win: 0.57
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Hastened Fatalis
  - Deathbringer
  - Dominance
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Hastened Fatalis
  - Silverbranch Bow
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, The Reaper, Avenging Blade,
    Tekko-Kagi, Titan''s Bane, Golden Blade, The Crusher, Transcendence, Arondight,
    Demon Blade, Runeforged Hammer, Pendulum Blade, Toxic Blade, Avatar''s Parashu,
    Damaru, Rage, Qin''s Blade, Barbed Carver, Berserker''s Shield, Breastplate of
    Valor, Genji''s Guard, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.42
    Hastened Fatalis:
      total: 0.6
      efficiency: 0.32
      win: 1.0
      pick: 0.05
      fit: 0.22
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.63
      pick: 0.22
      fit: 0.33
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Hastened Fatalis
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Hastened Fatalis
  - Damaru
  - Deathbringer
  - Dominance
  - Demon Blade
  flex_slots:
  - Dominance
  - Damaru
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Demon Blade, Golden Blade, Avenging Blade, Damaru, Rage,
    Qin''s Blade, Jotunn''s Revenge, Hydra''s Lament, Tekko-Kagi, Transcendence, The
    Reaper, Runeforged Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver, Bloodforge,
    Vital Amplifier, Heartseeker, Toxic Blade, Shield Splitter, The Crusher, Tyrfing.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.6
    Hastened Fatalis:
      total: 0.63
      efficiency: 0.32
      win: 1.0
      pick: 0.05
      fit: 0.41
    Damaru:
      total: 0.49
      efficiency: 0.42
      win: 0.57
      pick: 0.0
      fit: 0.57
    Deathbringer:
      total: 0.54
      efficiency: 0.51
      win: 0.55
      pick: 0.53
      fit: 0.57
    Dominance:
      total: 0.51
      efficiency: 0.45
      win: 0.57
      pick: 0.24
      fit: 0.6
    Demon Blade:
      total: 0.52
      efficiency: 0.38
      win: 0.57
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Hastened Fatalis
  - Deathbringer
  - Dominance
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Avenging Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Hastened Fatalis
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Avenging Blade, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Shield of the Phoenix, Shifter''s Shield, Pharaoh''s
    Curse, Yogi''s Necklace, Shield Splitter, Shogun''s Ofuda, Lernaean Bow, Eye of
    the Storm, Phoenix Feather, Erosion, The Reaper, Eye of Providence, Draconic Scale,
    Daybreak Gavel, Stone of Binding, Midgardian Mail, Umbral Link, Magi''s Cloak,
    Hide of the Nemean Lion, Leviathan''s Hide, Genji''s Guard, Tyrfing.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.54
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.67
      pick: 0.04
      fit: 0.38
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.5
    Hastened Fatalis:
      total: 0.6
      efficiency: 0.32
      win: 1.0
      pick: 0.05
      fit: 0.27
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Avenging Blade
  - Hastened Fatalis
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - Hastened Fatalis
  - Silverbranch Bow
  - Tekko-Kagi
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker,
    Titan''s Bane, The Crusher, Lernaean Bow, Toxic Blade, Avatar''s Parashu, Golden
    Blade, Demon Blade, Hydra''s Lament, Oath-Sworn Spear, Transcendence, Qin''s Blade,
    Damaru, Runeforged Hammer, Rage, Pendulum Blade, Berserker''s Shield, Sun Beam
    Bow, Barbed Carver, Tyrfing.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.44
      win: 0.67
      pick: 0.04
      fit: 0.54
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.47
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.56
    Hastened Fatalis:
      total: 0.61
      efficiency: 0.32
      win: 1.0
      pick: 0.05
      fit: 0.29
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.63
      pick: 0.22
      fit: 0.63
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Avenging Blade
  - Hastened Fatalis
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Hastened Fatalis
  - Deathbringer
  - Dominance
  - Silverbranch Bow
  flex_slots:
  - Deathbringer
  - Dominance
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
    this god: Hastened Fatalis, Lernaean Bow, Golden Blade, Avenging Blade, Demon
    Blade, Qin''s Blade, Sun Beam Bow, Jotunn''s Revenge, Hydra''s Lament, Damaru,
    Tekko-Kagi, Rage, Transcendence, Berserker''s Shield, Runeforged Hammer, The Reaper,
    Toxic Blade, Barbed Carver, Vital Amplifier, Bloodforge, Heartseeker, Daybreak
    Gavel, Tyrfing.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.55
    Hastened Fatalis:
      total: 0.64
      efficiency: 0.32
      win: 1.0
      pick: 0.05
      fit: 0.49
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.55
      pick: 0.53
      fit: 0.41
    Dominance:
      total: 0.51
      efficiency: 0.45
      win: 0.57
      pick: 0.24
      fit: 0.55
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.42
      win: 0.63
      pick: 0.22
      fit: 0.49
  community_ordered:
  - Hastened Fatalis
  - Deathbringer
  - Dominance
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Deathbringer
  - Hastened Fatalis
  flex_slots:
  - Deathbringer
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Lernaean Bow, Arondight, Avenging Blade, Golden Blade, Breastplate of Valor, Demon
    Blade, Genji''s Guard, Qin''s Blade, Transcendence, Runeforged Hammer, Damaru,
    Rage, Berserker''s Shield, The Reaper, Tekko-Kagi, Sun Beam Bow, Eye of Erebus,
    Daybreak Gavel, Barbed Carver, Vital Amplifier, Screeching Gargoyle, Chandra''s
    Grace, Tyrfing.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.51
    Arondight:
      total: 0.49
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.41
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.55
      pick: 0.53
      fit: 0.3
    Hastened Fatalis:
      total: 0.61
      efficiency: 0.32
      win: 1.0
      pick: 0.05
      fit: 0.28
  community_ordered:
  - Deathbringer
  - Hastened Fatalis
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Deathbringer
  - Dominance
  - Demon Blade
  flex_slots:
  - Deathbringer
  - Dominance
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Tyrfing, Lernaean Bow, Demon Blade, Golden Blade, Damaru,
    Rage, Qin''s Blade, Tekko-Kagi, Jotunn''s Revenge, Hydra''s Lament, Transcendence,
    The Reaper, Berserker''s Shield, Runeforged Hammer, Sun Beam Bow, Barbed Carver,
    Avenging Blade, Vital Amplifier, Bloodforge, Toxic Blade, Heartseeker, Shield
    Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.43
      efficiency: 0.48
      win: 0.33
      pick: 0.09
      fit: 0.75
    Deathbringer:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.53
      fit: 0.54
    Dominance:
      total: 0.52
      efficiency: 0.45
      win: 0.57
      pick: 0.24
      fit: 0.64
    Demon Blade:
      total: 0.52
      efficiency: 0.38
      win: 0.57
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Tyrfing
  - Deathbringer
  - Dominance
  starter: *id001
---
