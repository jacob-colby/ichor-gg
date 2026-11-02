---
type: smite-build
god: Cu Chulainn
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Warped
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.49
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.37
    win_rate: 0.51
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.3
      win_rate: 0.46
    - name: Mystical Mail
      pick_rate: 0.18
      win_rate: 0.6
  - name: Mystical Mail
    pick_rate: 0.13
    win_rate: 0.51
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.45
    - name: Sanguine Lash
      pick_rate: 0.12
      win_rate: 0.53
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.44
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.64
    - name: Sanguine Lash
      pick_rate: 0.07
      win_rate: 0.51
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.49
    alternates:
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.53
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.58
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.53
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.63
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.64
  - name: Medal of Defense
    pick_rate: 0.08
    win_rate: 0.48
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.62
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.59
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.5
    win_rate: 0.58
  - name: Bluestone Pendant
    pick_rate: 0.34
    win_rate: 0.4
  - name: Bumba's Hammer
    pick_rate: 0.07
    win_rate: 0.8
  source_url: https://smitebrain.com/gods/cu-chulainn/
  last_verified: '2026-10-30'
  god_win_rate: 0.4965986394557823
  god_matches_won: 365
  god_matches_played: 735
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Golden Blade,
    Runeforged Hammer, Lernaean Bow, Shield Splitter, Tyrfing, Genji''s Guard, Eye
    of the Storm, Breastplate of Valor, Hydra''s Lament, Pharaoh''s Curse, Avenging
    Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance, Deathbringer, Erosion, Heartseeker,
    Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch Bow, Toxic
    Blade, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.31
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.46
    Draconic Scale:
      total: 0.5
      efficiency: 0.5
      win: 0.59
      pick: 0.15
      fit: 0.34
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, Golden Blade, Runeforged Hammer, Shield Splitter, Genji''s Guard, Eye
    of the Storm, Yogi''s Necklace, The Reaper, Breastplate of Valor, Pharaoh''s Curse,
    Lernaean Bow, Erosion, Shogun''s Ofuda, Phoenix Feather, Eye of Providence, Tyrfing,
    Avenging Blade, Riptalon, Hydra''s Lament, Chandra''s Grace, Daybreak Gavel, Midgardian
    Mail, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.47
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.22
      fit: 0.54
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.63
    Draconic Scale:
      total: 0.51
      efficiency: 0.5
      win: 0.59
      pick: 0.15
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tekko-Kagi
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Tekko-Kagi
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Berserker''s Shield, Avenging Blade, Amanita
    Charm, Tekko-Kagi, Heartseeker, Stone of Binding, Silverbranch Bow, Runeforged
    Hammer, Screeching Gargoyle, Void Shield, Golden Blade, Titan''s Bane, Toxic Blade,
    The Crusher, Genji''s Guard, Void Stone, The Reaper, Lernaean Bow, Breastplate
    of Valor, Shield Splitter, Tyrfing, Hydra''s Lament, Eye of the Storm, Riptalon,
    Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.49
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.61
    Heartseeker:
      total: 0.49
      efficiency: 0.46
      win: 0.51
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.25
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Jotunn''s Revenge, Amanita Charm,
    Tyrfing, Riptalon, Lernaean Bow, Genji''s Guard, Runeforged Hammer, Silverbranch
    Bow, Breastplate of Valor, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda, Shield
    Splitter, Hydra''s Lament, Tekko-Kagi, The Reaper, Eye of the Storm, Dominance,
    Daybreak Gavel, Avenging Blade, Erosion, Shield of the Phoenix, Eye of Providence,
    Qin''s Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.18
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.51
      pick: 0.0
      fit: 0.59
    Draconic Scale:
      total: 0.49
      efficiency: 0.5
      win: 0.59
      pick: 0.15
      fit: 0.25
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.25
  community_ordered:
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Berserker''s Shield, Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield
    of the Phoenix, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Arondight,
    Lernaean Bow, Pharaoh''s Curse, Shield Splitter, Eye of Erebus, Daybreak Gavel,
    Gladiator''s Shield, Tyrfing, Shogun''s Ofuda, Eye of the Storm, Prophetic Cloak,
    Chandra''s Grace, Erosion, Avenging Blade, Eye of Providence, Silverbranch Bow,
    Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.24
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
    Guard, Eye of the Storm, Breastplate of Valor, Hydra''s Lament, Pharaoh''s Curse,
    Avenging Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance, Deathbringer, Erosion,
    Heartseeker, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch
    Bow, Toxic Blade, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.57
      win: 0.49
      pick: 0.22
      fit: 0.44
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
