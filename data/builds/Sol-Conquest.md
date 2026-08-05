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
    this god: Gluttonous Grimoire, Obsidian Shard, Bracer of The Abyss, Nimble Ring,
    Spear of the Magus, Ethereal Staff, Bragi''s Harp, Genji''s Guard, Bancroft''s
    Talon, The Cosmic Horror, Blood-Bound Book, Death Metal, Chronos'' Pendant, Wish-Granting
    Pearl, Jade Scepter, Rod of Asclepius, Breastplate of Valor, Dreamer''s Idol,
    Typhon’s Heart, Oni Hunter''s Garb, Helm of Radiance, Gem of Focus, Yogi''s Necklace,
    The World Stone, Kinetic Cuirass.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.25
      fit: 0.58
    Spear of the Magus:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.47
      win: 0.59
      pick: 0.25
      fit: 0.46
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.14
      fit: 0.46
    Soul Gem:
      total: 0.63
      efficiency: 0.62
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
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Bragi's Harp
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
    god: Gluttonous Grimoire, Obsidian Shard, Genji''s Guard, Bragi''s Harp, Spear
    of the Magus, Death Metal, Bracer of The Abyss, Ethereal Staff, The Cosmic Horror,
    Nimble Ring, Breastplate of Valor, Bancroft''s Talon, Blood-Bound Book, Chronos''
    Pendant, Wish-Granting Pearl, Oni Hunter''s Garb, Jade Scepter, Dreamer''s Idol,
    Yogi''s Necklace, Rod of Asclepius, Triton''s Conch, Kinetic Cuirass, Shield of
    the Phoenix, Amanita Charm, Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.16
    Bragi's Harp:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.25
      fit: 0.56
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.47
      win: 0.59
      pick: 0.25
      fit: 0.4
    Obsidian Shard:
      total: 0.51
      efficiency: 0.55
      win: 0.57
      pick: 0.14
      fit: 0.4
    Soul Gem:
      total: 0.62
      efficiency: 0.62
      win: 0.64
      pick: 0.17
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Ethereal Staff
  - Gluttonous Grimoire
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Amanita Charm, Shield of the Phoenix, Rod of Asclepius,
    Bancroft''s Talon, Blood-Bound Book, Kinetic Cuirass, Chandra''s Grace, Ethereal
    Staff, Genji''s Guard, Oni Hunter''s Garb, Eye of Providence, Lifebinder, Spectral
    Armor, Wish-Granting Pearl, Bracer of The Abyss, Jade Scepter, Yogi''s Necklace,
    Breastplate of Valor, Phoenix Feather, Shifter''s Shield, Spear of the Magus,
    Mantle Of Discord, Nimble Ring, Freya''s Tears, Erosion.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.19
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.48
    Oni Hunter's Garb:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.26
    Ethereal Staff:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.6
    Soul Gem:
      total: 0.64
      efficiency: 0.62
      win: 0.64
      pick: 0.17
      fit: 0.83
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Obsidian Shard, Spear of the Magus, The Cosmic
    Horror, Bracer of The Abyss, Ethereal Staff, Nimble Ring, Genji''s Guard, Dreamer''s
    Idol, Bragi''s Harp, Bancroft''s Talon, Blood-Bound Book, The World Stone, Doom
    Orb, Death Metal, Wish-Granting Pearl, Chronos'' Pendant, Jade Scepter, Breastplate
    of Valor, Screeching Gargoyle, Rod of Asclepius, Oni Hunter''s Garb, Yogi''s Necklace,
    Kinetic Cuirass.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.56
      pick: 0.25
      fit: 0.66
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.47
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
      total: 0.64
      efficiency: 0.62
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
    this god: Gluttonous Grimoire, Bragi''s Harp, Obsidian Shard, Bracer of The Abyss,
    Genji''s Guard, Ethereal Staff, Death Metal, Nimble Ring, Spear of the Magus,
    Bancroft''s Talon, Blood-Bound Book, The Cosmic Horror, Wish-Granting Pearl, Breastplate
    of Valor, Oni Hunter''s Garb, Jade Scepter, Rod of Asclepius, Chronos'' Pendant,
    Yogi''s Necklace, Kinetic Cuirass, Amanita Charm, Triton''s Conch, Spectral Armor,
    Helm of Radiance, Typhon’s Heart.'
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
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.25
      fit: 0.39
    Obsidian Shard:
      total: 0.5
      efficiency: 0.55
      win: 0.57
      pick: 0.14
      fit: 0.31
    Soul Gem:
      total: 0.6
      efficiency: 0.62
      win: 0.64
      pick: 0.17
      fit: 0.57
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
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Genji''s Guard,
    Breastplate of Valor, Chronos'' Pendant, Shield of the Phoenix, Bracer of The
    Abyss, Bragi''s Harp, Chandra''s Grace, Ethereal Staff, Freya''s Tears, Death
    Metal, Gem of Focus, Spear of the Magus, Nimble Ring, Bancroft''s Talon, Blood-Bound
    Book, Oni Hunter''s Garb, The Cosmic Horror, Yogi''s Necklace, Kinetic Cuirass,
    Wish-Granting Pearl, Screeching Gargoyle, Amanita Charm, Jade Scepter, Rod of
    Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.34
    Chronos' Pendant:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.25
      fit: 0.6
    Obsidian Shard:
      total: 0.49
      efficiency: 0.55
      win: 0.57
      pick: 0.14
      fit: 0.26
    Soul Gem:
      total: 0.63
      efficiency: 0.62
      win: 0.64
      pick: 0.17
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Crusher
  - Soul Gem
  flex_slots:
  - Runeforged Hammer
  - Lernaean Bow
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
    win/pick). Underrated for this god: Gluttonous Grimoire, The Crusher, Jotunn''s
    Revenge, Hydra''s Lament, Runeforged Hammer, Lernaean Bow, Death Metal, The Reaper,
    Bragi''s Harp, Obsidian Shard, Golden Blade, Avenging Blade, Berserker''s Shield,
    Ethereal Staff, Spear of the Magus, Damaru, Heartseeker, Genji''s Guard, Riptalon,
    Triton''s Conch, Tekko-Kagi, Avatar''s Parashu, Arondight, Bancroft''s Talon,
    Blood-Bound Book, The Cosmic Horror, Bracer of The Abyss, Tyrfing, Barbed Carver,
    Nimble Ring, Wish-Granting Pearl, Pendulum Blade, Chronos'' Pendant, Jade Scepter,
    Titan''s Bane, Breastplate of Valor, Bloodforge.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.49
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.39
    The Crusher:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.62
      efficiency: 0.62
      win: 0.64
      pick: 0.17
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Bragi's Harp
  - The Crusher
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Bragi's Harp
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
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, The Crusher,
    Jotunn''s Revenge, Lernaean Bow, Hydra''s Lament, Bragi''s Harp, Berserker''s
    Shield, Runeforged Hammer, Death Metal, Obsidian Shard, Golden Blade, Riptalon,
    Bracer of The Abyss, The Reaper, Ethereal Staff, Spear of the Magus, Nimble Ring,
    Genji''s Guard, Tekko-Kagi, Avenging Blade, Bancroft''s Talon, Blood-Bound Book,
    The Cosmic Horror, Tyrfing, Damaru, Heartseeker, Pharaoh''s Curse, Triton''s Conch,
    Wish-Granting Pearl, Jade Scepter, Chronos'' Pendant, Arondight, Rod of Asclepius,
    Avatar''s Parashu, Breastplate of Valor, Oni Hunter''s Garb, Yogi''s Necklace.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.48
    Hydra's Lament:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.4
    Bragi's Harp:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.75
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.48
    Soul Gem:
      total: 0.61
      efficiency: 0.62
      win: 0.64
      pick: 0.17
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Bragi's Harp
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of the Magus
  flex_slots:
  - Bragi's Harp
  - Genji's Guard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Bracer of The Abyss, Nimble Ring,
    Spear of the Magus, Ethereal Staff, Bragi''s Harp, Genji''s Guard, Bancroft''s
    Talon, The Cosmic Horror, Blood-Bound Book, Death Metal, Chronos'' Pendant, Wish-Granting
    Pearl, Obsidian Shard, Jade Scepter, Rod of Asclepius, Breastplate of Valor, Dreamer''s
    Idol, Typhon’s Heart, Oni Hunter''s Garb, Helm of Radiance, Gem of Focus, Yogi''s
    Necklace, The World Stone, Kinetic Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.12
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.54
    Bragi's Harp:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.64
    Ethereal Staff:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.24
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spear of the Magus:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
---
