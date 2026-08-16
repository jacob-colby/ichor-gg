---
type: smite-build
god: Morgan Le Fay
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cursed Crown
  aspect_pick_rate: 0.43
  aspect_win_rate: 0.53
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.26
    win_rate: 0.54
    alternates:
    - name: Lifebinder
      pick_rate: 0.15
      win_rate: 0.58
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.57
  - name: The Cosmic Horror
    pick_rate: 0.11
    win_rate: 0.51
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.1
      win_rate: 0.61
    - name: Soul Reaver
      pick_rate: 0.1
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.61
    alternates:
    - name: Totem of Death
      pick_rate: 0.12
      win_rate: 0.55
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.7
  - name: Rod of Tahuti
    pick_rate: 0.16
    win_rate: 0.6
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.7
    - name: Ethereal Staff
      pick_rate: 0.08
      win_rate: 0.59
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.65
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.88
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.68
  - name: Void Shard
    pick_rate: 0.07
    win_rate: 0.81
    alternates:
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.55
    - name: Sundering Echo
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.46
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.33
    win_rate: 0.46
  - name: Heroism
    pick_rate: 0.07
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/morgan-le-fay/
  last_verified: '2026-08-16'
  god_win_rate: 0.5570469798657718
  god_matches_won: 249
  god_matches_played: 447
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Nimble Ring, Chronos''
    Pendant, Doom Orb, Freya''s Tears, The World Stone, Dreamer''s Idol, Gem of Focus,
    Death Metal, Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Breastplate
    of Valor, Bancroft''s Talon, Jade Scepter, Ethereal Staff, Bracer of The Abyss,
    Alchemist Coat, Book of Thoth.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.51
      pick: 0.15
      fit: 0.79
    Spear of the Magus:
      total: 0.59
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.79
    Obsidian Shard:
      total: 0.61
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.79
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.7
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Nimble Ring, Death Metal, Spear of the Magus, Freya''s
    Tears, Breastplate of Valor, Chronos'' Pendant, Doom Orb, Bragi''s Harp, The World
    Stone, Bancroft''s Talon, Triton''s Conch, Helm of Radiance, Gem of Focus, Blood-Bound
    Book, Rod of Asclepius, Book of Thoth, Oni Hunter''s Garb, Polynomicon, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.24
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.24
    Death Metal:
      total: 0.55
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.57
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.47
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.7
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
  - Spear of Desolation
  - Spear of the Magus
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
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Freya''s Tears, Nimble
    Ring, Death Metal, Chronos'' Pendant, Breastplate of Valor, Doom Orb, Shield of
    the Phoenix, The World Stone, Gem of Focus, Dreamer''s Idol, Bragi''s Harp, Helm
    of Radiance, Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Amanita Charm,
    Screeching Gargoyle, Triton''s Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.22
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 0.78
    Spear of the Magus:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.56
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.56
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire,
    Freya''s Tears, Kinetic Cuirass, Rod of Asclepius, Chandra''s Grace, Nimble Ring,
    Blood-Bound Book, Oni Hunter''s Garb, Lifebinder, Bancroft''s Talon, Breastplate
    of Valor, Spear of the Magus, Phoenix Feather, Erosion, Spectral Armor, Eye of
    Providence, Shifter''s Shield, Draconic Scale, Helm of Radiance, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.26
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.68
      pick: 0.11
      fit: 0.42
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.39
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.7
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom Orb, The
    World Stone, Nimble Ring, Dreamer''s Idol, Freya''s Tears, Chronos'' Pendant,
    Screeching Gargoyle, Breastplate of Valor, Death Metal, Helm of Radiance, Gem
    of Focus, Blood-Bound Book, Rod of Asclepius, Bancroft''s Talon, Jade Scepter,
    Ethereal Staff, Stone of Binding, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.51
      pick: 0.15
      fit: 0.85
    Spear of the Magus:
      total: 0.6
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.85
    Obsidian Shard:
      total: 0.62
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.85
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 1.0
  starter: *id001
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
  - Bragi's Harp
  - Bracer of The Abyss
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Freya''s Tears, Spear of
    the Magus, Bragi''s Harp, Death Metal, Bracer of The Abyss, Breastplate of Valor,
    Chronos'' Pendant, Blood-Bound Book, Shield of the Phoenix, Bancroft''s Talon,
    Kinetic Cuirass, Amanita Charm, Helm of Radiance, Rod of Asclepius, Eye of Providence,
    Oni Hunter''s Garb, Jade Scepter, Doom Orb, Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.08
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.58
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.51
      efficiency: 0.42
      win: 0.59
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.32
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.7
      pick: 0.12
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
  - Spear of Desolation
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Soul Gem, Freya''s Tears, Breastplate
    of Valor, Gluttonous Grimoire, Chronos'' Pendant, Shield of the Phoenix, Gem of
    Focus, Nimble Ring, Screeching Gargoyle, Chandra''s Grace, Spear of the Magus,
    Death Metal, Gladiator''s Shield, Kinetic Cuirass, Prophetic Cloak, Amanita Charm,
    Doom Orb, The World Stone, Helm of Radiance, Eye of Providence, Oni Hunter''s
    Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.68
      pick: 0.11
      fit: 0.48
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 0.86
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.37
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.7
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
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
      total: 0.59
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.65
    Death Metal:
      total: 0.55
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.59
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.44
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.44
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.7
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, The Crusher,
    Gluttonous Grimoire, Death Metal, Nimble Ring, Spear of the Magus, Hydra''s Lament,
    Freya''s Tears, The Reaper, Chronos'' Pendant, Runeforged Hammer, Bragi''s Harp,
    Pendulum Blade, Doom Orb, Damaru, The World Stone, Triton''s Conch, Heartseeker,
    Breastplate of Valor, Helm of Radiance, Titan''s Bane, Tekko-Kagi, Dreamer''s
    Idol, Blood-Bound Book, Rod of Asclepius, Gem of Focus, Lernaean Bow, Arondight,
    Bancroft''s Talon, Golden Blade, Jade Scepter, Berserker''s Shield, Transcendence,
    Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.69
    Death Metal:
      total: 0.56
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.59
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.56
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.56
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.7
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
    of Valor, Bancroft''s Talon, Jade Scepter, Bracer of The Abyss, Ethereal Staff,
    Alchemist Coat, Freya''s Tears, Book of Thoth.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.62
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.51
      pick: 0.15
      fit: 0.79
    Spear of the Magus:
      total: 0.59
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.79
    Obsidian Shard:
      total: 0.61
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Shield of the Phoenix,
    Rod of Asclepius, Freya''s Tears, Kinetic Cuirass, Chandra''s Grace, Nimble Ring,
    Oni Hunter''s Garb, Spear of the Magus, Lifebinder, Jade Scepter, Ethereal Staff,
    Blood-Bound Book, Bancroft''s Talon, Phoenix Feather, Alchemist Coat, Chronos''
    Pendant, Breastplate of Valor, Spectral Armor, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.25
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.68
      pick: 0.11
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.62
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.47
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.47
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.92
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Genji's Guard
  - Death Metal
  - Freya's Tears
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
    Gem, Gluttonous Grimoire, Amanita Charm, Shield of the Phoenix, Rod of Asclepius,
    Freya''s Tears, Nimble Ring, Death Metal, Bancroft''s Talon, Oni Hunter''s Garb,
    Chandra''s Grace, Kinetic Cuirass, Blood-Bound Book, Spear of the Magus, Breastplate
    of Valor, Lifebinder, Triton''s Conch, Jade Scepter, Chronos'' Pendant, Ethereal
    Staff, Yogi''s Necklace, Wish-Granting Pearl.'
  slot_scores:
    Bancroft's Talon:
      total: 0.53
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.25
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.68
      pick: 0.11
      fit: 0.17
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.44
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.37
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Freya's Tears
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Shield of the Phoenix, Amanita Charm, Freya''s
    Tears, Rod of Asclepius, Chandra''s Grace, Nimble Ring, Spear of the Magus, Kinetic
    Cuirass, Oni Hunter''s Garb, Breastplate of Valor, Death Metal, Blood-Bound Book,
    Chronos'' Pendant, Bancroft''s Talon, Lifebinder, Jade Scepter, Ethereal Staff,
    Triton''s Conch, Spectral Armor, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.24
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.68
      pick: 0.11
      fit: 0.24
    Spear of the Magus:
      total: 0.53
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.42
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.42
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.89
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire,
    Freya''s Tears, Kinetic Cuirass, Rod of Asclepius, Chandra''s Grace, Oni Hunter''s
    Garb, Nimble Ring, Breastplate of Valor, Erosion, Blood-Bound Book, Phoenix Feather,
    Lifebinder, Eye of Providence, Spectral Armor, Shifter''s Shield, Bancroft''s
    Talon, Draconic Scale, Spear of the Magus, Leviathan''s Hide, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.68
      pick: 0.11
      fit: 0.44
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.36
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.83
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.87
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Shield of the Phoenix,
    Spear of the Magus, Rod of Asclepius, Kinetic Cuirass, Nimble Ring, Chandra''s
    Grace, Screeching Gargoyle, Oni Hunter''s Garb, Void Stone, Void Shield, Doom
    Orb, The World Stone, Lifebinder, Blood-Bound Book, Dreamer''s Idol, Jade Scepter,
    Bancroft''s Talon, Breastplate of Valor, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.2
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.68
      pick: 0.11
      fit: 0.2
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.59
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.65
      pick: 0.35
      fit: 0.59
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.7
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
    this god: Soul Gem, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Shield of
    the Phoenix, Freya''s Tears, Rod of Asclepius, Kinetic Cuirass, Blood-Bound Book,
    Chandra''s Grace, Oni Hunter''s Garb, Bancroft''s Talon, Spear of the Magus, Breastplate
    of Valor, Death Metal, Lifebinder, Bracer of The Abyss, Bragi''s Harp, Spectral
    Armor, Jade Scepter, Yogi''s Necklace, Phoenix Feather, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.12
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.31
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.37
    Bragi's Harp:
      total: 0.49
      efficiency: 0.42
      win: 0.59
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.23
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.7
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
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Soul Gem, Shield of the Phoenix, Freya''s
    Tears, Gluttonous Grimoire, Chandra''s Grace, Amanita Charm, Breastplate of Valor,
    Rod of Asclepius, Chronos'' Pendant, Kinetic Cuirass, Nimble Ring, Oni Hunter''s
    Garb, Screeching Gargoyle, Spear of the Magus, Gem of Focus, Gladiator''s Shield,
    Blood-Bound Book, Lifebinder, Bancroft''s Talon, Spectral Armor, Death Metal,
    Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.36
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.68
      pick: 0.11
      fit: 0.43
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 0.64
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.28
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.7
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
  - Freya's Tears
  - The Crusher
  - Soul Gem
  flex_slots:
  - Freya's Tears
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
    Jotunn''s Revenge, Amanita Charm, Shield of the Phoenix, The Reaper, Nimble Ring,
    Freya''s Tears, Runeforged Hammer, Berserker''s Shield, Rod of Asclepius, Golden
    Blade, Hydra''s Lament, Kinetic Cuirass, Riptalon, Death Metal, Chandra''s Grace,
    Eye of the Storm, Oni Hunter''s Garb, Avenging Blade, Spear of the Magus, Lernaean
    Bow, Pharaoh''s Curse, Blood-Bound Book, Damaru, Triton''s Conch, Breastplate
    of Valor, Bancroft''s Talon, Lifebinder, Bragi''s Harp, Tekko-Kagi, Jade Scepter,
    Tyrfing, Shogun''s Ofuda, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.16
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.52
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.68
      pick: 0.11
      fit: 0.16
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.53
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.7
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    Crusher, Jotunn''s Revenge, Amanita Charm, Shield of the Phoenix, Rod of Asclepius,
    Freya''s Tears, The Reaper, Nimble Ring, Runeforged Hammer, Death Metal, Spear
    of the Magus, Kinetic Cuirass, Hydra''s Lament, Chandra''s Grace, Berserker''s
    Shield, Blood-Bound Book, Oni Hunter''s Garb, Lifebinder, Eye of the Storm, Bancroft''s
    Talon, Triton''s Conch, Golden Blade, Jade Scepter, Riptalon, Ethereal Staff,
    Avenging Blade, Chronos'' Pendant, Breastplate of Valor, Alchemist Coat, Damaru,
    Pharaoh''s Curse, Spectral Armor, Phoenix Feather, Bragi''s Harp.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.51
    Transcendence:
      total: 0.48
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.23
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.41
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.7
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
    Asclepius, Shield of the Phoenix, Kinetic Cuirass, Chandra''s Grace, Nimble Ring,
    Oni Hunter''s Garb, Spear of the Magus, Lifebinder, Jade Scepter, Blood-Bound
    Book, Ethereal Staff, Bancroft''s Talon, Phoenix Feather, Alchemist Coat, Chronos''
    Pendant, Breastplate of Valor, Spectral Armor, Freya''s Tears, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.62
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.54
      pick: 0.26
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.6
      pick: 0.27
      fit: 0.47
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.92
  starter: *id001
  aspect: Aspect of the Cursed Crown
---
