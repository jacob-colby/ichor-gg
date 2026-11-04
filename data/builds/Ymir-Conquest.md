---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Avenging Blade
    pick_rate: 1.0
    win_rate: 1.0
  - name: Berserker's Shield
    pick_rate: 1.0
    win_rate: 1.0
  - name: Kinetic Cuirass
    pick_rate: 1.0
    win_rate: 1.0
  - name: Hussar's Wings
    pick_rate: 1.0
    win_rate: 1.0
  - name: Hide of the Nemean Lion
    pick_rate: 1.0
    win_rate: 1.0
  - name: Brawler’s Beat Stick
    pick_rate: 1.0
    win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 1.0
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-11-04'
  god_win_rate: 1
  god_matches_won: 1
  god_matches_played: 1
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
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Hussar's Wings
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Freya''s Tears, Erosion,
    Eye of Providence, Breastplate of Valor, Draconic Scale, Oni Hunter''s Garb, Helm
    of Darkness, Shield of the Phoenix, Shifter''s Shield, Stone of Binding, Nimble
    Ring, Magi''s Cloak, Midgardian Mail, Helm of Radiance, Mantle Of Discord, Leviathan''s
    Hide, Screeching Gargoyle, Soul Gem, Ancile, Gluttonous Grimoire, Prophetic Cloak,
    Stampede, Void Stone, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.74
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.81
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.74
    Freya's Tears:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.57
    Hussar's Wings:
      total: 0.73
      efficiency: 0.38
      win: 1.0
      pick: 1.0
      fit: 0.64
    Hide of the Nemean Lion:
      total: 0.74
      efficiency: 0.51
      win: 1.0
      pick: 1.0
      fit: 0.41
    Amanita Charm:
      total: 0.77
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Kinetic Cuirass
  - Hussar's Wings
  - Hide of the Nemean Lion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
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
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Soul Gem, Genji''s
    Guard, Blood-Bound Book, Phoenix Feather, Freya''s Tears, Erosion, Ethereal Staff,
    Eye of Providence, Yogi''s Necklace, Draconic Scale, Breastplate of Valor, Oni
    Hunter''s Garb, Chandra''s Grace, Nimble Ring, Midgardian Mail, Shifter''s Shield,
    Glorious Pridwen, Leviathan''s Hide, Bancroft''s Talon, Helm of Darkness, Gluttonous
    Grimoire, Regrowth Striders, Helm of Radiance, Stone of Binding, Sphere of Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.74
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.8
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.73
    Shield of the Phoenix:
      total: 0.76
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.85
    Hide of the Nemean Lion:
      total: 0.74
      efficiency: 0.51
      win: 1.0
      pick: 1.0
      fit: 0.43
    Freya's Tears:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.82
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.93
  community_ordered:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Amanita Charm, Soul Gem, Stone
    of Binding, Genji''s Guard, Screeching Gargoyle, Spear of Desolation, Obsidian
    Shard, Void Stone, Void Shield, Freya''s Tears, Spear of the Magus, Breastplate
    of Valor, Nimble Ring, Erosion, Oni Hunter''s Garb, Eye of Providence, Doom Orb,
    Helm of Radiance, Draconic Scale, The World Stone, Helm of Darkness, Shield of
    the Phoenix, Midgardian Mail, Magi''s Cloak, Dreamer''s Idol, Mantle Of Discord.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.73
      efficiency: 0.5
      win: 1.0
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.78
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.67
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Genji''s Guard, Nimble Ring, Freya''s
    Tears, Breastplate of Valor, Oni Hunter''s Garb, Helm of Radiance, Erosion, Eye
    of Providence, Stone of Binding, Draconic Scale, Helm of Darkness, Midgardian
    Mail, Shield of the Phoenix, Magi''s Cloak, Soul Gem, Screeching Gargoyle, Bragi''s
    Harp, Leviathan''s Hide, Mantle Of Discord, Blood-Bound Book, Shifter''s Shield,
    Gluttonous Grimoire, Ancient Signet, Bracer of The Abyss, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.72
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.2
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.48
    Bracer of The Abyss:
      total: 0.67
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.72
      efficiency: 0.63
      win: 1.0
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.73
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Freya''s
    Tears, Amanita Charm, Breastplate of Valor, Soul Gem, Shield of the Phoenix, Screeching
    Gargoyle, Nimble Ring, Chronos'' Pendant, Helm of Radiance, Prophetic Cloak, Oni
    Hunter''s Garb, Erosion, Helm of Darkness, Eye of Providence, Draconic Scale,
    Stone of Binding, Gladiator''s Shield, Gem of Focus, Spear of Desolation, Midgardian
    Mail, Magi''s Cloak, Heartwood Charm, Blood-Bound Book, Mantle Of Discord, Leviathan''s
    Hide, Gluttonous Grimoire.'
  slot_scores:
    Genji's Guard:
      total: 0.76
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.74
      efficiency: 0.63
      win: 1.0
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 1.0
      fit: 0.27
    Freya's Tears:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Shield Splitter, Gluttonous Grimoire, Genji''s Guard, Soul Gem, Runeforged
    Hammer, The Reaper, Tekko-Kagi, Golden Blade, Titan''s Bane, Freya''s Tears, Breastplate
    of Valor, Hydra''s Lament, Nimble Ring, Obsidian Shard, Tyrfing, Spear of Desolation,
    The Crusher, Oni Hunter''s Garb, Lernaean Bow, Helm of Radiance, Erosion, Eye
    of Providence, Heartseeker, Stone of Binding, Toxic Blade, Draconic Scale, Helm
    of Darkness, Midgardian Mail, Shield of the Phoenix, Arondight, Spear of the Magus,
    Silverbranch Bow, Magi''s Cloak, Death Metal, Pharaoh''s Curse.'
  slot_scores:
    Avenging Blade:
      total: 0.74
      efficiency: 0.49
      win: 1.0
      pick: 1.0
      fit: 0.42
    Berserker's Shield:
      total: 0.81
      efficiency: 0.74
      win: 1.0
      pick: 1.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.49
    Shield Splitter:
      total: 0.73
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    Jotunn''s Revenge, Amanita Charm, Soul Gem, Shield Splitter, Genji''s Guard, Obsidian
    Shard, Spear of Desolation, Nimble Ring, Helm of Radiance, Freya''s Tears, Runeforged
    Hammer, Breastplate of Valor, The Reaper, Titan''s Bane, Helm of Darkness, Spear
    of the Magus, Hydra''s Lament, Tekko-Kagi, Golden Blade, Blood-Bound Book, Death
    Metal, Oni Hunter''s Garb, Ancient Signet, Erosion, Eye of Providence, The Crusher,
    Tyrfing, Jade Scepter, Stone of Binding, Doom Orb, Draconic Scale, Midgardian
    Mail, Shield of the Phoenix, The World Stone, Magi''s Cloak, Chronos'' Pendant.'
  slot_scores:
    Avenging Blade:
      total: 0.73
      efficiency: 0.49
      win: 1.0
      pick: 1.0
      fit: 0.37
    Berserker's Shield:
      total: 0.8
      efficiency: 0.74
      win: 1.0
      pick: 1.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.3
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Eye of Providence
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Freya''s
    Tears, Erosion, Eye of Providence, Breastplate of Valor, Draconic Scale, Oni Hunter''s
    Garb, Helm of Darkness, Shield of the Phoenix, Shifter''s Shield, Stone of Binding,
    Nimble Ring, Magi''s Cloak, Midgardian Mail, Helm of Radiance, Mantle Of Discord,
    Leviathan''s Hide, Screeching Gargoyle, Soul Gem, Ancile, Gluttonous Grimoire,
    Prophetic Cloak, Stampede, Void Stone, Void Shield.'
  slot_scores:
    Eye of Providence:
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.74
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.81
      efficiency: 0.56
      win: 1.0
      pick: 1.0
      fit: 0.74
    Freya's Tears:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.77
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
