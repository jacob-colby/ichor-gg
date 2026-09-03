---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.48
  aspect_win_rate: 0.54
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.22
    win_rate: 0.45
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.21
      win_rate: 0.59
    - name: Golden Blade
      pick_rate: 0.13
      win_rate: 0.64
  - name: Berserker's Shield
    pick_rate: 0.19
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.5
    - name: Barbed Carver
      pick_rate: 0.11
      win_rate: 0.62
  - name: Shogun's Ofuda
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.52
  - name: Heartseeker
    pick_rate: 0.09
    win_rate: 0.61
    alternates:
    - name: The Crusher
      pick_rate: 0.06
      win_rate: 0.76
    - name: Berserker's Shield
      pick_rate: 0.06
      win_rate: 0.52
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.61
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.65
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.6
  - name: Blinking Abyss
    pick_rate: 0.04
    win_rate: 0.67
    alternates:
    - name: Titan's Bane
      pick_rate: 0.04
      win_rate: 0.88
    - name: Lucerne Hammer
      pick_rate: 0.04
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.29
    win_rate: 0.66
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.39
  - name: Bumba's Hammer
    pick_rate: 0.11
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-09-03'
  god_win_rate: 0.5602240896358543
  god_matches_won: 200
  god_matches_played: 357
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-03'
  god_matches_analyzed: 10626
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Titan''s Bane, The Crusher, Golden Blade, Amanita Charm, Runeforged
    Hammer, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Freya''s Tears, Genji''s
    Guard, Breastplate of Valor, Eye of the Storm, Silverbranch Bow, Toxic Blade,
    Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Daybreak Gavel, Deathbringer,
    Dominance, Erosion, Eye of Providence, Shield of the Phoenix, Shogun''s Ofuda.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.64
      pick: 0.13
      fit: 0.6
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.26
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.37
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.76
      pick: 0.1
      fit: 0.44
    Titan's Bane:
      total: 0.63
      efficiency: 0.47
      win: 0.88
      pick: 0.12
      fit: 0.44
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.32
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Titan''s
    Bane, The Crusher, Golden Blade, Amanita Charm, Genji''s Guard, Breastplate of
    Valor, Runeforged Hammer, Hydra''s Lament, Freya''s Tears, Lernaean Bow, Tyrfing,
    Shield Splitter, Tekko-Kagi, Eye of the Storm, Avenging Blade, Silverbranch Bow,
    Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, Toxic Blade,
    Transcendence, Deathbringer, Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.64
      pick: 0.13
      fit: 0.43
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.2
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.41
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.76
      pick: 0.1
      fit: 0.37
    Titan's Bane:
      total: 0.62
      efficiency: 0.47
      win: 0.88
      pick: 0.12
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Golden Blade
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
    this god: Amanita Charm, Golden Blade, Shield of the Phoenix, The Reaper, Runeforged
    Hammer, Riptalon, Freya''s Tears, Shield Splitter, Genji''s Guard, Breastplate
    of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean Bow, Tyrfing, Pharaoh''s
    Curse, Phoenix Feather, Erosion, Tekko-Kagi, Toxic Blade, Eye of Providence, Avenging
    Blade, Silverbranch Bow, Hydra''s Lament, Draconic Scale, Shogun''s Ofuda.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.64
      pick: 0.13
      fit: 0.56
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.26
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.32
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.76
      pick: 0.1
      fit: 0.4
    Titan's Bane:
      total: 0.63
      efficiency: 0.47
      win: 0.88
      pick: 0.12
      fit: 0.4
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Avenging Blade
  - Berserker's Shield
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
    for this god: Titan''s Bane, The Crusher, Golden Blade, Avenging Blade, Amanita
    Charm, Tekko-Kagi, Stone of Binding, Silverbranch Bow, Toxic Blade, Runeforged
    Hammer, Screeching Gargoyle, Void Shield, Void Stone, Genji''s Guard, Breastplate
    of Valor, Freya''s Tears, Lernaean Bow, The Reaper, Tyrfing, Shield Splitter,
    Riptalon, Hydra''s Lament, Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.64
      pick: 0.13
      fit: 0.5
    Avenging Blade:
      total: 0.55
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.26
      fit: 0.33
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.48
    The Crusher:
      total: 0.59
      efficiency: 0.47
      win: 0.76
      pick: 0.1
      fit: 0.55
    Titan's Bane:
      total: 0.65
      efficiency: 0.47
      win: 0.88
      pick: 0.12
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Berserker's Shield
  - Riptalon
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
    this god: Golden Blade, Amanita Charm, Riptalon, Tyrfing, Silverbranch Bow, Runeforged
    Hammer, Toxic Blade, Genji''s Guard, Lernaean Bow, Breastplate of Valor, Freya''s
    Tears, Pharaoh''s Curse, The Reaper, Tekko-Kagi, Shield Splitter, Hydra''s Lament,
    Daybreak Gavel, Eye of the Storm, Avenging Blade, Dominance, Erosion, Shield of
    the Phoenix, Eye of Providence, Stone of Binding, Shogun''s Ofuda.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.64
      pick: 0.13
      fit: 0.56
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.26
      fit: 0.38
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.24
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.76
      pick: 0.1
      fit: 0.32
    Titan's Bane:
      total: 0.61
      efficiency: 0.47
      win: 0.88
      pick: 0.12
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Amanita Charm, Golden Blade, Hydra''s Lament, Shield of the Phoenix,
    Screeching Gargoyle, Runeforged Hammer, Silverbranch Bow, Lernaean Bow, Arondight,
    Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak Gavel, Toxic Blade, Eye of
    Erebus, Tekko-Kagi, Eye of the Storm, Gladiator''s Shield, Avenging Blade, Erosion,
    Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.33
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.45
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.13
      fit: 0.39
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.76
      pick: 0.1
      fit: 0.28
    Titan's Bane:
      total: 0.61
      efficiency: 0.47
      win: 0.88
      pick: 0.12
      fit: 0.28
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
    Freya''s Tears, Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s Lament,
    Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, Titan''s Bane, The Crusher,
    Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of
    the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.64
      pick: 0.13
      fit: 0.6
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.26
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.61
      pick: 0.15
      fit: 0.42
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.32
  starter: *id001
---
