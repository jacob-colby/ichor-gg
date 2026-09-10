---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.73
  aspect_win_rate: 0.72
  slot_order:
  - name: Transcendence
    pick_rate: 0.35
    win_rate: 0.86
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.3
      win_rate: 0.58
    - name: Golden Blade
      pick_rate: 0.1
      win_rate: 0.75
  - name: Jotunn's Revenge
    pick_rate: 0.38
    win_rate: 0.87
    alternates:
    - name: Transcendence
      pick_rate: 0.18
      win_rate: 0.71
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 1.0
  - name: Barbed Carver
    pick_rate: 0.43
    win_rate: 0.76
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.67
    - name: The Crusher
      pick_rate: 0.13
      win_rate: 0.8
  - name: The Crusher
    pick_rate: 0.28
    win_rate: 0.64
    alternates:
    - name: The Reaper
      pick_rate: 0.15
      win_rate: 1.0
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 1.0
  - name: Heartseeker
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: The Crusher
      pick_rate: 0.13
      win_rate: 1.0
    - name: Blinking Abyss
      pick_rate: 0.11
      win_rate: 0.5
  - name: Titan's Bane
    pick_rate: 0.18
    win_rate: 1.0
    alternates:
    - name: Veve Charm
      pick_rate: 0.09
      win_rate: 0.5
    - name: Draconic Scale
      pick_rate: 0.09
      win_rate: 0.5
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.5
    win_rate: 0.7
  - name: Bluestone Brooch
    pick_rate: 0.2
    win_rate: 0.88
  - name: Leather Cowl
    pick_rate: 0.1
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-09-10'
  god_win_rate: 0.7
  god_matches_won: 28
  god_matches_played: 40
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Transcendence
  - The Reaper
  - Titan's Bane
  flex_slots:
  - Transcendence
  - Golden Blade
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
    this god: Berserker''s Shield, Golden Blade, Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow,
    Toxic Blade, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda,
    Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of
    the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.61
      efficiency: 0.52
      win: 0.75
      pick: 0.1
      fit: 0.6
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.72
      win: 0.87
      pick: 0.52
      fit: 0.37
    Berserker's Shield:
      total: 0.75
      efficiency: 0.68
      win: 1.0
      pick: 0.11
      fit: 0.4
    Transcendence:
      total: 0.62
      efficiency: 0.53
      win: 0.86
      pick: 0.35
      fit: 0.2
    The Reaper:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.34
    Titan's Bane:
      total: 0.71
      efficiency: 0.47
      win: 1.0
      pick: 0.55
      fit: 0.44
  community_ordered:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Transcendence
  - The Reaper
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
  - Transcendence
  - The Reaper
  - Titan's Bane
  flex_slots:
  - Transcendence
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
    Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Golden Blade, Runeforged
    Hammer, Hydra''s Lament, Freya''s Tears, Kinetic Cuirass, Lernaean Bow, Tyrfing,
    Shield Splitter, Tekko-Kagi, Eye of the Storm, Avenging Blade, Silverbranch Bow,
    Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, Toxic Blade,
    Deathbringer, Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.75
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.73
      efficiency: 0.72
      win: 0.87
      pick: 0.52
      fit: 0.41
    Berserker's Shield:
      total: 0.73
      efficiency: 0.68
      win: 1.0
      pick: 0.11
      fit: 0.27
    Transcendence:
      total: 0.62
      efficiency: 0.53
      win: 0.86
      pick: 0.35
      fit: 0.22
    The Reaper:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.27
    Titan's Bane:
      total: 0.7
      efficiency: 0.47
      win: 1.0
      pick: 0.55
      fit: 0.37
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Transcendence
  - The Reaper
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Transcendence
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
    this god: Berserker''s Shield, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Riptalon, Freya''s Tears, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean Bow,
    Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda, Tekko-Kagi,
    Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Hydra''s Lament.'
  slot_scores:
    Berserker's Shield:
      total: 0.76
      efficiency: 0.68
      win: 1.0
      pick: 0.11
      fit: 0.43
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.72
      win: 0.87
      pick: 0.52
      fit: 0.32
    Transcendence:
      total: 0.61
      efficiency: 0.53
      win: 0.86
      pick: 0.35
      fit: 0.17
    The Reaper:
      total: 0.73
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.6
    Titan's Bane:
      total: 0.7
      efficiency: 0.47
      win: 1.0
      pick: 0.55
      fit: 0.4
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Transcendence
  - The Reaper
  - Titan's Bane
  flex_slots:
  - Transcendence
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
    for this god: Berserker''s Shield, Avenging Blade, Amanita Charm, Golden Blade,
    Tekko-Kagi, Stone of Binding, Silverbranch Bow, Toxic Blade, Runeforged Hammer,
    Screeching Gargoyle, Void Shield, Kinetic Cuirass, Void Stone, Genji''s Guard,
    Breastplate of Valor, Lernaean Bow, Tyrfing, Freya''s Tears, Shield Splitter,
    Riptalon, Hydra''s Lament, Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.61
      efficiency: 0.49
      win: 0.75
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.72
      win: 0.87
      pick: 0.52
      fit: 0.48
    Berserker's Shield:
      total: 0.74
      efficiency: 0.68
      win: 1.0
      pick: 0.11
      fit: 0.33
    Transcendence:
      total: 0.61
      efficiency: 0.53
      win: 0.86
      pick: 0.35
      fit: 0.16
    The Reaper:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.45
    Titan's Bane:
      total: 0.73
      efficiency: 0.47
      win: 1.0
      pick: 0.55
      fit: 0.55
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Transcendence
  - The Reaper
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - The Reaper
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
    this god: Berserker''s Shield, Golden Blade, Amanita Charm, Riptalon, Tyrfing,
    Silverbranch Bow, Kinetic Cuirass, Runeforged Hammer, Toxic Blade, Genji''s Guard,
    Lernaean Bow, Breastplate of Valor, Freya''s Tears, Pharaoh''s Curse, Tekko-Kagi,
    Shogun''s Ofuda, Shield Splitter, Hydra''s Lament, Daybreak Gavel, Eye of the
    Storm, Avenging Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence,
    Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.61
      efficiency: 0.52
      win: 0.75
      pick: 0.1
      fit: 0.56
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.72
      win: 0.87
      pick: 0.52
      fit: 0.24
    Berserker's Shield:
      total: 0.75
      efficiency: 0.68
      win: 1.0
      pick: 0.11
      fit: 0.38
    The Reaper:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.25
      fit: 0.28
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.75
      pick: 0.0
      fit: 0.51
    Titan's Bane:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.55
      fit: 0.32
  community_ordered:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - The Reaper
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Breastplate of Valor
  - The Reaper
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
    the Phoenix, Kinetic Cuirass, Golden Blade, Screeching Gargoyle, Runeforged Hammer,
    Silverbranch Bow, Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter,
    Daybreak Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Tekko-Kagi, Eye of
    the Storm, Gladiator''s Shield, Avenging Blade, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.75
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.74
      efficiency: 0.68
      win: 1.0
      pick: 0.11
      fit: 0.3
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.72
      win: 0.87
      pick: 0.52
      fit: 0.45
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.33
    The Reaper:
      total: 0.66
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.18
    Titan's Bane:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.55
      fit: 0.28
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
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
      total: 0.61
      efficiency: 0.52
      win: 0.75
      pick: 0.1
      fit: 0.6
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.72
      win: 0.87
      pick: 0.52
      fit: 0.37
    Berserker's Shield:
      total: 0.75
      efficiency: 0.68
      win: 1.0
      pick: 0.11
      fit: 0.4
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.6
      efficiency: 0.57
      win: 0.75
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  starter: *id001
---
