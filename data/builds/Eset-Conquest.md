---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.43
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.41
    win_rate: 0.68
    alternates:
    - name: Book of Thoth
      pick_rate: 0.25
      win_rate: 0.42
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 0.29
  - name: Book of Thoth
    pick_rate: 0.12
    win_rate: 0.56
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.27
      win_rate: 0.5
    - name: Doom Orb
      pick_rate: 0.12
      win_rate: 0.89
  - name: Rod of Tahuti
    pick_rate: 0.39
    win_rate: 0.54
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.07
      win_rate: 0.8
    - name: Soul Gem
      pick_rate: 0.07
      win_rate: 0.8
  - name: Obsidian Shard
    pick_rate: 0.21
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.22
      win_rate: 0.6
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.67
  - name: Soul Gem
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.29
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 1.0
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: Spear of the Magus
      pick_rate: 0.09
      win_rate: 0.67
    - name: Ancient Signet
      pick_rate: 0.09
      win_rate: 0.67
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.39
    win_rate: 0.59
  - name: Conduit Gem
    pick_rate: 0.27
    win_rate: 0.5
  - name: Pendulum of the Ages
    pick_rate: 0.11
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-10-24'
  god_win_rate: 0.56
  god_matches_won: 42
  god_matches_played: 75
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-24'
  god_matches_analyzed: 3785
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
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
    this god: Chronos'' Pendant, Gluttonous Grimoire, Dreamer''s Idol, The Cosmic
    Horror, Gem of Focus, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer
    of The Abyss, Nimble Ring.'
  slot_scores:
    Chronos' Pendant:
      total: 0.65
      efficiency: 0.55
      win: 0.8
      pick: 0.11
      fit: 0.64
    Spear of Desolation:
      total: 0.68
      efficiency: 0.57
      win: 0.68
      pick: 0.41
      fit: 1.0
    Doom Orb:
      total: 0.71
      efficiency: 0.53
      win: 0.89
      pick: 0.16
      fit: 0.77
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.54
      pick: 0.61
      fit: 0.77
    Spear of the Magus:
      total: 0.64
      efficiency: 0.6
      win: 0.67
      pick: 0.28
      fit: 0.77
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.64
      pick: 0.35
      fit: 0.87
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - The World Stone
  flex_slots:
  - Spear of the Magus
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Chronos''
    Pendant, Death Metal, Gluttonous Grimoire, Dreamer''s Idol, Bragi''s Harp, Gem
    of Focus, Polynomicon, Soul Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s
    Talon, Totem of Death, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine
    Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    Chronos' Pendant:
      total: 0.62
      efficiency: 0.55
      win: 0.8
      pick: 0.11
      fit: 0.43
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.68
      pick: 0.41
      fit: 0.61
    Doom Orb:
      total: 0.68
      efficiency: 0.53
      win: 0.89
      pick: 0.16
      fit: 0.57
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.54
      pick: 0.61
      fit: 0.57
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.28
      fit: 0.47
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.67
      pick: 0.15
      fit: 0.57
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - The World Stone
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Chronos'' Pendant, Gluttonous Grimoire, Dreamer''s Idol, Death Metal, Gem
    of Focus, The Cosmic Horror, Bragi''s Harp, Totem of Death, Rod of Asclepius,
    Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Triton''s
    Conch, Breastplate of Valor, Bancroft''s Talon, Genji''s Guard, Helm of Radiance,
    Ethereal Staff.'
  slot_scores:
    Chronos' Pendant:
      total: 0.62
      efficiency: 0.55
      win: 0.8
      pick: 0.11
      fit: 0.44
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.68
      pick: 0.41
      fit: 0.78
    Doom Orb:
      total: 0.68
      efficiency: 0.53
      win: 0.89
      pick: 0.16
      fit: 0.56
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.54
      pick: 0.61
      fit: 0.56
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.67
      pick: 0.28
      fit: 0.56
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.64
      pick: 0.35
      fit: 0.66
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Spear of Desolation
  - Rod of Asclepius
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Genji''s Guard, Breastplate of
    Valor, Shifter''s Shield, Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s
    Necklace, Erosion, Eye of Providence, Phoenix Feather, Draconic Scale, Chandra''s
    Grace, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Glorious Pridwen.'
  slot_scores:
    Chronos' Pendant:
      total: 0.61
      efficiency: 0.55
      win: 0.8
      pick: 0.11
      fit: 0.32
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.68
      pick: 0.41
      fit: 0.5
    Doom Orb:
      total: 0.65
      efficiency: 0.53
      win: 0.89
      pick: 0.16
      fit: 0.38
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.54
      pick: 0.61
      fit: 0.38
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.8
    Rod of Asclepius:
      total: 0.6
      efficiency: 0.57
      win: 0.66
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Chronos' Pendant
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
    for this god: Chronos'' Pendant, Gluttonous Grimoire, Dreamer''s Idol, The Cosmic
    Horror, Gem of Focus, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Screeching Gargoyle, Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Breastplate
    of Valor, Staff of Myrddin.'
  slot_scores:
    Chronos' Pendant:
      total: 0.63
      efficiency: 0.55
      win: 0.8
      pick: 0.11
      fit: 0.45
    Spear of Desolation:
      total: 0.68
      efficiency: 0.57
      win: 0.68
      pick: 0.41
      fit: 1.0
    Doom Orb:
      total: 0.72
      efficiency: 0.53
      win: 0.89
      pick: 0.16
      fit: 0.84
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.54
      pick: 0.61
      fit: 0.84
    Spear of the Magus:
      total: 0.65
      efficiency: 0.6
      win: 0.67
      pick: 0.28
      fit: 0.84
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.64
      pick: 0.35
      fit: 0.94
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
  - Nimble Ring
  - Rod of Tahuti
  - Bragi's Harp
  - Doom Orb
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
    this god: Chronos'' Pendant, Nimble Ring, Gluttonous Grimoire, Bragi''s Harp,
    Bracer of The Abyss, Blood-Bound Book, Dreamer''s Idol, Death Metal, Bancroft''s
    Talon, Gem of Focus, Rod of Asclepius, The Cosmic Horror, Polynomicon, Typhon’s
    Heart, Soul Reaver, Totem of Death, Jade Scepter, Divine Ruin, Helm of Radiance,
    Daybreak Gavel.'
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.55
      win: 0.8
      pick: 0.11
      fit: 0.26
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.52
      win: 0.66
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.54
      pick: 0.61
      fit: 0.31
    Bragi's Harp:
      total: 0.54
      efficiency: 0.44
      win: 0.66
      pick: 0.0
      fit: 0.62
    Doom Orb:
      total: 0.64
      efficiency: 0.53
      win: 0.89
      pick: 0.16
      fit: 0.31
  community_ordered:
  - Chronos' Pendant
  - Rod of Tahuti
  - Doom Orb
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Gluttonous
    Grimoire, Totem of Death, Breastplate of Valor, Dreamer''s Idol, Genji''s Guard,
    Death Metal, Staff of Myrddin, The Cosmic Horror, Eye of Erebus, Screeching Gargoyle,
    Bragi''s Harp, Rod of Asclepius, Chandra''s Grace, Freya''s Tears, Polynomicon,
    Blood-Bound Book, Soul Reaver, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.65
      efficiency: 0.55
      win: 0.8
      pick: 0.11
      fit: 0.63
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.68
      pick: 0.41
      fit: 0.86
    Doom Orb:
      total: 0.65
      efficiency: 0.53
      win: 0.89
      pick: 0.16
      fit: 0.37
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.54
      pick: 0.61
      fit: 0.37
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.67
      pick: 0.28
      fit: 0.37
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.26
      fit: 0.96
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Jotunn's Revenge
  - Rod of Tahuti
  - Doom Orb
  - Spear of the Magus
  flex_slots:
  - Chronos' Pendant
  - Spear of the Magus
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Chronos'' Pendant, Heartseeker,
    Hydra''s Lament, Tyrfing, Bragi''s Harp, Tekko-Kagi, Lernaean Bow, Nimble Ring,
    Death Metal, Titan''s Bane, Gluttonous Grimoire, The Crusher, Silverbranch Bow,
    The Reaper, Golden Blade, Pendulum Blade, Dreamer''s Idol, Arondight, Dominance,
    Avatar''s Parashu, Bracer of The Abyss, Transcendence, Riptalon, Runeforged Hammer,
    Gem of Focus, Toxic Blade, The Cosmic Horror, Avenging Blade, Triton''s Conch,
    Rod of Asclepius, Polynomicon, Totem of Death.'
  slot_scores:
    Chronos' Pendant:
      total: 0.61
      efficiency: 0.55
      win: 0.8
      pick: 0.11
      fit: 0.35
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.68
      pick: 0.41
      fit: 0.56
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.54
      pick: 0.61
      fit: 0.43
    Doom Orb:
      total: 0.66
      efficiency: 0.53
      win: 0.89
      pick: 0.16
      fit: 0.43
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.67
      pick: 0.28
      fit: 0.43
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Doom Orb
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Jotunn's Revenge
  - Rod of Tahuti
  - Doom Orb
  - Spear of the Magus
  flex_slots:
  - Chronos' Pendant
  - Spear of the Magus
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Chronos'' Pendant,
    Heartseeker, Gluttonous Grimoire, Hydra''s Lament, Death Metal, Titan''s Bane,
    The Crusher, Dreamer''s Idol, The Reaper, Pendulum Blade, Bragi''s Harp, Arondight,
    Gem of Focus, Avatar''s Parashu, Tyrfing, The Cosmic Horror, Transcendence, Runeforged
    Hammer, Tekko-Kagi, Rod of Asclepius, Totem of Death, Triton''s Conch, Polynomicon,
    Avenging Blade, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Golden Blade, Silverbranch Bow, Helm of Radiance.'
  slot_scores:
    Chronos' Pendant:
      total: 0.62
      efficiency: 0.55
      win: 0.8
      pick: 0.11
      fit: 0.45
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.68
      pick: 0.41
      fit: 0.7
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.54
      pick: 0.61
      fit: 0.55
    Doom Orb:
      total: 0.68
      efficiency: 0.53
      win: 0.89
      pick: 0.16
      fit: 0.55
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.67
      pick: 0.28
      fit: 0.55
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Doom Orb
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
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
    Underrated for this god: Gluttonous Grimoire, Dreamer''s Idol, Chronos'' Pendant,
    The Cosmic Horror, Gem of Focus, Totem of Death, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm
    of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart,
    Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.68
      efficiency: 0.57
      win: 0.68
      pick: 0.41
      fit: 1.0
    Doom Orb:
      total: 0.71
      efficiency: 0.53
      win: 0.89
      pick: 0.16
      fit: 0.77
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.54
      pick: 0.61
      fit: 0.77
    Spear of the Magus:
      total: 0.64
      efficiency: 0.6
      win: 0.67
      pick: 0.28
      fit: 0.77
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.64
      pick: 0.35
      fit: 0.87
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.57
      pick: 0.26
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  starter: *id001
---
