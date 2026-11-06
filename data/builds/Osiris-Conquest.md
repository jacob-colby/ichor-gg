---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.26
  aspect_win_rate: 0.33
  slot_order:
  - name: Golden Blade
    pick_rate: 0.26
    win_rate: 0.25
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.21
      win_rate: 0.5
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.33
  - name: Berserker's Shield
    pick_rate: 0.13
    win_rate: 0.33
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.33
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.4
  - name: Kinetic Cuirass
    pick_rate: 0.11
    win_rate: 0.2
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.25
    - name: Contagion
      pick_rate: 0.07
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.6
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.17
      win_rate: 0.38
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.25
  - name: Hussar's Wings
    pick_rate: 0.1
    win_rate: 0.25
    alternates:
    - name: Veve Charm
      pick_rate: 0.08
      win_rate: 0.0
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.0
  - name: Olmec Blue
    pick_rate: 0.12
    win_rate: 0.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
    - name: Shield
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.23
    win_rate: 0.64
  - name: Death's Toll
    pick_rate: 0.23
    win_rate: 0.18
  - name: Sundering Axe
    pick_rate: 0.19
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-11-06'
  god_win_rate: 0.3404255319148936
  god_matches_won: 16
  god_matches_played: 47
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Tyrfing, Genji''s Guard, Shield Splitter,
    Runeforged Hammer, The Reaper, Hydra''s Lament, Oni Hunter''s Garb, Breastplate
    of Valor, Shield of the Phoenix, Lernaean Bow, Dominance, Tekko-Kagi, Draconic
    Scale, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, The Crusher, Midgardian
    Mail, Erosion, Toxic Blade, Eye of Providence, Heartseeker, Leviathan''s Hide.'
  slot_scores:
    Contagion:
      total: 0.48
      efficiency: 0.4
      win: 0.67
      pick: 0.11
      fit: 0.24
    Berserker's Shield:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.18
      fit: 0.41
    Jotunn's Revenge:
      total: 0.42
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.27
    Shifter's Shield:
      total: 0.46
      efficiency: 0.5
      win: 0.5
      pick: 0.21
      fit: 0.32
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.6
      pick: 0.18
      fit: 0.21
    Amanita Charm:
      total: 0.43
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Contagion
  - Berserker's Shield
  - Shifter's Shield
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Contagion
  - Berserker's Shield
  - Shield of the Phoenix
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
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
    Contagion:
      total: 0.49
      efficiency: 0.4
      win: 0.67
      pick: 0.11
      fit: 0.25
    Berserker's Shield:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.18
      fit: 0.43
    Shield of the Phoenix:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.0
      fit: 0.61
    Shifter's Shield:
      total: 0.47
      efficiency: 0.5
      win: 0.5
      pick: 0.21
      fit: 0.4
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.6
      pick: 0.18
      fit: 0.28
    Amanita Charm:
      total: 0.49
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Contagion
  - Berserker's Shield
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    Contagion:
      total: 0.48
      efficiency: 0.4
      win: 0.67
      pick: 0.11
      fit: 0.21
    Berserker's Shield:
      total: 0.46
      efficiency: 0.72
      win: 0.33
      pick: 0.18
      fit: 0.31
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.45
    Shifter's Shield:
      total: 0.45
      efficiency: 0.5
      win: 0.5
      pick: 0.21
      fit: 0.24
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.6
      pick: 0.18
      fit: 0.16
    Amanita Charm:
      total: 0.42
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Contagion
  - Berserker's Shield
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Shifter's Shield
  - Freya's Tears
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Tyrfing, Genji''s Guard, Jotunn''s Revenge, Shield Splitter,
    Runeforged Hammer, Toxic Blade, Breastplate of Valor, Oni Hunter''s Garb, The
    Reaper, Shogun''s Ofuda, Shield of the Phoenix, Pharaoh''s Curse, Lernaean Bow,
    Dominance, Silverbranch Bow, Hydra''s Lament, Riptalon, Tekko-Kagi, Draconic Scale,
    Midgardian Mail, Qin''s Blade, Erosion, Leviathan''s Hide, Eye of Providence,
    Hide of the Nemean Lion.'
  slot_scores:
    Contagion:
      total: 0.48
      efficiency: 0.4
      win: 0.67
      pick: 0.11
      fit: 0.22
    Golden Blade:
      total: 0.39
      efficiency: 0.51
      win: 0.25
      pick: 0.26
      fit: 0.6
    Berserker's Shield:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.18
      fit: 0.41
    Tyrfing:
      total: 0.42
      efficiency: 0.53
      win: 0.33
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.45
      efficiency: 0.5
      win: 0.5
      pick: 0.21
      fit: 0.26
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.6
      pick: 0.18
      fit: 0.17
  community_ordered:
  - Contagion
  - Golden Blade
  - Berserker's Shield
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Amanita Charm, Breastplate of Valor, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Tyrfing, Arondight, Runeforged Hammer, Shield Splitter, Oni Hunter''s
    Garb, Gladiator''s Shield, The Reaper, Chandra''s Grace, Draconic Scale, Midgardian
    Mail, Eye of Erebus, Damaru, Shogun''s Ofuda, Pharaoh''s Curse, Leviathan''s Hide,
    Eye of Providence, Erosion, Hide of the Nemean Lion.'
  slot_scores:
    Contagion:
      total: 0.48
      efficiency: 0.4
      win: 0.67
      pick: 0.11
      fit: 0.21
    Genji's Guard:
      total: 0.45
      efficiency: 0.71
      win: 0.33
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.46
      efficiency: 0.72
      win: 0.33
      pick: 0.18
      fit: 0.3
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.38
    Shifter's Shield:
      total: 0.45
      efficiency: 0.5
      win: 0.5
      pick: 0.21
      fit: 0.24
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.18
      fit: 0.4
  community_ordered:
  - Contagion
  - Berserker's Shield
  - Shifter's Shield
  - Freya's Tears
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
      total: 0.42
      efficiency: 0.71
      win: 0.33
      pick: 0.0
      fit: 0.12
    Berserker's Shield:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.18
      fit: 0.41
    Jotunn's Revenge:
      total: 0.42
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.37
      efficiency: 0.61
      win: 0.2
      pick: 0.17
      fit: 0.42
    Tyrfing:
      total: 0.42
      efficiency: 0.53
      win: 0.33
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.43
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
