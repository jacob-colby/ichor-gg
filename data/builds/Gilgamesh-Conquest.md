---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.68
  aspect_win_rate: 0.57
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.29
    win_rate: 0.59
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.22
      win_rate: 0.59
    - name: Barbed Carver
      pick_rate: 0.09
      win_rate: 0.53
  - name: Barbed Carver
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.52
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.64
  - name: Berserker's Shield
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.8
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.67
    - name: Sanguine Lash
      pick_rate: 0.08
      win_rate: 0.64
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.71
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.75
    - name: Brawler’s Beat Stick
      pick_rate: 0.05
      win_rate: 0.88
  - name: Veve Charm
    pick_rate: 0.05
    win_rate: 0.2
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 1.0
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.26
    win_rate: 0.67
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.62
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.34
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-26'
  god_win_rate: 0.5860215053763441
  god_matches_won: 109
  god_matches_played: 186
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-26'
  god_matches_analyzed: 6194
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
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
    this god: Amanita Charm, Golden Blade, Runeforged Hammer, Kinetic Cuirass, Tyrfing,
    Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate of Valor,
    Eye of the Storm, Silverbranch Bow, Toxic Blade, Shifter''s Shield, Hydra''s Lament,
    Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, Daybreak Gavel, Deathbringer,
    Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.58
      efficiency: 0.42
      win: 0.88
      pick: 0.11
      fit: 0.18
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.19
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.22
      fit: 0.37
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.71
      pick: 0.19
      fit: 0.21
    Titan's Bane:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.15
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Hydra''s Lament,
    Golden Blade, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield Splitter, Tekko-Kagi,
    Eye of the Storm, Avenging Blade, Silverbranch Bow, Shifter''s Shield, Dominance,
    Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, Toxic Blade, Transcendence,
    Deathbringer, Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.57
      efficiency: 0.42
      win: 0.88
      pick: 0.11
      fit: 0.12
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.2
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.22
      fit: 0.41
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.71
      pick: 0.19
      fit: 0.2
    Titan's Bane:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.15
      fit: 0.37
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Golden Blade,
    The Reaper, Runeforged Hammer, Riptalon, Shield Splitter, Shifter''s Shield, Genji''s
    Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean Bow,
    Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda, Tekko-Kagi,
    Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Hydra''s Lament,
    Draconic Scale.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.59
      efficiency: 0.42
      win: 0.88
      pick: 0.11
      fit: 0.25
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.59
      pick: 0.19
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.22
      fit: 0.32
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.71
      pick: 0.19
      fit: 0.27
    Titan's Bane:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.15
      fit: 0.4
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Berserker's Shield
  - The Crusher
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
    for this god: Avenging Blade, Amanita Charm, Tekko-Kagi, Stone of Binding, Silverbranch
    Bow, Golden Blade, Toxic Blade, Runeforged Hammer, Screeching Gargoyle, Void Shield,
    Kinetic Cuirass, Void Stone, Genji''s Guard, Breastplate of Valor, Lernaean Bow,
    The Reaper, Tyrfing, Shield Splitter, Riptalon, Hydra''s Lament, Eye of the Storm,
    Shifter''s Shield, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.57
      efficiency: 0.42
      win: 0.88
      pick: 0.11
      fit: 0.14
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.19
      fit: 0.33
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.22
      fit: 0.48
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.71
      pick: 0.19
      fit: 0.17
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.55
    Titan's Bane:
      total: 0.71
      efficiency: 0.47
      win: 1.0
      pick: 0.15
      fit: 0.55
  community_ordered:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Freya's Tears
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
    this god: Amanita Charm, Golden Blade, Riptalon, Tyrfing, Silverbranch Bow, Kinetic
    Cuirass, Runeforged Hammer, Toxic Blade, Genji''s Guard, Lernaean Bow, Breastplate
    of Valor, Pharaoh''s Curse, The Reaper, Tekko-Kagi, Shogun''s Ofuda, Shifter''s
    Shield, Shield Splitter, Hydra''s Lament, Daybreak Gavel, Eye of the Storm, Avenging
    Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence, Stone of
    Binding.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.56
    Brawler’s Beat Stick:
      total: 0.57
      efficiency: 0.42
      win: 0.88
      pick: 0.11
      fit: 0.14
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.19
      fit: 0.38
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.71
      pick: 0.19
      fit: 0.16
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.51
    Titan's Bane:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.15
      fit: 0.32
  community_ordered:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  flex_slots:
  - Berserker's Shield
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic Cuirass, Screeching
    Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch Bow, Shifter''s Shield,
    Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak
    Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Tekko-Kagi, Eye of the Storm,
    Gladiator''s Shield, Avenging Blade, Erosion, Eye of Providence.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.57
      efficiency: 0.42
      win: 0.88
      pick: 0.11
      fit: 0.13
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.19
      fit: 0.3
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.22
      fit: 0.45
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.71
      pick: 0.19
      fit: 0.39
    Titan's Bane:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.15
      fit: 0.28
  community_ordered:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
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
    Underrated for this god: Amanita Charm, Golden Blade, Runeforged Hammer, Kinetic
    Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Silverbranch Bow, Toxic Blade, Shifter''s Shield,
    Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, Daybreak Gavel,
    Deathbringer, Dominance, Erosion, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.19
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.22
      fit: 0.37
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  starter: *id001
---
