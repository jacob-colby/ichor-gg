---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.45
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.38
    win_rate: 0.57
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.55
    - name: Runeforged Hammer
      pick_rate: 0.1
      win_rate: 0.61
  - name: Stampede
    pick_rate: 0.22
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.55
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.58
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.65
  - name: Shell of Rebuke
    pick_rate: 0.16
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.18
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.63
  - name: Draconic Scale
    pick_rate: 0.04
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.69
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.57
  - name: Sage's Ring
    pick_rate: 0.1
    win_rate: 0.61
    alternates:
    - name: Engraved Guard
      pick_rate: 0.09
      win_rate: 0.66
    - name: Medal of Defense
      pick_rate: 0.09
      win_rate: 0.68
  community_starters:
  - name: Selflessness
    pick_rate: 0.33
    win_rate: 0.57
  - name: Heroism
    pick_rate: 0.15
    win_rate: 0.64
  - name: Warrior's Axe
    pick_rate: 0.15
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-11-04'
  god_win_rate: 0.5574636723910171
  god_matches_won: 422
  god_matches_played: 757
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shield Splitter,
    Berserker''s Shield, Runeforged Hammer, Shield of the Phoenix, Breastplate of
    Valor, Hydra''s Lament, Oni Hunter''s Garb, Erosion, The Reaper, Eye of Providence,
    Shifter''s Shield, Screeching Gargoyle, Midgardian Mail, Stone of Binding, Leviathan''s
    Hide, Arondight, Hide of the Nemean Lion, Wyrmskin Hide, Magi''s Cloak, Mantle
    Of Discord, Avenging Blade, Gladiator''s Shield, Tyrfing, Draconic Scale, The
    Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.31
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.55
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.55
      pick: 0.25
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, The Reaper, Jotunn''s
    Revenge, Berserker''s Shield, Runeforged Hammer, Shield Splitter, Phoenix Feather,
    Yogi''s Necklace, Breastplate of Valor, Chandra''s Grace, Hydra''s Lament, Oni
    Hunter''s Garb, Erosion, Bloodforge, Eye of Providence, Regrowth Striders, Shifter''s
    Shield, Glorious Pridwen, Midgardian Mail, Screeching Gargoyle, Leviathan''s Hide,
    Avenging Blade, Hide of the Nemean Lion, Wyrmskin Hide, Arondight, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.29
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.79
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Screeching Gargoyle,
    The Reaper, Stone of Binding, Berserker''s Shield, Avenging Blade, Shield Splitter,
    Runeforged Hammer, Void Stone, The Crusher, Void Shield, Breastplate of Valor,
    Heartseeker, Shield of the Phoenix, Titan''s Bane, Hydra''s Lament, Oni Hunter''s
    Garb, Erosion, Eye of Providence, Shifter''s Shield, Midgardian Mail, Avatar''s
    Parashu, Leviathan''s Hide, Arondight, Hide of the Nemean Lion, Draconic Scale.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.63
    Stone of Binding:
      total: 0.54
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.55
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Tyrfing, Jotunn''s
    Revenge, Golden Blade, Shield Splitter, Breastplate of Valor, Runeforged Hammer,
    Shield of the Phoenix, Oni Hunter''s Garb, Hydra''s Lament, Shogun''s Ofuda, Pharaoh''s
    Curse, Toxic Blade, Screeching Gargoyle, Erosion, Eye of Providence, The Reaper,
    Midgardian Mail, Lernaean Bow, Shifter''s Shield, Dominance, Silverbranch Bow,
    Stone of Binding, Leviathan''s Hide, Tekko-Kagi, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.22
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Jotunn''s Revenge,
    Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix, Berserker''s Shield,
    Hydra''s Lament, Screeching Gargoyle, Shield Splitter, Runeforged Hammer, Gladiator''s
    Shield, Oni Hunter''s Garb, Arondight, Prophetic Cloak, Erosion, Eye of Providence,
    Chandra''s Grace, Shifter''s Shield, Midgardian Mail, The Reaper, Stone of Binding,
    Regrowth Striders, Leviathan''s Hide, Eye of Erebus, Hide of the Nemean Lion,
    Magi''s Cloak, Mantle Of Discord, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.44
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.55
      pick: 0.25
      fit: 0.58
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Shield
    Splitter, Berserker''s Shield, Shield of the Phoenix, Breastplate of Valor, Runeforged
    Hammer, Hydra''s Lament, Draconic Scale, Oni Hunter''s Garb, Erosion, The Reaper,
    Eye of Providence, Shifter''s Shield, Screeching Gargoyle, Midgardian Mail, Stone
    of Binding, Leviathan''s Hide, Arondight, Hide of the Nemean Lion, Wyrmskin Hide,
    Magi''s Cloak, Mantle Of Discord, Avenging Blade, Gladiator''s Shield, Tyrfing,
    The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.31
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.55
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.55
      pick: 0.25
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
