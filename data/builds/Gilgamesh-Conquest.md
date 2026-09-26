---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.63
  aspect_win_rate: 0.59
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.21
    win_rate: 0.46
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.17
      win_rate: 0.73
    - name: Transcendence
      pick_rate: 0.17
      win_rate: 0.71
  - name: Barbed Carver
    pick_rate: 0.14
    win_rate: 0.61
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.23
      win_rate: 0.72
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.61
  - name: Berserker's Shield
    pick_rate: 0.11
    win_rate: 0.79
    alternates:
    - name: Barbed Carver
      pick_rate: 0.16
      win_rate: 0.5
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.64
  - name: The Reaper
    pick_rate: 0.16
    win_rate: 0.65
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.3
    - name: Barbed Carver
      pick_rate: 0.07
      win_rate: 0.78
  - name: Heartseeker
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.86
    - name: Titan's Bane
      pick_rate: 0.04
      win_rate: 1.0
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Magi's Cloak
      pick_rate: 0.07
      win_rate: 0.8
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.75
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.31
    win_rate: 0.64
  - name: Hunter's Cowl
    pick_rate: 0.21
    win_rate: 0.58
  - name: Bluestone Pendant
    pick_rate: 0.12
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-09-26'
  god_win_rate: 0.5555555555555556
  god_matches_won: 70
  god_matches_played: 126
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-26'
  god_matches_analyzed: 4198
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Magi's Cloak
  - Runeforged Hammer
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Runeforged Hammer
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
    this god: Amanita Charm, Golden Blade, Runeforged Hammer, Kinetic Cuirass, Tyrfing,
    Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s Lament,
    Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The Crusher, Daybreak Gavel,
    Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.66
      efficiency: 0.68
      win: 0.79
      pick: 0.17
      fit: 0.4
    Magi's Cloak:
      total: 0.58
      efficiency: 0.53
      win: 0.8
      pick: 0.22
      fit: 0.18
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.44
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.18
      fit: 0.44
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Magi's Cloak
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Transcendence
  - Magi's Cloak
  - Heartseeker
  flex_slots:
  - Breastplate of Valor
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Hydra''s Lament,
    Golden Blade, Freya''s Tears, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield Splitter,
    Tekko-Kagi, Eye of the Storm, Avenging Blade, Silverbranch Bow, Dominance, Daybreak
    Gavel, Shield of the Phoenix, Pharaoh''s Curse, The Crusher, Toxic Blade, Deathbringer,
    Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.64
      efficiency: 0.68
      win: 0.79
      pick: 0.17
      fit: 0.27
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.2
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.17
      fit: 0.22
    Magi's Cloak:
      total: 0.57
      efficiency: 0.53
      win: 0.8
      pick: 0.22
      fit: 0.12
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.53
  community_ordered:
  - Berserker's Shield
  - Transcendence
  - Magi's Cloak
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Magi's Cloak
  - Shield of the Phoenix
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Golden Blade,
    Runeforged Hammer, Riptalon, Freya''s Tears, Shield Splitter, Genji''s Guard,
    Breastplate of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean Bow, Tyrfing,
    Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda, Tekko-Kagi, Toxic
    Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Hydra''s Lament, Draconic
    Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.67
      efficiency: 0.68
      win: 0.79
      pick: 0.17
      fit: 0.43
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.5
    Magi's Cloak:
      total: 0.59
      efficiency: 0.53
      win: 0.8
      pick: 0.22
      fit: 0.25
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.6
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.75
      pick: 0.18
      fit: 0.4
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - Magi's Cloak
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Magi's Cloak
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    for this god: Avenging Blade, Amanita Charm, Tekko-Kagi, Stone of Binding, Silverbranch
    Bow, Golden Blade, Toxic Blade, Runeforged Hammer, Screeching Gargoyle, Void Shield,
    Kinetic Cuirass, Void Stone, The Crusher, Genji''s Guard, Breastplate of Valor,
    Lernaean Bow, Tyrfing, Freya''s Tears, Shield Splitter, Riptalon, Hydra''s Lament,
    Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.58
      efficiency: 0.49
      win: 0.67
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.79
      pick: 0.17
      fit: 0.33
    Magi's Cloak:
      total: 0.58
      efficiency: 0.53
      win: 0.8
      pick: 0.22
      fit: 0.14
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.65
    Titan's Bane:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.18
      fit: 0.55
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Berserker's Shield
  - Magi's Cloak
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Magi's Cloak
  - Riptalon
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Titan's Bane
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Golden Blade, Riptalon, Tyrfing, Silverbranch Bow, Kinetic
    Cuirass, Runeforged Hammer, Toxic Blade, Genji''s Guard, Lernaean Bow, Breastplate
    of Valor, Freya''s Tears, Pharaoh''s Curse, Tekko-Kagi, Shogun''s Ofuda, Shield
    Splitter, Hydra''s Lament, Daybreak Gavel, Eye of the Storm, Avenging Blade, Dominance,
    Erosion, Shield of the Phoenix, Eye of Providence, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.66
      efficiency: 0.68
      win: 0.79
      pick: 0.17
      fit: 0.38
    Magi's Cloak:
      total: 0.58
      efficiency: 0.53
      win: 0.8
      pick: 0.22
      fit: 0.14
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.51
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.75
      pick: 0.18
      fit: 0.32
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Berserker's Shield
  - Magi's Cloak
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Magi's Cloak
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch Bow,
    Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak
    Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Tekko-Kagi, Eye of the Storm,
    Gladiator''s Shield, Avenging Blade, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.79
      pick: 0.17
      fit: 0.3
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.33
    Magi's Cloak:
      total: 0.58
      efficiency: 0.53
      win: 0.8
      pick: 0.22
      fit: 0.13
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Berserker's Shield
  - Magi's Cloak
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
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
    Underrated for this god: Amanita Charm, Golden Blade, Runeforged Hammer, Kinetic
    Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate
    of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s
    Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The Crusher, Daybreak
    Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.46
      pick: 0.21
      fit: 0.37
    Berserker's Shield:
      total: 0.66
      efficiency: 0.68
      win: 0.79
      pick: 0.17
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.67
      pick: 0.0
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
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  starter: *id001
---
