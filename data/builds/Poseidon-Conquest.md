---
type: smite-build
god: Poseidon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Trident
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.61
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.59
    win_rate: 0.56
    alternates:
    - name: Book of Thoth
      pick_rate: 0.13
      win_rate: 0.6
    - name: Chronos' Pendant
      pick_rate: 0.07
      win_rate: 0.55
  - name: The World Stone
    pick_rate: 0.27
    win_rate: 0.58
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.49
  - name: Nimble Ring
    pick_rate: 0.23
    win_rate: 0.51
    alternates:
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.48
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.54
  - name: Rod of Tahuti
    pick_rate: 0.29
    win_rate: 0.48
    alternates:
    - name: Nimble Ring
      pick_rate: 0.18
      win_rate: 0.59
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.61
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.61
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.67
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.42
  - name: Evil Eye
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.85
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.6
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.3
    win_rate: 0.6
  - name: Sands Of Time
    pick_rate: 0.22
    win_rate: 0.44
  - name: Archmage's Gem
    pick_rate: 0.19
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/poseidon/
  last_verified: '2026-08-17'
  god_win_rate: 0.56
  god_matches_won: 224
  god_matches_played: 400
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-17'
  god_matches_analyzed: 7467
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Nimble Ring
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
    this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear of the Magus,
    Chronos'' Pendant, Doom Orb, Genji''s Guard, Dreamer''s Idol, Gem of Focus, Totem
    of Death, Death Metal, Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Breastplate
    of Valor, Bancroft''s Talon, Jade Scepter, Bracer of The Abyss, Ethereal Staff,
    Alchemist Coat, Freya''s Tears.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.51
      pick: 0.36
      fit: 0.42
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.56
      pick: 0.59
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.79
    The World Stone:
      total: 0.56
      efficiency: 0.46
      win: 0.58
      pick: 0.37
      fit: 0.79
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.48
      pick: 0.48
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.61
      pick: 0.39
      fit: 0.79
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Soul Gem, Death Metal, Genji''s Guard, The Cosmic Horror, Spear of the
    Magus, Chronos'' Pendant, Breastplate of Valor, Doom Orb, Bragi''s Harp, Bancroft''s
    Talon, Triton''s Conch, Helm of Radiance, Gem of Focus, Blood-Bound Book, Rod
    of Asclepius, Totem of Death, Oni Hunter''s Garb, Polynomicon, Jade Scepter, Freya''s
    Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.36
      fit: 0.29
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.56
      pick: 0.59
      fit: 0.61
    The World Stone:
      total: 0.53
      efficiency: 0.46
      win: 0.58
      pick: 0.37
      fit: 0.57
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.48
      pick: 0.48
      fit: 0.57
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.39
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Genji''s
    Guard, Chronos'' Pendant, Death Metal, Breastplate of Valor, Doom Orb, Freya''s
    Tears, Gem of Focus, Dreamer''s Idol, Totem of Death, Shield of the Phoenix, Bragi''s
    Harp, Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Amanita
    Charm, Screeching Gargoyle, Triton''s Conch.'
  slot_scores:
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.51
      pick: 0.36
      fit: 0.22
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.56
      pick: 0.59
      fit: 0.78
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.52
      efficiency: 0.46
      win: 0.58
      pick: 0.37
      fit: 0.56
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.48
      pick: 0.48
      fit: 0.56
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.61
      pick: 0.39
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Genji''s Guard, Chandra''s Grace, Blood-Bound
    Book, Freya''s Tears, Oni Hunter''s Garb, Lifebinder, The Cosmic Horror, Bancroft''s
    Talon, Breastplate of Valor, Spear of the Magus, Phoenix Feather, Erosion, Shifter''s
    Shield, Spectral Armor, Eye of Providence, Draconic Scale, Helm of Radiance, Jade
    Scepter.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.59
      fit: 0.49
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.48
      pick: 0.48
      fit: 0.39
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.61
      pick: 0.39
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear of the Magus,
    Doom Orb, Dreamer''s Idol, Chronos'' Pendant, Genji''s Guard, Screeching Gargoyle,
    Breastplate of Valor, Death Metal, Helm of Radiance, Gem of Focus, Blood-Bound
    Book, Rod of Asclepius, Totem of Death, Bancroft''s Talon, Jade Scepter, Freya''s
    Tears, Stone of Binding, Bracer of The Abyss, Ethereal Staff.'
  slot_scores:
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.36
      fit: 0.3
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.56
      pick: 0.59
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.85
    The World Stone:
      total: 0.57
      efficiency: 0.46
      win: 0.58
      pick: 0.37
      fit: 0.85
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.48
      pick: 0.48
      fit: 0.85
    Obsidian Shard:
      total: 0.6
      efficiency: 0.52
      win: 0.61
      pick: 0.39
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
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
    this god: Gluttonous Grimoire, Soul Gem, Genji''s Guard, The Cosmic Horror, Spear
    of the Magus, Chronos'' Pendant, Bragi''s Harp, Death Metal, Bracer of The Abyss,
    Breastplate of Valor, Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass, Amanita
    Charm, Helm of Radiance, Freya''s Tears, Rod of Asclepius, Eye of Providence,
    Oni Hunter''s Garb, Shield of the Phoenix, Jade Scepter, Doom Orb, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.51
      pick: 0.36
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.42
      win: 0.53
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.59
      fit: 0.4
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.48
      pick: 0.48
      fit: 0.32
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
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Chronos''
    Pendant, Breastplate of Valor, Gluttonous Grimoire, Freya''s Tears, Shield of
    the Phoenix, Gem of Focus, Totem of Death, The Cosmic Horror, Screeching Gargoyle,
    Chandra''s Grace, Spear of the Magus, Death Metal, Gladiator''s Shield, Kinetic
    Cuirass, Prophetic Cloak, Amanita Charm, Doom Orb, Helm of Radiance, Eye of Providence,
    Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.07
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.56
      pick: 0.59
      fit: 0.86
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.48
      pick: 0.48
      fit: 0.37
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Nimble Ring
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
    win/pick). Underrated for this god: Jotunn''s Revenge, The Crusher, Gluttonous
    Grimoire, Soul Gem, Death Metal, Hydra''s Lament, The Cosmic Horror, Spear of
    the Magus, Bragi''s Harp, The Reaper, Genji''s Guard, Lernaean Bow, Runeforged
    Hammer, Chronos'' Pendant, Tekko-Kagi, Golden Blade, Berserker''s Shield, Damaru,
    Tyrfing, Pendulum Blade, Breastplate of Valor, Heartseeker, Riptalon, Titan''s
    Bane, Triton''s Conch, Silverbranch Bow, Dominance, Bracer of The Abyss, Arondight,
    Transcendence, Avenging Blade, Helm of Radiance, Doom Orb, Shield Splitter, Blood-Bound
    Book, Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.65
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.51
      pick: 0.36
      fit: 0.35
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.56
      pick: 0.59
      fit: 0.55
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.48
      pick: 0.48
      fit: 0.44
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.39
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, The Crusher, Gluttonous
    Grimoire, Soul Gem, Death Metal, The Cosmic Horror, Spear of the Magus, Hydra''s
    Lament, Chronos'' Pendant, The Reaper, Genji''s Guard, Runeforged Hammer, Bragi''s
    Harp, Pendulum Blade, Doom Orb, Damaru, Triton''s Conch, Heartseeker, Breastplate
    of Valor, Helm of Radiance, Titan''s Bane, Tekko-Kagi, Dreamer''s Idol, Blood-Bound
    Book, Rod of Asclepius, Gem of Focus, Lernaean Bow, Totem of Death, Arondight,
    Bancroft''s Talon, Golden Blade, Jade Scepter, Berserker''s Shield, Transcendence,
    Avenging Blade, Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.69
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.36
      fit: 0.31
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.56
      pick: 0.59
      fit: 0.69
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.48
      pick: 0.48
      fit: 0.56
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.61
      pick: 0.39
      fit: 0.56
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
    Underrated for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear
    of the Magus, Chronos'' Pendant, Doom Orb, Genji''s Guard, Dreamer''s Idol, Gem
    of Focus, Totem of Death, Death Metal, Helm of Radiance, Blood-Bound Book, Rod
    of Asclepius, Breastplate of Valor, Bancroft''s Talon, Jade Scepter, Bracer of
    The Abyss, Ethereal Staff, Alchemist Coat, Freya''s Tears.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.56
      pick: 0.59
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.48
      pick: 0.48
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.61
      pick: 0.39
      fit: 0.79
  starter: *id001
---
