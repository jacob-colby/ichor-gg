---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.49
  slot_order:
  - name: Golden Blade
    pick_rate: 0.24
    win_rate: 0.63
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.23
      win_rate: 0.51
    - name: Devourer's Gauntlet
      pick_rate: 0.1
      win_rate: 0.32
  - name: Berserker's Shield
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Golden Blade
      pick_rate: 0.19
      win_rate: 0.47
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.24
    win_rate: 0.53
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.38
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.39
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.12
      win_rate: 0.63
    - name: Contagion
      pick_rate: 0.06
      win_rate: 0.38
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.7
    - name: Hussar's Wings
      pick_rate: 0.05
      win_rate: 0.45
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.64
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.22
    - name: Hussar's Wings
      pick_rate: 0.06
      win_rate: 0.63
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.39
    win_rate: 0.57
  - name: Death's Toll
    pick_rate: 0.22
    win_rate: 0.4
  - name: Sundering Axe
    pick_rate: 0.1
    win_rate: 0.8
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-11-04'
  god_win_rate: 0.5083333333333333
  god_matches_won: 122
  god_matches_played: 240
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
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
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Tyrfing, Genji''s Guard, Shield Splitter,
    Runeforged Hammer, The Reaper, Hydra''s Lament, Oni Hunter''s Garb, Breastplate
    of Valor, Shield of the Phoenix, Lernaean Bow, Dominance, Tekko-Kagi, Draconic
    Scale, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, The Crusher, Midgardian
    Mail, Erosion, Toxic Blade, Eye of Providence, Heartseeker, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.51
      win: 0.63
      pick: 0.24
      fit: 0.58
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.3
      fit: 0.41
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.37
      fit: 0.42
    Tyrfing:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, The Reaper, Genji''s Guard, Shield
    Splitter, Phoenix Feather, Jotunn''s Revenge, Yogi''s Necklace, Tyrfing, Runeforged
    Hammer, Riptalon, Oni Hunter''s Garb, Draconic Scale, Breastplate of Valor, Bloodforge,
    Chandra''s Grace, Erosion, Eye of Providence, Hydra''s Lament, Midgardian Mail,
    Shogun''s Ofuda, Pharaoh''s Curse, Leviathan''s Hide, Regrowth Striders, Lernaean
    Bow.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.51
      win: 0.63
      pick: 0.24
      fit: 0.54
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.3
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.37
      fit: 0.5
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, The Reaper, Avenging Blade, Genji''s
    Guard, Screeching Gargoyle, The Crusher, Tekko-Kagi, Stone of Binding, Tyrfing,
    Heartseeker, Void Stone, Void Shield, Toxic Blade, Titan''s Bane, Runeforged Hammer,
    Shield Splitter, Silverbranch Bow, Breastplate of Valor, Riptalon, Hydra''s Lament,
    Oni Hunter''s Garb, Shield of the Phoenix, Lernaean Bow, Dominance, Avatar''s
    Parashu.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.51
      win: 0.63
      pick: 0.24
      fit: 0.45
    Avenging Blade:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.3
      fit: 0.31
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.37
      fit: 0.34
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Genji's Guard
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Tyrfing, Genji''s Guard, Jotunn''s Revenge, Shield Splitter,
    Runeforged Hammer, Toxic Blade, Breastplate of Valor, Oni Hunter''s Garb, The
    Reaper, Shogun''s Ofuda, Shield of the Phoenix, Pharaoh''s Curse, Lernaean Bow,
    Dominance, Silverbranch Bow, Hydra''s Lament, Riptalon, Tekko-Kagi, Draconic Scale,
    Midgardian Mail, Qin''s Blade, Erosion, Leviathan''s Hide, Eye of Providence.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.51
      win: 0.63
      pick: 0.24
      fit: 0.6
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.1
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.3
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.37
      fit: 0.36
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Jotunn's Revenge
  flex_slots:
  - Jotunn's Revenge
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Amanita Charm, Breastplate of Valor, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Tyrfing, Arondight, Runeforged Hammer, Shield Splitter, Oni Hunter''s
    Garb, Gladiator''s Shield, The Reaper, Chandra''s Grace, Draconic Scale, Midgardian
    Mail, Eye of Erebus, Damaru, Shogun''s Ofuda, Prophetic Cloak, Pharaoh''s Curse,
    Leviathan''s Hide, Eye of Providence, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.51
      win: 0.63
      pick: 0.24
      fit: 0.37
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.3
      fit: 0.3
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.37
      fit: 0.34
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Tyrfing, Genji''s Guard,
    Shield Splitter, Runeforged Hammer, The Reaper, Hydra''s Lament, Oni Hunter''s
    Garb, Breastplate of Valor, Shield of the Phoenix, Lernaean Bow, Dominance, Tekko-Kagi,
    Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, The Crusher,
    Midgardian Mail, Erosion, Toxic Blade, Eye of Providence, Heartseeker, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.12
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.3
      fit: 0.41
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.37
      fit: 0.42
    Tyrfing:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Jotunn''s Revenge,
    Tyrfing, Genji''s Guard, Shield Splitter, Runeforged Hammer, The Reaper, Hydra''s
    Lament, Oni Hunter''s Garb, Breastplate of Valor, Shield of the Phoenix, Lernaean
    Bow, Dominance, Tekko-Kagi, Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse,
    Avenging Blade, The Crusher, Midgardian Mail, Erosion, Toxic Blade, Eye of Providence,
    Heartseeker, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.51
      win: 0.63
      pick: 0.24
      fit: 0.58
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.3
      fit: 0.41
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.37
      fit: 0.42
    Tyrfing:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  swaps:
  - added: Golden Blade
    removed: Genji's Guard
    reason: community 63% win over 58 matches (vs 51% on this god), taking the model's
      weakest slot from Genji's Guard
  starter: *id001
---
