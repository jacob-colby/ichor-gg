---
type: smite-build
god: Sol
mode: Conquest
builds:
- source: community
  aspect: Aspect of Conflagration
  aspect_pick_rate: 0.63
  aspect_win_rate: 0.59
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.25
    win_rate: 0.56
    alternates:
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.57
    - name: Tyrfing
      pick_rate: 0.14
      win_rate: 0.5
  - name: Book of Thoth
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.57
    - name: Doom Orb
      pick_rate: 0.08
      win_rate: 0.72
  - name: Soul Gem
    pick_rate: 0.17
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.43
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.53
  - name: Rod of Tahuti
    pick_rate: 0.25
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.5
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.56
  - name: Obsidian Shard
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.8
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.85
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.86
    - name: Qin's Blade
      pick_rate: 0.06
      win_rate: 0.83
  source_url: https://smitebrain.com/gods/sol/
  last_verified: '2026-08-01'
  god_win_rate: 0.5409090909090909
  god_matches_won: 119
  god_matches_played: 220
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
  - Bracer of The Abyss
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Doom Orb, Gluttonous Grimoire, Obsidian Shard, Spear of the Magus, Bracer
    of The Abyss, The Cosmic Horror, Nimble Ring, Genji''s Guard, Bragi''s Harp, Blood-Bound
    Book, Bancroft''s Talon, Chronos'' Pendant, Breastplate of Valor, Death Metal,
    Rod of Asclepius, The World Stone, Helm of Radiance, Dreamer''s Idol, Jade Scepter,
    Gem of Focus, Typhon’s Heart, Amanita Charm, Oni Hunter''s Garb, Kinetic Cuirass,
    Yogi''s Necklace.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.54
      efficiency: 0.54
      win: 0.56
      pick: 0.25
      fit: 0.58
    Doom Orb:
      total: 0.57
      efficiency: 0.5
      win: 0.72
      pick: 0.08
      fit: 0.46
    Spear of the Magus:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.14
      fit: 0.46
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.64
      pick: 0.17
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
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Spear of the Magus
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
    god: Doom Orb, Gluttonous Grimoire, Obsidian Shard, Genji''s Guard, Spear of the
    Magus, The Cosmic Horror, Death Metal, Bragi''s Harp, Bracer of The Abyss, Breastplate
    of Valor, Chronos'' Pendant, Blood-Bound Book, Bancroft''s Talon, Nimble Ring,
    Rod of Asclepius, The World Stone, Dreamer''s Idol, Amanita Charm, Helm of Radiance,
    Freya''s Tears, Oni Hunter''s Garb, Gem of Focus, Kinetic Cuirass, Yogi''s Necklace,
    Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.16
    Spear of Desolation:
      total: 0.54
      efficiency: 0.54
      win: 0.56
      pick: 0.25
      fit: 0.56
    Doom Orb:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.08
      fit: 0.4
    Spear of the Magus:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.4
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.14
      fit: 0.4
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.64
      pick: 0.17
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Doom Orb
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
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
    of Valor, Spear of the Magus, Freya''s Tears, Shifter''s Shield, Phoenix Feather,
    Bracer of The Abyss, The Cosmic Horror, Yogi''s Necklace, Spectral Armor, Helm
    of Radiance, Jade Scepter, Erosion, Umbral Link.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.19
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.51
      efficiency: 0.54
      win: 0.56
      pick: 0.25
      fit: 0.36
    Doom Orb:
      total: 0.55
      efficiency: 0.5
      win: 0.72
      pick: 0.08
      fit: 0.28
    Amanita Charm:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.64
      pick: 0.17
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
  - Spear of the Magus
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Doom Orb, Gluttonous Grimoire, Obsidian Shard, Spear of the Magus,
    The Cosmic Horror, Genji''s Guard, Bracer of The Abyss, The World Stone, Dreamer''s
    Idol, Nimble Ring, Screeching Gargoyle, Blood-Bound Book, Bancroft''s Talon, Bragi''s
    Harp, Breastplate of Valor, Chronos'' Pendant, Death Metal, Rod of Asclepius,
    Helm of Radiance, Amanita Charm, Stone of Binding, Jade Scepter, Oni Hunter''s
    Garb, Kinetic Cuirass.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.54
      win: 0.56
      pick: 0.25
      fit: 0.66
    Doom Orb:
      total: 0.59
      efficiency: 0.5
      win: 0.72
      pick: 0.08
      fit: 0.56
    Spear of the Magus:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.45
      win: 0.59
      pick: 0.25
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.14
      fit: 0.56
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.64
      pick: 0.17
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Doom Orb
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
    this god: Doom Orb, Gluttonous Grimoire, Obsidian Shard, Genji''s Guard, Spear
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
      total: 0.51
      efficiency: 0.54
      win: 0.56
      pick: 0.25
      fit: 0.39
    Doom Orb:
      total: 0.55
      efficiency: 0.5
      win: 0.72
      pick: 0.08
      fit: 0.31
    Soul Gem:
      total: 0.59
      efficiency: 0.59
      win: 0.64
      pick: 0.17
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
  - Breastplate of Valor
  - Obsidian Shard
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
    Breastplate of Valor, Obsidian Shard, Chronos'' Pendant, Freya''s Tears, Spear
    of the Magus, Shield of the Phoenix, Bracer of The Abyss, Gem of Focus, The Cosmic
    Horror, Bragi''s Harp, Death Metal, Screeching Gargoyle, Chandra''s Grace, Blood-Bound
    Book, Amanita Charm, Nimble Ring, Bancroft''s Talon, Oni Hunter''s Garb, Kinetic
    Cuirass, Yogi''s Necklace, Rod of Asclepius, Helm of Radiance, Eye of Providence.'
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
      total: 0.54
      efficiency: 0.54
      win: 0.56
      pick: 0.25
      fit: 0.6
    Doom Orb:
      total: 0.54
      efficiency: 0.5
      win: 0.72
      pick: 0.08
      fit: 0.26
    Obsidian Shard:
      total: 0.49
      efficiency: 0.55
      win: 0.57
      pick: 0.14
      fit: 0.26
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.64
      pick: 0.17
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Qin's Blade
  - Spear of Desolation
  - Doom Orb
  - The Crusher
  - Soul Gem
  flex_slots:
  - The Crusher
  - Spear of Desolation
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
    win/pick). Underrated for this god: Doom Orb, Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Obsidian Shard, Hydra''s Lament, Death Metal, The Reaper, Lernaean
    Bow, Spear of the Magus, Runeforged Hammer, Bragi''s Harp, Genji''s Guard, The
    Cosmic Horror, Berserker''s Shield, Golden Blade, Riptalon, Tekko-Kagi, Tyrfing,
    Damaru, Heartseeker, Blood-Bound Book, Dominance, Bancroft''s Talon, Bracer of
    The Abyss, Breastplate of Valor, Chronos'' Pendant, Avenging Blade, Triton''s
    Conch, Pendulum Blade, Rod of Asclepius, Titan''s Bane, Arondight, Silverbranch
    Bow, Helm of Radiance, Shield Splitter, Nimble Ring, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.59
    Qin's Blade:
      total: 0.55
      efficiency: 0.39
      win: 0.83
      pick: 0.06
      fit: 0.22
    Spear of Desolation:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.25
      fit: 0.49
    Doom Orb:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.08
      fit: 0.39
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.64
      pick: 0.17
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Qin's Blade
  - Spear of Desolation
  - Doom Orb
  - The Crusher
  - Soul Gem
  flex_slots:
  - The Crusher
  - Spear of Desolation
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
    Revenge, The Crusher, Obsidian Shard, Berserker''s Shield, Lernaean Bow, Bragi''s
    Harp, Hydra''s Lament, Death Metal, Spear of the Magus, Riptalon, Bracer of The
    Abyss, The Cosmic Horror, Genji''s Guard, Golden Blade, The Reaper, Runeforged
    Hammer, Tyrfing, Tekko-Kagi, Dominance, Blood-Bound Book, Silverbranch Bow, Nimble
    Ring, Bancroft''s Talon, Chronos'' Pendant, Breastplate of Valor, Rod of Asclepius,
    Damaru, Helm of Radiance, Pharaoh''s Curse, Heartseeker, Jade Scepter, Amanita
    Charm, The World Stone, Dreamer''s Idol, Triton''s Conch, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Qin's Blade:
      total: 0.56
      efficiency: 0.39
      win: 0.83
      pick: 0.06
      fit: 0.33
    Spear of Desolation:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.25
      fit: 0.48
    Doom Orb:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.08
      fit: 0.38
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.64
      pick: 0.17
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
    Abyss, The Cosmic Horror, Nimble Ring, Genji''s Guard, Bragi''s Harp, Obsidian
    Shard, Blood-Bound Book, Bancroft''s Talon, Chronos'' Pendant, Breastplate of
    Valor, Death Metal, Rod of Asclepius, The World Stone, Doom Orb, Helm of Radiance,
    Dreamer''s Idol, Jade Scepter, Gem of Focus, Typhon’s Heart, Amanita Charm, Oni
    Hunter''s Garb, Kinetic Cuirass, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.12
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.57
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
      total: 0.54
      efficiency: 0.54
      win: 0.56
      pick: 0.25
      fit: 0.58
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.46
    Spear of the Magus:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
---
