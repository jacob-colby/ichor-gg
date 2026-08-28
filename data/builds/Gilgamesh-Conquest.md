---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.59
  aspect_win_rate: 0.53
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.27
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.48
    - name: Golden Blade
      pick_rate: 0.12
      win_rate: 0.56
  - name: Berserker's Shield
    pick_rate: 0.18
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.37
    - name: Barbed Carver
      pick_rate: 0.14
      win_rate: 0.61
  - name: Shogun's Ofuda
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.13
      win_rate: 0.5
    - name: Barbed Carver
      pick_rate: 0.09
      win_rate: 0.33
  - name: Heartseeker
    pick_rate: 0.09
    win_rate: 0.64
    alternates:
    - name: The Reaper
      pick_rate: 0.08
      win_rate: 0.4
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.44
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.7
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.69
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.63
  - name: Mote of Chaos
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Medal of Disruption
      pick_rate: 0.05
      win_rate: 0.33
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.25
    win_rate: 0.73
  - name: Hunter's Cowl
    pick_rate: 0.14
    win_rate: 0.56
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.29
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-08-28'
  god_win_rate: 0.549618320610687
  god_matches_won: 72
  god_matches_played: 131
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-28'
  god_matches_analyzed: 3498
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shogun''s Ofuda, Golden Blade, Amanita Charm, Runeforged Hammer, Tyrfing,
    Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate of Valor,
    Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s Lament, Pharaoh''s Curse,
    Avenging Blade, Titan''s Bane, The Crusher, Daybreak Gavel, Deathbringer, Dominance,
    Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.25
      fit: 0.4
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.27
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.42
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.7
      pick: 0.19
      fit: 0.21
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.64
      pick: 0.15
      fit: 0.54
    Shogun's Ofuda:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.14
      fit: 0.4
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Shogun''s
    Ofuda, Golden Blade, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Hydra''s Lament, Lernaean Bow, Tyrfing, Shield Splitter, Tekko-Kagi, Eye
    of the Storm, Avenging Blade, Silverbranch Bow, Dominance, Daybreak Gavel, Shield
    of the Phoenix, Titan''s Bane, Pharaoh''s Curse, The Crusher, Toxic Blade, Transcendence,
    Deathbringer, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.25
      fit: 0.27
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.27
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.31
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.7
      pick: 0.19
      fit: 0.2
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.64
      pick: 0.15
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Berserker's Shield
  - Shogun's Ofuda
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
    this god: Amanita Charm, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix,
    Runeforged Hammer, Riptalon, Shield Splitter, Genji''s Guard, Breastplate of Valor,
    Yogi''s Necklace, Eye of the Storm, Lernaean Bow, Tyrfing, Pharaoh''s Curse, Phoenix
    Feather, Erosion, Tekko-Kagi, Toxic Blade, Eye of Providence, Avenging Blade,
    Silverbranch Bow, Hydra''s Lament, Draconic Scale, The Reaper.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.52
      pick: 0.25
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.27
      fit: 0.32
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.5
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.7
      pick: 0.19
      fit: 0.27
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.7
    Shogun's Ofuda:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.14
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  - Shogun's Ofuda
  flex_slots:
  - Berserker's Shield
  - Shogun's Ofuda
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
    for this god: Avenging Blade, Golden Blade, Amanita Charm, Tekko-Kagi, Stone of
    Binding, Silverbranch Bow, Toxic Blade, Runeforged Hammer, Screeching Gargoyle,
    Void Shield, Titan''s Bane, Void Stone, The Crusher, Genji''s Guard, Breastplate
    of Valor, Lernaean Bow, Tyrfing, Shield Splitter, Riptalon, Hydra''s Lament, Eye
    of the Storm, Pharaoh''s Curse, Avatar''s Parashu, The Reaper.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.25
      fit: 0.33
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.54
      pick: 0.27
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.36
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.7
      pick: 0.19
      fit: 0.17
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.64
      pick: 0.15
      fit: 0.65
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.14
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shogun''s Ofuda, Golden Blade, Amanita Charm, Riptalon, Tyrfing, Silverbranch
    Bow, Runeforged Hammer, Toxic Blade, Genji''s Guard, Lernaean Bow, Breastplate
    of Valor, Pharaoh''s Curse, Tekko-Kagi, Shield Splitter, Hydra''s Lament, Daybreak
    Gavel, Eye of the Storm, Avenging Blade, Dominance, Erosion, Shield of the Phoenix,
    Eye of Providence, Stone of Binding, The Reaper.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.12
      fit: 0.56
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.25
      fit: 0.38
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.27
      fit: 0.24
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.34
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.7
      pick: 0.19
      fit: 0.16
    Shogun's Ofuda:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.14
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Genji's Guard
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
    + fit + win/pick). Underrated for this god: Shogun''s Ofuda, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Hydra''s Lament, Golden Blade, Shield of the Phoenix,
    Screeching Gargoyle, Runeforged Hammer, Silverbranch Bow, Lernaean Bow, Arondight,
    Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak Gavel, Toxic Blade, Eye of
    Erebus, Tekko-Kagi, Eye of the Storm, Gladiator''s Shield, Avenging Blade, Erosion,
    Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.25
      fit: 0.3
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.27
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.34
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.19
      fit: 0.39
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.14
      fit: 0.3
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Golden Blade, Runeforged Hammer, Tyrfing,
    Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate of Valor,
    Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s Lament, Pharaoh''s Curse,
    Avenging Blade, Shogun''s Ofuda, Titan''s Bane, The Crusher, Daybreak Gavel, Deathbringer,
    Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.12
      fit: 0.6
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.25
      fit: 0.4
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.27
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.42
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.32
  starter: *id001
---
