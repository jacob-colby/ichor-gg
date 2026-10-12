---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.71
  aspect_win_rate: 0.53
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.39
    win_rate: 0.58
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.28
      win_rate: 0.64
    - name: Hydra's Lament
      pick_rate: 0.12
      win_rate: 0.44
  - name: Jotunn's Revenge
    pick_rate: 0.29
    win_rate: 0.54
    alternates:
    - name: Barbed Carver
      pick_rate: 0.18
      win_rate: 0.53
    - name: Sanguine Lash
      pick_rate: 0.12
      win_rate: 0.53
  - name: Barbed Carver
    pick_rate: 0.28
    win_rate: 0.54
    alternates:
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.61
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.52
  - name: The Reaper
    pick_rate: 0.21
    win_rate: 0.46
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.49
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.36
  - name: Heartseeker
    pick_rate: 0.13
    win_rate: 0.43
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.12
      win_rate: 0.55
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.63
  - name: Tekko-Kagi
    pick_rate: 0.1
    win_rate: 0.69
    alternates:
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.27
    - name: Magi's Cloak
      pick_rate: 0.06
      win_rate: 0.4
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.28
    win_rate: 0.65
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.54
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-12'
  god_win_rate: 0.5636363636363636
  god_matches_won: 155
  god_matches_played: 275
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-12'
  god_matches_analyzed: 6672
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
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
    this god: Berserker''s Shield, Amanita Charm, Golden Blade, Runeforged Hammer,
    Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Silverbranch Bow, Toxic Blade, Shifter''s Shield,
    Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The Crusher, Daybreak Gavel,
    Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix, Hydra''s
    Lament, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.4
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.12
      fit: 0.4
    Tekko-Kagi:
      total: 0.57
      efficiency: 0.49
      win: 0.69
      pick: 0.31
      fit: 0.51
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.44
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
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
  - Breastplate of Valor
  - Tekko-Kagi
  - Titan's Bane
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Berserker''s
    Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged Hammer,
    Golden Blade, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield Splitter, Eye of
    the Storm, Avenging Blade, Silverbranch Bow, Shifter''s Shield, Dominance, Daybreak
    Gavel, Shield of the Phoenix, Pharaoh''s Curse, The Crusher, Hydra''s Lament,
    Toxic Blade, Transcendence, Deathbringer, Eye of Providence, Shogun''s Ofuda,
    Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.12
      fit: 0.27
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.54
      pick: 0.4
      fit: 0.41
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.2
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.69
      pick: 0.31
      fit: 0.39
    Titan's Bane:
      total: 0.51
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.37
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tekko-Kagi
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Tekko-Kagi
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Titan's Bane
  - Shield of the Phoenix
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Riptalon, Shield Splitter, Shifter''s Shield,
    Genji''s Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean
    Bow, Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda, Toxic
    Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Draconic Scale, Hydra''s
    Lament, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.12
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.4
      fit: 0.32
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.6
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.69
      pick: 0.31
      fit: 0.45
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.4
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tekko-Kagi
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
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
    for this god: Berserker''s Shield, Avenging Blade, Amanita Charm, Stone of Binding,
    Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged Hammer, Screeching Gargoyle,
    Void Shield, Kinetic Cuirass, Void Stone, The Crusher, Genji''s Guard, Breastplate
    of Valor, Lernaean Bow, Tyrfing, Shield Splitter, Riptalon, Eye of the Storm,
    Shifter''s Shield, Pharaoh''s Curse, Avatar''s Parashu, Hydra''s Lament, Freya''s
    Tears.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.54
      pick: 0.4
      fit: 0.48
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.12
      fit: 0.33
    Tekko-Kagi:
      total: 0.59
      efficiency: 0.49
      win: 0.69
      pick: 0.31
      fit: 0.6
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.55
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
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
    this god: Berserker''s Shield, Amanita Charm, Golden Blade, Riptalon, Tyrfing,
    Silverbranch Bow, Kinetic Cuirass, Runeforged Hammer, Toxic Blade, Genji''s Guard,
    Lernaean Bow, Breastplate of Valor, Pharaoh''s Curse, Shogun''s Ofuda, Shifter''s
    Shield, Shield Splitter, Daybreak Gavel, Eye of the Storm, Avenging Blade, Dominance,
    Erosion, Shield of the Phoenix, Eye of Providence, Stone of Binding, Hydra''s
    Lament, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.54
      pick: 0.4
      fit: 0.24
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.12
      fit: 0.38
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.69
      pick: 0.31
      fit: 0.42
    Titan's Bane:
      total: 0.5
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.32
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Breastplate of Valor
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Screeching
    Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch Bow, Shifter''s Shield,
    Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Hydra''s Lament, Shield Splitter,
    Daybreak Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Eye of the Storm,
    Gladiator''s Shield, Avenging Blade, Erosion, Eye of Providence, Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.12
      fit: 0.3
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.54
      pick: 0.4
      fit: 0.45
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.33
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.69
      pick: 0.31
      fit: 0.32
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tekko-Kagi
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
    Ofuda, The Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.4
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.12
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  starter: *id001
---
