---
type: smite-build
god: Amaterasu
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Golden Blade
    pick_rate: 0.32
    win_rate: 0.66
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.22
      win_rate: 0.65
    - name: Berserker's Shield
      pick_rate: 0.2
      win_rate: 0.68
  - name: Berserker's Shield
    pick_rate: 0.3
    win_rate: 0.62
    alternates:
    - name: Golden Blade
      pick_rate: 0.4
      win_rate: 0.66
    - name: Shogun's Ofuda
      pick_rate: 0.11
      win_rate: 0.63
  - name: Kinetic Cuirass
    pick_rate: 0.27
    win_rate: 0.65
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.28
      win_rate: 0.64
    - name: Shogun's Ofuda
      pick_rate: 0.13
      win_rate: 0.67
  - name: Shogun's Ofuda
    pick_rate: 0.17
    win_rate: 0.64
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.18
      win_rate: 0.63
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.62
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.12
      win_rate: 0.71
    - name: Hussar's Wings
      pick_rate: 0.09
      win_rate: 0.67
  - name: Medal of Defense
    pick_rate: 0.09
    win_rate: 0.56
    alternates:
    - name: Hussar's Wings
      pick_rate: 0.08
      win_rate: 0.76
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.68
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.39
    win_rate: 0.65
  - name: Death's Embrace
    pick_rate: 0.24
    win_rate: 0.75
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/amaterasu/
  last_verified: '2026-11-02'
  god_win_rate: 0.6313912009512486
  god_matches_won: 531
  god_matches_played: 841
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
  - Jotunn's Revenge
  - Berserker's Shield
  - Shield Splitter
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Erosion, Runeforged Hammer, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Hydra''s Lament, Oni Hunter''s Garb, Stone of Binding,
    Helm of Darkness, Magi''s Cloak, Midgardian Mail, Screeching Gargoyle, Gluttonous
    Grimoire, Mantle Of Discord, Sundering Echo, Helm of Radiance, Leviathan''s Hide,
    Titan''s Bane, Wyrmskin Hide, Spear of Desolation, Avenging Blade, Prophetic Cloak,
    Ancile, Obsidian Shard, Hide of the Nemean Lion, Soul Gem, Void Stone, Stampede,
    Arondight, Void Shield, Xibalban Effigy, Gladiator''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.38
    Berserker's Shield:
      total: 0.58
      efficiency: 0.63
      win: 0.62
      pick: 0.41
      fit: 0.36
    Shield Splitter:
      total: 0.57
      efficiency: 0.54
      win: 0.65
      pick: 0.0
      fit: 0.61
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.53
      win: 0.65
      pick: 0.42
      fit: 0.67
    Freya's Tears:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.24
      fit: 0.53
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Berserker's Shield
  - Shield of the Phoenix
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Jotunn''s Revenge,
    Genji''s Guard, Shield Splitter, Soul Gem, Phoenix Feather, Runeforged Hammer,
    Yogi''s Necklace, Breastplate of Valor, Chandra''s Grace, Ethereal Staff, The
    Reaper, Erosion, Eye of Providence, Hydra''s Lament, Draconic Scale, Oni Hunter''s
    Garb, Gluttonous Grimoire, Glorious Pridwen, Midgardian Mail, Regrowth Striders,
    Avenging Blade, Sundering Echo, Wyrmskin Hide, Leviathan''s Hide, Titan''s Bane,
    Rod of Asclepius, Stone of Binding, Screeching Gargoyle, Blood-Bound Book, Spear
    of Desolation, Sphere of Negation, Helm of Darkness, Helm of Radiance, Ancile,
    Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.39
    Berserker's Shield:
      total: 0.58
      efficiency: 0.63
      win: 0.62
      pick: 0.41
      fit: 0.38
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.49
      win: 0.65
      pick: 0.0
      fit: 0.81
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.53
      win: 0.65
      pick: 0.42
      fit: 0.65
    Freya's Tears:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.24
      fit: 0.46
    Amanita Charm:
      total: 0.64
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Screeching Gargoyle, Genji''s Guard, Gluttonous Grimoire, Titan''s Bane, Obsidian
    Shard, Spear of Desolation, Avenging Blade, Shield Splitter, Soul Gem, Void Stone,
    Void Shield, Breastplate of Valor, Heartseeker, The Crusher, Spear of the Magus,
    Runeforged Hammer, The Reaper, Hydra''s Lament, Erosion, Doom Orb, Oni Hunter''s
    Garb, Eye of Providence, Draconic Scale, Shield of the Phoenix, The World Stone,
    Sundering Echo, Tekko-Kagi, Midgardian Mail, Helm of Radiance, Magi''s Cloak,
    Helm of Darkness, Mantle Of Discord, Leviathan''s Hide, Pendulum Blade.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.47
      win: 0.65
      pick: 0.0
      fit: 0.7
    Berserker's Shield:
      total: 0.56
      efficiency: 0.63
      win: 0.62
      pick: 0.41
      fit: 0.27
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.65
      pick: 0.42
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.24
      fit: 0.39
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Nimble Ring
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Genji''s Guard, Jotunn''s Revenge, Nimble
    Ring, Gluttonous Grimoire, Breastplate of Valor, Shield Splitter, Tyrfing, Soul
    Gem, Pharaoh''s Curse, Tekko-Kagi, Toxic Blade, Runeforged Hammer, Silverbranch
    Bow, Lernaean Bow, Oni Hunter''s Garb, Erosion, Hydra''s Lament, Eros'' Bow, Riptalon,
    Shield of the Phoenix, Eye of Providence, Stone of Binding, Obsidian Shard, Helm
    of Radiance, Draconic Scale, Screeching Gargoyle, Midgardian Mail, Spear of Desolation,
    Magi''s Cloak, Sundering Echo, The Reaper, Helm of Darkness, Titan''s Bane, Leviathan''s
    Hide, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.49
      win: 0.66
      pick: 0.32
      fit: 0.53
    Berserker's Shield:
      total: 0.61
      efficiency: 0.7
      win: 0.62
      pick: 0.41
      fit: 0.43
    Nimble Ring:
      total: 0.55
      efficiency: 0.61
      win: 0.65
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.53
      win: 0.65
      pick: 0.42
      fit: 0.46
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.24
      fit: 0.34
    Amanita Charm:
      total: 0.56
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
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
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Jotunn''s
    Revenge, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Spear of
    Desolation, Screeching Gargoyle, Hydra''s Lament, Soul Gem, Shield Splitter, Chronos''
    Pendant, Prophetic Cloak, Erosion, Gladiator''s Shield, Arondight, Gluttonous
    Grimoire, Eye of Providence, Helm of Radiance, Helm of Darkness, Oni Hunter''s
    Garb, Draconic Scale, Runeforged Hammer, Obsidian Shard, Stone of Binding, Heartwood
    Charm, Gem of Focus, Chandra''s Grace, Midgardian Mail, Magi''s Cloak, Sundering
    Echo, Glorious Pridwen, Mantle Of Discord, Leviathan''s Hide, Regrowth Striders,
    Eye of Erebus, Ancile, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.61
      win: 0.65
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.65
      pick: 0.42
      fit: 0.55
    Freya's Tears:
      total: 0.6
      efficiency: 0.55
      win: 0.67
      pick: 0.24
      fit: 0.64
    Amanita Charm:
      total: 0.58
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Genji''s Guard, Spear of Desolation, Gluttonous Grimoire, Obsidian Shard,
    Soul Gem, Shield Splitter, Breastplate of Valor, Sundering Echo, Helm of Radiance,
    Helm of Darkness, Spear of the Magus, Titan''s Bane, Runeforged Hammer, Hydra''s
    Lament, Doom Orb, Chronos'' Pendant, Death Metal, The World Stone, Shield of the
    Phoenix, Erosion, Oni Hunter''s Garb, Screeching Gargoyle, Jade Scepter, Eye of
    Providence, Draconic Scale, Stone of Binding, Midgardian Mail, Magi''s Cloak,
    Heartseeker, Ethereal Staff, Dreamer''s Idol, The Crusher, Mantle Of Discord,
    Leviathan''s Hide, Heartwood Charm.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.25
    Berserker's Shield:
      total: 0.56
      efficiency: 0.63
      win: 0.62
      pick: 0.41
      fit: 0.25
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.53
      win: 0.65
      pick: 0.42
      fit: 0.49
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.24
      fit: 0.39
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Genji''s Guard, Gluttonous Grimoire, Shield Splitter, Obsidian
    Shard, Spear of Desolation, Soul Gem, Breastplate of Valor, Sundering Echo, Helm
    of Radiance, Titan''s Bane, Runeforged Hammer, Helm of Darkness, Spear of the
    Magus, Hydra''s Lament, Erosion, Oni Hunter''s Garb, Death Metal, Eye of Providence,
    Doom Orb, Shield of the Phoenix, Draconic Scale, Stone of Binding, The World Stone,
    Heartseeker, Screeching Gargoyle, Midgardian Mail, The Crusher, Chronos'' Pendant,
    Magi''s Cloak, Jade Scepter, Mantle Of Discord, Leviathan''s Hide, Avenging Blade,
    The Reaper, Triton''s Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.56
      efficiency: 0.63
      win: 0.62
      pick: 0.41
      fit: 0.26
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.65
      pick: 0.42
      fit: 0.51
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.24
      fit: 0.38
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield
    Splitter, Genji''s Guard, Breastplate of Valor, Erosion, Runeforged Hammer, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Oni Hunter''s
    Garb, Stone of Binding, Helm of Darkness, Magi''s Cloak, Midgardian Mail, Screeching
    Gargoyle, Gluttonous Grimoire, Mantle Of Discord, Sundering Echo, Helm of Radiance,
    Leviathan''s Hide, Titan''s Bane, Wyrmskin Hide, Spear of Desolation, Avenging
    Blade, Prophetic Cloak, Ancile, Obsidian Shard, Hide of the Nemean Lion, Soul
    Gem, Void Stone, Stampede, Arondight, Void Shield, Xibalban Effigy, Gladiator''s
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.32
    Berserker's Shield:
      total: 0.58
      efficiency: 0.63
      win: 0.62
      pick: 0.41
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.53
      win: 0.65
      pick: 0.42
      fit: 0.67
    Shield Splitter:
      total: 0.57
      efficiency: 0.54
      win: 0.65
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
