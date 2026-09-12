---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.52
  aspect_win_rate: 0.59
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.14
    win_rate: 0.68
    alternates:
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.39
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.86
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.4
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.38
  - name: Genji's Guard
    pick_rate: 0.1
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.33
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.38
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 0.45
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.8
  - name: Olmec Blue
    pick_rate: 0.07
    win_rate: 0.4
    alternates:
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 0.33
    - name: Ring
      pick_rate: 0.04
      win_rate: 0.33
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.22
    win_rate: 0.59
  - name: Conduit Gem
    pick_rate: 0.18
    win_rate: 0.48
  - name: Sands Of Time
    pick_rate: 0.12
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-09-12'
  god_win_rate: 0.5714285714285714
  god_matches_won: 88
  god_matches_played: 154
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-12'
  god_matches_analyzed: 4284
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Freya's Tears
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Freya's Tears
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
    this god: Spear of Desolation, Soul Gem, Spear of the Magus, Gluttonous Grimoire,
    Doom Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror,
    Gem of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer
    of The Abyss, Nimble Ring, Book of Thoth.'
  slot_scores:
    Freya's Tears:
      total: 0.55
      efficiency: 0.36
      win: 0.86
      pick: 0.12
      fit: 0.23
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 1.0
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.45
      pick: 0.22
      fit: 0.77
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.58
      pick: 0.22
      fit: 0.87
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Freya's Tears
  - Spear of Desolation
  - Doom Orb
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of Desolation, Soul Gem, Spear of the Magus, Doom Orb, The World Stone, Death
    Metal, Gluttonous Grimoire, Ancient Signet, Chronos'' Pendant, Dreamer''s Idol,
    Bragi''s Harp, Gem of Focus, Polynomicon, Soul Reaver, The Cosmic Horror, Rod
    of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s Conch, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate
    of Valor, Ethereal Staff, Book of Thoth.'
  slot_scores:
    Freya's Tears:
      total: 0.54
      efficiency: 0.36
      win: 0.86
      pick: 0.12
      fit: 0.14
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.61
    Doom Orb:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.57
    The World Stone:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.45
      pick: 0.22
      fit: 0.57
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.58
      pick: 0.22
      fit: 0.57
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Freya's Tears
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
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
    god: Spear of Desolation, Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom
    Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, Death Metal, Gem of
    Focus, The Cosmic Horror, Ancient Signet, Bragi''s Harp, Totem of Death, Rod of
    Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin,
    Triton''s Conch, Breastplate of Valor, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Book of Thoth.'
  slot_scores:
    Freya's Tears:
      total: 0.55
      efficiency: 0.36
      win: 0.86
      pick: 0.12
      fit: 0.22
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.78
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.45
      pick: 0.22
      fit: 0.56
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.58
      pick: 0.22
      fit: 0.66
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Chandra's Grace
  - Genji's Guard
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
    this god: Freya''s Tears, Spear of Desolation, Amanita Charm, Chandra''s Grace,
    Soul Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire, Kinetic
    Cuirass, Ethereal Staff, Spear of the Magus, Breastplate of Valor, Shifter''s
    Shield, Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s Necklace, Erosion,
    Eye of Providence, Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Doom Orb, Glorious Pridwen.'
  slot_scores:
    Chandra's Grace:
      total: 0.56
      efficiency: 0.45
      win: 0.67
      pick: 0.1
      fit: 0.61
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.16
      fit: 0.27
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.86
      pick: 0.12
      fit: 0.42
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.5
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.22
      fit: 0.38
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Chandra's Grace
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Freya's Tears
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Freya's Tears
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
    for this god: Spear of Desolation, Spear of the Magus, Soul Gem, Gluttonous Grimoire,
    Doom Orb, The World Stone, Dreamer''s Idol, The Cosmic Horror, Chronos'' Pendant,
    Ancient Signet, Gem of Focus, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Screeching Gargoyle, Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Breastplate
    of Valor, Staff of Myrddin, Book of Thoth.'
  slot_scores:
    Freya's Tears:
      total: 0.54
      efficiency: 0.36
      win: 0.86
      pick: 0.12
      fit: 0.16
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 1.0
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.45
      pick: 0.22
      fit: 0.84
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.58
      pick: 0.22
      fit: 0.94
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Freya's Tears
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
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
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
    this god: Spear of Desolation, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear
    of the Magus, Bragi''s Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant,
    The World Stone, Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Death Metal,
    Bancroft''s Talon, Gem of Focus, Rod of Asclepius, The Cosmic Horror, Polynomicon,
    Typhon’s Heart, Soul Reaver, Totem of Death, Jade Scepter, Divine Ruin, Helm of
    Radiance, Daybreak Gavel, Book of Thoth.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    Freya's Tears:
      total: 0.53
      efficiency: 0.36
      win: 0.86
      pick: 0.12
      fit: 0.09
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.41
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.45
      pick: 0.22
      fit: 0.31
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Spear of Desolation, Freya''s Tears,
    Soul Gem, Chronos'' Pendant, Chandra''s Grace, Gem of Focus, Spear of the Magus,
    Gluttonous Grimoire, Totem of Death, Doom Orb, The World Stone, Breastplate of
    Valor, Dreamer''s Idol, Ancient Signet, Death Metal, Staff of Myrddin, The Cosmic
    Horror, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Soul Reaver, Jade Scepter, Book of Thoth.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.59
      efficiency: 0.36
      win: 0.86
      pick: 0.12
      fit: 0.48
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.86
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.22
      fit: 0.37
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.22
      fit: 0.47
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Freya's Tears
  - Nimble Ring
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
    win/pick). Underrated for this god: Spear of Desolation, Jotunn''s Revenge, Soul
    Gem, Spear of the Magus, Heartseeker, Hydra''s Lament, Tyrfing, Bragi''s Harp,
    Tekko-Kagi, Lernaean Bow, Nimble Ring, Death Metal, Titan''s Bane, Gluttonous
    Grimoire, The Crusher, Silverbranch Bow, The Reaper, Golden Blade, Doom Orb, The
    World Stone, Pendulum Blade, Chronos'' Pendant, Dreamer''s Idol, Arondight, Dominance,
    Avatar''s Parashu, Bracer of The Abyss, Ancient Signet, Transcendence, Riptalon,
    Runeforged Hammer, Gem of Focus, Toxic Blade, The Cosmic Horror, Avenging Blade,
    Triton''s Conch, Rod of Asclepius, Polynomicon, Totem of Death, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.65
    Nimble Ring:
      total: 0.49
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.35
    Freya's Tears:
      total: 0.54
      efficiency: 0.36
      win: 0.86
      pick: 0.12
      fit: 0.13
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.56
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.45
      pick: 0.22
      fit: 0.43
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.22
      fit: 0.53
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Soul Gem
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
    + fit + win/pick). Underrated for this god: Spear of Desolation, Jotunn''s Revenge,
    Soul Gem, Spear of the Magus, Heartseeker, Gluttonous Grimoire, Hydra''s Lament,
    Death Metal, Doom Orb, The World Stone, Titan''s Bane, The Crusher, Dreamer''s
    Idol, Chronos'' Pendant, The Reaper, Pendulum Blade, Bragi''s Harp, Ancient Signet,
    Arondight, Gem of Focus, Avatar''s Parashu, Tyrfing, The Cosmic Horror, Transcendence,
    Runeforged Hammer, Tekko-Kagi, Rod of Asclepius, Totem of Death, Triton''s Conch,
    Polynomicon, Avenging Blade, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Golden Blade, Silverbranch Bow, Helm of Radiance, Book
    of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.7
    Freya's Tears:
      total: 0.54
      efficiency: 0.36
      win: 0.86
      pick: 0.12
      fit: 0.15
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.7
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.45
      pick: 0.22
      fit: 0.55
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.58
      pick: 0.22
      fit: 0.65
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Freya's Tears
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
    Underrated for this god: Spear of Desolation, Soul Gem, Spear of the Magus, Gluttonous
    Grimoire, Doom Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic
    Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Book of
    Thoth, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin,
    Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 1.0
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.45
      pick: 0.22
      fit: 0.77
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.58
      pick: 0.22
      fit: 0.87
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
