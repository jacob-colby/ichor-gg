---
type: smite-build
god: Cu Chulainn
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Warped
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.23
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.58
    win_rate: 0.56
    alternates:
    - name: Mystical Mail
      pick_rate: 0.2
      win_rate: 0.42
    - name: Sanguine Lash
      pick_rate: 0.04
      win_rate: 0.88
  - name: Gladiator's Shield
    pick_rate: 0.21
    win_rate: 0.47
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.48
    - name: Mystical Mail
      pick_rate: 0.12
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.45
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.15
      win_rate: 0.42
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.76
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.56
    - name: Draconic Scale
      pick_rate: 0.09
      win_rate: 0.53
  - name: Draconic Scale
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.44
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.27
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.38
    alternates:
    - name: Draconic Scale
      pick_rate: 0.07
      win_rate: 0.38
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.71
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.45
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.32
    win_rate: 0.46
  - name: Sundering Axe
    pick_rate: 0.07
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/cu-chulainn/
  last_verified: '2026-08-27'
  god_win_rate: 0.5094339622641509
  god_matches_won: 108
  god_matches_played: 212
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Sanguine Lash
  flex_slots:
  - Shifter's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Golden Blade,
    Runeforged Hammer, Lernaean Bow, Shield Splitter, Tyrfing, Eye of the Storm, Breastplate
    of Valor, Pharaoh''s Curse, Hydra''s Lament, Avenging Blade, Tekko-Kagi, Shogun''s
    Ofuda, Dominance, Heartseeker, Deathbringer, Erosion, Daybreak Gavel, Eye of Providence,
    Shield of the Phoenix, Silverbranch Bow, Toxic Blade, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.31
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.76
      pick: 0.23
      fit: 0.23
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.58
      fit: 0.34
    Draconic Scale:
      total: 0.51
      efficiency: 0.5
      win: 0.59
      pick: 0.32
      fit: 0.34
    Sanguine Lash:
      total: 0.59
      efficiency: 0.36
      win: 0.88
      pick: 0.04
      fit: 0.42
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  - Sanguine Lash
  flex_slots:
  - Shifter's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, Runeforged Hammer, Golden Blade, Shield Splitter, Eye of the Storm, Breastplate
    of Valor, The Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean Bow, Erosion,
    Shogun''s Ofuda, Phoenix Feather, Eye of Providence, Tyrfing, Avenging Blade,
    Riptalon, Hydra''s Lament, Chandra''s Grace, Stone of Binding, Daybreak Gavel,
    Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.76
      pick: 0.23
      fit: 0.3
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.58
      fit: 0.44
    Draconic Scale:
      total: 0.52
      efficiency: 0.5
      win: 0.59
      pick: 0.32
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.74
    Sanguine Lash:
      total: 0.59
      efficiency: 0.36
      win: 0.88
      pick: 0.04
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Sanguine Lash
  flex_slots:
  - Shifter's Shield
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Berserker''s Shield, Avenging Blade, Amanita
    Charm, Heartseeker, Tekko-Kagi, Stone of Binding, Silverbranch Bow, Screeching
    Gargoyle, Runeforged Hammer, Void Shield, Titan''s Bane, Golden Blade, The Crusher,
    Toxic Blade, Void Stone, Breastplate of Valor, Lernaean Bow, The Reaper, Shield
    Splitter, Tyrfing, Hydra''s Lament, Eye of the Storm, Riptalon, Pharaoh''s Curse,
    Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.76
      pick: 0.23
      fit: 0.17
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.58
      fit: 0.25
    Sanguine Lash:
      total: 0.58
      efficiency: 0.36
      win: 0.88
      pick: 0.04
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Freya's Tears
  - Shifter's Shield
  - Sanguine Lash
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
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Golden Blade, Amanita Charm,
    Tyrfing, Riptalon, Lernaean Bow, Runeforged Hammer, Silverbranch Bow, Breastplate
    of Valor, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda, Shield Splitter, Tekko-Kagi,
    Hydra''s Lament, The Reaper, Eye of the Storm, Daybreak Gavel, Dominance, Avenging
    Blade, Erosion, Heartseeker, Shield of the Phoenix, Qin''s Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.4
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.52
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.76
      pick: 0.23
      fit: 0.18
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.58
      fit: 0.25
    Sanguine Lash:
      total: 0.59
      efficiency: 0.4
      win: 0.88
      pick: 0.04
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Sanguine Lash
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield,
    Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Screeching
    Gargoyle, Runeforged Hammer, Golden Blade, Arondight, Lernaean Bow, Pharaoh''s
    Curse, Shield Splitter, Eye of Erebus, Tyrfing, Daybreak Gavel, Shogun''s Ofuda,
    Eye of the Storm, Prophetic Cloak, Chandra''s Grace, Erosion, Avenging Blade,
    Eye of Providence, Silverbranch Bow, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.76
      pick: 0.23
      fit: 0.43
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.58
      fit: 0.24
    Sanguine Lash:
      total: 0.56
      efficiency: 0.36
      win: 0.88
      pick: 0.04
      fit: 0.26
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
    Golden Blade, Runeforged Hammer, Lernaean Bow, Shield Splitter, Tyrfing, Eye of
    the Storm, Breastplate of Valor, Pharaoh''s Curse, Hydra''s Lament, Avenging Blade,
    Tekko-Kagi, Shogun''s Ofuda, Dominance, Heartseeker, Deathbringer, Erosion, Daybreak
    Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch Bow, Toxic Blade,
    Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.56
      win: 0.38
      pick: 0.22
      fit: 0.44
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Freya's Tears
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Jotunn''s Revenge,
    Amanita Charm, Golden Blade, Runeforged Hammer, Lernaean Bow, Shield Splitter,
    Tyrfing, Eye of the Storm, Breastplate of Valor, Pharaoh''s Curse, Hydra''s Lament,
    Avenging Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance, Heartseeker, Deathbringer,
    Erosion, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch
    Bow, Toxic Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.31
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.76
      pick: 0.23
      fit: 0.23
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.34
  swaps:
  - added: Freya's Tears
    removed: Kinetic Cuirass
    reason: community 76% win over 30 matches (vs 51% on this god), taking the model's
      weakest slot from Kinetic Cuirass
  starter: *id001
---
