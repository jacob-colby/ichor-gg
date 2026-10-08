---
type: smite-build
god: Cu Chulainn
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Warped
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.47
    win_rate: 0.42
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.25
      win_rate: 0.46
    - name: Mystical Mail
      pick_rate: 0.18
      win_rate: 0.53
  - name: Sanguine Lash
    pick_rate: 0.33
    win_rate: 0.41
    alternates:
    - name: Mystical Mail
      pick_rate: 0.16
      win_rate: 0.4
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.42
  - name: Umbral Link
    pick_rate: 0.14
    win_rate: 0.54
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.14
      win_rate: 0.46
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.31
  - name: Freya's Tears
    pick_rate: 0.23
    win_rate: 0.33
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.27
    - name: Brawler’s Beat Stick
      pick_rate: 0.06
      win_rate: 0.33
  - name: Hide of the Nemean Lion
    pick_rate: 0.17
    win_rate: 0.07
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.63
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.4
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.25
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.25
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.5
    win_rate: 0.48
  - name: Bluestone Pendant
    pick_rate: 0.32
    win_rate: 0.39
  - name: Hunter's Cowl
    pick_rate: 0.07
    win_rate: 0.71
  source_url: https://smitebrain.com/gods/cu-chulainn/
  last_verified: '2026-10-08'
  god_win_rate: 0.4583333333333333
  god_matches_won: 44
  god_matches_played: 96
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Shifter's Shield
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Genji''s Guard,
    Golden Blade, Runeforged Hammer, Kinetic Cuirass, Lernaean Bow, Shield Splitter,
    Tyrfing, Eye of the Storm, Breastplate of Valor, Pharaoh''s Curse, Hydra''s Lament,
    Avenging Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance, Heartseeker, Deathbringer,
    Erosion, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch
    Bow, Draconic Scale, Toxic Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.52
      win: 0.36
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.44
      efficiency: 0.66
      win: 0.4
      pick: 0.13
      fit: 0.13
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.46
      pick: 0.25
      fit: 0.34
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.44
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, Kinetic Cuirass, Genji''s Guard, Runeforged Hammer, Golden Blade, Shield
    Splitter, Eye of the Storm, Breastplate of Valor, The Reaper, Yogi''s Necklace,
    Pharaoh''s Curse, Lernaean Bow, Erosion, Shogun''s Ofuda, Phoenix Feather, Eye
    of Providence, Tyrfing, Avenging Blade, Riptalon, Draconic Scale, Hydra''s Lament,
    Chandra''s Grace, Stone of Binding, Daybreak Gavel, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.47
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.56
      win: 0.36
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.48
      efficiency: 0.55
      win: 0.46
      pick: 0.25
      fit: 0.44
    Shield of the Phoenix:
      total: 0.44
      efficiency: 0.53
      win: 0.36
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Berserker's Shield
  - Shifter's Shield
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Berserker''s Shield, Avenging Blade, Genji''s
    Guard, Amanita Charm, Heartseeker, Tekko-Kagi, Stone of Binding, Silverbranch
    Bow, Screeching Gargoyle, Runeforged Hammer, Void Shield, Kinetic Cuirass, Titan''s
    Bane, Golden Blade, The Crusher, Toxic Blade, Void Stone, Breastplate of Valor,
    Lernaean Bow, The Reaper, Shield Splitter, Tyrfing, Hydra''s Lament, Eye of the
    Storm, Riptalon, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.44
      efficiency: 0.49
      win: 0.36
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.43
      efficiency: 0.66
      win: 0.4
      pick: 0.13
      fit: 0.1
    Berserker's Shield:
      total: 0.45
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.32
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.46
      pick: 0.25
      fit: 0.25
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.43
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.25
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Tyrfing
  flex_slots:
  - Genji's Guard
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Golden Blade, Genji''s Guard,
    Amanita Charm, Tyrfing, Riptalon, Kinetic Cuirass, Lernaean Bow, Runeforged Hammer,
    Silverbranch Bow, Breastplate of Valor, Pharaoh''s Curse, Toxic Blade, Shogun''s
    Ofuda, Shield Splitter, Tekko-Kagi, Hydra''s Lament, The Reaper, Eye of the Storm,
    Daybreak Gavel, Dominance, Avenging Blade, Erosion, Heartseeker, Shield of the
    Phoenix, Qin''s Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.52
      win: 0.36
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.43
      efficiency: 0.66
      win: 0.4
      pick: 0.13
      fit: 0.1
    Berserker's Shield:
      total: 0.46
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.18
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.46
      pick: 0.25
      fit: 0.25
    Tyrfing:
      total: 0.42
      efficiency: 0.48
      win: 0.36
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Berserker''s Shield, Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield
    of the Phoenix, Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden
    Blade, Arondight, Lernaean Bow, Pharaoh''s Curse, Shield Splitter, Eye of Erebus,
    Tyrfing, Daybreak Gavel, Gladiator''s Shield, Shogun''s Ofuda, Eye of the Storm,
    Prophetic Cloak, Chandra''s Grace, Erosion, Avenging Blade, Eye of Providence,
    Silverbranch Bow, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.66
      win: 0.4
      pick: 0.13
      fit: 0.36
    Berserker's Shield:
      total: 0.45
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.41
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.46
      pick: 0.25
      fit: 0.24
    Freya's Tears:
      total: 0.45
      efficiency: 0.61
      win: 0.33
      pick: 0.38
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Underrated for this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Golden Blade, Runeforged Hammer, Kinetic Cuirass, Lernaean Bow, Shield Splitter,
    Tyrfing, Genji''s Guard, Eye of the Storm, Breastplate of Valor, Pharaoh''s Curse,
    Hydra''s Lament, Avenging Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance, Heartseeker,
    Deathbringer, Erosion, Daybreak Gavel, Eye of Providence, Shield of the Phoenix,
    Silverbranch Bow, Draconic Scale, Toxic Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.52
      win: 0.36
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.36
      pick: 0.0
      fit: 0.44
    Runeforged Hammer:
      total: 0.43
      efficiency: 0.57
      win: 0.36
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.44
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.34
  starter: *id001
---
