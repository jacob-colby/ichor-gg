---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.4
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.25
    win_rate: 0.56
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.09
      win_rate: 0.33
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.83
  - name: Genji's Guard
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.08
      win_rate: 0.8
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.2
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.73
    alternates:
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.2
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.25
  - name: Obsidian Shard
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.22
      win_rate: 0.38
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.67
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.15
      win_rate: 0.38
    - name: Soul Reaver
      pick_rate: 0.08
      win_rate: 0.25
  - name: Killing Stone
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.67
    - name: Medallion
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.23
    win_rate: 0.73
  - name: Conduit Gem
    pick_rate: 0.2
    win_rate: 0.38
  - name: Sands Of Time
    pick_rate: 0.17
    win_rate: 0.18
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-09-25'
  god_win_rate: 0.46153846153846156
  god_matches_won: 30
  god_matches_played: 65
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-25'
  god_matches_analyzed: 2996
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Spear of Desolation
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
    this god: Soul Gem, Spear of the Magus, Book of Thoth, Gluttonous Grimoire, Doom
    Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Gem
    of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss,
    Nimble Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.62
      efficiency: 0.51
      win: 0.83
      pick: 0.09
      fit: 0.41
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.56
      pick: 0.25
      fit: 1.0
    Spear of the Magus:
      total: 0.63
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.73
      pick: 0.26
      fit: 0.77
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.67
      pick: 0.17
      fit: 0.87
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Book
    of Thoth, Soul Gem, Spear of the Magus, Doom Orb, The World Stone, Death Metal,
    Gluttonous Grimoire, Ancient Signet, Chronos'' Pendant, Dreamer''s Idol, Bragi''s
    Harp, Gem of Focus, Polynomicon, The Cosmic Horror, Rod of Asclepius, Bancroft''s
    Talon, Totem of Death, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine
    Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.61
      efficiency: 0.51
      win: 0.83
      pick: 0.09
      fit: 0.39
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.57
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.73
      pick: 0.26
      fit: 0.57
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.17
      fit: 0.57
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Spear of Desolation
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
    god: Soul Gem, Spear of the Magus, Book of Thoth, Gluttonous Grimoire, Doom Orb,
    The World Stone, Dreamer''s Idol, Chronos'' Pendant, Death Metal, Gem of Focus,
    The Cosmic Horror, Ancient Signet, Bragi''s Harp, Totem of Death, Rod of Asclepius,
    Polynomicon, Blood-Bound Book, Jade Scepter, Divine Ruin, Triton''s Conch, Breastplate
    of Valor, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.59
      efficiency: 0.51
      win: 0.83
      pick: 0.09
      fit: 0.22
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.56
      pick: 0.25
      fit: 0.78
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.73
      pick: 0.26
      fit: 0.56
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.67
      pick: 0.17
      fit: 0.66
    Soul Gem:
      total: 0.61
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Book of Thoth
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
    this god: Amanita Charm, Soul Gem, Chandra''s Grace, Rod of Asclepius, Shield
    of the Phoenix, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s
    Tears, Spear of the Magus, Breastplate of Valor, Shifter''s Shield, Lifebinder,
    Helm of Radiance, Sphere of Negation, Yogi''s Necklace, Erosion, Eye of Providence,
    Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Genji''s Guard, Doom Orb, Glorious Pridwen.'
  slot_scores:
    Book of Thoth:
      total: 0.59
      efficiency: 0.51
      win: 0.83
      pick: 0.09
      fit: 0.2
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.73
      pick: 0.26
      fit: 0.38
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.62
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.9
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
    for this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom Orb, The
    World Stone, Dreamer''s Idol, Book of Thoth, The Cosmic Horror, Chronos'' Pendant,
    Ancient Signet, Gem of Focus, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Screeching
    Gargoyle, Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Breastplate of
    Valor, Staff of Myrddin.'
  slot_scores:
    Book of Thoth:
      total: 0.6
      efficiency: 0.51
      win: 0.83
      pick: 0.09
      fit: 0.29
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.56
      pick: 0.25
      fit: 1.0
    Spear of the Magus:
      total: 0.64
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.77
      efficiency: 0.86
      win: 0.73
      pick: 0.26
      fit: 0.84
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.67
      pick: 0.17
      fit: 0.94
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Bracer of The Abyss
  - Nimble Ring
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
    this god: Nimble Ring, Soul Gem, Book of Thoth, Gluttonous Grimoire, Spear of
    the Magus, Bragi''s Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, The
    World Stone, Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Death Metal, Bancroft''s
    Talon, Gem of Focus, Rod of Asclepius, The Cosmic Horror, Polynomicon, Typhon’s
    Heart, Totem of Death, Jade Scepter, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.58
      efficiency: 0.51
      win: 0.83
      pick: 0.09
      fit: 0.17
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.55
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.73
      pick: 0.26
      fit: 0.31
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Book
    of Thoth, Gem of Focus, Spear of the Magus, Chandra''s Grace, Gluttonous Grimoire,
    Totem of Death, Doom Orb, The World Stone, Breastplate of Valor, Dreamer''s Idol,
    Ancient Signet, Death Metal, Staff of Myrddin, The Cosmic Horror, Genji''s Guard,
    Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Freya''s
    Tears, Polynomicon, Blood-Bound Book, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.58
      efficiency: 0.51
      win: 0.83
      pick: 0.09
      fit: 0.14
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.56
      pick: 0.25
      fit: 0.86
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.73
      pick: 0.26
      fit: 0.37
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.17
      fit: 0.47
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Book of Thoth, Soul Gem,
    Spear of the Magus, Heartseeker, Hydra''s Lament, Tyrfing, Bragi''s Harp, Tekko-Kagi,
    Lernaean Bow, Nimble Ring, Death Metal, Titan''s Bane, Gluttonous Grimoire, The
    Crusher, Silverbranch Bow, The Reaper, Golden Blade, Doom Orb, The World Stone,
    Pendulum Blade, Chronos'' Pendant, Dreamer''s Idol, Arondight, Dominance, Avatar''s
    Parashu, Bracer of The Abyss, Ancient Signet, Transcendence, Riptalon, Runeforged
    Hammer, Gem of Focus, Toxic Blade, The Cosmic Horror, Avenging Blade, Triton''s
    Conch, Rod of Asclepius, Polynomicon, Totem of Death.'
  slot_scores:
    Book of Thoth:
      total: 0.59
      efficiency: 0.51
      win: 0.83
      pick: 0.09
      fit: 0.22
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.65
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.32
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.73
      pick: 0.26
      fit: 0.43
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.67
      pick: 0.17
      fit: 0.53
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Book
    of Thoth, Spear of the Magus, Heartseeker, Gluttonous Grimoire, Hydra''s Lament,
    Death Metal, Doom Orb, The World Stone, Titan''s Bane, The Crusher, Dreamer''s
    Idol, Chronos'' Pendant, The Reaper, Pendulum Blade, Bragi''s Harp, Ancient Signet,
    Arondight, Gem of Focus, Avatar''s Parashu, Tyrfing, The Cosmic Horror, Transcendence,
    Runeforged Hammer, Tekko-Kagi, Rod of Asclepius, Totem of Death, Triton''s Conch,
    Polynomicon, Avenging Blade, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Golden Blade, Silverbranch Bow, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.6
      efficiency: 0.51
      win: 0.83
      pick: 0.09
      fit: 0.3
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.7
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.3
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.73
      pick: 0.26
      fit: 0.55
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.67
      pick: 0.17
      fit: 0.65
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Book of Thoth
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
    Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Gem
    of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Book of Thoth, Polynomicon,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer
    of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.56
      pick: 0.25
      fit: 1.0
    Doom Orb:
      total: 0.6
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.63
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.73
      pick: 0.26
      fit: 0.77
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.67
      pick: 0.17
      fit: 0.87
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
