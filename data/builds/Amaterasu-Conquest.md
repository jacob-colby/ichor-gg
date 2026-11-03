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
      win_rate: 0.63
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
    win_rate: 0.57
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
  last_verified: '2026-11-03'
  god_win_rate: 0.631079478054567
  god_matches_won: 532
  god_matches_played: 843
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
  - Jotunn's Revenge
  - Berserker's Shield
  - Shield Splitter
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
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
    this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Jotunn''s Revenge, Genji''s
    Guard, Breastplate of Valor, Runeforged Hammer, Erosion, Eye of Providence, Hydra''s
    Lament, Draconic Scale, Oni Hunter''s Garb, Shield of the Phoenix, Helm of Darkness,
    Stone of Binding, Magi''s Cloak, Helm of Radiance, Midgardian Mail, Mantle Of
    Discord, Screeching Gargoyle, Avenging Blade, Gluttonous Grimoire, Leviathan''s
    Hide, Titan''s Bane, Wyrmskin Hide, Spear of Desolation, Arondight, Obsidian Shard,
    Ancile, Prophetic Cloak, Soul Gem, Hide of the Nemean Lion, Stampede, Void Stone,
    Void Shield, Death Metal, Brawler’s Beat Stick, The Crusher.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.38
    Berserker's Shield:
      total: 0.59
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.36
    Shield Splitter:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.61
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.67
    Freya's Tears:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.53
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
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
  - Jotunn's Revenge
  - Freya's Tears
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Jotunn''s Revenge,
    Shield Splitter, Genji''s Guard, Soul Gem, Runeforged Hammer, Phoenix Feather,
    Yogi''s Necklace, Breastplate of Valor, The Reaper, Ethereal Staff, Hydra''s Lament,
    Erosion, Eye of Providence, Chandra''s Grace, Oni Hunter''s Garb, Draconic Scale,
    Avenging Blade, Gluttonous Grimoire, Midgardian Mail, Regrowth Striders, Glorious
    Pridwen, Rod of Asclepius, Wyrmskin Hide, Leviathan''s Hide, Titan''s Bane, Blood-Bound
    Book, Helm of Radiance, Spear of Desolation, Helm of Darkness, Stone of Binding,
    Sphere of Negation, Arondight, Screeching Gargoyle, Magi''s Cloak, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.39
    Berserker's Shield:
      total: 0.59
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.38
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.52
      win: 0.65
      pick: 0.0
      fit: 0.81
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.65
    Freya's Tears:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.46
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Genji''s Guard, Screeching Gargoyle, Shield Splitter, Avenging Blade, Gluttonous
    Grimoire, Titan''s Bane, Spear of Desolation, Obsidian Shard, Soul Gem, Void Stone,
    Void Shield, Breastplate of Valor, The Crusher, Runeforged Hammer, Spear of the
    Magus, Heartseeker, The Reaper, Hydra''s Lament, Oni Hunter''s Garb, Erosion,
    Eye of Providence, Doom Orb, Helm of Radiance, Draconic Scale, Shield of the Phoenix,
    Tekko-Kagi, The World Stone, Midgardian Mail, Helm of Darkness, Magi''s Cloak,
    Mantle Of Discord, Leviathan''s Hide, Dreamer''s Idol, Pendulum Blade.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.5
      win: 0.65
      pick: 0.0
      fit: 0.7
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.27
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Genji''s Guard, Jotunn''s Revenge, Nimble
    Ring, Shield Splitter, Gluttonous Grimoire, Tyrfing, Breastplate of Valor, Soul
    Gem, Runeforged Hammer, Tekko-Kagi, Pharaoh''s Curse, Lernaean Bow, Toxic Blade,
    Hydra''s Lament, Oni Hunter''s Garb, Eros'' Bow, Silverbranch Bow, Helm of Radiance,
    Erosion, Eye of Providence, Stone of Binding, Spear of Desolation, Shield of the
    Phoenix, Obsidian Shard, Draconic Scale, Midgardian Mail, Helm of Darkness, Screeching
    Gargoyle, The Reaper, Magi''s Cloak, Titan''s Bane, Riptalon, Leviathan''s Hide,
    Mantle Of Discord, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.52
      win: 0.66
      pick: 0.32
      fit: 0.53
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
      win: 0.62
      pick: 0.41
      fit: 0.43
    Nimble Ring:
      total: 0.56
      efficiency: 0.63
      win: 0.65
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.46
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.34
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
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
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Jotunn''s
    Revenge, Amanita Charm, Breastplate of Valor, Spear of Desolation, Shield of the
    Phoenix, Hydra''s Lament, Shield Splitter, Screeching Gargoyle, Soul Gem, Lotus
    Sickle, Chronos'' Pendant, Arondight, Prophetic Cloak, Helm of Radiance, Runeforged
    Hammer, Erosion, Helm of Darkness, Oni Hunter''s Garb, Eye of Providence, Gluttonous
    Grimoire, Gladiator''s Shield, Draconic Scale, Obsidian Shard, Stone of Binding,
    Gem of Focus, Midgardian Mail, Heartwood Charm, Magi''s Cloak, Mantle Of Discord,
    Leviathan''s Hide, Regrowth Striders, Chandra''s Grace, Eye of Erebus, Glorious
    Pridwen, Ancient Signet, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.63
      win: 0.65
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.55
    Freya's Tears:
      total: 0.61
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.64
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Genji''s Guard, Spear of Desolation, Gluttonous Grimoire, Obsidian Shard,
    Shield Splitter, Soul Gem, Helm of Radiance, Breastplate of Valor, Helm of Darkness,
    Spear of the Magus, Runeforged Hammer, Hydra''s Lament, Lotus Sickle, Titan''s
    Bane, Death Metal, Ancient Signet, Chronos'' Pendant, Doom Orb, Oni Hunter''s
    Garb, Jade Scepter, Erosion, Shield of the Phoenix, The World Stone, Eye of Providence,
    Screeching Gargoyle, Stone of Binding, Draconic Scale, Midgardian Mail, The Crusher,
    Dreamer''s Idol, Magi''s Cloak, Ethereal Staff, Arondight, Avenging Blade, Leviathan''s
    Hide, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.25
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.25
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.49
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Shield Splitter, Genji''s Guard, Gluttonous Grimoire, Spear of
    Desolation, Obsidian Shard, Soul Gem, Helm of Radiance, Runeforged Hammer, Breastplate
    of Valor, Helm of Darkness, Titan''s Bane, Spear of the Magus, Hydra''s Lament,
    Death Metal, Oni Hunter''s Garb, Erosion, Lotus Sickle, Eye of Providence, Ancient
    Signet, The Crusher, Draconic Scale, Shield of the Phoenix, Doom Orb, Jade Scepter,
    Stone of Binding, Midgardian Mail, The World Stone, Avenging Blade, Chronos''
    Pendant, Magi''s Cloak, Screeching Gargoyle, Heartseeker, Mantle Of Discord, Arondight,
    Leviathan''s Hide, The Reaper.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.41
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.26
    Shield Splitter:
      total: 0.57
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.51
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.38
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Jotunn''s
    Revenge, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Erosion, Eye
    of Providence, Hydra''s Lament, Draconic Scale, Oni Hunter''s Garb, Shield of
    the Phoenix, Helm of Darkness, Stone of Binding, Magi''s Cloak, Helm of Radiance,
    Midgardian Mail, Mantle Of Discord, Screeching Gargoyle, Avenging Blade, Gluttonous
    Grimoire, Leviathan''s Hide, Titan''s Bane, Wyrmskin Hide, Spear of Desolation,
    Arondight, Obsidian Shard, Ancile, Prophetic Cloak, Soul Gem, Hide of the Nemean
    Lion, Stampede, Void Stone, Void Shield, Death Metal, Brawler’s Beat Stick, The
    Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.32
    Berserker's Shield:
      total: 0.59
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.67
    Shield Splitter:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
