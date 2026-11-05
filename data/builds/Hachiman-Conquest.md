---
type: smite-build
god: Hachiman
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Steel Wind
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.42
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.66
    win_rate: 0.49
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.37
    - name: Tyrfing
      pick_rate: 0.09
      win_rate: 0.49
  - name: Dagger of Frenzy
    pick_rate: 0.55
    win_rate: 0.46
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.49
    - name: Tyrfing
      pick_rate: 0.07
      win_rate: 0.48
  - name: Dominance
    pick_rate: 0.32
    win_rate: 0.47
    alternates:
    - name: The Executioner
      pick_rate: 0.15
      win_rate: 0.47
    - name: Odysseus' Bow
      pick_rate: 0.09
      win_rate: 0.57
  - name: Riptalon
    pick_rate: 0.25
    win_rate: 0.45
    alternates:
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.47
    - name: Dominance
      pick_rate: 0.12
      win_rate: 0.53
  - name: Deathbringer
    pick_rate: 0.19
    win_rate: 0.52
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.13
      win_rate: 0.53
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.49
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.58
    alternates:
    - name: Deathbringer
      pick_rate: 0.09
      win_rate: 0.58
    - name: Riptalon
      pick_rate: 0.08
      win_rate: 0.55
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.44
    win_rate: 0.52
  - name: Gilded Arrow
    pick_rate: 0.2
    win_rate: 0.36
  - name: Hunter's Cowl
    pick_rate: 0.1
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/hachiman/
  last_verified: '2026-11-04'
  god_win_rate: 0.46682750301568154
  god_matches_won: 387
  god_matches_played: 829
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Tyrfing
  - Dominance
  - The Reaper
  - Tekko-Kagi
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Dominance
  - Deathbringer
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
    this god: Tyrfing, The Reaper, Tekko-Kagi, Lernaean Bow, The Crusher, Heartseeker,
    Jotunn''s Revenge, Titan''s Bane, Golden Blade, Demon Blade, Rage, Toxic Blade,
    Hydra''s Lament, Qin''s Blade, Avatar''s Parashu, Bloodforge, Barbed Carver, Transcendence,
    Runeforged Hammer, Berserker''s Shield, Musashi''s Dual Swords, Shield Splitter,
    Eye of the Storm, Avenging Blade, Arondight.'
  slot_scores:
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.48
      pick: 0.1
      fit: 0.65
    Dominance:
      total: 0.49
      efficiency: 0.47
      win: 0.47
      pick: 0.5
      fit: 0.56
    The Reaper:
      total: 0.49
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.49
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.64
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.49
      win: 0.53
      pick: 0.28
      fit: 0.52
    Deathbringer:
      total: 0.48
      efficiency: 0.44
      win: 0.52
      pick: 0.41
      fit: 0.45
  community_ordered:
  - Tyrfing
  - Dominance
  - Silverbranch Bow
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Dominance
  - Hydra's Lament
  - The Reaper
  flex_slots:
  - The Reaper
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
    Revenge, Tyrfing, Hydra''s Lament, The Reaper, Heartseeker, Tekko-Kagi, The Crusher,
    Lernaean Bow, Titan''s Bane, Arondight, Golden Blade, Rage, Transcendence, Avatar''s
    Parashu, Genji''s Guard, Runeforged Hammer, Toxic Blade, Demon Blade, Bloodforge,
    Qin''s Blade, Pendulum Blade, Barbed Carver, Damaru, Shield Splitter, Eye of the
    Storm, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.49
      pick: 0.11
      fit: 0.46
    Transcendence:
      total: 0.43
      efficiency: 0.5
      win: 0.49
      pick: 0.0
      fit: 0.25
    Tyrfing:
      total: 0.48
      efficiency: 0.53
      win: 0.48
      pick: 0.1
      fit: 0.48
    Dominance:
      total: 0.48
      efficiency: 0.47
      win: 0.47
      pick: 0.5
      fit: 0.5
    Hydra's Lament:
      total: 0.48
      efficiency: 0.55
      win: 0.49
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.47
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Rage
  - Tyrfing
  - The Reaper
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Rage
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
    this god: Tyrfing, The Reaper, Tekko-Kagi, Lernaean Bow, The Crusher, Heartseeker,
    Demon Blade, Jotunn''s Revenge, Rage, Titan''s Bane, Golden Blade, Odysseus''
    Bow, Toxic Blade, Qin''s Blade, Hydra''s Lament, Avatar''s Parashu, Musashi''s
    Dual Swords, Bloodforge, Berserker''s Shield, Barbed Carver, Transcendence, Runeforged
    Hammer, Shield Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Rage:
      total: 0.45
      efficiency: 0.46
      win: 0.49
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.48
      pick: 0.1
      fit: 0.6
    The Reaper:
      total: 0.49
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.44
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.49
      win: 0.53
      pick: 0.28
      fit: 0.5
    Demon Blade:
      total: 0.46
      efficiency: 0.36
      win: 0.49
      pick: 0.0
      fit: 0.73
    Deathbringer:
      total: 0.48
      efficiency: 0.44
      win: 0.52
      pick: 0.41
      fit: 0.48
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - Silverbranch Bow
  flex_slots:
  - Hydra's Lament
  - Tekko-Kagi
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Reaper, Tyrfing, Hydra''s Lament, Tekko-Kagi, The
    Crusher, Heartseeker, Titan''s Bane, Arondight, Lernaean Bow, Toxic Blade, Avatar''s
    Parashu, Golden Blade, Pendulum Blade, Rage, Qin''s Blade, Damaru, Genji''s Guard,
    Demon Blade, Transcendence, Runeforged Hammer, Bloodforge, Barbed Carver, Berserker''s
    Shield, Shield Splitter, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.49
      pick: 0.11
      fit: 0.48
    Tyrfing:
      total: 0.48
      efficiency: 0.53
      win: 0.48
      pick: 0.1
      fit: 0.45
    Hydra's Lament:
      total: 0.47
      efficiency: 0.55
      win: 0.49
      pick: 0.0
      fit: 0.37
    The Reaper:
      total: 0.48
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.41
    Tekko-Kagi:
      total: 0.47
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.5
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.49
      win: 0.53
      pick: 0.28
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Tyrfing
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, The Reaper, Kinetic Cuirass, Shield
    of the Phoenix, Phoenix Feather, Yogi''s Necklace, Shield Splitter, Tyrfing, Golden
    Blade, Runeforged Hammer, Oni Hunter''s Garb, Draconic Scale, Genji''s Guard,
    Bloodforge, Erosion, Shogun''s Ofuda, Eye of Providence, Pharaoh''s Curse, Toxic
    Blade, Midgardian Mail, Tekko-Kagi, Shifter''s Shield, The Crusher, Leviathan''s
    Hide, Hide of the Nemean Lion, Lernaean Bow, Heartseeker.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.72
      win: 0.49
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.49
      pick: 0.0
      fit: 0.47
    Shield Splitter:
      total: 0.48
      efficiency: 0.58
      win: 0.49
      pick: 0.0
      fit: 0.35
    Tyrfing:
      total: 0.47
      efficiency: 0.53
      win: 0.48
      pick: 0.1
      fit: 0.45
    The Reaper:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.49
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - Silverbranch Bow
  - The Crusher
  - Heartseeker
  flex_slots:
  - Tyrfing
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
    for this god: The Reaper, Tekko-Kagi, The Crusher, Tyrfing, Heartseeker, Jotunn''s
    Revenge, Titan''s Bane, Toxic Blade, Avatar''s Parashu, Lernaean Bow, Avenging
    Blade, Golden Blade, Rage, Hydra''s Lament, Demon Blade, Qin''s Blade, Oath-Sworn
    Spear, Bloodforge, Transcendence, Runeforged Hammer, Barbed Carver, Pendulum Blade,
    Berserker''s Shield, Shield Splitter.'
  slot_scores:
    Tyrfing:
      total: 0.49
      efficiency: 0.53
      win: 0.48
      pick: 0.1
      fit: 0.53
    The Reaper:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.6
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.71
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.49
      win: 0.53
      pick: 0.28
      fit: 0.62
    The Crusher:
      total: 0.49
      efficiency: 0.51
      win: 0.49
      pick: 0.0
      fit: 0.61
    Heartseeker:
      total: 0.49
      efficiency: 0.45
      win: 0.49
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Dominance
  - The Reaper
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, The Reaper, Tekko-Kagi, Golden Blade, Lernaean Bow, Toxic Blade,
    The Crusher, Qin''s Blade, Heartseeker, Odysseus'' Bow, Jotunn''s Revenge, Titan''s
    Bane, Demon Blade, Rage, Hydra''s Lament, Avatar''s Parashu, Berserker''s Shield,
    Sun Beam Bow, Transcendence, Bloodforge, Runeforged Hammer, Barbed Carver, Shield
    Splitter, Musashi''s Dual Swords, Eye of the Storm.'
  slot_scores:
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.48
      pick: 0.1
      fit: 0.68
    Dominance:
      total: 0.48
      efficiency: 0.47
      win: 0.47
      pick: 0.5
      fit: 0.5
    The Reaper:
      total: 0.47
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.37
    Tekko-Kagi:
      total: 0.47
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.54
    Riptalon:
      total: 0.48
      efficiency: 0.45
      win: 0.45
      pick: 0.42
      fit: 0.66
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.49
      win: 0.53
      pick: 0.28
      fit: 0.58
  community_ordered:
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Arondight
  - The Reaper
  - Silverbranch Bow
  flex_slots:
  - Arondight
  - The Reaper
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
    Tyrfing, Arondight, The Reaper, Tekko-Kagi, The Crusher, Damaru, Genji''s Guard,
    Lernaean Bow, Heartseeker, Titan''s Bane, Pendulum Blade, Golden Blade, Toxic
    Blade, Breastplate of Valor, Qin''s Blade, Rage, Chandra''s Grace, Avatar''s Parashu,
    Demon Blade, Berserker''s Shield, Transcendence, Runeforged Hammer, Bloodforge,
    Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.49
      pick: 0.11
      fit: 0.5
    Tyrfing:
      total: 0.47
      efficiency: 0.53
      win: 0.48
      pick: 0.1
      fit: 0.41
    Hydra's Lament:
      total: 0.49
      efficiency: 0.55
      win: 0.49
      pick: 0.0
      fit: 0.48
    Arondight:
      total: 0.46
      efficiency: 0.53
      win: 0.49
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.46
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.28
    Silverbranch Bow:
      total: 0.47
      efficiency: 0.49
      win: 0.53
      pick: 0.28
      fit: 0.34
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - Riptalon
  - The Crusher
  flex_slots:
  - Riptalon
  - The Crusher
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
    Underrated for this god: Tyrfing, The Reaper, Tekko-Kagi, Lernaean Bow, The Crusher,
    Heartseeker, Titan''s Bane, Golden Blade, Jotunn''s Revenge, Demon Blade, Rage,
    Toxic Blade, Hydra''s Lament, Qin''s Blade, Avatar''s Parashu, Bloodforge, Barbed
    Carver, Transcendence, Runeforged Hammer, Berserker''s Shield, Musashi''s Dual
    Swords, Shield Splitter, Eye of the Storm, Avenging Blade, Arondight.'
  slot_scores:
    Lernaean Bow:
      total: 0.47
      efficiency: 0.47
      win: 0.49
      pick: 0.0
      fit: 0.56
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.48
      pick: 0.1
      fit: 0.65
    The Reaper:
      total: 0.49
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.49
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.64
    Riptalon:
      total: 0.47
      efficiency: 0.45
      win: 0.45
      pick: 0.42
      fit: 0.63
    The Crusher:
      total: 0.47
      efficiency: 0.51
      win: 0.49
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Tyrfing
  - Riptalon
  starter: *id001
---
