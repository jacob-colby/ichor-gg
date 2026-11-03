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
  last_verified: '2026-11-03'
  god_win_rate: 0.5083333333333333
  god_matches_won: 122
  god_matches_played: 240
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield Splitter, Runeforged Hammer,
    Tekko-Kagi, Tyrfing, Genji''s Guard, Lernaean Bow, Hydra''s Lament, Avenging Blade,
    Titan''s Bane, Pharaoh''s Curse, Breastplate of Valor, Dominance, Oni Hunter''s
    Garb, Toxic Blade, Shogun''s Ofuda, Midgardian Mail, Erosion, Eye of Providence,
    Silverbranch Bow, The Crusher, Arondight, Wyrmskin Hide, Draconic Scale, Leviathan''s
    Hide.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.63
      pick: 0.24
      fit: 0.64
    Berserker's Shield:
      total: 0.57
      efficiency: 0.74
      win: 0.5
      pick: 0.3
      fit: 0.45
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.37
      fit: 0.45
    Shield Splitter:
      total: 0.49
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Shield Splitter, Jotunn''s Revenge,
    Runeforged Hammer, Genji''s Guard, Yogi''s Necklace, Phoenix Feather, The Reaper,
    Tekko-Kagi, Tyrfing, Pharaoh''s Curse, Lernaean Bow, Oni Hunter''s Garb, Breastplate
    of Valor, Erosion, Hydra''s Lament, Eye of Providence, Avenging Blade, Shogun''s
    Ofuda, Draconic Scale, Titan''s Bane, Midgardian Mail, Chandra''s Grace, Toxic
    Blade, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.63
      pick: 0.24
      fit: 0.59
    Berserker's Shield:
      total: 0.57
      efficiency: 0.74
      win: 0.5
      pick: 0.3
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.53
      pick: 0.37
      fit: 0.54
    Shield Splitter:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.46
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.74
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
  - Tekko-Kagi
  flex_slots:
  - Kinetic Cuirass
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    for this god: Jotunn''s Revenge, Tekko-Kagi, Avenging Blade, Titan''s Bane, Amanita
    Charm, Toxic Blade, Stone of Binding, The Crusher, Genji''s Guard, Screeching
    Gargoyle, Silverbranch Bow, Runeforged Hammer, Shield Splitter, Heartseeker, Void
    Stone, Void Shield, The Reaper, Tyrfing, Lernaean Bow, Hydra''s Lament, Breastplate
    of Valor, Oni Hunter''s Garb, Pharaoh''s Curse, Dominance, Avatar''s Parashu,
    Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.24
      fit: 0.48
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.3
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.37
      fit: 0.36
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: attack-speed
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Tyrfing, Genji''s Guard, Tekko-Kagi,
    Runeforged Hammer, Shield Splitter, Toxic Blade, Lernaean Bow, Silverbranch Bow,
    Pharaoh''s Curse, Breastplate of Valor, Shogun''s Ofuda, Riptalon, Hydra''s Lament,
    The Reaper, Oni Hunter''s Garb, Dominance, Titan''s Bane, Avenging Blade, Midgardian
    Mail, Qin''s Blade, Erosion, Leviathan''s Hide, Eye of Providence, Shield of the
    Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.63
      pick: 0.24
      fit: 0.6
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.5
      pick: 0.3
      fit: 0.41
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.18
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.37
      fit: 0.36
    Tyrfing:
      total: 0.49
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
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
    Gargoyle, Arondight, Runeforged Hammer, Shield Splitter, Tekko-Kagi, Tyrfing,
    Oni Hunter''s Garb, Lernaean Bow, Pharaoh''s Curse, Chandra''s Grace, Eye of Erebus,
    Titan''s Bane, Midgardian Mail, Gladiator''s Shield, Shogun''s Ofuda, Toxic Blade,
    Prophetic Cloak, Avenging Blade, Erosion, Silverbranch Bow.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.63
      pick: 0.24
      fit: 0.39
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.3
      fit: 0.33
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.37
      fit: 0.36
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Shield Splitter, Runeforged
    Hammer, Tekko-Kagi, Tyrfing, Genji''s Guard, Lernaean Bow, Hydra''s Lament, Avenging
    Blade, Titan''s Bane, Pharaoh''s Curse, Breastplate of Valor, Dominance, Oni Hunter''s
    Garb, Toxic Blade, Shogun''s Ofuda, Midgardian Mail, Erosion, Eye of Providence,
    Silverbranch Bow, The Crusher, Arondight, Wyrmskin Hide, Draconic Scale, Leviathan''s
    Hide.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.63
      pick: 0.24
      fit: 0.64
    Berserker's Shield:
      total: 0.57
      efficiency: 0.74
      win: 0.5
      pick: 0.3
      fit: 0.45
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.3
    Shield Splitter:
      total: 0.49
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.41
    Runeforged Hammer:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  starter: *id001
---
