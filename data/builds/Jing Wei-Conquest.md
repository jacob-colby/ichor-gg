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
    pick_rate: 0.85
    win_rate: 0.51
    alternates:
    - name: Tyrfing
      pick_rate: 0.07
      win_rate: 0.38
    - name: Avenging Blade
      pick_rate: 0.03
      win_rate: 0.5
  - name: Dagger of Frenzy
    pick_rate: 0.67
    win_rate: 0.52
    alternates:
    - name: Riptalon
      pick_rate: 0.05
      win_rate: 0.6
    - name: Musashi's Dual Swords
      pick_rate: 0.05
      win_rate: 0.44
  - name: Dominance
    pick_rate: 0.25
    win_rate: 0.53
    alternates:
    - name: Musashi's Dual Swords
      pick_rate: 0.23
      win_rate: 0.53
    - name: The Executioner
      pick_rate: 0.11
      win_rate: 0.48
  - name: Deathbringer
    pick_rate: 0.37
    win_rate: 0.56
    alternates:
    - name: Dominance
      pick_rate: 0.15
      win_rate: 0.45
    - name: Riptalon
      pick_rate: 0.12
      win_rate: 0.45
  - name: Riptalon
    pick_rate: 0.16
    win_rate: 0.86
    alternates:
    - name: Deathbringer
      pick_rate: 0.32
      win_rate: 0.47
    - name: Dominance
      pick_rate: 0.11
      win_rate: 0.53
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.64
    alternates:
    - name: Dominance
      pick_rate: 0.11
      win_rate: 0.67
    - name: Hunter's Bow
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.71
    win_rate: 0.61
  - name: Gilded Arrow
    pick_rate: 0.22
    win_rate: 0.21
  - name: Hunter's Cowl
    pick_rate: 0.05
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/jing-wei/
  last_verified: '2026-10-01'
  god_win_rate: 0.5050505050505051
  god_matches_won: 100
  god_matches_played: 198
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-10-01'
  god_matches_analyzed: 10386
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Riptalon
  - Dominance
  - Deathbringer
  - Demon Blade
  flex_slots:
  - Demon Blade
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
    this god: Lernaean Bow, Demon Blade, Golden Blade, Damaru, Rage, Qin''s Blade,
    Tekko-Kagi, Jotunn''s Revenge, Hydra''s Lament, Tyrfing, Transcendence, Silverbranch
    Bow, The Reaper, Berserker''s Shield, Runeforged Hammer, Sun Beam Bow, Barbed
    Carver, Vital Amplifier, Bloodforge, Toxic Blade, Avenging Blade, Heartseeker,
    Odysseus'' Bow, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.64
    Riptalon:
      total: 0.63
      efficiency: 0.41
      win: 0.86
      pick: 0.35
      fit: 0.57
    Dominance:
      total: 0.51
      efficiency: 0.45
      win: 0.53
      pick: 0.39
      fit: 0.64
    Deathbringer:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.62
      fit: 0.54
    Demon Blade:
      total: 0.5
      efficiency: 0.38
      win: 0.53
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Riptalon
  - Dominance
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Dominance
  - Deathbringer
  - Riptalon
  flex_slots:
  - Dominance
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
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Silverbranch
    Bow, Titan''s Bane, Golden Blade, The Crusher, Transcendence, Arondight, Demon
    Blade, Runeforged Hammer, Pendulum Blade, Toxic Blade, Avatar''s Parashu, Damaru,
    Rage, Qin''s Blade, Barbed Carver, Berserker''s Shield, Breastplate of Valor,
    Avenging Blade, Genji''s Guard, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.42
    Dominance:
      total: 0.49
      efficiency: 0.45
      win: 0.53
      pick: 0.39
      fit: 0.5
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.62
      fit: 0.34
    Riptalon:
      total: 0.64
      efficiency: 0.51
      win: 0.86
      pick: 0.35
      fit: 0.39
  community_ordered:
  - Dominance
  - Deathbringer
  - Riptalon
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Musashi's Dual Swords
  - Riptalon
  - Dominance
  - Deathbringer
  - Demon Blade
  flex_slots:
  - Dominance
  - Demon Blade
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
    this god: Lernaean Bow, Demon Blade, Golden Blade, Damaru, Rage, Qin''s Blade,
    Jotunn''s Revenge, Hydra''s Lament, Tekko-Kagi, Transcendence, The Reaper, Tyrfing,
    Runeforged Hammer, Silverbranch Bow, Berserker''s Shield, Sun Beam Bow, Barbed
    Carver, Bloodforge, Vital Amplifier, Avenging Blade, Heartseeker, Toxic Blade,
    Shield Splitter, The Crusher.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.6
    Musashi's Dual Swords:
      total: 0.5
      efficiency: 0.46
      win: 0.53
      pick: 0.36
      fit: 0.57
    Riptalon:
      total: 0.63
      efficiency: 0.41
      win: 0.86
      pick: 0.35
      fit: 0.53
    Dominance:
      total: 0.5
      efficiency: 0.45
      win: 0.53
      pick: 0.39
      fit: 0.6
    Deathbringer:
      total: 0.55
      efficiency: 0.51
      win: 0.56
      pick: 0.62
      fit: 0.57
    Demon Blade:
      total: 0.5
      efficiency: 0.38
      win: 0.53
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Musashi's Dual Swords
  - Riptalon
  - Dominance
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Riptalon
  - Deathbringer
  - Amanita Charm
  flex_slots:
  - Deathbringer
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
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Golden Blade, Runeforged
    Hammer, Shield of the Phoenix, Shifter''s Shield, Pharaoh''s Curse, Yogi''s Necklace,
    Shield Splitter, Shogun''s Ofuda, Lernaean Bow, Eye of the Storm, Phoenix Feather,
    Erosion, The Reaper, Eye of Providence, Draconic Scale, Daybreak Gavel, Stone
    of Binding, Midgardian Mail, Umbral Link, Magi''s Cloak, Hide of the Nemean Lion,
    Leviathan''s Hide, Genji''s Guard, Avenging Blade, Tyrfing.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.5
    Riptalon:
      total: 0.64
      efficiency: 0.41
      win: 0.86
      pick: 0.35
      fit: 0.64
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.62
      fit: 0.32
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Silverbranch Bow
  - Riptalon
  - Tekko-Kagi
  - Deathbringer
  - Heartseeker
  flex_slots:
  - Deathbringer
  - Heartseeker
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
    for this god: Silverbranch Bow, Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker,
    Titan''s Bane, The Crusher, Lernaean Bow, Toxic Blade, Avatar''s Parashu, Golden
    Blade, Avenging Blade, Demon Blade, Hydra''s Lament, Oath-Sworn Spear, Transcendence,
    Qin''s Blade, Damaru, Runeforged Hammer, Rage, Pendulum Blade, Berserker''s Shield,
    Sun Beam Bow, Barbed Carver, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.47
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.63
    Riptalon:
      total: 0.69
      efficiency: 0.51
      win: 0.86
      pick: 0.35
      fit: 0.72
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.69
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.62
      fit: 0.36
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Dagger of Frenzy
  - Dominance
  - Deathbringer
  - Riptalon
  flex_slots:
  - Dominance
  - Dagger of Frenzy
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
    this god: Lernaean Bow, Golden Blade, Demon Blade, Qin''s Blade, Silverbranch
    Bow, Tyrfing, Sun Beam Bow, Jotunn''s Revenge, Hydra''s Lament, Damaru, Tekko-Kagi,
    Rage, Transcendence, Berserker''s Shield, Runeforged Hammer, The Reaper, Toxic
    Blade, Barbed Carver, Vital Amplifier, Hastened Fatalis, Bloodforge, Avenging
    Blade, Heartseeker, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.55
    Dagger of Frenzy:
      total: 0.48
      efficiency: 0.37
      win: 0.52
      pick: 0.91
      fit: 0.49
    Dominance:
      total: 0.5
      efficiency: 0.45
      win: 0.53
      pick: 0.39
      fit: 0.55
    Deathbringer:
      total: 0.52
      efficiency: 0.51
      win: 0.56
      pick: 0.62
      fit: 0.41
    Riptalon:
      total: 0.63
      efficiency: 0.41
      win: 0.86
      pick: 0.35
      fit: 0.59
  community_ordered:
  - Dagger of Frenzy
  - Dominance
  - Deathbringer
  - Riptalon
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Deathbringer
  - Riptalon
  flex_slots:
  - Lernaean Bow
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
    Lernaean Bow, Arondight, Golden Blade, Breastplate of Valor, Demon Blade, Genji''s
    Guard, Qin''s Blade, Transcendence, Runeforged Hammer, Damaru, Rage, Berserker''s
    Shield, The Reaper, Silverbranch Bow, Tekko-Kagi, Sun Beam Bow, Eye of Erebus,
    Daybreak Gavel, Barbed Carver, Vital Amplifier, Screeching Gargoyle, Tyrfing,
    Chandra''s Grace, Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.53
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.51
    Arondight:
      total: 0.48
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.41
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.56
      pick: 0.62
      fit: 0.3
    Riptalon:
      total: 0.6
      efficiency: 0.41
      win: 0.86
      pick: 0.35
      fit: 0.35
  community_ordered:
  - Deathbringer
  - Riptalon
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Dominance
  - Deathbringer
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
    Silverbranch Bow, The Reaper, Berserker''s Shield, Runeforged Hammer, Sun Beam
    Bow, Barbed Carver, Avenging Blade, Vital Amplifier, Bloodforge, Toxic Blade,
    Heartseeker, Odysseus'' Bow, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.46
      efficiency: 0.48
      win: 0.38
      pick: 0.07
      fit: 0.75
    Dominance:
      total: 0.51
      efficiency: 0.45
      win: 0.53
      pick: 0.39
      fit: 0.64
    Deathbringer:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.62
      fit: 0.54
    Demon Blade:
      total: 0.5
      efficiency: 0.38
      win: 0.53
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Tyrfing
  - Dominance
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Riptalon
  - Deathbringer
  - Demon Blade
  flex_slots:
  - Deathbringer
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Tyrfing, Lernaean Bow, Demon Blade,
    Golden Blade, Damaru, Rage, Qin''s Blade, Tekko-Kagi, Jotunn''s Revenge, Hydra''s
    Lament, Transcendence, Silverbranch Bow, The Reaper, Berserker''s Shield, Runeforged
    Hammer, Sun Beam Bow, Barbed Carver, Avenging Blade, Vital Amplifier, Bloodforge,
    Toxic Blade, Heartseeker, Odysseus'' Bow, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.46
      efficiency: 0.48
      win: 0.38
      pick: 0.07
      fit: 0.75
    Riptalon:
      total: 0.63
      efficiency: 0.41
      win: 0.86
      pick: 0.35
      fit: 0.57
    Deathbringer:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.62
      fit: 0.54
    Demon Blade:
      total: 0.5
      efficiency: 0.38
      win: 0.53
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Tyrfing
  - Riptalon
  - Deathbringer
  swaps:
  - added: Riptalon
    removed: Dominance
    reason: community 86% win over 32 matches (vs 51% on this god), taking the model's
      weakest slot from Dominance
  starter: *id001
---
