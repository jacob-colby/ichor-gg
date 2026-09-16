---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.51
  aspect_win_rate: 0.58
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.18
    win_rate: 0.57
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.14
      win_rate: 0.51
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.62
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.63
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.47
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.63
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.46
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.59
  - name: Obsidian Shard
    pick_rate: 0.11
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.57
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.61
  - name: Shell of Rebuke
    pick_rate: 0.04
    win_rate: 0.55
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.63
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.56
  - name: Olmec Blue
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 1.0
    - name: Rod of Tahuti
      pick_rate: 0.04
      win_rate: 0.67
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.22
    win_rate: 0.65
  - name: Conduit Gem
    pick_rate: 0.18
    win_rate: 0.52
  - name: Sands Of Time
    pick_rate: 0.11
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-09-16'
  god_win_rate: 0.5757575757575758
  god_matches_won: 190
  god_matches_played: 330
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-16'
  god_matches_analyzed: 9166
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
    this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World
    Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Book
    of Thoth, Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer
    of The Abyss, Nimble Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.62
      pick: 0.11
      fit: 0.41
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.57
      pick: 0.18
      fit: 1.0
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.52
      pick: 0.16
      fit: 0.77
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.57
      pick: 0.18
      fit: 0.87
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.57
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Spear of the Magus, Doom Orb, The World Stone, Death Metal, Book of Thoth,
    Gluttonous Grimoire, Ancient Signet, Chronos'' Pendant, Dreamer''s Idol, Bragi''s
    Harp, Gem of Focus, Polynomicon, Soul Reaver, The Cosmic Horror, Rod of Asclepius,
    Bancroft''s Talon, Totem of Death, Triton''s Conch, Blood-Bound Book, Jade Scepter,
    Divine Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate of Valor, Ethereal
    Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.62
      pick: 0.11
      fit: 0.39
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.57
      pick: 0.18
      fit: 0.61
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.57
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.52
      pick: 0.16
      fit: 0.57
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone,
    Dreamer''s Idol, Chronos'' Pendant, Death Metal, Gem of Focus, Book of Thoth,
    The Cosmic Horror, Ancient Signet, Genji''s Guard, Bragi''s Harp, Totem of Death,
    Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.62
      pick: 0.11
      fit: 0.22
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.57
      pick: 0.18
      fit: 0.78
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.52
      pick: 0.16
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.18
      fit: 0.66
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.57
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
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
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
    this god: Amanita Charm, Soul Gem, Rod of Asclepius, Genji''s Guard, Shield of
    the Phoenix, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, Spear of the
    Magus, Breastplate of Valor, Shifter''s Shield, Lifebinder, Helm of Radiance,
    Sphere of Negation, Yogi''s Necklace, Erosion, Eye of Providence, Phoenix Feather,
    Draconic Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Doom Orb,
    Glorious Pridwen, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.63
      pick: 0.1
      fit: 0.27
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.42
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.18
      fit: 0.5
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.9
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom Orb, The
    World Stone, Dreamer''s Idol, The Cosmic Horror, Chronos'' Pendant, Book of Thoth,
    Ancient Signet, Gem of Focus, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Screeching Gargoyle, Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Breastplate
    of Valor, Staff of Myrddin.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.57
      pick: 0.18
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.84
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.52
      pick: 0.16
      fit: 0.84
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.57
      pick: 0.18
      fit: 0.94
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, Book of Thoth, The World
    Stone, Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Death Metal, Bancroft''s
    Talon, Gem of Focus, Rod of Asclepius, The Cosmic Horror, Polynomicon, Typhon’s
    Heart, Soul Reaver, Totem of Death, Jade Scepter, Divine Ruin, Helm of Radiance,
    Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.51
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.57
      pick: 0.18
      fit: 0.41
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.52
      pick: 0.16
      fit: 0.31
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Gem of Focus
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Gem of
    Focus, Spear of the Magus, Genji''s Guard, Gluttonous Grimoire, Totem of Death,
    Doom Orb, The World Stone, Breastplate of Valor, Dreamer''s Idol, Book of Thoth,
    Ancient Signet, Death Metal, Staff of Myrddin, The Cosmic Horror, Eye of Erebus,
    Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Chandra''s Grace.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.63
    Gem of Focus:
      total: 0.53
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.57
      pick: 0.18
      fit: 0.86
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.52
      pick: 0.16
      fit: 0.37
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.18
      fit: 0.47
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.57
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
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Spear of the
    Magus, Heartseeker, Hydra''s Lament, Tyrfing, Bragi''s Harp, Tekko-Kagi, Lernaean
    Bow, Nimble Ring, Death Metal, Titan''s Bane, Gluttonous Grimoire, The Crusher,
    Silverbranch Bow, The Reaper, Golden Blade, Doom Orb, The World Stone, Pendulum
    Blade, Chronos'' Pendant, Dreamer''s Idol, Arondight, Book of Thoth, Dominance,
    Avatar''s Parashu, Bracer of The Abyss, Ancient Signet, Transcendence, Riptalon,
    Runeforged Hammer, Gem of Focus, Toxic Blade, The Cosmic Horror, Avenging Blade,
    Triton''s Conch, Rod of Asclepius, Polynomicon, Totem of Death.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.62
      pick: 0.11
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.65
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.32
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.18
      fit: 0.56
    Nimble Ring:
      total: 0.52
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.52
      pick: 0.16
      fit: 0.43
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Spear
    of the Magus, Heartseeker, Gluttonous Grimoire, Hydra''s Lament, Death Metal,
    Doom Orb, The World Stone, Titan''s Bane, The Crusher, Dreamer''s Idol, Chronos''
    Pendant, The Reaper, Pendulum Blade, Book of Thoth, Bragi''s Harp, Ancient Signet,
    Arondight, Gem of Focus, Avatar''s Parashu, Tyrfing, The Cosmic Horror, Transcendence,
    Runeforged Hammer, Tekko-Kagi, Rod of Asclepius, Totem of Death, Triton''s Conch,
    Polynomicon, Avenging Blade, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Golden Blade, Silverbranch Bow, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.62
      pick: 0.11
      fit: 0.3
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.7
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.57
      pick: 0.18
      fit: 0.7
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.52
      pick: 0.16
      fit: 0.55
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
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
    Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm
    of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart,
    Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.57
      pick: 0.18
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.52
      pick: 0.16
      fit: 0.77
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.57
      pick: 0.18
      fit: 0.87
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
