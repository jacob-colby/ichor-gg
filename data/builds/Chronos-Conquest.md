---
type: smite-build
god: Chronos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Relativity
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.83
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.53
    win_rate: 0.46
    alternates:
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.5
    - name: Polynomicon
      pick_rate: 0.06
      win_rate: 0.67
  - name: Polynomicon
    pick_rate: 0.49
    win_rate: 0.49
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.5
    - name: Nimble Ring
      pick_rate: 0.07
      win_rate: 0.62
  - name: Rod of Tahuti
    pick_rate: 0.42
    win_rate: 0.56
    alternates:
    - name: Nimble Ring
      pick_rate: 0.23
      win_rate: 0.4
    - name: Polynomicon
      pick_rate: 0.11
      win_rate: 0.55
  - name: Nimble Ring
    pick_rate: 0.35
    win_rate: 0.6
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.23
      win_rate: 0.35
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.55
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.48
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.13
      win_rate: 0.43
    - name: Nimble Ring
      pick_rate: 0.09
      win_rate: 0.27
  - name: Blinking Abyss
    pick_rate: 0.14
    win_rate: 0.62
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.36
    - name: Killing Stone
      pick_rate: 0.1
      win_rate: 0.6
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.48
    win_rate: 0.53
  - name: Sands Of Time
    pick_rate: 0.21
    win_rate: 0.53
  - name: Archmage's Gem
    pick_rate: 0.06
    win_rate: 0.36
  source_url: https://smitebrain.com/gods/chronos/
  last_verified: '2026-11-08'
  god_win_rate: 0.5208333333333334
  god_matches_won: 100
  god_matches_played: 192
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Bracer of The Abyss
  - Polynomicon
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Polynomicon
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
    this god: Soul Gem, Gluttonous Grimoire, Blood-Bound Book, Bracer of The Abyss,
    Spear of the Magus, Dreamer''s Idol, Ancient Signet, Chronos'' Pendant, Doom Orb,
    The World Stone, Bancroft''s Talon, Gem of Focus, Heartwood Charm, Soul Reaver,
    The Cosmic Horror, Bragi''s Harp, Typhon’s Heart, Totem of Death, Jade Scepter,
    Divine Ruin, Genji''s Guard, Ethereal Staff, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.56
    Polynomicon:
      total: 0.5
      efficiency: 0.56
      win: 0.49
      pick: 0.67
      fit: 0.34
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.44
    Nimble Ring:
      total: 0.6
      efficiency: 0.57
      win: 0.6
      pick: 0.58
      fit: 0.68
    Obsidian Shard:
      total: 0.5
      efficiency: 0.53
      win: 0.48
      pick: 0.39
      fit: 0.54
  community_ordered:
  - Polynomicon
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Polynomicon
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Bragi's Harp
  flex_slots:
  - Polynomicon
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Bragi''s Harp, Gluttonous Grimoire, Death Metal, Ancient Signet, Blood-Bound
    Book, Spear of the Magus, Chronos'' Pendant, Bracer of The Abyss, Doom Orb, Dreamer''s
    Idol, Bancroft''s Talon, The World Stone, Heartwood Charm, Soul Reaver, Gem of
    Focus, The Cosmic Horror, Totem of Death, Genji''s Guard, Typhon’s Heart, Triton''s
    Conch, Jade Scepter, Divine Ruin.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.16
      fit: 0.28
    Polynomicon:
      total: 0.51
      efficiency: 0.56
      win: 0.49
      pick: 0.67
      fit: 0.38
    Spear of Desolation:
      total: 0.51
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.45
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.42
    Nimble Ring:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.58
      fit: 0.48
    Bragi's Harp:
      total: 0.51
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Polynomicon
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Bragi's Harp
  - Rod of Tahuti
  - Nimble Ring
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Spear of the Magus
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
    god: Soul Gem, Gluttonous Grimoire, Bragi''s Harp, Spear of the Magus, Blood-Bound
    Book, Dreamer''s Idol, Death Metal, Chronos'' Pendant, Ancient Signet, Bracer
    of The Abyss, Doom Orb, The World Stone, Gem of Focus, Heartwood Charm, Bancroft''s
    Talon, The Cosmic Horror, Soul Reaver, Totem of Death, Damaru, Genji''s Guard,
    Typhon’s Heart, Jade Scepter, Divine Ruin.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.56
    Bragi's Harp:
      total: 0.5
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.4
    Nimble Ring:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.58
      fit: 0.44
    Spear of the Magus:
      total: 0.49
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.4
    Obsidian Shard:
      total: 0.5
      efficiency: 0.53
      win: 0.48
      pick: 0.39
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Blood-Bound Book, Gluttonous
    Grimoire, Kinetic Cuirass, Genji''s Guard, Ethereal Staff, Phoenix Feather, Yogi''s
    Necklace, Bancroft''s Talon, Freya''s Tears, Breastplate of Valor, Chandra''s
    Grace, Oni Hunter''s Garb, Draconic Scale, Helm of Radiance, Sphere of Negation,
    Ancient Signet, Erosion, Regrowth Striders, Eye of Providence, Spear of the Magus,
    Helm of Darkness, Bracer of The Abyss.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.19
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.31
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.27
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Nimble Ring
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Doom Orb
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
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Dreamer''s Idol,
    Doom Orb, The World Stone, Blood-Bound Book, Bracer of The Abyss, Ancient Signet,
    The Cosmic Horror, Chronos'' Pendant, Bancroft''s Talon, Gem of Focus, Heartwood
    Charm, Soul Reaver, Typhon’s Heart, Totem of Death, Bragi''s Harp, Screeching
    Gargoyle, Jade Scepter, Genji''s Guard, Divine Ruin, Ethereal Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.66
    Doom Orb:
      total: 0.5
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.57
    Nimble Ring:
      total: 0.58
      efficiency: 0.57
      win: 0.6
      pick: 0.58
      fit: 0.53
    Spear of the Magus:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.57
    Obsidian Shard:
      total: 0.52
      efficiency: 0.53
      win: 0.48
      pick: 0.39
      fit: 0.67
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Bragi's Harp
  - Rod of Tahuti
  - Nimble Ring
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
    this god: Soul Gem, Bragi''s Harp, Gluttonous Grimoire, Blood-Bound Book, Bracer
    of The Abyss, Death Metal, Ancient Signet, Spear of the Magus, Chronos'' Pendant,
    Dreamer''s Idol, Doom Orb, Bancroft''s Talon, The World Stone, Soul Reaver, Gem
    of Focus, Heartwood Charm, The Cosmic Horror, Typhon’s Heart, Totem of Death,
    Damaru, Genji''s Guard, Jade Scepter, Divine Ruin.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.5
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.38
    Bragi's Harp:
      total: 0.5
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.64
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.3
    Nimble Ring:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.58
      fit: 0.49
    Soul Gem:
      total: 0.53
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Bragi's Harp
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Gem of Focus
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
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Gluttonous
    Grimoire, Bragi''s Harp, Gem of Focus, Heartwood Charm, Blood-Bound Book, Bracer
    of The Abyss, Spear of the Magus, Ancient Signet, Damaru, Genji''s Guard, Death
    Metal, Totem of Death, Dreamer''s Idol, Doom Orb, Bancroft''s Talon, Breastplate
    of Valor, The World Stone, Chandra''s Grace, Soul Reaver, The Cosmic Horror, Typhon’s
    Heart, Screeching Gargoyle.'
  slot_scores:
    Chronos' Pendant:
      total: 0.5
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.45
    Bragi's Harp:
      total: 0.48
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.59
    Gem of Focus:
      total: 0.48
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.24
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Bragi's Harp
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Tyrfing, The
    Reaper, Gluttonous Grimoire, Bragi''s Harp, Death Metal, The Crusher, Hydra''s
    Lament, Tekko-Kagi, Heartseeker, Blood-Bound Book, Titan''s Bane, Spear of the
    Magus, Dreamer''s Idol, Golden Blade, Ancient Signet, Riptalon, Silverbranch Bow,
    Arondight, Lernaean Bow, Dominance, Chronos'' Pendant, Doom Orb, Avatar''s Parashu,
    The World Stone, Bracer of The Abyss, Bancroft''s Talon, Pendulum Blade, Toxic
    Blade, Gem of Focus, Heartwood Charm, Bloodforge, Soul Reaver, Transcendence,
    Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.49
    Bragi's Harp:
      total: 0.51
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.71
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.39
    Soul Gem:
      total: 0.55
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Bragi's Harp
  flex_slots:
  - Bragi's Harp
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Tyrfing,
    Bragi''s Harp, Gluttonous Grimoire, The Reaper, Tekko-Kagi, Death Metal, Blood-Bound
    Book, Silverbranch Bow, Spear of the Magus, Riptalon, Hydra''s Lament, The Crusher,
    Bracer of The Abyss, Golden Blade, Ancient Signet, Lernaean Bow, Dominance, Heartseeker,
    Dreamer''s Idol, Chronos'' Pendant, Titan''s Bane, Doom Orb, Toxic Blade, The
    World Stone, Arondight, Bancroft''s Talon, Qin''s Blade, Gem of Focus, Heartwood
    Charm, Soul Reaver, Avatar''s Parashu, The Cosmic Horror, Pendulum Blade, Dagger
    of Frenzy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.47
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.39
    Nimble Ring:
      total: 0.58
      efficiency: 0.57
      win: 0.6
      pick: 0.58
      fit: 0.53
    Bragi's Harp:
      total: 0.52
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.75
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Bracer of The Abyss
  - Spear of the Magus
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
    Underrated for this god: Soul Gem, Gluttonous Grimoire, Blood-Bound Book, Bracer
    of The Abyss, Spear of the Magus, Dreamer''s Idol, Ancient Signet, Chronos'' Pendant,
    Doom Orb, The World Stone, Bancroft''s Talon, Gem of Focus, Heartwood Charm, Soul
    Reaver, The Cosmic Horror, Bragi''s Harp, Typhon’s Heart, Totem of Death, Jade
    Scepter, Divine Ruin, Genji''s Guard, Ethereal Staff, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.44
    Nimble Ring:
      total: 0.6
      efficiency: 0.57
      win: 0.6
      pick: 0.58
      fit: 0.68
    Spear of the Magus:
      total: 0.5
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.44
    Obsidian Shard:
      total: 0.5
      efficiency: 0.53
      win: 0.48
      pick: 0.39
      fit: 0.54
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Spear of Desolation
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Lotus Sickle, Eros'' Bow, Gluttonous Grimoire, Genji''s Guard,
    Amanita Charm, Void Stone, Blood-Bound Book, Bracer of The Abyss, Chronos'' Pendant,
    Doublet of Binding, Spear of the Magus, Rod of Asclepius, Screeching Gargoyle,
    Soul Locket, Ancient Signet, Dreamer''s Idol, Oni Hunter''s Garb, Doom Orb, Gem
    of Focus, Heartwood Charm, Jade Scepter, Lifebinder, Kinetic Cuirass, Bancroft''s
    Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.25
    Spear of Desolation:
      total: 0.51
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.46
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.29
    Lotus Sickle:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.69
    Eros' Bow:
      total: 0.53
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Genji's Guard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Lotus Sickle, Eros'' Bow, Genji''s Guard, Gluttonous Grimoire, Triton''s
    Conch, Amanita Charm, Bragi''s Harp, Ancient Signet, Death Metal, Blood-Bound
    Book, Rod of Asclepius, Spear of the Magus, Soul Locket, Void Stone, Chronos''
    Pendant, Bracer of The Abyss, Doom Orb, Dreamer''s Idol, Oni Hunter''s Garb, Doublet
    of Binding, Bancroft''s Talon, Heartwood Charm, The World Stone, Soul Reaver.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.16
      fit: 0.25
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.21
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.37
    Lotus Sickle:
      total: 0.55
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.75
    Eros' Bow:
      total: 0.52
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.71
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Genji's Guard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Lotus Sickle, Gluttonous Grimoire, Genji''s Guard, Eros'' Bow,
    Amanita Charm, Triton''s Conch, Bragi''s Harp, Spear of the Magus, Blood-Bound
    Book, Dreamer''s Idol, Void Stone, Death Metal, Chronos'' Pendant, Ancient Signet,
    Rod of Asclepius, Soul Locket, Doublet of Binding, Bracer of The Abyss, Doom Orb,
    Screeching Gargoyle, The World Stone, Oni Hunter''s Garb, Gem of Focus, Heartwood
    Charm.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.48
      win: 0.5
      pick: 0.16
      fit: 0.14
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.49
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.2
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.35
    Lotus Sickle:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Lotus Sickle
  - Rod of Tahuti
  - Eros' Bow
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Lotus Sickle, Rod of
    Asclepius, Eros'' Bow, Kinetic Cuirass, Soul Locket, Genji''s Guard, Blood-Bound
    Book, Erosion, Gluttonous Grimoire, Lifebinder, Freya''s Tears, Umbral Link, Void
    Stone, Phoenix Feather, Stampede, Ethereal Staff, Yogi''s Necklace, Void Shield,
    Spectral Armor, Breastplate of Valor, Doublet of Binding, Chandra''s Grace, Bancroft''s
    Talon, Oni Hunter''s Garb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.49
    Lotus Sickle:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.21
    Eros' Bow:
      total: 0.53
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.74
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.99
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Void Stone
  - Rod of Tahuti
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Void Stone
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Lotus Sickle, Void Stone, Genji''s
    Guard, Eros'' Bow, Screeching Gargoyle, Amanita Charm, Spear of the Magus, Dreamer''s
    Idol, Doom Orb, Blood-Bound Book, The World Stone, Doublet of Binding, Chronos''
    Pendant, Rod of Asclepius, Bracer of The Abyss, Ancient Signet, Soul Locket, Oni
    Hunter''s Garb, The Cosmic Horror, Kinetic Cuirass, Jade Scepter, Gem of Focus,
    Lifebinder.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.2
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.57
    Void Stone:
      total: 0.53
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.83
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.43
    Lotus Sickle:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bragi's Harp
  - Rod of Tahuti
  - Nimble Ring
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Lotus Sickle, Eros'' Bow, Genji''s Guard, Gluttonous Grimoire,
    Amanita Charm, Bragi''s Harp, Triton''s Conch, Void Stone, Blood-Bound Book, Doublet
    of Binding, Bracer of The Abyss, Rod of Asclepius, Ancient Signet, Death Metal,
    Chronos'' Pendant, Soul Locket, Screeching Gargoyle, Spear of the Magus, Oni Hunter''s
    Garb, Dreamer''s Idol, Kinetic Cuirass, Jade Scepter, Doom Orb, Lifebinder.'
  slot_scores:
    Bragi's Harp:
      total: 0.48
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.21
    Nimble Ring:
      total: 0.55
      efficiency: 0.57
      win: 0.6
      pick: 0.58
      fit: 0.38
    Lotus Sickle:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.61
    Eros' Bow:
      total: 0.52
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.67
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Rod of Tahuti
  - Nimble Ring
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Eros' Bow
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Lotus Sickle, Genji''s Guard,
    Eros'' Bow, Gluttonous Grimoire, Amanita Charm, Chronos'' Pendant, Screeching
    Gargoyle, Void Stone, Triton''s Conch, Blood-Bound Book, Bragi''s Harp, Gem of
    Focus, Heartwood Charm, Doublet of Binding, Rod of Asclepius, Ancient Signet,
    Soul Locket, Spear of the Magus, Bracer of The Abyss, Oni Hunter''s Garb, Chandra''s
    Grace, Freya''s Tears, Death Metal, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.36
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.46
      pick: 0.53
      fit: 0.52
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.21
    Lotus Sickle:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.79
    Eros' Bow:
      total: 0.51
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.99
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Lotus Sickle,
    Gluttonous Grimoire, Genji''s Guard, Tyrfing, The Reaper, Amanita Charm, Triton''s
    Conch, Hydra''s Lament, Golden Blade, Eros'' Bow, Sanguine Lash, The Crusher,
    Runeforged Hammer, Heartseeker, Shogun''s Ofuda, Death Metal, Pharaoh''s Curse,
    Tekko-Kagi, Bragi''s Harp, Titan''s Bane, Void Stone, Arondight, Blood-Bound Book,
    Toxic Blade, Spear of the Magus, Doublet of Binding, Lernaean Bow, Dominance,
    Silverbranch Bow, Chronos'' Pendant, Riptalon, Rod of Asclepius, Ancient Signet,
    Soul Locket, Screeching Gargoyle, Shield Splitter.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.48
      win: 0.5
      pick: 0.16
      fit: 0.1
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.57
    Transcendence:
      total: 0.45
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.26
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.28
    Lotus Sickle:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.9
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Lotus Sickle, Jotunn''s
    Revenge, Eros'' Bow, Gluttonous Grimoire, Tyrfing, Genji''s Guard, Amanita Charm,
    Triton''s Conch, Shogun''s Ofuda, Bragi''s Harp, Pharaoh''s Curse, Golden Blade,
    The Reaper, Hydra''s Lament, Blood-Bound Book, Death Metal, Tekko-Kagi, Sanguine
    Lash, Spear of the Magus, Rod of Asclepius, Ancient Signet, Runeforged Hammer,
    Void Stone, Toxic Blade, The Crusher, Chronos'' Pendant, Silverbranch Bow, Soul
    Locket, Bracer of The Abyss, Riptalon, Heartseeker, Dreamer''s Idol, Lernaean
    Bow, Dominance, Doublet of Binding, Titan''s Bane.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.48
      win: 0.5
      pick: 0.16
      fit: 0.18
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.44
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.18
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.32
    Lotus Sickle:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: model
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Genji's Guard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Lotus Sickle, Eros'' Bow, Gluttonous Grimoire,
    Genji''s Guard, Amanita Charm, Void Stone, Blood-Bound Book, Bracer of The Abyss,
    Chronos'' Pendant, Doublet of Binding, Spear of the Magus, Rod of Asclepius, Screeching
    Gargoyle, Soul Locket, Ancient Signet, Dreamer''s Idol, Oni Hunter''s Garb, Doom
    Orb, Gem of Focus, Heartwood Charm, Jade Scepter, Lifebinder, Kinetic Cuirass,
    Bancroft''s Talon.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.48
      win: 0.5
      pick: 0.16
      fit: 0.12
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.25
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.56
      pick: 0.65
      fit: 0.29
    Lotus Sickle:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.69
    Eros' Bow:
      total: 0.53
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-10-20'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of Relativity
    status: below minimum
    matches_by_window:
      ob47: 7
      ob46: 28
---
