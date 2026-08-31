---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.49
  aspect_win_rate: 0.52
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.25
    win_rate: 0.42
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.23
      win_rate: 0.58
    - name: Golden Blade
      pick_rate: 0.09
      win_rate: 0.45
  - name: Berserker's Shield
    pick_rate: 0.21
    win_rate: 0.48
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.39
    - name: Barbed Carver
      pick_rate: 0.12
      win_rate: 0.6
  - name: Shogun's Ofuda
    pick_rate: 0.09
    win_rate: 0.59
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.46
    - name: The Reaper
      pick_rate: 0.08
      win_rate: 0.67
  - name: Heartseeker
    pick_rate: 0.08
    win_rate: 0.61
    alternates:
    - name: The Reaper
      pick_rate: 0.06
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.67
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.46
  - name: Blinking Abyss
    pick_rate: 0.05
    win_rate: 0.57
    alternates:
    - name: Lucerne Hammer
      pick_rate: 0.04
      win_rate: 0.33
    - name: Kinetic Cuirass
      pick_rate: 0.04
      win_rate: 0.4
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.29
    win_rate: 0.64
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.31
  - name: Hunter's Cowl
    pick_rate: 0.12
    win_rate: 0.66
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-08-31'
  god_win_rate: 0.5311203319502075
  god_matches_won: 128
  god_matches_played: 241
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-31'
  god_matches_analyzed: 7103
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Heartseeker, Runeforged Hammer, Tyrfing, Lernaean Bow,
    Shogun''s Ofuda, Shield Splitter, Tekko-Kagi, Breastplate of Valor, Eye of the
    Storm, Silverbranch Bow, Toxic Blade, Hydra''s Lament, Pharaoh''s Curse, Avenging
    Blade, Titan''s Bane, The Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion,
    Eye of Providence, Shield of the Phoenix, Golden Blade, Genji''s Guard, Kinetic
    Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.48
      pick: 0.29
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.23
      fit: 0.37
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.2
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.21
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.61
      pick: 0.13
      fit: 0.54
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.32
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Reaper
  - Heartseeker
  flex_slots:
  - Breastplate of Valor
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Heartseeker,
    Amanita Charm, Breastplate of Valor, Runeforged Hammer, Hydra''s Lament, Lernaean
    Bow, Tyrfing, Shield Splitter, Genji''s Guard, Shogun''s Ofuda, Tekko-Kagi, Eye
    of the Storm, Avenging Blade, Silverbranch Bow, Dominance, Daybreak Gavel, Shield
    of the Phoenix, Titan''s Bane, Pharaoh''s Curse, The Crusher, Toxic Blade, Transcendence,
    Deathbringer, Eye of Providence, Kinetic Cuirass, Golden Blade.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.23
      fit: 0.41
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.22
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.2
    The Reaper:
      total: 0.52
      efficiency: 0.5
      win: 0.67
      pick: 0.12
      fit: 0.27
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.61
      pick: 0.13
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Heartseeker
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
    this god: Amanita Charm, The Reaper, Shield of the Phoenix, Heartseeker, Runeforged
    Hammer, Riptalon, Shield Splitter, Shogun''s Ofuda, Breastplate of Valor, Yogi''s
    Necklace, Eye of the Storm, Lernaean Bow, Tyrfing, Pharaoh''s Curse, Phoenix Feather,
    Erosion, Tekko-Kagi, Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch
    Bow, Hydra''s Lament, Draconic Scale, Kinetic Cuirass, Genji''s Guard, Golden
    Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.48
      pick: 0.29
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.23
      fit: 0.32
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.27
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.12
      fit: 0.6
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.61
      pick: 0.13
      fit: 0.5
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.7
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
  - Avenging Blade
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Heartseeker, Avenging Blade, Amanita Charm, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Toxic Blade, Runeforged Hammer, Screeching
    Gargoyle, Void Shield, Titan''s Bane, Void Stone, The Crusher, Breastplate of
    Valor, Lernaean Bow, Tyrfing, Shield Splitter, Riptalon, Hydra''s Lament, Eye
    of the Storm, Pharaoh''s Curse, Avatar''s Parashu, Genji''s Guard, Kinetic Cuirass,
    Golden Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.23
      fit: 0.48
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.16
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.17
    The Reaper:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.12
      fit: 0.45
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.61
      pick: 0.13
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, Riptalon, Tyrfing, Silverbranch Bow, Heartseeker,
    Shogun''s Ofuda, Runeforged Hammer, Toxic Blade, Lernaean Bow, Breastplate of
    Valor, Pharaoh''s Curse, Tekko-Kagi, Shield Splitter, Hydra''s Lament, Daybreak
    Gavel, Eye of the Storm, Avenging Blade, Dominance, Genji''s Guard, Erosion, Shield
    of the Phoenix, Golden Blade, Eye of Providence, Stone of Binding, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.48
      pick: 0.29
      fit: 0.38
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.58
      pick: 0.23
      fit: 0.24
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.16
    The Reaper:
      total: 0.54
      efficiency: 0.55
      win: 0.67
      pick: 0.12
      fit: 0.28
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Hydra's Lament
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Hydra''s Lament, Genji''s Guard, Shield of the Phoenix, Heartseeker, Screeching
    Gargoyle, Runeforged Hammer, Shogun''s Ofuda, Silverbranch Bow, Lernaean Bow,
    Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak Gavel, Toxic Blade,
    Eye of Erebus, Tekko-Kagi, Eye of the Storm, Gladiator''s Shield, Avenging Blade,
    Erosion, Eye of Providence, Kinetic Cuirass, Golden Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.48
      pick: 0.29
      fit: 0.3
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.23
      fit: 0.45
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.39
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.24
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
    Underrated for this god: Amanita Charm, Golden Blade, Runeforged Hammer, Kinetic
    Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Heartseeker, Silverbranch Bow, Toxic Blade, Hydra''s
    Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, Titan''s Bane, The
    Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.45
      pick: 0.09
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.48
      pick: 0.29
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.23
      fit: 0.37
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.46
      pick: 0.13
      fit: 0.42
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.32
  starter: *id001
---
