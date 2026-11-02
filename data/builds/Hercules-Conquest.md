---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.22
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.2
    win_rate: 0.39
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.44
    - name: Runeforged Hammer
      pick_rate: 0.1
      win_rate: 0.61
  - name: Breastplate of Valor
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.48
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.36
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.54
    - name: Regrowth Striders
      pick_rate: 0.05
      win_rate: 0.6
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.64
    - name: Brawler’s Beat Stick
      pick_rate: 0.05
      win_rate: 0.58
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.64
    alternates:
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.5
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.4
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.42
    win_rate: 0.61
  - name: Bumba's Cudgel
    pick_rate: 0.33
    win_rate: 0.39
  - name: War Banner
    pick_rate: 0.06
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-11-02'
  god_win_rate: 0.4838709677419355
  god_matches_won: 150
  god_matches_played: 310
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield Splitter, Kinetic Cuirass,
    Berserker''s Shield, Erosion, Eye of Providence, Hydra''s Lament, Draconic Scale,
    Shield of the Phoenix, Stone of Binding, Oni Hunter''s Garb, Magi''s Cloak, Midgardian
    Mail, Avenging Blade, Wyrmskin Hide, Mantle Of Discord, Titan''s Bane, Screeching
    Gargoyle, Leviathan''s Hide, Arondight, Ancile, Prophetic Cloak, Stampede, Hide
    of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.33
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.22
      fit: 0.33
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.67
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.1
      fit: 0.51
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Shield Splitter
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Shield Splitter
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield of the Phoenix, Shield Splitter,
    Kinetic Cuirass, Berserker''s Shield, Regrowth Striders, Phoenix Feather, The
    Reaper, Yogi''s Necklace, Hydra''s Lament, Erosion, Eye of Providence, Draconic
    Scale, Chandra''s Grace, Avenging Blade, Oni Hunter''s Garb, Wyrmskin Hide, Midgardian
    Mail, Titan''s Bane, Glorious Pridwen, Leviathan''s Hide, Stone of Binding, Arondight,
    Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.3
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.61
      pick: 0.22
      fit: 0.3
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.61
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.82
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.1
      fit: 0.57
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Runeforged Hammer, Stone of Binding, Shield Splitter,
    Avenging Blade, Screeching Gargoyle, Titan''s Bane, Berserker''s Shield, Kinetic
    Cuirass, Void Stone, Void Shield, The Crusher, Heartseeker, The Reaper, Hydra''s
    Lament, Erosion, Eye of Providence, Tekko-Kagi, Draconic Scale, Oni Hunter''s
    Garb, Shield of the Phoenix, Midgardian Mail, Magi''s Cloak, Mantle Of Discord,
    Pendulum Blade.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.24
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.61
      pick: 0.22
      fit: 0.24
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.48
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.56
      win: 0.61
      pick: 0.1
      fit: 0.4
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
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
    this god: Berserker''s Shield, Amanita Charm, Runeforged Hammer, Kinetic Cuirass,
    Golden Blade, Shield Splitter, Tyrfing, Tekko-Kagi, Pharaoh''s Curse, Lernaean
    Bow, Toxic Blade, Shogun''s Ofuda, Silverbranch Bow, Hydra''s Lament, Erosion,
    Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Shield
    of the Phoenix, Midgardian Mail, Magi''s Cloak, Screeching Gargoyle, The Reaper,
    Riptalon, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.21
    Berserker's Shield:
      total: 0.57
      efficiency: 0.75
      win: 0.54
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.61
      pick: 0.22
      fit: 0.21
    Tyrfing:
      total: 0.5
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  flex_slots:
  - Berserker's Shield
  - Shield of the Phoenix
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Berserker''s Shield, Shield of the Phoenix, Hydra''s Lament,
    Shield Splitter, Screeching Gargoyle, Regrowth Striders, Arondight, Prophetic
    Cloak, Erosion, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone
    of Binding, Oni Hunter''s Garb, Midgardian Mail, Magi''s Cloak, Mantle Of Discord,
    Chandra''s Grace, Leviathan''s Hide, Eye of Erebus, Glorious Pridwen, Titan''s
    Bane.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.67
      win: 0.54
      pick: 0.0
      fit: 0.29
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.61
      pick: 0.22
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.61
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.56
      win: 0.61
      pick: 0.1
      fit: 0.32
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Shield Splitter, Kinetic Cuirass, Berserker''s
    Shield, Runeforged Hammer, Erosion, Eye of Providence, Hydra''s Lament, Draconic
    Scale, Shield of the Phoenix, Stone of Binding, Oni Hunter''s Garb, Magi''s Cloak,
    Midgardian Mail, Avenging Blade, Wyrmskin Hide, Mantle Of Discord, Titan''s Bane,
    Screeching Gargoyle, Leviathan''s Hide, Arondight, Ancile, Hide of the Nemean
    Lion, Prophetic Cloak, Stampede.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.67
      win: 0.54
      pick: 0.0
      fit: 0.38
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.33
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.69
      win: 0.39
      pick: 0.2
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Runeforged Hammer
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Erosion, Kinetic Cuirass, Berserker''s
    Shield, Shield Splitter, Shield of the Phoenix, Stampede, Void Stone, Void Shield,
    Spectral Armor, Doublet of Binding, Eye of Providence, Draconic Scale, Phoenix
    Feather, Hydra''s Lament, Oni Hunter''s Garb, Shogun''s Ofuda, Pharaoh''s Curse,
    Avenging Blade, Midgardian Mail, Yogi''s Necklace, Mystical Mail, Wyrmskin Hide,
    Sanguine Lash.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.29
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.61
      pick: 0.22
      fit: 0.29
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.71
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.1
      fit: 0.58
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Erosion, Shield of the Phoenix, Shield
    Splitter, Kinetic Cuirass, Berserker''s Shield, Stampede, Void Stone, Void Shield,
    Spectral Armor, Phoenix Feather, Doublet of Binding, The Reaper, Yogi''s Necklace,
    Hydra''s Lament, Eye of Providence, Draconic Scale, Chandra''s Grace, Avenging
    Blade, Oni Hunter''s Garb, Shogun''s Ofuda, Pharaoh''s Curse, Sanguine Lash, Wyrmskin
    Hide, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.3
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.61
      pick: 0.22
      fit: 0.3
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.82
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.1
      fit: 0.57
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  - Void Shield
  - Void Stone
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Void Stone, Void Shield, Runeforged Hammer, Erosion,
    Avenging Blade, Berserker''s Shield, The Reaper, Kinetic Cuirass, Stone of Binding,
    Titan''s Bane, Screeching Gargoyle, Shield Splitter, Shield of the Phoenix, Stampede,
    Spectral Armor, Doublet of Binding, The Crusher, Heartseeker, Hydra''s Lament,
    Phoenix Feather, Yogi''s Necklace, Eye of Providence, Oni Hunter''s Garb, Shogun''s
    Ofuda, Pharaoh''s Curse.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.21
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.61
      pick: 0.22
      fit: 0.21
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.56
      win: 0.61
      pick: 0.1
      fit: 0.45
    Void Shield:
      total: 0.55
      efficiency: 0.46
      win: 0.54
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.56
      efficiency: 0.46
      win: 0.54
      pick: 0.0
      fit: 1.0
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Breastplate of Valor
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Pharaoh's Curse
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Pharaoh''s Curse, Runeforged Hammer,
    Shogun''s Ofuda, Erosion, Golden Blade, Kinetic Cuirass, Stampede, Shield of the
    Phoenix, Void Stone, Void Shield, Shield Splitter, The Reaper, Spectral Armor,
    Riptalon, Tyrfing, Doublet of Binding, Umbral Link, Sanguine Lash, Toxic Blade,
    Tekko-Kagi, Yogi''s Necklace, Phoenix Feather, Lernaean Bow, Oni Hunter''s Garb.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.75
      win: 0.54
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.19
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.61
      pick: 0.22
      fit: 0.19
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Breastplate of Valor
  - Shield of the Phoenix
  - Runeforged Hammer
  - Erosion
  flex_slots:
  - Runeforged Hammer
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield of the Phoenix,
    Erosion, Runeforged Hammer, Regrowth Striders, Berserker''s Shield, Kinetic Cuirass,
    Stampede, Void Stone, Hydra''s Lament, Void Shield, Chandra''s Grace, Screeching
    Gargoyle, Shield Splitter, Spectral Armor, Doublet of Binding, Glorious Pridwen,
    Arondight, Phoenix Feather, Yogi''s Necklace, Eye of Providence, Gladiator''s
    Shield, Oni Hunter''s Garb, Shogun''s Ofuda, Pharaoh''s Curse, Prophetic Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.67
      win: 0.54
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.6
      pick: 0.22
      fit: 0.45
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.61
      pick: 0.22
      fit: 0.45
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.84
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.56
      win: 0.61
      pick: 0.1
      fit: 0.38
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  - Erosion
  flex_slots:
  - Berserker's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Erosion, Kinetic Cuirass, Berserker''s
    Shield, Shield Splitter, Shield of the Phoenix, Stampede, Void Stone, Void Shield,
    Runeforged Hammer, Spectral Armor, Doublet of Binding, Eye of Providence, Draconic
    Scale, Phoenix Feather, Hydra''s Lament, Oni Hunter''s Garb, Shogun''s Ofuda,
    Pharaoh''s Curse, Avenging Blade, Midgardian Mail, Yogi''s Necklace, Mystical
    Mail, Wyrmskin Hide, Sanguine Lash.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.67
      win: 0.54
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.69
      win: 0.39
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.71
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
  aspect: Aspect of Preservation
---
