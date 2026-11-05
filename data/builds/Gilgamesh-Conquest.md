---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.61
  aspect_win_rate: 0.58
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.28
    win_rate: 0.6
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.21
      win_rate: 0.65
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.6
  - name: Barbed Carver
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.14
      win_rate: 0.61
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.56
  - name: The Reaper
    pick_rate: 0.13
    win_rate: 0.58
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.62
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.24
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.71
    - name: The Crusher
      pick_rate: 0.06
      win_rate: 0.62
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.76
    - name: The Crusher
      pick_rate: 0.06
      win_rate: 0.67
  - name: Medal of Defense
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Axe
      pick_rate: 0.06
      win_rate: 0.36
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.45
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.28
    win_rate: 0.67
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.62
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-11-04'
  god_win_rate: 0.5906040268456376
  god_matches_won: 264
  god_matches_played: 447
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Crusher, Kinetic Cuirass, Genji''s Guard, Tyrfing,
    Golden Blade, Shield Splitter, Runeforged Hammer, Freya''s Tears, Tekko-Kagi,
    Hydra''s Lament, Oni Hunter''s Garb, Breastplate of Valor, Toxic Blade, Shield
    of the Phoenix, Lernaean Bow, Dominance, Draconic Scale, Titan''s Bane, Avenging
    Blade, Shogun''s Ofuda, Pharaoh''s Curse, Midgardian Mail, Silverbranch Bow, Erosion,
    Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.6
      pick: 0.0
      fit: 0.11
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.19
      fit: 0.37
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.28
      fit: 0.34
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.39
    The Crusher:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.13
      fit: 0.41
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, The Crusher, Amanita Charm, Kinetic Cuirass, Hydra''s Lament, Breastplate
    of Valor, Tyrfing, Freya''s Tears, Runeforged Hammer, Shield Splitter, Golden
    Blade, Oni Hunter''s Garb, Shield of the Phoenix, Dominance, Tekko-Kagi, Lernaean
    Bow, Titan''s Bane, Screeching Gargoyle, Arondight, Yogi''s Necklace, Avenging
    Blade, Draconic Scale, Midgardian Mail, Eye of Providence, Toxic Blade, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.6
      pick: 0.0
      fit: 0.19
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.19
      fit: 0.25
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.28
      fit: 0.39
    Transcendence:
      total: 0.48
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.21
    The Crusher:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.13
      fit: 0.35
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.2
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, The Crusher,
    Genji''s Guard, Phoenix Feather, Yogi''s Necklace, Shield Splitter, Riptalon,
    Tyrfing, Freya''s Tears, Golden Blade, Runeforged Hammer, Oni Hunter''s Garb,
    Breastplate of Valor, Draconic Scale, Bloodforge, Chandra''s Grace, Shifter''s
    Shield, Hydra''s Lament, Erosion, Tekko-Kagi, Eye of Providence, Midgardian Mail,
    Toxic Blade, Shogun''s Ofuda, Pharaoh''s Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.72
      win: 0.61
      pick: 0.19
      fit: 0.4
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.28
      fit: 0.3
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.47
    The Reaper:
      total: 0.57
      efficiency: 0.57
      win: 0.58
      pick: 0.2
      fit: 0.65
    The Crusher:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.13
      fit: 0.37
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
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
    for this god: The Crusher, Amanita Charm, Kinetic Cuirass, Avenging Blade, Genji''s
    Guard, Screeching Gargoyle, Tekko-Kagi, Tyrfing, Stone of Binding, Void Stone,
    Void Shield, Toxic Blade, Titan''s Bane, Runeforged Hammer, Shield Splitter, Golden
    Blade, Freya''s Tears, Silverbranch Bow, Riptalon, Breastplate of Valor, Hydra''s
    Lament, Oni Hunter''s Garb, Shield of the Phoenix, Lernaean Bow, Dominance, Avatar''s
    Parashu.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.19
      fit: 0.31
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.6
      pick: 0.28
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.34
    The Crusher:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.13
      fit: 0.52
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.61
      pick: 0.4
      fit: 0.62
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
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
  - Kinetic Cuirass
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Tyrfing, Kinetic Cuirass, The Crusher, Genji''s Guard,
    Golden Blade, Toxic Blade, Freya''s Tears, Shield Splitter, Runeforged Hammer,
    Silverbranch Bow, Breastplate of Valor, Tekko-Kagi, Oni Hunter''s Garb, Riptalon,
    Shield of the Phoenix, Lernaean Bow, Shogun''s Ofuda, Dominance, Hydra''s Lament,
    Pharaoh''s Curse, Draconic Scale, Midgardian Mail, Qin''s Blade, Leviathan''s
    Hide, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.19
      fit: 0.38
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.28
      fit: 0.24
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.34
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Breastplate of Valor
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Freya''s Tears, Amanita
    Charm, Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix, The Crusher,
    Hydra''s Lament, Screeching Gargoyle, Tyrfing, Arondight, Runeforged Hammer, Shield
    Splitter, Oni Hunter''s Garb, Golden Blade, Gladiator''s Shield, Chandra''s Grace,
    Draconic Scale, Midgardian Mail, Toxic Blade, Eye of Providence, Tekko-Kagi, Eye
    of Erebus, Damaru, Leviathan''s Hide, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.0
      fit: 0.31
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.19
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.6
      pick: 0.28
      fit: 0.42
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.31
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.13
      fit: 0.37
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.22
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
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
  - Genji's Guard
  - Tyrfing
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Genji''s Guard, Tyrfing,
    Golden Blade, Shield Splitter, Runeforged Hammer, Tekko-Kagi, Freya''s Tears,
    The Crusher, Hydra''s Lament, Oni Hunter''s Garb, Breastplate of Valor, Toxic
    Blade, Shield of the Phoenix, Lernaean Bow, Dominance, Draconic Scale, Titan''s
    Bane, Avenging Blade, Shogun''s Ofuda, Pharaoh''s Curse, Midgardian Mail, Silverbranch
    Bow, Erosion, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.6
      pick: 0.0
      fit: 0.11
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.19
      fit: 0.37
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.28
      fit: 0.34
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  starter: *id001
---
