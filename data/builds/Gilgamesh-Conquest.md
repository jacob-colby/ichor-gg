---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.7
  aspect_win_rate: 0.53
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.38
    win_rate: 0.58
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.29
      win_rate: 0.61
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.5
  - name: Jotunn's Revenge
    pick_rate: 0.27
    win_rate: 0.59
    alternates:
    - name: Barbed Carver
      pick_rate: 0.17
      win_rate: 0.46
    - name: Sanguine Lash
      pick_rate: 0.12
      win_rate: 0.48
  - name: Barbed Carver
    pick_rate: 0.26
    win_rate: 0.57
    alternates:
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.65
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 0.47
  - name: The Reaper
    pick_rate: 0.19
    win_rate: 0.47
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.3
  - name: Heartseeker
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.12
      win_rate: 0.57
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.58
  - name: Tekko-Kagi
    pick_rate: 0.11
    win_rate: 0.69
    alternates:
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.33
    - name: Magi's Cloak
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.28
    win_rate: 0.67
  - name: Bluestone Brooch
    pick_rate: 0.23
    win_rate: 0.55
  - name: Leather Cowl
    pick_rate: 0.16
    win_rate: 0.39
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-11'
  god_win_rate: 0.5566037735849056
  god_matches_won: 118
  god_matches_played: 212
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-11'
  god_matches_analyzed: 5242
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
  - Titan's Bane
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    of Valor, Hydra''s Lament, Eye of the Storm, Silverbranch Bow, Toxic Blade, Shifter''s
    Shield, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The Crusher, Daybreak
    Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix,
    Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.37
      fit: 0.37
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.47
      pick: 0.11
      fit: 0.4
    Tekko-Kagi:
      total: 0.58
      efficiency: 0.49
      win: 0.69
      pick: 0.34
      fit: 0.51
    Titan's Bane:
      total: 0.5
      efficiency: 0.47
      win: 0.58
      pick: 0.15
      fit: 0.44
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Berserker''s
    Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament,
    Runeforged Hammer, Golden Blade, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield
    Splitter, Eye of the Storm, Avenging Blade, Silverbranch Bow, Shifter''s Shield,
    Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, The Crusher,
    Toxic Blade, Transcendence, Deathbringer, Eye of Providence, Shogun''s Ofuda,
    Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.47
      pick: 0.11
      fit: 0.27
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.37
      fit: 0.41
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.2
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.69
      pick: 0.34
      fit: 0.39
    Titan's Bane:
      total: 0.49
      efficiency: 0.47
      win: 0.58
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
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Riptalon, Shield Splitter, Shifter''s Shield,
    Genji''s Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean
    Bow, Tyrfing, Pharaoh''s Curse, Hydra''s Lament, Phoenix Feather, Erosion, Shogun''s
    Ofuda, Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Draconic
    Scale, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.47
      pick: 0.11
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.37
      fit: 0.32
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.6
    Tekko-Kagi:
      total: 0.57
      efficiency: 0.49
      win: 0.69
      pick: 0.34
      fit: 0.45
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tekko-Kagi
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
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
    for this god: Berserker''s Shield, Avenging Blade, Amanita Charm, Stone of Binding,
    Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged Hammer, Screeching Gargoyle,
    Void Shield, Kinetic Cuirass, Void Stone, The Crusher, Genji''s Guard, Breastplate
    of Valor, Lernaean Bow, Tyrfing, Hydra''s Lament, Shield Splitter, Riptalon, Eye
    of the Storm, Shifter''s Shield, Pharaoh''s Curse, Avatar''s Parashu, Freya''s
    Tears.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.59
      pick: 0.37
      fit: 0.48
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.47
      pick: 0.11
      fit: 0.33
    Tekko-Kagi:
      total: 0.59
      efficiency: 0.49
      win: 0.69
      pick: 0.34
      fit: 0.6
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.3
      fit: 0.65
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.58
      pick: 0.15
      fit: 0.55
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
  - Heartseeker
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
  - Golden Blade
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Lernaean Bow, Breastplate of Valor, Pharaoh''s Curse, Shogun''s Ofuda, Hydra''s
    Lament, Shifter''s Shield, Shield Splitter, Daybreak Gavel, Eye of the Storm,
    Avenging Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence,
    Stone of Binding, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.37
      fit: 0.24
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.47
      pick: 0.11
      fit: 0.38
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.69
      pick: 0.34
      fit: 0.42
    Titan's Bane:
      total: 0.48
      efficiency: 0.47
      win: 0.58
      pick: 0.15
      fit: 0.32
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.5
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
  - Berserker's Shield
  - Amanita Charm
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Berserker''s Shield, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch Bow,
    Shifter''s Shield, Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield
    Splitter, Daybreak Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Eye of
    the Storm, Gladiator''s Shield, Avenging Blade, Erosion, Eye of Providence, Freya''s
    Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.47
      pick: 0.11
      fit: 0.3
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.37
      fit: 0.45
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.69
      pick: 0.34
      fit: 0.32
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.5
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
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.37
      fit: 0.37
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.47
      pick: 0.11
      fit: 0.4
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  starter: *id001
---
