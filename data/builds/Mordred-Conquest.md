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
      win_rate: 0.46
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
    win_rate: 0.41
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
  last_verified: '2026-11-02'
  god_win_rate: 0.5472370766488414
  god_matches_won: 307
  god_matches_played: 561
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
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
    Splitter, Genji''s Guard, Berserker''s Shield, Breastplate of Valor, Runeforged
    Hammer, Gluttonous Grimoire, Erosion, Titan''s Bane, Eye of Providence, Hydra''s
    Lament, Spear of Desolation, Oni Hunter''s Garb, Obsidian Shard, Stone of Binding,
    Soul Gem, Midgardian Mail, Helm of Darkness, Magi''s Cloak, Sundering Echo, Screeching
    Gargoyle, Mantle Of Discord, Helm of Radiance, Leviathan''s Hide, Heartseeker,
    The Crusher, Wyrmskin Hide, Avenging Blade, Ancile, Spear of the Magus, Void Stone,
    Stampede, The Reaper, Void Shield, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.53
      win: 0.63
      pick: 0.1
      fit: 0.61
    Shield Splitter:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.56
    Draconic Scale:
      total: 0.57
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.51
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Amanita Charm
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Draconic Scale, Kinetic Cuirass, Genji''s Guard, Amanita Charm, Berserker''s
    Shield, Breastplate of Valor, Shield Splitter, Gluttonous Grimoire, Obsidian Shard,
    Spear of Desolation, Sundering Echo, Soul Gem, Hydra''s Lament, Helm of Radiance,
    Runeforged Hammer, Titan''s Bane, Helm of Darkness, Oni Hunter''s Garb, Spear
    of the Magus, Doom Orb, The World Stone, Death Metal, Heartseeker, Erosion, Chronos''
    Pendant, Screeching Gargoyle, Eye of Providence, Stone of Binding, Jade Scepter,
    The Crusher, Midgardian Mail, Wish-Granting Pearl, Heartwood Charm, Ancient Signet,
    Magi''s Cloak, Polynomicon, Avenging Blade, Arondight, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.63
      pick: 0.1
      fit: 0.46
    Draconic Scale:
      total: 0.55
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.36
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.81
      win: 0.62
      pick: 0.17
      fit: 0.36
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.36
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
  - Spear of Desolation
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Spear of Desolation
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Draconic Scale, Kinetic Cuirass, Amanita Charm, Genji''s
    Guard, Spear of Desolation, Gluttonous Grimoire, Soul Gem, Obsidian Shard, Berserker''s
    Shield, Breastplate of Valor, Shield Splitter, Titan''s Bane, Spear of the Magus,
    Hydra''s Lament, Sundering Echo, Helm of Radiance, Runeforged Hammer, Helm of
    Darkness, Doom Orb, Screeching Gargoyle, The World Stone, Heartseeker, Erosion,
    Oni Hunter''s Garb, The Crusher, Chronos'' Pendant, Eye of Providence, Stone of
    Binding, Midgardian Mail, The Reaper, Magi''s Cloak, Death Metal, Leviathan''s
    Hide, Mantle Of Discord, Dreamer''s Idol, Arondight, Jade Scepter, Shield of the
    Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.1
      fit: 0.48
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.48
    Draconic Scale:
      total: 0.55
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
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
  - Jotunn's Revenge
  - Soul Gem
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
    this god: Amanita Charm, Draconic Scale, Kinetic Cuirass, Jotunn''s Revenge, Soul
    Gem, Berserker''s Shield, Genji''s Guard, Shield Splitter, The Reaper, Phoenix
    Feather, Runeforged Hammer, Yogi''s Necklace, Gluttonous Grimoire, Breastplate
    of Valor, Ethereal Staff, Chandra''s Grace, Titan''s Bane, Erosion, Hydra''s Lament,
    Spear of Desolation, Oni Hunter''s Garb, Eye of Providence, Obsidian Shard, Shield
    of the Phoenix, Midgardian Mail, Glorious Pridwen, Sundering Echo, Regrowth Striders,
    Avenging Blade, Leviathan''s Hide, Blood-Bound Book, Rod of Asclepius, Heartseeker,
    Wyrmskin Hide, Stone of Binding, Sphere of Negation, The Crusher, Screeching Gargoyle,
    Helm of Radiance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.1
      fit: 0.6
    Draconic Scale:
      total: 0.57
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.5
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.81
      win: 0.62
      pick: 0.17
      fit: 0.2
    Amanita Charm:
      total: 0.6
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.54
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Draconic Scale, Kinetic Cuirass, Amanita Charm,
    Stone of Binding, Screeching Gargoyle, Genji''s Guard, Gluttonous Grimoire, Titan''s
    Bane, Berserker''s Shield, Obsidian Shard, Shield Splitter, Avenging Blade, Spear
    of Desolation, Void Stone, Void Shield, Soul Gem, Breastplate of Valor, Heartseeker,
    The Crusher, Spear of the Magus, Runeforged Hammer, The Reaper, Erosion, Hydra''s
    Lament, Oni Hunter''s Garb, Doom Orb, Eye of Providence, The World Stone, Tekko-Kagi,
    Sundering Echo, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Helm of Darkness,
    Mantle Of Discord, Leviathan''s Hide, Pendulum Blade, Shield of the Phoenix.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.63
    Stone of Binding:
      total: 0.53
      efficiency: 0.47
      win: 0.58
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.1
      fit: 0.52
    Draconic Scale:
      total: 0.56
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Draconic Scale, Kinetic Cuirass, Amanita Charm,
    Jotunn''s Revenge, Genji''s Guard, Gluttonous Grimoire, Golden Blade, Soul Gem,
    Breastplate of Valor, Shield Splitter, Tekko-Kagi, Toxic Blade, Tyrfing, Silverbranch
    Bow, Pharaoh''s Curse, Obsidian Shard, Riptalon, Runeforged Hammer, Spear of Desolation,
    Shogun''s Ofuda, Titan''s Bane, The Reaper, Lernaean Bow, Oni Hunter''s Garb,
    Hydra''s Lament, Erosion, Eros'' Bow, Stone of Binding, Helm of Radiance, Eye
    of Providence, Midgardian Mail, Screeching Gargoyle, Sundering Echo, Magi''s Cloak,
    Helm of Darkness, Leviathan''s Hide, Mantle Of Discord, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.5
    Berserker's Shield:
      total: 0.57
      efficiency: 0.7
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.63
      pick: 0.1
      fit: 0.44
    Nimble Ring:
      total: 0.53
      efficiency: 0.61
      win: 0.6
      pick: 0.19
      fit: 0.28
    Draconic Scale:
      total: 0.54
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.34
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
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
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Draconic Scale, Kinetic Cuirass, Breastplate of Valor, Amanita Charm, Spear of
    Desolation, Soul Gem, Berserker''s Shield, Hydra''s Lament, Screeching Gargoyle,
    Shield Splitter, Gluttonous Grimoire, Obsidian Shard, Chronos'' Pendant, Prophetic
    Cloak, Erosion, Arondight, Helm of Radiance, Oni Hunter''s Garb, Gladiator''s
    Shield, Runeforged Hammer, Helm of Darkness, Eye of Providence, Stone of Binding,
    Titan''s Bane, Heartwood Charm, Gem of Focus, Midgardian Mail, Chandra''s Grace,
    Magi''s Cloak, Sundering Echo, Spear of the Magus, Mantle Of Discord, Leviathan''s
    Hide, Glorious Pridwen, Regrowth Striders, Eye of Erebus, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.1
      fit: 0.51
    Freya's Tears:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.25
      fit: 0.59
    Draconic Scale:
      total: 0.56
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.41
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spear of Desolation
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Spear of Desolation
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
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Draconic Scale, Kinetic Cuirass, Jotunn''s
    Revenge, Amanita Charm, Genji''s Guard, Spear of Desolation, Gluttonous Grimoire,
    Obsidian Shard, Berserker''s Shield, Soul Gem, Shield Splitter, Breastplate of
    Valor, Sundering Echo, Helm of Radiance, Helm of Darkness, Spear of the Magus,
    Titan''s Bane, Runeforged Hammer, Hydra''s Lament, Doom Orb, Chronos'' Pendant,
    Death Metal, The World Stone, Erosion, Oni Hunter''s Garb, Screeching Gargoyle,
    Jade Scepter, Eye of Providence, Stone of Binding, Midgardian Mail, Magi''s Cloak,
    Heartseeker, Ethereal Staff, The Crusher, Dreamer''s Idol, Mantle Of Discord,
    Leviathan''s Hide, Heartwood Charm, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.1
      fit: 0.49
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.46
    Draconic Scale:
      total: 0.55
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.39
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Kinetic Cuirass, Jotunn''s
    Revenge, Amanita Charm, Genji''s Guard, Gluttonous Grimoire, Berserker''s Shield,
    Shield Splitter, Obsidian Shard, Spear of Desolation, Soul Gem, Sundering Echo,
    Breastplate of Valor, Helm of Radiance, Titan''s Bane, Runeforged Hammer, Helm
    of Darkness, Spear of the Magus, Hydra''s Lament, Erosion, Oni Hunter''s Garb,
    Death Metal, Eye of Providence, Doom Orb, Stone of Binding, The World Stone, Heartseeker,
    Midgardian Mail, The Crusher, Screeching Gargoyle, Magi''s Cloak, Jade Scepter,
    Chronos'' Pendant, Mantle Of Discord, Leviathan''s Hide, Avenging Blade, The Reaper,
    Triton''s Conch, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.23
    Berserker's Shield:
      total: 0.52
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.1
      fit: 0.52
    Draconic Scale:
      total: 0.56
      efficiency: 0.47
      win: 0.72
      pick: 0.11
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
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
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Genji''s Guard, Berserker''s Shield, Breastplate of Valor, Runeforged
    Hammer, Gluttonous Grimoire, Erosion, Titan''s Bane, Eye of Providence, Draconic
    Scale, Hydra''s Lament, Spear of Desolation, Oni Hunter''s Garb, Obsidian Shard,
    Shield of the Phoenix, Stone of Binding, Soul Gem, Midgardian Mail, Helm of Darkness,
    Magi''s Cloak, Sundering Echo, Screeching Gargoyle, Mantle Of Discord, Helm of
    Radiance, Leviathan''s Hide, Heartseeker, The Crusher, Wyrmskin Hide, Avenging
    Blade, Ancile, Spear of the Magus, Void Stone, Stampede, The Reaper, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.28
    Berserker's Shield:
      total: 0.53
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.53
      win: 0.63
      pick: 0.1
      fit: 0.61
    Shield Splitter:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.58
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
