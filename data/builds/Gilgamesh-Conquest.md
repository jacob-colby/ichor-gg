---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.69
  aspect_win_rate: 0.61
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.42
    win_rate: 0.73
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.27
      win_rate: 0.71
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.0
  - name: The Reaper
    pick_rate: 0.23
    win_rate: 1.0
    alternates:
    - name: Barbed Carver
      pick_rate: 0.15
      win_rate: 0.75
    - name: Dagger of Frenzy
      pick_rate: 0.08
      win_rate: 0.5
  - name: Barbed Carver
    pick_rate: 0.24
    win_rate: 1.0
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.67
    - name: Tekko-Kagi
      pick_rate: 0.08
      win_rate: 1.0
  - name: Sanguine Lash
    pick_rate: 0.3
    win_rate: 0.86
    alternates:
    - name: Heartseeker
      pick_rate: 0.22
      win_rate: 0.8
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.33
  - name: Brawler’s Beat Stick
    pick_rate: 0.24
    win_rate: 1.0
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.5
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.23
    win_rate: 1.0
    alternates:
    - name: Plated Metal
      pick_rate: 0.08
      win_rate: 0.0
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.46
    win_rate: 0.83
  - name: Leather Cowl
    pick_rate: 0.23
    win_rate: 0.33
  - name: Bluestone Brooch
    pick_rate: 0.08
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-21'
  god_win_rate: 0.5769230769230769
  god_matches_won: 15
  god_matches_played: 26
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - The Reaper
  - Tekko-Kagi
  - Freya's Tears
  - Titan's Bane
  flex_slots:
  - Berserker's Shield
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Tekko-Kagi, Berserker''s Shield, Amanita Charm, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Genji''s Guard,
    Breastplate of Valor, Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s
    Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The Crusher, Daybreak
    Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.66
      efficiency: 0.52
      win: 0.86
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.69
      efficiency: 0.68
      win: 0.86
      pick: 0.0
      fit: 0.4
    The Reaper:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.31
      fit: 0.34
    Tekko-Kagi:
      total: 0.7
      efficiency: 0.49
      win: 1.0
      pick: 0.12
      fit: 0.51
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.71
      fit: 0.21
    Titan's Bane:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.44
  community_ordered:
  - The Reaper
  - Tekko-Kagi
  - Freya's Tears
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tekko-Kagi
  - Freya's Tears
  - Titan's Bane
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Tekko-Kagi,
    Berserker''s Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Hydra''s Lament, Golden Blade, Kinetic Cuirass, Lernaean Bow, Tyrfing,
    Shield Splitter, Eye of the Storm, Avenging Blade, Silverbranch Bow, Dominance,
    Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, The Crusher, Toxic Blade,
    Transcendence, Deathbringer, Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.86
      pick: 0.0
      fit: 0.2
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.65
      win: 0.86
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.71
      pick: 0.27
      fit: 0.41
    Tekko-Kagi:
      total: 0.69
      efficiency: 0.49
      win: 1.0
      pick: 0.12
      fit: 0.39
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.71
      fit: 0.2
    Titan's Bane:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.37
  community_ordered:
  - Jotunn's Revenge
  - Tekko-Kagi
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - The Reaper
  - Tekko-Kagi
  - Freya's Tears
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Tekko-Kagi, Berserker''s Shield, Shield of the Phoenix,
    Kinetic Cuirass, Golden Blade, Runeforged Hammer, Riptalon, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean Bow,
    Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda, Toxic Blade,
    Eye of Providence, Avenging Blade, Silverbranch Bow, Hydra''s Lament, Draconic
    Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.69
      efficiency: 0.68
      win: 0.86
      pick: 0.0
      fit: 0.43
    The Reaper:
      total: 0.73
      efficiency: 0.5
      win: 1.0
      pick: 0.31
      fit: 0.6
    Tekko-Kagi:
      total: 0.69
      efficiency: 0.49
      win: 1.0
      pick: 0.12
      fit: 0.45
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.71
      fit: 0.27
    Titan's Bane:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.4
    Amanita Charm:
      total: 0.72
      efficiency: 0.65
      win: 0.86
      pick: 0.0
      fit: 0.7
  community_ordered:
  - The Reaper
  - Tekko-Kagi
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - The Reaper
  - Tekko-Kagi
  - Freya's Tears
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Tekko-Kagi, Berserker''s Shield, Avenging Blade, Amanita Charm,
    Stone of Binding, Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged Hammer,
    Screeching Gargoyle, Void Shield, Kinetic Cuirass, Void Stone, The Crusher, Genji''s
    Guard, Breastplate of Valor, Lernaean Bow, Tyrfing, Shield Splitter, Riptalon,
    Hydra''s Lament, Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.66
      efficiency: 0.49
      win: 0.86
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.68
      efficiency: 0.68
      win: 0.86
      pick: 0.0
      fit: 0.33
    The Reaper:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.31
      fit: 0.45
    Tekko-Kagi:
      total: 0.72
      efficiency: 0.49
      win: 1.0
      pick: 0.12
      fit: 0.6
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.71
      fit: 0.17
    Titan's Bane:
      total: 0.71
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.55
  community_ordered:
  - The Reaper
  - Tekko-Kagi
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - The Reaper
  - Tekko-Kagi
  - Freya's Tears
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Tekko-Kagi, Berserker''s Shield, Amanita Charm, Golden Blade, Riptalon,
    Tyrfing, Silverbranch Bow, Kinetic Cuirass, Runeforged Hammer, Toxic Blade, Genji''s
    Guard, Lernaean Bow, Breastplate of Valor, Pharaoh''s Curse, Shogun''s Ofuda,
    Shield Splitter, Hydra''s Lament, Daybreak Gavel, Eye of the Storm, Avenging Blade,
    Dominance, Erosion, Shield of the Phoenix, Eye of Providence, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.65
      efficiency: 0.52
      win: 0.86
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.68
      efficiency: 0.68
      win: 0.86
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.31
      fit: 0.28
    Tekko-Kagi:
      total: 0.69
      efficiency: 0.49
      win: 1.0
      pick: 0.12
      fit: 0.42
    Freya's Tears:
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.71
      fit: 0.16
    Titan's Bane:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.32
  community_ordered:
  - The Reaper
  - Tekko-Kagi
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Tekko-Kagi
  - Freya's Tears
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
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Tekko-Kagi, Berserker''s Shield, Genji''s
    Guard, Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix,
    Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch
    Bow, Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak
    Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Eye of the Storm, Gladiator''s
    Shield, Avenging Blade, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.86
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.67
      efficiency: 0.68
      win: 0.86
      pick: 0.0
      fit: 0.3
    Breastplate of Valor:
      total: 0.66
      efficiency: 0.65
      win: 0.86
      pick: 0.0
      fit: 0.33
    Tekko-Kagi:
      total: 0.67
      efficiency: 0.49
      win: 1.0
      pick: 0.12
      fit: 0.32
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 0.71
      fit: 0.39
    Titan's Bane:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.25
      fit: 0.28
  community_ordered:
  - Tekko-Kagi
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
    Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The Crusher,
    Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of
    the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.66
      efficiency: 0.52
      win: 0.86
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.69
      efficiency: 0.68
      win: 0.86
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.71
      pick: 0.27
      fit: 0.37
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.56
      win: 0.86
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.65
      efficiency: 0.57
      win: 0.86
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.66
      efficiency: 0.65
      win: 0.86
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
