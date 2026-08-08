---
type: smite-build
god: Morgan Le Fay
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cursed Crown
  aspect_pick_rate: 0.4
  aspect_win_rate: 0.56
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.24
    win_rate: 0.45
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.18
      win_rate: 0.48
    - name: Lifebinder
      pick_rate: 0.12
      win_rate: 0.56
  - name: Soul Reaver
    pick_rate: 0.14
    win_rate: 0.47
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.42
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.48
  - name: Soul Gem
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.49
    - name: Ethereal Staff
      pick_rate: 0.08
      win_rate: 0.51
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.53
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.48
    - name: Ethereal Staff
      pick_rate: 0.07
      win_rate: 0.53
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.53
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.33
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.45
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.5
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.57
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.42
    win_rate: 0.56
  - name: Bluestone Pendant
    pick_rate: 0.26
    win_rate: 0.43
  - name: Sundering Axe
    pick_rate: 0.09
    win_rate: 0.78
  source_url: https://smitebrain.com/gods/morgan-le-fay/
  last_verified: '2026-08-08'
  god_win_rate: 0.5028790786948176
  god_matches_won: 524
  god_matches_played: 1042
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-08'
  god_matches_analyzed: 14443
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The Cosmic Horror
  - Rod of Tahuti
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
    this god: Gluttonous Grimoire, Soul Gem, Obsidian Shard, Spear of the Magus, The
    Cosmic Horror, Dreamer''s Idol, The World Stone, Doom Orb, Genji''s Guard, Gem
    of Focus, Death Metal, Rod of Asclepius, Blood-Bound Book, Helm of Radiance, Bancroft''s
    Talon, Jade Scepter, Breastplate of Valor, Bracer of The Abyss, Ethereal Staff,
    Wish-Granting Pearl, Polynomicon, Ancient Signet, Alchemist Coat, Typhon’s Heart.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.45
      pick: 0.24
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.44
      win: 0.53
      pick: 0.17
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Obsidian Shard, Spear of the Magus, The Cosmic
    Horror, Genji''s Guard, Death Metal, Breastplate of Valor, Dreamer''s Idol, The
    World Stone, Doom Orb, Gem of Focus, Bragi''s Harp, Rod of Asclepius, Freya''s
    Tears, Blood-Bound Book, Helm of Radiance, Bancroft''s Talon, Shield of the Phoenix,
    Jade Scepter, Amanita Charm, Triton''s Conch, Bracer of The Abyss, Oni Hunter''s
    Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.22
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.45
      pick: 0.24
      fit: 0.78
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.56
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Rod of Asclepius, Lifebinder, Kinetic Cuirass, Eye of Providence, Genji''s Guard,
    Oni Hunter''s Garb, Blood-Bound Book, Bancroft''s Talon, Chandra''s Grace, Spear
    of the Magus, Shifter''s Shield, Breastplate of Valor, Freya''s Tears, The Cosmic
    Horror, Phoenix Feather, Spectral Armor, Jade Scepter, Erosion, Helm of Radiance,
    Yogi''s Necklace, Draconic Scale, Wish-Granting Pearl.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.51
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.26
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
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
    for this god: Gluttonous Grimoire, Soul Gem, Obsidian Shard, Spear of the Magus,
    The Cosmic Horror, Dreamer''s Idol, The World Stone, Doom Orb, Genji''s Guard,
    Screeching Gargoyle, Death Metal, Rod of Asclepius, Breastplate of Valor, Blood-Bound
    Book, Helm of Radiance, Bancroft''s Talon, Gem of Focus, Jade Scepter, Bracer
    of The Abyss, Ethereal Staff, Wish-Granting Pearl, Polynomicon, Amanita Charm,
    Ancient Signet.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.45
      pick: 0.24
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.44
      win: 0.53
      pick: 0.17
      fit: 0.85
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Obsidian Shard, Genji''s Guard, Spear
    of the Magus, Bracer of The Abyss, Bragi''s Harp, Death Metal, The Cosmic Horror,
    Nimble Ring, Breastplate of Valor, Blood-Bound Book, Bancroft''s Talon, Rod of
    Asclepius, Amanita Charm, Oni Hunter''s Garb, Helm of Radiance, Yogi''s Necklace,
    Kinetic Cuirass, Jade Scepter, Dreamer''s Idol, The World Stone, Freya''s Tears,
    Doom Orb, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.08
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
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Gluttonous
    Grimoire, Breastplate of Valor, Obsidian Shard, Freya''s Tears, Shield of the
    Phoenix, Gem of Focus, Spear of the Magus, The Cosmic Horror, Screeching Gargoyle,
    Chandra''s Grace, Death Metal, Gladiator''s Shield, Amanita Charm, Rod of Asclepius,
    Oni Hunter''s Garb, Dreamer''s Idol, The World Stone, Yogi''s Necklace, Blood-Bound
    Book, Doom Orb, Kinetic Cuirass, Helm of Radiance, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.56
      win: 0.48
      pick: 0.18
      fit: 0.63
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.45
      pick: 0.24
      fit: 0.86
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.37
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Hydra's Lament
  - Death Metal
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
    win/pick). Underrated for this god: Jotunn''s Revenge, The Crusher, Gluttonous
    Grimoire, Soul Gem, Obsidian Shard, Hydra''s Lament, Death Metal, Spear of the
    Magus, Lernaean Bow, Bragi''s Harp, Runeforged Hammer, The Cosmic Horror, The
    Reaper, Berserker''s Shield, Genji''s Guard, Golden Blade, Tekko-Kagi, Damaru,
    Heartseeker, Dominance, Bracer of The Abyss, Tyrfing, Breastplate of Valor, Triton''s
    Conch, Riptalon, Pendulum Blade, Avenging Blade, Titan''s Bane, Rod of Asclepius,
    Arondight, Silverbranch Bow, Blood-Bound Book, Dreamer''s Idol, Helm of Radiance,
    The World Stone, Bancroft''s Talon, Doom Orb, Shield Splitter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.65
    Hydra's Lament:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.53
    Death Metal:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of the Magus
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Death Metal
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Gluttonous
    Grimoire, The Crusher, Obsidian Shard, Death Metal, Spear of the Magus, Hydra''s
    Lament, The Cosmic Horror, The Reaper, Runeforged Hammer, Genji''s Guard, Bragi''s
    Harp, Heartseeker, Dreamer''s Idol, Triton''s Conch, Lernaean Bow, The World Stone,
    Doom Orb, Damaru, Rod of Asclepius, Pendulum Blade, Blood-Bound Book, Breastplate
    of Valor, Helm of Radiance, Bancroft''s Talon, Berserker''s Shield, Titan''s Bane,
    Jade Scepter, Tekko-Kagi, Gem of Focus, Bracer of The Abyss, Arondight, Avenging
    Blade, Golden Blade, Wish-Granting Pearl, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.69
    Death Metal:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.56
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.79
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
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The
    Cosmic Horror, Obsidian Shard, Dreamer''s Idol, The World Stone, Doom Orb, Genji''s
    Guard, Gem of Focus, Death Metal, Rod of Asclepius, Blood-Bound Book, Helm of
    Radiance, Bancroft''s Talon, Jade Scepter, Breastplate of Valor, Bracer of The
    Abyss, Wish-Granting Pearl, Polynomicon, Ethereal Staff, Ancient Signet, Alchemist
    Coat, Typhon’s Heart.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.56
      win: 0.48
      pick: 0.18
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.45
      pick: 0.24
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Rod of Asclepius, Lifebinder,
    Obsidian Shard, Shield of the Phoenix, Oni Hunter''s Garb, Genji''s Guard, Kinetic
    Cuirass, Spear of the Magus, Chandra''s Grace, The Cosmic Horror, Eye of Providence,
    Jade Scepter, Ethereal Staff, Yogi''s Necklace, Blood-Bound Book, Bancroft''s
    Talon, Wish-Granting Pearl, Alchemist Coat, Breastplate of Valor, Shifter''s Shield,
    Phoenix Feather, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.25
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.48
    Oni Hunter's Garb:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.85
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.47
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.92
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Oni Hunter's Garb
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Oni Hunter's Garb
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
    god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Obsidian Shard, Rod of Asclepius,
    Lifebinder, Genji''s Guard, Shield of the Phoenix, Spear of the Magus, The Cosmic
    Horror, Chandra''s Grace, Oni Hunter''s Garb, Kinetic Cuirass, Death Metal, Blood-Bound
    Book, Bancroft''s Talon, Breastplate of Valor, Eye of Providence, Yogi''s Necklace,
    Jade Scepter, Ethereal Staff, Freya''s Tears, Triton''s Conch, Wish-Granting Pearl,
    Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.24
    Oni Hunter's Garb:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.24
    The Cosmic Horror:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.42
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.42
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.42
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.89
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Rod of Asclepius, Lifebinder, Kinetic Cuirass, Eye of Providence, Genji''s Guard,
    Oni Hunter''s Garb, Chandra''s Grace, Blood-Bound Book, Shifter''s Shield, Bancroft''s
    Talon, Freya''s Tears, Breastplate of Valor, Spear of the Magus, Erosion, Phoenix
    Feather, Spectral Armor, Yogi''s Necklace, The Cosmic Horror, Draconic Scale,
    Jade Scepter, Helm of Radiance, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.63
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.83
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.87
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Obsidian Shard, Amanita Charm, Spear
    of the Magus, Rod of Asclepius, The Cosmic Horror, Lifebinder, Shield of the Phoenix,
    Genji''s Guard, Oni Hunter''s Garb, Kinetic Cuirass, Chandra''s Grace, Eye of
    Providence, Screeching Gargoyle, Dreamer''s Idol, The World Stone, Blood-Bound
    Book, Doom Orb, Void Stone, Yogi''s Necklace, Bancroft''s Talon, Jade Scepter,
    Void Shield, Breastplate of Valor, Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.2
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.9
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.45
      pick: 0.24
      fit: 0.7
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.59
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
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
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Lifebinder,
    Obsidian Shard, Genji''s Guard, Shield of the Phoenix, Blood-Bound Book, Bancroft''s
    Talon, Oni Hunter''s Garb, Kinetic Cuirass, Chandra''s Grace, Yogi''s Necklace,
    Spear of the Magus, Eye of Providence, Bracer of The Abyss, Death Metal, Breastplate
    of Valor, The Cosmic Horror, Bragi''s Harp, Jade Scepter, Spectral Armor, Nimble
    Ring, Wish-Granting Pearl, Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.12
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.31
    Nimble Ring:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.37
    Bragi's Harp:
      total: 0.46
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.51
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.23
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.67
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, Genji''s
    Guard, Shield of the Phoenix, Amanita Charm, Chandra''s Grace, Breastplate of
    Valor, Rod of Asclepius, Lifebinder, Freya''s Tears, Oni Hunter''s Garb, Kinetic
    Cuirass, Eye of Providence, Yogi''s Necklace, Spear of the Magus, Screeching Gargoyle,
    Blood-Bound Book, Bancroft''s Talon, Gem of Focus, The Cosmic Horror, Jade Scepter,
    Death Metal, Gladiator''s Shield, Spectral Armor, Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.43
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Freya's Tears:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.49
      efficiency: 0.52
      win: 0.45
      pick: 0.24
      fit: 0.64
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.28
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.94
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Crusher
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Hydra's Lament
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Amanita Charm, Runeforged Hammer, Berserker''s Shield, Rod of Asclepius,
    Lifebinder, The Reaper, Hydra''s Lament, Golden Blade, Genji''s Guard, Shield
    of the Phoenix, Death Metal, Riptalon, Oni Hunter''s Garb, Lernaean Bow, Kinetic
    Cuirass, Avenging Blade, Spear of the Magus, Eye of the Storm, Chandra''s Grace,
    Blood-Bound Book, Pharaoh''s Curse, Eye of Providence, Bancroft''s Talon, Yogi''s
    Necklace, The Cosmic Horror, Bragi''s Harp, Triton''s Conch, Damaru, Jade Scepter,
    Breastplate of Valor, Dominance, Tekko-Kagi, Heartseeker, Shogun''s Ofuda, Shield
    Splitter.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.53
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.7
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Runeforged Hammer
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Runeforged Hammer
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Soul Gem, Jotunn''s
    Revenge, The Crusher, Amanita Charm, Rod of Asclepius, Lifebinder, Obsidian Shard,
    Runeforged Hammer, The Reaper, Death Metal, Hydra''s Lament, Berserker''s Shield,
    Shield of the Phoenix, Genji''s Guard, Spear of the Magus, Oni Hunter''s Garb,
    Blood-Bound Book, Bancroft''s Talon, The Cosmic Horror, Kinetic Cuirass, Jade
    Scepter, Triton''s Conch, Chandra''s Grace, Ethereal Staff, Avenging Blade, Eye
    of Providence, Golden Blade, Eye of the Storm, Yogi''s Necklace, Riptalon, Wish-Granting
    Pearl, Alchemist Coat, Breastplate of Valor, Lernaean Bow, Bragi''s Harp, Damaru,
    Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.58
      pick: 0.13
      fit: 0.41
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Spear of the Magus
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Rod of
    Asclepius, Shield of the Phoenix, Genji''s Guard, Oni Hunter''s Garb, Kinetic
    Cuirass, Spear of the Magus, Chandra''s Grace, Lifebinder, The Cosmic Horror,
    Eye of Providence, Jade Scepter, Yogi''s Necklace, Blood-Bound Book, Bancroft''s
    Talon, Wish-Granting Pearl, Ethereal Staff, Obsidian Shard, Alchemist Coat, Breastplate
    of Valor, Shifter''s Shield, Phoenix Feather, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.48
      pick: 0.09
      fit: 0.25
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.48
    Oni Hunter's Garb:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.15
      fit: 0.92
  starter: *id001
  aspect: Aspect of the Cursed Crown
---
