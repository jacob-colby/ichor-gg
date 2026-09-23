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
    win_rate: 0.5
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.14
      win_rate: 0.6
    - name: Gem of Focus
      pick_rate: 0.03
      win_rate: 1.0
  - name: Chronos' Pendant
    pick_rate: 0.26
    win_rate: 0.33
    alternates:
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.4
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.5
  - name: Soul Gem
    pick_rate: 0.24
    win_rate: 0.38
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.67
    - name: The World Stone
      pick_rate: 0.15
      win_rate: 0.6
  - name: Rod of Tahuti
    pick_rate: 0.3
    win_rate: 0.4
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.15
      win_rate: 0.4
    - name: Dreamer's Idol
      pick_rate: 0.12
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.22
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 1.0
    - name: Evil Eye
      pick_rate: 0.11
      win_rate: 0.33
  - name: Evil Eye
    pick_rate: 0.11
    win_rate: 0.0
    alternates:
    - name: Killing Stone
      pick_rate: 0.11
      win_rate: 0.0
    - name: Spear of the Magus
      pick_rate: 0.11
      win_rate: 0.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.29
    win_rate: 0.7
  - name: Conduit Gem
    pick_rate: 0.29
    win_rate: 0.2
  - name: Bluestone Brooch
    pick_rate: 0.11
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/princess-bari/
  last_verified: '2026-09-23'
  god_win_rate: 0.5142857142857142
  god_matches_won: 18
  god_matches_played: 35
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Nimble Ring
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gem of Focus, Jotunn''s Revenge, Nimble Ring, Riptalon, Tyrfing, Silverbranch
    Bow, Gluttonous Grimoire, Golden Blade, Bragi''s Harp, Lernaean Bow, Tekko-Kagi,
    The Reaper, Toxic Blade, Bracer of The Abyss, Hydra''s Lament, Heartseeker, Qin''s
    Blade, Doom Orb, Dominance, Death Metal, Blood-Bound Book, Ancient Signet, Titan''s
    Bane, The Crusher, Bancroft''s Talon, Sun Beam Bow, Arondight, Pendulum Blade,
    The Cosmic Horror, Transcendence, Typhon’s Heart, Dagger of Frenzy, Rod of Asclepius,
    Book of Thoth.'
  slot_scores:
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.63
      fit: 0.47
    Gem of Focus:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.03
      fit: 0.31
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.23
      fit: 0.36
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.36
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.48
      fit: 0.46
  community_ordered:
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    of Focus, Jotunn''s Revenge, Nimble Ring, Tyrfing, Gluttonous Grimoire, Riptalon,
    Hydra''s Lament, Bragi''s Harp, Silverbranch Bow, Heartseeker, Lernaean Bow, The
    Reaper, Golden Blade, Tekko-Kagi, Doom Orb, Ancient Signet, Dominance, Bracer
    of The Abyss, Death Metal, Bancroft''s Talon, Titan''s Bane, Toxic Blade, The
    Crusher, Blood-Bound Book, Transcendence, Arondight, Book of Thoth, Qin''s Blade,
    Polynomicon, Pendulum Blade, Runeforged Hammer, Soul Reaver, Avatar''s Parashu,
    Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.4
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.63
      fit: 0.45
    Gem of Focus:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.03
      fit: 0.31
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.23
      fit: 0.42
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.42
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.67
      pick: 0.48
      fit: 0.44
  community_ordered:
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    god: Gem of Focus, Jotunn''s Revenge, Nimble Ring, Riptalon, Gluttonous Grimoire,
    Silverbranch Bow, Tyrfing, The Reaper, Tekko-Kagi, Heartseeker, Hydra''s Lament,
    Lernaean Bow, Toxic Blade, Golden Blade, Bragi''s Harp, Doom Orb, Titan''s Bane,
    The Crusher, Bracer of The Abyss, Pendulum Blade, Death Metal, Dominance, Ancient
    Signet, Arondight, Blood-Bound Book, Qin''s Blade, Avatar''s Parashu, The Cosmic
    Horror, Bancroft''s Talon, Transcendence, Runeforged Hammer, Sun Beam Bow, Rod
    of Asclepius, Book of Thoth.'
  slot_scores:
    Nimble Ring:
      total: 0.47
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.63
      fit: 0.56
    Gem of Focus:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.03
      fit: 0.32
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.23
      fit: 0.4
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.4
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.48
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Riptalon, Berserker''s Shield, Jotunn''s Revenge, Gluttonous
    Grimoire, Rod of Asclepius, Nimble Ring, The Reaper, Shield of the Phoenix, Golden
    Blade, Kinetic Cuirass, Blood-Bound Book, Ethereal Staff, Freya''s Tears, Genji''s
    Guard, Breastplate of Valor, Bancroft''s Talon, Tyrfing, Silverbranch Bow, Toxic
    Blade, Runeforged Hammer, Yogi''s Necklace, Lifebinder, Shifter''s Shield, Helm
    of Radiance, Pharaoh''s Curse, Shield Splitter, Sphere of Negation, Lernaean Bow,
    Shogun''s Ofuda, Chandra''s Grace, Phoenix Feather, Eye of the Storm, Bragi''s
    Harp, Hydra''s Lament, Erosion, Eye of Providence.'
  slot_scores:
    Nimble Ring:
      total: 0.46
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.37
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.63
      fit: 0.31
    Gem of Focus:
      total: 0.66
      efficiency: 0.5
      win: 1.0
      pick: 0.03
      fit: 0.2
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.24
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.48
      fit: 0.34
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Gem of Focus, Jotunn''s Revenge, Riptalon, Silverbranch Bow, Gluttonous
    Grimoire, Nimble Ring, The Reaper, Tekko-Kagi, Tyrfing, Toxic Blade, Heartseeker,
    Doom Orb, Titan''s Bane, The Crusher, Lernaean Bow, Golden Blade, Bragi''s Harp,
    Bracer of The Abyss, Hydra''s Lament, Avenging Blade, Pendulum Blade, The Cosmic
    Horror, Avatar''s Parashu, Ancient Signet, Qin''s Blade, Blood-Bound Book, Death
    Metal, Dominance, Bancroft''s Talon, The Executioner, Arondight, Sun Beam Bow,
    Oath-Sworn Spear, Transcendence.'
  slot_scores:
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.63
      fit: 0.57
    Gem of Focus:
      total: 0.66
      efficiency: 0.5
      win: 1.0
      pick: 0.03
      fit: 0.25
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.23
      fit: 0.49
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.49
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.67
      pick: 0.48
      fit: 0.59
  community_ordered:
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Gem of Focus
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Gem of Focus, Jotunn''s Revenge, Nimble Ring, Riptalon, Gluttonous Grimoire,
    Tyrfing, Silverbranch Bow, Lernaean Bow, Bragi''s Harp, Tekko-Kagi, Golden Blade,
    Bracer of The Abyss, The Reaper, Hydra''s Lament, Toxic Blade, Heartseeker, Doom
    Orb, Dominance, Ancient Signet, Blood-Bound Book, Death Metal, Qin''s Blade, Titan''s
    Bane, The Crusher, Bancroft''s Talon, Arondight, Sun Beam Bow, Transcendence,
    Rod of Asclepius, Book of Thoth, Runeforged Hammer, Pendulum Blade, The Cosmic
    Horror, Typhon’s Heart.'
  slot_scores:
    Tyrfing:
      total: 0.45
      efficiency: 0.48
      win: 0.4
      pick: 0.0
      fit: 0.64
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.49
    Gem of Focus:
      total: 0.66
      efficiency: 0.5
      win: 1.0
      pick: 0.03
      fit: 0.25
    Riptalon:
      total: 0.45
      efficiency: 0.51
      win: 0.4
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.29
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.48
      fit: 0.39
  community_ordered:
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Nimble Ring
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Jotunn's Revenge
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    + fit + win/pick). Underrated for this god: Gem of Focus, Jotunn''s Revenge, Nimble
    Ring, Riptalon, Hydra''s Lament, Silverbranch Bow, Tyrfing, Gluttonous Grimoire,
    Golden Blade, Lernaean Bow, Arondight, The Reaper, Tekko-Kagi, Toxic Blade, Pendulum
    Blade, Bragi''s Harp, Bracer of The Abyss, Heartseeker, Qin''s Blade, Totem of
    Death, Doom Orb, Dominance, Ancient Signet, Titan''s Bane, Blood-Bound Book, The
    Crusher, Breastplate of Valor, Genji''s Guard, Death Metal, Sun Beam Bow, Bancroft''s
    Talon, Transcendence, Runeforged Hammer, Dagger of Frenzy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.4
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.5
      pick: 0.63
      fit: 0.59
    Nimble Ring:
      total: 0.47
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.41
    Gem of Focus:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.03
      fit: 0.45
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.24
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.48
      fit: 0.34
  community_ordered:
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    win/pick). Underrated for this god: Gem of Focus, Jotunn''s Revenge, Nimble Ring,
    Gluttonous Grimoire, Tyrfing, The Reaper, Riptalon, Silverbranch Bow, Heartseeker,
    Hydra''s Lament, Golden Blade, Tekko-Kagi, Bragi''s Harp, Lernaean Bow, Titan''s
    Bane, The Crusher, Death Metal, Doom Orb, Toxic Blade, Pendulum Blade, Arondight,
    Dominance, Avatar''s Parashu, Blood-Bound Book, Ancient Signet, Bracer of The
    Abyss, Transcendence, Runeforged Hammer, Bancroft''s Talon, Qin''s Blade, The
    Cosmic Horror, Avenging Blade, Barbed Carver, Rod of Asclepius.'
  slot_scores:
    Nimble Ring:
      total: 0.47
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.63
      fit: 0.49
    Gem of Focus:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.03
      fit: 0.3
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.23
      fit: 0.39
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.39
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.48
      fit: 0.49
  community_ordered:
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Nimble Ring
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gem of Focus, Jotunn''s Revenge, Nimble
    Ring, Riptalon, Tyrfing, Gluttonous Grimoire, Silverbranch Bow, Bragi''s Harp,
    Golden Blade, Tekko-Kagi, The Reaper, Lernaean Bow, Heartseeker, Hydra''s Lament,
    Bracer of The Abyss, Toxic Blade, Doom Orb, Death Metal, Titan''s Bane, Dominance,
    The Crusher, Ancient Signet, Blood-Bound Book, Qin''s Blade, Bancroft''s Talon,
    Arondight, Pendulum Blade, Avatar''s Parashu, Transcendence, The Cosmic Horror,
    Runeforged Hammer, Sun Beam Bow, Rod of Asclepius, Book of Thoth.'
  slot_scores:
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.63
      fit: 0.48
    Gem of Focus:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.03
      fit: 0.3
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.23
      fit: 0.38
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.38
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.48
      fit: 0.48
  community_ordered:
  - Spear of Desolation
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Tyrfing
  - Nimble Ring
  - Rod of Tahuti
  - Silverbranch Bow
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
    Underrated for this god: Jotunn''s Revenge, Nimble Ring, Riptalon, Tyrfing, Silverbranch
    Bow, Gluttonous Grimoire, Golden Blade, Bragi''s Harp, Lernaean Bow, Tekko-Kagi,
    The Reaper, Toxic Blade, Bracer of The Abyss, Hydra''s Lament, Heartseeker, Qin''s
    Blade, Doom Orb, Dominance, Death Metal, Blood-Bound Book, Ancient Signet, Titan''s
    Bane, The Crusher, Bancroft''s Talon, Sun Beam Bow, Gem of Focus, Arondight, Pendulum
    Blade, The Cosmic Horror, Transcendence, Typhon’s Heart, Dagger of Frenzy, Rod
    of Asclepius, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.4
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.63
      fit: 0.47
    Tyrfing:
      total: 0.47
      efficiency: 0.48
      win: 0.4
      pick: 0.0
      fit: 0.79
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.36
    Silverbranch Bow:
      total: 0.47
      efficiency: 0.53
      win: 0.4
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
