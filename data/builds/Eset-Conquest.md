---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.23
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.42
    win_rate: 0.58
    alternates:
    - name: Book of Thoth
      pick_rate: 0.18
      win_rate: 0.47
    - name: Gauntlet of Thebes
      pick_rate: 0.07
      win_rate: 0.43
  - name: Book of Thoth
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.2
      win_rate: 0.58
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.7
  - name: Rod of Tahuti
    pick_rate: 0.22
    win_rate: 0.57
    alternates:
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.68
    - name: The World Stone
      pick_rate: 0.06
      win_rate: 0.7
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.23
      win_rate: 0.7
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.44
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.85
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.61
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.58
  - name: Killing Stone
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.67
    - name: Oracle Staff
      pick_rate: 0.06
      win_rate: 0.82
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.31
    win_rate: 0.58
  - name: Conduit Gem
    pick_rate: 0.24
    win_rate: 0.5
  - name: Pendulum of the Ages
    pick_rate: 0.12
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-11-02'
  god_win_rate: 0.550351288056206
  god_matches_won: 235
  god_matches_played: 427
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
  - Obsidian Shard
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
    this god: Soul Gem, Doom Orb, The World Stone, Spear of the Magus, Gluttonous
    Grimoire, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Heartwood Charm,
    Gem of Focus, Totem of Death, Ancient Signet, Polynomicon, Blood-Bound Book, Soul
    Reaver, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Typhon’s Heart, Rod of Asclepius, Genji''s Guard, Bracer
    of The Abyss, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.56
      win: 0.58
      pick: 0.42
      fit: 1.0
    Doom Orb:
      total: 0.61
      efficiency: 0.51
      win: 0.7
      pick: 0.12
      fit: 0.77
    The World Stone:
      total: 0.61
      efficiency: 0.5
      win: 0.7
      pick: 0.09
      fit: 0.77
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.81
      win: 0.57
      pick: 0.34
      fit: 0.77
    Obsidian Shard:
      total: 0.6
      efficiency: 0.55
      win: 0.58
      pick: 0.27
      fit: 0.87
    Soul Gem:
      total: 0.64
      efficiency: 0.5
      win: 0.68
      pick: 0.12
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
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
    Gem, Doom Orb, The World Stone, Sundering Echo, Death Metal, Spear of the Magus,
    Gluttonous Grimoire, Chronos'' Pendant, Heartwood Charm, Ancient Signet, Polynomicon,
    Dreamer''s Idol, Bragi''s Harp, Gem of Focus, Soul Reaver, The Cosmic Horror,
    Blood-Bound Book, Bancroft''s Talon, Totem of Death, Triton''s Conch, Divine Ruin,
    Jade Scepter, Genji''s Guard, Helm of Radiance, Ethereal Staff, Breastplate of
    Valor.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.56
      win: 0.58
      pick: 0.42
      fit: 0.61
    Doom Orb:
      total: 0.58
      efficiency: 0.51
      win: 0.7
      pick: 0.12
      fit: 0.57
    The World Stone:
      total: 0.58
      efficiency: 0.5
      win: 0.7
      pick: 0.09
      fit: 0.57
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.81
      win: 0.57
      pick: 0.34
      fit: 0.57
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.58
      pick: 0.27
      fit: 0.57
    Soul Gem:
      total: 0.59
      efficiency: 0.5
      win: 0.68
      pick: 0.12
      fit: 0.71
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Doom Orb, The World Stone, Spear of the Magus, Gluttonous Grimoire,
    Sundering Echo, Chronos'' Pendant, Dreamer''s Idol, Death Metal, The Cosmic Horror,
    Heartwood Charm, Gem of Focus, Totem of Death, Ancient Signet, Polynomicon, Bragi''s
    Harp, Blood-Bound Book, Soul Reaver, Genji''s Guard, Damaru, Divine Ruin, Jade
    Scepter, Triton''s Conch, Bancroft''s Talon, Breastplate of Valor, Chandra''s
    Grace.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.22
    Spear of Desolation:
      total: 0.59
      efficiency: 0.56
      win: 0.58
      pick: 0.42
      fit: 0.78
    Doom Orb:
      total: 0.58
      efficiency: 0.51
      win: 0.7
      pick: 0.12
      fit: 0.56
    The World Stone:
      total: 0.58
      efficiency: 0.5
      win: 0.7
      pick: 0.09
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.81
      win: 0.57
      pick: 0.34
      fit: 0.56
    Soul Gem:
      total: 0.62
      efficiency: 0.5
      win: 0.68
      pick: 0.12
      fit: 0.88
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - The World Stone
  - Book of Thoth
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
    this god: Soul Gem, Amanita Charm, Shield of the Phoenix, Doom Orb, The World
    Stone, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Phoenix
    Feather, Yogi''s Necklace, Breastplate of Valor, Blood-Bound Book, Rod of Asclepius,
    Chandra''s Grace, Sphere of Negation, Helm of Radiance, Spear of the Magus, Helm
    of Darkness, Erosion, Oni Hunter''s Garb, Eye of Providence, Draconic Scale, Jade
    Scepter, Glorious Pridwen, Midgardian Mail, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.2
    Doom Orb:
      total: 0.56
      efficiency: 0.51
      win: 0.7
      pick: 0.12
      fit: 0.38
    The World Stone:
      total: 0.55
      efficiency: 0.5
      win: 0.7
      pick: 0.09
      fit: 0.38
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.81
      win: 0.57
      pick: 0.34
      fit: 0.38
    Amanita Charm:
      total: 0.61
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.62
      efficiency: 0.5
      win: 0.68
      pick: 0.12
      fit: 0.9
  community_ordered:
  - Book of Thoth
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
  - Obsidian Shard
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
    for this god: Soul Gem, Doom Orb, The World Stone, Spear of the Magus, Gluttonous
    Grimoire, Dreamer''s Idol, The Cosmic Horror, Chronos'' Pendant, Heartwood Charm,
    Gem of Focus, Ancient Signet, Polynomicon, Blood-Bound Book, Totem of Death, Soul
    Reaver, Divine Ruin, Jade Scepter, Bancroft''s Talon, Screeching Gargoyle, Helm
    of Radiance, Ethereal Staff, Genji''s Guard, Typhon’s Heart, Rod of Asclepius,
    Staff of Myrddin, Breastplate of Valor.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.56
      win: 0.58
      pick: 0.42
      fit: 1.0
    Doom Orb:
      total: 0.62
      efficiency: 0.51
      win: 0.7
      pick: 0.12
      fit: 0.84
    The World Stone:
      total: 0.62
      efficiency: 0.5
      win: 0.7
      pick: 0.09
      fit: 0.84
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.81
      win: 0.57
      pick: 0.34
      fit: 0.84
    Obsidian Shard:
      total: 0.61
      efficiency: 0.55
      win: 0.58
      pick: 0.27
      fit: 0.94
    Soul Gem:
      total: 0.64
      efficiency: 0.5
      win: 0.68
      pick: 0.12
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Doom Orb
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
    this god: Soul Gem, Nimble Ring, Doom Orb, The World Stone, Gluttonous Grimoire,
    Sundering Echo, Bragi''s Harp, Spear of the Magus, Blood-Bound Book, Bracer of
    The Abyss, Chronos'' Pendant, Eros'' Bow, Death Metal, Dreamer''s Idol, Bancroft''s
    Talon, Heartwood Charm, Gem of Focus, Ancient Signet, Polynomicon, The Cosmic
    Horror, Typhon’s Heart, Soul Reaver, Totem of Death, Divine Ruin, Jade Scepter,
    Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.51
      efficiency: 0.41
      win: 0.6
      pick: 0.0
      fit: 0.62
    Doom Orb:
      total: 0.55
      efficiency: 0.51
      win: 0.7
      pick: 0.12
      fit: 0.31
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.81
      win: 0.57
      pick: 0.34
      fit: 0.31
    Soul Gem:
      total: 0.59
      efficiency: 0.55
      win: 0.68
      pick: 0.12
      fit: 0.58
  community_ordered:
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The World Stone
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
    + fit + win/pick). Underrated for this god: Soul Gem, Doom Orb, The World Stone,
    Chronos'' Pendant, Heartwood Charm, Gem of Focus, Spear of the Magus, Totem of
    Death, Gluttonous Grimoire, Sundering Echo, Genji''s Guard, Damaru, Breastplate
    of Valor, Chandra''s Grace, Dreamer''s Idol, Death Metal, The Cosmic Horror, Staff
    of Myrddin, Ancient Signet, Polynomicon, Blood-Bound Book, Screeching Gargoyle,
    Eye of Erebus, Bragi''s Harp, Soul Reaver, Freya''s Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.61
      efficiency: 0.56
      win: 0.58
      pick: 0.42
      fit: 0.86
    Doom Orb:
      total: 0.55
      efficiency: 0.51
      win: 0.7
      pick: 0.12
      fit: 0.37
    The World Stone:
      total: 0.55
      efficiency: 0.5
      win: 0.7
      pick: 0.09
      fit: 0.37
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.57
      pick: 0.34
      fit: 0.37
    Soul Gem:
      total: 0.63
      efficiency: 0.5
      win: 0.68
      pick: 0.12
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Doom Orb
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Doom Orb, The
    World Stone, Tekko-Kagi, Sundering Echo, Titan''s Bane, Hydra''s Lament, Tyrfing,
    Bragi''s Harp, Death Metal, Spear of the Magus, Heartseeker, The Crusher, Nimble
    Ring, Gluttonous Grimoire, Lernaean Bow, The Reaper, Silverbranch Bow, Golden
    Blade, Arondight, Chronos'' Pendant, Pendulum Blade, Dominance, Dreamer''s Idol,
    Toxic Blade, Bracer of The Abyss, Transcendence, Heartwood Charm, The Cosmic Horror,
    Gem of Focus, Avatar''s Parashu, Runeforged Hammer, Ancient Signet, Eros'' Bow,
    Polynomicon, Blood-Bound Book, Riptalon, Avenging Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.22
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.65
    Transcendence:
      total: 0.49
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.32
    Doom Orb:
      total: 0.56
      efficiency: 0.51
      win: 0.7
      pick: 0.12
      fit: 0.43
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.81
      win: 0.57
      pick: 0.34
      fit: 0.43
    Soul Gem:
      total: 0.59
      efficiency: 0.5
      win: 0.68
      pick: 0.12
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: str-int
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Doom
    Orb, The World Stone, Sundering Echo, Titan''s Bane, Spear of the Magus, Death
    Metal, Gluttonous Grimoire, Hydra''s Lament, Heartseeker, The Crusher, Chronos''
    Pendant, The Reaper, Dreamer''s Idol, Pendulum Blade, Arondight, Tekko-Kagi, The
    Cosmic Horror, Bragi''s Harp, Heartwood Charm, Gem of Focus, Tyrfing, Ancient
    Signet, Polynomicon, Blood-Bound Book, Avatar''s Parashu, Transcendence, Totem
    of Death, Runeforged Hammer, Soul Reaver, Triton''s Conch, Divine Ruin, Jade Scepter,
    Avenging Blade, Eye of the Storm, Bancroft''s Talon, Golden Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.3
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.42
      fit: 0.7
    Transcendence:
      total: 0.49
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.3
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.81
      win: 0.57
      pick: 0.34
      fit: 0.55
    Soul Gem:
      total: 0.61
      efficiency: 0.5
      win: 0.68
      pick: 0.12
      fit: 0.8
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
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
  - Spear of the Magus
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
    Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Heartwood
    Charm, Gem of Focus, Totem of Death, Ancient Signet, Polynomicon, Blood-Bound
    Book, Soul Reaver, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Typhon’s Heart, Rod of Asclepius, Genji''s Guard,
    Bracer of The Abyss, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.56
      win: 0.58
      pick: 0.42
      fit: 1.0
    Doom Orb:
      total: 0.61
      efficiency: 0.51
      win: 0.7
      pick: 0.12
      fit: 0.77
    Spear of the Magus:
      total: 0.57
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.81
      win: 0.57
      pick: 0.34
      fit: 0.77
    Obsidian Shard:
      total: 0.6
      efficiency: 0.55
      win: 0.58
      pick: 0.27
      fit: 0.87
    Soul Gem:
      total: 0.64
      efficiency: 0.5
      win: 0.68
      pick: 0.12
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
---
