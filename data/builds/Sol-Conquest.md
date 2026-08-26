---
type: smite-build
god: Sol
mode: Conquest
builds:
- source: community
  aspect: Aspect of Conflagration
  aspect_pick_rate: 0.63
  aspect_win_rate: 0.8
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.33
    win_rate: 0.88
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.25
      win_rate: 0.67
    - name: Tyrfing
      pick_rate: 0.13
      win_rate: 0.33
  - name: Doom Orb
    pick_rate: 0.17
    win_rate: 0.75
    alternates:
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 1.0
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.67
  - name: Spear of Desolation
    pick_rate: 0.17
    win_rate: 1.0
    alternates:
    - name: Soul Gem
      pick_rate: 0.17
      win_rate: 1.0
    - name: Riptalon
      pick_rate: 0.17
      win_rate: 0.25
  - name: Rod of Tahuti
    pick_rate: 0.43
    win_rate: 0.89
    alternates:
    - name: Spear of the Magus
      pick_rate: 0.1
      win_rate: 0.5
    - name: Avenging Blade
      pick_rate: 0.1
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.37
    win_rate: 0.71
    alternates:
    - name: Dominance
      pick_rate: 0.16
      win_rate: 0.33
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.5
  - name: Void Shard
    pick_rate: 0.07
    win_rate: 1.0
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 1.0
    - name: Soul Reaver
      pick_rate: 0.07
      win_rate: 0.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.25
    win_rate: 0.67
  - name: Pendulum of the Ages
    pick_rate: 0.17
    win_rate: 1.0
  - name: Conduit Gem
    pick_rate: 0.13
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/sol/
  last_verified: '2026-08-26'
  god_win_rate: 0.7083333333333334
  god_matches_won: 17
  god_matches_played: 24
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
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
    this god: Nimble Ring, Gluttonous Grimoire, Bracer of The Abyss, Chronos'' Pendant,
    Dreamer''s Idol, Blood-Bound Book, Ancient Signet, Bancroft''s Talon, Gem of Focus,
    The Cosmic Horror, Typhon’s Heart, Rod of Asclepius, Polynomicon, Totem of Death,
    Jade Scepter, Divine Ruin, Bragi''s Harp, Helm of Radiance, Ethereal Staff, Wish-Granting
    Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.63
      efficiency: 0.51
      win: 0.88
      pick: 0.33
      fit: 0.24
    Spear of Desolation:
      total: 0.75
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.58
    The World Stone:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.18
      fit: 0.46
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 0.89
      pick: 0.72
      fit: 0.46
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.71
      pick: 0.8
      fit: 0.56
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.8
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Obsidian Shard
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Nimble
    Ring, Gluttonous Grimoire, Bragi''s Harp, Ancient Signet, Bracer of The Abyss,
    Death Metal, Chronos'' Pendant, Bancroft''s Talon, Blood-Bound Book, Dreamer''s
    Idol, Gem of Focus, Polynomicon, Rod of Asclepius, The Cosmic Horror, Typhon’s
    Heart, Totem of Death, Jade Scepter, Divine Ruin, Triton''s Conch, Wish-Granting
    Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.63
      efficiency: 0.51
      win: 0.88
      pick: 0.33
      fit: 0.28
    Spear of Desolation:
      total: 0.73
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.45
    The World Stone:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.18
      fit: 0.42
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 0.89
      pick: 0.72
      fit: 0.42
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.71
      pick: 0.8
      fit: 0.44
    Soul Gem:
      total: 0.76
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
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
    god: Nimble Ring, Gluttonous Grimoire, Bragi''s Harp, Chronos'' Pendant, Bracer
    of The Abyss, Dreamer''s Idol, Death Metal, Ancient Signet, Blood-Bound Book,
    Gem of Focus, The Cosmic Horror, Bancroft''s Talon, Rod of Asclepius, Totem of
    Death, Typhon’s Heart, Polynomicon, Jade Scepter, Divine Ruin, Breastplate of
    Valor, Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.61
      efficiency: 0.51
      win: 0.88
      pick: 0.33
      fit: 0.16
    Spear of Desolation:
      total: 0.75
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.56
    The World Stone:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.18
      fit: 0.4
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 0.89
      pick: 0.72
      fit: 0.4
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.71
      pick: 0.8
      fit: 0.5
    Soul Gem:
      total: 0.77
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Nimble Ring
  - Book of Thoth
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
    Genji''s Guard, Breastplate of Valor, Bancroft''s Talon, Shifter''s Shield, Lifebinder,
    Yogi''s Necklace, Helm of Radiance, Sphere of Negation, Phoenix Feather, Chandra''s
    Grace, Erosion, Eye of Providence, Jade Scepter, Bracer of The Abyss, Draconic
    Scale.'
  slot_scores:
    Book of Thoth:
      total: 0.61
      efficiency: 0.51
      win: 0.88
      pick: 0.33
      fit: 0.15
    Nimble Ring:
      total: 0.62
      efficiency: 0.65
      win: 0.73
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.72
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.36
    The World Stone:
      total: 0.68
      efficiency: 0.52
      win: 1.0
      pick: 0.18
      fit: 0.28
    Rod of Tahuti:
      total: 0.78
      efficiency: 0.86
      win: 0.89
      pick: 0.72
      fit: 0.28
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.83
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
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
    for this god: Gluttonous Grimoire, Nimble Ring, Dreamer''s Idol, Bracer of The
    Abyss, The Cosmic Horror, Chronos'' Pendant, Blood-Bound Book, Ancient Signet,
    Bancroft''s Talon, Gem of Focus, Rod of Asclepius, Typhon’s Heart, Polynomicon,
    Totem of Death, Jade Scepter, Divine Ruin, Screeching Gargoyle, Helm of Radiance,
    Bragi''s Harp, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.62
      efficiency: 0.51
      win: 0.88
      pick: 0.33
      fit: 0.19
    Spear of Desolation:
      total: 0.76
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.66
    The World Stone:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.18
      fit: 0.56
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 0.89
      pick: 0.72
      fit: 0.56
    Obsidian Shard:
      total: 0.65
      efficiency: 0.54
      win: 0.71
      pick: 0.8
      fit: 0.66
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
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
    this god: Nimble Ring, Gluttonous Grimoire, Bragi''s Harp, Bracer of The Abyss,
    Chronos'' Pendant, Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Death Metal,
    Bancroft''s Talon, Gem of Focus, The Cosmic Horror, Rod of Asclepius, Typhon’s
    Heart, Polynomicon, Totem of Death, Jade Scepter, Divine Ruin, Helm of Radiance,
    Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.57
      efficiency: 0.52
      win: 0.73
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.63
      efficiency: 0.65
      win: 0.73
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.58
      efficiency: 0.44
      win: 0.73
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.72
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.39
    Rod of Tahuti:
      total: 0.78
      efficiency: 0.86
      win: 0.89
      pick: 0.72
      fit: 0.31
    Soul Gem:
      total: 0.75
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Nimble Ring, Gluttonous Grimoire,
    Chronos'' Pendant, Gem of Focus, Bragi''s Harp, Bracer of The Abyss, Totem of
    Death, Ancient Signet, Dreamer''s Idol, Blood-Bound Book, Breastplate of Valor,
    Death Metal, Genji''s Guard, Bancroft''s Talon, The Cosmic Horror, Rod of Asclepius,
    Typhon’s Heart, Polynomicon, Staff of Myrddin, Eye of Erebus.'
  slot_scores:
    Book of Thoth:
      total: 0.61
      efficiency: 0.51
      win: 0.88
      pick: 0.33
      fit: 0.1
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.73
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.75
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.6
    The World Stone:
      total: 0.68
      efficiency: 0.52
      win: 1.0
      pick: 0.18
      fit: 0.26
    Rod of Tahuti:
      total: 0.77
      efficiency: 0.86
      win: 0.89
      pick: 0.72
      fit: 0.26
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Transcendence
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Nimble Ring, Gluttonous
    Grimoire, The Reaper, Heartseeker, Hydra''s Lament, Bragi''s Harp, Tekko-Kagi,
    Silverbranch Bow, Lernaean Bow, Golden Blade, Titan''s Bane, Death Metal, The
    Crusher, Chronos'' Pendant, Pendulum Blade, Dreamer''s Idol, Arondight, Blood-Bound
    Book, Avatar''s Parashu, Ancient Signet, Toxic Blade, Bracer of The Abyss, Transcendence,
    Runeforged Hammer, Bancroft''s Talon, Gem of Focus, The Cosmic Horror, Barbed
    Carver, Qin''s Blade, Rod of Asclepius, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.62
      efficiency: 0.51
      win: 0.88
      pick: 0.33
      fit: 0.2
    Transcendence:
      total: 0.56
      efficiency: 0.53
      win: 0.73
      pick: 0.0
      fit: 0.29
    Spear of Desolation:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.49
    The World Stone:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.18
      fit: 0.39
    Rod of Tahuti:
      total: 0.79
      efficiency: 0.86
      win: 0.89
      pick: 0.72
      fit: 0.39
    Soul Gem:
      total: 0.77
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Transcendence
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Nimble Ring, Gluttonous
    Grimoire, Silverbranch Bow, Bragi''s Harp, Tekko-Kagi, The Reaper, Lernaean Bow,
    Golden Blade, Heartseeker, Hydra''s Lament, Bracer of The Abyss, Death Metal,
    Toxic Blade, Titan''s Bane, Chronos'' Pendant, The Crusher, Dreamer''s Idol, Ancient
    Signet, Blood-Bound Book, Bancroft''s Talon, Qin''s Blade, Arondight, Gem of Focus,
    Pendulum Blade, Avatar''s Parashu, Transcendence, The Cosmic Horror, Runeforged
    Hammer, Rod of Asclepius, Typhon’s Heart, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.62
      efficiency: 0.51
      win: 0.88
      pick: 0.33
      fit: 0.21
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.73
      pick: 0.0
      fit: 0.21
    Spear of Desolation:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.48
    The World Stone:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.18
      fit: 0.38
    Rod of Tahuti:
      total: 0.79
      efficiency: 0.86
      win: 0.89
      pick: 0.72
      fit: 0.38
    Soul Gem:
      total: 0.76
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.66
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
    Underrated for this god: Nimble Ring, Gluttonous Grimoire, Bracer of The Abyss,
    Chronos'' Pendant, Dreamer''s Idol, Blood-Bound Book, Ancient Signet, Bancroft''s
    Talon, Gem of Focus, The Cosmic Horror, Typhon’s Heart, Rod of Asclepius, Polynomicon,
    Totem of Death, Jade Scepter, Divine Ruin, Bragi''s Harp, Helm of Radiance, Ethereal
    Staff, Wish-Granting Pearl.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.59
      efficiency: 0.52
      win: 0.73
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.65
      efficiency: 0.65
      win: 0.73
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.75
      efficiency: 0.57
      win: 1.0
      pick: 0.26
      fit: 0.58
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.17
      fit: 0.46
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 0.89
      pick: 0.72
      fit: 0.46
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.71
      pick: 0.8
      fit: 0.56
  starter: *id001
---
