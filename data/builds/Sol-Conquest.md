---
type: smite-build
god: Sol
mode: Conquest
builds:
- source: community
  aspect: Aspect of Conflagration
  aspect_pick_rate: 0.56
  aspect_win_rate: 0.56
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.31
    win_rate: 1.0
    alternates:
    - name: Tyrfing
      pick_rate: 0.31
      win_rate: 0.2
    - name: Daybreak Gavel
      pick_rate: 0.13
      win_rate: 0.0
  - name: The World Stone
    pick_rate: 0.19
    win_rate: 1.0
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.19
      win_rate: 0.0
    - name: Vital Amplifier
      pick_rate: 0.13
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Cursed Sickle
      pick_rate: 0.06
      win_rate: 1.0
    - name: Vital Amplifier
      pick_rate: 0.06
      win_rate: 0.0
  - name: The Executioner
    pick_rate: 0.19
    win_rate: 0.0
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.25
      win_rate: 0.25
    - name: Void Shard
      pick_rate: 0.13
      win_rate: 1.0
  - name: Hunter's Bow
    pick_rate: 0.21
    win_rate: 0.33
    alternates:
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.0
    - name: Dreamer's Idol
      pick_rate: 0.14
      win_rate: 1.0
  - name: Riptalon
    pick_rate: 0.17
    win_rate: 0.0
    alternates:
    - name: Manchu Bow
      pick_rate: 0.17
      win_rate: 0.0
    - name: Hunter's Bow
      pick_rate: 0.17
      win_rate: 0.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.25
    win_rate: 0.0
  - name: Archmage's Gem
    pick_rate: 0.19
    win_rate: 1.0
  - name: Pendulum of the Ages
    pick_rate: 0.19
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/sol/
  last_verified: '2026-09-10'
  god_win_rate: 0.375
  god_matches_won: 6
  god_matches_played: 16
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Obsidian
    Shard, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, Blood-Bound Book, Ancient
    Signet, Bancroft''s Talon, Gem of Focus, The Cosmic Horror, Typhon’s Heart, Rod
    of Asclepius, Book of Thoth, Polynomicon, Totem of Death, Soul Reaver, Jade Scepter,
    Divine Ruin, Bragi''s Harp, Helm of Radiance, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.4
      efficiency: 0.51
      win: 0.42
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.75
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.58
    The World Stone:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.26
      fit: 0.46
    Rod of Tahuti:
      total: 0.84
      efficiency: 0.86
      win: 1.0
      pick: 0.39
      fit: 0.46
    Dreamer's Idol:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.3
      fit: 0.46
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Nimble
    Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Obsidian
    Shard, Doom Orb, Ancient Signet, Bracer of The Abyss, Death Metal, Chronos'' Pendant,
    Bancroft''s Talon, Blood-Bound Book, Gem of Focus, Book of Thoth, Polynomicon,
    Soul Reaver, Rod of Asclepius, The Cosmic Horror, Typhon’s Heart, Totem of Death,
    Jade Scepter, Divine Ruin, Triton''s Conch, Wish-Granting Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.73
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.45
    Doom Orb:
      total: 0.43
      efficiency: 0.53
      win: 0.42
      pick: 0.0
      fit: 0.42
    The World Stone:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.26
      fit: 0.42
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.39
      fit: 0.42
    Dreamer's Idol:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.3
      fit: 0.34
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Obsidian
    Shard, Bragi''s Harp, Doom Orb, Chronos'' Pendant, Bracer of The Abyss, Death
    Metal, Ancient Signet, Blood-Bound Book, Gem of Focus, The Cosmic Horror, Bancroft''s
    Talon, Rod of Asclepius, Book of Thoth, Totem of Death, Typhon’s Heart, Polynomicon,
    Soul Reaver, Jade Scepter, Divine Ruin, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.51
      win: 0.42
      pick: 0.0
      fit: 0.16
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.75
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.56
    The World Stone:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.26
      fit: 0.4
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.39
      fit: 0.4
    Dreamer's Idol:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.3
      fit: 0.4
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Nimble Ring
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Nimble Ring, Rod of Asclepius,
    Shield of the Phoenix, Kinetic Cuirass, Blood-Bound Book, Ethereal Staff, Freya''s
    Tears, Genji''s Guard, Breastplate of Valor, Bancroft''s Talon, Spear of the Magus,
    Shifter''s Shield, Lifebinder, Obsidian Shard, Yogi''s Necklace, Helm of Radiance,
    Sphere of Negation, Phoenix Feather, Chandra''s Grace, Erosion, Eye of Providence,
    Jade Scepter, Bracer of The Abyss, Draconic Scale.'
  slot_scores:
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.72
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.36
    The World Stone:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.26
      fit: 0.28
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 1.0
      pick: 0.39
      fit: 0.28
    Dreamer's Idol:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.3
      fit: 0.28
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Nimble Ring, Spear of the Magus,
    Obsidian Shard, Doom Orb, Bracer of The Abyss, The Cosmic Horror, Chronos'' Pendant,
    Blood-Bound Book, Ancient Signet, Bancroft''s Talon, Gem of Focus, Rod of Asclepius,
    Book of Thoth, Typhon’s Heart, Polynomicon, Totem of Death, Soul Reaver, Jade
    Scepter, Divine Ruin, Screeching Gargoyle, Helm of Radiance, Bragi''s Harp, Ethereal
    Staff.'
  slot_scores:
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.77
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.66
    Spear of the Magus:
      total: 0.48
      efficiency: 0.6
      win: 0.42
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 0.26
      fit: 0.56
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 0.39
      fit: 0.56
    Dreamer's Idol:
      total: 0.73
      efficiency: 0.51
      win: 1.0
      pick: 0.3
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - The World Stone
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Obsidian
    Shard, Bragi''s Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, Ancient
    Signet, Blood-Bound Book, Death Metal, Bancroft''s Talon, Gem of Focus, The Cosmic
    Horror, Rod of Asclepius, Book of Thoth, Typhon’s Heart, Polynomicon, Soul Reaver,
    Totem of Death, Jade Scepter, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.52
      win: 0.42
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.44
      efficiency: 0.44
      win: 0.42
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.73
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.39
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 1.0
      pick: 0.39
      fit: 0.31
    The World Stone:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.26
      fit: 0.31
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - The World Stone
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Nimble Ring, Gluttonous
    Grimoire, Chronos'' Pendant, Spear of the Magus, Obsidian Shard, Gem of Focus,
    Bragi''s Harp, Bracer of The Abyss, Doom Orb, Totem of Death, Ancient Signet,
    Blood-Bound Book, Breastplate of Valor, Death Metal, Genji''s Guard, Bancroft''s
    Talon, The Cosmic Horror, Rod of Asclepius, Book of Thoth, Typhon’s Heart, Polynomicon,
    Staff of Myrddin, Soul Reaver, Eye of Erebus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.44
      efficiency: 0.55
      win: 0.42
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.76
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.6
    The World Stone:
      total: 0.68
      efficiency: 0.52
      win: 1.0
      pick: 0.26
      fit: 0.26
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 1.0
      pick: 0.39
      fit: 0.26
    Dreamer's Idol:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.3
      fit: 0.26
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.42
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Jotunn's Revenge
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Nimble Ring,
    Gluttonous Grimoire, The Reaper, Spear of the Magus, Heartseeker, Hydra''s Lament,
    Obsidian Shard, Bragi''s Harp, Tekko-Kagi, Silverbranch Bow, Lernaean Bow, Golden
    Blade, Titan''s Bane, Death Metal, The Crusher, Doom Orb, Chronos'' Pendant, Pendulum
    Blade, Arondight, Dominance, Blood-Bound Book, Avatar''s Parashu, Ancient Signet,
    Toxic Blade, Bracer of The Abyss, Transcendence, Runeforged Hammer, Bancroft''s
    Talon, Gem of Focus, The Cosmic Horror, Avenging Blade, Barbed Carver, Qin''s
    Blade, Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.59
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.49
    The World Stone:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.26
      fit: 0.39
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.39
      fit: 0.39
    Dreamer's Idol:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.3
      fit: 0.39
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Jotunn's Revenge
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Nimble Ring, Soul
    Gem, Gluttonous Grimoire, Silverbranch Bow, Spear of the Magus, Bragi''s Harp,
    Obsidian Shard, Tekko-Kagi, The Reaper, Lernaean Bow, Golden Blade, Heartseeker,
    Hydra''s Lament, Bracer of The Abyss, Doom Orb, Death Metal, Toxic Blade, Titan''s
    Bane, Chronos'' Pendant, Dominance, The Crusher, Ancient Signet, Blood-Bound Book,
    Bancroft''s Talon, Qin''s Blade, Arondight, Gem of Focus, Pendulum Blade, Avatar''s
    Parashu, Transcendence, The Cosmic Horror, Runeforged Hammer, Rod of Asclepius,
    Book of Thoth, Typhon’s Heart.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.48
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.48
    The World Stone:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.26
      fit: 0.38
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.39
      fit: 0.38
    Dreamer's Idol:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.3
      fit: 0.38
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of
    the Magus, Obsidian Shard, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, Blood-Bound
    Book, Ancient Signet, Bancroft''s Talon, Gem of Focus, The Cosmic Horror, Typhon’s
    Heart, Rod of Asclepius, Book of Thoth, Polynomicon, Totem of Death, Soul Reaver,
    Jade Scepter, Divine Ruin, Bragi''s Harp, Helm of Radiance, Ethereal Staff, Wish-Granting
    Pearl.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.42
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.75
      efficiency: 0.57
      win: 1.0
      pick: 0.31
      fit: 0.58
    Rod of Tahuti:
      total: 0.84
      efficiency: 0.86
      win: 1.0
      pick: 0.39
      fit: 0.46
    Spear of the Magus:
      total: 0.47
      efficiency: 0.6
      win: 0.42
      pick: 0.0
      fit: 0.46
    Obsidian Shard:
      total: 0.46
      efficiency: 0.54
      win: 0.42
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
