---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.35
  aspect_win_rate: 0.38
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.45
    win_rate: 0.42
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.33
    - name: Helm of Radiance
      pick_rate: 0.09
      win_rate: 0.5
  - name: Berserker's Shield
    pick_rate: 0.23
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.5
    - name: Sanguine Lash
      pick_rate: 0.16
      win_rate: 0.45
  - name: Shifter's Shield
    pick_rate: 0.12
    win_rate: 0.38
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.13
      win_rate: 0.22
    - name: Sanguine Lash
      pick_rate: 0.1
      win_rate: 0.57
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.44
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.8
    - name: Shogun's Ofuda
      pick_rate: 0.06
      win_rate: 0.0
  - name: Kinetic Cuirass
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.4
    - name: Hide of the Nemean Lion
      pick_rate: 0.09
      win_rate: 0.8
  - name: Sage's Ring
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Medal of Defense
      pick_rate: 0.11
      win_rate: 0.75
    - name: Survivor's Sash
      pick_rate: 0.08
      win_rate: 0.0
  community_starters:
  - name: Death's Toll
    pick_rate: 0.22
    win_rate: 0.33
  - name: Death's Embrace
    pick_rate: 0.19
    win_rate: 0.54
  - name: Bluestone Pendant
    pick_rate: 0.12
    win_rate: 0.13
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-10-10'
  god_win_rate: 0.4057971014492754
  god_matches_won: 28
  god_matches_played: 69
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-10'
  god_matches_analyzed: 4063
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
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
    this god: Jotunn''s Revenge, Amanita Charm, Golden Blade, Runeforged Hammer, Lernaean
    Bow, Tyrfing, Shield Splitter, Eye of the Storm, Genji''s Guard, Freya''s Tears,
    Breastplate of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament, Tekko-Kagi,
    Heartseeker, Dominance, Deathbringer, Toxic Blade, Erosion, Silverbranch Bow,
    Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Draconic Scale, Midgardian
    Mail, Shogun''s Ofuda.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.56
      pick: 0.31
      fit: 0.45
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.26
      fit: 0.45
    Hide of the Nemean Lion:
      total: 0.59
      efficiency: 0.52
      win: 0.8
      pick: 0.19
      fit: 0.25
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
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
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
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
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Golden Blade,
    Runeforged Hammer, Shield Splitter, Freya''s Tears, Eye of the Storm, Genji''s
    Guard, Breastplate of Valor, The Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean
    Bow, Tyrfing, Riptalon, Erosion, Phoenix Feather, Eye of Providence, Avenging
    Blade, Draconic Scale, Hydra''s Lament, Chandra''s Grace, Stone of Binding, Daybreak
    Gavel, Midgardian Mail, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.56
      pick: 0.31
      fit: 0.47
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.26
      fit: 0.54
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.63
    Hide of the Nemean Lion:
      total: 0.6
      efficiency: 0.52
      win: 0.8
      pick: 0.19
      fit: 0.3
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
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
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Amanita Charm, Heartseeker, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Runeforged Hammer, Golden Blade, Screeching
    Gargoyle, Void Shield, Toxic Blade, Titan''s Bane, Void Stone, The Crusher, Genji''s
    Guard, Breastplate of Valor, Lernaean Bow, The Reaper, Freya''s Tears, Tyrfing,
    Shield Splitter, Hydra''s Lament, Riptalon, Eye of the Storm, Pharaoh''s Curse,
    Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.49
      efficiency: 0.49
      win: 0.47
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.31
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.26
      fit: 0.36
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.52
      win: 0.8
      pick: 0.19
      fit: 0.19
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Hide of the Nemean Lion
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Golden Blade, Amanita Charm, Tyrfing, Riptalon, Runeforged
    Hammer, Lernaean Bow, Genji''s Guard, Silverbranch Bow, Breastplate of Valor,
    Freya''s Tears, Pharaoh''s Curse, Toxic Blade, Shield Splitter, Eye of the Storm,
    Hydra''s Lament, Tekko-Kagi, The Reaper, Daybreak Gavel, Avenging Blade, Dominance,
    Erosion, Shield of the Phoenix, Eye of Providence, Heartseeker, Vital Amplifier,
    Shogun''s Ofuda.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.56
      pick: 0.31
      fit: 0.41
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.18
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.26
      fit: 0.36
    Tyrfing:
      total: 0.47
      efficiency: 0.48
      win: 0.47
      pick: 0.0
      fit: 0.58
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.52
      win: 0.8
      pick: 0.19
      fit: 0.19
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Freya''s Tears, Amanita Charm, Hydra''s Lament, Shield of
    the Phoenix, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Arondight,
    Lernaean Bow, Pharaoh''s Curse, Tyrfing, Shield Splitter, Daybreak Gavel, Eye
    of Erebus, Gladiator''s Shield, Eye of the Storm, Prophetic Cloak, Chandra''s
    Grace, Silverbranch Bow, Erosion, Avenging Blade, Eye of Providence, Stone of
    Binding, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.31
      fit: 0.33
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.26
      fit: 0.36
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.52
      win: 0.8
      pick: 0.19
      fit: 0.18
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Golden Blade, Runeforged
    Hammer, Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm, Genji''s Guard,
    Freya''s Tears, Breastplate of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s
    Lament, Shogun''s Ofuda, Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic
    Blade, Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield of
    the Phoenix, Draconic Scale, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.56
      pick: 0.31
      fit: 0.45
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.26
      fit: 0.45
    Runeforged Hammer:
      total: 0.48
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
