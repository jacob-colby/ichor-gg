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
    pick_rate: 0.37
    win_rate: 0.56
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.55
    - name: Runeforged Hammer
      pick_rate: 0.11
      win_rate: 0.61
  - name: Stampede
    pick_rate: 0.22
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.56
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.58
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.65
  - name: Shell of Rebuke
    pick_rate: 0.17
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.18
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.62
  - name: Draconic Scale
    pick_rate: 0.04
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.69
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.58
  - name: Sage's Ring
    pick_rate: 0.1
    win_rate: 0.59
    alternates:
    - name: Engraved Guard
      pick_rate: 0.09
      win_rate: 0.66
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 0.67
  community_starters:
  - name: Selflessness
    pick_rate: 0.32
    win_rate: 0.57
  - name: Warrior's Axe
    pick_rate: 0.16
    win_rate: 0.51
  - name: Heroism
    pick_rate: 0.15
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-11-02'
  god_win_rate: 0.5558546433378196
  god_matches_won: 413
  god_matches_played: 743
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
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
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter,
    Runeforged Hammer, Berserker''s Shield, Breastplate of Valor, Hydra''s Lament,
    Erosion, Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb, Screeching
    Gargoyle, Shifter''s Shield, Stone of Binding, Titan''s Bane, Midgardian Mail,
    Wyrmskin Hide, Magi''s Cloak, Avenging Blade, Leviathan''s Hide, Arondight, Mantle
    Of Discord, Prophetic Cloak, Draconic Scale, Ancile, Hide of the Nemean Lion,
    Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.2
      fit: 0.35
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.65
    Shield Splitter:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.62
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.11
      fit: 0.51
    Amanita Charm:
      total: 0.56
      efficiency: 0.62
      win: 0.57
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Genji's Guard
  - Runeforged Hammer
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Runeforged
    Hammer, Kinetic Cuirass, Berserker''s Shield, Shield Splitter, Phoenix Feather,
    Breastplate of Valor, Chandra''s Grace, Yogi''s Necklace, Hydra''s Lament, The
    Reaper, Erosion, Eye of Providence, Oni Hunter''s Garb, Glorious Pridwen, Regrowth
    Striders, Midgardian Mail, Avenging Blade, Wyrmskin Hide, Shifter''s Shield, Titan''s
    Bane, Screeching Gargoyle, Leviathan''s Hide, Arondight, Stone of Binding, Draconic
    Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.2
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.84
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.11
      fit: 0.55
    Amanita Charm:
      total: 0.6
      efficiency: 0.62
      win: 0.57
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Genji's Guard
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Screeching Gargoyle, Stone of
    Binding, Titan''s Bane, Runeforged Hammer, Avenging Blade, Kinetic Cuirass, Berserker''s
    Shield, Shield Splitter, Void Stone, Void Shield, Breastplate of Valor, Heartseeker,
    The Crusher, Hydra''s Lament, The Reaper, Shield of the Phoenix, Erosion, Oni
    Hunter''s Garb, Tekko-Kagi, Pendulum Blade, Eye of Providence, Midgardian Mail,
    Magi''s Cloak, Leviathan''s Hide, Shifter''s Shield, Draconic Scale.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.53
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.2
      fit: 0.25
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.6
    Titan's Bane:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.57
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Jotunn''s Revenge, Golden Blade,
    Kinetic Cuirass, Runeforged Hammer, Breastplate of Valor, Shield Splitter, Tyrfing,
    Pharaoh''s Curse, Toxic Blade, Tekko-Kagi, Silverbranch Bow, Shogun''s Ofuda,
    Hydra''s Lament, Lernaean Bow, Oni Hunter''s Garb, Riptalon, Shield of the Phoenix,
    Erosion, Screeching Gargoyle, Eye of Providence, Stone of Binding, Midgardian
    Mail, The Reaper, Titan''s Bane, Magi''s Cloak, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.56
      pick: 0.2
      fit: 0.22
    Berserker's Shield:
      total: 0.57
      efficiency: 0.7
      win: 0.57
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.5
      efficiency: 0.46
      win: 0.57
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.57
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
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s Shield,
    Hydra''s Lament, Screeching Gargoyle, Runeforged Hammer, Shield Splitter, Prophetic
    Cloak, Arondight, Gladiator''s Shield, Erosion, Oni Hunter''s Garb, Eye of Providence,
    Chandra''s Grace, Stone of Binding, Midgardian Mail, Magi''s Cloak, Glorious Pridwen,
    Leviathan''s Hide, Shifter''s Shield, Regrowth Striders, Eye of Erebus, Mantle
    Of Discord, Titan''s Bane, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.25
      fit: 0.63
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.57
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Berserker''s Shield, Breastplate of Valor, Runeforged Hammer, Hydra''s
    Lament, Erosion, Shield of the Phoenix, Eye of Providence, Draconic Scale, Oni
    Hunter''s Garb, Screeching Gargoyle, Shifter''s Shield, Stone of Binding, Titan''s
    Bane, Midgardian Mail, Wyrmskin Hide, Magi''s Cloak, Avenging Blade, Leviathan''s
    Hide, Arondight, Mantle Of Discord, Prophetic Cloak, Ancile, Hide of the Nemean
    Lion, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.2
      fit: 0.35
    Berserker's Shield:
      total: 0.53
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.65
    Shield Splitter:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.62
      win: 0.57
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Genji's Guard
  starter: *id001
---
