---
type: smite-build
god: Nike
mode: Conquest
builds:
- source: community
  aspect: Aspect of Victorious Conquest
  aspect_pick_rate: 0.67
  aspect_win_rate: 0.58
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.35
    win_rate: 0.6
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.24
      win_rate: 0.58
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.54
  - name: Transcendence
    pick_rate: 0.29
    win_rate: 0.6
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.16
      win_rate: 0.55
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.49
  - name: The Crusher
    pick_rate: 0.23
    win_rate: 0.59
    alternates:
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.6
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.55
  - name: Heartseeker
    pick_rate: 0.35
    win_rate: 0.58
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.52
    - name: The Crusher
      pick_rate: 0.07
      win_rate: 0.61
  - name: Avatar's Parashu
    pick_rate: 0.1
    win_rate: 0.62
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.68
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.64
  - name: Skeggox
    pick_rate: 0.11
    win_rate: 0.55
    alternates:
    - name: Avatar's Parashu
      pick_rate: 0.08
      win_rate: 0.75
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.76
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.35
    win_rate: 0.65
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.61
  - name: Conduit Gem
    pick_rate: 0.16
    win_rate: 0.48
  source_url: https://smitebrain.com/gods/nike/
  last_verified: '2026-11-04'
  god_win_rate: 0.5653923541247485
  god_matches_won: 843
  god_matches_played: 1491
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
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
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
    this god: Amanita Charm, Kinetic Cuirass, Genji''s Guard, Shield Splitter, Berserker''s
    Shield, Breastplate of Valor, Shield of the Phoenix, Freya''s Tears, Draconic
    Scale, Runeforged Hammer, Hydra''s Lament, Erosion, Oni Hunter''s Garb, Eye of
    Providence, The Reaper, Screeching Gargoyle, Midgardian Mail, Stone of Binding,
    Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean Lion,
    Arondight, Wyrmskin Hide, Gladiator''s Shield, Tyrfing, Avenging Blade, Prophetic
    Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.58
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.35
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.62
    Shield Splitter:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.58
    Titan's Bane:
      total: 0.57
      efficiency: 0.48
      win: 0.76
      pick: 0.22
      fit: 0.35
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Jotunn's Revenge
  - Titan's Bane
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
  - Titan's Bane
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, The Reaper, Genji''s
    Guard, Berserker''s Shield, Shield Splitter, Phoenix Feather, Yogi''s Necklace,
    Runeforged Hammer, Breastplate of Valor, Chandra''s Grace, Hydra''s Lament, Draconic
    Scale, Oni Hunter''s Garb, Freya''s Tears, Erosion, Bloodforge, Eye of Providence,
    Regrowth Striders, Glorious Pridwen, Midgardian Mail, Screeching Gargoyle, Leviathan''s
    Hide, Avenging Blade, Hide of the Nemean Lion, Wyrmskin Hide, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.58
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.6
      pick: 0.35
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.79
    Titan's Bane:
      total: 0.57
      efficiency: 0.48
      win: 0.76
      pick: 0.22
      fit: 0.36
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Jotunn's Revenge
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Kinetic Cuirass, Genji''s Guard, Screeching Gargoyle,
    The Reaper, Stone of Binding, Berserker''s Shield, Shield Splitter, Avenging Blade,
    Void Stone, Void Shield, Breastplate of Valor, Shield of the Phoenix, Runeforged
    Hammer, Hydra''s Lament, Freya''s Tears, Oni Hunter''s Garb, Draconic Scale, Erosion,
    Eye of Providence, Midgardian Mail, Leviathan''s Hide, Magi''s Cloak, Mantle Of
    Discord.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.64
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.58
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.35
      fit: 0.54
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.49
    Titan's Bane:
      total: 0.6
      efficiency: 0.48
      win: 0.76
      pick: 0.22
      fit: 0.53
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Jotunn's Revenge
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Genji''s Guard, Kinetic Cuirass,
    Tyrfing, Golden Blade, Shield Splitter, Breastplate of Valor, Shield of the Phoenix,
    Freya''s Tears, Oni Hunter''s Garb, Draconic Scale, Runeforged Hammer, Hydra''s
    Lament, Shogun''s Ofuda, Pharaoh''s Curse, Erosion, Screeching Gargoyle, Eye of
    Providence, Toxic Blade, Midgardian Mail, The Reaper, Stone of Binding, Lernaean
    Bow, Dominance, Leviathan''s Hide, Silverbranch Bow, Magi''s Cloak.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.35
      fit: 0.23
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.54
    Titan's Bane:
      total: 0.56
      efficiency: 0.48
      win: 0.76
      pick: 0.22
      fit: 0.24
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Jotunn's Revenge
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Amanita Charm, Kinetic
    Cuirass, Breastplate of Valor, Shield of the Phoenix, Freya''s Tears, Berserker''s
    Shield, Screeching Gargoyle, Hydra''s Lament, Shield Splitter, Gladiator''s Shield,
    Draconic Scale, Oni Hunter''s Garb, Prophetic Cloak, Arondight, Erosion, Eye of
    Providence, Runeforged Hammer, Midgardian Mail, Stone of Binding, Chandra''s Grace,
    Leviathan''s Hide, Regrowth Striders, The Reaper, Magi''s Cloak, Mantle Of Discord,
    Hide of the Nemean Lion, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.58
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.6
      pick: 0.35
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.51
    Titan's Bane:
      total: 0.55
      efficiency: 0.48
      win: 0.76
      pick: 0.22
      fit: 0.22
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Jotunn's Revenge
  - Titan's Bane
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
  - Freya's Tears
  - Jotunn's Revenge
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Genji''s Guard, Shield
    Splitter, Freya''s Tears, Berserker''s Shield, Breastplate of Valor, Shield of
    the Phoenix, Draconic Scale, Runeforged Hammer, Hydra''s Lament, Erosion, Oni
    Hunter''s Garb, Eye of Providence, The Reaper, Screeching Gargoyle, Midgardian
    Mail, Stone of Binding, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Hide
    of the Nemean Lion, Arondight, Wyrmskin Hide, Gladiator''s Shield, Tyrfing, Avenging
    Blade, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.58
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.35
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.62
    Shield Splitter:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.52
      pick: 0.12
      fit: 0.51
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  starter: *id001
---
