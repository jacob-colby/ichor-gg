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
    win_rate: 0.57
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.1
      win_rate: 0.47
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.51
  - name: Nimble Ring
    pick_rate: 0.13
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.48
    - name: Sanguine Lash
      pick_rate: 0.08
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.61
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
      win_rate: 0.69
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
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.36
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.68
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-11-04'
  god_win_rate: 0.5469026548672566
  god_matches_won: 309
  god_matches_played: 565
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Draconic Scale, Amanita Charm, Jotunn''s Revenge, Genji''s
    Guard, Shield Splitter, Gluttonous Grimoire, Berserker''s Shield, Soul Gem, Breastplate
    of Valor, The Reaper, Runeforged Hammer, Oni Hunter''s Garb, Spear of Desolation,
    Erosion, Eye of Providence, Hydra''s Lament, The Crusher, Midgardian Mail, Stone
    of Binding, Screeching Gargoyle, Leviathan''s Hide, Heartseeker, Helm of Radiance,
    Magi''s Cloak, Mantle Of Discord, Helm of Darkness, Blood-Bound Book, Death Metal,
    Titan''s Bane, Obsidian Shard, Ancile, Avenging Blade, Wyrmskin Hide, Tyrfing,
    Arondight, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.1
      fit: 0.57
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.25
      fit: 0.42
    Draconic Scale:
      total: 0.57
      efficiency: 0.53
      win: 0.69
      pick: 0.11
      fit: 0.47
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
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
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Kinetic
    Cuirass, Draconic Scale, Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Soul
    Gem, Gluttonous Grimoire, Spear of Desolation, Shield Splitter, Berserker''s Shield,
    Breastplate of Valor, Hydra''s Lament, The Reaper, Ancient Signet, Oni Hunter''s
    Garb, Blood-Bound Book, Death Metal, Helm of Radiance, Runeforged Hammer, Polynomicon,
    Obsidian Shard, Heartseeker, Helm of Darkness, Spear of the Magus, Chronos'' Pendant,
    The Crusher, Screeching Gargoyle, Erosion, Dreamer''s Idol, Doom Orb, Eye of Providence,
    Jade Scepter, Bancroft''s Talon, Midgardian Mail, Soul Reaver, Heartwood Charm,
    Stone of Binding, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.1
      fit: 0.44
    Transcendence:
      total: 0.47
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.23
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.69
      pick: 0.11
      fit: 0.34
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.61
      pick: 0.18
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
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
  - Draconic Scale
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Kinetic Cuirass, Draconic Scale, Soul Gem, Jotunn''s Revenge, Amanita Charm,
    Gluttonous Grimoire, Genji''s Guard, Spear of Desolation, Berserker''s Shield,
    Breastplate of Valor, Shield Splitter, The Reaper, Obsidian Shard, Hydra''s Lament,
    Spear of the Magus, Blood-Bound Book, Oni Hunter''s Garb, Helm of Radiance, Runeforged
    Hammer, The Crusher, Screeching Gargoyle, Heartseeker, Dreamer''s Idol, Death
    Metal, Chronos'' Pendant, Helm of Darkness, Ancient Signet, Erosion, Eye of Providence,
    Titan''s Bane, Polynomicon, Midgardian Mail, Doom Orb, Stone of Binding, Leviathan''s
    Hide, Arondight, Jade Scepter, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.1
      fit: 0.46
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.11
      fit: 0.36
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.61
      pick: 0.18
      fit: 0.32
    Soul Gem:
      total: 0.55
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.61
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
  - Draconic Scale
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Soul Gem, Draconic Scale, The Reaper,
    Jotunn''s Revenge, Genji''s Guard, Gluttonous Grimoire, Blood-Bound Book, Berserker''s
    Shield, Shield Splitter, Phoenix Feather, Shield of the Phoenix, Yogi''s Necklace,
    Runeforged Hammer, Ethereal Staff, Breastplate of Valor, Chandra''s Grace, Oni
    Hunter''s Garb, Spear of Desolation, Hydra''s Lament, Bancroft''s Talon, Erosion,
    Bloodforge, Eye of Providence, Regrowth Striders, The Crusher, Midgardian Mail,
    Leviathan''s Hide, Heartseeker, Glorious Pridwen, Screeching Gargoyle, Avenging
    Blade, Death Metal, Titan''s Bane, Helm of Radiance, Sphere of Negation.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.1
      fit: 0.55
    Draconic Scale:
      total: 0.57
      efficiency: 0.53
      win: 0.69
      pick: 0.11
      fit: 0.45
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.61
      pick: 0.18
      fit: 0.18
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.57
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
  - Screeching Gargoyle
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Kinetic Cuirass, Draconic Scale, Jotunn''s Revenge, Amanita Charm,
    Gluttonous Grimoire, Soul Gem, Genji''s Guard, Screeching Gargoyle, Stone of Binding,
    The Reaper, Spear of Desolation, Berserker''s Shield, Shield Splitter, Avenging
    Blade, Void Stone, Void Shield, The Crusher, Breastplate of Valor, Heartseeker,
    Obsidian Shard, Titan''s Bane, Runeforged Hammer, Oni Hunter''s Garb, Spear of
    the Magus, Hydra''s Lament, Erosion, Eye of Providence, Dreamer''s Idol, Midgardian
    Mail, Blood-Bound Book, Helm of Radiance, Leviathan''s Hide, Magi''s Cloak, Mantle
    Of Discord, Doom Orb, Death Metal, Shield of the Phoenix.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.61
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.21
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.1
      fit: 0.49
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.11
      fit: 0.39
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Nimble Ring
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Draconic Scale, Amanita Charm,
    Genji''s Guard, Jotunn''s Revenge, Tyrfing, Gluttonous Grimoire, Soul Gem, Shield
    Splitter, Golden Blade, Breastplate of Valor, Spear of Desolation, Oni Hunter''s
    Garb, The Reaper, Toxic Blade, Runeforged Hammer, Hydra''s Lament, Shogun''s Ofuda,
    Erosion, Silverbranch Bow, Pharaoh''s Curse, Eye of Providence, Tekko-Kagi, Screeching
    Gargoyle, Blood-Bound Book, Bragi''s Harp, Midgardian Mail, Helm of Radiance,
    Riptalon, Stone of Binding, Lernaean Bow, Leviathan''s Hide, Dominance, The Crusher,
    Obsidian Shard, Shield of the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.1
      fit: 0.44
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.5
    Nimble Ring:
      total: 0.52
      efficiency: 0.57
      win: 0.6
      pick: 0.2
      fit: 0.28
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.69
      pick: 0.11
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.57
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
  - Soul Gem
  - Jotunn's Revenge
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
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Genji''s Guard, Draconic
    Scale, Soul Gem, Jotunn''s Revenge, Amanita Charm, Breastplate of Valor, Spear
    of Desolation, Gluttonous Grimoire, Berserker''s Shield, Screeching Gargoyle,
    Hydra''s Lament, Shield Splitter, Chronos'' Pendant, Oni Hunter''s Garb, Gladiator''s
    Shield, Shield of the Phoenix, Prophetic Cloak, The Reaper, Arondight, Erosion,
    Blood-Bound Book, Helm of Radiance, Eye of Providence, Runeforged Hammer, Midgardian
    Mail, Gem of Focus, Obsidian Shard, Heartwood Charm, Helm of Darkness, Stone of
    Binding, Ancient Signet, Chandra''s Grace, Leviathan''s Hide, Magi''s Cloak, Mantle
    Of Discord, Regrowth Striders.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.1
      fit: 0.48
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.56
      pick: 0.25
      fit: 0.55
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.11
      fit: 0.38
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.57
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
  - Draconic Scale
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Kinetic Cuirass, Draconic Scale, Soul Gem,
    Amanita Charm, Gluttonous Grimoire, Jotunn''s Revenge, Genji''s Guard, Spear of
    Desolation, Berserker''s Shield, Shield Splitter, Breastplate of Valor, Blood-Bound
    Book, Helm of Radiance, Obsidian Shard, The Reaper, Death Metal, Helm of Darkness,
    Ancient Signet, Spear of the Magus, Hydra''s Lament, Runeforged Hammer, Oni Hunter''s
    Garb, Chronos'' Pendant, Polynomicon, Dreamer''s Idol, Screeching Gargoyle, Erosion,
    The Crusher, Jade Scepter, Eye of Providence, Midgardian Mail, Heartseeker, Doom
    Orb, Stone of Binding, Ethereal Staff, Leviathan''s Hide, Triton''s Conch, Shield
    of the Phoenix.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.1
      fit: 0.46
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.11
      fit: 0.36
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.61
      pick: 0.18
      fit: 0.33
    Soul Gem:
      total: 0.55
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Draconic Scale, Amanita
    Charm, Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, Genji''s Guard, Shield
    Splitter, Spear of Desolation, Berserker''s Shield, The Reaper, Breastplate of
    Valor, Blood-Bound Book, Helm of Radiance, Runeforged Hammer, Obsidian Shard,
    Death Metal, Oni Hunter''s Garb, Helm of Darkness, Hydra''s Lament, Spear of the
    Magus, Ancient Signet, The Crusher, Erosion, Eye of Providence, Polynomicon, Heartseeker,
    Dreamer''s Idol, Chronos'' Pendant, Screeching Gargoyle, Midgardian Mail, Stone
    of Binding, Jade Scepter, Titan''s Bane, Leviathan''s Hide, Magi''s Cloak, Mantle
    Of Discord, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.21
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.1
      fit: 0.49
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.25
      fit: 0.35
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.11
      fit: 0.39
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
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
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Genji''s
    Guard, Shield Splitter, Gluttonous Grimoire, Berserker''s Shield, Soul Gem, Breastplate
    of Valor, The Reaper, Shield of the Phoenix, Draconic Scale, Runeforged Hammer,
    Oni Hunter''s Garb, Spear of Desolation, Erosion, Eye of Providence, Hydra''s
    Lament, The Crusher, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s
    Hide, Heartseeker, Helm of Radiance, Magi''s Cloak, Mantle Of Discord, Helm of
    Darkness, Blood-Bound Book, Death Metal, Titan''s Bane, Obsidian Shard, Ancile,
    Avenging Blade, Wyrmskin Hide, Tyrfing, Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.1
      fit: 0.57
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.25
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
