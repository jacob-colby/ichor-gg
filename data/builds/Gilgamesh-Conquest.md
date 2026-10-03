---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.61
  aspect_win_rate: 0.55
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.27
    win_rate: 0.44
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.17
      win_rate: 0.6
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.69
  - name: Barbed Carver
    pick_rate: 0.14
    win_rate: 0.51
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.21
      win_rate: 0.61
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.48
  - name: Berserker's Shield
    pick_rate: 0.08
    win_rate: 0.69
    alternates:
    - name: Barbed Carver
      pick_rate: 0.22
      win_rate: 0.55
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.53
  - name: The Reaper
    pick_rate: 0.17
    win_rate: 0.68
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.5
    - name: Berserker's Shield
      pick_rate: 0.06
      win_rate: 0.38
  - name: Heartseeker
    pick_rate: 0.17
    win_rate: 0.65
    alternates:
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.64
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.53
  - name: Magi's Cloak
    pick_rate: 0.09
    win_rate: 0.74
    alternates:
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.5
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.32
    win_rate: 0.59
  - name: Hunter's Cowl
    pick_rate: 0.19
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-03'
  god_win_rate: 0.5336426914153132
  god_matches_won: 230
  god_matches_played: 431
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-10-03'
  god_matches_analyzed: 12830
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Hydra's Lament
  - Magi's Cloak
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Heartseeker
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
    this god: Berserker''s Shield, Amanita Charm, Golden Blade, Hydra''s Lament, Runeforged
    Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow,
    Toxic Blade, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The Crusher, Daybreak
    Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix,
    Shifter''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.69
      pick: 0.12
      fit: 0.4
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.69
      pick: 0.11
      fit: 0.33
    Magi's Cloak:
      total: 0.56
      efficiency: 0.53
      win: 0.74
      pick: 0.28
      fit: 0.18
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.65
      pick: 0.37
      fit: 0.54
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Hydra's Lament
  - Magi's Cloak
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Hydra's Lament
  - Magi's Cloak
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Berserker''s
    Shield, Hydra''s Lament, Amanita Charm, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Golden Blade, Freya''s Tears, Kinetic Cuirass, Lernaean Bow,
    Tyrfing, Shield Splitter, Tekko-Kagi, Eye of the Storm, Avenging Blade, Silverbranch
    Bow, Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, The Crusher,
    Toxic Blade, Transcendence, Deathbringer, Eye of Providence, Shogun''s Ofuda,
    Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.64
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.69
      pick: 0.12
      fit: 0.27
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.69
      pick: 0.11
      fit: 0.41
    Magi's Cloak:
      total: 0.55
      efficiency: 0.53
      win: 0.74
      pick: 0.28
      fit: 0.12
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.65
      pick: 0.37
      fit: 0.53
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.21
  community_ordered:
  - Berserker's Shield
  - Hydra's Lament
  - Magi's Cloak
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Magi's Cloak
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Hydra''s Lament, Runeforged Hammer, Riptalon, Freya''s Tears, Shield
    Splitter, Genji''s Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm,
    Lernaean Bow, Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda,
    Tekko-Kagi, Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch Bow,
    Draconic Scale, Shifter''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.69
      pick: 0.12
      fit: 0.43
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.5
    Magi's Cloak:
      total: 0.57
      efficiency: 0.53
      win: 0.74
      pick: 0.28
      fit: 0.25
    The Reaper:
      total: 0.58
      efficiency: 0.5
      win: 0.68
      pick: 0.28
      fit: 0.6
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - Magi's Cloak
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Hydra's Lament
  - Magi's Cloak
  - The Reaper
  - Heartseeker
  flex_slots:
  - Magi's Cloak
  - Hydra's Lament
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
    for this god: Berserker''s Shield, Avenging Blade, Amanita Charm, Hydra''s Lament,
    Tekko-Kagi, Stone of Binding, Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged
    Hammer, Screeching Gargoyle, Void Shield, Kinetic Cuirass, Void Stone, The Crusher,
    Genji''s Guard, Breastplate of Valor, Lernaean Bow, Tyrfing, Freya''s Tears, Shield
    Splitter, Riptalon, Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu, Shifter''s
    Shield.'
  slot_scores:
    Avenging Blade:
      total: 0.56
      efficiency: 0.49
      win: 0.64
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.69
      pick: 0.12
      fit: 0.33
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.69
      pick: 0.11
      fit: 0.29
    Magi's Cloak:
      total: 0.56
      efficiency: 0.53
      win: 0.74
      pick: 0.28
      fit: 0.14
    The Reaper:
      total: 0.56
      efficiency: 0.5
      win: 0.68
      pick: 0.28
      fit: 0.45
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.65
      pick: 0.37
      fit: 0.65
  community_ordered:
  - Berserker's Shield
  - Hydra's Lament
  - Magi's Cloak
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Hydra's Lament
  - Magi's Cloak
  - The Reaper
  - Riptalon
  flex_slots:
  - Riptalon
  - Hydra's Lament
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Golden Blade, Riptalon, Hydra''s
    Lament, Tyrfing, Silverbranch Bow, Kinetic Cuirass, Runeforged Hammer, Toxic Blade,
    Genji''s Guard, Lernaean Bow, Breastplate of Valor, Freya''s Tears, Pharaoh''s
    Curse, Tekko-Kagi, Shogun''s Ofuda, Shield Splitter, Daybreak Gavel, Eye of the
    Storm, Avenging Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence,
    Stone of Binding, Shifter''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.69
      pick: 0.12
      fit: 0.38
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.69
      pick: 0.11
      fit: 0.23
    Magi's Cloak:
      total: 0.55
      efficiency: 0.53
      win: 0.74
      pick: 0.28
      fit: 0.14
    The Reaper:
      total: 0.55
      efficiency: 0.55
      win: 0.68
      pick: 0.28
      fit: 0.28
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.64
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Berserker's Shield
  - Hydra's Lament
  - Magi's Cloak
  - The Reaper
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Magi's Cloak
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Hydra''s Lament,
    Genji''s Guard, Breastplate of Valor, Freya''s Tears, Amanita Charm, Shield of
    the Phoenix, Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade,
    Silverbranch Bow, Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter,
    Daybreak Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Tekko-Kagi, Eye of
    the Storm, Gladiator''s Shield, Avenging Blade, Erosion, Eye of Providence, Shifter''s
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.69
      pick: 0.12
      fit: 0.3
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.33
    Magi's Cloak:
      total: 0.55
      efficiency: 0.53
      win: 0.74
      pick: 0.28
      fit: 0.13
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.69
      pick: 0.11
      fit: 0.44
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Berserker's Shield
  - Magi's Cloak
  - Hydra's Lament
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
      total: 0.56
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.27
      fit: 0.37
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.69
      pick: 0.12
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.64
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.64
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
  - Magi's Cloak
  - Tyrfing
  - The Reaper
  flex_slots:
  - The Reaper
  - Magi's Cloak
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
      total: 0.56
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.27
      fit: 0.37
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.69
      pick: 0.12
      fit: 0.4
    Magi's Cloak:
      total: 0.56
      efficiency: 0.53
      win: 0.74
      pick: 0.28
      fit: 0.18
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.64
      pick: 0.0
      fit: 0.56
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.68
      pick: 0.28
      fit: 0.34
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Magi's Cloak
  - The Reaper
  swaps:
  - added: Magi's Cloak
    removed: Kinetic Cuirass
    reason: community 74% win over 39 matches (vs 53% on this god), taking the model's
      weakest slot from Kinetic Cuirass
  - added: The Reaper
    removed: Runeforged Hammer
    reason: community 68% win over 73 matches (vs 53% on this god), taking the model's
      weakest slot from Runeforged Hammer
  starter: *id001
---
