---
type: smite-build
god: Ganesha
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Triumphant
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.5
  slot_order:
  - name: Amanita Charm
    pick_rate: 0.21
    win_rate: 0.5
    alternates:
    - name: Stampede
      pick_rate: 0.21
      win_rate: 0.0
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.33
  - name: Genji's Guard
    pick_rate: 0.26
    win_rate: 0.4
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.0
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.5
  - name: Stampede
    pick_rate: 0.16
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.25
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.33
  - name: Shell of Rebuke
    pick_rate: 0.17
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.5
  - name: Medal of Defense
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.14
      win_rate: 0.5
    - name: Circe's Hexstone
      pick_rate: 0.07
      win_rate: 1.0
  - name: Olmec Blue
    pick_rate: 0.33
    win_rate: 0.67
    alternates:
    - name: Medal of Disruption
      pick_rate: 0.11
      win_rate: 0.0
    - name: Mote of Chaos
      pick_rate: 0.11
      win_rate: 0.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.47
    win_rate: 0.44
  - name: Bluestone Pendant
    pick_rate: 0.11
    win_rate: 0.0
  - name: War Banner
    pick_rate: 0.11
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/ganesha/
  last_verified: '2026-09-09'
  god_win_rate: 0.3684210526315789
  god_matches_won: 7
  god_matches_played: 19
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shifter's Shield
  - Spear of Desolation
  - Amanita Charm
  - Circe's Hexstone
  flex_slots:
  - Spear of Desolation
  - Shifter's Shield
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
    this god: Rod of Tahuti, Kinetic Cuirass, Breastplate of Valor, Erosion, Eye of
    Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Screeching Gargoyle,
    Midgardian Mail, Prophetic Cloak, Hide of the Nemean Lion, Leviathan''s Hide,
    Helm of Darkness, Void Shield, Ancile, Oni Hunter''s Garb, Gladiator''s Shield,
    Xibalban Effigy.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.36
      pick: 0.0
      fit: 0.8
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.4
      pick: 0.35
      fit: 0.4
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.33
      pick: 0.25
      fit: 0.7
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.5
      pick: 0.15
      fit: 0.3
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.21
      fit: 0.7
    Circe's Hexstone:
      total: 0.59
      efficiency: 0.23
      win: 1.0
      pick: 0.15
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Spear of Desolation
  - Amanita Charm
  - Circe's Hexstone
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Spear of Desolation
  - Amanita Charm
  - Circe's Hexstone
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass, Rod of Asclepius,
    Soul Gem, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Ethereal
    Staff, Gluttonous Grimoire, Phoenix Feather, Chandra''s Grace, Yogi''s Necklace,
    Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding, Helm of Radiance,
    Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s Cloak, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.36
      pick: 0.0
      fit: 0.78
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.4
      pick: 0.35
      fit: 0.37
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.53
      win: 0.36
      pick: 0.0
      fit: 0.93
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.5
      pick: 0.15
      fit: 0.32
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.5
      pick: 0.21
      fit: 0.98
    Circe's Hexstone:
      total: 0.6
      efficiency: 0.23
      win: 1.0
      pick: 0.15
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Amanita Charm
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Spear of Desolation
  - Circe's Hexstone
  - Amanita Charm
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass,
    Screeching Gargoyle, Soul Gem, Spear of the Magus, Void Shield, Breastplate of
    Valor, Obsidian Shard, Void Stone, Erosion, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Doom Orb, Helm of Radiance, The World Stone, Magi''s Cloak, Dreamer''s
    Idol, Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean
    Lion.'
  slot_scores:
    Stone of Binding:
      total: 0.45
      efficiency: 0.51
      win: 0.36
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.47
      efficiency: 0.66
      win: 0.4
      pick: 0.35
      fit: 0.28
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.15
      fit: 0.51
    Circe's Hexstone:
      total: 0.57
      efficiency: 0.23
      win: 1.0
      pick: 0.15
      fit: 0.24
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.21
      fit: 0.49
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.36
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Circe's Hexstone
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Genji's Guard
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  - Circe's Hexstone
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Kinetic Cuirass, Gluttonous Grimoire, Breastplate
    of Valor, Soul Gem, Helm of Radiance, Erosion, Shield of the Phoenix, Stone of
    Binding, Eye of Providence, Draconic Scale, Magi''s Cloak, Screeching Gargoyle,
    Spear of the Magus, Daybreak Gavel, Bragi''s Harp, Rod of Asclepius, Midgardian
    Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard, Hide of the Nemean
    Lion, Leviathan''s Hide.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.38
      efficiency: 0.52
      win: 0.36
      pick: 0.0
      fit: 0.24
    Genji's Guard:
      total: 0.46
      efficiency: 0.66
      win: 0.4
      pick: 0.35
      fit: 0.21
    Nimble Ring:
      total: 0.44
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.39
      efficiency: 0.44
      win: 0.36
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.21
      fit: 0.36
    Circe's Hexstone:
      total: 0.57
      efficiency: 0.23
      win: 1.0
      pick: 0.15
      fit: 0.18
  community_ordered:
  - Genji's Guard
  - Amanita Charm
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Amanita Charm
  - Circe's Hexstone
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Soul Gem, Chronos''
    Pendant, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous Grimoire, Eye
    of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Gem of Focus,
    Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of
    Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.4
      pick: 0.35
      fit: 0.48
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.56
      win: 0.36
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.15
      fit: 0.46
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.21
      fit: 0.45
    Circe's Hexstone:
      total: 0.61
      efficiency: 0.23
      win: 1.0
      pick: 0.15
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Amanita Charm
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Spear of Desolation
  - Amanita Charm
  - Circe's Hexstone
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Kinetic Cuirass, Shield Splitter, Golden Blade, Breastplate of Valor,
    Runeforged Hammer, Gluttonous Grimoire, Eye of the Storm, Hydra''s Lament, Tyrfing,
    Heartseeker, Lernaean Bow, Spear of the Magus, Erosion, Tekko-Kagi, Eye of Providence,
    Soul Gem, Shield of the Phoenix, Avenging Blade, Helm of Radiance, Silverbranch
    Bow, Stone of Binding, Draconic Scale, Obsidian Shard, Titan''s Bane, The Crusher,
    Toxic Blade, Pharaoh''s Curse, Nimble Ring, Magi''s Cloak, The Reaper, Screeching
    Gargoyle, Shogun''s Ofuda, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.45
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.35
    Genji's Guard:
      total: 0.46
      efficiency: 0.66
      win: 0.4
      pick: 0.35
      fit: 0.23
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.5
      pick: 0.15
      fit: 0.29
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.21
      fit: 0.41
    Circe's Hexstone:
      total: 0.57
      efficiency: 0.23
      win: 1.0
      pick: 0.15
      fit: 0.2
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Amanita Charm
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Spear of Desolation
  - Circe's Hexstone
  - Amanita Charm
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Kinetic Cuirass, Gluttonous Grimoire, Breastplate of Valor, Shield Splitter, Spear
    of the Magus, Soul Gem, Runeforged Hammer, Helm of Radiance, Obsidian Shard, Berserker''s
    Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion,
    Eye of Providence, Shield of the Phoenix, Stone of Binding, Draconic Scale, Doom
    Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Chronos''
    Pendant, Magi''s Cloak, The World Stone, Helm of Darkness, Titan''s Bane, Screeching
    Gargoyle, Ancient Signet, The Crusher, Mantle Of Discord, Dreamer''s Idol, Midgardian
    Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.41
    Genji's Guard:
      total: 0.46
      efficiency: 0.66
      win: 0.4
      pick: 0.35
      fit: 0.24
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.15
      fit: 0.41
    Circe's Hexstone:
      total: 0.57
      efficiency: 0.23
      win: 1.0
      pick: 0.15
      fit: 0.21
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.21
      fit: 0.41
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.36
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Circe's Hexstone
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Kinetic Cuirass, Breastplate of Valor,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Screeching
    Gargoyle, Midgardian Mail, Prophetic Cloak, Hide of the Nemean Lion, Leviathan''s
    Hide, Helm of Darkness, Void Shield, Ancile, Oni Hunter''s Garb, Gladiator''s
    Shield, Xibalban Effigy.'
  slot_scores:
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.4
      pick: 0.35
      fit: 0.4
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.36
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.32
      efficiency: 0.61
      win: 0.0
      pick: 0.22
      fit: 0.65
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.33
      pick: 0.25
      fit: 0.7
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.21
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  starter: *id001
---
