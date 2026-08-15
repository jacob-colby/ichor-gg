---
type: smite-build
god: Morgan Le Fay
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cursed Crown
  aspect_pick_rate: 0.42
  aspect_win_rate: 0.52
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.27
    win_rate: 0.53
    alternates:
    - name: Lifebinder
      pick_rate: 0.17
      win_rate: 0.55
    - name: Chronos' Pendant
      pick_rate: 0.12
      win_rate: 0.57
  - name: The Cosmic Horror
    pick_rate: 0.12
    win_rate: 0.49
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.11
      win_rate: 0.62
    - name: Soul Reaver
      pick_rate: 0.1
      win_rate: 0.62
  - name: Totem of Death
    pick_rate: 0.13
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.58
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.72
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.63
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.61
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.81
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.94
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.47
  - name: Void Shard
    pick_rate: 0.09
    win_rate: 0.8
    alternates:
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 0.43
    - name: Evil Eye
      pick_rate: 0.04
      win_rate: 0.29
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.46
    win_rate: 0.62
  - name: Bluestone Pendant
    pick_rate: 0.33
    win_rate: 0.43
  - name: Pendulum of the Ages
    pick_rate: 0.07
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/morgan-le-fay/
  last_verified: '2026-08-15'
  god_win_rate: 0.5439093484419264
  god_matches_won: 192
  god_matches_played: 353
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Nimble Ring, Chronos''
    Pendant, Doom Orb, The World Stone, Dreamer''s Idol, Gem of Focus, Death Metal,
    Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Breastplate of Valor, Bancroft''s
    Talon, Jade Scepter, Bracer of The Abyss, Alchemist Coat, Freya''s Tears, Book
    of Thoth.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.49
      pick: 0.16
      fit: 0.79
    Spear of the Magus:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.79
    Obsidian Shard:
      total: 0.6
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.79
    Soul Gem:
      total: 0.68
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Death Metal
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Death Metal
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Nimble Ring, Death Metal, Spear of the Magus, Breastplate
    of Valor, Chronos'' Pendant, Doom Orb, Bragi''s Harp, The World Stone, Bancroft''s
    Talon, Triton''s Conch, Helm of Radiance, Gem of Focus, Blood-Bound Book, Rod
    of Asclepius, Book of Thoth, Oni Hunter''s Garb, Polynomicon, Jade Scepter, Freya''s
    Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.24
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.24
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.57
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.47
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Nimble Ring, Death Metal,
    Chronos'' Pendant, Breastplate of Valor, Doom Orb, The World Stone, Freya''s Tears,
    Gem of Focus, Dreamer''s Idol, Bragi''s Harp, Helm of Radiance, Blood-Bound Book,
    Rod of Asclepius, Kinetic Cuirass, Amanita Charm, Screeching Gargoyle, Triton''s
    Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.22
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 0.78
    Spear of the Magus:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.56
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.56
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
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
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Rod of
    Asclepius, Chandra''s Grace, Nimble Ring, Blood-Bound Book, Freya''s Tears, Oni
    Hunter''s Garb, Bancroft''s Talon, Breastplate of Valor, Spear of the Magus, Phoenix
    Feather, Erosion, Shifter''s Shield, Spectral Armor, Eye of Providence, Draconic
    Scale, Helm of Radiance, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.26
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.39
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.39
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.72
      pick: 0.12
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
  - Spear of Desolation
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom Orb, The
    World Stone, Nimble Ring, Dreamer''s Idol, Chronos'' Pendant, Screeching Gargoyle,
    Breastplate of Valor, Death Metal, Helm of Radiance, Gem of Focus, Blood-Bound
    Book, Rod of Asclepius, Bancroft''s Talon, Jade Scepter, Freya''s Tears, Stone
    of Binding, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.49
      pick: 0.16
      fit: 0.85
    Spear of the Magus:
      total: 0.59
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.85
    Obsidian Shard:
      total: 0.61
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.85
    Soul Gem:
      total: 0.68
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Death Metal, Bracer of The Abyss, Breastplate of Valor, Chronos'' Pendant,
    Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass, Amanita Charm, Helm of Radiance,
    Freya''s Tears, Rod of Asclepius, Eye of Providence, Oni Hunter''s Garb, Jade
    Scepter, Doom Orb, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.5
      efficiency: 0.42
      win: 0.58
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.32
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.32
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
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
    + fit + win/pick). Underrated for this god: Soul Gem, Breastplate of Valor, Gluttonous
    Grimoire, Chronos'' Pendant, Freya''s Tears, Gem of Focus, Nimble Ring, Screeching
    Gargoyle, Chandra''s Grace, Spear of the Magus, Death Metal, Gladiator''s Shield,
    Kinetic Cuirass, Prophetic Cloak, Amanita Charm, Doom Orb, The World Stone, Helm
    of Radiance, Eye of Providence, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.12
      fit: 0.63
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 0.86
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.37
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, The Crusher,
    Gluttonous Grimoire, Nimble Ring, Death Metal, Hydra''s Lament, Spear of the Magus,
    Bragi''s Harp, The Reaper, Lernaean Bow, Runeforged Hammer, Tekko-Kagi, Golden
    Blade, Berserker''s Shield, Damaru, Chronos'' Pendant, Tyrfing, Pendulum Blade,
    Breastplate of Valor, Heartseeker, Riptalon, Titan''s Bane, Triton''s Conch, Silverbranch
    Bow, Dominance, Bracer of The Abyss, Arondight, Transcendence, Avenging Blade,
    Helm of Radiance, Doom Orb, Shield Splitter, The World Stone, Blood-Bound Book,
    Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.65
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.44
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.44
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, The Crusher,
    Gluttonous Grimoire, Death Metal, Nimble Ring, Spear of the Magus, Hydra''s Lament,
    The Reaper, Chronos'' Pendant, Runeforged Hammer, Bragi''s Harp, Pendulum Blade,
    Doom Orb, Damaru, The World Stone, Triton''s Conch, Heartseeker, Breastplate of
    Valor, Helm of Radiance, Titan''s Bane, Tekko-Kagi, Dreamer''s Idol, Blood-Bound
    Book, Rod of Asclepius, Gem of Focus, Lernaean Bow, Arondight, Bancroft''s Talon,
    Golden Blade, Jade Scepter, Berserker''s Shield, Transcendence, Avenging Blade,
    Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.69
    Death Metal:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.56
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.56
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.72
      pick: 0.12
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
      total: 0.62
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.49
      pick: 0.16
      fit: 0.79
    Spear of the Magus:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.79
    Obsidian Shard:
      total: 0.6
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
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
    this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Kinetic
    Cuirass, Chandra''s Grace, Nimble Ring, Oni Hunter''s Garb, Spear of the Magus,
    Jade Scepter, Blood-Bound Book, Bancroft''s Talon, Phoenix Feather, Alchemist
    Coat, Chronos'' Pendant, Breastplate of Valor, Spectral Armor, Freya''s Tears,
    Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.25
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.47
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.47
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.92
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Genji's Guard
  - Oni Hunter's Garb
  - Death Metal
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Bancroft's Talon
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Nimble Ring, Death
    Metal, Bancroft''s Talon, Oni Hunter''s Garb, Chandra''s Grace, Kinetic Cuirass,
    Blood-Bound Book, Spear of the Magus, Breastplate of Valor, Triton''s Conch, Chronos''
    Pendant, Jade Scepter, Yogi''s Necklace, Wish-Granting Pearl, Freya''s Tears.'
  slot_scores:
    Bancroft's Talon:
      total: 0.52
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.25
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.3
    Death Metal:
      total: 0.52
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.44
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.37
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Chandra''s
    Grace, Nimble Ring, Spear of the Magus, Kinetic Cuirass, Oni Hunter''s Garb, Breastplate
    of Valor, Death Metal, Blood-Bound Book, Chronos'' Pendant, Bancroft''s Talon,
    Freya''s Tears, Jade Scepter, Triton''s Conch, Spectral Armor, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.24
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 0.59
    Spear of the Magus:
      total: 0.52
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.42
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.42
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.89
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
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
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Rod of
    Asclepius, Chandra''s Grace, Freya''s Tears, Oni Hunter''s Garb, Nimble Ring,
    Breastplate of Valor, Erosion, Blood-Bound Book, Phoenix Feather, Shifter''s Shield,
    Eye of Providence, Spectral Armor, Bancroft''s Talon, Draconic Scale, Spear of
    the Magus, Leviathan''s Hide, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.27
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.36
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.36
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.83
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.87
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Spear of the Magus,
    Rod of Asclepius, Kinetic Cuirass, Nimble Ring, Chandra''s Grace, Screeching Gargoyle,
    Oni Hunter''s Garb, Void Stone, Void Shield, Doom Orb, The World Stone, Blood-Bound
    Book, Dreamer''s Idol, Jade Scepter, Bancroft''s Talon, Breastplate of Valor,
    Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.2
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 0.7
    Spear of the Magus:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.59
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.59
    Soul Gem:
      total: 0.68
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 1.0
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
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
    this god: Soul Gem, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Rod of Asclepius,
    Kinetic Cuirass, Blood-Bound Book, Chandra''s Grace, Oni Hunter''s Garb, Bancroft''s
    Talon, Spear of the Magus, Breastplate of Valor, Death Metal, Bracer of The Abyss,
    Freya''s Tears, Bragi''s Harp, Spectral Armor, Jade Scepter, Chronos'' Pendant,
    Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.12
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.31
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.37
    Bragi's Harp:
      total: 0.48
      efficiency: 0.42
      win: 0.58
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.23
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.72
      pick: 0.12
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
  - Rod of Tahuti
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
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, Chandra''s
    Grace, Amanita Charm, Breastplate of Valor, Freya''s Tears, Rod of Asclepius,
    Chronos'' Pendant, Kinetic Cuirass, Nimble Ring, Oni Hunter''s Garb, Screeching
    Gargoyle, Spear of the Magus, Gem of Focus, Gladiator''s Shield, Blood-Bound Book,
    Bancroft''s Talon, Spectral Armor, Death Metal, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.36
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 0.64
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.28
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.94
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Runeforged Hammer
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
    win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, The Crusher,
    Jotunn''s Revenge, Amanita Charm, The Reaper, Nimble Ring, Runeforged Hammer,
    Berserker''s Shield, Rod of Asclepius, Golden Blade, Hydra''s Lament, Kinetic
    Cuirass, Riptalon, Death Metal, Chandra''s Grace, Eye of the Storm, Oni Hunter''s
    Garb, Avenging Blade, Spear of the Magus, Lernaean Bow, Pharaoh''s Curse, Blood-Bound
    Book, Damaru, Triton''s Conch, Breastplate of Valor, Bancroft''s Talon, Bragi''s
    Harp, Tekko-Kagi, Jade Scepter, Tyrfing, Freya''s Tears, Shogun''s Ofuda, Spectral
    Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.16
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.52
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.31
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.7
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, The
    Crusher, Jotunn''s Revenge, Amanita Charm, Rod of Asclepius, The Reaper, Nimble
    Ring, Runeforged Hammer, Death Metal, Spear of the Magus, Kinetic Cuirass, Hydra''s
    Lament, Chandra''s Grace, Berserker''s Shield, Blood-Bound Book, Oni Hunter''s
    Garb, Eye of the Storm, Bancroft''s Talon, Triton''s Conch, Golden Blade, Jade
    Scepter, Riptalon, Avenging Blade, Chronos'' Pendant, Breastplate of Valor, Alchemist
    Coat, Damaru, Freya''s Tears, Pharaoh''s Curse, Spectral Armor, Phoenix Feather,
    Bragi''s Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.17
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.41
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.41
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.72
      pick: 0.12
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
    Asclepius, Kinetic Cuirass, Chandra''s Grace, Nimble Ring, Oni Hunter''s Garb,
    Spear of the Magus, Jade Scepter, Blood-Bound Book, Bancroft''s Talon, Phoenix
    Feather, Alchemist Coat, Chronos'' Pendant, Breastplate of Valor, Spectral Armor,
    Freya''s Tears, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.19
      fit: 0.25
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 0.62
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.63
      pick: 0.28
      fit: 0.47
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.72
      pick: 0.12
      fit: 0.92
  starter: *id001
  aspect: Aspect of the Cursed Crown
---
