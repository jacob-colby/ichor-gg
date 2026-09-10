---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.75
  aspect_win_rate: 0.67
  slot_order:
  - name: Lifebinder
    pick_rate: 0.75
    win_rate: 0.67
    alternates:
    - name: Golden Blade
      pick_rate: 0.25
      win_rate: 0.0
  - name: Helm of Radiance
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.5
      win_rate: 0.0
  - name: Gladiator's Shield
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.25
      win_rate: 0.0
    - name: Sphere of Negation
      pick_rate: 0.25
      win_rate: 1.0
  - name: Glorious Pridwen
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Killing Stone
      pick_rate: 0.25
      win_rate: 1.0
    - name: Sphere of Negation
      pick_rate: 0.25
      win_rate: 0.0
  - name: Genji's Guard
    pick_rate: 0.25
    win_rate: 0.0
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.25
      win_rate: 1.0
    - name: Helm of Radiance
      pick_rate: 0.25
      win_rate: 0.0
  - name: Midgardian Mail
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Engraved Guard
      pick_rate: 0.33
      win_rate: 0.0
    - name: Hide of the Nemean Lion
      pick_rate: 0.33
      win_rate: 0.0
  community_starters:
  - name: Sundering Axe
    pick_rate: 0.5
    win_rate: 0.5
  - name: Warrior's Axe
    pick_rate: 0.5
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-09-10'
  god_win_rate: 0.5
  god_matches_won: 2
  god_matches_played: 4
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Glorious Pridwen
  - Midgardian Mail
  - Runeforged Hammer
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Kinetic Cuirass,
    Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm, Freya''s Tears, Breastplate
    of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament, Shogun''s Ofuda,
    Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic Blade, Erosion, Silverbranch
    Bow, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.72
      win: 0.34
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.56
      win: 0.34
      pick: 0.0
      fit: 0.45
    Gladiator's Shield:
      total: 0.67
      efficiency: 0.39
      win: 1.0
      pick: 0.39
      fit: 0.39
    Glorious Pridwen:
      total: 0.64
      efficiency: 0.38
      win: 1.0
      pick: 0.42
      fit: 0.23
    Midgardian Mail:
      total: 0.72
      efficiency: 0.53
      win: 1.0
      pick: 1.0
      fit: 0.25
    Runeforged Hammer:
      total: 0.42
      efficiency: 0.57
      win: 0.34
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Gladiator's Shield
  - Glorious Pridwen
  - Midgardian Mail
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Glorious Pridwen
  - Midgardian Mail
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, Shield Splitter, Freya''s Tears, Eye of the Storm, Breastplate
    of Valor, The Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean Bow, Tyrfing,
    Riptalon, Erosion, Shogun''s Ofuda, Phoenix Feather, Eye of Providence, Avenging
    Blade, Draconic Scale, Hydra''s Lament, Chandra''s Grace, Stone of Binding, Daybreak
    Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.72
      win: 0.34
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.34
      pick: 0.0
      fit: 0.54
    Gladiator's Shield:
      total: 0.67
      efficiency: 0.39
      win: 1.0
      pick: 0.39
      fit: 0.43
    Glorious Pridwen:
      total: 0.69
      efficiency: 0.38
      win: 1.0
      pick: 0.42
      fit: 0.6
    Midgardian Mail:
      total: 0.73
      efficiency: 0.53
      win: 1.0
      pick: 1.0
      fit: 0.3
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.34
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Gladiator's Shield
  - Glorious Pridwen
  - Midgardian Mail
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Gladiator's Shield
  - Glorious Pridwen
  - Midgardian Mail
  - Heartseeker
  flex_slots:
  - Avenging Blade
  - Heartseeker
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
    for this god: Jotunn''s Revenge, Avenging Blade, Amanita Charm, Heartseeker, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Runeforged Hammer, Screeching Gargoyle, Void
    Shield, Toxic Blade, Kinetic Cuirass, Titan''s Bane, Void Stone, The Crusher,
    Breastplate of Valor, Lernaean Bow, The Reaper, Freya''s Tears, Tyrfing, Shield
    Splitter, Hydra''s Lament, Riptalon, Eye of the Storm, Pharaoh''s Curse, Avatar''s
    Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.43
      efficiency: 0.49
      win: 0.34
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.34
      pick: 0.0
      fit: 0.48
    Gladiator's Shield:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.39
      fit: 0.31
    Glorious Pridwen:
      total: 0.63
      efficiency: 0.38
      win: 1.0
      pick: 0.42
      fit: 0.17
    Midgardian Mail:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 1.0
      fit: 0.19
    Heartseeker:
      total: 0.41
      efficiency: 0.47
      win: 0.34
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Gladiator's Shield
  - Glorious Pridwen
  - Midgardian Mail
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - Gladiator's Shield
  - Glorious Pridwen
  - Midgardian Mail
  - Riptalon
  flex_slots:
  - Riptalon
  - Lernaean Bow
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
    this god: Jotunn''s Revenge, Amanita Charm, Tyrfing, Kinetic Cuirass, Riptalon,
    Runeforged Hammer, Lernaean Bow, Silverbranch Bow, Breastplate of Valor, Freya''s
    Tears, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda, Shield Splitter, Eye of
    the Storm, Hydra''s Lament, Tekko-Kagi, The Reaper, Daybreak Gavel, Avenging Blade,
    Dominance, Erosion, Shield of the Phoenix, Eye of Providence, Heartseeker, Vital
    Amplifier.'
  slot_scores:
    Lernaean Bow:
      total: 0.4
      efficiency: 0.52
      win: 0.34
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.41
      efficiency: 0.48
      win: 0.34
      pick: 0.0
      fit: 0.58
    Gladiator's Shield:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.39
      fit: 0.32
    Glorious Pridwen:
      total: 0.63
      efficiency: 0.38
      win: 1.0
      pick: 0.42
      fit: 0.17
    Midgardian Mail:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 1.0
      fit: 0.19
    Riptalon:
      total: 0.4
      efficiency: 0.51
      win: 0.34
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Gladiator's Shield
  - Glorious Pridwen
  - Midgardian Mail
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gladiator's Shield
  - Glorious Pridwen
  - Midgardian Mail
  - Freya's Tears
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Freya''s Tears, Amanita Charm, Hydra''s Lament, Shield of the Phoenix,
    Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer, Arondight, Lernaean Bow,
    Pharaoh''s Curse, Tyrfing, Shield Splitter, Daybreak Gavel, Eye of Erebus, Shogun''s
    Ofuda, Eye of the Storm, Prophetic Cloak, Chandra''s Grace, Silverbranch Bow,
    Erosion, Avenging Blade, Eye of Providence, Stone of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.43
      efficiency: 0.65
      win: 0.34
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.72
      win: 0.34
      pick: 0.0
      fit: 0.4
    Gladiator's Shield:
      total: 0.69
      efficiency: 0.39
      win: 1.0
      pick: 0.39
      fit: 0.57
    Glorious Pridwen:
      total: 0.67
      efficiency: 0.38
      win: 1.0
      pick: 0.42
      fit: 0.43
    Midgardian Mail:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 1.0
      fit: 0.18
    Freya's Tears:
      total: 0.43
      efficiency: 0.61
      win: 0.34
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Gladiator's Shield
  - Glorious Pridwen
  - Midgardian Mail
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
    Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm, Freya''s
    Tears, Breastplate of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament,
    Shogun''s Ofuda, Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic Blade,
    Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield of the Phoenix,
    Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.29
      efficiency: 0.52
      win: 0.0
      pick: 0.25
      fit: 0.64
    Berserker's Shield:
      total: 0.32
      efficiency: 0.68
      win: 0.0
      pick: 0.39
      fit: 0.45
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.72
      win: 0.34
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.56
      win: 0.34
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.42
      efficiency: 0.57
      win: 0.34
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.43
      efficiency: 0.65
      win: 0.34
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  starter: *id001
---
