---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.69
  aspect_win_rate: 0.56
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.41
    win_rate: 0.61
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.26
      win_rate: 0.65
    - name: Hydra's Lament
      pick_rate: 0.12
      win_rate: 0.46
  - name: Jotunn's Revenge
    pick_rate: 0.29
    win_rate: 0.55
    alternates:
    - name: Barbed Carver
      pick_rate: 0.17
      win_rate: 0.55
    - name: Sanguine Lash
      pick_rate: 0.12
      win_rate: 0.6
  - name: Barbed Carver
    pick_rate: 0.28
    win_rate: 0.56
    alternates:
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.59
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 0.54
  - name: The Reaper
    pick_rate: 0.22
    win_rate: 0.51
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.51
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 0.67
  - name: Blinking Abyss
    pick_rate: 0.13
    win_rate: 0.58
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.42
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.63
  - name: Tekko-Kagi
    pick_rate: 0.11
    win_rate: 0.64
    alternates:
    - name: Magi's Cloak
      pick_rate: 0.07
      win_rate: 0.36
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.25
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.32
    win_rate: 0.67
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.57
  - name: Leather Cowl
    pick_rate: 0.15
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-14'
  god_win_rate: 0.5787965616045845
  god_matches_won: 202
  god_matches_played: 349
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-14'
  god_matches_analyzed: 8861
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
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
    this god: Kinetic Cuirass, Berserker''s Shield, Amanita Charm, Golden Blade, Titan''s
    Bane, Runeforged Hammer, Tyrfing, Lernaean Bow, Shield Splitter, Genji''s Guard,
    Breastplate of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow, Toxic
    Blade, Shifter''s Shield, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The
    Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix, Hydra''s Lament.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.4
      fit: 0.37
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.11
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.08
      fit: 0.42
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.64
      pick: 0.34
      fit: 0.51
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Tekko-Kagi
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Breastplate of Valor
  - Kinetic Cuirass
  - Tekko-Kagi
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Kinetic
    Cuirass, Berserker''s Shield, Titan''s Bane, Amanita Charm, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Golden Blade, Freya''s Tears, Lernaean Bow, Tyrfing,
    Shield Splitter, Eye of the Storm, Avenging Blade, Silverbranch Bow, Shifter''s
    Shield, Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, The
    Crusher, Toxic Blade, Transcendence, Deathbringer, Eye of Providence, Shogun''s
    Ofuda, Hydra''s Lament.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.54
      pick: 0.11
      fit: 0.27
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.4
      fit: 0.41
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.2
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.67
      pick: 0.08
      fit: 0.31
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.64
      pick: 0.34
      fit: 0.39
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tekko-Kagi
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Tekko-Kagi
  - Shield of the Phoenix
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
    this god: Amanita Charm, Kinetic Cuirass, Berserker''s Shield, Shield of the Phoenix,
    Golden Blade, Runeforged Hammer, Riptalon, Freya''s Tears, Shield Splitter, Shifter''s
    Shield, Genji''s Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm,
    Lernaean Bow, Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda,
    Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Draconic Scale,
    Hydra''s Lament.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.11
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.4
      fit: 0.32
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.08
      fit: 0.5
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.6
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.64
      pick: 0.34
      fit: 0.45
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tekko-Kagi
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Tekko-Kagi
  - Titan's Bane
  flex_slots:
  - Berserker's Shield
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
    for this god: Kinetic Cuirass, Titan''s Bane, Berserker''s Shield, Avenging Blade,
    Amanita Charm, Stone of Binding, Silverbranch Bow, Golden Blade, Toxic Blade,
    Runeforged Hammer, Screeching Gargoyle, Void Shield, Void Stone, The Crusher,
    Genji''s Guard, Breastplate of Valor, Lernaean Bow, Tyrfing, Freya''s Tears, Shield
    Splitter, Riptalon, Eye of the Storm, Shifter''s Shield, Pharaoh''s Curse, Avatar''s
    Parashu, Hydra''s Lament.'
  slot_scores:
    Avenging Blade:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.55
      pick: 0.4
      fit: 0.48
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.11
      fit: 0.33
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.67
      pick: 0.08
      fit: 0.36
    Tekko-Kagi:
      total: 0.57
      efficiency: 0.49
      win: 0.64
      pick: 0.34
      fit: 0.6
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.13
      fit: 0.55
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Tekko-Kagi
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Berserker''s Shield, Amanita Charm, Golden Blade, Riptalon,
    Tyrfing, Silverbranch Bow, Runeforged Hammer, Toxic Blade, Genji''s Guard, Lernaean
    Bow, Breastplate of Valor, Freya''s Tears, Pharaoh''s Curse, Shogun''s Ofuda,
    Shifter''s Shield, Shield Splitter, Daybreak Gavel, Eye of the Storm, Avenging
    Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence, Stone of
    Binding, Hydra''s Lament.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.4
      fit: 0.24
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.11
      fit: 0.38
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.67
      pick: 0.08
      fit: 0.34
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.64
      pick: 0.34
      fit: 0.42
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Tekko-Kagi
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Berserker''s Shield,
    Genji''s Guard, Breastplate of Valor, Freya''s Tears, Amanita Charm, Shield of
    the Phoenix, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch
    Bow, Shifter''s Shield, Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield
    Splitter, Daybreak Gavel, Toxic Blade, Hydra''s Lament, Eye of Erebus, Shogun''s
    Ofuda, Eye of the Storm, Gladiator''s Shield, Avenging Blade, Erosion, Eye of
    Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.54
      pick: 0.11
      fit: 0.3
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.4
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.67
      pick: 0.08
      fit: 0.34
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Genji''s Guard,
    Breastplate of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow, Toxic
    Blade, Shifter''s Shield, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s
    Ofuda, Titan''s Bane, The Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion,
    Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.4
      fit: 0.37
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.11
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.08
      fit: 0.42
    Runeforged Hammer:
      total: 0.51
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
  - Kinetic Cuirass
  starter: *id001
---
