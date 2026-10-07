---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.33
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.87
    win_rate: 0.46
    alternates:
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.67
    - name: Berserker's Shield
      pick_rate: 0.03
      win_rate: 0.0
  - name: Sanguine Lash
    pick_rate: 0.4
    win_rate: 0.58
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.13
      win_rate: 0.5
    - name: Umbral Link
      pick_rate: 0.07
      win_rate: 0.5
  - name: Berserker's Shield
    pick_rate: 0.23
    win_rate: 0.29
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.3
      win_rate: 0.33
    - name: Umbral Link
      pick_rate: 0.17
      win_rate: 0.8
  - name: Kinetic Cuirass
    pick_rate: 0.11
    win_rate: 0.33
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.15
      win_rate: 0.75
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.33
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 1.0
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.5
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 1.0
  - name: Mote of Chaos
    pick_rate: 0.12
    win_rate: 1.0
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.12
      win_rate: 0.0
    - name: Engraved Guard
      pick_rate: 0.12
      win_rate: 0.5
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.4
    win_rate: 0.58
  - name: Death's Embrace
    pick_rate: 0.17
    win_rate: 0.2
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-10-07'
  god_win_rate: 0.4666666666666667
  god_matches_won: 14
  god_matches_played: 30
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
  - Genji's Guard
  - Jotunn's Revenge
  - Shield Splitter
  - Shell of Rebuke
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield Splitter, Shifter''s Shield,
    Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm, Erosion,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone
    of Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail,
    Screeching Gargoyle, Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile,
    Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Shell of Rebuke:
      total: 0.62
      efficiency: 0.28
      win: 1.0
      pick: 0.17
      fit: 0.43
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Shell of Rebuke
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Shell of Rebuke
  - Runeforged Hammer
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Jotunn''s Revenge, Shield of the Phoenix,
    Runeforged Hammer, Shield Splitter, Shifter''s Shield, Eye of the Storm, Genji''s
    Guard, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Hydra''s
    Lament, Yogi''s Necklace, Avenging Blade, Phoenix Feather, Chandra''s Grace, Glorious
    Pridwen, Stone of Binding, Midgardian Mail, Golden Blade, Daybreak Gavel, Magi''s
    Cloak, Leviathan''s Hide, Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.42
    Shield Splitter:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.17
      fit: 0.36
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.57
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.1
      fit: 0.6
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Shell of Rebuke
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Shell of Rebuke
  - The Reaper
  flex_slots:
  - Avenging Blade
  - Screeching Gargoyle
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, Amanita Charm, Stone of Binding,
    Avenging Blade, Screeching Gargoyle, Heartseeker, Void Shield, Genji''s Guard,
    Shield Splitter, Breastplate of Valor, Void Stone, Shifter''s Shield, Runeforged
    Hammer, Titan''s Bane, The Crusher, Eye of the Storm, Erosion, Hydra''s Lament,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak, Pendulum
    Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.57
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.17
      fit: 0.31
    The Reaper:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.1
      fit: 0.48
  community_ordered:
  - Shell of Rebuke
  - The Reaper
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Tyrfing
  - Shell of Rebuke
  - The Reaper
  - Umbral Link
  - Pharaoh's Curse
  flex_slots:
  - Tyrfing
  - Pharaoh's Curse
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
    this god: The Reaper, Amanita Charm, Jotunn''s Revenge, Golden Blade, Genji''s
    Guard, Breastplate of Valor, Tyrfing, Shifter''s Shield, Shield Splitter, Pharaoh''s
    Curse, Runeforged Hammer, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch
    Bow, Erosion, Eye of Providence, Stone of Binding, Toxic Blade, Eye of the Storm,
    Shield of the Phoenix, Hydra''s Lament, Draconic Scale, Magi''s Cloak, Screeching
    Gargoyle, Daybreak Gavel, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.17
      fit: 0.27
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.67
      pick: 0.1
      fit: 0.21
    Umbral Link:
      total: 0.55
      efficiency: 0.43
      win: 0.8
      pick: 0.26
      fit: 0.2
    Pharaoh's Curse:
      total: 0.47
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Shell of Rebuke
  - The Reaper
  - Umbral Link
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Umbral Link
  - Shell of Rebuke
  flex_slots:
  - Umbral Link
  - Hydra's Lament
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Shifter''s Shield, Shield Splitter, Prophetic Cloak, Erosion, Runeforged
    Hammer, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.52
    Umbral Link:
      total: 0.52
      efficiency: 0.36
      win: 0.8
      pick: 0.26
      fit: 0.16
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.17
      fit: 0.32
  community_ordered:
  - Umbral Link
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Shield Splitter, Shifter''s
    Shield, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament,
    Stone of Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Heartseeker, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.56
      win: 0.33
      pick: 0.18
      fit: 0.7
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.45
      efficiency: 0.61
      win: 0.33
      pick: 0.18
      fit: 0.54
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
