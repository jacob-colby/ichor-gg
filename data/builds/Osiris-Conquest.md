---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.28
  aspect_win_rate: 0.44
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.51
    win_rate: 0.48
    alternates:
    - name: Golden Blade
      pick_rate: 0.17
      win_rate: 0.43
    - name: Berserker's Shield
      pick_rate: 0.05
      win_rate: 0.38
  - name: Berserker's Shield
    pick_rate: 0.21
    win_rate: 0.45
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.48
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.52
  - name: Kinetic Cuirass
    pick_rate: 0.12
    win_rate: 0.35
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.17
      win_rate: 0.49
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.54
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.47
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.39
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.33
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.32
  - name: Veve Charm
    pick_rate: 0.05
    win_rate: 0.38
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.38
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.63
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.34
    win_rate: 0.52
  - name: Death's Toll
    pick_rate: 0.24
    win_rate: 0.38
  - name: Bluestone Brooch
    pick_rate: 0.13
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-08-22'
  god_win_rate: 0.4404332129963899
  god_matches_won: 122
  god_matches_played: 277
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Runeforged Hammer
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Lernaean Bow, Tyrfing,
    Shield Splitter, Eye of the Storm, Genji''s Guard, Freya''s Tears, Breastplate
    of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament, Shogun''s Ofuda,
    Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic Blade, Erosion, Silverbranch
    Bow, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Draconic Scale,
    Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.43
      pick: 0.17
      fit: 0.64
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.45
      pick: 0.29
      fit: 0.45
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.3
    Runeforged Hammer:
      total: 0.47
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.47
    Shifter's Shield:
      total: 0.49
      efficiency: 0.55
      win: 0.48
      pick: 0.51
      fit: 0.35
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.35
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Golden Blade
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Runeforged
    Hammer, Shield Splitter, Freya''s Tears, Eye of the Storm, Genji''s Guard, Breastplate
    of Valor, The Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean Bow, Tyrfing,
    Riptalon, Erosion, Shogun''s Ofuda, Phoenix Feather, Eye of Providence, Avenging
    Blade, Draconic Scale, Hydra''s Lament, Chandra''s Grace, Stone of Binding, Daybreak
    Gavel, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.52
      win: 0.43
      pick: 0.17
      fit: 0.59
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.45
      pick: 0.29
      fit: 0.47
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.26
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.48
      pick: 0.51
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Heartseeker
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
    for this god: Jotunn''s Revenge, Avenging Blade, Amanita Charm, Heartseeker, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Runeforged Hammer, Screeching Gargoyle, Void
    Shield, Toxic Blade, Titan''s Bane, Void Stone, The Crusher, Genji''s Guard, Breastplate
    of Valor, Lernaean Bow, The Reaper, Freya''s Tears, Tyrfing, Shield Splitter,
    Hydra''s Lament, Riptalon, Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.45
      pick: 0.29
      fit: 0.33
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.47
      efficiency: 0.55
      win: 0.48
      pick: 0.51
      fit: 0.26
    Heartseeker:
      total: 0.46
      efficiency: 0.47
      win: 0.45
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Tyrfing
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Tyrfing, Riptalon, Runeforged Hammer,
    Lernaean Bow, Genji''s Guard, Silverbranch Bow, Breastplate of Valor, Freya''s
    Tears, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda, Shield Splitter, Eye of
    the Storm, Hydra''s Lament, Tekko-Kagi, The Reaper, Daybreak Gavel, Avenging Blade,
    Dominance, Erosion, Shield of the Phoenix, Eye of Providence, Heartseeker, Vital
    Amplifier.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.52
      win: 0.43
      pick: 0.17
      fit: 0.6
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.45
      pick: 0.29
      fit: 0.41
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.18
    Tyrfing:
      total: 0.46
      efficiency: 0.48
      win: 0.45
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.47
      efficiency: 0.55
      win: 0.48
      pick: 0.51
      fit: 0.26
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gladiator's Shield
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Freya''s Tears, Gladiator''s Shield, Amanita Charm, Hydra''s
    Lament, Prophetic Cloak, Shield of the Phoenix, Screeching Gargoyle, Runeforged
    Hammer, Arondight, Lernaean Bow, Pharaoh''s Curse, Tyrfing, Shield Splitter, Daybreak
    Gavel, Eye of Erebus, Shogun''s Ofuda, Eye of the Storm, Chandra''s Grace, Silverbranch
    Bow, Erosion, Avenging Blade, Eye of Providence, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.45
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.45
      pick: 0.29
      fit: 0.33
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.4
    Gladiator's Shield:
      total: 0.47
      efficiency: 0.39
      win: 0.54
      pick: 0.14
      fit: 0.57
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.45
      pick: 0.0
      fit: 0.43
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer,
    Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm, Genji''s Guard, Freya''s
    Tears, Breastplate of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament,
    Shogun''s Ofuda, Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic Blade,
    Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.43
      pick: 0.17
      fit: 0.64
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.45
      pick: 0.29
      fit: 0.45
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.35
      pick: 0.19
      fit: 0.45
    Runeforged Hammer:
      total: 0.47
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.35
  starter: *id001
---
