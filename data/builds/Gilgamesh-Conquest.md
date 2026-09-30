---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.6
  aspect_win_rate: 0.54
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.28
    win_rate: 0.43
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.15
      win_rate: 0.56
    - name: Transcendence
      pick_rate: 0.11
      win_rate: 0.62
  - name: Barbed Carver
    pick_rate: 0.14
    win_rate: 0.51
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.21
      win_rate: 0.6
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.43
  - name: Berserker's Shield
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Barbed Carver
      pick_rate: 0.23
      win_rate: 0.54
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.65
  - name: The Reaper
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.5
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 0.33
  - name: Heartseeker
    pick_rate: 0.15
    win_rate: 0.65
    alternates:
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.78
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.5
  - name: Magi's Cloak
    pick_rate: 0.07
    win_rate: 0.69
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.6
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.31
    win_rate: 0.6
  - name: Hunter's Cowl
    pick_rate: 0.21
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-09-30'
  god_win_rate: 0.51
  god_matches_won: 153
  god_matches_played: 300
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-30'
  god_matches_analyzed: 9423
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Runeforged Hammer
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Runeforged Hammer
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
    Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s
    Guard, Breastplate of Valor, Eye of the Storm, Silverbranch Bow, Toxic Blade,
    Shifter''s Shield, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s
    Ofuda, The Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.71
      pick: 0.12
      fit: 0.4
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.44
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.65
      pick: 0.32
      fit: 0.54
    Titan's Bane:
      total: 0.59
      efficiency: 0.47
      win: 0.78
      pick: 0.15
      fit: 0.44
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Heartseeker
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
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Berserker''s
    Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged Hammer,
    Hydra''s Lament, Golden Blade, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield
    Splitter, Tekko-Kagi, Eye of the Storm, Transcendence, Avenging Blade, Silverbranch
    Bow, Shifter''s Shield, Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s
    Curse, The Crusher, Toxic Blade, Deathbringer, Eye of Providence, Shogun''s Ofuda,
    Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.71
      pick: 0.12
      fit: 0.27
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.2
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.65
      pick: 0.32
      fit: 0.53
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.78
      pick: 0.15
      fit: 0.37
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.21
  community_ordered:
  - Berserker's Shield
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - The Reaper
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Kinetic Cuirass
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
    this god: Berserker''s Shield, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Riptalon, Shield Splitter, Shifter''s Shield,
    Genji''s Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean
    Bow, Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda, Tekko-Kagi,
    Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Hydra''s Lament,
    Draconic Scale, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.71
      pick: 0.12
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.5
    The Reaper:
      total: 0.58
      efficiency: 0.5
      win: 0.67
      pick: 0.27
      fit: 0.6
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.65
      pick: 0.32
      fit: 0.5
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.78
      pick: 0.15
      fit: 0.4
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - The Reaper
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - The Reaper
  - Tekko-Kagi
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Avenging Blade
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Screeching Gargoyle, Void Shield, Kinetic Cuirass, Void Stone, The Crusher, Genji''s
    Guard, Breastplate of Valor, Lernaean Bow, Tyrfing, Shield Splitter, Riptalon,
    Hydra''s Lament, Eye of the Storm, Shifter''s Shield, Pharaoh''s Curse, Avatar''s
    Parashu, Freya''s Tears.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.71
      pick: 0.12
      fit: 0.33
    The Reaper:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.27
      fit: 0.45
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.6
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.65
      pick: 0.32
      fit: 0.65
    Titan's Bane:
      total: 0.61
      efficiency: 0.47
      win: 0.78
      pick: 0.15
      fit: 0.55
  community_ordered:
  - Berserker's Shield
  - The Reaper
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - The Reaper
  - Riptalon
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
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
    Lernaean Bow, Breastplate of Valor, Pharaoh''s Curse, Tekko-Kagi, Shogun''s Ofuda,
    Shifter''s Shield, Shield Splitter, Hydra''s Lament, Daybreak Gavel, Eye of the
    Storm, Avenging Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence,
    Stone of Binding, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.71
      pick: 0.12
      fit: 0.38
    The Reaper:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.27
      fit: 0.28
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.51
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.65
      pick: 0.32
      fit: 0.42
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.78
      pick: 0.15
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - The Reaper
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Hydra's Lament
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch Bow,
    Freya''s Tears, Shifter''s Shield, Lernaean Bow, Arondight, Tyrfing, Pharaoh''s
    Curse, Shield Splitter, Daybreak Gavel, Toxic Blade, Eye of Erebus, Shogun''s
    Ofuda, Tekko-Kagi, Eye of the Storm, Gladiator''s Shield, Avenging Blade, Erosion,
    Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.71
      pick: 0.12
      fit: 0.3
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.33
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.44
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.78
      pick: 0.15
      fit: 0.28
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Berserker's Shield
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
    Toxic Blade, Shifter''s Shield, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade,
    Shogun''s Ofuda, The Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion,
    Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.43
      pick: 0.28
      fit: 0.37
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.71
      pick: 0.12
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Tyrfing
  - Runeforged Hammer
  - The Reaper
  flex_slots:
  - Tyrfing
  - The Reaper
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Amanita Charm,
    Golden Blade, Runeforged Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield
    Splitter, Tekko-Kagi, Genji''s Guard, Breastplate of Valor, Freya''s Tears, Eye
    of the Storm, Silverbranch Bow, Toxic Blade, Shifter''s Shield, Hydra''s Lament,
    Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The Crusher, Daybreak Gavel,
    Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.43
      pick: 0.28
      fit: 0.37
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.71
      pick: 0.12
      fit: 0.4
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.61
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.27
      fit: 0.34
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - The Reaper
  swaps:
  - added: The Reaper
    removed: Kinetic Cuirass
    reason: community 67% win over 48 matches (vs 51% on this god), taking the model's
      weakest slot from Kinetic Cuirass
  starter: *id001
---
