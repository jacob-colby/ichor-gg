---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.4
  aspect_win_rate: 0.53
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.31
    win_rate: 0.59
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.75
  - name: Genji's Guard
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.71
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.67
  - name: Soul Gem
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.71
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.59
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.56
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.65
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.46
  - name: Obsidian Shard
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.63
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.45
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.6
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.8
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-08-01'
  god_win_rate: 0.5829787234042553
  god_matches_won: 137
  god_matches_played: 235
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Book of Thoth
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
    this god: Obsidian Shard, Doom Orb, Gluttonous Grimoire, Spear of the Magus, The
    Cosmic Horror, Chronos'' Pendant, Genji''s Guard, The World Stone, Dreamer''s
    Idol, Gem of Focus, Death Metal, Rod of Asclepius, Blood-Bound Book, Helm of Radiance,
    Bancroft''s Talon, Jade Scepter, Breastplate of Valor, Bracer of The Abyss, Polynomicon,
    Ethereal Staff, Ancient Signet, Wish-Granting Pearl, Alchemist Coat, Typhon’s
    Heart.'
  slot_scores:
    Book of Thoth:
      total: 0.56
      efficiency: 0.43
      win: 0.75
      pick: 0.12
      fit: 0.41
    Spear of Desolation:
      total: 0.62
      efficiency: 0.54
      win: 0.59
      pick: 0.31
      fit: 1.0
    Doom Orb:
      total: 0.6
      efficiency: 0.5
      win: 0.67
      pick: 0.09
      fit: 0.77
    Spear of the Magus:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.61
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.77
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.56
      pick: 0.17
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Obsidian Shard, Doom Orb, Gluttonous Grimoire, Spear of the Magus, The Cosmic
    Horror, Genji''s Guard, Death Metal, Chronos'' Pendant, Breastplate of Valor,
    The World Stone, Dreamer''s Idol, Gem of Focus, Bragi''s Harp, Rod of Asclepius,
    Blood-Bound Book, Helm of Radiance, Bancroft''s Talon, Jade Scepter, Shield of
    the Phoenix, Triton''s Conch, Bracer of The Abyss, Amanita Charm, Oni Hunter''s
    Garb, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.43
      win: 0.75
      pick: 0.12
      fit: 0.22
    Spear of Desolation:
      total: 0.59
      efficiency: 0.54
      win: 0.59
      pick: 0.31
      fit: 0.78
    Doom Orb:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.09
      fit: 0.56
    Spear of the Magus:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.56
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.56
      pick: 0.17
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Dwarven Plate
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Dwarven Plate
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Genji''s Guard, Eye of Providence, Shifter''s Shield, Blood-Bound
    Book, Oni Hunter''s Garb, Lifebinder, Bancroft''s Talon, Chandra''s Grace, Spear
    of the Magus, Breastplate of Valor, The Cosmic Horror, Phoenix Feather, Erosion,
    Jade Scepter, Spectral Armor, Helm of Radiance, Yogi''s Necklace, Draconic Scale,
    Freya''s Tears, Sphere of Negation.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.54
      win: 0.59
      pick: 0.31
      fit: 0.5
    Doom Orb:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.09
      fit: 0.38
    Dwarven Plate:
      total: 0.54
      efficiency: 0.37
      win: 0.8
      pick: 0.05
      fit: 0.31
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.38
    Amanita Charm:
      total: 0.58
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.56
      pick: 0.17
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Obsidian Shard, Doom Orb, Gluttonous Grimoire, Spear of the Magus,
    The Cosmic Horror, The World Stone, Dreamer''s Idol, Genji''s Guard, Chronos''
    Pendant, Screeching Gargoyle, Death Metal, Rod of Asclepius, Breastplate of Valor,
    Blood-Bound Book, Helm of Radiance, Gem of Focus, Bancroft''s Talon, Jade Scepter,
    Bracer of The Abyss, Polynomicon, Ethereal Staff, Amanita Charm, Ancient Signet,
    Stone of Binding.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.54
      win: 0.59
      pick: 0.31
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.84
    Doom Orb:
      total: 0.61
      efficiency: 0.5
      win: 0.67
      pick: 0.09
      fit: 0.84
    Spear of the Magus:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.84
    Obsidian Shard:
      total: 0.62
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.84
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.56
      pick: 0.17
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Obsidian Shard, Gluttonous Grimoire, Doom Orb, Genji''s Guard, Spear
    of the Magus, Bracer of The Abyss, Bragi''s Harp, Death Metal, The Cosmic Horror,
    Nimble Ring, Blood-Bound Book, Breastplate of Valor, Bancroft''s Talon, Chronos''
    Pendant, Rod of Asclepius, Amanita Charm, Helm of Radiance, Oni Hunter''s Garb,
    Kinetic Cuirass, Yogi''s Necklace, Jade Scepter, The World Stone, Dreamer''s Idol,
    Eye of Providence, Freya''s Tears.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.53
      efficiency: 0.54
      win: 0.59
      pick: 0.31
      fit: 0.41
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.31
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.56
      pick: 0.17
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Doom Orb
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Dwarven Plate — magical protection
    swap_item: Dwarven Plate
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Obsidian Shard, Genji''s Guard, Doom
    Orb, Gluttonous Grimoire, Breastplate of Valor, Chronos'' Pendant, Gem of Focus,
    Shield of the Phoenix, Spear of the Magus, Freya''s Tears, The Cosmic Horror,
    Screeching Gargoyle, Chandra''s Grace, Death Metal, Gladiator''s Shield, Amanita
    Charm, Rod of Asclepius, The World Stone, Dreamer''s Idol, Oni Hunter''s Garb,
    Blood-Bound Book, Helm of Radiance, Kinetic Cuirass, Yogi''s Necklace, Prophetic
    Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.11
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.6
      efficiency: 0.54
      win: 0.59
      pick: 0.31
      fit: 0.86
    Doom Orb:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.09
      fit: 0.37
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.37
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.56
      pick: 0.17
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Doom Orb
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Crusher
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Obsidian Shard, Jotunn''s Revenge, The Crusher,
    Doom Orb, Gluttonous Grimoire, Hydra''s Lament, Death Metal, Bragi''s Harp, Spear
    of the Magus, Lernaean Bow, Genji''s Guard, Runeforged Hammer, The Cosmic Horror,
    The Reaper, Berserker''s Shield, Tekko-Kagi, Golden Blade, Heartseeker, Damaru,
    Dominance, Tyrfing, Bracer of The Abyss, Chronos'' Pendant, Pendulum Blade, Triton''s
    Conch, Breastplate of Valor, Riptalon, Avenging Blade, Arondight, Titan''s Bane,
    Rod of Asclepius, Silverbranch Bow, Blood-Bound Book, Helm of Radiance, The World
    Stone, Shield Splitter, Dreamer''s Idol, Bancroft''s Talon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.55
      efficiency: 0.54
      win: 0.59
      pick: 0.31
      fit: 0.56
    Doom Orb:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.09
      fit: 0.43
    The Crusher:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.43
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.56
      pick: 0.17
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Doom Orb
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Obsidian Shard, Doom Orb, Jotunn''s
    Revenge, Gluttonous Grimoire, The Crusher, Death Metal, Spear of the Magus, Hydra''s
    Lament, The Cosmic Horror, Genji''s Guard, The Reaper, Runeforged Hammer, Bragi''s
    Harp, Chronos'' Pendant, Heartseeker, Triton''s Conch, Pendulum Blade, Lernaean
    Bow, The World Stone, Dreamer''s Idol, Rod of Asclepius, Damaru, Blood-Bound Book,
    Helm of Radiance, Breastplate of Valor, Bancroft''s Talon, Titan''s Bane, Gem
    of Focus, Tekko-Kagi, Berserker''s Shield, Jade Scepter, Arondight, Bracer of
    The Abyss, Avenging Blade, Golden Blade, Shield Splitter, Polynomicon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.57
      efficiency: 0.54
      win: 0.59
      pick: 0.31
      fit: 0.7
    Doom Orb:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.09
      fit: 0.55
    The Crusher:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.65
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.55
    Soul Gem:
      total: 0.59
      efficiency: 0.59
      win: 0.56
      pick: 0.17
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Obsidian Shard, Chronos'' Pendant, The World Stone, Doom Orb, Dreamer''s Idol,
    Genji''s Guard, Gem of Focus, Death Metal, Rod of Asclepius, Blood-Bound Book,
    Helm of Radiance, Bancroft''s Talon, Jade Scepter, Breastplate of Valor, Bracer
    of The Abyss, Polynomicon, Ethereal Staff, Ancient Signet, Wish-Granting Pearl,
    Alchemist Coat, Typhon’s Heart.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.64
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.62
      efficiency: 0.54
      win: 0.59
      pick: 0.31
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.61
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.77
  starter: *id001
---
