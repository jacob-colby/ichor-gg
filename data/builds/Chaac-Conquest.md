---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.33
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.25
    win_rate: 0.25
    alternates:
    - name: Helm of Radiance
      pick_rate: 0.19
      win_rate: 0.33
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.67
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.0
  - name: Gladiator's Shield
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.0
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.27
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 1.0
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 1.0
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.5
    - name: Spirit Robe
      pick_rate: 0.14
      win_rate: 0.5
  - name: Brawler’s Beat Stick
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Contagion
      pick_rate: 0.1
      win_rate: 0.0
    - name: Mana Tome
      pick_rate: 0.1
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.63
    win_rate: 0.6
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.33
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-08-26'
  god_win_rate: 0.5
  god_matches_won: 8
  god_matches_played: 16
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Shield Splitter, Spear of Desolation, Runeforged Hammer, Spear of the Magus, Soul
    Gem, Berserker''s Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye of Providence,
    Hydra''s Lament, Draconic Scale, Heartseeker, Shield of the Phoenix, Stone of
    Binding, Rod of Asclepius, Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb,
    Screeching Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of Darkness,
    Midgardian Mail, Titan''s Bane, Death Metal, Chronos'' Pendant, The Crusher, Daybreak
    Gavel, The World Stone, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.55
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.12
      fit: 0.32
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.3
      fit: 0.4
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Spear of Desolation,
    Shield Splitter, Spear of the Magus, Hydra''s Lament, Runeforged Hammer, Soul
    Gem, Obsidian Shard, Heartseeker, Berserker''s Shield, Eye of the Storm, Rod of
    Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet, The World Stone, Shield
    of the Phoenix, Erosion, Death Metal, Chronos'' Pendant, Jade Scepter, Stone of
    Binding, Eye of Providence, Avenging Blade, Draconic Scale, Screeching Gargoyle,
    Magi''s Cloak, Titan''s Bane, Helm of Darkness, Triton''s Conch, The Crusher,
    Daybreak Gavel, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.29
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.12
      fit: 0.26
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.3
      fit: 0.35
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Spear
    of Desolation, Soul Gem, Spear of the Magus, Obsidian Shard, Shield Splitter,
    Runeforged Hammer, Berserker''s Shield, Hydra''s Lament, Heartseeker, Shield of
    the Phoenix, Eye of the Storm, Erosion, Doom Orb, Rod of Asclepius, Eye of Providence,
    Screeching Gargoyle, Stone of Binding, Chronos'' Pendant, Draconic Scale, The
    World Stone, Titan''s Bane, The Crusher, Dreamer''s Idol, Magi''s Cloak, Jade
    Scepter, The Reaper, Wish-Granting Pearl, Avenging Blade, Daybreak Gavel, Mantle
    Of Discord, Midgardian Mail, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.27
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.48
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.12
      fit: 0.27
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.3
      fit: 0.41
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Soul Gem, Rod of Asclepius,
    Shield of the Phoenix, Gluttonous Grimoire, Ethereal Staff, The Reaper, Runeforged
    Hammer, Spear of Desolation, Spear of the Magus, Shield Splitter, Berserker''s
    Shield, Lifebinder, Obsidian Shard, Eye of the Storm, Yogi''s Necklace, Sphere
    of Negation, Hydra''s Lament, Erosion, Heartseeker, Phoenix Feather, Eye of Providence,
    Chandra''s Grace, Draconic Scale, Avenging Blade, Blood-Bound Book, Jade Scepter,
    Wish-Granting Pearl, Stone of Binding, Daybreak Gavel, Doom Orb, Glorious Pridwen,
    Midgardian Mail, Titan''s Bane.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.42
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.12
      fit: 0.26
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.3
      fit: 0.35
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Stone of Binding, Spear of Desolation, Spear of the Magus, Avenging Blade, Screeching
    Gargoyle, Soul Gem, Obsidian Shard, Void Shield, Heartseeker, Void Stone, Shield
    Splitter, Runeforged Hammer, Berserker''s Shield, Doom Orb, Titan''s Bane, The
    Crusher, The World Stone, Eye of the Storm, Hydra''s Lament, Dreamer''s Idol,
    Erosion, The Reaper, Eye of Providence, Rod of Asclepius, Shield of the Phoenix,
    Draconic Scale, Magi''s Cloak, Jade Scepter, Daybreak Gavel, Wish-Granting Pearl,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.48
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.12
      fit: 0.27
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.3
      fit: 0.34
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Shell of Rebuke
  - Freya's Tears
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Gluttonous Grimoire,
    Nimble Ring, Amanita Charm, Soul Gem, Golden Blade, Riptalon, Spear of the Magus,
    Spear of Desolation, Silverbranch Bow, Runeforged Hammer, Tyrfing, Shield Splitter,
    Obsidian Shard, Lernaean Bow, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda,
    The Reaper, Rod of Asclepius, Hydra''s Lament, Stone of Binding, Erosion, Tekko-Kagi,
    Bragi''s Harp, Shield of the Phoenix, Eye of Providence, Eye of the Storm, Bracer
    of The Abyss, Heartseeker, Draconic Scale, Daybreak Gavel, Magi''s Cloak, Screeching
    Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.12
      fit: 0.22
    Freya's Tears:
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.3
      fit: 0.28
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Spear of Desolation, Soul Gem, Shield of the Phoenix, Hydra''s
    Lament, Screeching Gargoyle, Gluttonous Grimoire, Berserker''s Shield, Chronos''
    Pendant, Shield Splitter, Spear of the Magus, Runeforged Hammer, Prophetic Cloak,
    Erosion, Obsidian Shard, Eye of Providence, Stone of Binding, Draconic Scale,
    Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Heartseeker,
    Eye of Erebus, Mantle Of Discord, Daybreak Gavel, Midgardian Mail, Pendulum Blade,
    Hide of the Nemean Lion, Glorious Pridwen, Jade Scepter, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.51
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.5
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.12
      fit: 0.29
    Freya's Tears:
      total: 0.77
      efficiency: 0.61
      win: 1.0
      pick: 0.3
      fit: 0.58
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous
    Grimoire, Shield Splitter, Spear of Desolation, Runeforged Hammer, Spear of the
    Magus, Soul Gem, Berserker''s Shield, Obsidian Shard, Eye of the Storm, Erosion,
    Eye of Providence, Hydra''s Lament, Draconic Scale, Heartseeker, Shield of the
    Phoenix, Stone of Binding, Rod of Asclepius, Magi''s Cloak, Avenging Blade, Jade
    Scepter, Doom Orb, Screeching Gargoyle, Wish-Granting Pearl, Mantle Of Discord,
    Helm of Darkness, Midgardian Mail, Titan''s Bane, Death Metal, Chronos'' Pendant,
    The Crusher, Daybreak Gavel, The World Stone, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.55
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.3
      fit: 0.4
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
---
