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
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Obsidian Shard, Gluttonous Grimoire, Spear of the Magus, The Cosmic
    Horror, Ethereal Staff, Chronos'' Pendant, Dreamer''s Idol, Genji''s Guard, The
    World Stone, Death Metal, Doom Orb, Gem of Focus, Wish-Granting Pearl, Jade Scepter,
    Bancroft''s Talon, Rod of Asclepius, Blood-Bound Book, Bracer of The Abyss, Breastplate
    of Valor, Helm of Radiance, Alchemist Coat, Polynomicon, Bragi''s Harp, Soul Reaver.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
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
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.47
      win: 0.56
      pick: 0.19
      fit: 0.77
    Obsidian Shard:
      total: 0.61
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.77
    Soul Gem:
      total: 0.63
      efficiency: 0.62
      win: 0.56
      pick: 0.17
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Death Metal
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Obsidian Shard, Gluttonous Grimoire, Spear of the Magus, Genji''s Guard,
    Death Metal, The Cosmic Horror, Ethereal Staff, Chronos'' Pendant, Breastplate
    of Valor, Dreamer''s Idol, Bragi''s Harp, Triton''s Conch, Wish-Granting Pearl,
    The World Stone, Gem of Focus, Jade Scepter, Doom Orb, Bancroft''s Talon, Rod
    of Asclepius, Blood-Bound Book, Bracer of The Abyss, Shield of the Phoenix, Oni
    Hunter''s Garb, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.74
      win: 0.5
      pick: 0.11
      fit: 0.22
    Death Metal:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.59
      pick: 0.31
      fit: 0.78
    Spear of the Magus:
      total: 0.52
      efficiency: 0.62
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
      total: 0.61
      efficiency: 0.62
      win: 0.56
      pick: 0.17
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Chandra''s Grace, Eye of Providence,
    Oni Hunter''s Garb, Bancroft''s Talon, Blood-Bound Book, Lifebinder, Spectral
    Armor, Wish-Granting Pearl, Jade Scepter, Shifter''s Shield, Phoenix Feather,
    Breastplate of Valor, Spear of the Magus, Yogi''s Necklace, Freya''s Tears, Erosion,
    Draconic Scale, Mantle Of Discord, Alchemist Coat.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.6
    Ethereal Staff:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.59
      pick: 0.31
      fit: 0.5
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.38
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.61
      efficiency: 0.62
      win: 0.56
      pick: 0.17
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Obsidian Shard, Gluttonous Grimoire, Spear of the Magus, The Cosmic
    Horror, Dreamer''s Idol, The World Stone, Doom Orb, Ethereal Staff, Genji''s Guard,
    Chronos'' Pendant, Death Metal, Wish-Granting Pearl, Jade Scepter, Bancroft''s
    Talon, Rod of Asclepius, Blood-Bound Book, Breastplate of Valor, Bracer of The
    Abyss, Screeching Gargoyle, Gem of Focus, Helm of Radiance, Alchemist Coat, Oni
    Hunter''s Garb, Polynomicon.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.59
      pick: 0.31
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.84
    Spear of the Magus:
      total: 0.57
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.47
      win: 0.56
      pick: 0.19
      fit: 0.84
    Obsidian Shard:
      total: 0.62
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.84
    Soul Gem:
      total: 0.63
      efficiency: 0.62
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
  - Bracer of The Abyss
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
    this god: Gluttonous Grimoire, Obsidian Shard, Bragi''s Harp, Genji''s Guard,
    Bracer of The Abyss, Ethereal Staff, Death Metal, Nimble Ring, Spear of the Magus,
    Bancroft''s Talon, Blood-Bound Book, The Cosmic Horror, Breastplate of Valor,
    Wish-Granting Pearl, Jade Scepter, Oni Hunter''s Garb, Chronos'' Pendant, Rod
    of Asclepius, Yogi''s Necklace, Kinetic Cuirass, Triton''s Conch, Amanita Charm,
    Helm of Radiance, Typhon’s Heart, Spectral Armor.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
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
      total: 0.57
      efficiency: 0.62
      win: 0.56
      pick: 0.17
      fit: 0.58
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
  - Breastplate of Valor
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Obsidian Shard, Gluttonous
    Grimoire, Breastplate of Valor, Chronos'' Pendant, Shield of the Phoenix, Gem
    of Focus, Chandra''s Grace, Freya''s Tears, Spear of the Magus, Death Metal, Ethereal
    Staff, Screeching Gargoyle, The Cosmic Horror, Gladiator''s Shield, Oni Hunter''s
    Garb, Wish-Granting Pearl, Jade Scepter, Yogi''s Necklace, Bragi''s Harp, Bancroft''s
    Talon, Rod of Asclepius, Blood-Bound Book, Dreamer''s Idol, Kinetic Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.74
      win: 0.5
      pick: 0.11
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.59
      pick: 0.31
      fit: 0.86
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.37
    Soul Gem:
      total: 0.62
      efficiency: 0.62
      win: 0.56
      pick: 0.17
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Obsidian Shard, The Crusher,
    Gluttonous Grimoire, Hydra''s Lament, Lernaean Bow, Death Metal, Runeforged Hammer,
    Bragi''s Harp, The Reaper, Golden Blade, Genji''s Guard, Spear of the Magus, Avenging
    Blade, Heartseeker, Ethereal Staff, Damaru, Berserker''s Shield, Triton''s Conch,
    Tekko-Kagi, Arondight, Avatar''s Parashu, The Cosmic Horror, Bracer of The Abyss,
    Tyrfing, Pendulum Blade, Riptalon, Chronos'' Pendant, Wish-Granting Pearl, Titan''s
    Bane, Jade Scepter, Breastplate of Valor, Bancroft''s Talon, Rod of Asclepius,
    Blood-Bound Book, Shield Splitter, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.65
    Hydra's Lament:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.59
      pick: 0.31
      fit: 0.56
    The Crusher:
      total: 0.56
      efficiency: 0.7
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
      total: 0.58
      efficiency: 0.62
      win: 0.56
      pick: 0.17
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Crusher
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Obsidian Shard, Jotunn''s Revenge,
    Gluttonous Grimoire, The Crusher, Hydra''s Lament, Death Metal, Runeforged Hammer,
    Spear of the Magus, Ethereal Staff, The Reaper, Bragi''s Harp, The Cosmic Horror,
    Lernaean Bow, Genji''s Guard, Triton''s Conch, Heartseeker, Avenging Blade, Avatar''s
    Parashu, Damaru, Chronos'' Pendant, Arondight, Pendulum Blade, Wish-Granting Pearl,
    Dreamer''s Idol, Jade Scepter, Bancroft''s Talon, Rod of Asclepius, Blood-Bound
    Book, Golden Blade, Bracer of The Abyss, Titan''s Bane, Tekko-Kagi, Berserker''s
    Shield, Breastplate of Valor, Gem of Focus, The World Stone, Helm of Radiance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.7
    Hydra's Lament:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.59
      pick: 0.31
      fit: 0.7
    The Crusher:
      total: 0.57
      efficiency: 0.7
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
      total: 0.6
      efficiency: 0.62
      win: 0.56
      pick: 0.17
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Ethereal Staff
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Obsidian Shard, Ethereal Staff, Chronos'' Pendant, Dreamer''s Idol, Genji''s Guard,
    The World Stone, Death Metal, Doom Orb, Gem of Focus, Wish-Granting Pearl, Jade
    Scepter, Bancroft''s Talon, Rod of Asclepius, Blood-Bound Book, Bracer of The
    Abyss, Breastplate of Valor, Helm of Radiance, Alchemist Coat, Polynomicon, Bragi''s
    Harp, Soul Reaver.'
  slot_scores:
    Ethereal Staff:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
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
      efficiency: 0.62
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
