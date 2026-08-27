---
type: smite-build
god: Poseidon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Trident
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.86
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.58
    win_rate: 0.55
    alternates:
    - name: Book of Thoth
      pick_rate: 0.18
      win_rate: 0.5
    - name: Doom Orb
      pick_rate: 0.05
      win_rate: 0.43
  - name: The World Stone
    pick_rate: 0.2
    win_rate: 0.56
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.55
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.5
  - name: Nimble Ring
    pick_rate: 0.16
    win_rate: 0.8
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.55
    - name: The World Stone
      pick_rate: 0.15
      win_rate: 0.42
  - name: Rod of Tahuti
    pick_rate: 0.37
    win_rate: 0.7
    alternates:
    - name: Nimble Ring
      pick_rate: 0.19
      win_rate: 0.5
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.33
  - name: Evil Eye
    pick_rate: 0.14
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.47
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.79
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.2
    - name: Dreamer's Idol
      pick_rate: 0.08
      win_rate: 0.6
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.3
    win_rate: 0.65
  - name: Sands Of Time
    pick_rate: 0.2
    win_rate: 0.52
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/poseidon/
  last_verified: '2026-08-27'
  god_win_rate: 0.5681818181818182
  god_matches_won: 75
  god_matches_played: 132
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
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - The World Stone
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
    this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Chronos'' Pendant,
    The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death, Doom Orb, Rod
    of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Bracer of The Abyss.'
  slot_scores:
    Nimble Ring:
      total: 0.57
      efficiency: 0.39
      win: 0.8
      pick: 0.25
      fit: 0.42
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.55
      pick: 0.58
      fit: 1.0
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.79
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.56
      pick: 0.27
      fit: 0.79
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.7
      pick: 0.62
      fit: 0.79
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.51
      win: 0.6
      pick: 0.25
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Nimble Ring
  - Ancient Signet
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - The World Stone
  - Ancient Signet
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
    Gem, Spear of the Magus, Death Metal, Gluttonous Grimoire, Ancient Signet, Chronos''
    Pendant, Bragi''s Harp, Gem of Focus, Polynomicon, Soul Reaver, The Cosmic Horror,
    Rod of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s Conch, Doom Orb,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm of Radiance,
    Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.39
      win: 0.8
      pick: 0.25
      fit: 0.29
    Ancient Signet:
      total: 0.51
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.55
      pick: 0.58
      fit: 0.61
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.47
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.27
      fit: 0.57
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.7
      pick: 0.62
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - The World Stone
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
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Chronos'' Pendant, Death
    Metal, Gem of Focus, The Cosmic Horror, Ancient Signet, Bragi''s Harp, Totem of
    Death, Doom Orb, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver,
    Jade Scepter, Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s
    Talon, Genji''s Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Nimble Ring:
      total: 0.54
      efficiency: 0.39
      win: 0.8
      pick: 0.25
      fit: 0.22
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.55
      pick: 0.58
      fit: 0.78
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.27
      fit: 0.56
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.7
      pick: 0.62
      fit: 0.56
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.25
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus,
    Shifter''s Shield, Genji''s Guard, Breastplate of Valor, Lifebinder, Helm of Radiance,
    Sphere of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale,
    Phoenix Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound
    Book, Glorious Pridwen, Doom Orb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.58
      fit: 0.49
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.7
      pick: 0.62
      fit: 0.39
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.89
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
  - The World Stone
  - Nimble Ring
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
    for this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, The Cosmic Horror,
    Chronos'' Pendant, Doom Orb, Ancient Signet, Gem of Focus, Rod of Asclepius, Totem
    of Death, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin,
    Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle, Wish-Granting
    Pearl, Typhon’s Heart, Breastplate of Valor, Bracer of The Abyss.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.39
      win: 0.8
      pick: 0.25
      fit: 0.3
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.55
      pick: 0.58
      fit: 1.0
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.85
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.56
      pick: 0.27
      fit: 0.85
    Rod of Tahuti:
      total: 0.77
      efficiency: 0.86
      win: 0.7
      pick: 0.62
      fit: 0.85
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.51
      win: 0.6
      pick: 0.25
      fit: 0.85
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
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Bracer
    of The Abyss, Chronos'' Pendant, Ancient Signet, Blood-Bound Book, Death Metal,
    Bancroft''s Talon, Gem of Focus, Rod of Asclepius, The Cosmic Horror, Typhon’s
    Heart, Polynomicon, Soul Reaver, Totem of Death, Jade Scepter, Divine Ruin, Helm
    of Radiance, Daybreak Gavel, Doom Orb.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.67
      efficiency: 0.65
      win: 0.8
      pick: 0.25
      fit: 0.48
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.55
      pick: 0.58
      fit: 0.4
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.7
      pick: 0.62
      fit: 0.32
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Gem of Focus
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Gem of Focus
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Gem of
    Focus, Spear of the Magus, Gluttonous Grimoire, Totem of Death, Breastplate of
    Valor, Genji''s Guard, Ancient Signet, Death Metal, Staff of Myrddin, The Cosmic
    Horror, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Chandra''s
    Grace, Freya''s Tears, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Doom Orb.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.63
    Gem of Focus:
      total: 0.52
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.55
      pick: 0.58
      fit: 0.86
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.7
      pick: 0.62
      fit: 0.37
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Spear of the
    Magus, Tyrfing, Heartseeker, Bragi''s Harp, Hydra''s Lament, Tekko-Kagi, Lernaean
    Bow, Death Metal, Titan''s Bane, Silverbranch Bow, The Crusher, Gluttonous Grimoire,
    Golden Blade, The Reaper, Pendulum Blade, Chronos'' Pendant, Arondight, Dominance,
    Avatar''s Parashu, Riptalon, Bracer of The Abyss, Ancient Signet, Transcendence,
    Runeforged Hammer, Toxic Blade, Gem of Focus, The Cosmic Horror, Avenging Blade,
    Triton''s Conch, Rod of Asclepius, Polynomicon, Totem of Death, Doom Orb.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.5
      pick: 0.18
      fit: 0.23
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.65
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.32
    Nimble Ring:
      total: 0.63
      efficiency: 0.6
      win: 0.8
      pick: 0.25
      fit: 0.35
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.55
      pick: 0.58
      fit: 0.55
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.7
      pick: 0.62
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Spear of the Magus
  - Dreamer's Idol
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Spear
    of the Magus, Heartseeker, Gluttonous Grimoire, Hydra''s Lament, Death Metal,
    Titan''s Bane, The Crusher, Chronos'' Pendant, The Reaper, Pendulum Blade, Bragi''s
    Harp, Ancient Signet, Tyrfing, Avatar''s Parashu, Arondight, Gem of Focus, The
    Cosmic Horror, Transcendence, Tekko-Kagi, Runeforged Hammer, Rod of Asclepius,
    Triton''s Conch, Polynomicon, Totem of Death, Avenging Blade, Blood-Bound Book,
    Soul Reaver, Doom Orb, Jade Scepter, Divine Ruin, Golden Blade, Silverbranch Bow,
    Bancroft''s Talon, Helm of Radiance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.69
    Nimble Ring:
      total: 0.55
      efficiency: 0.39
      win: 0.8
      pick: 0.25
      fit: 0.31
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.55
      pick: 0.58
      fit: 0.69
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.7
      pick: 0.62
      fit: 0.56
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.25
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
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
    Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom
    Orb, Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem
    of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin,
    Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.55
      pick: 0.58
      fit: 1.0
    Doom Orb:
      total: 0.5
      efficiency: 0.53
      win: 0.43
      pick: 0.05
      fit: 0.79
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.7
      pick: 0.62
      fit: 0.79
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.33
      pick: 0.28
      fit: 0.89
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 1.0
  starter: *id001
---
