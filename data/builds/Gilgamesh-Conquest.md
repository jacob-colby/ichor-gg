---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.62
  aspect_win_rate: 0.56
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.29
    win_rate: 0.6
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.2
      win_rate: 0.62
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.59
  - name: Barbed Carver
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.13
      win_rate: 0.55
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.52
  - name: The Reaper
    pick_rate: 0.12
    win_rate: 0.62
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.57
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.8
  - name: Heartseeker
    pick_rate: 0.22
    win_rate: 0.6
    alternates:
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.63
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.43
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.63
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.7
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.67
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.23
    alternates:
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.45
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 0.89
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.27
    win_rate: 0.68
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-30'
  god_win_rate: 0.5757575757575758
  god_matches_won: 190
  god_matches_played: 330
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Golden Blade, Runeforged Hammer, Tyrfing, Lernaean Bow,
    The Crusher, Genji''s Guard, Tekko-Kagi, Shield Splitter, Eye of the Storm, Silverbranch
    Bow, Toxic Blade, Breastplate of Valor, Hydra''s Lament, Pharaoh''s Curse, Shifter''s
    Shield, Avenging Blade, Shogun''s Ofuda, Dominance, Daybreak Gavel, Erosion, Deathbringer,
    Eye of Providence, Shield of the Phoenix, Kinetic Cuirass.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.18
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.6
      pick: 0.29
      fit: 0.37
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.21
    Titan's Bane:
      total: 0.64
      efficiency: 0.47
      win: 0.89
      pick: 0.15
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
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
  - Genji's Guard
  - Heartseeker
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Amanita Charm, Breastplate of Valor, Hydra''s Lament, Runeforged Hammer,
    Golden Blade, The Crusher, Lernaean Bow, Tyrfing, Shield Splitter, Tekko-Kagi,
    Eye of the Storm, Avenging Blade, Silverbranch Bow, Dominance, Shifter''s Shield,
    Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, Toxic Blade, Transcendence,
    Oni Hunter''s Garb, Eye of Providence, Deathbringer, Kinetic Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.55
      pick: 0.18
      fit: 0.27
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.6
      pick: 0.29
      fit: 0.41
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.2
    Heartseeker:
      total: 0.53
      efficiency: 0.46
      win: 0.6
      pick: 0.37
      fit: 0.53
    Titan's Bane:
      total: 0.63
      efficiency: 0.47
      win: 0.89
      pick: 0.15
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
  - The Reaper
  - Freya's Tears
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
    this god: Amanita Charm, Shield of the Phoenix, Golden Blade, Runeforged Hammer,
    Riptalon, Shield Splitter, Genji''s Guard, Shifter''s Shield, Yogi''s Necklace,
    Breastplate of Valor, Eye of the Storm, Tyrfing, Lernaean Bow, Pharaoh''s Curse,
    Erosion, Phoenix Feather, Tekko-Kagi, Toxic Blade, Shogun''s Ofuda, Eye of Providence,
    Avenging Blade, Silverbranch Bow, Hydra''s Lament, Draconic Scale, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.18
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.6
      pick: 0.29
      fit: 0.32
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.27
    The Reaper:
      total: 0.55
      efficiency: 0.49
      win: 0.62
      pick: 0.19
      fit: 0.6
    Titan's Bane:
      total: 0.63
      efficiency: 0.47
      win: 0.89
      pick: 0.15
      fit: 0.4
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
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
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Berserker's Shield
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, The Crusher, Amanita Charm, Tekko-Kagi, Silverbranch
    Bow, Stone of Binding, Golden Blade, Toxic Blade, Runeforged Hammer, Void Shield,
    Screeching Gargoyle, Void Stone, Genji''s Guard, Lernaean Bow, Tyrfing, Breastplate
    of Valor, Shield Splitter, Riptalon, Hydra''s Lament, Eye of the Storm, Shifter''s
    Shield, Pharaoh''s Curse, Daybreak Gavel, Kinetic Cuirass.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.18
      fit: 0.33
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.6
      pick: 0.29
      fit: 0.48
    Transcendence:
      total: 0.48
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.16
    Heartseeker:
      total: 0.55
      efficiency: 0.46
      win: 0.6
      pick: 0.37
      fit: 0.65
    Titan's Bane:
      total: 0.66
      efficiency: 0.47
      win: 0.89
      pick: 0.15
      fit: 0.55
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Amanita Charm, Riptalon, Tyrfing, Silverbranch Bow, Toxic
    Blade, Genji''s Guard, Runeforged Hammer, Lernaean Bow, Breastplate of Valor,
    Pharaoh''s Curse, Tekko-Kagi, Shogun''s Ofuda, Shifter''s Shield, Shield Splitter,
    Hydra''s Lament, Daybreak Gavel, Eye of the Storm, Avenging Blade, Dominance,
    Erosion, Shield of the Phoenix, Eye of Providence, Midgardian Mail, Kinetic Cuirass.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.18
      fit: 0.38
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.6
      pick: 0.29
      fit: 0.24
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.51
    Titan's Bane:
      total: 0.62
      efficiency: 0.47
      win: 0.89
      pick: 0.15
      fit: 0.32
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
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
  - Breastplate of Valor
  - Berserker's Shield
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
    Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Screeching Gargoyle, Runeforged
    Hammer, Golden Blade, Silverbranch Bow, Shifter''s Shield, Lernaean Bow, Arondight,
    Tyrfing, Pharaoh''s Curse, Daybreak Gavel, Toxic Blade, Shield Splitter, Eye of
    Erebus, Shogun''s Ofuda, Gladiator''s Shield, Tekko-Kagi, Eye of the Storm, Erosion,
    Eye of Providence, Avenging Blade, Kinetic Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.18
      fit: 0.3
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.6
      pick: 0.29
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.33
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.39
    Titan's Bane:
      total: 0.62
      efficiency: 0.47
      win: 0.89
      pick: 0.15
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Golden Blade, Runeforged Hammer, Kinetic
    Cuirass, Tyrfing, Lernaean Bow, Genji''s Guard, Tekko-Kagi, Shield Splitter, Eye
    of the Storm, Silverbranch Bow, Toxic Blade, Breastplate of Valor, Hydra''s Lament,
    Pharaoh''s Curse, Shifter''s Shield, Avenging Blade, Shogun''s Ofuda, The Crusher,
    Dominance, Daybreak Gavel, Erosion, Deathbringer, Eye of Providence, Shield of
    the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.18
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.6
      pick: 0.29
      fit: 0.37
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.57
      win: 0.43
      pick: 0.12
      fit: 0.42
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  starter: *id001
---
