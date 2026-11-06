---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.67
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.21
    win_rate: 0.67
    alternates:
    - name: Circe's Hexstone
      pick_rate: 0.17
      win_rate: 0.43
    - name: Chandra's Grace
      pick_rate: 0.17
      win_rate: 0.29
  - name: Spear of Desolation
    pick_rate: 0.19
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.6
    - name: Spirit Robe
      pick_rate: 0.12
      win_rate: 1.0
  - name: Freya's Tears
    pick_rate: 0.31
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.25
  - name: Shell of Rebuke
    pick_rate: 0.26
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.67
  - name: Spectral Armor
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.4
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.67
  - name: Medal of Defense
    pick_rate: 0.12
    win_rate: 1.0
    alternates:
    - name: Oracle Staff
      pick_rate: 0.08
      win_rate: 0.5
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.43
    win_rate: 0.67
  - name: Bluestone Pendant
    pick_rate: 0.26
    win_rate: 0.45
  - name: Heroism
    pick_rate: 0.12
    win_rate: 0.8
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-11-06'
  god_win_rate: 0.5952380952380952
  god_matches_won: 25
  god_matches_played: 42
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Spirit Robe
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  flex_slots:
  - Genji's Guard
  - Spear of Desolation
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Soul Gem, Gluttonous
    Grimoire, Shield of the Phoenix, Erosion, Eye of Providence, Oni Hunter''s Garb,
    Shifter''s Shield, Helm of Darkness, Lotus Sickle, Helm of Radiance, Screeching
    Gargoyle, Stone of Binding, Midgardian Mail, Blood-Bound Book, Magi''s Cloak,
    Mantle Of Discord, Leviathan''s Hide, Gladiator''s Shield, Hide of the Nemean
    Lion, Prophetic Cloak, Chronos'' Pendant, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.6
      pick: 0.19
      fit: 0.36
    Spirit Robe:
      total: 0.64
      efficiency: 0.35
      win: 1.0
      pick: 0.16
      fit: 0.41
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.48
      fit: 0.56
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.33
    Draconic Scale:
      total: 0.73
      efficiency: 0.53
      win: 1.0
      pick: 0.25
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Spirit Robe
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Spirit Robe
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Rod of Tahuti, Kinetic
    Cuirass, Blood-Bound Book, Gluttonous Grimoire, Phoenix Feather, Ethereal Staff,
    Yogi''s Necklace, Oni Hunter''s Garb, Bancroft''s Talon, Erosion, Eye of Providence,
    Rod of Asclepius, Lotus Sickle, Shifter''s Shield, Soul Locket, Regrowth Striders,
    Glorious Pridwen, Midgardian Mail, Helm of Radiance, Screeching Gargoyle, Helm
    of Darkness.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.6
      pick: 0.19
      fit: 0.33
    Spirit Robe:
      total: 0.68
      efficiency: 0.35
      win: 1.0
      pick: 0.16
      fit: 0.64
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.62
      pick: 0.48
      fit: 0.5
    Draconic Scale:
      total: 0.73
      efficiency: 0.53
      win: 1.0
      pick: 0.25
      fit: 0.55
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Genji's Guard
  - Spirit Robe
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spirit Robe
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Genji's Guard
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Soul Gem, Gluttonous Grimoire, Amanita Charm, Kinetic
    Cuirass, Screeching Gargoyle, Stone of Binding, Void Stone, Void Shield, Obsidian
    Shard, Shield of the Phoenix, Spear of the Magus, Dreamer''s Idol, Oni Hunter''s
    Garb, Lotus Sickle, Erosion, Eye of Providence, Helm of Radiance, Blood-Bound
    Book, Doom Orb, Shifter''s Shield, Helm of Darkness, Midgardian Mail, The World
    Stone, Leviathan''s Hide.'
  slot_scores:
    Spirit Robe:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.16
      fit: 0.3
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.19
      fit: 0.26
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.62
      pick: 0.48
      fit: 0.41
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.51
    Draconic Scale:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.25
      fit: 0.42
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.6
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Spirit Robe
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Spirit Robe
  - Bragi's Harp
  - Freya's Tears
  - Draconic Scale
  - Eros' Bow
  flex_slots:
  - Bragi's Harp
  - Eros' Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Nimble Ring, Shield of the Phoenix, Oni Hunter''s Garb, Lotus Sickle,
    Blood-Bound Book, Bragi''s Harp, Helm of Radiance, Screeching Gargoyle, Erosion,
    Eros'' Bow, Eye of Providence, Ancient Signet, Midgardian Mail, Shifter''s Shield,
    Helm of Darkness, Stone of Binding, Death Metal, Leviathan''s Hide, Bracer of
    The Abyss, Chronos'' Pendant.'
  slot_scores:
    Nimble Ring:
      total: 0.52
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.32
    Spirit Robe:
      total: 0.62
      efficiency: 0.35
      win: 1.0
      pick: 0.16
      fit: 0.24
    Bragi's Harp:
      total: 0.5
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.48
      fit: 0.33
    Draconic Scale:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.25
      fit: 0.34
    Eros' Bow:
      total: 0.5
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Spirit Robe
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Spirit Robe
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Shield of the Phoenix, Lotus Sickle, Screeching Gargoyle,
    Gluttonous Grimoire, Chronos'' Pendant, Gladiator''s Shield, Oni Hunter''s Garb,
    Prophetic Cloak, Erosion, Eye of Providence, Helm of Radiance, Blood-Bound Book,
    Shifter''s Shield, Gem of Focus, Heartwood Charm, Helm of Darkness, Midgardian
    Mail, Stone of Binding, Leviathan''s Hide, Regrowth Striders.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.52
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.6
      pick: 0.19
      fit: 0.45
    Spirit Robe:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.16
      fit: 0.3
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.62
      pick: 0.48
      fit: 0.6
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.42
    Draconic Scale:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.25
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Spirit Robe
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Spirit Robe
  - Draconic Scale
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Kinetic Cuirass, Soul Gem, Gluttonous Grimoire, Shield
    Splitter, The Reaper, Tyrfing, Runeforged Hammer, Hydra''s Lament, Shield of the
    Phoenix, Golden Blade, Oni Hunter''s Garb, The Crusher, Lotus Sickle, Death Metal,
    Heartseeker, Blood-Bound Book, Helm of Radiance, Erosion, Obsidian Shard, Screeching
    Gargoyle, Bragi''s Harp, Eye of Providence, Tekko-Kagi, Nimble Ring, Titan''s
    Bane, Shifter''s Shield, Midgardian Mail, Helm of Darkness, Arondight, Ancient
    Signet, Spear of the Magus, Stone of Binding, Leviathan''s Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.31
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.19
      fit: 0.22
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.48
      fit: 0.35
    Spirit Robe:
      total: 0.62
      efficiency: 0.35
      win: 1.0
      pick: 0.16
      fit: 0.26
    Draconic Scale:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.25
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spirit Robe
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Spirit Robe
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Jotunn''s Revenge, Gluttonous Grimoire, Kinetic Cuirass, Shield Splitter,
    Berserker''s Shield, Lotus Sickle, The Reaper, Shield of the Phoenix, Blood-Bound
    Book, Helm of Radiance, Runeforged Hammer, Hydra''s Lament, Obsidian Shard, Death
    Metal, Oni Hunter''s Garb, Helm of Darkness, Spear of the Magus, Ancient Signet,
    The Crusher, Chronos'' Pendant, Erosion, Screeching Gargoyle, Eye of Providence,
    Polynomicon, Heartseeker, Dreamer''s Idol, Shifter''s Shield, Midgardian Mail,
    Stone of Binding, Jade Scepter, Titan''s Bane, Leviathan''s Hide, Tyrfing, Magi''s
    Cloak.'
  slot_scores:
    Spirit Robe:
      total: 0.62
      efficiency: 0.35
      win: 1.0
      pick: 0.16
      fit: 0.27
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.19
      fit: 0.23
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.48
      fit: 0.37
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.4
    Draconic Scale:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.25
      fit: 0.38
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.6
      pick: 0.0
      fit: 0.3
  community_ordered:
  - Spirit Robe
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Soul Gem,
    Gluttonous Grimoire, Shield of the Phoenix, Erosion, Eye of Providence, Oni Hunter''s
    Garb, Shifter''s Shield, Helm of Darkness, Lotus Sickle, Helm of Radiance, Screeching
    Gargoyle, Stone of Binding, Midgardian Mail, Blood-Bound Book, Magi''s Cloak,
    Mantle Of Discord, Leviathan''s Hide, Gladiator''s Shield, Hide of the Nemean
    Lion, Prophetic Cloak, Chronos'' Pendant, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.4
      efficiency: 0.63
      win: 0.25
      pick: 0.16
      fit: 0.36
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.6
      pick: 0.19
      fit: 0.36
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.48
      fit: 0.56
    Draconic Scale:
      total: 0.73
      efficiency: 0.53
      win: 1.0
      pick: 0.25
      fit: 0.57
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
---
