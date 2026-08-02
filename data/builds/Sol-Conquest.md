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
  - Blink Rune
  - Bracer of The Abyss
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
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
    this god: Gluttonous Grimoire, Blink Rune, Obsidian Shard, Bracer of The Abyss,
    Nimble Ring, Spear of the Magus, Ethereal Staff, Bragi''s Harp, Genji''s Guard,
    Bancroft''s Talon, The Cosmic Horror, Blood-Bound Book, Death Metal, Chronos''
    Pendant, Wish-Granting Pearl, Jade Scepter, Rod of Asclepius, Breastplate of Valor,
    Dreamer''s Idol, Typhon’s Heart, Oni Hunter''s Garb, Helm of Radiance, Gem of
    Focus, Yogi''s Necklace, The World Stone, Kinetic Cuirass.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
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
  - Blink Rune
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Rod of Tahuti
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
    god: Gluttonous Grimoire, Blink Rune, Obsidian Shard, Genji''s Guard, Bragi''s
    Harp, Spear of the Magus, Death Metal, Bracer of The Abyss, Ethereal Staff, The
    Cosmic Horror, Nimble Ring, Breastplate of Valor, Bancroft''s Talon, Blood-Bound
    Book, Chronos'' Pendant, Wish-Granting Pearl, Oni Hunter''s Garb, Jade Scepter,
    Dreamer''s Idol, Yogi''s Necklace, Rod of Asclepius, Triton''s Conch, Kinetic
    Cuirass, Shield of the Phoenix, Amanita Charm, Gem of Focus.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Genji's Guard:
      total: 0.51
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.16
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
  - Blink Rune
  - Genji's Guard
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Soul Gem
  flex_slots:
  - Ethereal Staff
  - Genji's Guard
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
    Blink Rune, Bancroft''s Talon, Blood-Bound Book, Kinetic Cuirass, Chandra''s Grace,
    Ethereal Staff, Genji''s Guard, Oni Hunter''s Garb, Eye of Providence, Lifebinder,
    Spectral Armor, Wish-Granting Pearl, Bracer of The Abyss, Jade Scepter, Yogi''s
    Necklace, Breastplate of Valor, Phoenix Feather, Shifter''s Shield, Spear of the
    Magus, Mantle Of Discord, Nimble Ring, Freya''s Tears, Erosion.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
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
  - Blink Rune
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Obsidian Shard, Blink Rune, Spear of the Magus,
    The Cosmic Horror, Bracer of The Abyss, Ethereal Staff, Nimble Ring, Genji''s
    Guard, Dreamer''s Idol, Bragi''s Harp, Bancroft''s Talon, Blood-Bound Book, The
    World Stone, Doom Orb, Death Metal, Wish-Granting Pearl, Chronos'' Pendant, Jade
    Scepter, Breastplate of Valor, Screeching Gargoyle, Rod of Asclepius, Oni Hunter''s
    Garb, Yogi''s Necklace, Kinetic Cuirass.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.56
      pick: 0.25
      fit: 0.66
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
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.3
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.33
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.31
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Death Metal:
      total: 0.32
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.33
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.31
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Blink Rune
  - Bracer of The Abyss
  - Bragi's Harp
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of the Magus
  flex_slots:
  - Ethereal Staff
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Blink Rune, Bracer of The Abyss,
    Nimble Ring, Spear of the Magus, Ethereal Staff, Bragi''s Harp, Genji''s Guard,
    Bancroft''s Talon, The Cosmic Horror, Blood-Bound Book, Death Metal, Chronos''
    Pendant, Wish-Granting Pearl, Obsidian Shard, Jade Scepter, Rod of Asclepius,
    Breastplate of Valor, Dreamer''s Idol, Typhon’s Heart, Oni Hunter''s Garb, Helm
    of Radiance, Gem of Focus, Yogi''s Necklace, The World Stone, Kinetic Cuirass.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
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
