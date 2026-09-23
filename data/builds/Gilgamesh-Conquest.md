---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.61
  aspect_win_rate: 0.64
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.43
    - name: Transcendence
      pick_rate: 0.15
      win_rate: 0.83
  - name: Shifter's Shield
    pick_rate: 0.24
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.22
      win_rate: 0.78
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.0
  - name: Barbed Carver
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.8
    - name: Shogun's Ofuda
      pick_rate: 0.1
      win_rate: 0.0
  - name: The Reaper
    pick_rate: 0.13
    win_rate: 0.8
    alternates:
    - name: Barbed Carver
      pick_rate: 0.13
      win_rate: 1.0
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.67
  - name: Heartseeker
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.0
  - name: Titan's Bane
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Magi's Cloak
      pick_rate: 0.08
      win_rate: 0.5
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.6
  - name: Bumba's Hammer
    pick_rate: 0.22
    win_rate: 0.56
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-09-23'
  god_win_rate: 0.5365853658536586
  god_matches_won: 22
  god_matches_played: 41
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Golden Blade, Runeforged Hammer, Kinetic
    Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s Lament, Pharaoh''s
    Curse, Avenging Blade, The Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion,
    Eye of Providence, Shield of the Phoenix, Berserker''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.37
    Transcendence:
      total: 0.59
      efficiency: 0.53
      win: 0.83
      pick: 0.15
      fit: 0.2
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.21
    The Reaper:
      total: 0.6
      efficiency: 0.5
      win: 0.8
      pick: 0.22
      fit: 0.34
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.32
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Transcendence,
    Freya''s Tears, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Hydra''s Lament, Golden Blade, Kinetic Cuirass, Lernaean Bow, Tyrfing,
    Shield Splitter, Tekko-Kagi, Eye of the Storm, Avenging Blade, Silverbranch Bow,
    Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, The Crusher,
    Toxic Blade, Deathbringer, Eye of Providence, Berserker''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.41
    Transcendence:
      total: 0.6
      efficiency: 0.53
      win: 0.83
      pick: 0.15
      fit: 0.22
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.2
    The Reaper:
      total: 0.59
      efficiency: 0.5
      win: 0.8
      pick: 0.22
      fit: 0.27
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.32
      fit: 0.53
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Jotunn's Revenge
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Riptalon, Shield Splitter, Genji''s Guard, Breastplate
    of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean Bow, Tyrfing, Pharaoh''s
    Curse, Phoenix Feather, Erosion, Tekko-Kagi, Toxic Blade, Eye of Providence, Avenging
    Blade, Silverbranch Bow, Hydra''s Lament, Draconic Scale, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.32
    Transcendence:
      total: 0.59
      efficiency: 0.53
      win: 0.83
      pick: 0.15
      fit: 0.17
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.27
    The Reaper:
      total: 0.63
      efficiency: 0.5
      win: 0.8
      pick: 0.22
      fit: 0.6
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.32
      fit: 0.5
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
  flex_slots:
  - Freya's Tears
  - Avenging Blade
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
    for this god: Freya''s Tears, Avenging Blade, Amanita Charm, Tekko-Kagi, Stone
    of Binding, Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged Hammer, Screeching
    Gargoyle, Void Shield, Kinetic Cuirass, Void Stone, The Crusher, Genji''s Guard,
    Breastplate of Valor, Lernaean Bow, Tyrfing, Shield Splitter, Riptalon, Hydra''s
    Lament, Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu, Berserker''s Shield.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.48
    Transcendence:
      total: 0.59
      efficiency: 0.53
      win: 0.83
      pick: 0.15
      fit: 0.16
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.17
    The Reaper:
      total: 0.61
      efficiency: 0.5
      win: 0.8
      pick: 0.22
      fit: 0.45
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.67
      pick: 0.32
      fit: 0.65
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Transcendence
  - Tyrfing
  - Freya's Tears
  - The Reaper
  - Riptalon
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Golden Blade, Riptalon, Tyrfing, Silverbranch
    Bow, Kinetic Cuirass, Runeforged Hammer, Toxic Blade, Genji''s Guard, Lernaean
    Bow, Breastplate of Valor, Pharaoh''s Curse, Tekko-Kagi, Shield Splitter, Hydra''s
    Lament, Daybreak Gavel, Eye of the Storm, Avenging Blade, Dominance, Erosion,
    Shield of the Phoenix, Eye of Providence, Stone of Binding, Berserker''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Transcendence:
      total: 0.58
      efficiency: 0.53
      win: 0.83
      pick: 0.15
      fit: 0.11
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.16
    The Reaper:
      total: 0.61
      efficiency: 0.55
      win: 0.8
      pick: 0.22
      fit: 0.28
    Riptalon:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Transcendence
  - Freya's Tears
  - The Reaper
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
  flex_slots:
  - Heartseeker
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic Cuirass,
    Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch Bow, Lernaean
    Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak Gavel, Toxic
    Blade, Eye of Erebus, Tekko-Kagi, Eye of the Storm, Gladiator''s Shield, Avenging
    Blade, Erosion, Eye of Providence, Berserker''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.45
    Transcendence:
      total: 0.58
      efficiency: 0.53
      win: 0.83
      pick: 0.15
      fit: 0.08
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.39
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.8
      pick: 0.22
      fit: 0.18
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.32
      fit: 0.38
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
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
    Underrated for this god: Berserker''s Shield, Amanita Charm, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow,
    Toxic Blade, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, The Crusher, Daybreak
    Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.31
      efficiency: 0.68
      win: 0.0
      pick: 0.14
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.2
      fit: 0.37
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  starter: *id001
---
