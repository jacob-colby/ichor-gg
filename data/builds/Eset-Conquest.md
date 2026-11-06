---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.62
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.42
    win_rate: 0.67
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.12
      win_rate: 0.38
    - name: Gauntlet of Thebes
      pick_rate: 0.08
      win_rate: 0.6
  - name: Soul Gem
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.45
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.63
    alternates:
    - name: Soul Gem
      pick_rate: 0.11
      win_rate: 0.71
    - name: The World Stone
      pick_rate: 0.08
      win_rate: 0.8
  - name: Obsidian Shard
    pick_rate: 0.22
    win_rate: 0.46
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.22
      win_rate: 0.69
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.67
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.4
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.88
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.25
  - name: Time-lock Aegis
    pick_rate: 0.15
    win_rate: 0.8
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.06
      win_rate: 1.0
    - name: Oracle Staff
      pick_rate: 0.06
      win_rate: 0.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.35
    win_rate: 0.48
  - name: Conduit Gem
    pick_rate: 0.15
    win_rate: 0.5
  - name: Pendulum of the Ages
    pick_rate: 0.11
    win_rate: 0.86
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-11-06'
  god_win_rate: 0.5230769230769231
  god_matches_won: 34
  god_matches_played: 65
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of the Magus
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
    this god: Soul Gem, The World Stone, Spear of the Magus, Lotus Sickle, Dreamer''s
    Idol, Gluttonous Grimoire, Doom Orb, Ancient Signet, Gem of Focus, Heartwood Charm,
    The Cosmic Horror, Polynomicon, Blood-Bound Book, Totem of Death, Soul Reaver,
    Book of Thoth, Bancroft''s Talon, Jade Scepter, Divine Ruin, Ethereal Staff, Helm
    of Radiance, Staff of Myrddin, Genji''s Guard, Bracer of The Abyss, Death Metal,
    Rod of Asclepius, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.54
      efficiency: 0.48
      win: 0.67
      pick: 0.12
      fit: 0.41
    Spear of Desolation:
      total: 0.68
      efficiency: 0.6
      win: 0.67
      pick: 0.42
      fit: 1.0
    Spear of the Magus:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.77
    The World Stone:
      total: 0.65
      efficiency: 0.49
      win: 0.8
      pick: 0.12
      fit: 0.77
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.63
      pick: 0.2
      fit: 0.77
    Soul Gem:
      total: 0.79
      efficiency: 0.53
      win: 1.0
      pick: 0.12
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
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
  - Soul Gem
  - Lotus Sickle
  flex_slots:
  - Lotus Sickle
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, The World Stone, Lotus Sickle, Death Metal, Ancient Signet, Polynomicon,
    Spear of the Magus, Doom Orb, Dreamer''s Idol, Heartwood Charm, Bragi''s Harp,
    Gluttonous Grimoire, Soul Reaver, Gem of Focus, Blood-Bound Book, Book of Thoth,
    The Cosmic Horror, Bancroft''s Talon, Totem of Death, Triton''s Conch, Genji''s
    Guard, Jade Scepter, Divine Ruin, Ethereal Staff, Damaru, Helm of Radiance, Chronos''
    Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.48
      win: 0.67
      pick: 0.12
      fit: 0.39
    Spear of Desolation:
      total: 0.63
      efficiency: 0.6
      win: 0.67
      pick: 0.42
      fit: 0.61
    The World Stone:
      total: 0.63
      efficiency: 0.49
      win: 0.8
      pick: 0.12
      fit: 0.57
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.63
      pick: 0.2
      fit: 0.57
    Soul Gem:
      total: 0.75
      efficiency: 0.53
      win: 1.0
      pick: 0.12
      fit: 0.71
    Lotus Sickle:
      total: 0.6
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  - Lotus Sickle
  flex_slots:
  - Lotus Sickle
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
    god: Soul Gem, The World Stone, Lotus Sickle, Spear of the Magus, Dreamer''s Idol,
    Gluttonous Grimoire, Death Metal, Doom Orb, Ancient Signet, Gem of Focus, Heartwood
    Charm, Polynomicon, The Cosmic Horror, Bragi''s Harp, Blood-Bound Book, Totem
    of Death, Soul Reaver, Damaru, Genji''s Guard, Book of Thoth, Triton''s Conch,
    Bancroft''s Talon, Jade Scepter, Divine Ruin, Breastplate of Valor, Ethereal Staff,
    Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.67
      pick: 0.12
      fit: 0.22
    Spear of Desolation:
      total: 0.65
      efficiency: 0.6
      win: 0.67
      pick: 0.42
      fit: 0.78
    The World Stone:
      total: 0.62
      efficiency: 0.49
      win: 0.8
      pick: 0.12
      fit: 0.56
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.63
      pick: 0.2
      fit: 0.56
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 1.0
      pick: 0.12
      fit: 0.88
    Lotus Sickle:
      total: 0.58
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Soul Gem, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Genji''s
    Guard, Ethereal Staff, Gluttonous Grimoire, Freya''s Tears, Phoenix Feather, Blood-Bound
    Book, Yogi''s Necklace, Rod of Asclepius, Soul Locket, Breastplate of Valor, Lotus
    Sickle, Chandra''s Grace, Draconic Scale, Oni Hunter''s Garb, Helm of Radiance,
    Sphere of Negation, Erosion, Helm of Darkness, Spear of the Magus, Eye of Providence,
    Shifter''s Shield, Regrowth Striders, Jade Scepter.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.67
      pick: 0.42
      fit: 0.5
    The World Stone:
      total: 0.6
      efficiency: 0.49
      win: 0.8
      pick: 0.12
      fit: 0.38
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.63
      pick: 0.2
      fit: 0.38
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.12
      fit: 0.9
    Amanita Charm:
      total: 0.66
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Spear of the Magus
  - Dreamer's Idol
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Time-lock Aegis — CC-immunity / cleanse
    swap_item: Time-lock Aegis
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
    for this god: Soul Gem, The World Stone, Spear of the Magus, Dreamer''s Idol,
    Gluttonous Grimoire, Doom Orb, The Cosmic Horror, Lotus Sickle, Ancient Signet,
    Polynomicon, Gem of Focus, Heartwood Charm, Blood-Bound Book, Soul Reaver, Totem
    of Death, Book of Thoth, Bancroft''s Talon, Jade Scepter, Divine Ruin, Screeching
    Gargoyle, Genji''s Guard, Ethereal Staff, Helm of Radiance, Bracer of The Abyss,
    Death Metal, Rod of Asclepius, Chronos'' Pendant.'
  slot_scores:
    Spear of Desolation:
      total: 0.68
      efficiency: 0.6
      win: 0.67
      pick: 0.42
      fit: 1.0
    Spear of the Magus:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.84
    The World Stone:
      total: 0.66
      efficiency: 0.49
      win: 0.8
      pick: 0.12
      fit: 0.84
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.82
      win: 0.63
      pick: 0.2
      fit: 0.84
    Soul Gem:
      total: 0.79
      efficiency: 0.53
      win: 1.0
      pick: 0.12
      fit: 1.0
    Dreamer's Idol:
      total: 0.62
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.84
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Bragi's Harp
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
    this god: Soul Gem, The World Stone, Nimble Ring, Gluttonous Grimoire, Bragi''s
    Harp, Lotus Sickle, Blood-Bound Book, Bracer of The Abyss, Spear of the Magus,
    Death Metal, Ancient Signet, Dreamer''s Idol, Polynomicon, Doom Orb, Eros'' Bow,
    Bancroft''s Talon, Gem of Focus, Heartwood Charm, Soul Reaver, The Cosmic Horror,
    Book of Thoth, Typhon’s Heart, Totem of Death, Damaru, Genji''s Guard, Jade Scepter,
    Chronos'' Pendant.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.55
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.57
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.67
      pick: 0.42
      fit: 0.41
    Bragi's Harp:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.63
      pick: 0.2
      fit: 0.31
    Soul Gem:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.12
      fit: 0.58
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  - Lotus Sickle
  flex_slots:
  - The World Stone
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Lotus Sickle, The World
    Stone, Gem of Focus, Heartwood Charm, Totem of Death, Spear of the Magus, Damaru,
    Genji''s Guard, Dreamer''s Idol, Death Metal, Gluttonous Grimoire, Ancient Signet,
    Doom Orb, Polynomicon, Breastplate of Valor, Chandra''s Grace, Blood-Bound Book,
    The Cosmic Horror, Bragi''s Harp, Soul Reaver, Staff of Myrddin, Screeching Gargoyle,
    Freya''s Tears, Eye of Erebus, Shield of the Phoenix, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.67
      pick: 0.12
      fit: 0.14
    Spear of Desolation:
      total: 0.66
      efficiency: 0.6
      win: 0.67
      pick: 0.42
      fit: 0.86
    The World Stone:
      total: 0.6
      efficiency: 0.49
      win: 0.8
      pick: 0.12
      fit: 0.37
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.63
      pick: 0.2
      fit: 0.37
    Soul Gem:
      total: 0.79
      efficiency: 0.53
      win: 1.0
      pick: 0.12
      fit: 0.96
    Lotus Sickle:
      total: 0.61
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, The World Stone,
    Tyrfing, Bragi''s Harp, Death Metal, Hydra''s Lament, The Crusher, Tekko-Kagi,
    Heartseeker, Lotus Sickle, Titan''s Bane, Spear of the Magus, The Reaper, Dreamer''s
    Idol, Arondight, Ancient Signet, Gluttonous Grimoire, Lernaean Bow, Dominance,
    Golden Blade, Doom Orb, Polynomicon, Silverbranch Bow, Avatar''s Parashu, Bracer
    of The Abyss, Pendulum Blade, Nimble Ring, Gem of Focus, Heartwood Charm, Blood-Bound
    Book, Soul Reaver, Toxic Blade, The Cosmic Horror, Transcendence, Runeforged Hammer,
    Triton''s Conch, Eros'' Bow, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.67
      pick: 0.12
      fit: 0.22
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.67
      pick: 0.42
      fit: 0.56
    Transcendence:
      total: 0.52
      efficiency: 0.5
      win: 0.67
      pick: 0.0
      fit: 0.32
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.63
      pick: 0.2
      fit: 0.43
    Soul Gem:
      total: 0.74
      efficiency: 0.53
      win: 1.0
      pick: 0.12
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Death Metal
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The World Stone
  - Death Metal
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, The World
    Stone, Death Metal, Lotus Sickle, Spear of the Magus, The Crusher, Hydra''s Lament,
    Heartseeker, Dreamer''s Idol, Gluttonous Grimoire, Titan''s Bane, The Reaper,
    Doom Orb, Ancient Signet, Tyrfing, Bragi''s Harp, Polynomicon, Arondight, Gem
    of Focus, Heartwood Charm, Avatar''s Parashu, Pendulum Blade, Blood-Bound Book,
    The Cosmic Horror, Soul Reaver, Tekko-Kagi, Totem of Death, Triton''s Conch, Transcendence,
    Book of Thoth, Runeforged Hammer, Dominance, Bancroft''s Talon, Jade Scepter,
    Divine Ruin, Shield Splitter, Eye of the Storm, Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.64
      efficiency: 0.6
      win: 0.67
      pick: 0.42
      fit: 0.7
    Death Metal:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.6
    The World Stone:
      total: 0.62
      efficiency: 0.49
      win: 0.8
      pick: 0.12
      fit: 0.55
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.63
      pick: 0.2
      fit: 0.55
    Soul Gem:
      total: 0.76
      efficiency: 0.53
      win: 1.0
      pick: 0.12
      fit: 0.8
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  - Lotus Sickle
  flex_slots:
  - Spear of the Magus
  - Lotus Sickle
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
    Underrated for this god: Soul Gem, Spear of the Magus, Lotus Sickle, Dreamer''s
    Idol, Gluttonous Grimoire, Doom Orb, Chronos'' Pendant, The World Stone, Ancient
    Signet, Gem of Focus, Heartwood Charm, The Cosmic Horror, Polynomicon, Blood-Bound
    Book, Totem of Death, Soul Reaver, Book of Thoth, Bancroft''s Talon, Jade Scepter,
    Divine Ruin, Ethereal Staff, Helm of Radiance, Staff of Myrddin, Genji''s Guard,
    Bracer of The Abyss, Death Metal, Rod of Asclepius.'
  slot_scores:
    Spear of Desolation:
      total: 0.68
      efficiency: 0.6
      win: 0.67
      pick: 0.42
      fit: 1.0
    Spear of the Magus:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.46
      pick: 0.37
      fit: 0.87
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.63
      pick: 0.2
      fit: 0.77
    Soul Gem:
      total: 0.79
      efficiency: 0.53
      win: 1.0
      pick: 0.12
      fit: 1.0
    Lotus Sickle:
      total: 0.61
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
---
