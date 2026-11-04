---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.46
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.32
    win_rate: 0.54
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.31
      win_rate: 0.51
    - name: Bracer of The Abyss
      pick_rate: 0.1
      win_rate: 0.6
  - name: Sanguine Lash
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.1
      win_rate: 0.47
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.51
  - name: Nimble Ring
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.48
    - name: Sanguine Lash
      pick_rate: 0.08
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.62
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.63
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.42
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.63
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.72
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.43
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.56
    - name: Killing Stone
      pick_rate: 0.04
      win_rate: 0.71
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.38
    win_rate: 0.62
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.36
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-11-03'
  god_win_rate: 0.5480427046263345
  god_matches_won: 308
  god_matches_played: 562
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Kinetic Cuirass, Amanita Charm, Jotunn''s Revenge, Shield
    Splitter, Gluttonous Grimoire, Genji''s Guard, Berserker''s Shield, Soul Gem,
    Runeforged Hammer, Breastplate of Valor, The Reaper, Titan''s Bane, Hydra''s Lament,
    Erosion, Spear of Desolation, Eye of Providence, Oni Hunter''s Garb, Obsidian
    Shard, Stone of Binding, Helm of Radiance, Helm of Darkness, Midgardian Mail,
    Magi''s Cloak, The Crusher, Avenging Blade, Mantle Of Discord, Screeching Gargoyle,
    Leviathan''s Hide, Heartseeker, Spear of the Magus, Arondight, Wyrmskin Hide,
    Blood-Bound Book, Ancile, Death Metal, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.57
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.51
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.47
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Gluttonous Grimoire
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Draconic Scale, Kinetic Cuirass, Gluttonous Grimoire, Genji''s Guard,
    Soul Gem, Amanita Charm, Shield Splitter, Berserker''s Shield, Spear of Desolation,
    Obsidian Shard, Breastplate of Valor, Hydra''s Lament, Helm of Radiance, Runeforged
    Hammer, The Reaper, Ancient Signet, Titan''s Bane, Helm of Darkness, Spear of
    the Magus, Oni Hunter''s Garb, Blood-Bound Book, Death Metal, Doom Orb, The World
    Stone, Heartseeker, Jade Scepter, Chronos'' Pendant, The Crusher, Erosion, Avenging
    Blade, Eye of Providence, Stone of Binding, Arondight, Screeching Gargoyle, Midgardian
    Mail, Magi''s Cloak, Polynomicon, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.44
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.23
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.54
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.34
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.62
      pick: 0.17
      fit: 0.34
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Draconic Scale, Gluttonous Grimoire, Soul Gem, Kinetic
    Cuirass, Amanita Charm, Genji''s Guard, Spear of Desolation, Berserker''s Shield,
    Obsidian Shard, Shield Splitter, Breastplate of Valor, The Reaper, Titan''s Bane,
    Spear of the Magus, Hydra''s Lament, Helm of Radiance, Runeforged Hammer, Helm
    of Darkness, Blood-Bound Book, The Crusher, Oni Hunter''s Garb, Doom Orb, Screeching
    Gargoyle, Erosion, The World Stone, Ancient Signet, Chronos'' Pendant, Eye of
    Providence, Heartseeker, Stone of Binding, Death Metal, Midgardian Mail, Arondight,
    Magi''s Cloak, Jade Scepter, Dreamer''s Idol, Leviathan''s Hide, Shield of the
    Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.59
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.36
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.62
      pick: 0.17
      fit: 0.32
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Draconic Scale, Kinetic Cuirass, The Reaper,
    Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s Shield, Shield Splitter,
    Genji''s Guard, Blood-Bound Book, Runeforged Hammer, Phoenix Feather, Yogi''s
    Necklace, Bloodforge, Ethereal Staff, Breastplate of Valor, Titan''s Bane, Hydra''s
    Lament, Spear of Desolation, Oni Hunter''s Garb, Chandra''s Grace, Obsidian Shard,
    Erosion, Shield of the Phoenix, Eye of Providence, Bancroft''s Talon, Avenging
    Blade, Midgardian Mail, Regrowth Striders, Helm of Radiance, The Crusher, Leviathan''s
    Hide, Sphere of Negation, Glorious Pridwen, Stone of Binding, Helm of Darkness,
    Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.55
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.45
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.62
      pick: 0.17
      fit: 0.18
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Draconic Scale, Kinetic Cuirass, Gluttonous Grimoire,
    Amanita Charm, Soul Gem, Stone of Binding, Genji''s Guard, Screeching Gargoyle,
    Avenging Blade, The Reaper, Berserker''s Shield, Shield Splitter, Titan''s Bane,
    Obsidian Shard, Spear of Desolation, Void Stone, Void Shield, Breastplate of Valor,
    The Crusher, Runeforged Hammer, Spear of the Magus, Heartseeker, Hydra''s Lament,
    Oni Hunter''s Garb, Erosion, Eye of Providence, Helm of Radiance, Doom Orb, Tekko-Kagi,
    The World Stone, Midgardian Mail, Helm of Darkness, Magi''s Cloak, Leviathan''s
    Hide, Mantle Of Discord, Dreamer''s Idol, Blood-Bound Book, Shield of the Phoenix.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.6
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.39
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.62
      pick: 0.17
      fit: 0.32
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
    this god: Berserker''s Shield, Draconic Scale, Kinetic Cuirass, Amanita Charm,
    Jotunn''s Revenge, Genji''s Guard, Gluttonous Grimoire, Shield Splitter, Golden
    Blade, Soul Gem, Tekko-Kagi, Tyrfing, Breastplate of Valor, Toxic Blade, Silverbranch
    Bow, Runeforged Hammer, Obsidian Shard, Pharaoh''s Curse, Spear of Desolation,
    Lernaean Bow, The Reaper, Oni Hunter''s Garb, Hydra''s Lament, Titan''s Bane,
    Helm of Radiance, Shogun''s Ofuda, Riptalon, Erosion, Eye of Providence, Stone
    of Binding, Midgardian Mail, Magi''s Cloak, Helm of Darkness, Screeching Gargoyle,
    Leviathan''s Hide, Spear of the Magus, Blood-Bound Book, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.5
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.44
    Nimble Ring:
      total: 0.54
      efficiency: 0.63
      win: 0.6
      pick: 0.19
      fit: 0.28
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.34
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Kinetic Cuirass
  - Nimble Ring
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Draconic Scale, Soul Gem, Kinetic Cuirass, Amanita Charm, Breastplate of Valor,
    Spear of Desolation, Gluttonous Grimoire, Berserker''s Shield, Hydra''s Lament,
    Shield Splitter, Screeching Gargoyle, Obsidian Shard, Chronos'' Pendant, Helm
    of Radiance, Arondight, Runeforged Hammer, Oni Hunter''s Garb, Prophetic Cloak,
    The Reaper, Helm of Darkness, Erosion, Eye of Providence, Titan''s Bane, Stone
    of Binding, Spear of the Magus, Midgardian Mail, Blood-Bound Book, Gem of Focus,
    Magi''s Cloak, Gladiator''s Shield, Heartwood Charm, Leviathan''s Hide, Mantle
    Of Discord, Ancient Signet, Regrowth Striders, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.48
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.56
      pick: 0.25
      fit: 0.55
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.38
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Draconic Scale, Gluttonous Grimoire, Kinetic
    Cuirass, Soul Gem, Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Spear of
    Desolation, Berserker''s Shield, Obsidian Shard, Shield Splitter, Helm of Radiance,
    Breastplate of Valor, Helm of Darkness, Spear of the Magus, Runeforged Hammer,
    The Reaper, Blood-Bound Book, Hydra''s Lament, Titan''s Bane, Ancient Signet,
    Death Metal, Chronos'' Pendant, Oni Hunter''s Garb, Jade Scepter, Doom Orb, Erosion,
    The World Stone, Eye of Providence, Screeching Gargoyle, Stone of Binding, Midgardian
    Mail, The Crusher, Magi''s Cloak, Dreamer''s Idol, Arondight, Avenging Blade,
    Ethereal Staff, Shield of the Phoenix.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.6
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.36
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.62
      pick: 0.17
      fit: 0.33
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Kinetic Cuirass, Gluttonous
    Grimoire, Jotunn''s Revenge, Amanita Charm, Soul Gem, Shield Splitter, Genji''s
    Guard, Berserker''s Shield, Obsidian Shard, Spear of Desolation, Helm of Radiance,
    Runeforged Hammer, The Reaper, Breastplate of Valor, Titan''s Bane, Helm of Darkness,
    Spear of the Magus, Hydra''s Lament, Blood-Bound Book, Death Metal, Oni Hunter''s
    Garb, Ancient Signet, Erosion, Eye of Providence, The Crusher, Jade Scepter, Doom
    Orb, Stone of Binding, Midgardian Mail, Avenging Blade, The World Stone, Magi''s
    Cloak, Chronos'' Pendant, Heartseeker, Screeching Gargoyle, Leviathan''s Hide,
    Mantle Of Discord, Shield of the Phoenix.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.59
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.39
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.62
      pick: 0.17
      fit: 0.3
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
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
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Shield Splitter, Kinetic
    Cuirass, Gluttonous Grimoire, Genji''s Guard, Berserker''s Shield, Soul Gem, Runeforged
    Hammer, Breastplate of Valor, The Reaper, Titan''s Bane, Hydra''s Lament, Erosion,
    Spear of Desolation, Eye of Providence, Oni Hunter''s Garb, Obsidian Shard, Draconic
    Scale, Stone of Binding, Shield of the Phoenix, Helm of Radiance, Helm of Darkness,
    Midgardian Mail, Magi''s Cloak, The Crusher, Avenging Blade, Mantle Of Discord,
    Screeching Gargoyle, Leviathan''s Hide, Heartseeker, Spear of the Magus, Arondight,
    Wyrmskin Hide, Blood-Bound Book, Ancile, Death Metal.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.26
    Berserker's Shield:
      total: 0.54
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.57
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
