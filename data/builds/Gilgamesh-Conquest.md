---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.66
  aspect_win_rate: 0.61
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.4
    win_rate: 0.68
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.27
      win_rate: 0.53
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 1.0
  - name: Barbed Carver
    pick_rate: 0.21
    win_rate: 0.62
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.21
      win_rate: 0.69
    - name: Brawler’s Beat Stick
      pick_rate: 0.16
      win_rate: 0.8
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Barbed Carver
      pick_rate: 0.22
      win_rate: 0.69
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.67
  - name: The Reaper
    pick_rate: 0.23
    win_rate: 0.69
    alternates:
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.5
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.6
  - name: Blinking Abyss
    pick_rate: 0.18
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.83
    - name: Ancile
      pick_rate: 0.1
      win_rate: 0.6
  - name: Tekko-Kagi
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Skeggox
      pick_rate: 0.09
      win_rate: 0.33
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.26
    win_rate: 0.88
  - name: Leather Cowl
    pick_rate: 0.23
    win_rate: 0.43
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-08'
  god_win_rate: 0.6129032258064516
  god_matches_won: 38
  god_matches_played: 62
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Berserker''s Shield, Amanita Charm, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Genji''s Guard,
    Breastplate of Valor, Eye of the Storm, Silverbranch Bow, Toxic Blade, Shifter''s
    Shield, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The Crusher, Daybreak
    Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.68
      pick: 0.4
      fit: 0.37
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.2
    Hydra's Lament:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.08
      fit: 0.33
    Heartseeker:
      total: 0.63
      efficiency: 0.47
      win: 0.83
      pick: 0.26
      fit: 0.54
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  flex_slots:
  - The Reaper
  - Transcendence
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Berserker''s Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Golden Blade, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield
    Splitter, Eye of the Storm, Avenging Blade, Silverbranch Bow, Shifter''s Shield,
    Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, The Crusher,
    Toxic Blade, Transcendence, Deathbringer, Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.68
      pick: 0.4
      fit: 0.41
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.71
      efficiency: 0.54
      win: 1.0
      pick: 0.08
      fit: 0.41
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.69
      pick: 0.38
      fit: 0.27
    Heartseeker:
      total: 0.63
      efficiency: 0.47
      win: 0.83
      pick: 0.26
      fit: 0.53
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - The Reaper
  - Berserker's Shield
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
    this god: Hydra''s Lament, Amanita Charm, Berserker''s Shield, Shield of the Phoenix,
    Kinetic Cuirass, Golden Blade, Runeforged Hammer, Riptalon, Shield Splitter, Shifter''s
    Shield, Genji''s Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm,
    Lernaean Bow, Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda,
    Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.68
      pick: 0.4
      fit: 0.32
    Hydra's Lament:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.08
      fit: 0.3
    The Reaper:
      total: 0.59
      efficiency: 0.5
      win: 0.69
      pick: 0.38
      fit: 0.6
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.83
      pick: 0.26
      fit: 0.5
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  flex_slots:
  - Berserker's Shield
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Hydra''s Lament, Berserker''s Shield, Avenging Blade, Amanita Charm,
    Stone of Binding, Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged Hammer,
    Screeching Gargoyle, Void Shield, Kinetic Cuirass, Void Stone, The Crusher, Genji''s
    Guard, Breastplate of Valor, Lernaean Bow, Tyrfing, Shield Splitter, Riptalon,
    Eye of the Storm, Shifter''s Shield, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.68
      pick: 0.4
      fit: 0.48
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.16
    Hydra's Lament:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.08
      fit: 0.29
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.69
      pick: 0.38
      fit: 0.45
    Heartseeker:
      total: 0.65
      efficiency: 0.47
      win: 0.83
      pick: 0.26
      fit: 0.65
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Hydra's Lament
  - Riptalon
  - Heartseeker
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
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Berserker''s Shield, Amanita Charm, Golden Blade, Riptalon,
    Tyrfing, Silverbranch Bow, Kinetic Cuirass, Runeforged Hammer, Toxic Blade, Genji''s
    Guard, Lernaean Bow, Breastplate of Valor, Pharaoh''s Curse, Shogun''s Ofuda,
    Shifter''s Shield, Shield Splitter, Daybreak Gavel, Eye of the Storm, Avenging
    Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence, Stone of
    Binding.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.68
      pick: 0.4
      fit: 0.24
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.38
    Hydra's Lament:
      total: 0.68
      efficiency: 0.54
      win: 1.0
      pick: 0.08
      fit: 0.23
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.51
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.83
      pick: 0.26
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Berserker's Shield
  - Transcendence
  - Hydra's Lament
  - Heartseeker
  flex_slots:
  - Genji's Guard
  - Transcendence
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Berserker''s Shield,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch Bow,
    Shifter''s Shield, Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield
    Splitter, Daybreak Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Eye of
    the Storm, Gladiator''s Shield, Avenging Blade, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.68
      pick: 0.4
      fit: 0.45
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.3
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.08
    Hydra's Lament:
      total: 0.71
      efficiency: 0.54
      win: 1.0
      pick: 0.08
      fit: 0.44
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.83
      pick: 0.26
      fit: 0.38
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
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
    Breastplate of Valor, Eye of the Storm, Silverbranch Bow, Toxic Blade, Shifter''s
    Shield, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The
    Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.68
      pick: 0.4
      fit: 0.37
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
