---
type: smite-build
god: Anhur
mode: Conquest
builds:
- source: community
  aspect: Aspect of Pride
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.8
    win_rate: 0.55
    alternates:
    - name: Tyrfing
      pick_rate: 0.1
      win_rate: 0.48
    - name: Avenging Blade
      pick_rate: 0.05
      win_rate: 0.4
  - name: Dagger of Frenzy
    pick_rate: 0.56
    win_rate: 0.52
    alternates:
    - name: Tyrfing
      pick_rate: 0.11
      win_rate: 0.52
    - name: Toxic Blade
      pick_rate: 0.04
      win_rate: 0.5
  - name: Dominance
    pick_rate: 0.35
    win_rate: 0.51
    alternates:
    - name: The Executioner
      pick_rate: 0.2
      win_rate: 0.6
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.38
  - name: The Executioner
    pick_rate: 0.22
    win_rate: 0.48
    alternates:
    - name: Riptalon
      pick_rate: 0.19
      win_rate: 0.61
    - name: Silverbranch Bow
      pick_rate: 0.15
      win_rate: 0.41
  - name: Riptalon
    pick_rate: 0.18
    win_rate: 0.56
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.18
      win_rate: 0.59
    - name: Deathbringer
      pick_rate: 0.14
      win_rate: 0.68
  - name: Deathbringer
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.13
      win_rate: 0.65
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 0.45
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.41
    win_rate: 0.63
  - name: Hunter's Cowl
    pick_rate: 0.19
    win_rate: 0.51
  - name: Gilded Arrow
    pick_rate: 0.16
    win_rate: 0.41
  source_url: https://smitebrain.com/gods/anhur/
  last_verified: '2026-11-06'
  god_win_rate: 0.5323383084577115
  god_matches_won: 107
  god_matches_played: 201
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  flex_slots:
  - Riptalon
  - Jotunn's Revenge
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
    this god: Jotunn''s Revenge, Lernaean Bow, The Reaper, Tekko-Kagi, Golden Blade,
    Demon Blade, Hydra''s Lament, Rage, The Crusher, Heartseeker, Qin''s Blade, Arondight,
    Titan''s Bane, Toxic Blade, Bloodforge, Musashi''s Dual Swords, Barbed Carver,
    Berserker''s Shield, Transcendence, Runeforged Hammer, Avatar''s Parashu, Shield
    Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.52
      pick: 0.15
      fit: 0.69
    Dominance:
      total: 0.51
      efficiency: 0.47
      win: 0.51
      pick: 0.55
      fit: 0.6
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.49
      win: 0.59
      pick: 0.39
      fit: 0.44
    Riptalon:
      total: 0.51
      efficiency: 0.45
      win: 0.56
      pick: 0.39
      fit: 0.55
    Deathbringer:
      total: 0.51
      efficiency: 0.44
      win: 0.58
      pick: 0.46
      fit: 0.5
  community_ordered:
  - Tyrfing
  - Dominance
  - Silverbranch Bow
  - Riptalon
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
  - Silverbranch Bow
  flex_slots:
  - Hydra's Lament
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
    Revenge, Hydra''s Lament, The Reaper, Heartseeker, Tekko-Kagi, The Crusher, Lernaean
    Bow, Titan''s Bane, Arondight, Golden Blade, Rage, Transcendence, Avatar''s Parashu,
    Demon Blade, Genji''s Guard, Qin''s Blade, Runeforged Hammer, Bloodforge, Toxic
    Blade, Barbed Carver, Pendulum Blade, Damaru, Shield Splitter, Eye of the Storm,
    Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.44
      efficiency: 0.5
      win: 0.52
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.52
      pick: 0.15
      fit: 0.49
    Dominance:
      total: 0.5
      efficiency: 0.47
      win: 0.51
      pick: 0.55
      fit: 0.5
    Hydra's Lament:
      total: 0.49
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.49
      win: 0.59
      pick: 0.39
      fit: 0.33
  community_ordered:
  - Tyrfing
  - Dominance
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Rage
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
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
    this god: Jotunn''s Revenge, The Reaper, Lernaean Bow, Tekko-Kagi, Demon Blade,
    Hydra''s Lament, Rage, Golden Blade, The Crusher, Heartseeker, Qin''s Blade, Arondight,
    Titan''s Bane, Musashi''s Dual Swords, Toxic Blade, Bloodforge, Berserker''s Shield,
    Barbed Carver, Transcendence, Runeforged Hammer, Avatar''s Parashu, Shield Splitter,
    Eye of the Storm, Avenging Blade.'
  slot_scores:
    Rage:
      total: 0.47
      efficiency: 0.46
      win: 0.52
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.52
      pick: 0.15
      fit: 0.65
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.49
      win: 0.59
      pick: 0.39
      fit: 0.42
    Riptalon:
      total: 0.51
      efficiency: 0.45
      win: 0.56
      pick: 0.39
      fit: 0.53
    Demon Blade:
      total: 0.48
      efficiency: 0.36
      win: 0.52
      pick: 0.0
      fit: 0.79
    Deathbringer:
      total: 0.52
      efficiency: 0.44
      win: 0.58
      pick: 0.46
      fit: 0.52
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    The Reaper, Genji''s Guard, Phoenix Feather, Yogi''s Necklace, Jotunn''s Revenge,
    Shield Splitter, Golden Blade, Freya''s Tears, Runeforged Hammer, Oni Hunter''s
    Garb, Breastplate of Valor, Draconic Scale, Chandra''s Grace, Shogun''s Ofuda,
    Pharaoh''s Curse, Bloodforge, Erosion, Eye of Providence, Midgardian Mail, Hydra''s
    Lament, Shifter''s Shield, Regrowth Striders, Lernaean Bow, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.52
      pick: 0.0
      fit: 0.14
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.52
      pick: 0.15
      fit: 0.47
    Riptalon:
      total: 0.52
      efficiency: 0.45
      win: 0.56
      pick: 0.39
      fit: 0.65
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Tyrfing
  - Riptalon
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Tekko-Kagi
  - Silverbranch Bow
  - Riptalon
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, The Crusher, Heartseeker,
    Titan''s Bane, Toxic Blade, Lernaean Bow, Hydra''s Lament, Avatar''s Parashu,
    Golden Blade, Rage, Pendulum Blade, Demon Blade, Arondight, Qin''s Blade, Oath-Sworn
    Spear, Transcendence, Bloodforge, Runeforged Hammer, Berserker''s Shield, Barbed
    Carver, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.52
      pick: 0.15
      fit: 0.53
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.68
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.49
      win: 0.59
      pick: 0.39
      fit: 0.6
    Riptalon:
      total: 0.53
      efficiency: 0.45
      win: 0.56
      pick: 0.39
      fit: 0.68
    The Crusher:
      total: 0.5
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Jotunn's Revenge
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
    this god: Jotunn''s Revenge, Golden Blade, Lernaean Bow, The Reaper, Tekko-Kagi,
    Qin''s Blade, Hydra''s Lament, Demon Blade, The Crusher, Toxic Blade, Rage, Heartseeker,
    Arondight, Titan''s Bane, Berserker''s Shield, Sun Beam Bow, Bloodforge, Transcendence,
    Runeforged Hammer, Barbed Carver, Musashi''s Dual Swords, Avatar''s Parashu, Shield
    Splitter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.22
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.52
      pick: 0.15
      fit: 0.7
    Dominance:
      total: 0.5
      efficiency: 0.47
      win: 0.51
      pick: 0.55
      fit: 0.52
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.49
      win: 0.59
      pick: 0.39
      fit: 0.5
    Riptalon:
      total: 0.52
      efficiency: 0.45
      win: 0.56
      pick: 0.39
      fit: 0.59
    Deathbringer:
      total: 0.5
      efficiency: 0.44
      win: 0.58
      pick: 0.46
      fit: 0.38
  community_ordered:
  - Tyrfing
  - Dominance
  - Silverbranch Bow
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Arondight
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Riptalon
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
    Arondight, The Reaper, Lernaean Bow, Damaru, Genji''s Guard, Tekko-Kagi, The Crusher,
    Golden Blade, Heartseeker, Qin''s Blade, Rage, Breastplate of Valor, Pendulum
    Blade, Chandra''s Grace, Titan''s Bane, Demon Blade, Berserker''s Shield, Toxic
    Blade, Transcendence, Runeforged Hammer, Bloodforge, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.52
      pick: 0.15
      fit: 0.45
    Hydra's Lament:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.5
    Arondight:
      total: 0.48
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.4
    Riptalon:
      total: 0.48
      efficiency: 0.45
      win: 0.56
      pick: 0.39
      fit: 0.38
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.49
      win: 0.59
      pick: 0.39
      fit: 0.3
  community_ordered:
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - The Reaper
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Lernaean Bow, The Reaper, Tekko-Kagi,
    Golden Blade, Demon Blade, Hydra''s Lament, Rage, The Crusher, Heartseeker, Qin''s
    Blade, Arondight, Titan''s Bane, Toxic Blade, Bloodforge, Musashi''s Dual Swords,
    Barbed Carver, Berserker''s Shield, Transcendence, Runeforged Hammer, Avatar''s
    Parashu, Shield Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.47
      win: 0.52
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.52
      pick: 0.15
      fit: 0.69
    Dominance:
      total: 0.51
      efficiency: 0.47
      win: 0.51
      pick: 0.55
      fit: 0.6
    The Reaper:
      total: 0.49
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.37
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Dominance
  starter: *id001
---
