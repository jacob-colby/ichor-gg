---
type: smite-build
god: Cu Chulainn
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Warped
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.43
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.5
    win_rate: 0.52
    alternates:
    - name: Mystical Mail
      pick_rate: 0.31
      win_rate: 0.6
    - name: The Reaper
      pick_rate: 0.05
      win_rate: 0.53
  - name: Mystical Mail
    pick_rate: 0.23
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.21
      win_rate: 0.58
    - name: Gladiator's Shield
      pick_rate: 0.1
      win_rate: 0.69
  - name: Freya's Tears
    pick_rate: 0.3
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.52
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.55
  - name: Shell of Rebuke
    pick_rate: 0.25
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.69
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 0.48
  - name: Hide of the Nemean Lion
    pick_rate: 0.17
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.72
    - name: Draconic Scale
      pick_rate: 0.07
      win_rate: 0.75
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.53
    - name: Hide of the Nemean Lion
      pick_rate: 0.09
      win_rate: 0.56
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.51
    win_rate: 0.65
  - name: Bluestone Pendant
    pick_rate: 0.37
    win_rate: 0.42
  - name: Bumba's Hammer
    pick_rate: 0.06
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/cu-chulainn/
  last_verified: '2026-09-11'
  god_win_rate: 0.5517241379310345
  god_matches_won: 192
  god_matches_played: 348
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Golden Blade,
    Runeforged Hammer, Lernaean Bow, Shield Splitter, Tyrfing, Genji''s Guard, Eye
    of the Storm, Breastplate of Valor, Pharaoh''s Curse, Hydra''s Lament, Avenging
    Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance, Heartseeker, Deathbringer, Erosion,
    Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch Bow, Toxic
    Blade, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.31
    Gladiator's Shield:
      total: 0.51
      efficiency: 0.39
      win: 0.69
      pick: 0.14
      fit: 0.37
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.47
      fit: 0.23
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.75
      pick: 0.15
      fit: 0.34
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, Runeforged Hammer, Golden Blade, Shield Splitter, Genji''s Guard, The
    Reaper, Eye of the Storm, Breastplate of Valor, Yogi''s Necklace, Pharaoh''s Curse,
    Lernaean Bow, Erosion, Shogun''s Ofuda, Phoenix Feather, Eye of Providence, Tyrfing,
    Avenging Blade, Riptalon, Hydra''s Lament, Chandra''s Grace, Stone of Binding,
    Daybreak Gavel, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.47
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.26
    Gladiator's Shield:
      total: 0.52
      efficiency: 0.39
      win: 0.69
      pick: 0.14
      fit: 0.43
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.47
      fit: 0.3
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.75
      pick: 0.15
      fit: 0.44
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
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
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Berserker''s Shield, Avenging Blade, Amanita
    Charm, Heartseeker, Tekko-Kagi, Stone of Binding, Silverbranch Bow, Screeching
    Gargoyle, Runeforged Hammer, Void Shield, Titan''s Bane, Golden Blade, The Crusher,
    Toxic Blade, Genji''s Guard, Void Stone, The Reaper, Breastplate of Valor, Lernaean
    Bow, Shield Splitter, Tyrfing, Hydra''s Lament, Eye of the Storm, Riptalon, Pharaoh''s
    Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.57
      pick: 0.47
      fit: 0.17
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.75
      pick: 0.15
      fit: 0.25
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.25
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Tyrfing
  - Draconic Scale
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
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Golden Blade, Amanita Charm,
    Tyrfing, Riptalon, Lernaean Bow, Genji''s Guard, Runeforged Hammer, Silverbranch
    Bow, Breastplate of Valor, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda, Shield
    Splitter, The Reaper, Tekko-Kagi, Hydra''s Lament, Eye of the Storm, Daybreak
    Gavel, Dominance, Avenging Blade, Erosion, Heartseeker, Shield of the Phoenix,
    Qin''s Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.18
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.57
      pick: 0.47
      fit: 0.18
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.53
      pick: 0.0
      fit: 0.59
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.75
      pick: 0.15
      fit: 0.25
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Gladiator''s Shield,
    Berserker''s Shield, Genji''s Guard, Breastplate of Valor, Amanita Charm, Hydra''s
    Lament, Shield of the Phoenix, Screeching Gargoyle, Runeforged Hammer, Golden
    Blade, Arondight, Lernaean Bow, Pharaoh''s Curse, Shield Splitter, Eye of Erebus,
    Tyrfing, Daybreak Gavel, Shogun''s Ofuda, Eye of the Storm, Prophetic Cloak, Chandra''s
    Grace, Erosion, Avenging Blade, Eye of Providence, Silverbranch Bow, Stone of
    Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.52
      pick: 0.12
      fit: 0.36
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.41
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.39
      win: 0.69
      pick: 0.14
      fit: 0.56
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.47
      fit: 0.43
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.75
      pick: 0.15
      fit: 0.24
  community_ordered:
  - Genji's Guard
  - Gladiator's Shield
  - Freya's Tears
  - Draconic Scale
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
    Golden Blade, Runeforged Hammer, Lernaean Bow, Shield Splitter, Tyrfing, Genji''s
    Guard, Eye of the Storm, Breastplate of Valor, Pharaoh''s Curse, Hydra''s Lament,
    Avenging Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance, Heartseeker, Deathbringer,
    Erosion, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch
    Bow, Toxic Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.44
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
