---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.47
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.45
    win_rate: 0.56
    alternates:
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.66
    - name: Circe's Hexstone
      pick_rate: 0.07
      win_rate: 0.65
  - name: Stampede
    pick_rate: 0.28
    win_rate: 0.45
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.64
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.82
  - name: Shell of Rebuke
    pick_rate: 0.15
    win_rate: 0.71
    alternates:
    - name: Screeching Gargoyle
      pick_rate: 0.11
      win_rate: 0.52
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.51
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.53
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.07
    win_rate: 0.62
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.73
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.56
  - name: Olmec Blue
    pick_rate: 0.1
    win_rate: 0.42
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.89
    - name: Shield
      pick_rate: 0.06
      win_rate: 0.25
  community_starters:
  - name: Selflessness
    pick_rate: 0.29
    win_rate: 0.51
  - name: Heroism
    pick_rate: 0.18
    win_rate: 0.65
  - name: Bluestone Pendant
    pick_rate: 0.09
    win_rate: 0.35
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-11-08'
  god_win_rate: 0.5407725321888412
  god_matches_won: 126
  god_matches_played: 233
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Berserker''s Shield,
    Shield of the Phoenix, Shield Splitter, Gluttonous Grimoire, Breastplate of Valor,
    Soul Gem, Erosion, Eye of Providence, Shifter''s Shield, Oni Hunter''s Garb, Jotunn''s
    Revenge, Stone of Binding, Midgardian Mail, Helm of Darkness, Magi''s Cloak, Mantle
    Of Discord, Leviathan''s Hide, Spear of Desolation, Hide of the Nemean Lion, Helm
    of Radiance, Gladiator''s Shield, Lotus Sickle, Runeforged Hammer, Prophetic Cloak,
    Ancile, Blood-Bound Book, Void Stone, Phoenix Feather, Hydra''s Lament, Void Shield,
    Spectral Armor, The Reaper, Doublet of Binding, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.64
      pick: 0.15
      fit: 0.34
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.69
      efficiency: 0.61
      win: 0.82
      pick: 0.1
      fit: 0.7
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.51
      pick: 0.35
      fit: 0.56
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.62
      pick: 0.15
      fit: 0.6
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Shield of the Phoenix, Soul Gem, Rod
    of Tahuti, Berserker''s Shield, Phoenix Feather, Blood-Bound Book, Gluttonous
    Grimoire, The Reaper, Yogi''s Necklace, Ethereal Staff, Chandra''s Grace, Breastplate
    of Valor, Oni Hunter''s Garb, Erosion, Jotunn''s Revenge, Shield Splitter, Eye
    of Providence, Shifter''s Shield, Regrowth Striders, Midgardian Mail, Glorious
    Pridwen, Bancroft''s Talon, Leviathan''s Hide, Rod of Asclepius, Runeforged Hammer,
    Spear of Desolation, Hide of the Nemean Lion, Soul Locket, Gladiator''s Shield,
    Lotus Sickle, Ancile, Stone of Binding, Helm of Darkness, Void Stone, Helm of
    Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.64
      pick: 0.15
      fit: 0.31
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.69
      efficiency: 0.61
      win: 0.82
      pick: 0.1
      fit: 0.68
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.84
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.62
      pick: 0.15
      fit: 0.58
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Kinetic Cuirass, Rod of Tahuti, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, Jotunn''s Revenge, Stone of Binding, Spear of Desolation, Berserker''s
    Shield, Void Stone, Void Shield, The Reaper, Breastplate of Valor, Shield Splitter,
    Shield of the Phoenix, Obsidian Shard, Avenging Blade, Oni Hunter''s Garb, Spear
    of the Magus, The Crusher, Erosion, Eye of Providence, Heartseeker, Dreamer''s
    Idol, Shifter''s Shield, Midgardian Mail, Titan''s Bane, Lotus Sickle, Helm of
    Radiance, Leviathan''s Hide, Doom Orb, Runeforged Hammer, Blood-Bound Book, Magi''s
    Cloak, Mantle Of Discord, Helm of Darkness, Hide of the Nemean Lion, Hydra''s
    Lament.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.64
      pick: 0.15
      fit: 0.25
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.61
      win: 0.82
      pick: 0.1
      fit: 0.54
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
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
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Berserker''s Shield, Rod of Tahuti, Amanita Charm,
    Tyrfing, Jotunn''s Revenge, Shield Splitter, Golden Blade, Breastplate of Valor,
    Gluttonous Grimoire, Soul Gem, Shield of the Phoenix, Oni Hunter''s Garb, Nimble
    Ring, Runeforged Hammer, Shogun''s Ofuda, Hydra''s Lament, Pharaoh''s Curse, Erosion,
    Spear of Desolation, Eye of Providence, Lotus Sickle, Toxic Blade, Bragi''s Harp,
    Shifter''s Shield, Midgardian Mail, The Reaper, Blood-Bound Book, Helm of Radiance,
    Stone of Binding, Eros'' Bow, Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch
    Bow, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean Lion.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.64
      pick: 0.15
      fit: 0.21
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.61
      win: 0.82
      pick: 0.1
      fit: 0.46
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Rod of Tahuti, Amanita
    Charm, Soul Gem, Jotunn''s Revenge, Breastplate of Valor, Shield of the Phoenix,
    Spear of Desolation, Lotus Sickle, Berserker''s Shield, Hydra''s Lament, Gluttonous
    Grimoire, Shield Splitter, Chronos'' Pendant, Gladiator''s Shield, Oni Hunter''s
    Garb, Prophetic Cloak, Arondight, Erosion, Eye of Providence, Helm of Radiance,
    Runeforged Hammer, Blood-Bound Book, Shifter''s Shield, Gem of Focus, Heartwood
    Charm, Helm of Darkness, Midgardian Mail, Chandra''s Grace, Stone of Binding,
    Leviathan''s Hide, Regrowth Striders, Ancient Signet, Magi''s Cloak, Mantle Of
    Discord, The Reaper, Hide of the Nemean Lion, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.64
      pick: 0.15
      fit: 0.45
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.61
      win: 0.82
      pick: 0.1
      fit: 0.52
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.51
      pick: 0.35
      fit: 0.6
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Kinetic Cuirass, Rod of Tahuti, Berserker''s
    Shield, Amanita Charm, Jotunn''s Revenge, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, The Reaper, Tyrfing, Breastplate of Valor, Runeforged Hammer, Hydra''s
    Lament, Golden Blade, Spear of Desolation, Shield of the Phoenix, The Crusher,
    Oni Hunter''s Garb, Heartseeker, Erosion, Eye of Providence, Tekko-Kagi, Titan''s
    Bane, Death Metal, Shifter''s Shield, Lotus Sickle, Midgardian Mail, Stone of
    Binding, Bragi''s Harp, Helm of Radiance, Blood-Bound Book, Obsidian Shard, Arondight,
    Avenging Blade, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Nimble Ring.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.64
      pick: 0.15
      fit: 0.22
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.61
      win: 0.82
      pick: 0.1
      fit: 0.49
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Draconic Scale
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Berserker''s
    Shield, Shield of the Phoenix, Shield Splitter, Gluttonous Grimoire, Breastplate
    of Valor, Soul Gem, Erosion, Eye of Providence, Shifter''s Shield, Oni Hunter''s
    Garb, Jotunn''s Revenge, Stone of Binding, Midgardian Mail, Helm of Darkness,
    Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Spear of Desolation, Hide
    of the Nemean Lion, Helm of Radiance, Gladiator''s Shield, Lotus Sickle, Runeforged
    Hammer, Prophetic Cloak, Ancile, Blood-Bound Book, Void Stone, Phoenix Feather,
    Hydra''s Lament, Void Shield, Spectral Armor, The Reaper, Doublet of Binding,
    Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.64
      pick: 0.15
      fit: 0.34
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.69
      efficiency: 0.61
      win: 0.82
      pick: 0.1
      fit: 0.7
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.51
      pick: 0.35
      fit: 0.56
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.62
      pick: 0.15
      fit: 0.6
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod
    of Tahuti, Berserker''s Shield, Shield of the Phoenix, Shield Splitter, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Erosion, Eye of Providence, Shifter''s
    Shield, Oni Hunter''s Garb, Jotunn''s Revenge, Stone of Binding, Midgardian Mail,
    Helm of Darkness, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Spear of
    Desolation, Hide of the Nemean Lion, Helm of Radiance, Gladiator''s Shield, Lotus
    Sickle, Runeforged Hammer, Prophetic Cloak, Ancile, Blood-Bound Book, Void Stone,
    Phoenix Feather, Hydra''s Lament, Void Shield, Spectral Armor, The Reaper, Doublet
    of Binding, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.64
      pick: 0.15
      fit: 0.34
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.69
      efficiency: 0.61
      win: 0.82
      pick: 0.1
      fit: 0.7
    Shell of Rebuke:
      total: 0.54
      efficiency: 0.41
      win: 0.71
      pick: 0.23
      fit: 0.43
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.51
      pick: 0.35
      fit: 0.56
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  swaps:
  - added: Shell of Rebuke
    removed: Draconic Scale
    reason: community 71% win over 35 matches (vs 54% on this god), taking the model's
      weakest slot from Draconic Scale
  starter: *id001
---
