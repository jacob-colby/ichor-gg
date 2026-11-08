---
type: smite-build
god: Sol
mode: Conquest
builds:
- source: community
  aspect: Aspect of Conflagration
  aspect_pick_rate: 0.47
  aspect_win_rate: 0.6
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.35
    win_rate: 0.63
    alternates:
    - name: Book of Thoth
      pick_rate: 0.23
      win_rate: 0.57
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.75
  - name: Dagger of Frenzy
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Tyrfing
      pick_rate: 0.12
      win_rate: 0.67
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.58
  - name: Rod of Tahuti
    pick_rate: 0.14
    win_rate: 0.56
    alternates:
    - name: Soul Gem
      pick_rate: 0.11
      win_rate: 0.5
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.53
  - name: Silverbranch Bow
    pick_rate: 0.13
    win_rate: 0.65
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.57
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.48
  - name: Obsidian Shard
    pick_rate: 0.08
    win_rate: 0.73
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.6
    - name: Riptalon
      pick_rate: 0.08
      win_rate: 0.5
  - name: Hunter's Bow
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Manchu Bow
      pick_rate: 0.06
      win_rate: 0.63
    - name: Bow
      pick_rate: 0.04
      win_rate: 0.83
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.24
    win_rate: 0.65
  - name: Sharpshooter's Arrow
    pick_rate: 0.15
    win_rate: 0.45
  - name: Gilded Arrow
    pick_rate: 0.14
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/sol/
  last_verified: '2026-11-08'
  god_win_rate: 0.5951219512195122
  god_matches_won: 122
  god_matches_played: 205
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5134
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Blood-Bound Book, Bracer of The Abyss,
    Spear of the Magus, Dreamer''s Idol, Chronos'' Pendant, Ancient Signet, Doom Orb,
    Polynomicon, The World Stone, Bancroft''s Talon, Gem of Focus, Heartwood Charm,
    The Cosmic Horror, Soul Reaver, Bragi''s Harp, Typhon’s Heart, Totem of Death,
    Jade Scepter, Divine Ruin, Genji''s Guard, Ethereal Staff, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.58
      pick: 0.16
      fit: 0.58
    Spear of the Magus:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.56
      pick: 0.22
      fit: 0.46
    Obsidian Shard:
      total: 0.61
      efficiency: 0.53
      win: 0.73
      pick: 0.17
      fit: 0.56
  community_ordered:
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
  - Nimble Ring
  - Ancient Signet
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Ancient Signet
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Bragi''s
    Harp, Nimble Ring, Gluttonous Grimoire, Death Metal, Ancient Signet, Blood-Bound
    Book, Polynomicon, Spear of the Magus, Chronos'' Pendant, Bracer of The Abyss,
    Doom Orb, Dreamer''s Idol, Bancroft''s Talon, The World Stone, Heartwood Charm,
    Soul Reaver, Gem of Focus, The Cosmic Horror, Totem of Death, Genji''s Guard,
    Typhon’s Heart, Triton''s Conch, Jade Scepter, Divine Ruin.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.48
      win: 0.57
      pick: 0.23
      fit: 0.28
    Nimble Ring:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.48
    Ancient Signet:
      total: 0.53
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.38
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.58
      pick: 0.16
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.56
      pick: 0.22
      fit: 0.42
    Obsidian Shard:
      total: 0.59
      efficiency: 0.53
      win: 0.73
      pick: 0.17
      fit: 0.44
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
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
    god: Gluttonous Grimoire, Nimble Ring, Bragi''s Harp, Spear of the Magus, Blood-Bound
    Book, Dreamer''s Idol, Death Metal, Chronos'' Pendant, Ancient Signet, Bracer
    of The Abyss, Doom Orb, Polynomicon, The World Stone, Gem of Focus, Heartwood
    Charm, Bancroft''s Talon, The Cosmic Horror, Soul Reaver, Totem of Death, Damaru,
    Genji''s Guard, Typhon’s Heart, Jade Scepter, Divine Ruin.'
  slot_scores:
    Nimble Ring:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.44
    Bragi's Harp:
      total: 0.53
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.58
      pick: 0.16
      fit: 0.56
    Spear of the Magus:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.56
      pick: 0.22
      fit: 0.4
    Obsidian Shard:
      total: 0.6
      efficiency: 0.53
      win: 0.73
      pick: 0.17
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire, Blood-Bound
    Book, Kinetic Cuirass, Genji''s Guard, Ethereal Staff, Phoenix Feather, Yogi''s
    Necklace, Bancroft''s Talon, Nimble Ring, Freya''s Tears, Breastplate of Valor,
    Chandra''s Grace, Oni Hunter''s Garb, Draconic Scale, Helm of Radiance, Sphere
    of Negation, Spear of the Magus, Ancient Signet, Regrowth Striders, Erosion, Eye
    of Providence, Helm of Darkness, Bracer of The Abyss.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.6
      pick: 0.0
      fit: 0.19
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.48
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.64
    Obsidian Shard:
      total: 0.58
      efficiency: 0.53
      win: 0.73
      pick: 0.17
      fit: 0.38
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.56
      pick: 0.22
      fit: 0.28
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
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
    for this god: Gluttonous Grimoire, Spear of the Magus, Nimble Ring, Dreamer''s
    Idol, Doom Orb, The World Stone, Blood-Bound Book, Bracer of The Abyss, Ancient
    Signet, The Cosmic Horror, Chronos'' Pendant, Polynomicon, Bancroft''s Talon,
    Gem of Focus, Heartwood Charm, Soul Reaver, Typhon’s Heart, Totem of Death, Bragi''s
    Harp, Screeching Gargoyle, Genji''s Guard, Jade Scepter, Divine Ruin, Ethereal
    Staff.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.58
      pick: 0.16
      fit: 0.66
    Doom Orb:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.56
      pick: 0.22
      fit: 0.56
    Obsidian Shard:
      total: 0.62
      efficiency: 0.53
      win: 0.73
      pick: 0.17
      fit: 0.66
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
    this god: Nimble Ring, Gluttonous Grimoire, Bragi''s Harp, Blood-Bound Book, Bracer
    of The Abyss, Spear of the Magus, Death Metal, Ancient Signet, Dreamer''s Idol,
    Polynomicon, Chronos'' Pendant, Doom Orb, The World Stone, Bancroft''s Talon,
    Gem of Focus, Soul Reaver, Heartwood Charm, The Cosmic Horror, Typhon’s Heart,
    Totem of Death, Damaru, Genji''s Guard, Jade Scepter, Divine Ruin.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.53
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.58
      pick: 0.16
      fit: 0.39
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.56
      pick: 0.22
      fit: 0.31
    Obsidian Shard:
      total: 0.59
      efficiency: 0.53
      win: 0.73
      pick: 0.17
      fit: 0.41
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Bragi's Harp
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - Bragi's Harp
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Nimble Ring, Gluttonous
    Grimoire, Bragi''s Harp, Gem of Focus, Heartwood Charm, Blood-Bound Book, Spear
    of the Magus, Bracer of The Abyss, Ancient Signet, Damaru, Genji''s Guard, Death
    Metal, Dreamer''s Idol, Polynomicon, Totem of Death, Doom Orb, The World Stone,
    Bancroft''s Talon, Breastplate of Valor, Chandra''s Grace, Soul Reaver, The Cosmic
    Horror, Typhon’s Heart, Screeching Gargoyle.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.44
    Bragi's Harp:
      total: 0.52
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.58
      pick: 0.16
      fit: 0.6
    Obsidian Shard:
      total: 0.58
      efficiency: 0.53
      win: 0.73
      pick: 0.17
      fit: 0.36
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.56
      pick: 0.22
      fit: 0.26
    Soul Gem:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.17
      fit: 0.78
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The Reaper
  - Spear of Desolation
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
    win/pick). Underrated for this god: Jotunn''s Revenge, The Reaper, Gluttonous
    Grimoire, Bragi''s Harp, Death Metal, Hydra''s Lament, The Crusher, Heartseeker,
    Tekko-Kagi, Nimble Ring, Blood-Bound Book, Titan''s Bane, Spear of the Magus,
    Dreamer''s Idol, Ancient Signet, Golden Blade, Arondight, Lernaean Bow, Dominance,
    Chronos'' Pendant, Polynomicon, Doom Orb, Avatar''s Parashu, The World Stone,
    Bracer of The Abyss, Bancroft''s Talon, Pendulum Blade, Toxic Blade, Gem of Focus,
    Heartwood Charm, Soul Reaver, Bloodforge, Transcendence, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.6
      efficiency: 0.53
      win: 0.67
      pick: 0.16
      fit: 0.68
    The Reaper:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.58
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.58
      pick: 0.16
      fit: 0.49
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.56
      pick: 0.22
      fit: 0.39
    Obsidian Shard:
      total: 0.6
      efficiency: 0.53
      win: 0.73
      pick: 0.17
      fit: 0.49
  community_ordered:
  - Tyrfing
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Silverbranch Bow
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Silverbranch Bow
  - Nimble Ring
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Bragi''s Harp,
    Nimble Ring, Gluttonous Grimoire, The Reaper, Tekko-Kagi, Death Metal, Blood-Bound
    Book, Spear of the Magus, Hydra''s Lament, The Crusher, Bracer of The Abyss, Ancient
    Signet, Lernaean Bow, Dominance, Heartseeker, Dreamer''s Idol, Golden Blade, Chronos''
    Pendant, Polynomicon, Titan''s Bane, Doom Orb, Toxic Blade, The World Stone, Arondight,
    Bancroft''s Talon, Qin''s Blade, Gem of Focus, Heartwood Charm, Soul Reaver, Avatar''s
    Parashu, The Cosmic Horror, Pendulum Blade, Typhon’s Heart.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.6
      efficiency: 0.53
      win: 0.67
      pick: 0.16
      fit: 0.69
    Nimble Ring:
      total: 0.55
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.52
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.49
      win: 0.65
      pick: 0.22
      fit: 0.55
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.56
      pick: 0.22
      fit: 0.38
    Obsidian Shard:
      total: 0.6
      efficiency: 0.53
      win: 0.73
      pick: 0.17
      fit: 0.48
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Rod of Tahuti
  - Obsidian Shard
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
    Underrated for this god: Nimble Ring, Gluttonous Grimoire, Blood-Bound Book, Bracer
    of The Abyss, Spear of the Magus, Dreamer''s Idol, Chronos'' Pendant, Ancient
    Signet, Doom Orb, Polynomicon, The World Stone, Bancroft''s Talon, Gem of Focus,
    Heartwood Charm, The Cosmic Horror, Soul Reaver, Bragi''s Harp, Typhon’s Heart,
    Totem of Death, Jade Scepter, Divine Ruin, Genji''s Guard, Ethereal Staff, Helm
    of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.58
      pick: 0.16
      fit: 0.58
    Spear of the Magus:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.56
      pick: 0.22
      fit: 0.46
    Obsidian Shard:
      total: 0.61
      efficiency: 0.53
      win: 0.73
      pick: 0.17
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
