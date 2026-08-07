---
type: smite-build
god: Sol
mode: Conquest
builds:
- source: community
  aspect: Aspect of Conflagration
  aspect_pick_rate: 0.68
  aspect_win_rate: 0.59
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.27
    win_rate: 0.6
    alternates:
    - name: Book of Thoth
      pick_rate: 0.2
      win_rate: 0.56
    - name: Tyrfing
      pick_rate: 0.11
      win_rate: 0.48
  - name: Book of Thoth
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.51
    - name: Doom Orb
      pick_rate: 0.06
      win_rate: 0.72
  - name: Soul Gem
    pick_rate: 0.21
    win_rate: 0.61
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.5
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.26
    win_rate: 0.63
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.51
    - name: Gem of Focus
      pick_rate: 0.07
      win_rate: 0.56
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.63
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.68
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.43
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.77
    - name: Obsidian Shard
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.31
    win_rate: 0.63
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 0.5
  - name: Pendulum of The Ages
    pick_rate: 0.07
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/sol/
  last_verified: '2026-08-06'
  god_win_rate: 0.5348432055749129
  god_matches_won: 307
  god_matches_played: 574
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-06'
  god_matches_analyzed: 12483
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Doom Orb, Gluttonous Grimoire, Spear of the Magus, Bracer of The Abyss,
    The Cosmic Horror, Genji''s Guard, Nimble Ring, Gem of Focus, Blood-Bound Book,
    Bragi''s Harp, Bancroft''s Talon, Chronos'' Pendant, Breastplate of Valor, Death
    Metal, Rod of Asclepius, Dreamer''s Idol, The World Stone, Helm of Radiance, Jade
    Scepter, Amanita Charm, Typhon’s Heart, Oni Hunter''s Garb, Yogi''s Necklace,
    Kinetic Cuirass.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.27
      fit: 0.58
    Doom Orb:
      total: 0.57
      efficiency: 0.49
      win: 0.72
      pick: 0.06
      fit: 0.46
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.44
      win: 0.63
      pick: 0.26
      fit: 0.46
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.16
      fit: 0.46
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.61
      pick: 0.21
      fit: 0.8
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Doom Orb, Gluttonous Grimoire, Genji''s Guard, Spear of the Magus, The Cosmic
    Horror, Death Metal, Gem of Focus, Bragi''s Harp, Breastplate of Valor, Bracer
    of The Abyss, Chronos'' Pendant, Blood-Bound Book, Bancroft''s Talon, Nimble Ring,
    Dreamer''s Idol, Rod of Asclepius, Amanita Charm, The World Stone, Freya''s Tears,
    Oni Hunter''s Garb, Helm of Radiance, Yogi''s Necklace, Kinetic Cuirass, Shield
    of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.16
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.27
      fit: 0.56
    Doom Orb:
      total: 0.56
      efficiency: 0.49
      win: 0.72
      pick: 0.06
      fit: 0.4
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.44
      win: 0.63
      pick: 0.26
      fit: 0.4
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.64
      pick: 0.16
      fit: 0.4
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.61
      pick: 0.21
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Doom Orb
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Shield of the
    Phoenix, Blood-Bound Book, Kinetic Cuirass, Bancroft''s Talon, Genji''s Guard,
    Eye of Providence, Oni Hunter''s Garb, Chandra''s Grace, Lifebinder, Breastplate
    of Valor, Spear of the Magus, Freya''s Tears, Shifter''s Shield, Yogi''s Necklace,
    Bracer of The Abyss, Phoenix Feather, Spectral Armor, The Cosmic Horror, Jade
    Scepter, Helm of Radiance, Erosion, Umbral Link.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.27
      fit: 0.36
    Doom Orb:
      total: 0.54
      efficiency: 0.49
      win: 0.72
      pick: 0.06
      fit: 0.28
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.64
      pick: 0.16
      fit: 0.28
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.61
      pick: 0.21
      fit: 0.83
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
  - Rod of Tahuti
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Doom Orb, Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Genji''s Guard, Bracer of The Abyss, Dreamer''s Idol, The World Stone, Nimble
    Ring, Blood-Bound Book, Screeching Gargoyle, Bancroft''s Talon, Breastplate of
    Valor, Bragi''s Harp, Chronos'' Pendant, Death Metal, Rod of Asclepius, Helm of
    Radiance, Amanita Charm, Oni Hunter''s Garb, Jade Scepter, Stone of Binding, Yogi''s
    Necklace.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.6
      pick: 0.27
      fit: 0.66
    Doom Orb:
      total: 0.58
      efficiency: 0.49
      win: 0.72
      pick: 0.06
      fit: 0.56
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.44
      win: 0.63
      pick: 0.26
      fit: 0.56
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.64
      pick: 0.16
      fit: 0.56
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.61
      pick: 0.21
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Doom Orb
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Doom Orb, Gluttonous Grimoire, Genji''s Guard, Spear of the Magus, Bracer
    of The Abyss, Bragi''s Harp, Death Metal, The Cosmic Horror, Nimble Ring, Breastplate
    of Valor, Blood-Bound Book, Bancroft''s Talon, Chronos'' Pendant, Rod of Asclepius,
    Amanita Charm, Oni Hunter''s Garb, Helm of Radiance, Yogi''s Necklace, Kinetic
    Cuirass, Jade Scepter, Dreamer''s Idol, Freya''s Tears, The World Stone, Eye of
    Providence.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.56
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
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.63
    Doom Orb:
      total: 0.54
      efficiency: 0.49
      win: 0.72
      pick: 0.06
      fit: 0.31
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.64
      pick: 0.16
      fit: 0.31
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.61
      pick: 0.21
      fit: 0.57
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
  - Obsidian Shard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Gluttonous Grimoire,
    Breastplate of Valor, Gem of Focus, Chronos'' Pendant, Freya''s Tears, Shield
    of the Phoenix, Spear of the Magus, Bracer of The Abyss, The Cosmic Horror, Death
    Metal, Bragi''s Harp, Screeching Gargoyle, Chandra''s Grace, Blood-Bound Book,
    Amanita Charm, Nimble Ring, Bancroft''s Talon, Oni Hunter''s Garb, Yogi''s Necklace,
    Kinetic Cuirass, Rod of Asclepius, Helm of Radiance, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.6
      pick: 0.27
      fit: 0.6
    Doom Orb:
      total: 0.54
      efficiency: 0.49
      win: 0.72
      pick: 0.06
      fit: 0.26
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.64
      pick: 0.16
      fit: 0.26
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.61
      pick: 0.21
      fit: 0.78
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
  - Spear of Desolation
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge, The
    Crusher, Hydra''s Lament, Death Metal, The Reaper, Lernaean Bow, Spear of the
    Magus, Runeforged Hammer, Genji''s Guard, Bragi''s Harp, Berserker''s Shield,
    The Cosmic Horror, Riptalon, Golden Blade, Damaru, Tekko-Kagi, Heartseeker, Blood-Bound
    Book, Dominance, Bancroft''s Talon, Breastplate of Valor, Bracer of The Abyss,
    Chronos'' Pendant, Avenging Blade, Tyrfing, Triton''s Conch, Rod of Asclepius,
    Pendulum Blade, Silverbranch Bow, Arondight, Titan''s Bane, Helm of Radiance,
    Nimble Ring, Amanita Charm, Shield Splitter, Dreamer''s Idol.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.27
      fit: 0.49
    Doom Orb:
      total: 0.56
      efficiency: 0.49
      win: 0.72
      pick: 0.06
      fit: 0.39
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.64
      pick: 0.16
      fit: 0.39
    Soul Gem:
      total: 0.59
      efficiency: 0.59
      win: 0.61
      pick: 0.21
      fit: 0.69
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Doom Orb, Gluttonous Grimoire, Jotunn''s
    Revenge, The Crusher, Berserker''s Shield, Lernaean Bow, Hydra''s Lament, Death
    Metal, Bragi''s Harp, Spear of the Magus, Riptalon, Genji''s Guard, Bracer of
    The Abyss, The Cosmic Horror, Golden Blade, The Reaper, Runeforged Hammer, Tekko-Kagi,
    Dominance, Silverbranch Bow, Blood-Bound Book, Nimble Ring, Bancroft''s Talon,
    Breastplate of Valor, Tyrfing, Chronos'' Pendant, Damaru, Rod of Asclepius, Pharaoh''s
    Curse, Helm of Radiance, Heartseeker, Amanita Charm, Jade Scepter, Dreamer''s
    Idol, Oni Hunter''s Garb, The World Stone, Triton''s Conch.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.27
      fit: 0.48
    Doom Orb:
      total: 0.55
      efficiency: 0.49
      win: 0.72
      pick: 0.06
      fit: 0.38
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.64
      pick: 0.16
      fit: 0.38
    Soul Gem:
      total: 0.59
      efficiency: 0.59
      win: 0.61
      pick: 0.21
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, Bracer of The
    Abyss, The Cosmic Horror, Genji''s Guard, Nimble Ring, Blood-Bound Book, Bragi''s
    Harp, Bancroft''s Talon, Chronos'' Pendant, Breastplate of Valor, Death Metal,
    Rod of Asclepius, Dreamer''s Idol, The World Stone, Helm of Radiance, Doom Orb,
    Jade Scepter, Gem of Focus, Amanita Charm, Typhon’s Heart, Oni Hunter''s Garb,
    Yogi''s Necklace, Kinetic Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.12
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.27
      fit: 0.58
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.46
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Bracer of The Abyss
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Rod of Tahuti
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Spear of the
    Magus, Bracer of The Abyss, The Cosmic Horror, Genji''s Guard, Nimble Ring, Blood-Bound
    Book, Bragi''s Harp, Bancroft''s Talon, Chronos'' Pendant, Breastplate of Valor,
    Death Metal, Rod of Asclepius, Dreamer''s Idol, The World Stone, Helm of Radiance,
    Doom Orb, Jade Scepter, Gem of Focus, Amanita Charm, Typhon’s Heart, Oni Hunter''s
    Garb, Yogi''s Necklace, Kinetic Cuirass.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.67
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.46
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.44
      win: 0.63
      pick: 0.26
      fit: 0.46
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.16
      fit: 0.46
  swaps:
  - added: Rod of Tahuti
    removed: Genji's Guard
    reason: community 63% win over 149 matches (vs 53% on this god), taking the model's
      weakest slot from Genji's Guard
  - added: Obsidian Shard
    removed: Spear of Desolation
    reason: community 64% win over 92 matches (vs 53% on this god), taking the model's
      weakest slot from Spear of Desolation
  starter: *id001
---
