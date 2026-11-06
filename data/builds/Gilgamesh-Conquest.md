---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.71
  aspect_win_rate: 0.58
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.46
    win_rate: 0.65
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.18
      win_rate: 0.65
    - name: Barbed Carver
      pick_rate: 0.13
      win_rate: 0.58
  - name: The Reaper
    pick_rate: 0.22
    win_rate: 0.65
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.22
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.7
  - name: Barbed Carver
    pick_rate: 0.26
    win_rate: 0.58
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.67
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.71
  - name: Sanguine Lash
    pick_rate: 0.23
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.19
      win_rate: 0.53
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.43
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.65
    alternates:
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 1.0
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.83
  - name: Sage's Ring
    pick_rate: 0.12
    win_rate: 0.75
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.1
      win_rate: 1.0
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.75
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.43
    win_rate: 0.73
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.08
    win_rate: 0.71
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-11-06'
  god_win_rate: 0.6236559139784946
  god_matches_won: 58
  god_matches_played: 93
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Tyrfing, Golden Blade, Shield Splitter,
    Runeforged Hammer, Tekko-Kagi, The Crusher, Hydra''s Lament, Oni Hunter''s Garb,
    Breastplate of Valor, Toxic Blade, Shield of the Phoenix, Lernaean Bow, Dominance,
    Draconic Scale, Titan''s Bane, Avenging Blade, Shogun''s Ofuda, Pharaoh''s Curse,
    Midgardian Mail, Silverbranch Bow, Erosion, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.11
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.18
      fit: 0.34
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.16
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.39
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.65
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Transcendence
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Amanita Charm, Hydra''s Lament, Breastplate of Valor, Tyrfing, Runeforged
    Hammer, Shield Splitter, Golden Blade, Oni Hunter''s Garb, Shield of the Phoenix,
    The Crusher, Dominance, Tekko-Kagi, Lernaean Bow, Titan''s Bane, Screeching Gargoyle,
    Arondight, Yogi''s Necklace, Avenging Blade, Draconic Scale, Midgardian Mail,
    Eye of Providence, Toxic Blade, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.65
      pick: 0.18
      fit: 0.39
    Brawler’s Beat Stick:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.11
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.3
    Transcendence:
      total: 0.5
      efficiency: 0.5
      win: 0.65
      pick: 0.0
      fit: 0.21
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.2
  community_ordered:
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - The Reaper
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Genji''s Guard, Phoenix Feather,
    Yogi''s Necklace, Shield Splitter, Riptalon, Tyrfing, Golden Blade, Runeforged
    Hammer, Oni Hunter''s Garb, Breastplate of Valor, Draconic Scale, Bloodforge,
    Chandra''s Grace, Hydra''s Lament, Erosion, The Crusher, Tekko-Kagi, Eye of Providence,
    Midgardian Mail, Toxic Blade, Shogun''s Ofuda, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.18
      fit: 0.3
    Brawler’s Beat Stick:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.23
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.47
    The Reaper:
      total: 0.6
      efficiency: 0.57
      win: 0.65
      pick: 0.3
      fit: 0.65
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.65
      pick: 0.41
      fit: 0.25
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - The Reaper
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Brawler’s Beat Stick
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  flex_slots:
  - Avenging Blade
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Avenging Blade, Genji''s Guard, Screeching Gargoyle,
    The Crusher, Tekko-Kagi, Tyrfing, Stone of Binding, Void Stone, Void Shield, Toxic
    Blade, Titan''s Bane, Runeforged Hammer, Shield Splitter, Golden Blade, Silverbranch
    Bow, Riptalon, Breastplate of Valor, Hydra''s Lament, Oni Hunter''s Garb, Shield
    of the Phoenix, Lernaean Bow, Dominance, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.56
      efficiency: 0.47
      win: 0.65
      pick: 0.0
      fit: 0.66
    Brawler’s Beat Stick:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.13
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.09
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.18
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.34
    The Reaper:
      total: 0.58
      efficiency: 0.57
      win: 0.65
      pick: 0.3
      fit: 0.49
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Tyrfing, Genji''s Guard, Golden Blade, Toxic Blade, Shield
    Splitter, Runeforged Hammer, Silverbranch Bow, Breastplate of Valor, Tekko-Kagi,
    Oni Hunter''s Garb, Riptalon, Shield of the Phoenix, Lernaean Bow, Shogun''s Ofuda,
    Dominance, Hydra''s Lament, Pharaoh''s Curse, The Crusher, Draconic Scale, Midgardian
    Mail, Qin''s Blade, Leviathan''s Hide, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.51
      win: 0.65
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.3
      fit: 0.38
    Brawler’s Beat Stick:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.14
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.34
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.65
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Berserker's Shield
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Amanita Charm, Breastplate
    of Valor, Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle, Tyrfing,
    Arondight, Runeforged Hammer, Shield Splitter, Oni Hunter''s Garb, Golden Blade,
    Gladiator''s Shield, Chandra''s Grace, Draconic Scale, The Crusher, Midgardian
    Mail, Toxic Blade, Eye of Providence, Tekko-Kagi, Eye of Erebus, Damaru, Leviathan''s
    Hide, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.65
      pick: 0.18
      fit: 0.42
    Brawler’s Beat Stick:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.31
      fit: 0.12
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.32
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.65
      pick: 0.41
      fit: 0.37
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.22
  community_ordered:
  - Jotunn's Revenge
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Genji''s Guard, Tyrfing, Golden Blade,
    Shield Splitter, Runeforged Hammer, Tekko-Kagi, The Crusher, Hydra''s Lament,
    Oni Hunter''s Garb, Breastplate of Valor, Toxic Blade, Shield of the Phoenix,
    Lernaean Bow, Dominance, Draconic Scale, Titan''s Bane, Avenging Blade, Shogun''s
    Ofuda, Pharaoh''s Curse, Midgardian Mail, Silverbranch Bow, Erosion, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.11
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.3
      fit: 0.37
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.18
      fit: 0.34
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.39
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.65
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  starter: *id001
---
