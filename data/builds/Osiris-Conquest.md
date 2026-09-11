---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.63
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.29
    win_rate: 0.4
    alternates:
    - name: Lifebinder
      pick_rate: 0.2
      win_rate: 0.71
    - name: Golden Blade
      pick_rate: 0.09
      win_rate: 0.33
  - name: The World Stone
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.43
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.25
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.67
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.15
      win_rate: 0.6
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.33
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.19
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.0
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Oracle Staff
      pick_rate: 0.08
      win_rate: 1.0
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 1.0
  - name: Manchu Bow
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Contagion
      pick_rate: 0.06
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.0
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.37
    win_rate: 0.46
  - name: Sundering Axe
    pick_rate: 0.2
    win_rate: 0.57
  - name: Death's Embrace
    pick_rate: 0.11
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-09-11'
  god_win_rate: 0.4857142857142857
  god_matches_won: 17
  god_matches_played: 35
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Lernaean Bow, Tyrfing,
    Shield Splitter, Eye of the Storm, Pharaoh''s Curse, Avenging Blade, Hydra''s
    Lament, Shogun''s Ofuda, Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic
    Blade, Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield of
    the Phoenix, Draconic Scale, Midgardian Mail, Golden Blade, Kinetic Cuirass.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.18
      fit: 0.26
    Breastplate of Valor:
      total: 0.71
      efficiency: 0.65
      win: 1.0
      pick: 0.17
      fit: 0.13
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.28
      fit: 0.23
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.19
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Shell of Rebuke
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Contagion
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Runeforged
    Hammer, Shield Splitter, Eye of the Storm, The Reaper, Yogi''s Necklace, Pharaoh''s
    Curse, Lernaean Bow, Tyrfing, Riptalon, Erosion, Shogun''s Ofuda, Phoenix Feather,
    Eye of Providence, Avenging Blade, Draconic Scale, Hydra''s Lament, Chandra''s
    Grace, Stone of Binding, Daybreak Gavel, Midgardian Mail, Kinetic Cuirass, Golden
    Blade.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.18
      fit: 0.27
    Breastplate of Valor:
      total: 0.71
      efficiency: 0.65
      win: 1.0
      pick: 0.17
      fit: 0.16
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.26
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.28
      fit: 0.3
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.27
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Avenging Blade
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shell of Rebuke
  flex_slots:
  - Avenging Blade
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Amanita Charm, Heartseeker, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Runeforged Hammer, Screeching Gargoyle, Void
    Shield, Toxic Blade, Titan''s Bane, Void Stone, The Crusher, Lernaean Bow, The
    Reaper, Tyrfing, Shield Splitter, Hydra''s Lament, Riptalon, Eye of the Storm,
    Pharaoh''s Curse, Avatar''s Parashu, Kinetic Cuirass, Golden Blade.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.18
      fit: 0.22
    Avenging Blade:
      total: 0.56
      efficiency: 0.49
      win: 0.64
      pick: 0.0
      fit: 0.68
    Breastplate of Valor:
      total: 0.7
      efficiency: 0.65
      win: 1.0
      pick: 0.17
      fit: 0.1
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.28
      fit: 0.17
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.14
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Lernaean Bow
  - Breastplate of Valor
  - Tyrfing
  - Shell of Rebuke
  - Riptalon
  flex_slots:
  - Riptalon
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Tyrfing, Riptalon, Runeforged Hammer,
    Lernaean Bow, Silverbranch Bow, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda,
    Shield Splitter, Eye of the Storm, Hydra''s Lament, Tekko-Kagi, The Reaper, Daybreak
    Gavel, Avenging Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence,
    Heartseeker, Vital Amplifier, Golden Blade, Kinetic Cuirass.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.18
      fit: 0.22
    Lernaean Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.7
      efficiency: 0.65
      win: 1.0
      pick: 0.17
      fit: 0.1
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.64
      pick: 0.0
      fit: 0.58
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.15
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.64
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Shell of Rebuke
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Hydra''s Lament, Shield of the Phoenix, Screeching Gargoyle, Runeforged Hammer,
    Arondight, Lernaean Bow, Pharaoh''s Curse, Tyrfing, Shield Splitter, Daybreak
    Gavel, Eye of Erebus, Shogun''s Ofuda, Eye of the Storm, Prophetic Cloak, Chandra''s
    Grace, Silverbranch Bow, Erosion, Avenging Blade, Eye of Providence, Stone of
    Binding, Kinetic Cuirass, Golden Blade.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.18
      fit: 0.21
    Breastplate of Valor:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.17
      fit: 0.36
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.28
      fit: 0.43
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.14
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm,
    Pharaoh''s Curse, Avenging Blade, Hydra''s Lament, Shogun''s Ofuda, Tekko-Kagi,
    Heartseeker, Dominance, Deathbringer, Toxic Blade, Erosion, Silverbranch Bow,
    Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Draconic Scale, Midgardian
    Mail.'
  slot_scores:
    Golden Blade:
      total: 0.43
      efficiency: 0.52
      win: 0.33
      pick: 0.09
      fit: 0.64
    Berserker's Shield:
      total: 0.43
      efficiency: 0.68
      win: 0.25
      pick: 0.15
      fit: 0.45
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.56
      win: 0.33
      pick: 0.14
      fit: 0.45
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
