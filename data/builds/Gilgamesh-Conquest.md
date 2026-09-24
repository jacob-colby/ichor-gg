---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.66
  aspect_win_rate: 0.57
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.27
    win_rate: 0.47
    alternates:
    - name: Transcendence
      pick_rate: 0.14
      win_rate: 0.8
    - name: Devourer's Gauntlet
      pick_rate: 0.14
      win_rate: 0.7
  - name: Shifter's Shield
    pick_rate: 0.16
    win_rate: 0.45
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.2
      win_rate: 0.71
    - name: Barbed Carver
      pick_rate: 0.11
      win_rate: 0.5
  - name: Barbed Carver
    pick_rate: 0.17
    win_rate: 0.42
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.1
      win_rate: 0.29
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.67
  - name: The Reaper
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Barbed Carver
      pick_rate: 0.1
      win_rate: 0.86
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.14
  - name: Heartseeker
    pick_rate: 0.14
    win_rate: 0.56
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.8
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 1.0
  - name: Titan's Bane
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.67
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.3
    win_rate: 0.57
  - name: Hunter's Cowl
    pick_rate: 0.2
    win_rate: 0.5
  - name: Bumba's Hammer
    pick_rate: 0.17
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-09-24'
  god_win_rate: 0.5
  god_matches_won: 35
  god_matches_played: 70
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Transcendence
  - Runeforged Hammer
  - The Reaper
  - Titan's Bane
  flex_slots:
  - Golden Blade
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Golden Blade, Runeforged Hammer, Kinetic Cuirass, Tyrfing,
    Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s Lament,
    Pharaoh''s Curse, Avenging Blade, The Crusher, Daybreak Gavel, Deathbringer, Dominance,
    Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.27
      fit: 0.37
    Transcendence:
      total: 0.58
      efficiency: 0.53
      win: 0.8
      pick: 0.14
      fit: 0.2
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.34
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.22
      fit: 0.44
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Transcendence,
    Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Hydra''s
    Lament, Golden Blade, Freya''s Tears, Kinetic Cuirass, Lernaean Bow, Tyrfing,
    Shield Splitter, Tekko-Kagi, Eye of the Storm, Avenging Blade, Silverbranch Bow,
    Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, The Crusher,
    Toxic Blade, Deathbringer, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.2
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.47
      pick: 0.27
      fit: 0.41
    Transcendence:
      total: 0.58
      efficiency: 0.53
      win: 0.8
      pick: 0.14
      fit: 0.22
    The Reaper:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.27
    Titan's Bane:
      total: 0.53
      efficiency: 0.47
      win: 0.67
      pick: 0.22
      fit: 0.37
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - The Reaper
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Golden Blade,
    Runeforged Hammer, Riptalon, Freya''s Tears, Shield Splitter, Genji''s Guard,
    Breastplate of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean Bow, Tyrfing,
    Pharaoh''s Curse, Phoenix Feather, Erosion, Tekko-Kagi, Toxic Blade, Eye of Providence,
    Avenging Blade, Silverbranch Bow, Hydra''s Lament, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.47
      pick: 0.27
      fit: 0.32
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.5
    Transcendence:
      total: 0.58
      efficiency: 0.53
      win: 0.8
      pick: 0.14
      fit: 0.17
    The Reaper:
      total: 0.58
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.6
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.22
      fit: 0.4
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
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
    for this god: Avenging Blade, Amanita Charm, Tekko-Kagi, Stone of Binding, Silverbranch
    Bow, Golden Blade, Toxic Blade, Runeforged Hammer, Screeching Gargoyle, Void Shield,
    Kinetic Cuirass, Void Stone, The Crusher, Genji''s Guard, Breastplate of Valor,
    Lernaean Bow, Tyrfing, Freya''s Tears, Shield Splitter, Riptalon, Hydra''s Lament,
    Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.27
      fit: 0.48
    Transcendence:
      total: 0.58
      efficiency: 0.53
      win: 0.8
      pick: 0.14
      fit: 0.16
    The Reaper:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.45
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.56
      pick: 0.3
      fit: 0.65
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.22
      fit: 0.55
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Transcendence
  - Tyrfing
  - The Reaper
  - Riptalon
  - Titan's Bane
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
    this god: Amanita Charm, Golden Blade, Riptalon, Tyrfing, Silverbranch Bow, Kinetic
    Cuirass, Runeforged Hammer, Toxic Blade, Genji''s Guard, Lernaean Bow, Breastplate
    of Valor, Freya''s Tears, Pharaoh''s Curse, Tekko-Kagi, Shield Splitter, Hydra''s
    Lament, Daybreak Gavel, Eye of the Storm, Avenging Blade, Dominance, Erosion,
    Shield of the Phoenix, Eye of Providence, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.56
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.8
      pick: 0.14
      fit: 0.11
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.55
    The Reaper:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.22
      fit: 0.28
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.51
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.67
      pick: 0.22
      fit: 0.32
  community_ordered:
  - Transcendence
  - The Reaper
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Titan's Bane
  flex_slots:
  - Freya's Tears
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch Bow,
    Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak
    Gavel, Toxic Blade, Eye of Erebus, Tekko-Kagi, Eye of the Storm, Gladiator''s
    Shield, Avenging Blade, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.33
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.47
      pick: 0.27
      fit: 0.45
    Transcendence:
      total: 0.56
      efficiency: 0.53
      win: 0.8
      pick: 0.14
      fit: 0.08
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.39
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.67
      pick: 0.22
      fit: 0.28
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Titan's Bane
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
    Lament, Pharaoh''s Curse, Avenging Blade, The Crusher, Daybreak Gavel, Deathbringer,
    Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.27
      fit: 0.37
    Berserker's Shield:
      total: 0.37
      efficiency: 0.68
      win: 0.14
      pick: 0.17
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  starter: *id001
---
