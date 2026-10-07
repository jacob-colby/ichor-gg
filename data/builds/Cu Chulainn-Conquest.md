---
type: smite-build
god: Cu Chulainn
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Warped
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.44
    win_rate: 0.39
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.23
      win_rate: 0.47
    - name: Mystical Mail
      pick_rate: 0.17
      win_rate: 0.45
  - name: Sanguine Lash
    pick_rate: 0.34
    win_rate: 0.36
    alternates:
    - name: Mystical Mail
      pick_rate: 0.19
      win_rate: 0.42
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.38
  - name: Umbral Link
    pick_rate: 0.16
    win_rate: 0.4
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.33
    - name: Sanguine Lash
      pick_rate: 0.13
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.23
    win_rate: 0.36
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.29
    - name: Umbral Link
      pick_rate: 0.07
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.14
    win_rate: 0.13
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.67
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.5
  - name: Engraved Guard
    pick_rate: 0.11
    win_rate: 0.25
    alternates:
    - name: Spectral Armor
      pick_rate: 0.08
      win_rate: 0.67
    - name: Olmec Blue
      pick_rate: 0.08
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.53
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.36
    win_rate: 0.35
  - name: Hunter's Cowl
    pick_rate: 0.05
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/cu-chulainn/
  last_verified: '2026-10-07'
  god_win_rate: 0.4375
  god_matches_won: 28
  god_matches_played: 64
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Shifter's Shield
  - Jotunn's Revenge
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Golden Blade,
    Runeforged Hammer, Kinetic Cuirass, Lernaean Bow, Shield Splitter, Tyrfing, Genji''s
    Guard, Eye of the Storm, Breastplate of Valor, Pharaoh''s Curse, Hydra''s Lament,
    Avenging Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance, Heartseeker, Deathbringer,
    Erosion, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch
    Bow, Draconic Scale, Toxic Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.52
      win: 0.38
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.47
      efficiency: 0.55
      win: 0.47
      pick: 0.23
      fit: 0.34
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.31
    Spectral Armor:
      total: 0.52
      efficiency: 0.5
      win: 0.67
      pick: 0.25
      fit: 0.24
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Shifter's Shield
  - Spectral Armor
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, Kinetic Cuirass, Runeforged Hammer, Golden Blade, Shield Splitter, Eye
    of the Storm, Genji''s Guard, Breastplate of Valor, The Reaper, Yogi''s Necklace,
    Pharaoh''s Curse, Lernaean Bow, Erosion, Shogun''s Ofuda, Phoenix Feather, Eye
    of Providence, Tyrfing, Avenging Blade, Riptalon, Draconic Scale, Hydra''s Lament,
    Chandra''s Grace, Stone of Binding, Daybreak Gavel, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.47
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.26
    Shifter's Shield:
      total: 0.48
      efficiency: 0.55
      win: 0.47
      pick: 0.23
      fit: 0.44
    Shield of the Phoenix:
      total: 0.45
      efficiency: 0.53
      win: 0.38
      pick: 0.0
      fit: 0.63
    Spectral Armor:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.25
      fit: 0.3
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Shifter's Shield
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Shifter's Shield
  - Jotunn's Revenge
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Berserker''s Shield, Avenging Blade, Amanita
    Charm, Heartseeker, Tekko-Kagi, Stone of Binding, Silverbranch Bow, Screeching
    Gargoyle, Runeforged Hammer, Void Shield, Kinetic Cuirass, Titan''s Bane, Golden
    Blade, The Crusher, Toxic Blade, Void Stone, Genji''s Guard, Breastplate of Valor,
    Lernaean Bow, The Reaper, Shield Splitter, Tyrfing, Hydra''s Lament, Eye of the
    Storm, Riptalon, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.44
      efficiency: 0.49
      win: 0.38
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.46
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.32
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.47
      pick: 0.23
      fit: 0.25
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.49
    Spectral Armor:
      total: 0.51
      efficiency: 0.5
      win: 0.67
      pick: 0.25
      fit: 0.18
    Amanita Charm:
      total: 0.44
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.25
  community_ordered:
  - Shifter's Shield
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Tyrfing
  - Spectral Armor
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Golden Blade, Amanita Charm,
    Tyrfing, Riptalon, Kinetic Cuirass, Lernaean Bow, Runeforged Hammer, Silverbranch
    Bow, Genji''s Guard, Breastplate of Valor, Pharaoh''s Curse, Toxic Blade, Shogun''s
    Ofuda, Shield Splitter, Tekko-Kagi, Hydra''s Lament, The Reaper, Eye of the Storm,
    Daybreak Gavel, Dominance, Avenging Blade, Erosion, Heartseeker, Shield of the
    Phoenix, Qin''s Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.52
      win: 0.38
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.18
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.47
      pick: 0.23
      fit: 0.25
    Tyrfing:
      total: 0.43
      efficiency: 0.48
      win: 0.38
      pick: 0.0
      fit: 0.59
    Spectral Armor:
      total: 0.51
      efficiency: 0.5
      win: 0.67
      pick: 0.25
      fit: 0.18
  community_ordered:
  - Shifter's Shield
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  - Spectral Armor
  flex_slots:
  - Shifter's Shield
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of
    the Phoenix, Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade,
    Arondight, Lernaean Bow, Pharaoh''s Curse, Shield Splitter, Eye of Erebus, Tyrfing,
    Daybreak Gavel, Gladiator''s Shield, Shogun''s Ofuda, Eye of the Storm, Prophetic
    Cloak, Chandra''s Grace, Erosion, Avenging Blade, Eye of Providence, Silverbranch
    Bow, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.45
      efficiency: 0.66
      win: 0.38
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.45
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.41
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.47
      pick: 0.23
      fit: 0.24
    Freya's Tears:
      total: 0.46
      efficiency: 0.61
      win: 0.36
      pick: 0.38
      fit: 0.43
    Spectral Armor:
      total: 0.51
      efficiency: 0.5
      win: 0.67
      pick: 0.25
      fit: 0.17
  community_ordered:
  - Shifter's Shield
  - Freya's Tears
  - Spectral Armor
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
      win: 0.38
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.38
      pick: 0.0
      fit: 0.44
    Runeforged Hammer:
      total: 0.44
      efficiency: 0.57
      win: 0.38
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.34
  starter: *id001
---
