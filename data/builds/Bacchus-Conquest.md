---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.8
  aspect_win_rate: 0.61
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.64
    win_rate: 0.64
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 0.48
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.53
  - name: Berserker's Shield
    pick_rate: 0.46
    win_rate: 0.61
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.15
      win_rate: 0.62
    - name: Stampede
      pick_rate: 0.05
      win_rate: 0.42
  - name: Kinetic Cuirass
    pick_rate: 0.24
    win_rate: 0.65
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.16
      win_rate: 0.67
    - name: Shogun's Ofuda
      pick_rate: 0.13
      win_rate: 0.66
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.6
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.19
      win_rate: 0.64
    - name: Shogun's Ofuda
      pick_rate: 0.09
      win_rate: 0.64
  - name: Hussar's Wings
    pick_rate: 0.09
    win_rate: 0.7
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.68
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.56
  - name: Medal of Defense
    pick_rate: 0.12
    win_rate: 0.65
    alternates:
    - name: Hussar's Wings
      pick_rate: 0.06
      win_rate: 0.68
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.41
    win_rate: 0.63
  - name: Leather Cowl
    pick_rate: 0.26
    win_rate: 0.62
  - name: Bumba's Cudgel
    pick_rate: 0.09
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-11-08'
  god_win_rate: 0.5935727788279773
  god_matches_won: 314
  god_matches_played: 529
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
  - Genji's Guard
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Draconic Scale, Shield
    Splitter, Shield of the Phoenix, Gluttonous Grimoire, Breastplate of Valor, Erosion,
    Eye of Providence, Soul Gem, Shifter''s Shield, Oni Hunter''s Garb, Jotunn''s
    Revenge, Stone of Binding, Midgardian Mail, Helm of Darkness, Screeching Gargoyle,
    Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Hide of the Nemean Lion,
    Spear of Desolation, Helm of Radiance, Gladiator''s Shield, Runeforged Hammer,
    Ancile, Prophetic Cloak, Blood-Bound Book, Void Stone, Phoenix Feather, Void Shield,
    Spectral Armor, Hydra''s Lament, The Reaper, Doublet of Binding, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.6
      efficiency: 0.66
      win: 0.61
      pick: 0.63
      fit: 0.39
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.61
      win: 0.65
      pick: 0.37
      fit: 0.71
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.55
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.61
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
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Rod of Tahuti, Genji''s
    Guard, Phoenix Feather, Gluttonous Grimoire, Blood-Bound Book, The Reaper, Draconic
    Scale, Yogi''s Necklace, Ethereal Staff, Oni Hunter''s Garb, Erosion, Chandra''s
    Grace, Breastplate of Valor, Eye of Providence, Shield Splitter, Jotunn''s Revenge,
    Shifter''s Shield, Midgardian Mail, Bancroft''s Talon, Regrowth Striders, Glorious
    Pridwen, Leviathan''s Hide, Runeforged Hammer, Hide of the Nemean Lion, Spear
    of Desolation, Screeching Gargoyle, Gladiator''s Shield, Ancile, Stone of Binding,
    Helm of Darkness, Void Stone, Helm of Radiance, Sphere of Negation, Magi''s Cloak,
    Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.3
    Berserker's Shield:
      total: 0.6
      efficiency: 0.66
      win: 0.61
      pick: 0.63
      fit: 0.41
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.61
      win: 0.65
      pick: 0.37
      fit: 0.69
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.83
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.49
    Amanita Charm:
      total: 0.65
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.89
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Jotunn''s
    Revenge, Genji''s Guard, Screeching Gargoyle, Stone of Binding, Spear of Desolation,
    Void Stone, Void Shield, The Reaper, Breastplate of Valor, Shield Splitter, Obsidian
    Shard, Shield of the Phoenix, Draconic Scale, Avenging Blade, Oni Hunter''s Garb,
    Spear of the Magus, The Crusher, Erosion, Eye of Providence, Dreamer''s Idol,
    Heartseeker, Shifter''s Shield, Midgardian Mail, Titan''s Bane, Helm of Radiance,
    Leviathan''s Hide, Doom Orb, Runeforged Hammer, Magi''s Cloak, Blood-Bound Book,
    Mantle Of Discord, Helm of Darkness, Hide of the Nemean Lion, The World Stone.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.64
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.61
      pick: 0.63
      fit: 0.28
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.61
      win: 0.65
      pick: 0.37
      fit: 0.54
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Berserker's Shield
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
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Genji''s Guard, Tyrfing, Jotunn''s Revenge,
    Golden Blade, Shield Splitter, Gluttonous Grimoire, Breastplate of Valor, Soul
    Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s Garb, Draconic Scale, Runeforged
    Hammer, Pharaoh''s Curse, Erosion, Hydra''s Lament, Eye of Providence, Spear of
    Desolation, Toxic Blade, Bragi''s Harp, Screeching Gargoyle, Shifter''s Shield,
    Midgardian Mail, The Reaper, Blood-Bound Book, Helm of Radiance, Stone of Binding,
    Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch Bow, Magi''s Cloak, Mantle
    Of Discord, Hide of the Nemean Lion, Helm of Darkness.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.62
      efficiency: 0.72
      win: 0.61
      pick: 0.63
      fit: 0.43
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.65
      pick: 0.37
      fit: 0.47
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Amanita
    Charm, Soul Gem, Jotunn''s Revenge, Breastplate of Valor, Shield of the Phoenix,
    Spear of Desolation, Screeching Gargoyle, Hydra''s Lament, Gluttonous Grimoire,
    Shield Splitter, Chronos'' Pendant, Gladiator''s Shield, Draconic Scale, Oni Hunter''s
    Garb, Prophetic Cloak, Arondight, Erosion, Eye of Providence, Helm of Radiance,
    Runeforged Hammer, Blood-Bound Book, Shifter''s Shield, Gem of Focus, Heartwood
    Charm, Helm of Darkness, Midgardian Mail, Chandra''s Grace, Stone of Binding,
    Leviathan''s Hide, Regrowth Striders, Ancient Signet, Magi''s Cloak, Mantle Of
    Discord, The Reaper, Hide of the Nemean Lion, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.61
      pick: 0.63
      fit: 0.27
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.65
      pick: 0.37
      fit: 0.52
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.6
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Berserker's Shield
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
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Genji''s Guard, Shield Splitter, Gluttonous Grimoire, Soul Gem, The Reaper, Tyrfing,
    Runeforged Hammer, Breastplate of Valor, Hydra''s Lament, Golden Blade, Spear
    of Desolation, Shield of the Phoenix, The Crusher, Oni Hunter''s Garb, Draconic
    Scale, Heartseeker, Erosion, Eye of Providence, Tekko-Kagi, Titan''s Bane, Death
    Metal, Shifter''s Shield, Midgardian Mail, Screeching Gargoyle, Bragi''s Harp,
    Stone of Binding, Helm of Radiance, Blood-Bound Book, Obsidian Shard, Avenging
    Blade, Leviathan''s Hide, Arondight, Magi''s Cloak, Mantle Of Discord, Nimble
    Ring.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.21
    Berserker's Shield:
      total: 0.61
      efficiency: 0.72
      win: 0.61
      pick: 0.63
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.65
      pick: 0.37
      fit: 0.49
    Shield Splitter:
      total: 0.55
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
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
  - Genji's Guard
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Soul Gem, Jotunn''s Revenge, Genji''s Guard, Shield Splitter, Spear
    of Desolation, The Reaper, Breastplate of Valor, Helm of Radiance, Blood-Bound
    Book, Runeforged Hammer, Shield of the Phoenix, Obsidian Shard, Death Metal, Oni
    Hunter''s Garb, Draconic Scale, Helm of Darkness, Hydra''s Lament, Spear of the
    Magus, Ancient Signet, The Crusher, Erosion, Eye of Providence, Polynomicon, Heartseeker,
    Dreamer''s Idol, Chronos'' Pendant, Shifter''s Shield, Midgardian Mail, Screeching
    Gargoyle, Stone of Binding, Jade Scepter, Tyrfing, Titan''s Bane, Leviathan''s
    Hide, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.21
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.63
      fit: 0.25
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.65
      pick: 0.37
      fit: 0.49
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.35
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.39
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Draconic
    Scale, Shield Splitter, Shield of the Phoenix, Gluttonous Grimoire, Breastplate
    of Valor, Erosion, Eye of Providence, Soul Gem, Shifter''s Shield, Oni Hunter''s
    Garb, Jotunn''s Revenge, Stone of Binding, Midgardian Mail, Helm of Darkness,
    Screeching Gargoyle, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Hide
    of the Nemean Lion, Spear of Desolation, Helm of Radiance, Gladiator''s Shield,
    Runeforged Hammer, Ancile, Prophetic Cloak, Blood-Bound Book, Void Stone, Phoenix
    Feather, Stampede, Void Shield, Spectral Armor, Hydra''s Lament, The Reaper, Doublet
    of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.6
      efficiency: 0.66
      win: 0.61
      pick: 0.63
      fit: 0.39
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.61
      win: 0.65
      pick: 0.37
      fit: 0.71
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.55
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
