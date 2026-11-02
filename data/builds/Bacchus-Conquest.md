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
      win_rate: 0.57
  - name: Kinetic Cuirass
    pick_rate: 0.14
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.56
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.54
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
    win_rate: 0.54
  - name: Bluestone Pendant
    pick_rate: 0.11
    win_rate: 0.41
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-11-02'
  god_win_rate: 0.5609756097560976
  god_matches_won: 621
  god_matches_played: 1107
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
    Breastplate of Valor, Eye of Providence, Draconic Scale, Jotunn''s Revenge, Shield
    of the Phoenix, Shifter''s Shield, Oni Hunter''s Garb, Stone of Binding, Helm
    of Darkness, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Hide of the Nemean
    Lion, Leviathan''s Hide, Screeching Gargoyle, Gluttonous Grimoire, Helm of Radiance,
    Prophetic Cloak, Ancile, Runeforged Hammer, Void Stone, Spear of Desolation, Void
    Shield, Xibalban Effigy, Gladiator''s Shield, Hussar''s Wings, Obsidian Shard,
    Soul Gem, Spectral Armor, Brawler’s Beat Stick, Phoenix Feather, Hydra''s Lament,
    Doublet of Binding, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.08
      fit: 0.37
    Berserker's Shield:
      total: 0.6
      efficiency: 0.63
      win: 0.64
      pick: 0.42
      fit: 0.44
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.53
      win: 0.64
      pick: 0.22
      fit: 0.78
    Shield Splitter:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.59
      pick: 0.25
      fit: 0.62
    Amanita Charm:
      total: 0.58
      efficiency: 0.62
      win: 0.58
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
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Genji''s Guard,
    Phoenix Feather, Soul Gem, Erosion, Jotunn''s Revenge, Yogi''s Necklace, Eye of
    Providence, Draconic Scale, Breastplate of Valor, Chandra''s Grace, Ethereal Staff,
    Shield Splitter, Oni Hunter''s Garb, Shifter''s Shield, Glorious Pridwen, Gluttonous
    Grimoire, Midgardian Mail, Hide of the Nemean Lion, Leviathan''s Hide, Runeforged
    Hammer, Regrowth Striders, Stone of Binding, Rod of Asclepius, Helm of Darkness,
    Ancile, Screeching Gargoyle, Magi''s Cloak, Sphere of Negation, Void Stone, Void
    Shield, Spear of Desolation, Helm of Radiance, Mantle Of Discord, Gladiator''s
    Shield, Blood-Bound Book, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.08
      fit: 0.34
    Berserker's Shield:
      total: 0.6
      efficiency: 0.63
      win: 0.64
      pick: 0.42
      fit: 0.46
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.53
      win: 0.64
      pick: 0.22
      fit: 0.76
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.55
      efficiency: 0.55
      win: 0.59
      pick: 0.25
      fit: 0.54
    Amanita Charm:
      total: 0.62
      efficiency: 0.62
      win: 0.58
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
    Gluttonous Grimoire, Screeching Gargoyle, Genji''s Guard, Obsidian Shard, Spear
    of Desolation, Soul Gem, Void Stone, Void Shield, Breastplate of Valor, Titan''s
    Bane, Shield Splitter, Spear of the Magus, Avenging Blade, Erosion, Eye of Providence,
    Doom Orb, Draconic Scale, Oni Hunter''s Garb, The World Stone, Shield of the Phoenix,
    Heartseeker, The Crusher, Midgardian Mail, Helm of Darkness, Magi''s Cloak, Shifter''s
    Shield, Helm of Radiance, Mantle Of Discord, Runeforged Hammer, The Reaper, Leviathan''s
    Hide, Dreamer''s Idol, Toxic Blade, Ancile, Hydra''s Lament.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.47
      win: 0.58
      pick: 0.0
      fit: 0.74
    Berserker's Shield:
      total: 0.58
      efficiency: 0.63
      win: 0.64
      pick: 0.42
      fit: 0.31
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.53
      win: 0.64
      pick: 0.22
      fit: 0.58
    Freya's Tears:
      total: 0.54
      efficiency: 0.55
      win: 0.59
      pick: 0.25
      fit: 0.43
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.58
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
    this god: Rod of Tahuti, Amanita Charm, Genji''s Guard, Nimble Ring, Jotunn''s
    Revenge, Golden Blade, Gluttonous Grimoire, Shield Splitter, Breastplate of Valor,
    Tyrfing, Soul Gem, Pharaoh''s Curse, Tekko-Kagi, Toxic Blade, Runeforged Hammer,
    Silverbranch Bow, Shogun''s Ofuda, Lernaean Bow, Oni Hunter''s Garb, Erosion,
    Eros'' Bow, Hydra''s Lament, Riptalon, Eye of Providence, Stone of Binding, Draconic
    Scale, Obsidian Shard, Shield of the Phoenix, Helm of Radiance, Midgardian Mail,
    Screeching Gargoyle, Spear of Desolation, Magi''s Cloak, Sundering Echo, The Reaper,
    Helm of Darkness, Titan''s Bane, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.62
      efficiency: 0.7
      win: 0.64
      pick: 0.42
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.64
      pick: 0.22
      fit: 0.47
    Nimble Ring:
      total: 0.52
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.52
      efficiency: 0.55
      win: 0.59
      pick: 0.25
      fit: 0.33
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.58
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
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Jotunn''s
    Revenge, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Spear of
    Desolation, Screeching Gargoyle, Hydra''s Lament, Soul Gem, Shield Splitter, Chronos''
    Pendant, Prophetic Cloak, Erosion, Gladiator''s Shield, Arondight, Gluttonous
    Grimoire, Eye of Providence, Helm of Radiance, Helm of Darkness, Oni Hunter''s
    Garb, Draconic Scale, Runeforged Hammer, Obsidian Shard, Stone of Binding, Heartwood
    Charm, Gem of Focus, Chandra''s Grace, Midgardian Mail, Magi''s Cloak, Sundering
    Echo, Shifter''s Shield, Glorious Pridwen, Mantle Of Discord, Leviathan''s Hide,
    Regrowth Striders, Eye of Erebus, Ancile, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.08
      fit: 0.48
    Berserker's Shield:
      total: 0.57
      efficiency: 0.63
      win: 0.64
      pick: 0.42
      fit: 0.29
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.53
      win: 0.64
      pick: 0.22
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.59
      pick: 0.25
      fit: 0.64
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
    Charm, Shield Splitter, Genji''s Guard, Tekko-Kagi, Titan''s Bane, Golden Blade,
    Runeforged Hammer, Breastplate of Valor, Hydra''s Lament, Gluttonous Grimoire,
    Obsidian Shard, Spear of Desolation, Tyrfing, Sundering Echo, Erosion, Heartseeker,
    Soul Gem, Oni Hunter''s Garb, The Crusher, Eye of Providence, Lernaean Bow, Draconic
    Scale, Toxic Blade, Stone of Binding, Shield of the Phoenix, Silverbranch Bow,
    Avenging Blade, Midgardian Mail, Pharaoh''s Curse, Helm of Radiance, The Reaper,
    Magi''s Cloak, Screeching Gargoyle, Helm of Darkness, Wyrmskin Hide, Mantle Of
    Discord, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.7
      win: 0.64
      pick: 0.42
      fit: 0.36
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.64
      pick: 0.22
      fit: 0.52
    Shield Splitter:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.59
      pick: 0.25
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.58
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
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    Shard, Spear of Desolation, Soul Gem, Sundering Echo, Breastplate of Valor, Helm
    of Radiance, Titan''s Bane, Runeforged Hammer, Helm of Darkness, Spear of the
    Magus, Hydra''s Lament, Erosion, Oni Hunter''s Garb, Death Metal, Eye of Providence,
    Doom Orb, Draconic Scale, Stone of Binding, Shield of the Phoenix, The World Stone,
    Heartseeker, Midgardian Mail, The Crusher, Screeching Gargoyle, Magi''s Cloak,
    Jade Scepter, Chronos'' Pendant, Mantle Of Discord, Leviathan''s Hide, Shifter''s
    Shield, Avenging Blade, The Reaper, Triton''s Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.57
      pick: 0.08
      fit: 0.23
    Berserker's Shield:
      total: 0.57
      efficiency: 0.63
      win: 0.64
      pick: 0.42
      fit: 0.27
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.64
      pick: 0.22
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.59
      pick: 0.25
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
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
    Splitter, Erosion, Breastplate of Valor, Eye of Providence, Draconic Scale, Jotunn''s
    Revenge, Shield of the Phoenix, Shifter''s Shield, Oni Hunter''s Garb, Stone of
    Binding, Helm of Darkness, Magi''s Cloak, Midgardian Mail, Mantle Of Discord,
    Leviathan''s Hide, Screeching Gargoyle, Gluttonous Grimoire, Helm of Radiance,
    Prophetic Cloak, Ancile, Runeforged Hammer, Hide of the Nemean Lion, Void Stone,
    Stampede, Spear of Desolation, Void Shield, Xibalban Effigy, Gladiator''s Shield,
    Hussar''s Wings, Obsidian Shard, Soul Gem, Spectral Armor, Brawler’s Beat Stick,
    Phoenix Feather, Hydra''s Lament, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.08
      fit: 0.37
    Berserker's Shield:
      total: 0.6
      efficiency: 0.63
      win: 0.64
      pick: 0.42
      fit: 0.44
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.53
      win: 0.64
      pick: 0.22
      fit: 0.78
    Shield Splitter:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.59
      pick: 0.25
      fit: 0.62
    Amanita Charm:
      total: 0.58
      efficiency: 0.62
      win: 0.58
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
    Guard, Shield Splitter, Erosion, Breastplate of Valor, Eye of Providence, Draconic
    Scale, Jotunn''s Revenge, Shield of the Phoenix, Shifter''s Shield, Oni Hunter''s
    Garb, Stone of Binding, Helm of Darkness, Magi''s Cloak, Midgardian Mail, Mantle
    Of Discord, Leviathan''s Hide, Screeching Gargoyle, Gluttonous Grimoire, Helm
    of Radiance, Prophetic Cloak, Ancile, Runeforged Hammer, Hide of the Nemean Lion,
    Void Stone, Stampede, Spear of Desolation, Void Shield, Xibalban Effigy, Gladiator''s
    Shield, Hussar''s Wings, Obsidian Shard, Soul Gem, Spectral Armor, Brawler’s Beat
    Stick, Phoenix Feather, Hydra''s Lament, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.08
      fit: 0.37
    Berserker's Shield:
      total: 0.6
      efficiency: 0.63
      win: 0.64
      pick: 0.42
      fit: 0.44
    Devourer's Gauntlet:
      total: 0.41
      efficiency: 0.27
      win: 0.63
      pick: 0.4
      fit: 0.06
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.53
      win: 0.64
      pick: 0.22
      fit: 0.78
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.59
      pick: 0.25
      fit: 0.62
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.81
      win: 0.58
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
    reason: community 63% win over 443 matches (vs 56% on this god), taking the model's
      weakest slot from Shield Splitter
  starter: *id001
---
