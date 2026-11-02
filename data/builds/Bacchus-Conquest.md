---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.59
  aspect_win_rate: 0.59
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.4
    win_rate: 0.63
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.51
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.47
  - name: Berserker's Shield
    pick_rate: 0.31
    win_rate: 0.64
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.47
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.56
  - name: Kinetic Cuirass
    pick_rate: 0.14
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.56
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.55
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.61
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.55
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.68
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.65
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.61
    alternates:
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.54
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.55
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.29
    win_rate: 0.65
  - name: Leather Cowl
    pick_rate: 0.18
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.11
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-11-02'
  god_win_rate: 0.5610412926391383
  god_matches_won: 625
  god_matches_played: 1114
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Shield Splitter, Erosion,
    Breastplate of Valor, Eye of Providence, Jotunn''s Revenge, Draconic Scale, Shield
    of the Phoenix, Shifter''s Shield, Helm of Darkness, Stone of Binding, Oni Hunter''s
    Garb, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Hide of the Nemean Lion,
    Helm of Radiance, Leviathan''s Hide, Screeching Gargoyle, Runeforged Hammer, Gluttonous
    Grimoire, Prophetic Cloak, Ancile, Spear of Desolation, Void Stone, Brawler’s
    Beat Stick, Void Shield, Xibalban Effigy, Hydra''s Lament, Soul Gem, Obsidian
    Shard, Gladiator''s Shield, Hussar''s Wings, Spectral Armor, Phoenix Feather,
    Doublet of Binding, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.08
      fit: 0.37
    Berserker's Shield:
      total: 0.61
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.44
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.78
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
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
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Genji''s Guard,
    Soul Gem, Phoenix Feather, Jotunn''s Revenge, Shield Splitter, Erosion, Eye of
    Providence, Breastplate of Valor, Draconic Scale, Yogi''s Necklace, Ethereal Staff,
    Chandra''s Grace, Oni Hunter''s Garb, Shifter''s Shield, Midgardian Mail, Runeforged
    Hammer, Gluttonous Grimoire, Glorious Pridwen, Hide of the Nemean Lion, Leviathan''s
    Hide, Helm of Darkness, Stone of Binding, Regrowth Striders, Rod of Asclepius,
    Helm of Radiance, Magi''s Cloak, Sphere of Negation, Ancile, Screeching Gargoyle,
    Spear of Desolation, Void Stone, Mantle Of Discord, Blood-Bound Book, Void Shield,
    The Reaper, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.08
      fit: 0.34
    Berserker's Shield:
      total: 0.61
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.46
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.76
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.56
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.54
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Genji's Guard
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
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Screeching Gargoyle, Spear of Desolation, Genji''s Guard,
    Obsidian Shard, Soul Gem, Void Stone, Void Shield, Shield Splitter, Breastplate
    of Valor, Titan''s Bane, Avenging Blade, Spear of the Magus, Erosion, Eye of Providence,
    Doom Orb, The Crusher, Draconic Scale, Heartseeker, The World Stone, Oni Hunter''s
    Garb, Helm of Radiance, Shield of the Phoenix, Helm of Darkness, Runeforged Hammer,
    Magi''s Cloak, Midgardian Mail, Shifter''s Shield, The Reaper, Mantle Of Discord,
    Dreamer''s Idol, Leviathan''s Hide, Hydra''s Lament, Toxic Blade, Ancile.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.74
    Berserker's Shield:
      total: 0.59
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.31
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.57
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.58
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.43
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.48
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
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Genji''s Guard, Nimble
    Ring, Golden Blade, Shield Splitter, Gluttonous Grimoire, Tyrfing, Breastplate
    of Valor, Soul Gem, Runeforged Hammer, Tekko-Kagi, Pharaoh''s Curse, Lernaean
    Bow, Toxic Blade, Hydra''s Lament, Shogun''s Ofuda, Silverbranch Bow, Helm of
    Radiance, Erosion, Eros'' Bow, Oni Hunter''s Garb, Eye of Providence, Stone of
    Binding, Draconic Scale, Obsidian Shard, Midgardian Mail, Shield of the Phoenix,
    Helm of Darkness, Spear of Desolation, Magi''s Cloak, Screeching Gargoyle, The
    Reaper, Riptalon, Titan''s Bane, Mantle Of Discord, Leviathan''s Hide, Blood-Bound
    Book.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.63
      efficiency: 0.75
      win: 0.64
      pick: 0.42
      fit: 0.43
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.47
    Nimble Ring:
      total: 0.53
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.33
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Jotunn''s
    Revenge, Amanita Charm, Breastplate of Valor, Spear of Desolation, Shield of the
    Phoenix, Hydra''s Lament, Shield Splitter, Screeching Gargoyle, Soul Gem, Chronos''
    Pendant, Arondight, Prophetic Cloak, Helm of Radiance, Runeforged Hammer, Helm
    of Darkness, Erosion, Eye of Providence, Gluttonous Grimoire, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Oni Hunter''s Garb, Gem of Focus, Obsidian Shard,
    Heartwood Charm, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Shifter''s
    Shield, Chandra''s Grace, Leviathan''s Hide, Eye of Erebus, Glorious Pridwen,
    Regrowth Striders, Titan''s Bane, Jade Scepter, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.56
      pick: 0.08
      fit: 0.48
    Berserker's Shield:
      total: 0.59
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.29
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.57
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.55
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Shield Splitter, Genji''s Guard, Runeforged Hammer, Tekko-Kagi, Golden
    Blade, Titan''s Bane, Breastplate of Valor, Hydra''s Lament, Gluttonous Grimoire,
    Tyrfing, Spear of Desolation, Obsidian Shard, The Crusher, Heartseeker, Lernaean
    Bow, Erosion, Avenging Blade, Soul Gem, Eye of Providence, Helm of Radiance, Oni
    Hunter''s Garb, Stone of Binding, Draconic Scale, Arondight, The Reaper, Shield
    of the Phoenix, Helm of Darkness, Toxic Blade, Midgardian Mail, Magi''s Cloak,
    Screeching Gargoyle, Pharaoh''s Curse, Death Metal, Silverbranch Bow, Spear of
    the Magus, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.62
      efficiency: 0.75
      win: 0.64
      pick: 0.42
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Desolation, Obsidian Shard, Soul Gem, Helm of Radiance, Breastplate of Valor,
    Runeforged Hammer, Helm of Darkness, Titan''s Bane, Spear of the Magus, Hydra''s
    Lament, Death Metal, Erosion, Eye of Providence, Doom Orb, The Crusher, Oni Hunter''s
    Garb, Stone of Binding, Draconic Scale, Jade Scepter, Heartseeker, Shield of the
    Phoenix, The World Stone, Midgardian Mail, Avenging Blade, Magi''s Cloak, Chronos''
    Pendant, Screeching Gargoyle, Mantle Of Discord, Arondight, The Reaper, Leviathan''s
    Hide, Shifter''s Shield, Dreamer''s Idol.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.27
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
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
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Shield
    Splitter, Erosion, Breastplate of Valor, Eye of Providence, Jotunn''s Revenge,
    Draconic Scale, Shield of the Phoenix, Shifter''s Shield, Helm of Darkness, Stone
    of Binding, Oni Hunter''s Garb, Magi''s Cloak, Midgardian Mail, Mantle Of Discord,
    Helm of Radiance, Leviathan''s Hide, Screeching Gargoyle, Runeforged Hammer, Gluttonous
    Grimoire, Prophetic Cloak, Ancile, Spear of Desolation, Hide of the Nemean Lion,
    Stampede, Void Stone, Brawler’s Beat Stick, Void Shield, Xibalban Effigy, Hydra''s
    Lament, Soul Gem, Obsidian Shard, Gladiator''s Shield, Hussar''s Wings, Spectral
    Armor, Phoenix Feather, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.08
      fit: 0.37
    Berserker's Shield:
      total: 0.61
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.44
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.78
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Devourer's Gauntlet
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Devourer's Gauntlet
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Genji''s
    Guard, Shield Splitter, Erosion, Breastplate of Valor, Eye of Providence, Jotunn''s
    Revenge, Draconic Scale, Shield of the Phoenix, Shifter''s Shield, Helm of Darkness,
    Stone of Binding, Oni Hunter''s Garb, Magi''s Cloak, Midgardian Mail, Mantle Of
    Discord, Helm of Radiance, Leviathan''s Hide, Screeching Gargoyle, Runeforged
    Hammer, Gluttonous Grimoire, Prophetic Cloak, Ancile, Spear of Desolation, Hide
    of the Nemean Lion, Stampede, Void Stone, Brawler’s Beat Stick, Void Shield, Xibalban
    Effigy, Hydra''s Lament, Soul Gem, Obsidian Shard, Gladiator''s Shield, Hussar''s
    Wings, Spectral Armor, Phoenix Feather, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.08
      fit: 0.37
    Berserker's Shield:
      total: 0.61
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.44
    Devourer's Gauntlet:
      total: 0.42
      efficiency: 0.29
      win: 0.63
      pick: 0.4
      fit: 0.06
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.78
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.62
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.87
      win: 0.57
      pick: 0.0
      fit: 0.13
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Devourer's Gauntlet
  - Kinetic Cuirass
  - Freya's Tears
  swaps:
  - added: Devourer's Gauntlet
    removed: Shield Splitter
    reason: community 63% win over 446 matches (vs 56% on this god), taking the model's
      weakest slot from Shield Splitter
  starter: *id001
---
