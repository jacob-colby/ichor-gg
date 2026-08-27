---
type: smite-build
god: Princess Bari
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.63
    win_rate: 0.8
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.13
      win_rate: 0.25
    - name: Chronos' Pendant
      pick_rate: 0.09
      win_rate: 0.67
  - name: Doom Orb
    pick_rate: 0.22
    win_rate: 1.0
    alternates:
    - name: The World Stone
      pick_rate: 0.19
      win_rate: 0.5
    - name: Spear of Desolation
      pick_rate: 0.19
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.38
    win_rate: 0.83
    alternates:
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.0
    - name: Gem of Focus
      pick_rate: 0.09
      win_rate: 1.0
  - name: Obsidian Shard
    pick_rate: 0.39
    win_rate: 0.82
    alternates:
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.0
    - name: Blinking Abyss
      pick_rate: 0.11
      win_rate: 0.67
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.0
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 1.0
    - name: Soul Reaver
      pick_rate: 0.09
      win_rate: 0.5
  - name: Magi's Cloak
    pick_rate: 0.17
    win_rate: 1.0
    alternates:
    - name: Dreamer's Idol
      pick_rate: 0.17
      win_rate: 0.5
    - name: Chronos' Pendant
      pick_rate: 0.08
      win_rate: 0.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.22
    win_rate: 0.86
  - name: Conduit Gem
    pick_rate: 0.22
    win_rate: 0.71
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.17
  source_url: https://smitebrain.com/gods/princess-bari/
  last_verified: '2026-08-27'
  god_win_rate: 0.65625
  god_matches_won: 21
  god_matches_played: 32
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Nimble Ring
  - Gem of Focus
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Nimble Ring
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gem of Focus, Nimble Ring, Soul Gem, Riptalon, Tyrfing, Silverbranch
    Bow, Gluttonous Grimoire, Golden Blade, Spear of the Magus, Bragi''s Harp, Lernaean
    Bow, Tekko-Kagi, Toxic Blade, Bracer of The Abyss, Hydra''s Lament, Qin''s Blade,
    Dominance, Death Metal, Blood-Bound Book, Ancient Signet, Titan''s Bane, The Crusher,
    Bancroft''s Talon, Sun Beam Bow, Arondight, Pendulum Blade, The Cosmic Horror,
    Jotunn''s Revenge, Transcendence, Typhon’s Heart, Dagger of Frenzy, Rod of Asclepius,
    Book of Thoth, The Reaper.'
  slot_scores:
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
    Gem of Focus:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.14
      fit: 0.31
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.8
      pick: 0.63
      fit: 0.47
    Doom Orb:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.3
      fit: 0.36
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.83
      pick: 0.59
      fit: 0.36
    Obsidian Shard:
      total: 0.66
      efficiency: 0.54
      win: 0.82
      pick: 0.65
      fit: 0.46
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Hydra's Lament
  - Gem of Focus
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Hydra's Lament
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gem
    of Focus, Nimble Ring, Soul Gem, Tyrfing, Gluttonous Grimoire, Riptalon, Hydra''s
    Lament, Spear of the Magus, Bragi''s Harp, Silverbranch Bow, Lernaean Bow, Golden
    Blade, Tekko-Kagi, Ancient Signet, Dominance, Bracer of The Abyss, Death Metal,
    Bancroft''s Talon, Titan''s Bane, Toxic Blade, The Crusher, Blood-Bound Book,
    Transcendence, Jotunn''s Revenge, Arondight, Book of Thoth, Qin''s Blade, Polynomicon,
    Pendulum Blade, Runeforged Hammer, Avatar''s Parashu, Rod of Asclepius, The Reaper.'
  slot_scores:
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.49
    Gem of Focus:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.14
      fit: 0.31
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.8
      pick: 0.63
      fit: 0.45
    Doom Orb:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.3
      fit: 0.42
    Rod of Tahuti:
      total: 0.77
      efficiency: 0.86
      win: 0.83
      pick: 0.59
      fit: 0.42
    Obsidian Shard:
      total: 0.66
      efficiency: 0.54
      win: 0.82
      pick: 0.65
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Gem of Focus
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Nimble Ring
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gem of Focus, Soul Gem, Nimble Ring, Riptalon, Gluttonous Grimoire, Silverbranch
    Bow, Spear of the Magus, Tyrfing, Tekko-Kagi, Hydra''s Lament, Lernaean Bow, Toxic
    Blade, Golden Blade, Bragi''s Harp, Titan''s Bane, The Crusher, Bracer of The
    Abyss, Pendulum Blade, Jotunn''s Revenge, Death Metal, Dominance, Ancient Signet,
    Arondight, Blood-Bound Book, Qin''s Blade, Avatar''s Parashu, The Cosmic Horror,
    Bancroft''s Talon, Transcendence, Runeforged Hammer, Sun Beam Bow, Rod of Asclepius,
    Book of Thoth, The Reaper.'
  slot_scores:
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Gem of Focus:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.14
      fit: 0.32
    Spear of Desolation:
      total: 0.68
      efficiency: 0.57
      win: 0.8
      pick: 0.63
      fit: 0.56
    Doom Orb:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.3
      fit: 0.4
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.83
      pick: 0.59
      fit: 0.4
    Obsidian Shard:
      total: 0.67
      efficiency: 0.54
      win: 0.82
      pick: 0.65
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Magi's Cloak
  - Gem of Focus
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Riptalon, Berserker''s Shield, Gluttonous Grimoire,
    Rod of Asclepius, Nimble Ring, Shield of the Phoenix, Golden Blade, Kinetic Cuirass,
    Blood-Bound Book, Ethereal Staff, Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Bancroft''s Talon, Tyrfing, Silverbranch Bow, Toxic Blade, Runeforged
    Hammer, Spear of the Magus, Yogi''s Necklace, Lifebinder, Shifter''s Shield, Helm
    of Radiance, Pharaoh''s Curse, Shield Splitter, Sphere of Negation, Lernaean Bow,
    Shogun''s Ofuda, Chandra''s Grace, Phoenix Feather, Eye of the Storm, Bragi''s
    Harp, Hydra''s Lament, Erosion, Eye of Providence, Jotunn''s Revenge, The Reaper.'
  slot_scores:
    Magi's Cloak:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.52
      fit: 0.21
    Gem of Focus:
      total: 0.66
      efficiency: 0.5
      win: 1.0
      pick: 0.14
      fit: 0.2
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.8
      pick: 0.63
      fit: 0.31
    Doom Orb:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.3
      fit: 0.24
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.83
      pick: 0.59
      fit: 0.24
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.82
      pick: 0.65
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Gem of Focus
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Gem of Focus
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gem of Focus, Soul Gem, Riptalon, Silverbranch Bow, Gluttonous Grimoire,
    Nimble Ring, Spear of the Magus, Tekko-Kagi, Tyrfing, Toxic Blade, Titan''s Bane,
    The Crusher, Lernaean Bow, Golden Blade, Bragi''s Harp, Bracer of The Abyss, Hydra''s
    Lament, Avenging Blade, Pendulum Blade, The Cosmic Horror, Avatar''s Parashu,
    Jotunn''s Revenge, Ancient Signet, Qin''s Blade, Blood-Bound Book, Death Metal,
    Dominance, Bancroft''s Talon, The Executioner, Arondight, Sun Beam Bow, Oath-Sworn
    Spear, Transcendence, The Reaper.'
  slot_scores:
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Gem of Focus:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.14
      fit: 0.25
    Spear of Desolation:
      total: 0.68
      efficiency: 0.57
      win: 0.8
      pick: 0.63
      fit: 0.57
    Doom Orb:
      total: 0.72
      efficiency: 0.53
      win: 1.0
      pick: 0.3
      fit: 0.49
    Rod of Tahuti:
      total: 0.78
      efficiency: 0.86
      win: 0.83
      pick: 0.59
      fit: 0.49
    Obsidian Shard:
      total: 0.68
      efficiency: 0.54
      win: 0.82
      pick: 0.65
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Gem of Focus
  - Doom Orb
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Riptalon
  - Tyrfing
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gem of Focus, Nimble Ring, Soul Gem, Riptalon, Gluttonous Grimoire,
    Tyrfing, Silverbranch Bow, Spear of the Magus, Lernaean Bow, Bragi''s Harp, Tekko-Kagi,
    Golden Blade, Bracer of The Abyss, Hydra''s Lament, Toxic Blade, Dominance, Ancient
    Signet, Blood-Bound Book, Death Metal, Qin''s Blade, Titan''s Bane, The Crusher,
    Bancroft''s Talon, Arondight, Sun Beam Bow, Transcendence, Rod of Asclepius, Book
    of Thoth, Runeforged Hammer, Pendulum Blade, The Cosmic Horror, Typhon’s Heart,
    Jotunn''s Revenge, The Reaper.'
  slot_scores:
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.64
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Gem of Focus:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.14
      fit: 0.25
    Doom Orb:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.3
      fit: 0.29
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.75
      efficiency: 0.86
      win: 0.83
      pick: 0.59
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Gem of Focus
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Soul Gem
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gem of Focus, Soul Gem, Nimble Ring,
    Riptalon, Hydra''s Lament, Silverbranch Bow, Tyrfing, Gluttonous Grimoire, Spear
    of the Magus, Golden Blade, Lernaean Bow, Arondight, Tekko-Kagi, Toxic Blade,
    Pendulum Blade, Bragi''s Harp, Jotunn''s Revenge, Bracer of The Abyss, Qin''s
    Blade, Totem of Death, Dominance, Ancient Signet, Titan''s Bane, Blood-Bound Book,
    The Crusher, Breastplate of Valor, Genji''s Guard, Death Metal, Sun Beam Bow,
    Bancroft''s Talon, Transcendence, Runeforged Hammer, Dagger of Frenzy, The Reaper.'
  slot_scores:
    Gem of Focus:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.14
      fit: 0.45
    Spear of Desolation:
      total: 0.68
      efficiency: 0.57
      win: 0.8
      pick: 0.63
      fit: 0.59
    Doom Orb:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.3
      fit: 0.24
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.83
      pick: 0.59
      fit: 0.24
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.82
      pick: 0.65
      fit: 0.34
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Nimble Ring
  - Gem of Focus
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Nimble Ring
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Gem of Focus, Soul Gem, Nimble Ring, Gluttonous
    Grimoire, Tyrfing, Riptalon, Spear of the Magus, Silverbranch Bow, Hydra''s Lament,
    Golden Blade, Tekko-Kagi, Bragi''s Harp, Lernaean Bow, Titan''s Bane, The Crusher,
    Death Metal, Toxic Blade, Pendulum Blade, Arondight, Jotunn''s Revenge, Dominance,
    Avatar''s Parashu, Blood-Bound Book, Ancient Signet, Bracer of The Abyss, Transcendence,
    Runeforged Hammer, Bancroft''s Talon, Qin''s Blade, The Cosmic Horror, Avenging
    Blade, Barbed Carver, Rod of Asclepius, The Reaper.'
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
    Gem of Focus:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.14
      fit: 0.3
    Spear of Desolation:
      total: 0.67
      efficiency: 0.57
      win: 0.8
      pick: 0.63
      fit: 0.49
    Doom Orb:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.3
      fit: 0.39
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.83
      pick: 0.59
      fit: 0.39
    Obsidian Shard:
      total: 0.67
      efficiency: 0.54
      win: 0.82
      pick: 0.65
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Nimble Ring
  - Gem of Focus
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Nimble Ring
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gem of Focus, Nimble Ring, Soul Gem,
    Riptalon, Tyrfing, Gluttonous Grimoire, Silverbranch Bow, Spear of the Magus,
    Bragi''s Harp, Golden Blade, Tekko-Kagi, Lernaean Bow, Hydra''s Lament, Bracer
    of The Abyss, Toxic Blade, Death Metal, Titan''s Bane, Dominance, The Crusher,
    Ancient Signet, Blood-Bound Book, Qin''s Blade, Bancroft''s Talon, Arondight,
    Pendulum Blade, Jotunn''s Revenge, Avatar''s Parashu, Transcendence, The Cosmic
    Horror, Runeforged Hammer, Sun Beam Bow, Rod of Asclepius, Book of Thoth, The
    Reaper.'
  slot_scores:
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.52
    Gem of Focus:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.14
      fit: 0.3
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.8
      pick: 0.63
      fit: 0.48
    Doom Orb:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.3
      fit: 0.38
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.83
      pick: 0.59
      fit: 0.38
    Obsidian Shard:
      total: 0.66
      efficiency: 0.54
      win: 0.82
      pick: 0.65
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Spear of Desolation
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - Spear of Desolation
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Riptalon, Tyrfing,
    Silverbranch Bow, Gluttonous Grimoire, Golden Blade, Spear of the Magus, Bragi''s
    Harp, Lernaean Bow, Tekko-Kagi, The Reaper, Toxic Blade, Bracer of The Abyss,
    Hydra''s Lament, Qin''s Blade, Dominance, Death Metal, Blood-Bound Book, Ancient
    Signet, Titan''s Bane, The Crusher, Bancroft''s Talon, Sun Beam Bow, Gem of Focus,
    Arondight, Pendulum Blade, The Cosmic Horror, Transcendence, Typhon’s Heart, Dagger
    of Frenzy, Rod of Asclepius, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.72
      win: 0.25
      pick: 0.13
      fit: 0.43
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.8
      pick: 0.63
      fit: 0.47
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.83
      pick: 0.59
      fit: 0.36
  starter: *id001
---
