---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Helm of Radiance
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.22
      win_rate: 0.5
    - name: Eye of Erebus
      pick_rate: 0.22
      win_rate: 1.0
  - name: Breastplate of Valor
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.22
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.22
      win_rate: 1.0
  - name: Ethereal Staff
    pick_rate: 0.22
    win_rate: 1.0
    alternates:
    - name: Leviathan's Hide
      pick_rate: 0.22
      win_rate: 0.5
    - name: Brawler’s Beat Stick
      pick_rate: 0.22
      win_rate: 0.5
  - name: Gladiator's Shield
    pick_rate: 0.44
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.0
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 1.0
  - name: Medallion
    pick_rate: 0.11
    win_rate: 0.0
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 1.0
    - name: Soul Reaver
      pick_rate: 0.11
      win_rate: 1.0
  - name: Contagion
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: The Reaper
      pick_rate: 0.13
      win_rate: 1.0
    - name: Olmec Blue
      pick_rate: 0.13
      win_rate: 1.0
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.33
    win_rate: 0.33
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.5
  - name: Death's Embrace
    pick_rate: 0.22
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-10-21'
  god_win_rate: 0.5555555555555556
  god_matches_won: 5
  god_matches_played: 9
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Freya''s Tears, Shield Splitter, Golden Blade, Runeforged Hammer, Eye of the Storm,
    Erosion, Pharaoh''s Curse, Eye of Providence, Lernaean Bow, Draconic Scale, Shogun''s
    Ofuda, Hydra''s Lament, Shield of the Phoenix, Stone of Binding, Tyrfing, Nimble
    Ring, Gluttonous Grimoire, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Screeching
    Gargoyle, Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of
    Desolation, Hide of the Nemean Lion, Heartseeker, Rod of Asclepius, Void Shield,
    Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.7
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.88
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.18
      fit: 0.58
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.88
      pick: 0.0
      fit: 0.43
    Shifter's Shield:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.3
      fit: 0.48
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Shield of the Phoenix, Rod of Asclepius, Freya''s Tears, Golden Blade, Soul Gem,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Pharaoh''s Curse, Yogi''s
    Necklace, Lernaean Bow, Erosion, Shogun''s Ofuda, Hydra''s Lament, Gluttonous
    Grimoire, Eye of Providence, Phoenix Feather, Tyrfing, Chandra''s Grace, Riptalon,
    Draconic Scale, Nimble Ring, Avenging Blade, Lifebinder, Stone of Binding, Glorious
    Pridwen, Daybreak Gavel, Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Sphere of
    Negation.'
  slot_scores:
    Berserker's Shield:
      total: 0.71
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.88
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.18
      fit: 0.56
    Shifter's Shield:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.3
      fit: 0.46
    The Reaper:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.53
    Amanita Charm:
      total: 0.74
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - The Reaper
  flex_slots:
  - Berserker's Shield
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Stone of Binding, Avenging Blade, Screeching Gargoyle, Gluttonous Grimoire, Freya''s
    Tears, Void Shield, Spear of Desolation, Spear of the Magus, Void Stone, Heartseeker,
    Shield Splitter, Soul Gem, Tekko-Kagi, Obsidian Shard, Runeforged Hammer, Silverbranch
    Bow, Golden Blade, Toxic Blade, Titan''s Bane, The Crusher, Eye of the Storm,
    Hydra''s Lament, Lernaean Bow, Erosion, Nimble Ring, Pharaoh''s Curse, Eye of
    Providence, Shield of the Phoenix, Draconic Scale, Doom Orb, Shogun''s Ofuda,
    Tyrfing.'
  slot_scores:
    Stone of Binding:
      total: 0.67
      efficiency: 0.51
      win: 0.88
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.69
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.72
      win: 0.88
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.18
      fit: 0.47
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.3
      fit: 0.37
    The Reaper:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.4
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - The Reaper
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Shifter's Shield
  - The Reaper
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Freya''s Tears, Golden Blade, Gluttonous Grimoire, Tyrfing, Shield
    Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Shogun''s Ofuda, Silverbranch Bow, Erosion, Eye of Providence, Stone of Binding,
    Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic Blade, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of Desolation,
    Spear of the Magus, Bragi''s Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi,
    Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.66
      efficiency: 0.52
      win: 0.88
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.7
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.18
      fit: 0.47
    Nimble Ring:
      total: 0.67
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.3
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.3
      fit: 0.37
    The Reaper:
      total: 0.69
      efficiency: 0.55
      win: 1.0
      pick: 0.4
      fit: 0.2
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - The Reaper
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Eye of Erebus
  - Shifter's Shield
  - Freya's Tears
  flex_slots:
  - Berserker's Shield
  - Eye of Erebus
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Freya''s Tears, Berserker''s Shield, Amanita Charm, Shield of the Phoenix, Spear
    of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant,
    Shield Splitter, Nimble Ring, Runeforged Hammer, Gluttonous Grimoire, Erosion,
    Pharaoh''s Curse, Golden Blade, Eye of Providence, Stone of Binding, Draconic
    Scale, Shogun''s Ofuda, Eye of the Storm, Arondight, Gem of Focus, Lernaean Bow,
    Spear of the Magus, Magi''s Cloak, Rod of Asclepius, Daybreak Gavel, Mantle Of
    Discord, Obsidian Shard, Midgardian Mail, Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.69
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.72
      win: 0.88
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.18
      fit: 0.49
    Eye of Erebus:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.22
      fit: 0.24
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.3
      fit: 0.39
    Freya's Tears:
      total: 0.69
      efficiency: 0.61
      win: 0.88
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Kinetic Cuirass
  - Eye of Erebus
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - The Reaper
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Freya''s Tears, Shield Splitter, Runeforged Hammer, Eye
    of the Storm, Gluttonous Grimoire, Golden Blade, Hydra''s Lament, Heartseeker,
    Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence, Spear
    of the Magus, Avenging Blade, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Tyrfing, Titan''s Bane, Soul Gem, The Crusher, Obsidian Shard, Pharaoh''s
    Curse, Magi''s Cloak, Nimble Ring, Shogun''s Ofuda, Screeching Gargoyle, Mantle
    Of Discord, Midgardian Mail, Daybreak Gavel, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.69
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.72
      win: 0.88
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.18
      fit: 0.52
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.88
      pick: 0.0
      fit: 0.38
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.3
      fit: 0.42
    The Reaper:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.37
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - The Reaper
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - The Reaper
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Shield
    Splitter, Spear of the Magus, Spear of Desolation, Nimble Ring, Runeforged Hammer,
    Soul Gem, Obsidian Shard, Golden Blade, Eye of the Storm, Hydra''s Lament, Lernaean
    Bow, Rod of Asclepius, Bragi''s Harp, Heartseeker, Erosion, Pharaoh''s Curse,
    Tekko-Kagi, Stone of Binding, Eye of Providence, Tyrfing, Shield of the Phoenix,
    Draconic Scale, Shogun''s Ofuda, Jade Scepter, Doom Orb, Silverbranch Bow, Wish-Granting
    Pearl, Avenging Blade, Death Metal, Chronos'' Pendant, Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.69
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.72
      win: 0.88
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.18
      fit: 0.46
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.88
      pick: 0.0
      fit: 0.33
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.3
      fit: 0.36
    The Reaper:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.28
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - The Reaper
  starter: *id001
- source: suggested
  archetype: model
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Freya''s Tears, Shield Splitter, Golden Blade, Runeforged Hammer, Eye
    of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence, Lernaean Bow, Draconic
    Scale, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Stone of Binding,
    Tyrfing, Nimble Ring, Gluttonous Grimoire, Magi''s Cloak, Avenging Blade, Mantle
    Of Discord, Screeching Gargoyle, Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Daybreak
    Gavel, Spear of Desolation, Hide of the Nemean Lion, Heartseeker, Rod of Asclepius,
    Void Shield, Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.7
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.88
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.18
      fit: 0.58
    Shield Splitter:
      total: 0.66
      efficiency: 0.55
      win: 0.88
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.88
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
