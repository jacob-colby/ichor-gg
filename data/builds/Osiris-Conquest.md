---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.69
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.49
    win_rate: 0.52
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.1
      win_rate: 0.43
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.57
  - name: Prophetic Cloak
    pick_rate: 0.15
    win_rate: 0.4
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.75
    - name: Golden Blade
      pick_rate: 0.1
      win_rate: 0.43
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.38
    - name: Gladiator's Shield
      pick_rate: 0.1
      win_rate: 0.29
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.57
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.67
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 0.6
  - name: Hide of the Nemean Lion
    pick_rate: 0.11
    win_rate: 0.71
    alternates:
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 0.4
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.8
  - name: Captain's Ring
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.83
    - name: Hide of the Nemean Lion
      pick_rate: 0.1
      win_rate: 1.0
  community_starters:
  - name: Sundering Axe
    pick_rate: 0.26
    win_rate: 0.5
  - name: Death's Embrace
    pick_rate: 0.19
    win_rate: 0.62
  - name: Death's Toll
    pick_rate: 0.19
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-09-25'
  god_win_rate: 0.5735294117647058
  god_matches_won: 39
  god_matches_played: 68
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-25'
  god_matches_analyzed: 2996
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
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
    this god: Jotunn''s Revenge, Golden Blade, Amanita Charm, Runeforged Hammer, Lernaean
    Bow, Tyrfing, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of
    Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament, Shogun''s Ofuda, Tekko-Kagi,
    Heartseeker, Dominance, Deathbringer, Toxic Blade, Erosion, Silverbranch Bow,
    Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.43
      pick: 0.14
      fit: 0.64
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.75
      pick: 0.16
      fit: 0.45
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.43
      pick: 0.0
      fit: 0.3
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.49
      fit: 0.35
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.2
      fit: 0.45
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.24
      fit: 0.25
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Shifter's Shield
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
  - Shifter's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
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
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Golden Blade,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate
    of Valor, The Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean Bow, Tyrfing,
    Riptalon, Erosion, Shogun''s Ofuda, Phoenix Feather, Eye of Providence, Avenging
    Blade, Hydra''s Lament, Chandra''s Grace, Stone of Binding, Daybreak Gavel, Midgardian
    Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.75
      pick: 0.16
      fit: 0.47
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.43
      pick: 0.0
      fit: 0.26
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.49
      fit: 0.44
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.2
      fit: 0.54
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.52
      win: 0.71
      pick: 0.24
      fit: 0.3
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.43
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Berserker's Shield
  - Shifter's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
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
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Amanita Charm, Heartseeker, Tekko-Kagi,
    Golden Blade, Stone of Binding, Silverbranch Bow, Runeforged Hammer, Screeching
    Gargoyle, Void Shield, Toxic Blade, Titan''s Bane, Void Stone, The Crusher, Genji''s
    Guard, Breastplate of Valor, Lernaean Bow, The Reaper, Tyrfing, Shield Splitter,
    Hydra''s Lament, Riptalon, Eye of the Storm, Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.49
      win: 0.43
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.75
      pick: 0.16
      fit: 0.33
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.43
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.49
      efficiency: 0.55
      win: 0.52
      pick: 0.49
      fit: 0.26
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.56
      pick: 0.2
      fit: 0.36
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.24
      fit: 0.19
  community_ordered:
  - Berserker's Shield
  - Shifter's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
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
    this god: Golden Blade, Jotunn''s Revenge, Amanita Charm, Tyrfing, Riptalon, Runeforged
    Hammer, Lernaean Bow, Genji''s Guard, Silverbranch Bow, Breastplate of Valor,
    Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda, Shield Splitter, Eye of the Storm,
    Hydra''s Lament, Tekko-Kagi, The Reaper, Daybreak Gavel, Avenging Blade, Dominance,
    Erosion, Shield of the Phoenix, Eye of Providence, Heartseeker, Vital Amplifier.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.52
      win: 0.43
      pick: 0.14
      fit: 0.6
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.75
      pick: 0.16
      fit: 0.41
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.56
      pick: 0.2
      fit: 0.36
    Shifter's Shield:
      total: 0.49
      efficiency: 0.55
      win: 0.52
      pick: 0.49
      fit: 0.26
    Tyrfing:
      total: 0.45
      efficiency: 0.48
      win: 0.43
      pick: 0.0
      fit: 0.58
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.24
      fit: 0.19
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
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
    Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Golden
    Blade, Screeching Gargoyle, Runeforged Hammer, Arondight, Lernaean Bow, Pharaoh''s
    Curse, Tyrfing, Shield Splitter, Daybreak Gavel, Eye of Erebus, Shogun''s Ofuda,
    Eye of the Storm, Chandra''s Grace, Silverbranch Bow, Erosion, Avenging Blade,
    Eye of Providence, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.43
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.75
      pick: 0.16
      fit: 0.33
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.43
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.43
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.56
      pick: 0.2
      fit: 0.36
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.24
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
    Breastplate of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament, Shogun''s
    Ofuda, Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic Blade, Erosion,
    Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Midgardian
    Mail.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.43
      pick: 0.14
      fit: 0.64
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.75
      pick: 0.16
      fit: 0.45
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.43
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.2
      fit: 0.45
    Runeforged Hammer:
      total: 0.46
      efficiency: 0.57
      win: 0.43
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.43
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
