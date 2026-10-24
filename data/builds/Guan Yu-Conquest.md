---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.43
  aspect_win_rate: 0.6
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.15
    win_rate: 0.43
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.5
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.75
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.13
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 1.0
  - name: Freya's Tears
    pick_rate: 0.27
    win_rate: 0.58
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.6
    - name: Nimble Ring
      pick_rate: 0.09
      win_rate: 1.0
  - name: Totem of Death
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.23
      win_rate: 0.56
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 1.0
  - name: Draconic Scale
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.33
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 1.0
  - name: Veve Charm
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.0
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.38
  - name: Hunter's Cowl
    pick_rate: 0.15
    win_rate: 0.43
  - name: Pendulum of the Ages
    pick_rate: 0.15
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-10-24'
  god_win_rate: 0.6304347826086957
  god_matches_won: 29
  god_matches_played: 46
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-24'
  god_matches_analyzed: 3785
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Freya's Tears
  - Draconic Scale
  - Stampede
  flex_slots:
  - Draconic Scale
  - Jotunn's Revenge
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Shifter''s Shield, Golden Blade, Runeforged Hammer, Eye of the Storm, Hydra''s
    Lament, Shield of the Phoenix, Erosion, Eye of Providence, Tyrfing, Stone of Binding,
    Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak,
    Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Heartseeker, Hide of the
    Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.18
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Prophetic Cloak:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.49
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.42
      fit: 0.49
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.6
      pick: 0.3
      fit: 0.5
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.75
      pick: 0.09
      fit: 0.33
  community_ordered:
  - Berserker's Shield
  - Prophetic Cloak
  - Freya's Tears
  - Draconic Scale
  - Stampede
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Prophetic Cloak
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Stampede
  flex_slots:
  - Berserker's Shield
  - Draconic Scale
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
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Shield Splitter, Shifter''s Shield, Eye of the
    Storm, Hydra''s Lament, The Reaper, Yogi''s Necklace, Erosion, Chandra''s Grace,
    Eye of Providence, Phoenix Feather, Avenging Blade, Tyrfing, Glorious Pridwen,
    Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Stone of Binding, Screeching
    Gargoyle.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.18
      fit: 0.45
    Prophetic Cloak:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.45
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.42
      fit: 0.45
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.6
      pick: 0.3
      fit: 0.5
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.8
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.75
      pick: 0.09
      fit: 0.35
  community_ordered:
  - Berserker's Shield
  - Prophetic Cloak
  - Freya's Tears
  - Draconic Scale
  - Stampede
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Freya's Tears
  - Draconic Scale
  - Stampede
  flex_slots:
  - Berserker's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    Avenging Blade, Kinetic Cuirass, Void Shield, Heartseeker, Void Stone, Shield
    Splitter, Runeforged Hammer, Silverbranch Bow, Shifter''s Shield, Tekko-Kagi,
    Titan''s Bane, The Crusher, Golden Blade, Toxic Blade, Hydra''s Lament, Eye of
    the Storm, The Reaper, Shield of the Phoenix, Erosion, Eye of Providence, Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.18
      fit: 0.32
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.55
    Prophetic Cloak:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.37
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.42
      fit: 0.37
    Draconic Scale:
      total: 0.52
      efficiency: 0.5
      win: 0.6
      pick: 0.3
      fit: 0.38
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.75
      pick: 0.09
      fit: 0.25
  community_ordered:
  - Berserker's Shield
  - Prophetic Cloak
  - Freya's Tears
  - Draconic Scale
  - Stampede
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Prophetic Cloak
  - Freya's Tears
  - Tyrfing
  - Stampede
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Golden Blade, Tyrfing,
    Shifter''s Shield, Runeforged Hammer, Shield Splitter, Pharaoh''s Curse, Riptalon,
    Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the
    Phoenix, Toxic Blade, Erosion, Eye of the Storm, Eye of Providence, Stone of Binding,
    Screeching Gargoyle, Daybreak Gavel, Magi''s Cloak, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.18
      fit: 0.43
    Prophetic Cloak:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.34
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.42
      fit: 0.34
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.55
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.75
      pick: 0.09
      fit: 0.23
  community_ordered:
  - Berserker's Shield
  - Prophetic Cloak
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Prophetic Cloak
  - Stampede
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Prophetic Cloak, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Shifter''s Shield, Shield Splitter, Runeforged Hammer, Erosion, Golden
    Blade, Gladiator''s Shield, Eye of Providence, Arondight, Stone of Binding, Eye
    of the Storm, Pharaoh''s Curse, Eye of Erebus, Magi''s Cloak, Daybreak Gavel,
    Midgardian Mail, Shogun''s Ofuda, Mantle Of Discord, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.44
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.18
      fit: 0.34
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.42
      fit: 0.58
    Prophetic Cloak:
      total: 0.7
      efficiency: 0.44
      win: 1.0
      pick: 0.1
      fit: 0.58
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.75
      pick: 0.09
      fit: 0.26
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Prophetic Cloak
  - Stampede
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield
    Splitter, Shifter''s Shield, Golden Blade, Runeforged Hammer, Eye of the Storm,
    Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence, Tyrfing, Stone
    of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle,
    Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Heartseeker,
    Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.32
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.18
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.42
      fit: 0.49
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
---
