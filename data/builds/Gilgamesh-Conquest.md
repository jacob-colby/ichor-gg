---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.65
  aspect_win_rate: 0.57
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.29
    win_rate: 0.63
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.22
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.61
  - name: Barbed Carver
    pick_rate: 0.14
    win_rate: 0.64
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.52
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.54
  - name: Berserker's Shield
    pick_rate: 0.12
    win_rate: 0.61
    alternates:
    - name: The Reaper
      pick_rate: 0.12
      win_rate: 0.66
    - name: Barbed Carver
      pick_rate: 0.09
      win_rate: 0.8
  - name: Heartseeker
    pick_rate: 0.22
    win_rate: 0.63
    alternates:
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.71
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.47
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.73
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.78
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.75
  - name: Veve Charm
    pick_rate: 0.06
    win_rate: 0.4
    alternates:
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.3
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.89
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.27
    win_rate: 0.69
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.58
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.38
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-29'
  god_win_rate: 0.5830388692579506
  god_matches_won: 165
  god_matches_played: 283
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-29'
  god_matches_analyzed: 9506
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - The Crusher
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, The Crusher, Golden Blade, Runeforged
    Hammer, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s Lament, Pharaoh''s
    Curse, Avenging Blade, Shifter''s Shield, Shogun''s Ofuda, Daybreak Gavel, Deathbringer,
    Dominance, Erosion, Eye of Providence, Shield of the Phoenix, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.19
      fit: 0.4
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.37
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.21
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.71
      pick: 0.13
      fit: 0.44
    Titan's Bane:
      total: 0.64
      efficiency: 0.47
      win: 0.89
      pick: 0.18
      fit: 0.44
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  - Titan's Bane
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Freya''s
    Tears, The Crusher, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Hydra''s Lament, Golden Blade, Lernaean Bow, Tyrfing, Shield Splitter,
    Tekko-Kagi, Eye of the Storm, Avenging Blade, Silverbranch Bow, Dominance, Daybreak
    Gavel, Shield of the Phoenix, Shifter''s Shield, Pharaoh''s Curse, Toxic Blade,
    Transcendence, Deathbringer, Eye of Providence, Shogun''s Ofuda, Kinetic Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.19
      fit: 0.27
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.41
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.2
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.37
      fit: 0.53
    Titan's Bane:
      total: 0.63
      efficiency: 0.47
      win: 0.89
      pick: 0.18
      fit: 0.37
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - The Reaper
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
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Golden Blade,
    Runeforged Hammer, Riptalon, Shield Splitter, Genji''s Guard, Breastplate of Valor,
    Yogi''s Necklace, Shifter''s Shield, Eye of the Storm, Lernaean Bow, Tyrfing,
    Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda, Tekko-Kagi, Toxic
    Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Hydra''s Lament, Draconic
    Scale, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.61
      pick: 0.19
      fit: 0.43
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.32
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.27
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.66
      pick: 0.19
      fit: 0.6
    Titan's Bane:
      total: 0.63
      efficiency: 0.47
      win: 0.89
      pick: 0.18
      fit: 0.4
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Berserker's Shield
  - Heartseeker
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
    for this god: Freya''s Tears, The Crusher, Avenging Blade, Amanita Charm, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged Hammer,
    Screeching Gargoyle, Void Shield, Void Stone, Genji''s Guard, Breastplate of Valor,
    Lernaean Bow, Tyrfing, Shield Splitter, Riptalon, Hydra''s Lament, Eye of the
    Storm, Pharaoh''s Curse, Shifter''s Shield, Avatar''s Parashu, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.19
      fit: 0.33
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.48
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.17
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.71
      pick: 0.13
      fit: 0.55
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.63
      pick: 0.37
      fit: 0.65
    Titan's Bane:
      total: 0.66
      efficiency: 0.47
      win: 0.89
      pick: 0.18
      fit: 0.55
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Riptalon
  - Titan's Bane
  flex_slots:
  - Golden Blade
  - Riptalon
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
    this god: Freya''s Tears, Amanita Charm, Golden Blade, Riptalon, Tyrfing, Silverbranch
    Bow, Runeforged Hammer, Toxic Blade, Genji''s Guard, Lernaean Bow, Breastplate
    of Valor, Pharaoh''s Curse, Tekko-Kagi, Shogun''s Ofuda, Shield Splitter, Shifter''s
    Shield, Hydra''s Lament, Daybreak Gavel, Eye of the Storm, Avenging Blade, Dominance,
    Erosion, Shield of the Phoenix, Eye of Providence, Stone of Binding, Kinetic Cuirass.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.19
      fit: 0.38
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.24
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.16
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.51
    Titan's Bane:
      total: 0.62
      efficiency: 0.47
      win: 0.89
      pick: 0.18
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Breastplate of Valor
  - Freya's Tears
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Screeching Gargoyle,
    Runeforged Hammer, Golden Blade, Silverbranch Bow, Lernaean Bow, Arondight, Tyrfing,
    Shifter''s Shield, Pharaoh''s Curse, Shield Splitter, Daybreak Gavel, Toxic Blade,
    Eye of Erebus, Shogun''s Ofuda, Tekko-Kagi, Eye of the Storm, Gladiator''s Shield,
    Avenging Blade, Erosion, Eye of Providence, Kinetic Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.19
      fit: 0.3
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.45
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.33
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.39
    Titan's Bane:
      total: 0.62
      efficiency: 0.47
      win: 0.89
      pick: 0.18
      fit: 0.28
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
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
    of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow, Toxic Blade, Shifter''s
    Shield, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The
    Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.19
      fit: 0.4
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.37
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.47
      pick: 0.12
      fit: 0.42
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  starter: *id001
---
