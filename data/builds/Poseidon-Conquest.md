---
type: smite-build
god: Poseidon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Trident
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.57
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.48
    win_rate: 0.6
    alternates:
    - name: Book of Thoth
      pick_rate: 0.19
      win_rate: 0.59
    - name: Doom Orb
      pick_rate: 0.07
      win_rate: 0.56
  - name: The World Stone
    pick_rate: 0.3
    win_rate: 0.59
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.21
      win_rate: 0.59
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.57
  - name: Rod of Tahuti
    pick_rate: 0.26
    win_rate: 0.59
    alternates:
    - name: Nimble Ring
      pick_rate: 0.21
      win_rate: 0.67
    - name: The World Stone
      pick_rate: 0.08
      win_rate: 0.58
  - name: Nimble Ring
    pick_rate: 0.19
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.28
      win_rate: 0.67
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.55
  - name: Obsidian Shard
    pick_rate: 0.17
    win_rate: 0.63
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.64
    - name: Nimble Ring
      pick_rate: 0.1
      win_rate: 0.71
  - name: Evil Eye
    pick_rate: 0.1
    win_rate: 0.48
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.78
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.74
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.3
    win_rate: 0.68
  - name: Archmage's Gem
    pick_rate: 0.21
    win_rate: 0.61
  - name: Sands Of Time
    pick_rate: 0.15
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/poseidon/
  last_verified: '2026-11-02'
  god_win_rate: 0.5813366960907944
  god_matches_won: 461
  god_matches_played: 793
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Dreamer''s Idol,
    Doom Orb, Lotus Sickle, Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Polynomicon, Ancient Signet, Totem of Death, Soul Reaver,
    Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Staff of Myrddin, Typhon’s Heart, Rod of Asclepius, Bracer of The Abyss, Alchemist
    Coat.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.5
      win: 0.59
      pick: 0.19
      fit: 0.42
    Spear of Desolation:
      total: 0.65
      efficiency: 0.59
      win: 0.6
      pick: 0.48
      fit: 1.0
    The World Stone:
      total: 0.59
      efficiency: 0.53
      win: 0.59
      pick: 0.41
      fit: 0.79
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.87
      win: 0.59
      pick: 0.4
      fit: 0.79
    Obsidian Shard:
      total: 0.64
      efficiency: 0.58
      win: 0.63
      pick: 0.37
      fit: 0.89
    Soul Gem:
      total: 0.6
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Lotus Sickle
  - Spear of Desolation
  - Book of Thoth
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
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
    Gem, Lotus Sickle, Death Metal, Spear of the Magus, Doom Orb, Gluttonous Grimoire,
    Chronos'' Pendant, Heartwood Charm, Polynomicon, Dreamer''s Idol, Ancient Signet,
    Bragi''s Harp, Gem of Focus, Soul Reaver, Blood-Bound Book, The Cosmic Horror,
    Bancroft''s Talon, Triton''s Conch, Totem of Death, Divine Ruin, Jade Scepter,
    Genji''s Guard, Helm of Radiance, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Lotus Sickle:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.59
      efficiency: 0.59
      win: 0.6
      pick: 0.48
      fit: 0.61
    Book of Thoth:
      total: 0.51
      efficiency: 0.5
      win: 0.59
      pick: 0.19
      fit: 0.39
    The World Stone:
      total: 0.56
      efficiency: 0.53
      win: 0.59
      pick: 0.41
      fit: 0.57
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.87
      win: 0.59
      pick: 0.4
      fit: 0.57
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.63
      pick: 0.37
      fit: 0.57
  community_ordered:
  - Spear of Desolation
  - Book of Thoth
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Lotus Sickle, Dreamer''s
    Idol, Doom Orb, Chronos'' Pendant, Death Metal, The Cosmic Horror, Gem of Focus,
    Heartwood Charm, Bragi''s Harp, Blood-Bound Book, Polynomicon, Ancient Signet,
    Totem of Death, Soul Reaver, Damaru, Divine Ruin, Jade Scepter, Genji''s Guard,
    Triton''s Conch, Bancroft''s Talon, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.59
      pick: 0.19
      fit: 0.22
    Spear of Desolation:
      total: 0.62
      efficiency: 0.59
      win: 0.6
      pick: 0.48
      fit: 0.78
    The World Stone:
      total: 0.55
      efficiency: 0.53
      win: 0.59
      pick: 0.41
      fit: 0.56
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.87
      win: 0.59
      pick: 0.4
      fit: 0.56
    Obsidian Shard:
      total: 0.6
      efficiency: 0.58
      win: 0.63
      pick: 0.37
      fit: 0.66
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Blood-Bound Book, Phoenix Feather,
    Rod of Asclepius, Freya''s Tears, Helm of Radiance, Yogi''s Necklace, Sphere of
    Negation, Helm of Darkness, Spear of the Magus, Breastplate of Valor, Erosion,
    Oni Hunter''s Garb, Chandra''s Grace, Eye of Providence, Jade Scepter, Draconic
    Scale, Lotus Sickle, Midgardian Mail, Doom Orb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.58
      efficiency: 0.59
      win: 0.6
      pick: 0.48
      fit: 0.49
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.87
      win: 0.59
      pick: 0.4
      fit: 0.39
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.63
      pick: 0.37
      fit: 0.49
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
  - Spear of the Magus
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
    for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Dreamer''s Idol,
    Doom Orb, The Cosmic Horror, Lotus Sickle, Chronos'' Pendant, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Polynomicon, Ancient Signet, Soul Reaver, Totem of Death,
    Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Screeching Gargoyle, Typhon’s Heart, Rod of Asclepius, Genji''s Guard, Staff of
    Myrddin.'
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.59
      win: 0.6
      pick: 0.48
      fit: 1.0
    Spear of the Magus:
      total: 0.6
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.85
    The World Stone:
      total: 0.6
      efficiency: 0.53
      win: 0.59
      pick: 0.41
      fit: 0.85
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.87
      win: 0.59
      pick: 0.4
      fit: 0.85
    Obsidian Shard:
      total: 0.65
      efficiency: 0.58
      win: 0.63
      pick: 0.37
      fit: 0.95
    Soul Gem:
      total: 0.6
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Bragi's Harp
  - Nimble Ring
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
    this god: Soul Gem, Gluttonous Grimoire, Bragi''s Harp, Spear of the Magus, Blood-Bound
    Book, Bracer of The Abyss, Lotus Sickle, Death Metal, Eros'' Bow, Chronos'' Pendant,
    Dreamer''s Idol, Doom Orb, Bancroft''s Talon, Polynomicon, Gem of Focus, Ancient
    Signet, Heartwood Charm, The Cosmic Horror, Typhon’s Heart, Soul Reaver, Divine
    Ruin, Jade Scepter, Totem of Death, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.48
      fit: 0.4
    Bragi's Harp:
      total: 0.52
      efficiency: 0.45
      win: 0.59
      pick: 0.0
      fit: 0.63
    Nimble Ring:
      total: 0.57
      efficiency: 0.63
      win: 0.58
      pick: 0.32
      fit: 0.48
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.87
      win: 0.59
      pick: 0.4
      fit: 0.32
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.63
      pick: 0.37
      fit: 0.42
  community_ordered:
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Lotus Sickle
  - Spear of Desolation
  - Chronos' Pendant
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Lotus Sickle
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
    + fit + win/pick). Underrated for this god: Soul Gem, Lotus Sickle, Chronos''
    Pendant, Gem of Focus, Heartwood Charm, Spear of the Magus, Totem of Death, Gluttonous
    Grimoire, Damaru, Genji''s Guard, Death Metal, Dreamer''s Idol, Doom Orb, Breastplate
    of Valor, Chandra''s Grace, The Cosmic Horror, Staff of Myrddin, Blood-Bound Book,
    Polynomicon, Ancient Signet, Eye of Erebus, Bragi''s Harp, Screeching Gargoyle,
    Soul Reaver, Freya''s Tears.'
  slot_scores:
    Lotus Sickle:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.63
      efficiency: 0.59
      win: 0.6
      pick: 0.48
      fit: 0.86
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.87
      win: 0.59
      pick: 0.4
      fit: 0.37
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.63
      pick: 0.37
      fit: 0.47
    Soul Gem:
      total: 0.59
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Tekko-Kagi
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Tekko-Kagi
  - Soul Gem
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Tekko-Kagi, Titan''s Bane,
    Soul Gem, Tyrfing, Hydra''s Lament, Death Metal, Bragi''s Harp, Spear of the Magus,
    The Crusher, Heartseeker, Lernaean Bow, The Reaper, Golden Blade, Silverbranch
    Bow, Gluttonous Grimoire, Arondight, Lotus Sickle, Dominance, Dreamer''s Idol,
    Doom Orb, Chronos'' Pendant, Pendulum Blade, Avatar''s Parashu, Toxic Blade, Bracer
    of The Abyss, Transcendence, Runeforged Hammer, Gem of Focus, The Cosmic Horror,
    Heartwood Charm, Eros'' Bow, Blood-Bound Book, Polynomicon, Ancient Signet, Riptalon,
    Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.67
      win: 0.59
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.58
      efficiency: 0.59
      win: 0.6
      pick: 0.48
      fit: 0.55
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.59
      pick: 0.4
      fit: 0.44
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.63
      pick: 0.37
      fit: 0.54
    Soul Gem:
      total: 0.55
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Titan''s
    Bane, Spear of the Magus, Death Metal, Hydra''s Lament, Gluttonous Grimoire, The
    Crusher, Heartseeker, Lotus Sickle, The Reaper, Dreamer''s Idol, Doom Orb, Chronos''
    Pendant, Arondight, Tyrfing, Tekko-Kagi, Bragi''s Harp, Pendulum Blade, The Cosmic
    Horror, Gem of Focus, Heartwood Charm, Avatar''s Parashu, Blood-Bound Book, Polynomicon,
    Ancient Signet, Transcendence, Runeforged Hammer, Triton''s Conch, Soul Reaver,
    Totem of Death, Avenging Blade, Divine Ruin, Jade Scepter, Golden Blade, Shield
    Splitter, Eye of the Storm.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.5
      win: 0.59
      pick: 0.19
      fit: 0.31
    Spear of Desolation:
      total: 0.61
      efficiency: 0.59
      win: 0.6
      pick: 0.48
      fit: 0.69
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.59
      pick: 0.0
      fit: 0.69
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.31
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.87
      win: 0.59
      pick: 0.4
      fit: 0.56
    Obsidian Shard:
      total: 0.6
      efficiency: 0.58
      win: 0.63
      pick: 0.37
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
    Orb, Dreamer''s Idol, Lotus Sickle, Chronos'' Pendant, The Cosmic Horror, Gem
    of Focus, Heartwood Charm, Blood-Bound Book, Polynomicon, Ancient Signet, Totem
    of Death, Soul Reaver, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Typhon’s Heart, Rod of Asclepius, Bracer of
    The Abyss, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.59
      win: 0.6
      pick: 0.48
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.54
      win: 0.56
      pick: 0.07
      fit: 0.79
    Spear of the Magus:
      total: 0.59
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.87
      win: 0.59
      pick: 0.4
      fit: 0.79
    Obsidian Shard:
      total: 0.64
      efficiency: 0.58
      win: 0.63
      pick: 0.37
      fit: 0.89
    Soul Gem:
      total: 0.6
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
