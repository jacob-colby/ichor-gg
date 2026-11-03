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
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.55
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.16
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
      win_rate: 0.57
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
      win_rate: 0.58
  - name: Sage's Ring
    pick_rate: 0.1
    win_rate: 0.59
    alternates:
    - name: Engraved Guard
      pick_rate: 0.09
      win_rate: 0.66
    - name: Medal of Defense
      pick_rate: 0.09
      win_rate: 0.68
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
  last_verified: '2026-11-03'
  god_win_rate: 0.5577689243027888
  god_matches_won: 420
  god_matches_played: 753
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
  - Runeforged Hammer
  - Kinetic Cuirass
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
    this god: Amanita Charm, Jotunn''s Revenge, Shield Splitter, Runeforged Hammer,
    Kinetic Cuirass, Berserker''s Shield, Breastplate of Valor, Hydra''s Lament, Erosion,
    Shield of the Phoenix, Eye of Providence, The Reaper, Oni Hunter''s Garb, Titan''s
    Bane, Avenging Blade, Stone of Binding, Screeching Gargoyle, Midgardian Mail,
    Arondight, Magi''s Cloak, Shifter''s Shield, Leviathan''s Hide, Wyrmskin Hide,
    Mantle Of Discord, Sanguine Lash, Ancile, The Crusher, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.2
      fit: 0.31
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.1
      fit: 0.47
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.5
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
  - Genji's Guard
  - Kinetic Cuirass
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
    this god: Amanita Charm, Shield of the Phoenix, The Reaper, Jotunn''s Revenge,
    Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Berserker''s Shield, Phoenix
    Feather, Breastplate of Valor, Bloodforge, Hydra''s Lament, Yogi''s Necklace,
    Chandra''s Grace, Oni Hunter''s Garb, Erosion, Eye of Providence, Avenging Blade,
    Regrowth Striders, Midgardian Mail, Glorious Pridwen, Titan''s Bane, Arondight,
    Leviathan''s Hide, Wyrmskin Hide, Screeching Gargoyle, Shifter''s Shield, Draconic
    Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.2
      fit: 0.29
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.79
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.1
      fit: 0.51
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Genji's Guard
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Avenging Blade
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Screeching Gargoyle, The Reaper,
    Stone of Binding, Avenging Blade, Runeforged Hammer, Titan''s Bane, Berserker''s
    Shield, Shield Splitter, Kinetic Cuirass, Void Stone, Void Shield, Breastplate
    of Valor, The Crusher, Hydra''s Lament, Heartseeker, Oni Hunter''s Garb, Shield
    of the Phoenix, Tekko-Kagi, Erosion, Eye of Providence, Midgardian Mail, Arondight,
    Pendulum Blade, Magi''s Cloak, Leviathan''s Hide, Draconic Scale.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.63
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.66
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Jotunn''s Revenge, Golden Blade,
    Kinetic Cuirass, Runeforged Hammer, Shield Splitter, Tyrfing, Breastplate of Valor,
    Tekko-Kagi, Pharaoh''s Curse, Hydra''s Lament, Lernaean Bow, Toxic Blade, Silverbranch
    Bow, Oni Hunter''s Garb, Shogun''s Ofuda, Shield of the Phoenix, Erosion, Eye
    of Providence, Screeching Gargoyle, The Reaper, Midgardian Mail, Stone of Binding,
    Riptalon, Titan''s Bane, Dominance, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.2
      fit: 0.22
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.58
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.52
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Berserker's Shield
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Breastplate of Valor, Berserker''s Shield, Kinetic Cuirass, Hydra''s Lament, Shield
    of the Phoenix, Runeforged Hammer, Screeching Gargoyle, Shield Splitter, Arondight,
    Prophetic Cloak, Oni Hunter''s Garb, Erosion, Eye of Providence, Gladiator''s
    Shield, Midgardian Mail, Stone of Binding, Magi''s Cloak, The Reaper, Leviathan''s
    Hide, Chandra''s Grace, Eye of Erebus, Regrowth Striders, Mantle Of Discord, Shifter''s
    Shield, Titan''s Bane, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.57
      pick: 0.2
      fit: 0.44
    Berserker's Shield:
      total: 0.53
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.26
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.55
      pick: 0.25
      fit: 0.58
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
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
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
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
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Shield Splitter, Kinetic
    Cuirass, Berserker''s Shield, Runeforged Hammer, Breastplate of Valor, Hydra''s
    Lament, Erosion, Shield of the Phoenix, Eye of Providence, The Reaper, Oni Hunter''s
    Garb, Draconic Scale, Titan''s Bane, Avenging Blade, Stone of Binding, Screeching
    Gargoyle, Midgardian Mail, Arondight, Magi''s Cloak, Shifter''s Shield, Leviathan''s
    Hide, Wyrmskin Hide, Mantle Of Discord, Sanguine Lash, Ancile, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.2
      fit: 0.31
    Berserker's Shield:
      total: 0.54
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  starter: *id001
---
