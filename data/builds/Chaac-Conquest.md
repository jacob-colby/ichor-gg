---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.58
  slot_order:
  - name: Daybreak Gavel
    pick_rate: 0.35
    win_rate: 0.48
    alternates:
    - name: Heartwood Charm
      pick_rate: 0.31
      win_rate: 0.64
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.38
  - name: Chronos' Pendant
    pick_rate: 0.27
    win_rate: 0.65
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.58
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.6
  - name: Rod of Asclepius
    pick_rate: 0.23
    win_rate: 0.62
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.36
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.67
  - name: Breastplate of Valor
    pick_rate: 0.17
    win_rate: 0.45
    alternates:
    - name: Rod of Asclepius
      pick_rate: 0.09
      win_rate: 0.64
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.55
  - name: Rod of Tahuti
    pick_rate: 0.18
    win_rate: 0.68
    alternates:
    - name: Heartwood Charm
      pick_rate: 0.05
      win_rate: 0.4
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.4
  - name: Shield
    pick_rate: 0.08
    win_rate: 0.8
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.8
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.23
    win_rate: 0.52
  - name: Blood-soaked Shroud
    pick_rate: 0.22
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-09-14'
  god_win_rate: 0.5725806451612904
  god_matches_won: 71
  god_matches_played: 124
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-14'
  god_matches_analyzed: 6946
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Kinetic Cuirass, Gluttonous
    Grimoire, Shield Splitter, Spear of Desolation, Runeforged Hammer, Spear of the
    Magus, Helm of Radiance, Soul Gem, Berserker''s Shield, Obsidian Shard, Eye of
    the Storm, Shifter''s Shield, Erosion, Eye of Providence, Hydra''s Lament, Draconic
    Scale, Heartseeker, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Avenging
    Blade, Jade Scepter, Doom Orb, Screeching Gargoyle, Wish-Granting Pearl, Mantle
    Of Discord, Helm of Darkness, Midgardian Mail, Titan''s Bane, Death Metal, The
    Crusher, The World Stone, Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.11
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.55
    Hide of the Nemean Lion:
      total: 0.6
      efficiency: 0.52
      win: 0.8
      pick: 0.25
      fit: 0.29
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.68
      pick: 0.39
      fit: 0.3
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Rod of Tahuti
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Genji''s Guard, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Spear of Desolation, Shield Splitter, Spear of the Magus, Hydra''s Lament, Runeforged
    Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Heartseeker, Berserker''s
    Shield, Eye of the Storm, Wish-Granting Pearl, Doom Orb, Ancient Signet, Shifter''s
    Shield, The World Stone, Shield of the Phoenix, Erosion, Death Metal, Jade Scepter,
    Stone of Binding, Eye of Providence, Avenging Blade, Draconic Scale, Screeching
    Gargoyle, Magi''s Cloak, Titan''s Bane, Helm of Darkness, Triton''s Conch, The
    Crusher, Oni Hunter''s Garb, Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.11
      fit: 0.29
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.46
    Hide of the Nemean Lion:
      total: 0.59
      efficiency: 0.52
      win: 0.8
      pick: 0.25
      fit: 0.23
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.68
      pick: 0.39
      fit: 0.36
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hide of the Nemean Lion
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Genji''s Guard, Amanita Charm, Gluttonous Grimoire, Spear
    of Desolation, Kinetic Cuirass, Soul Gem, Spear of the Magus, Obsidian Shard,
    Shield Splitter, Runeforged Hammer, Helm of Radiance, Berserker''s Shield, Hydra''s
    Lament, Heartseeker, Shield of the Phoenix, Shifter''s Shield, Eye of the Storm,
    Erosion, Doom Orb, Eye of Providence, Screeching Gargoyle, Stone of Binding, Draconic
    Scale, The World Stone, Titan''s Bane, The Crusher, Dreamer''s Idol, Magi''s Cloak,
    Jade Scepter, The Reaper, Wish-Granting Pearl, Avenging Blade, Mantle Of Discord,
    Midgardian Mail, Ancient Signet, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.14
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.11
      fit: 0.27
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.14
    Hide of the Nemean Lion:
      total: 0.59
      efficiency: 0.52
      win: 0.8
      pick: 0.25
      fit: 0.25
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.68
      pick: 0.39
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Rod of Tahuti
  - Rod of Asclepius
  - Amanita Charm
  flex_slots:
  - Rod of Asclepius
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Soul Gem, Genji''s Guard, Shield of
    the Phoenix, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, The Reaper,
    Runeforged Hammer, Spear of Desolation, Spear of the Magus, Shield Splitter, Berserker''s
    Shield, Lifebinder, Obsidian Shard, Helm of Radiance, Eye of the Storm, Yogi''s
    Necklace, Sphere of Negation, Shifter''s Shield, Hydra''s Lament, Erosion, Heartseeker,
    Phoenix Feather, Eye of Providence, Chandra''s Grace, Draconic Scale, Avenging
    Blade, Blood-Bound Book, Jade Scepter, Wish-Granting Pearl, Stone of Binding,
    Doom Orb, Glorious Pridwen, Midgardian Mail, Titan''s Bane, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.16
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.42
    Hide of the Nemean Lion:
      total: 0.6
      efficiency: 0.52
      win: 0.8
      pick: 0.25
      fit: 0.3
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.68
      pick: 0.39
      fit: 0.31
    Rod of Asclepius:
      total: 0.59
      efficiency: 0.57
      win: 0.62
      pick: 0.36
      fit: 0.62
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Hide of the Nemean Lion
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hide of the Nemean Lion
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Genji''s Guard, Amanita Charm, Gluttonous Grimoire,
    Stone of Binding, Spear of Desolation, Spear of the Magus, Avenging Blade, Kinetic
    Cuirass, Screeching Gargoyle, Soul Gem, Obsidian Shard, Void Shield, Heartseeker,
    Void Stone, Shield Splitter, Runeforged Hammer, Helm of Radiance, Berserker''s
    Shield, Doom Orb, Titan''s Bane, The Crusher, The World Stone, Eye of the Storm,
    Shifter''s Shield, Hydra''s Lament, Dreamer''s Idol, Erosion, The Reaper, Eye
    of Providence, Shield of the Phoenix, Draconic Scale, Magi''s Cloak, Jade Scepter,
    Wish-Granting Pearl, Mantle Of Discord, Midgardian Mail, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.13
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.11
      fit: 0.21
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.49
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.14
    Hide of the Nemean Lion:
      total: 0.59
      efficiency: 0.52
      win: 0.8
      pick: 0.25
      fit: 0.25
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.68
      pick: 0.39
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Hide of the Nemean Lion
  - Rod of Tahuti
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
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Genji''s Guard, Gluttonous Grimoire,
    Nimble Ring, Amanita Charm, Soul Gem, Kinetic Cuirass, Golden Blade, Riptalon,
    Spear of the Magus, Spear of Desolation, Silverbranch Bow, Helm of Radiance, Runeforged
    Hammer, Tyrfing, Shield Splitter, Obsidian Shard, Lernaean Bow, Pharaoh''s Curse,
    Toxic Blade, Shogun''s Ofuda, The Reaper, Shifter''s Shield, Hydra''s Lament,
    Stone of Binding, Erosion, Tekko-Kagi, Bragi''s Harp, Shield of the Phoenix, Eye
    of Providence, Eye of the Storm, Bracer of The Abyss, Heartseeker, Draconic Scale,
    Magi''s Cloak, Screeching Gargoyle, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.33
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.52
      win: 0.8
      pick: 0.25
      fit: 0.2
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.68
      pick: 0.39
      fit: 0.21
  community_ordered:
  - Hide of the Nemean Lion
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Chronos' Pendant
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Amanita Charm, Spear of Desolation, Kinetic Cuirass, Soul Gem, Shield of the Phoenix,
    Hydra''s Lament, Screeching Gargoyle, Gluttonous Grimoire, Berserker''s Shield,
    Shield Splitter, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Shifter''s
    Shield, Prophetic Cloak, Erosion, Obsidian Shard, Eye of Providence, Stone of
    Binding, Draconic Scale, Gladiator''s Shield, Eye of the Storm, Arondight, Gem
    of Focus, Magi''s Cloak, Heartseeker, Eye of Erebus, Mantle Of Discord, Midgardian
    Mail, Pendulum Blade, Glorious Pridwen, Jade Scepter, Chandra''s Grace, Freya''s
    Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.11
      fit: 0.43
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.37
      fit: 0.37
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.51
    Hide of the Nemean Lion:
      total: 0.59
      efficiency: 0.52
      win: 0.8
      pick: 0.25
      fit: 0.26
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.68
      pick: 0.39
      fit: 0.22
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Chronos' Pendant
  - Hide of the Nemean Lion
  - Rod of Tahuti
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Freya''s
    Tears, Gluttonous Grimoire, Genji''s Guard, Shield Splitter, Shifter''s Shield,
    Spear of Desolation, Runeforged Hammer, Spear of the Magus, Helm of Radiance,
    Soul Gem, Berserker''s Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye
    of Providence, Hydra''s Lament, Draconic Scale, Heartseeker, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb, Screeching
    Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of Darkness, Midgardian
    Mail, Titan''s Bane, Death Metal, The Crusher, The World Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.11
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.44
      efficiency: 0.61
      win: 0.36
      pick: 0.14
      fit: 0.4
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.68
      pick: 0.39
      fit: 0.3
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
