---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.43
  slot_order:
  - name: Berserker's Shield
    pick_rate: 0.28
    win_rate: 0.53
    alternates:
    - name: Golden Blade
      pick_rate: 0.22
      win_rate: 0.7
    - name: Devourer's Gauntlet
      pick_rate: 0.1
      win_rate: 0.25
  - name: Golden Blade
    pick_rate: 0.25
    win_rate: 0.49
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.21
      win_rate: 0.44
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.54
  - name: Kinetic Cuirass
    pick_rate: 0.26
    win_rate: 0.54
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.4
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.41
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.12
      win_rate: 0.65
    - name: Contagion
      pick_rate: 0.08
      win_rate: 0.45
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 0.67
    - name: Hussar's Wings
      pick_rate: 0.06
      win_rate: 0.63
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.57
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.67
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.42
    win_rate: 0.58
  - name: Death's Toll
    pick_rate: 0.23
    win_rate: 0.37
  - name: Sundering Axe
    pick_rate: 0.09
    win_rate: 0.93
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-10-29'
  god_win_rate: 0.5163398692810458
  god_matches_won: 79
  god_matches_played: 153
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-29'
  god_matches_analyzed: 9506
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Lernaean Bow, Tyrfing,
    Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor, Pharaoh''s
    Curse, Avenging Blade, Hydra''s Lament, Shogun''s Ofuda, Tekko-Kagi, Heartseeker,
    Dominance, Deathbringer, Toxic Blade, Erosion, Silverbranch Bow, Daybreak Gavel,
    Eye of Providence, Shield of the Phoenix, Midgardian Mail, Shifter''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.49
      pick: 0.34
      fit: 0.64
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.28
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.4
      fit: 0.45
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.35
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Runeforged
    Hammer, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor,
    The Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean Bow, Tyrfing, Riptalon,
    Erosion, Shogun''s Ofuda, Phoenix Feather, Eye of Providence, Avenging Blade,
    Hydra''s Lament, Chandra''s Grace, Stone of Binding, Daybreak Gavel, Midgardian
    Mail, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.28
      fit: 0.47
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.4
      fit: 0.54
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.63
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Amanita Charm, Heartseeker, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Runeforged Hammer, Screeching Gargoyle, Void
    Shield, Toxic Blade, Titan''s Bane, Void Stone, The Crusher, Genji''s Guard, Breastplate
    of Valor, Lernaean Bow, The Reaper, Tyrfing, Shield Splitter, Hydra''s Lament,
    Riptalon, Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu, Shifter''s Shield.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.28
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.54
      pick: 0.4
      fit: 0.36
    Draconic Scale:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.26
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Draconic Scale
  flex_slots:
  - Jotunn's Revenge
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Tyrfing, Riptalon, Runeforged Hammer,
    Lernaean Bow, Genji''s Guard, Silverbranch Bow, Breastplate of Valor, Pharaoh''s
    Curse, Toxic Blade, Shogun''s Ofuda, Shield Splitter, Eye of the Storm, Hydra''s
    Lament, Tekko-Kagi, The Reaper, Daybreak Gavel, Avenging Blade, Dominance, Erosion,
    Shield of the Phoenix, Eye of Providence, Heartseeker, Vital Amplifier, Shifter''s
    Shield.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.49
      pick: 0.34
      fit: 0.6
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.28
      fit: 0.41
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.18
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.54
      pick: 0.4
      fit: 0.36
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.52
      pick: 0.0
      fit: 0.58
    Draconic Scale:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.26
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Jotunn's Revenge
  - Draconic Scale
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Screeching
    Gargoyle, Runeforged Hammer, Prophetic Cloak, Arondight, Lernaean Bow, Pharaoh''s
    Curse, Tyrfing, Shield Splitter, Daybreak Gavel, Eye of Erebus, Gladiator''s Shield,
    Shogun''s Ofuda, Eye of the Storm, Chandra''s Grace, Silverbranch Bow, Erosion,
    Avenging Blade, Eye of Providence, Stone of Binding, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.28
      fit: 0.33
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.54
      pick: 0.4
      fit: 0.36
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.4
    Draconic Scale:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.26
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Draconic Scale
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer,
    Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate
    of Valor, Pharaoh''s Curse, Shifter''s Shield, Avenging Blade, Hydra''s Lament,
    Shogun''s Ofuda, Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic Blade,
    Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield of the Phoenix,
    Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.49
      pick: 0.34
      fit: 0.64
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.28
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.4
      fit: 0.45
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
