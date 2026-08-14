---
type: smite-build
god: Morgan Le Fay
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cursed Crown
  aspect_pick_rate: 0.43
  aspect_win_rate: 0.46
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.25
    win_rate: 0.52
    alternates:
    - name: Lifebinder
      pick_rate: 0.18
      win_rate: 0.47
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.48
  - name: The Cosmic Horror
    pick_rate: 0.11
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.61
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.65
  - name: Totem of Death
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.5
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.71
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.11
      win_rate: 0.67
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.95
  - name: Obsidian Shard
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.55
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.45
  - name: Void Shard
    pick_rate: 0.09
    win_rate: 0.73
    alternates:
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.33
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 0.2
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.45
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.33
    win_rate: 0.43
  - name: Pendulum of the Ages
    pick_rate: 0.08
    win_rate: 0.7
  source_url: https://smitebrain.com/gods/morgan-le-fay/
  last_verified: '2026-08-14'
  god_win_rate: 0.5306122448979592
  god_matches_won: 130
  god_matches_played: 245
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
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
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Nimble Ring, Chronos''
    Pendant, Doom Orb, The World Stone, Dreamer''s Idol, Gem of Focus, Death Metal,
    Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Breastplate of Valor, Freya''s
    Tears, Bancroft''s Talon, Jade Scepter, Bracer of The Abyss, Alchemist Coat, Book
    of Thoth.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.52
      pick: 0.15
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.79
    Soul Gem:
      total: 0.68
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Ethereal Staff
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Nimble Ring, Death Metal, Spear of the Magus, Breastplate
    of Valor, Chronos'' Pendant, Doom Orb, Bragi''s Harp, The World Stone, Bancroft''s
    Talon, Freya''s Tears, Triton''s Conch, Helm of Radiance, Gem of Focus, Blood-Bound
    Book, Rod of Asclepius, Book of Thoth, Oni Hunter''s Garb, Polynomicon, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.5
      pick: 0.16
      fit: 0.24
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.24
    Ethereal Staff:
      total: 0.53
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.29
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.57
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.47
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
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
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Nimble Ring, Death Metal,
    Chronos'' Pendant, Breastplate of Valor, Freya''s Tears, Doom Orb, The World Stone,
    Gem of Focus, Dreamer''s Idol, Shield of the Phoenix, Bragi''s Harp, Helm of Radiance,
    Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Amanita Charm, Screeching
    Gargoyle, Triton''s Conch.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.78
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.52
      pick: 0.15
      fit: 0.56
    Spear of the Magus:
      total: 0.52
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.56
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Freya''s Tears, Chandra''s Grace, Nimble Ring,
    Blood-Bound Book, Oni Hunter''s Garb, Bancroft''s Talon, Breastplate of Valor,
    Spear of the Magus, Phoenix Feather, Erosion, Spectral Armor, Eye of Providence,
    Draconic Scale, Helm of Radiance, Jade Scepter, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.61
    Ethereal Staff:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.4
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.39
    Obsidian Shard:
      total: 0.52
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.89
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
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom Orb, The
    World Stone, Nimble Ring, Dreamer''s Idol, Chronos'' Pendant, Screeching Gargoyle,
    Breastplate of Valor, Death Metal, Freya''s Tears, Helm of Radiance, Gem of Focus,
    Blood-Bound Book, Rod of Asclepius, Bancroft''s Talon, Jade Scepter, Stone of
    Binding, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.52
      pick: 0.15
      fit: 0.85
    Spear of the Magus:
      total: 0.57
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.85
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.85
    Soul Gem:
      total: 0.68
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
  - Rod of Tahuti
  - Soul Gem
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Death Metal, Bracer of The Abyss, Breastplate of Valor, Freya''s Tears,
    Chronos'' Pendant, Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass, Amanita
    Charm, Helm of Radiance, Rod of Asclepius, Eye of Providence, Oni Hunter''s Garb,
    Shield of the Phoenix, Jade Scepter, Doom Orb, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.42
      win: 0.54
      pick: 0.0
      fit: 0.63
    Ethereal Staff:
      total: 0.51
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.17
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.32
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Breastplate of Valor, Gluttonous
    Grimoire, Freya''s Tears, Chronos'' Pendant, Shield of the Phoenix, Gem of Focus,
    Nimble Ring, Screeching Gargoyle, Chandra''s Grace, Spear of the Magus, Death
    Metal, Gladiator''s Shield, Kinetic Cuirass, Prophetic Cloak, Amanita Charm, Doom
    Orb, The World Stone, Helm of Radiance, Eye of Providence, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.16
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.48
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.86
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.37
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Ethereal Staff
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, The Crusher,
    Gluttonous Grimoire, Nimble Ring, Death Metal, Hydra''s Lament, Spear of the Magus,
    Bragi''s Harp, The Reaper, Lernaean Bow, Runeforged Hammer, Tekko-Kagi, Golden
    Blade, Berserker''s Shield, Damaru, Tyrfing, Chronos'' Pendant, Pendulum Blade,
    Breastplate of Valor, Heartseeker, Riptalon, Titan''s Bane, Triton''s Conch, Silverbranch
    Bow, Dominance, Bracer of The Abyss, Arondight, Transcendence, Avenging Blade,
    Helm of Radiance, Doom Orb, Shield Splitter, The World Stone, Blood-Bound Book,
    Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.65
    Ethereal Staff:
      total: 0.52
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.23
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.44
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.44
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Ethereal Staff
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, The Crusher,
    Gluttonous Grimoire, Death Metal, Nimble Ring, Spear of the Magus, Hydra''s Lament,
    The Reaper, Chronos'' Pendant, Runeforged Hammer, Bragi''s Harp, Pendulum Blade,
    Doom Orb, Damaru, The World Stone, Triton''s Conch, Heartseeker, Breastplate of
    Valor, Helm of Radiance, Titan''s Bane, Tekko-Kagi, Freya''s Tears, Dreamer''s
    Idol, Blood-Bound Book, Rod of Asclepius, Gem of Focus, Lernaean Bow, Arondight,
    Bancroft''s Talon, Golden Blade, Jade Scepter, Berserker''s Shield, Transcendence,
    Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.69
    Ethereal Staff:
      total: 0.53
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.31
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.56
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, Nimble
    Ring, Chronos'' Pendant, Doom Orb, The World Stone, Dreamer''s Idol, Gem of Focus,
    Death Metal, Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Breastplate
    of Valor, Bancroft''s Talon, Jade Scepter, Bracer of The Abyss, Alchemist Coat,
    Freya''s Tears, Book of Thoth.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.52
      pick: 0.15
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Shield
    of the Phoenix, Kinetic Cuirass, Chandra''s Grace, Nimble Ring, Oni Hunter''s
    Garb, Spear of the Magus, Jade Scepter, Freya''s Tears, Blood-Bound Book, Bancroft''s
    Talon, Phoenix Feather, Alchemist Coat, Chronos'' Pendant, Breastplate of Valor,
    Spectral Armor, Yogi''s Necklace.'
  slot_scores:
    Ethereal Staff:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.47
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.47
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.92
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Genji's Guard
  - Ethereal Staff
  - Death Metal
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Death Metal
  - Bancroft's Talon
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Nimble Ring, Shield
    of the Phoenix, Death Metal, Bancroft''s Talon, Oni Hunter''s Garb, Chandra''s
    Grace, Kinetic Cuirass, Blood-Bound Book, Spear of the Magus, Breastplate of Valor,
    Freya''s Tears, Triton''s Conch, Jade Scepter, Chronos'' Pendant, Yogi''s Necklace,
    Wish-Granting Pearl.'
  slot_scores:
    Bancroft's Talon:
      total: 0.5
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.5
      pick: 0.16
      fit: 0.25
    Ethereal Staff:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.38
    Death Metal:
      total: 0.5
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.44
    Obsidian Shard:
      total: 0.52
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.37
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Ethereal Staff
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Shield of the Phoenix, Rod
    of Asclepius, Chandra''s Grace, Nimble Ring, Spear of the Magus, Kinetic Cuirass,
    Freya''s Tears, Oni Hunter''s Garb, Breastplate of Valor, Death Metal, Blood-Bound
    Book, Chronos'' Pendant, Bancroft''s Talon, Jade Scepter, Triton''s Conch, Spectral
    Armor, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.5
      pick: 0.16
      fit: 0.24
    Ethereal Staff:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.34
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.59
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.42
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.42
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.89
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Freya''s Tears, Chandra''s Grace, Oni Hunter''s
    Garb, Nimble Ring, Breastplate of Valor, Erosion, Blood-Bound Book, Phoenix Feather,
    Eye of Providence, Spectral Armor, Bancroft''s Talon, Draconic Scale, Spear of
    the Magus, Leviathan''s Hide, Midgardian Mail, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.63
    Ethereal Staff:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.37
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.44
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.36
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.83
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.87
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ethereal Staff
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - The Cosmic Horror
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
    for this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Spear of the Magus,
    Rod of Asclepius, Shield of the Phoenix, Kinetic Cuirass, Nimble Ring, Chandra''s
    Grace, Screeching Gargoyle, Oni Hunter''s Garb, Void Stone, Void Shield, Doom
    Orb, The World Stone, Blood-Bound Book, Dreamer''s Idol, Jade Scepter, Bancroft''s
    Talon, Breastplate of Valor, Stone of Binding.'
  slot_scores:
    Ethereal Staff:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.38
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.7
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.52
      pick: 0.15
      fit: 0.59
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.59
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.59
    Soul Gem:
      total: 0.68
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 1.0
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Shield of
    the Phoenix, Rod of Asclepius, Kinetic Cuirass, Blood-Bound Book, Chandra''s Grace,
    Oni Hunter''s Garb, Bancroft''s Talon, Freya''s Tears, Spear of the Magus, Breastplate
    of Valor, Death Metal, Bracer of The Abyss, Bragi''s Harp, Spectral Armor, Jade
    Scepter, Yogi''s Necklace, Phoenix Feather, Chronos'' Pendant.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.31
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.37
    Bragi's Harp:
      total: 0.46
      efficiency: 0.42
      win: 0.54
      pick: 0.0
      fit: 0.51
    Ethereal Staff:
      total: 0.53
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.24
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.23
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.67
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Ethereal Staff
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
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
    + fit + win/pick). Underrated for this god: Soul Gem, Shield of the Phoenix, Gluttonous
    Grimoire, Chandra''s Grace, Amanita Charm, Freya''s Tears, Breastplate of Valor,
    Rod of Asclepius, Chronos'' Pendant, Kinetic Cuirass, Nimble Ring, Oni Hunter''s
    Garb, Screeching Gargoyle, Spear of the Magus, Gem of Focus, Gladiator''s Shield,
    Blood-Bound Book, Bancroft''s Talon, Spectral Armor, Death Metal, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.16
      fit: 0.43
    Ethereal Staff:
      total: 0.53
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.29
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.43
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.64
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.28
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.94
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Ethereal Staff
  - Runeforged Hammer
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Ethereal Staff
  - Runeforged Hammer
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, The Crusher,
    Jotunn''s Revenge, Amanita Charm, The Reaper, Nimble Ring, Runeforged Hammer,
    Berserker''s Shield, Rod of Asclepius, Shield of the Phoenix, Golden Blade, Hydra''s
    Lament, Kinetic Cuirass, Riptalon, Death Metal, Chandra''s Grace, Eye of the Storm,
    Oni Hunter''s Garb, Avenging Blade, Spear of the Magus, Lernaean Bow, Pharaoh''s
    Curse, Freya''s Tears, Blood-Bound Book, Damaru, Triton''s Conch, Breastplate
    of Valor, Bancroft''s Talon, Bragi''s Harp, Tekko-Kagi, Jade Scepter, Tyrfing,
    Shogun''s Ofuda, Spectral Armor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.52
    Ethereal Staff:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.31
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.31
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.7
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Ethereal Staff
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Obsidian Shard
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, The
    Crusher, Jotunn''s Revenge, Amanita Charm, Rod of Asclepius, The Reaper, Nimble
    Ring, Shield of the Phoenix, Runeforged Hammer, Death Metal, Spear of the Magus,
    Kinetic Cuirass, Hydra''s Lament, Chandra''s Grace, Berserker''s Shield, Blood-Bound
    Book, Oni Hunter''s Garb, Eye of the Storm, Bancroft''s Talon, Triton''s Conch,
    Golden Blade, Jade Scepter, Riptalon, Freya''s Tears, Avenging Blade, Chronos''
    Pendant, Breastplate of Valor, Alchemist Coat, Damaru, Pharaoh''s Curse, Spectral
    Armor, Phoenix Feather, Bragi''s Harp.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.51
    Ethereal Staff:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.18
      fit: 0.41
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.41
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.37
      fit: 0.41
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.81
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Rod of
    Asclepius, Shield of the Phoenix, Kinetic Cuirass, Chandra''s Grace, Nimble Ring,
    Oni Hunter''s Garb, Spear of the Magus, Jade Scepter, Blood-Bound Book, Bancroft''s
    Talon, Phoenix Feather, Alchemist Coat, Chronos'' Pendant, Breastplate of Valor,
    Spectral Armor, Freya''s Tears, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.5
      pick: 0.16
      fit: 0.25
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.59
      pick: 0.28
      fit: 0.47
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.71
      pick: 0.14
      fit: 0.92
  starter: *id001
  aspect: Aspect of the Cursed Crown
---
