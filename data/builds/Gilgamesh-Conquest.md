---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.74
  aspect_win_rate: 0.56
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.36
    win_rate: 0.58
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.26
      win_rate: 0.58
    - name: Barbed Carver
      pick_rate: 0.11
      win_rate: 0.5
  - name: Barbed Carver
    pick_rate: 0.15
    win_rate: 0.55
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.5
    - name: The Reaper
      pick_rate: 0.11
      win_rate: 0.88
  - name: Berserker's Shield
    pick_rate: 0.09
    win_rate: 0.0
    alternates:
    - name: Barbed Carver
      pick_rate: 0.11
      win_rate: 1.0
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.6
  - name: Heartseeker
    pick_rate: 0.24
    win_rate: 0.63
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.12
      win_rate: 0.88
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.5
  - name: Brawler’s Beat Stick
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.56
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.33
    - name: Magi's Cloak
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.34
    win_rate: 0.56
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.63
  - name: Leather Cowl
    pick_rate: 0.19
    win_rate: 0.36
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-23'
  god_win_rate: 0.5068493150684932
  god_matches_won: 37
  god_matches_played: 73
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-23'
  god_matches_analyzed: 2743
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - Transcendence
  - The Reaper
  - Freya's Tears
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Golden Blade, Runeforged Hammer, Kinetic Cuirass, Tyrfing,
    Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate of Valor,
    Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s Lament, Pharaoh''s Curse,
    Avenging Blade, Shogun''s Ofuda, The Crusher, Daybreak Gavel, Deathbringer, Dominance,
    Erosion, Eye of Providence, Shield of the Phoenix, Titan''s Bane, Berserker''s
    Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.26
      fit: 0.37
    Brawler’s Beat Stick:
      total: 0.63
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.18
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.2
    The Reaper:
      total: 0.63
      efficiency: 0.5
      win: 0.88
      pick: 0.15
      fit: 0.34
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.31
      fit: 0.21
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.63
      pick: 0.4
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - The Reaper
  - Freya's Tears
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Jotunn's Revenge
  - The Reaper
  - Freya's Tears
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Hydra''s Lament,
    Golden Blade, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield Splitter, Tekko-Kagi,
    Eye of the Storm, Avenging Blade, Silverbranch Bow, Dominance, Daybreak Gavel,
    Shield of the Phoenix, Pharaoh''s Curse, The Crusher, Toxic Blade, Transcendence,
    Deathbringer, Eye of Providence, Shogun''s Ofuda, Titan''s Bane, Berserker''s
    Shield.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.63
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.12
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.26
      fit: 0.41
    The Reaper:
      total: 0.62
      efficiency: 0.5
      win: 0.88
      pick: 0.15
      fit: 0.27
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.31
      fit: 0.2
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.63
      pick: 0.4
      fit: 0.53
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - The Reaper
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - The Reaper
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Golden Blade,
    Runeforged Hammer, Riptalon, Shield Splitter, Genji''s Guard, Breastplate of Valor,
    Yogi''s Necklace, Eye of the Storm, Lernaean Bow, Tyrfing, Pharaoh''s Curse, Phoenix
    Feather, Erosion, Shogun''s Ofuda, Tekko-Kagi, Toxic Blade, Eye of Providence,
    Avenging Blade, Silverbranch Bow, Hydra''s Lament, Draconic Scale, Berserker''s
    Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.26
      fit: 0.32
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.25
    The Reaper:
      total: 0.67
      efficiency: 0.5
      win: 0.88
      pick: 0.15
      fit: 0.6
    Freya's Tears:
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.31
      fit: 0.27
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.4
      fit: 0.5
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - The Reaper
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - Freya's Tears
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, Amanita Charm, Tekko-Kagi, Stone of Binding, Silverbranch
    Bow, Golden Blade, Toxic Blade, Runeforged Hammer, Screeching Gargoyle, Void Shield,
    Kinetic Cuirass, Void Stone, The Crusher, Genji''s Guard, Breastplate of Valor,
    Lernaean Bow, Tyrfing, Shield Splitter, Riptalon, Hydra''s Lament, Eye of the
    Storm, Pharaoh''s Curse, Avatar''s Parashu, Titan''s Bane, Berserker''s Shield.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.63
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.14
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.58
      pick: 0.26
      fit: 0.48
    The Reaper:
      total: 0.65
      efficiency: 0.5
      win: 0.88
      pick: 0.15
      fit: 0.45
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.31
      fit: 0.17
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.63
      pick: 0.4
      fit: 0.65
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - The Reaper
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Brawler’s Beat Stick
  - Tyrfing
  - The Reaper
  - Freya's Tears
  - Riptalon
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Golden Blade, Riptalon, Tyrfing, Silverbranch Bow, Kinetic
    Cuirass, Runeforged Hammer, Toxic Blade, Genji''s Guard, Lernaean Bow, Breastplate
    of Valor, Pharaoh''s Curse, Tekko-Kagi, Shogun''s Ofuda, Shield Splitter, Hydra''s
    Lament, Daybreak Gavel, Eye of the Storm, Avenging Blade, Dominance, Erosion,
    Shield of the Phoenix, Eye of Providence, Stone of Binding, Berserker''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.56
    Brawler’s Beat Stick:
      total: 0.63
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.14
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.55
    The Reaper:
      total: 0.64
      efficiency: 0.55
      win: 0.88
      pick: 0.15
      fit: 0.28
    Freya's Tears:
      total: 0.7
      efficiency: 0.61
      win: 1.0
      pick: 0.31
      fit: 0.16
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Brawler’s Beat Stick
  - The Reaper
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Jotunn's Revenge
  - Breastplate of Valor
  - The Reaper
  - Freya's Tears
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic Cuirass, Screeching
    Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch Bow, Lernaean Bow, Arondight,
    Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak Gavel, Toxic Blade, Eye of
    Erebus, Shogun''s Ofuda, Tekko-Kagi, Eye of the Storm, Gladiator''s Shield, Avenging
    Blade, Erosion, Eye of Providence, Berserker''s Shield.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.63
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.13
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.26
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.33
    The Reaper:
      total: 0.6
      efficiency: 0.5
      win: 0.88
      pick: 0.15
      fit: 0.18
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.31
      fit: 0.39
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - The Reaper
  - Freya's Tears
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
    Underrated for this god: Berserker''s Shield, Amanita Charm, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s
    Guard, Breastplate of Valor, Eye of the Storm, Silverbranch Bow, Toxic Blade,
    Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, Titan''s Bane,
    The Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.31
      efficiency: 0.68
      win: 0.0
      pick: 0.14
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.26
      fit: 0.37
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  starter: *id001
---
