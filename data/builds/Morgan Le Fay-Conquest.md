---
type: smite-build
god: Morgan Le Fay
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cursed Crown
  aspect_pick_rate: 0.33
  aspect_win_rate: 0.45
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.35
    win_rate: 0.5
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.13
      win_rate: 0.46
    - name: Lifebinder
      pick_rate: 0.11
      win_rate: 0.49
  - name: The World Stone
    pick_rate: 0.1
    win_rate: 0.42
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.49
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.55
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.48
    alternates:
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.54
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.44
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.51
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.2
      win_rate: 0.47
    - name: Spear of the Magus
      pick_rate: 0.06
      win_rate: 0.52
  - name: Ethereal Staff
    pick_rate: 0.07
    win_rate: 0.58
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.41
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.53
  - name: Void Shard
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.56
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.73
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.38
    win_rate: 0.51
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.42
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/morgan-le-fay/
  last_verified: '2026-11-02'
  god_win_rate: 0.475
  god_matches_won: 228
  god_matches_played: 480
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
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Soul Reaver
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Helm of Darkness — magical protection
    swap_item: Helm of Darkness
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    The Cosmic Horror, Chronos'' Pendant, Gem of Focus, The World Stone, Heartwood
    Charm, Ancient Signet, Blood-Bound Book, Polynomicon, Totem of Death, Book of
    Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Staff of
    Myrddin, Typhon’s Heart, Rod of Asclepius, Bracer of The Abyss, Wish-Granting
    Pearl.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 1.0
    Spear of the Magus:
      total: 0.56
      efficiency: 0.58
      win: 0.52
      pick: 0.1
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.89
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.79
    Soul Reaver:
      total: 0.58
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.62
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, Death Metal, Doom Orb, Gluttonous Grimoire, Heartwood Charm, Ancient
    Signet, Polynomicon, Dreamer''s Idol, Bragi''s Harp, Chronos'' Pendant, Gem of
    Focus, The World Stone, Book of Thoth, Blood-Bound Book, The Cosmic Horror, Bancroft''s
    Talon, Totem of Death, Triton''s Conch, Divine Ruin, Jade Scepter, Helm of Radiance,
    Wish-Granting Pearl, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.61
    Doom Orb:
      total: 0.5
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.57
    Obsidian Shard:
      total: 0.53
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.57
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.57
    Soul Reaver:
      total: 0.57
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.59
    Soul Gem:
      total: 0.54
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.71
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol, Death
    Metal, Chronos'' Pendant, Gem of Focus, The Cosmic Horror, Heartwood Charm, The
    World Stone, Ancient Signet, Bragi''s Harp, Blood-Bound Book, Polynomicon, Totem
    of Death, Book of Thoth, Divine Ruin, Jade Scepter, Damaru, Triton''s Conch, Bancroft''s
    Talon, Helm of Radiance, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.78
    Spear of the Magus:
      total: 0.52
      efficiency: 0.58
      win: 0.52
      pick: 0.1
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.66
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.56
    Soul Reaver:
      total: 0.55
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.42
    Soul Gem:
      total: 0.57
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.88
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - Obsidian Shard
  - Soul Reaver
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire, Kinetic Cuirass,
    Spear of the Magus, Phoenix Feather, Blood-Bound Book, Freya''s Tears, Helm of
    Radiance, Yogi''s Necklace, Rod of Asclepius, Sphere of Negation, Breastplate
    of Valor, Helm of Darkness, Erosion, Genji''s Guard, Chandra''s Grace, Eye of
    Providence, Jade Scepter, Draconic Scale, Oni Hunter''s Garb, Doom Orb, Midgardian
    Mail, The World Stone.'
  slot_scores:
    Spear of Desolation:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.49
    Obsidian Shard:
      total: 0.52
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.49
    Soul Reaver:
      total: 0.54
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.41
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.57
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Soul Reaver
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Soul Reaver
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
    for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    The Cosmic Horror, The World Stone, Chronos'' Pendant, Gem of Focus, Heartwood
    Charm, Ancient Signet, Blood-Bound Book, Polynomicon, Totem of Death, Book of
    Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Screeching
    Gargoyle, Typhon’s Heart, Rod of Asclepius, Staff of Myrddin, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 1.0
    Spear of the Magus:
      total: 0.57
      efficiency: 0.58
      win: 0.52
      pick: 0.1
      fit: 0.85
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.95
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.85
    Soul Reaver:
      total: 0.56
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.5
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Reaver
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Blood-Bound Book, Bracer of The Abyss, Doom Orb, Death Metal, Eros'' Bow, Dreamer''s
    Idol, Ancient Signet, Bancroft''s Talon, Chronos'' Pendant, Polynomicon, Gem of
    Focus, Heartwood Charm, The Cosmic Horror, Typhon’s Heart, Book of Thoth, The
    World Stone, Divine Ruin, Jade Scepter, Totem of Death, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.45
      win: 0.51
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.32
    Soul Reaver:
      total: 0.54
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.37
    Soul Gem:
      total: 0.54
      efficiency: 0.58
      win: 0.54
      pick: 0.16
      fit: 0.58
  community_ordered:
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Heartwood
    Charm, Spear of the Magus, Totem of Death, Gluttonous Grimoire, Doom Orb, Damaru,
    Death Metal, Dreamer''s Idol, Breastplate of Valor, Chandra''s Grace, The Cosmic
    Horror, Genji''s Guard, Staff of Myrddin, Ancient Signet, Blood-Bound Book, Polynomicon,
    The World Stone, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Book of Thoth,
    Freya''s Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.5
      efficiency: 0.55
      win: 0.46
      pick: 0.13
      fit: 0.63
    Spear of Desolation:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.86
    Obsidian Shard:
      total: 0.51
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.47
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.37
    Soul Reaver:
      total: 0.53
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.34
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.96
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
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
    Tyrfing, Spear of the Magus, Hydra''s Lament, Bragi''s Harp, Death Metal, The
    Crusher, Heartseeker, Lernaean Bow, The Reaper, Nimble Ring, Gluttonous Grimoire,
    Silverbranch Bow, Golden Blade, Arondight, Doom Orb, Dominance, Dreamer''s Idol,
    Pendulum Blade, Avatar''s Parashu, Transcendence, Bracer of The Abyss, Toxic Blade,
    Runeforged Hammer, Chronos'' Pendant, Gem of Focus, The Cosmic Horror, Ancient
    Signet, Heartwood Charm, Blood-Bound Book, Polynomicon, Eros'' Bow, Avenging Blade,
    The World Stone, Riptalon, Triton''s Conch.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.55
    Obsidian Shard:
      total: 0.52
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.54
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.44
    Soul Reaver:
      total: 0.55
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.43
    Soul Gem:
      total: 0.53
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.65
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Soul Reaver
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Spear of the Magus,
    Titan''s Bane, Death Metal, Hydra''s Lament, Gluttonous Grimoire, Doom Orb, The
    Crusher, Heartseeker, The Reaper, Dreamer''s Idol, Arondight, Tekko-Kagi, Bragi''s
    Harp, Pendulum Blade, Tyrfing, The Cosmic Horror, Chronos'' Pendant, Gem of Focus,
    Avatar''s Parashu, Heartwood Charm, Ancient Signet, Blood-Bound Book, Polynomicon,
    The World Stone, Transcendence, Runeforged Hammer, Triton''s Conch, Book of Thoth,
    Totem of Death, Avenging Blade, Divine Ruin, Jade Scepter, Eye of the Storm, Shield
    Splitter, Golden Blade, Bancroft''s Talon.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.69
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.31
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.56
    Soul Reaver:
      total: 0.56
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.51
    Soul Gem:
      total: 0.55
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.79
  community_ordered:
  - Rod of Tahuti
  - Soul Reaver
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, The
    World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Gem of Focus,
    Heartwood Charm, Ancient Signet, Blood-Bound Book, Polynomicon, Totem of Death,
    Book of Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance,
    Staff of Myrddin, Typhon’s Heart, Rod of Asclepius, Bracer of The Abyss, Wish-Granting
    Pearl.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 1.0
    Doom Orb:
      total: 0.54
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.58
      win: 0.52
      pick: 0.1
      fit: 0.79
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.89
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Ethereal Staff
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
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
    this god: Gluttonous Grimoire, Spear of the Magus, Amanita Charm, Jade Scepter,
    Rod of Asclepius, Yogi''s Necklace, Doom Orb, Chandra''s Grace, Phoenix Feather,
    Oni Hunter''s Garb, Genji''s Guard, Blood-Bound Book, Wish-Granting Pearl, Dreamer''s
    Idol, Sphere of Negation, Ancile, Alchemist Coat, Screeching Gargoyle, Void Stone,
    Lifebinder, Kinetic Cuirass, Chronos'' Pendant, The Cosmic Horror, The World Stone.'
  slot_scores:
    Ethereal Staff:
      total: 0.55
      efficiency: 0.47
      win: 0.58
      pick: 0.15
      fit: 0.79
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.62
    Obsidian Shard:
      total: 0.53
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.57
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.47
    Soul Reaver:
      total: 0.55
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.42
    Soul Gem:
      total: 0.57
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.92
  community_ordered:
  - Ethereal Staff
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: mana-stack
  slot_order:
  - Yogi's Necklace
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Reaver
  flex_slots:
  - Yogi's Necklace
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Spear of the Magus, Death Metal, Amanita Charm, Yogi''s Necklace, Doom
    Orb, Blood-Bound Book, Genji''s Guard, Jade Scepter, Wish-Granting Pearl, Chandra''s
    Grace, Triton''s Conch, Rod of Asclepius, Oni Hunter''s Garb, Ancient Signet,
    Bancroft''s Talon, Heartwood Charm, Sphere of Negation, Polynomicon, Phoenix Feather,
    Dreamer''s Idol, Chronos'' Pendant, Gem of Focus, The World Stone.'
  slot_scores:
    Yogi's Necklace:
      total: 0.48
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.44
    Book of Thoth:
      total: 0.45
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.48
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.44
    Obsidian Shard:
      total: 0.51
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.47
    Soul Reaver:
      total: 0.56
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Reaver
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Spear of the Magus, Amanita Charm, Doom Orb, Genji''s
    Guard, Blood-Bound Book, Chandra''s Grace, Yogi''s Necklace, Death Metal, Jade
    Scepter, Dreamer''s Idol, Rod of Asclepius, Phoenix Feather, Screeching Gargoyle,
    Oni Hunter''s Garb, Triton''s Conch, Sphere of Negation, Wish-Granting Pearl,
    Chronos'' Pendant, Gem of Focus, Heartwood Charm, The Cosmic Horror, Ancient Signet,
    The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.17
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.59
    Obsidian Shard:
      total: 0.52
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.52
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.42
    Soul Reaver:
      total: 0.54
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.37
    Soul Gem:
      total: 0.57
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Gluttonous Grimoire,
    Phoenix Feather, Freya''s Tears, Yogi''s Necklace, Spear of the Magus, Breastplate
    of Valor, Blood-Bound Book, Helm of Radiance, Erosion, Rod of Asclepius, Sphere
    of Negation, Helm of Darkness, Eye of Providence, Chandra''s Grace, Genji''s Guard,
    Draconic Scale, Oni Hunter''s Garb, Midgardian Mail, Jade Scepter, Shifter''s
    Shield, Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.47
    Soul Reaver:
      total: 0.54
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.36
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.83
    Soul Gem:
      total: 0.56
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.87
  community_ordered:
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Soul Reaver
  - Spear of the Magus
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
    for this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, Screeching Gargoyle,
    Amanita Charm, Void Stone, Dreamer''s Idol, Yogi''s Necklace, The Cosmic Horror,
    Jade Scepter, Blood-Bound Book, Rod of Asclepius, Genji''s Guard, Phoenix Feather,
    Chandra''s Grace, Oni Hunter''s Garb, The World Stone, Wish-Granting Pearl, Sphere
    of Negation, Ancile, Chronos'' Pendant, Kinetic Cuirass, Gem of Focus, Lifebinder.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.7
    Spear of the Magus:
      total: 0.53
      efficiency: 0.58
      win: 0.52
      pick: 0.1
      fit: 0.59
    Obsidian Shard:
      total: 0.55
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.69
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.59
    Soul Reaver:
      total: 0.54
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.37
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Soul Reaver
  - Rod of Tahuti
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
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Blood-Bound Book, Amanita Charm, Eros''
    Bow, Spear of the Magus, Yogi''s Necklace, Bancroft''s Talon, Bragi''s Harp, Genji''s
    Guard, Bracer of The Abyss, Phoenix Feather, Jade Scepter, Oni Hunter''s Garb,
    Chandra''s Grace, Rod of Asclepius, Death Metal, Doom Orb, Sphere of Negation,
    Screeching Gargoyle, Wish-Granting Pearl, Dreamer''s Idol, Chronos'' Pendant,
    The World Stone.'
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.37
    Bragi's Harp:
      total: 0.46
      efficiency: 0.45
      win: 0.51
      pick: 0.0
      fit: 0.51
    Soul Reaver:
      total: 0.53
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.31
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.23
    Eros' Bow:
      total: 0.48
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.55
      efficiency: 0.58
      win: 0.54
      pick: 0.16
      fit: 0.67
  community_ordered:
  - Soul Reaver
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Book of Thoth
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Chandra''s Grace,
    Gluttonous Grimoire, Screeching Gargoyle, Amanita Charm, Spear of the Magus, Chronos''
    Pendant, Gem of Focus, Yogi''s Necklace, Heartwood Charm, Eye of Erebus, Shield
    of the Phoenix, Phoenix Feather, Blood-Bound Book, Oni Hunter''s Garb, Jade Scepter,
    Rod of Asclepius, Doom Orb, Freya''s Tears, Totem of Death, Death Metal, Damaru,
    Wish-Granting Pearl, The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.11
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.64
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.44
      pick: 0.12
      fit: 0.43
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.28
    Soul Reaver:
      total: 0.53
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.31
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.94
  community_ordered:
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Golden Blade, Runeforged
    Hammer, Gluttonous Grimoire, Tekko-Kagi, The Reaper, Titan''s Bane, Hydra''s Lament,
    Tyrfing, Amanita Charm, Spear of the Magus, Avenging Blade, The Crusher, Toxic
    Blade, Death Metal, Heartseeker, Lernaean Bow, Bragi''s Harp, Yogi''s Necklace,
    Eros'' Bow, Arondight, Nimble Ring, Blood-Bound Book, Silverbranch Bow, Triton''s
    Conch, Genji''s Guard, Jade Scepter, Phoenix Feather, Shield Splitter, Doom Orb,
    Rod of Asclepius, Chandra''s Grace, Oni Hunter''s Garb, Riptalon, Dominance, Berserker''s
    Shield, The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.14
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.52
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.26
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.31
    Soul Reaver:
      total: 0.53
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.34
    Soul Gem:
      total: 0.54
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.7
  community_ordered:
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire,
    Runeforged Hammer, Spear of the Magus, The Reaper, Titan''s Bane, Amanita Charm,
    Hydra''s Lament, Death Metal, Blood-Bound Book, Jade Scepter, Avenging Blade,
    Triton''s Conch, Doom Orb, The Crusher, Rod of Asclepius, Heartseeker, Yogi''s
    Necklace, Genji''s Guard, Wish-Granting Pearl, Dreamer''s Idol, Phoenix Feather,
    Arondight, Sphere of Negation, Golden Blade, Chandra''s Grace, Oni Hunter''s Garb,
    Shield Splitter, Wyrmskin Hide, Tyrfing, Tekko-Kagi, Bragi''s Harp, Chronos''
    Pendant, Ancient Signet, Bancroft''s Talon, Gem of Focus, The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.51
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.23
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.41
    Soul Reaver:
      total: 0.55
      efficiency: 0.42
      win: 0.73
      pick: 0.18
      fit: 0.43
    Soul Gem:
      total: 0.56
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.81
  community_ordered:
  - Rod of Tahuti
  - Soul Reaver
  - Soul Gem
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Genji's Guard
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
    Underrated for this god: Gluttonous Grimoire, Amanita Charm, Genji''s Guard, Spear
    of the Magus, Jade Scepter, Rod of Asclepius, Yogi''s Necklace, Doom Orb, Chandra''s
    Grace, Phoenix Feather, The World Stone, Oni Hunter''s Garb, Blood-Bound Book,
    Wish-Granting Pearl, Dreamer''s Idol, Chronos'' Pendant, Sphere of Negation, Ancile,
    Lifebinder, Alchemist Coat, Screeching Gargoyle, Void Stone, Kinetic Cuirass,
    The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.69
      win: 0.44
      pick: 0.12
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.35
      fit: 0.62
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.87
      win: 0.48
      pick: 0.3
      fit: 0.47
    Obsidian Shard:
      total: 0.53
      efficiency: 0.58
      win: 0.51
      pick: 0.22
      fit: 0.57
    Soul Gem:
      total: 0.57
      efficiency: 0.53
      win: 0.54
      pick: 0.16
      fit: 0.92
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
  aspect: Aspect of the Cursed Crown
---
