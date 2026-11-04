---
type: smite-build
god: Nike
mode: Conquest
builds:
- source: community
  aspect: Aspect of Victorious Conquest
  aspect_pick_rate: 1.0
  aspect_win_rate: 0.5
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 1.0
    win_rate: 0.5
  - name: Arondight
    pick_rate: 0.5
    win_rate: 0.0
    alternates:
    - name: Avatar's Parashu
      pick_rate: 0.5
      win_rate: 1.0
  - name: The Crusher
    pick_rate: 1.0
    win_rate: 0.5
  - name: Heartseeker
    pick_rate: 1.0
    win_rate: 0.5
  - name: Mote of Chaos
    pick_rate: 0.5
    win_rate: 0.0
    alternates:
    - name: Time-lock Aegis
      pick_rate: 0.5
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.5
    win_rate: 1.0
  - name: Conduit Gem
    pick_rate: 0.5
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/nike/
  last_verified: '2026-11-04'
  god_win_rate: 0.5
  god_matches_won: 1
  god_matches_played: 2
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Avatar's Parashu
  - Shield Splitter
  - Time-lock Aegis
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield Splitter, Genji''s Guard, Kinetic Cuirass, Berserker''s
    Shield, Freya''s Tears, Breastplate of Valor, Runeforged Hammer, Hydra''s Lament,
    Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Oni Hunter''s
    Garb, The Reaper, Stone of Binding, Screeching Gargoyle, Midgardian Mail, Magi''s
    Cloak, Titan''s Bane, Shifter''s Shield, Avenging Blade, Mantle Of Discord, Leviathan''s
    Hide, Wyrmskin Hide, Prophetic Cloak, Ancile, Sanguine Lash.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.5
      pick: 1.0
      fit: 0.39
    Avatar's Parashu:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.68
      fit: 0.25
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.58
    Time-lock Aegis:
      total: 0.63
      efficiency: 0.21
      win: 1.0
      pick: 1.0
      fit: 0.37
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Jotunn's Revenge
  - Avatar's Parashu
  - Time-lock Aegis
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Avatar's Parashu
  - Shield of the Phoenix
  - Time-lock Aegis
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
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
    this god: Amanita Charm, Shield of the Phoenix, The Reaper, Kinetic Cuirass, Berserker''s
    Shield, Shield Splitter, Genji''s Guard, Runeforged Hammer, Freya''s Tears, Phoenix
    Feather, Breastplate of Valor, Bloodforge, Yogi''s Necklace, Hydra''s Lament,
    Chandra''s Grace, Oni Hunter''s Garb, Erosion, Eye of Providence, Avenging Blade,
    Draconic Scale, Regrowth Striders, Glorious Pridwen, Midgardian Mail, Titan''s
    Bane, Leviathan''s Hide, Screeching Gargoyle, Wyrmskin Hide, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.5
      pick: 1.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.6
    Avatar's Parashu:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.68
      fit: 0.26
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.79
    Time-lock Aegis:
      total: 0.62
      efficiency: 0.21
      win: 1.0
      pick: 1.0
      fit: 0.31
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Jotunn's Revenge
  - Avatar's Parashu
  - Time-lock Aegis
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Avatar's Parashu
  - The Crusher
  - Heartseeker
  - Time-lock Aegis
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Genji''s Guard, Screeching Gargoyle,
    Avenging Blade, The Reaper, Shield Splitter, Berserker''s Shield, Kinetic Cuirass,
    Titan''s Bane, Freya''s Tears, Void Stone, Void Shield, Breastplate of Valor,
    Runeforged Hammer, Hydra''s Lament, Oni Hunter''s Garb, Erosion, Shield of the
    Phoenix, Eye of Providence, Tekko-Kagi, Draconic Scale, Midgardian Mail, Magi''s
    Cloak, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.5
      pick: 1.0
      fit: 0.54
    Avatar's Parashu:
      total: 0.7
      efficiency: 0.44
      win: 1.0
      pick: 0.68
      fit: 0.43
    The Crusher:
      total: 0.53
      efficiency: 0.49
      win: 0.5
      pick: 1.0
      fit: 0.53
    Heartseeker:
      total: 0.52
      efficiency: 0.43
      win: 0.5
      pick: 1.0
      fit: 0.63
    Time-lock Aegis:
      total: 0.62
      efficiency: 0.21
      win: 1.0
      pick: 1.0
      fit: 0.28
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Jotunn's Revenge
  - Avatar's Parashu
  - The Crusher
  - Heartseeker
  - Time-lock Aegis
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Avatar's Parashu
  - Tyrfing
  - Time-lock Aegis
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Genji''s Guard, Kinetic Cuirass,
    Golden Blade, Shield Splitter, Freya''s Tears, Breastplate of Valor, Tyrfing,
    Runeforged Hammer, Tekko-Kagi, Pharaoh''s Curse, Hydra''s Lament, Lernaean Bow,
    Toxic Blade, Oni Hunter''s Garb, Shogun''s Ofuda, Silverbranch Bow, Erosion, Shield
    of the Phoenix, Eye of Providence, Stone of Binding, Screeching Gargoyle, Draconic
    Scale, Midgardian Mail, The Reaper, Magi''s Cloak, Riptalon, Titan''s Bane.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.5
      pick: 1.0
      fit: 0.23
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.44
    Avatar's Parashu:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.68
      fit: 0.14
    Tyrfing:
      total: 0.48
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.54
    Time-lock Aegis:
      total: 0.61
      efficiency: 0.21
      win: 1.0
      pick: 1.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Avatar's Parashu
  - Time-lock Aegis
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Avatar's Parashu
  - Freya's Tears
  - Time-lock Aegis
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Freya''s Tears, Amanita
    Charm, Breastplate of Valor, Berserker''s Shield, Kinetic Cuirass, Hydra''s Lament,
    Shield of the Phoenix, Shield Splitter, Screeching Gargoyle, Runeforged Hammer,
    Prophetic Cloak, Oni Hunter''s Garb, Erosion, Eye of Providence, Draconic Scale,
    Stone of Binding, Gladiator''s Shield, Midgardian Mail, Magi''s Cloak, Mantle
    Of Discord, Leviathan''s Hide, The Reaper, Shifter''s Shield, Regrowth Striders,
    Chandra''s Grace, Eye of Erebus, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.5
      pick: 1.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.68
      fit: 0.12
    Freya's Tears:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.59
    Time-lock Aegis:
      total: 0.62
      efficiency: 0.21
      win: 1.0
      pick: 1.0
      fit: 0.3
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Jotunn's Revenge
  - Avatar's Parashu
  - Time-lock Aegis
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Berserker's Shield
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
    Underrated for this god: Amanita Charm, Shield Splitter, Genji''s Guard, Kinetic
    Cuirass, Berserker''s Shield, Freya''s Tears, Breastplate of Valor, Runeforged
    Hammer, Hydra''s Lament, Erosion, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Oni Hunter''s Garb, The Reaper, Stone of Binding, Screeching Gargoyle,
    Midgardian Mail, Magi''s Cloak, Titan''s Bane, Shifter''s Shield, Avenging Blade,
    Mantle Of Discord, Leviathan''s Hide, Wyrmskin Hide, Prophetic Cloak, Ancile,
    Sanguine Lash.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.5
      pick: 1.0
      fit: 0.39
    Berserker's Shield:
      total: 0.51
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
