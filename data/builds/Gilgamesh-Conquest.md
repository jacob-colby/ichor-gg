---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.59
  aspect_win_rate: 0.55
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.44
    win_rate: 0.6
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.21
      win_rate: 0.29
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 1.0
  - name: Barbed Carver
    pick_rate: 0.24
    win_rate: 0.38
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.15
      win_rate: 0.8
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.25
  - name: The Reaper
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: Barbed Carver
      pick_rate: 0.19
      win_rate: 0.83
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.33
  - name: Titan's Bane
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: The Reaper
      pick_rate: 0.25
      win_rate: 0.75
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.0
  - name: Heartseeker
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Ancile
      pick_rate: 0.07
      win_rate: 1.0
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.0
  - name: Skeggox
    pick_rate: 0.11
    win_rate: 0.0
    alternates:
    - name: Lucerne Hammer
      pick_rate: 0.11
      win_rate: 1.0
    - name: Brawler’s Beat Stick
      pick_rate: 0.11
      win_rate: 0.5
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.24
    win_rate: 0.88
  - name: Leather Cowl
    pick_rate: 0.18
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-07'
  god_win_rate: 0.5588235294117647
  god_matches_won: 19
  god_matches_played: 34
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
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
  - Ancile
  - Heartseeker
  flex_slots:
  - Berserker's Shield
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Berserker''s Shield, Amanita Charm, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow,
    Toxic Blade, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, The Crusher, Daybreak
    Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.45
      efficiency: 0.68
      win: 0.33
      pick: 0.14
      fit: 0.4
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.6
      pick: 0.44
      fit: 0.37
    Transcendence:
      total: 0.38
      efficiency: 0.53
      win: 0.38
      pick: 0.0
      fit: 0.2
    Hydra's Lament:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.09
      fit: 0.33
    Ancile:
      total: 0.67
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.23
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.24
      fit: 0.54
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Ancile
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Ancile
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Berserker''s Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Golden Blade, Freya''s Tears, Kinetic Cuirass, Lernaean Bow,
    Tyrfing, Shield Splitter, Tekko-Kagi, Eye of the Storm, Avenging Blade, Silverbranch
    Bow, Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, The Crusher,
    Toxic Blade, Transcendence, Deathbringer, Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.43
      efficiency: 0.68
      win: 0.33
      pick: 0.14
      fit: 0.27
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.6
      pick: 0.44
      fit: 0.41
    Hydra's Lament:
      total: 0.71
      efficiency: 0.54
      win: 1.0
      pick: 0.09
      fit: 0.41
    Ancile:
      total: 0.66
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.15
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.24
      fit: 0.53
    Amanita Charm:
      total: 0.43
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.21
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Ancile
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Ancile
  - Heartseeker
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Amanita Charm, Berserker''s Shield, Shield of the Phoenix,
    Kinetic Cuirass, Golden Blade, Runeforged Hammer, Riptalon, Freya''s Tears, Shield
    Splitter, Genji''s Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm,
    The Reaper, Lernaean Bow, Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion,
    Shogun''s Ofuda, Tekko-Kagi, Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch
    Bow, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.44
      fit: 0.32
    Transcendence:
      total: 0.38
      efficiency: 0.53
      win: 0.38
      pick: 0.0
      fit: 0.17
    Hydra's Lament:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.09
      fit: 0.3
    Ancile:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.28
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.24
      fit: 0.5
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Ancile
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Ancile
  - Heartseeker
  flex_slots:
  - Avenging Blade
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Hydra''s Lament, Avenging Blade, Berserker''s Shield, Amanita Charm,
    Tekko-Kagi, Stone of Binding, Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged
    Hammer, Screeching Gargoyle, Void Shield, Kinetic Cuirass, Void Stone, The Crusher,
    Genji''s Guard, Breastplate of Valor, Lernaean Bow, Tyrfing, Freya''s Tears, Shield
    Splitter, Riptalon, Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu, The
    Reaper.'
  slot_scores:
    Avenging Blade:
      total: 0.45
      efficiency: 0.49
      win: 0.38
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.44
      fit: 0.48
    Transcendence:
      total: 0.38
      efficiency: 0.53
      win: 0.38
      pick: 0.0
      fit: 0.16
    Hydra's Lament:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.09
      fit: 0.29
    Ancile:
      total: 0.66
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.19
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.24
      fit: 0.65
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Ancile
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Hydra's Lament
  - Ancile
  - Riptalon
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
    this god: Hydra''s Lament, Berserker''s Shield, Amanita Charm, Golden Blade, Riptalon,
    Tyrfing, Silverbranch Bow, Kinetic Cuirass, Runeforged Hammer, Toxic Blade, Genji''s
    Guard, Lernaean Bow, Breastplate of Valor, Freya''s Tears, Pharaoh''s Curse, Tekko-Kagi,
    Shogun''s Ofuda, Shield Splitter, Daybreak Gavel, Eye of the Storm, Avenging Blade,
    The Reaper, Dominance, Erosion, Shield of the Phoenix, Eye of Providence, Stone
    of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.52
      win: 0.38
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.44
      fit: 0.24
    Berserker's Shield:
      total: 0.45
      efficiency: 0.68
      win: 0.33
      pick: 0.14
      fit: 0.38
    Hydra's Lament:
      total: 0.68
      efficiency: 0.54
      win: 1.0
      pick: 0.09
      fit: 0.23
    Ancile:
      total: 0.66
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.18
    Riptalon:
      total: 0.43
      efficiency: 0.51
      win: 0.38
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Hydra's Lament
  - Ancile
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Ancile
  - Heartseeker
  flex_slots:
  - Genji's Guard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Genji''s Guard, Breastplate
    of Valor, Freya''s Tears, Berserker''s Shield, Amanita Charm, Shield of the Phoenix,
    Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch
    Bow, Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak
    Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Tekko-Kagi, Eye of the Storm,
    Gladiator''s Shield, Avenging Blade, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.45
      efficiency: 0.66
      win: 0.38
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.44
      fit: 0.45
    Transcendence:
      total: 0.37
      efficiency: 0.53
      win: 0.38
      pick: 0.0
      fit: 0.08
    Hydra's Lament:
      total: 0.71
      efficiency: 0.54
      win: 1.0
      pick: 0.09
      fit: 0.44
    Ancile:
      total: 0.66
      efficiency: 0.51
      win: 1.0
      pick: 0.15
      fit: 0.17
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.67
      pick: 0.24
      fit: 0.38
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Ancile
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
    Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow,
    Toxic Blade, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda,
    The Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.52
      win: 0.38
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.6
      pick: 0.44
      fit: 0.37
    Berserker's Shield:
      total: 0.45
      efficiency: 0.68
      win: 0.33
      pick: 0.14
      fit: 0.4
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.38
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.43
      efficiency: 0.57
      win: 0.38
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  starter: *id001
---
