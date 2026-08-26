---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.59
  aspect_win_rate: 0.55
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.27
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.22
      win_rate: 0.38
    - name: Hydra's Lament
      pick_rate: 0.16
      win_rate: 0.67
  - name: Barbed Carver
    pick_rate: 0.24
    win_rate: 0.67
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.16
      win_rate: 0.5
    - name: Shogun's Ofuda
      pick_rate: 0.11
      win_rate: 0.0
  - name: Berserker's Shield
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.33
    - name: The Reaper
      pick_rate: 0.08
      win_rate: 1.0
  - name: The Crusher
    pick_rate: 0.14
    win_rate: 1.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.0
  - name: Heartseeker
    pick_rate: 0.17
    win_rate: 0.8
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 1.0
    - name: Hide of the Nemean Lion
      pick_rate: 0.1
      win_rate: 0.33
  - name: Mote of Chaos
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 1.0
    - name: Pharaoh's Curse
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.32
    win_rate: 0.75
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.29
  - name: Bumba's Hammer
    pick_rate: 0.14
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-08-26'
  god_win_rate: 0.5675675675675675
  god_matches_won: 21
  god_matches_played: 37
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Freya's Tears
  - The Reaper
  - The Crusher
  - Heartseeker
  - Pharaoh's Curse
  flex_slots:
  - Berserker's Shield
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Golden Blade, Runeforged Hammer, Tyrfing, Lernaean Bow,
    Shield Splitter, Tekko-Kagi, Breastplate of Valor, Eye of the Storm, Silverbranch
    Bow, Toxic Blade, Avenging Blade, Titan''s Bane, Daybreak Gavel, Deathbringer,
    Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.64
      efficiency: 0.68
      win: 0.75
      pick: 0.17
      fit: 0.4
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.34
      fit: 0.21
    The Reaper:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.34
    The Crusher:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.44
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.8
      pick: 0.37
      fit: 0.54
    Pharaoh's Curse:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.4
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  - Heartseeker
  - Pharaoh's Curse
  flex_slots:
  - Jotunn's Revenge
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Breastplate of Valor, Runeforged Hammer, Golden Blade, Lernaean Bow, Tyrfing,
    Shield Splitter, Tekko-Kagi, Eye of the Storm, Avenging Blade, Silverbranch Bow,
    Dominance, Daybreak Gavel, Shield of the Phoenix, Titan''s Bane, Toxic Blade,
    Transcendence, Deathbringer, Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.6
      pick: 0.27
      fit: 0.41
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.16
      fit: 0.41
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.34
      fit: 0.2
    The Crusher:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.37
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.8
      pick: 0.37
      fit: 0.53
    Pharaoh's Curse:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Freya's Tears
  - The Reaper
  - The Crusher
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, Shield of the Phoenix, Golden Blade, Runeforged
    Hammer, Riptalon, Shield Splitter, Breastplate of Valor, Yogi''s Necklace, Eye
    of the Storm, Lernaean Bow, Tyrfing, Phoenix Feather, Erosion, Tekko-Kagi, Toxic
    Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.75
      pick: 0.17
      fit: 0.43
    Freya's Tears:
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.34
      fit: 0.27
    The Reaper:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.6
    The Crusher:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.4
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.7
    Pharaoh's Curse:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Freya's Tears
  - The Reaper
  - The Crusher
  - Heartseeker
  - Pharaoh's Curse
  flex_slots:
  - Heartseeker
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Avenging Blade, Amanita Charm, Tekko-Kagi, Stone of
    Binding, Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged Hammer, Screeching
    Gargoyle, Void Shield, Titan''s Bane, Void Stone, Breastplate of Valor, Lernaean
    Bow, Tyrfing, Shield Splitter, Riptalon, Eye of the Storm, Avatar''s Parashu.'
  slot_scores:
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.75
      pick: 0.17
      fit: 0.33
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.34
      fit: 0.17
    The Reaper:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.45
    The Crusher:
      total: 0.71
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.55
    Heartseeker:
      total: 0.64
      efficiency: 0.47
      win: 0.8
      pick: 0.37
      fit: 0.65
    Pharaoh's Curse:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Freya's Tears
  - The Reaper
  - The Crusher
  - Pharaoh's Curse
  flex_slots:
  - Berserker's Shield
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, Golden Blade, Riptalon, Tyrfing, Silverbranch
    Bow, Runeforged Hammer, Toxic Blade, Lernaean Bow, Breastplate of Valor, Tekko-Kagi,
    Shield Splitter, Daybreak Gavel, Eye of the Storm, Avenging Blade, Dominance,
    Erosion, Shield of the Phoenix, Eye of Providence, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.64
      efficiency: 0.68
      win: 0.75
      pick: 0.17
      fit: 0.38
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.34
      fit: 0.16
    The Reaper:
      total: 0.69
      efficiency: 0.55
      win: 1.0
      pick: 0.12
      fit: 0.28
    The Crusher:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.32
    Pharaoh's Curse:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - The Crusher
  - Pharaoh's Curse
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Shield of the Phoenix, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch
    Bow, Lernaean Bow, Arondight, Tyrfing, Shield Splitter, Daybreak Gavel, Toxic
    Blade, Eye of Erebus, Tekko-Kagi, Eye of the Storm, Gladiator''s Shield, Avenging
    Blade, Erosion, Eye of Providence.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.6
      pick: 0.27
      fit: 0.45
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.34
      fit: 0.39
    The Reaper:
      total: 0.66
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.18
    The Crusher:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.28
    Pharaoh's Curse:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.15
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
    Lernaean Bow, Shield Splitter, Tekko-Kagi, Breastplate of Valor, Eye of the Storm,
    Silverbranch Bow, Toxic Blade, Avenging Blade, Titan''s Bane, Daybreak Gavel,
    Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.64
      efficiency: 0.68
      win: 0.75
      pick: 0.17
      fit: 0.4
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.27
      fit: 0.37
    Kinetic Cuirass:
      total: 0.27
      efficiency: 0.56
      win: 0.0
      pick: 0.15
      fit: 0.42
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.32
  starter: *id001
---
