---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.58
  aspect_win_rate: 0.51
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.29
    win_rate: 0.55
    alternates:
    - name: Transcendence
      pick_rate: 0.19
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.53
  - name: Barbed Carver
    pick_rate: 0.11
    win_rate: 0.46
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.24
      win_rate: 0.55
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.57
  - name: Shifter's Shield
    pick_rate: 0.1
    win_rate: 0.66
    alternates:
    - name: Barbed Carver
      pick_rate: 0.21
      win_rate: 0.53
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.36
  - name: The Reaper
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.6
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.55
  - name: Heartseeker
    pick_rate: 0.11
    win_rate: 0.62
    alternates:
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.41
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.6
  - name: Titan's Bane
    pick_rate: 0.06
    win_rate: 0.72
    alternates:
    - name: Heartseeker
      pick_rate: 0.05
      win_rate: 0.6
    - name: Lucerne Hammer
      pick_rate: 0.05
      win_rate: 0.47
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.23
    win_rate: 0.55
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-09-21'
  god_win_rate: 0.5376782077393075
  god_matches_won: 264
  god_matches_played: 491
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-21'
  god_matches_analyzed: 15551
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Transcendence
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
    this god: Berserker''s Shield, Amanita Charm, Golden Blade, Runeforged Hammer,
    Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow,
    Toxic Blade, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda,
    Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of
    the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.14
      fit: 0.4
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.29
      fit: 0.37
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.54
      pick: 0.19
      fit: 0.2
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.66
      pick: 0.16
      fit: 0.32
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.62
      pick: 0.24
      fit: 0.54
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.72
      pick: 0.18
      fit: 0.44
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Berserker's Shield
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Shifter's Shield
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Berserker''s
    Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged Hammer,
    Hydra''s Lament, Golden Blade, Freya''s Tears, Kinetic Cuirass, Lernaean Bow,
    Tyrfing, Shield Splitter, Tekko-Kagi, Eye of the Storm, Avenging Blade, Silverbranch
    Bow, Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, Toxic
    Blade, Deathbringer, Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.29
      fit: 0.41
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.14
      fit: 0.27
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.66
      pick: 0.16
      fit: 0.21
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.62
      pick: 0.24
      fit: 0.53
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.72
      pick: 0.18
      fit: 0.37
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Heartseeker
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
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Riptalon, Freya''s Tears, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean Bow,
    Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda, Tekko-Kagi,
    Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Hydra''s Lament,
    Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.57
      pick: 0.14
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.29
      fit: 0.32
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.66
      pick: 0.16
      fit: 0.4
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.62
      pick: 0.24
      fit: 0.5
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.72
      pick: 0.18
      fit: 0.4
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Shifter's Shield
  - Transcendence
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
    for this god: Berserker''s Shield, Avenging Blade, Amanita Charm, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged Hammer,
    Screeching Gargoyle, Void Shield, Kinetic Cuirass, Void Stone, Genji''s Guard,
    Breastplate of Valor, Lernaean Bow, Tyrfing, Freya''s Tears, Shield Splitter,
    Riptalon, Hydra''s Lament, Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.14
      fit: 0.33
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.29
      fit: 0.48
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.54
      pick: 0.19
      fit: 0.16
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.66
      pick: 0.16
      fit: 0.26
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.62
      pick: 0.24
      fit: 0.65
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.72
      pick: 0.18
      fit: 0.55
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Shifter's Shield
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Golden Blade, Riptalon, Tyrfing,
    Silverbranch Bow, Kinetic Cuirass, Runeforged Hammer, Toxic Blade, Genji''s Guard,
    Lernaean Bow, Breastplate of Valor, Freya''s Tears, Pharaoh''s Curse, Tekko-Kagi,
    Shogun''s Ofuda, Shield Splitter, Hydra''s Lament, Daybreak Gavel, Eye of the
    Storm, Avenging Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence,
    Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.29
      fit: 0.24
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.14
      fit: 0.38
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.66
      pick: 0.16
      fit: 0.24
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.51
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.72
      pick: 0.18
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Shifter's Shield
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Breastplate of Valor
  - Shifter's Shield
  - Titan's Bane
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Genji''s Guard,
    Breastplate of Valor, Freya''s Tears, Amanita Charm, Hydra''s Lament, Shield of
    the Phoenix, Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade,
    Silverbranch Bow, Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter,
    Daybreak Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Tekko-Kagi, Eye of
    the Storm, Gladiator''s Shield, Avenging Blade, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.14
      fit: 0.3
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.29
      fit: 0.45
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.33
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.66
      pick: 0.16
      fit: 0.24
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.72
      pick: 0.18
      fit: 0.28
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
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
    Underrated for this god: Berserker''s Shield, Amanita Charm, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow,
    Toxic Blade, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda,
    Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of
    the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.29
      fit: 0.37
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.14
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  starter: *id001
---
