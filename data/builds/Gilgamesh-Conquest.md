---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.49
  aspect_win_rate: 0.58
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.21
    win_rate: 0.59
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.52
    - name: Golden Blade
      pick_rate: 0.12
      win_rate: 0.63
  - name: Berserker's Shield
    pick_rate: 0.17
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.52
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.57
  - name: Shifter's Shield
    pick_rate: 0.09
    win_rate: 0.54
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.57
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.52
  - name: Heartseeker
    pick_rate: 0.11
    win_rate: 0.57
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.63
    - name: The Crusher
      pick_rate: 0.06
      win_rate: 0.74
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.71
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.58
  - name: Mote of Chaos
    pick_rate: 0.04
    win_rate: 0.53
    alternates:
    - name: Lucerne Hammer
      pick_rate: 0.04
      win_rate: 0.53
    - name: Engraved Guard
      pick_rate: 0.04
      win_rate: 0.57
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.25
    win_rate: 0.66
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.43
  - name: Hunter's Cowl
    pick_rate: 0.15
    win_rate: 0.72
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-09-08'
  god_win_rate: 0.5751533742331288
  god_matches_won: 375
  god_matches_played: 652
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-08'
  god_matches_analyzed: 17639
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
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
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
    this god: The Crusher, Golden Blade, Freya''s Tears, Amanita Charm, Runeforged
    Hammer, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Kinetic Cuirass, Silverbranch Bow, Toxic Blade, Hydra''s
    Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, Shifter''s Shield,
    Titan''s Bane, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.63
      pick: 0.12
      fit: 0.6
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.23
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.37
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.21
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.74
      pick: 0.1
      fit: 0.44
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Breastplate of Valor
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Crusher, Golden Blade, Freya''s Tears, Amanita Charm, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Hydra''s Lament, Lernaean Bow, Tyrfing, Shield Splitter,
    Tekko-Kagi, Kinetic Cuirass, Eye of the Storm, Avenging Blade, Silverbranch Bow,
    Dominance, Daybreak Gavel, Shield of the Phoenix, Titan''s Bane, Pharaoh''s Curse,
    Shifter''s Shield, Toxic Blade, Transcendence, Deathbringer, Eye of Providence,
    Shogun''s Ofuda.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.63
      pick: 0.12
      fit: 0.43
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.23
      fit: 0.27
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.41
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.2
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.74
      pick: 0.1
      fit: 0.37
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Freya's Tears
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
    this god: Amanita Charm, Golden Blade, Freya''s Tears, Shield of the Phoenix,
    The Reaper, Runeforged Hammer, Riptalon, Kinetic Cuirass, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm, Shifter''s Shield,
    Lernaean Bow, Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda,
    Tekko-Kagi, Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch Bow,
    Hydra''s Lament, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.12
      fit: 0.56
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.23
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.32
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.27
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.74
      pick: 0.1
      fit: 0.4
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  flex_slots:
  - Avenging Blade
  - Freya's Tears
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
    for this god: The Crusher, Golden Blade, Avenging Blade, Freya''s Tears, Amanita
    Charm, Tekko-Kagi, Stone of Binding, Silverbranch Bow, Toxic Blade, Runeforged
    Hammer, Screeching Gargoyle, Void Shield, Titan''s Bane, Void Stone, Genji''s
    Guard, Breastplate of Valor, Lernaean Bow, The Reaper, Tyrfing, Shield Splitter,
    Kinetic Cuirass, Riptalon, Hydra''s Lament, Eye of the Storm, Pharaoh''s Curse,
    Avatar''s Parashu, Shifter''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.12
      fit: 0.5
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.23
      fit: 0.33
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.48
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.17
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.74
      pick: 0.1
      fit: 0.55
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Riptalon
  - The Crusher
  flex_slots:
  - Freya's Tears
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
    this god: Golden Blade, Freya''s Tears, Amanita Charm, Riptalon, Tyrfing, Silverbranch
    Bow, Runeforged Hammer, Toxic Blade, Genji''s Guard, Lernaean Bow, Breastplate
    of Valor, Pharaoh''s Curse, The Reaper, Tekko-Kagi, Kinetic Cuirass, Shogun''s
    Ofuda, Shield Splitter, Hydra''s Lament, Daybreak Gavel, Eye of the Storm, Shifter''s
    Shield, Avenging Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence,
    Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.12
      fit: 0.56
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.23
      fit: 0.38
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.24
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.16
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.74
      pick: 0.1
      fit: 0.32
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
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
    of Valor, Golden Blade, Amanita Charm, Hydra''s Lament, Shield of the Phoenix,
    Screeching Gargoyle, Runeforged Hammer, Kinetic Cuirass, Silverbranch Bow, Lernaean
    Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak Gavel, Toxic
    Blade, Shifter''s Shield, Eye of Erebus, Shogun''s Ofuda, Tekko-Kagi, Eye of the
    Storm, Gladiator''s Shield, Avenging Blade, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.23
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
      win: 0.59
      pick: 0.21
      fit: 0.45
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.13
      fit: 0.39
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.74
      pick: 0.1
      fit: 0.28
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
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
    Shield, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, Titan''s
    Bane, The Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.63
      pick: 0.12
      fit: 0.6
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.23
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.21
      fit: 0.37
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.52
      pick: 0.14
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
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  starter: *id001
---
