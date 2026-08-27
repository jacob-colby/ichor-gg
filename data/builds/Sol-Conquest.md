---
type: smite-build
god: Sol
mode: Conquest
builds:
- source: community
  aspect: Aspect of Conflagration
  aspect_pick_rate: 0.5
  aspect_win_rate: 0.66
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.2
    win_rate: 0.68
    alternates:
    - name: Book of Thoth
      pick_rate: 0.18
      win_rate: 0.65
    - name: Tyrfing
      pick_rate: 0.15
      win_rate: 0.43
  - name: Book of Thoth
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Gem of Focus
      pick_rate: 0.09
      win_rate: 0.75
    - name: Odysseus' Bow
      pick_rate: 0.07
      win_rate: 0.29
  - name: Riptalon
    pick_rate: 0.12
    win_rate: 0.55
    alternates:
    - name: Soul Gem
      pick_rate: 0.12
      win_rate: 0.55
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 1.0
  - name: Rod of Tahuti
    pick_rate: 0.29
    win_rate: 0.75
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.06
      win_rate: 0.4
    - name: The Executioner
      pick_rate: 0.06
      win_rate: 0.2
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.69
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.67
    - name: Dominance
      pick_rate: 0.05
      win_rate: 0.25
  - name: Deathbringer
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 1.0
    - name: Soul Gem
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.17
    win_rate: 0.69
  - name: Archmage's Gem
    pick_rate: 0.13
    win_rate: 0.75
  - name: Death's Embrace
    pick_rate: 0.12
    win_rate: 0.36
  source_url: https://smitebrain.com/gods/sol/
  last_verified: '2026-08-27'
  god_win_rate: 0.5638297872340425
  god_matches_won: 53
  god_matches_played: 94
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
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Gem of Focus
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Reaver, Nimble Ring, Gem of Focus, Gluttonous Grimoire, Spear of
    the Magus, Bracer of The Abyss, Doom Orb, The World Stone, Chronos'' Pendant,
    Dreamer''s Idol, Blood-Bound Book, Ancient Signet, Bancroft''s Talon, The Cosmic
    Horror, Typhon’s Heart, Rod of Asclepius, Polynomicon, Totem of Death, Jade Scepter,
    Divine Ruin, Bragi''s Harp, Helm of Radiance, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.66
    Gem of Focus:
      total: 0.57
      efficiency: 0.5
      win: 0.75
      pick: 0.12
      fit: 0.36
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.68
      pick: 0.2
      fit: 0.58
    Soul Reaver:
      total: 0.66
      efficiency: 0.4
      win: 1.0
      pick: 0.08
      fit: 0.44
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.75
      pick: 0.48
      fit: 0.46
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.69
      pick: 0.39
      fit: 0.56
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Doom Orb
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Reaver, Gem of Focus, Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Doom Orb, Ancient Signet, The World Stone, Bracer of The Abyss, Death Metal,
    Chronos'' Pendant, Bancroft''s Talon, Blood-Bound Book, Dreamer''s Idol, Polynomicon,
    Rod of Asclepius, The Cosmic Horror, Typhon’s Heart, Totem of Death, Jade Scepter,
    Divine Ruin, Triton''s Conch, Wish-Granting Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.68
      pick: 0.2
      fit: 0.45
    Doom Orb:
      total: 0.5
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.42
    Soul Reaver:
      total: 0.66
      efficiency: 0.4
      win: 1.0
      pick: 0.08
      fit: 0.48
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.75
      pick: 0.48
      fit: 0.42
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.69
      pick: 0.39
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Gem of Focus
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Gem of Focus
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Reaver, Gem of Focus, Nimble Ring, Gluttonous Grimoire, Spear of the
    Magus, Bragi''s Harp, Doom Orb, The World Stone, Chronos'' Pendant, Bracer of
    The Abyss, Dreamer''s Idol, Death Metal, Ancient Signet, Blood-Bound Book, The
    Cosmic Horror, Bancroft''s Talon, Rod of Asclepius, Totem of Death, Typhon’s Heart,
    Polynomicon, Jade Scepter, Divine Ruin, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.44
    Gem of Focus:
      total: 0.57
      efficiency: 0.5
      win: 0.75
      pick: 0.12
      fit: 0.32
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.68
      pick: 0.2
      fit: 0.56
    Soul Reaver:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.08
      fit: 0.36
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.75
      pick: 0.48
      fit: 0.4
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.69
      pick: 0.39
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Nimble Ring
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Nimble Ring, Rod of Asclepius, Shield
    of the Phoenix, Kinetic Cuirass, Blood-Bound Book, Ethereal Staff, Freya''s Tears,
    Genji''s Guard, Breastplate of Valor, Bancroft''s Talon, Spear of the Magus, Shifter''s
    Shield, Lifebinder, Yogi''s Necklace, Helm of Radiance, Sphere of Negation, Phoenix
    Feather, Chandra''s Grace, Erosion, Eye of Providence, Jade Scepter, Bracer of
    The Abyss, Draconic Scale.'
  slot_scores:
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.68
      pick: 0.2
      fit: 0.36
    Soul Reaver:
      total: 0.64
      efficiency: 0.4
      win: 1.0
      pick: 0.08
      fit: 0.35
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.75
      pick: 0.48
      fit: 0.28
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.69
      pick: 0.39
      fit: 0.38
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.55
      pick: 0.19
      fit: 0.83
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Gem of Focus
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Gem of Focus
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Soul Reaver, Gem of Focus, Gluttonous Grimoire, Nimble Ring, Spear
    of the Magus, Doom Orb, The World Stone, Dreamer''s Idol, Bracer of The Abyss,
    The Cosmic Horror, Chronos'' Pendant, Blood-Bound Book, Ancient Signet, Bancroft''s
    Talon, Rod of Asclepius, Typhon’s Heart, Polynomicon, Totem of Death, Jade Scepter,
    Divine Ruin, Screeching Gargoyle, Helm of Radiance, Bragi''s Harp, Ethereal Staff.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.53
    Gem of Focus:
      total: 0.56
      efficiency: 0.5
      win: 0.75
      pick: 0.12
      fit: 0.29
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.68
      pick: 0.2
      fit: 0.66
    Soul Reaver:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.08
      fit: 0.39
    Rod of Tahuti:
      total: 0.75
      efficiency: 0.86
      win: 0.75
      pick: 0.48
      fit: 0.56
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.69
      pick: 0.39
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
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
    this god: Soul Reaver, Gem of Focus, Nimble Ring, Gluttonous Grimoire, Spear of
    the Magus, Bragi''s Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, The
    World Stone, Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Death Metal, Bancroft''s
    Talon, The Cosmic Horror, Rod of Asclepius, Typhon’s Heart, Polynomicon, Totem
    of Death, Jade Scepter, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.55
      pick: 0.0
      fit: 0.63
    Soul Reaver:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.08
      fit: 0.36
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.75
      pick: 0.48
      fit: 0.31
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.69
      pick: 0.39
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Gem of Focus
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Soul Gem
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Reaver, Gem of Focus, Nimble
    Ring, Gluttonous Grimoire, Chronos'' Pendant, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Doom Orb, The World Stone, Totem of Death, Ancient Signet,
    Dreamer''s Idol, Blood-Bound Book, Breastplate of Valor, Death Metal, Genji''s
    Guard, Bancroft''s Talon, The Cosmic Horror, Rod of Asclepius, Typhon’s Heart,
    Polynomicon, Staff of Myrddin, Eye of Erebus.'
  slot_scores:
    Gem of Focus:
      total: 0.58
      efficiency: 0.5
      win: 0.75
      pick: 0.12
      fit: 0.44
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.68
      pick: 0.2
      fit: 0.6
    Soul Reaver:
      total: 0.64
      efficiency: 0.4
      win: 1.0
      pick: 0.08
      fit: 0.3
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.75
      pick: 0.48
      fit: 0.26
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.69
      pick: 0.39
      fit: 0.36
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.55
      pick: 0.19
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Soul Reaver
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Gem of Focus, Nimble Ring,
    Gluttonous Grimoire, The Reaper, Spear of the Magus, Heartseeker, Hydra''s Lament,
    Bragi''s Harp, Tekko-Kagi, Lernaean Bow, Golden Blade, Titan''s Bane, Death Metal,
    The Crusher, Doom Orb, The World Stone, Chronos'' Pendant, Pendulum Blade, Dreamer''s
    Idol, Arondight, Blood-Bound Book, Avatar''s Parashu, Ancient Signet, Toxic Blade,
    Bracer of The Abyss, Tyrfing, Transcendence, Runeforged Hammer, Bancroft''s Talon,
    The Cosmic Horror, Avenging Blade, Barbed Carver, Qin''s Blade, Rod of Asclepius,
    Silverbranch Bow, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.59
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.68
      pick: 0.2
      fit: 0.49
    Soul Reaver:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.08
      fit: 0.4
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.75
      pick: 0.48
      fit: 0.39
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.69
      pick: 0.39
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Soul Reaver
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Gem of Focus, Nimble
    Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Tekko-Kagi, The
    Reaper, Lernaean Bow, Golden Blade, Heartseeker, Hydra''s Lament, Bracer of The
    Abyss, Doom Orb, Death Metal, Toxic Blade, The World Stone, Titan''s Bane, Chronos''
    Pendant, The Crusher, Dreamer''s Idol, Ancient Signet, Blood-Bound Book, Tyrfing,
    Bancroft''s Talon, Qin''s Blade, Arondight, Pendulum Blade, Avatar''s Parashu,
    Transcendence, The Cosmic Horror, Runeforged Hammer, Rod of Asclepius, Silverbranch
    Bow, Typhon’s Heart, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.48
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.68
      pick: 0.2
      fit: 0.48
    Soul Reaver:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.08
      fit: 0.41
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.75
      pick: 0.48
      fit: 0.38
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.69
      pick: 0.39
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
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
    Underrated for this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus,
    Bracer of The Abyss, Doom Orb, The World Stone, Chronos'' Pendant, Dreamer''s
    Idol, Blood-Bound Book, Ancient Signet, Bancroft''s Talon, Gem of Focus, The Cosmic
    Horror, Typhon’s Heart, Rod of Asclepius, Polynomicon, Totem of Death, Soul Reaver,
    Jade Scepter, Divine Ruin, Bragi''s Harp, Helm of Radiance, Ethereal Staff, Wish-Granting
    Pearl.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.68
      pick: 0.2
      fit: 0.58
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.75
      pick: 0.48
      fit: 0.46
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.69
      pick: 0.39
      fit: 0.56
  starter: *id001
---
