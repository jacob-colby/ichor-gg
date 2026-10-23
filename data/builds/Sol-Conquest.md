---
type: smite-build
god: Sol
mode: Conquest
builds:
- source: community
  aspect: Aspect of Conflagration
  aspect_pick_rate: 0.43
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.32
    win_rate: 0.81
    alternates:
    - name: Book of Thoth
      pick_rate: 0.18
      win_rate: 0.53
    - name: Bragi's Harp
      pick_rate: 0.1
      win_rate: 0.88
  - name: Spear of Desolation
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.11
      win_rate: 0.89
    - name: Gem of Focus
      pick_rate: 0.1
      win_rate: 0.63
  - name: Riptalon
    pick_rate: 0.15
    win_rate: 0.75
    alternates:
    - name: Dominance
      pick_rate: 0.12
      win_rate: 1.0
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.57
  - name: Rod of Tahuti
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.82
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.83
  - name: Demon Blade
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.5
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.67
  - name: Deathbringer
    pick_rate: 0.16
    win_rate: 0.78
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.8
    - name: Axe
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.53
  - name: Sharpshooter's Arrow
    pick_rate: 0.17
    win_rate: 1.0
  - name: Hunter's Cowl
    pick_rate: 0.12
    win_rate: 0.7
  source_url: https://smitebrain.com/gods/sol/
  last_verified: '2026-10-23'
  god_win_rate: 0.6547619047619048
  god_matches_won: 55
  god_matches_played: 84
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-23'
  god_matches_analyzed: 2743
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of the Magus
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Obsidian Shard,
    Bragi''s Harp, Bracer of The Abyss, Doom Orb, The World Stone, Chronos'' Pendant,
    Dreamer''s Idol, Soul Gem, Blood-Bound Book, Ancient Signet, Bancroft''s Talon,
    The Cosmic Horror, Typhon’s Heart, Rod of Asclepius, Polynomicon, Totem of Death,
    Soul Reaver, Jade Scepter, Divine Ruin, Helm of Radiance, Ethereal Staff, Wish-Granting
    Pearl, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.6
      efficiency: 0.52
      win: 0.75
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.66
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.6
      efficiency: 0.3
      win: 0.88
      pick: 0.1
      fit: 0.64
    Spear of the Magus:
      total: 0.62
      efficiency: 0.6
      win: 0.75
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.56
      pick: 0.18
      fit: 0.46
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.75
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Bragi's Harp
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Ancient Signet
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Doom Orb
  - Ancient Signet
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Bragi''s
    Harp, Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Obsidian Shard, Doom
    Orb, Ancient Signet, The World Stone, Bracer of The Abyss, Death Metal, Chronos''
    Pendant, Bancroft''s Talon, Blood-Bound Book, Dreamer''s Idol, Soul Gem, Polynomicon,
    Soul Reaver, Rod of Asclepius, The Cosmic Horror, Typhon’s Heart, Totem of Death,
    Jade Scepter, Divine Ruin, Triton''s Conch, Wish-Granting Pearl, Gem of Focus.'
  slot_scores:
    Nimble Ring:
      total: 0.64
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.66
      efficiency: 0.44
      win: 0.88
      pick: 0.1
      fit: 0.71
    Ancient Signet:
      total: 0.58
      efficiency: 0.53
      win: 0.75
      pick: 0.0
      fit: 0.38
    Doom Orb:
      total: 0.59
      efficiency: 0.53
      win: 0.75
      pick: 0.0
      fit: 0.42
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.75
      pick: 0.0
      fit: 0.34
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.56
      pick: 0.18
      fit: 0.42
  community_ordered:
  - Bragi's Harp
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Bragi''s Harp, Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Obsidian
    Shard, Doom Orb, The World Stone, Chronos'' Pendant, Bracer of The Abyss, Dreamer''s
    Idol, Soul Gem, Death Metal, Ancient Signet, Blood-Bound Book, The Cosmic Horror,
    Bancroft''s Talon, Rod of Asclepius, Totem of Death, Typhon’s Heart, Polynomicon,
    Soul Reaver, Jade Scepter, Divine Ruin, Breastplate of Valor, Genji''s Guard,
    Gem of Focus.'
  slot_scores:
    Nimble Ring:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.44
    Bragi's Harp:
      total: 0.65
      efficiency: 0.44
      win: 0.88
      pick: 0.1
      fit: 0.62
    Doom Orb:
      total: 0.58
      efficiency: 0.53
      win: 0.75
      pick: 0.0
      fit: 0.4
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.75
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.56
      pick: 0.18
      fit: 0.4
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.75
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Bragi's Harp
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Gluttonous Grimoire, Nimble Ring, Rod of Asclepius, Shield
    of the Phoenix, Kinetic Cuirass, Blood-Bound Book, Ethereal Staff, Freya''s Tears,
    Genji''s Guard, Breastplate of Valor, Bancroft''s Talon, Spear of the Magus, Soul
    Gem, Shifter''s Shield, Lifebinder, Obsidian Shard, Yogi''s Necklace, Helm of
    Radiance, Sphere of Negation, Phoenix Feather, Chandra''s Grace, Erosion, Eye
    of Providence, Jade Scepter, Bracer of The Abyss, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.75
      pick: 0.0
      fit: 0.19
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.19
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.75
      pick: 0.0
      fit: 0.31
    Gluttonous Grimoire:
      total: 0.64
      efficiency: 0.6
      win: 0.75
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.68
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Doom Orb
  - The World Stone
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
    for this god: Gluttonous Grimoire, Nimble Ring, Spear of the Magus, Obsidian Shard,
    Doom Orb, The World Stone, Dreamer''s Idol, Soul Gem, Bragi''s Harp, Bracer of
    The Abyss, The Cosmic Horror, Chronos'' Pendant, Blood-Bound Book, Ancient Signet,
    Bancroft''s Talon, Rod of Asclepius, Typhon’s Heart, Polynomicon, Totem of Death,
    Soul Reaver, Jade Scepter, Divine Ruin, Screeching Gargoyle, Helm of Radiance,
    Ethereal Staff, Gem of Focus.'
  slot_scores:
    Nimble Ring:
      total: 0.64
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.53
    Doom Orb:
      total: 0.61
      efficiency: 0.53
      win: 0.75
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.63
      efficiency: 0.6
      win: 0.75
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.6
      efficiency: 0.52
      win: 0.75
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.56
      pick: 0.18
      fit: 0.56
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.75
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Spear of the Magus
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
    this god: Bragi''s Harp, Nimble Ring, Gluttonous Grimoire, Spear of the Magus,
    Obsidian Shard, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, The World Stone,
    Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Death Metal, Bancroft''s Talon,
    Soul Gem, The Cosmic Horror, Rod of Asclepius, Typhon’s Heart, Polynomicon, Soul
    Reaver, Totem of Death, Jade Scepter, Divine Ruin, Helm of Radiance, Daybreak
    Gavel, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.58
      efficiency: 0.52
      win: 0.75
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.64
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.65
      efficiency: 0.44
      win: 0.88
      pick: 0.1
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.49
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.75
      pick: 0.0
      fit: 0.31
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.56
      pick: 0.18
      fit: 0.31
  community_ordered:
  - Bragi's Harp
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Bragi's Harp
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Bragi''s Harp, Nimble Ring, Gluttonous
    Grimoire, Chronos'' Pendant, Spear of the Magus, Obsidian Shard, Soul Gem, Bracer
    of The Abyss, Doom Orb, The World Stone, Totem of Death, Ancient Signet, Dreamer''s
    Idol, Blood-Bound Book, Breastplate of Valor, Death Metal, Genji''s Guard, Bancroft''s
    Talon, The Cosmic Horror, Gem of Focus, Rod of Asclepius, Typhon’s Heart, Polynomicon,
    Staff of Myrddin, Soul Reaver, Eye of Erebus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.0
      fit: 0.44
    Bragi's Harp:
      total: 0.63
      efficiency: 0.44
      win: 0.88
      pick: 0.1
      fit: 0.52
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.16
      fit: 0.6
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.75
      pick: 0.0
      fit: 0.26
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.56
      pick: 0.18
      fit: 0.26
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.57
      pick: 0.14
      fit: 0.78
  community_ordered:
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Bragi's Harp
  - Dominance
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Rod of Tahuti
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Bragi''s Harp, Nimble Ring,
    Gluttonous Grimoire, The Reaper, Tyrfing, Spear of the Magus, Heartseeker, Hydra''s
    Lament, Obsidian Shard, Tekko-Kagi, Lernaean Bow, Golden Blade, Titan''s Bane,
    Death Metal, The Crusher, Doom Orb, The World Stone, Chronos'' Pendant, Pendulum
    Blade, Dreamer''s Idol, Arondight, Blood-Bound Book, Avatar''s Parashu, Ancient
    Signet, Toxic Blade, Bracer of The Abyss, Soul Gem, Transcendence, Runeforged
    Hammer, Bancroft''s Talon, The Cosmic Horror, Avenging Blade, Barbed Carver, Qin''s
    Blade, Rod of Asclepius, Gem of Focus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.59
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.75
      pick: 0.0
      fit: 0.29
    Bragi's Harp:
      total: 0.66
      efficiency: 0.44
      win: 0.88
      pick: 0.1
      fit: 0.71
    Dominance:
      total: 0.69
      efficiency: 0.45
      win: 1.0
      pick: 0.19
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.62
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.56
      pick: 0.18
      fit: 0.39
  community_ordered:
  - Bragi's Harp
  - Dominance
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Dominance
  - Riptalon
  - Spear of the Magus
  flex_slots:
  - Tyrfing
  - Spear of the Magus
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
    + fit + win/pick). Underrated for this god: Bragi''s Harp, Jotunn''s Revenge,
    Nimble Ring, Gluttonous Grimoire, Tyrfing, Spear of the Magus, Obsidian Shard,
    Tekko-Kagi, The Reaper, Lernaean Bow, Golden Blade, Heartseeker, Hydra''s Lament,
    Bracer of The Abyss, Doom Orb, Death Metal, Toxic Blade, The World Stone, Titan''s
    Bane, Chronos'' Pendant, The Crusher, Dreamer''s Idol, Ancient Signet, Blood-Bound
    Book, Soul Gem, Bancroft''s Talon, Qin''s Blade, Arondight, Pendulum Blade, Avatar''s
    Parashu, Transcendence, The Cosmic Horror, Runeforged Hammer, Rod of Asclepius,
    Typhon’s Heart, Gem of Focus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.61
      efficiency: 0.48
      win: 0.75
      pick: 0.0
      fit: 0.72
    Bragi's Harp:
      total: 0.67
      efficiency: 0.44
      win: 0.88
      pick: 0.1
      fit: 0.75
    Dominance:
      total: 0.7
      efficiency: 0.45
      win: 1.0
      pick: 0.19
      fit: 0.54
    Riptalon:
      total: 0.63
      efficiency: 0.51
      win: 0.75
      pick: 0.23
      fit: 0.67
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.75
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Bragi's Harp
  - Dominance
  - Riptalon
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
    Underrated for this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of
    the Magus, Obsidian Shard, Bracer of The Abyss, Doom Orb, The World Stone, Chronos''
    Pendant, Dreamer''s Idol, Blood-Bound Book, Ancient Signet, Bancroft''s Talon,
    Gem of Focus, The Cosmic Horror, Typhon’s Heart, Rod of Asclepius, Polynomicon,
    Totem of Death, Soul Reaver, Jade Scepter, Divine Ruin, Bragi''s Harp, Helm of
    Radiance, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.6
      efficiency: 0.52
      win: 0.75
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.66
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.16
      fit: 0.58
    Spear of the Magus:
      total: 0.62
      efficiency: 0.6
      win: 0.75
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.56
      pick: 0.18
      fit: 0.46
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.75
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
