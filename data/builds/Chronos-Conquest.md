---
type: smite-build
god: Chronos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Relativity
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.53
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.35
    win_rate: 0.47
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.23
      win_rate: 0.41
    - name: Tyrfing
      pick_rate: 0.07
      win_rate: 0.54
  - name: Spear of Desolation
    pick_rate: 0.24
    win_rate: 0.48
    alternates:
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.48
    - name: Nimble Ring
      pick_rate: 0.05
      win_rate: 0.4
  - name: Nimble Ring
    pick_rate: 0.27
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.54
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.31
  - name: Rod of Tahuti
    pick_rate: 0.24
    win_rate: 0.38
    alternates:
    - name: Nimble Ring
      pick_rate: 0.13
      win_rate: 0.5
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.42
  - name: Obsidian Shard
    pick_rate: 0.14
    win_rate: 0.43
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.54
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.43
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.64
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.82
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.3
    win_rate: 0.54
  - name: Sands Of Time
    pick_rate: 0.23
    win_rate: 0.26
  - name: Bluestone Brooch
    pick_rate: 0.08
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/chronos/
  last_verified: '2026-08-19'
  god_win_rate: 0.47435897435897434
  god_matches_won: 185
  god_matches_played: 390
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Spear of the Magus
  - Book of Thoth
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
    this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear of the Magus,
    Bracer of The Abyss, Genji''s Guard, Blood-Bound Book, Chronos'' Pendant, Bragi''s
    Harp, Breastplate of Valor, Bancroft''s Talon, Death Metal, Helm of Radiance,
    Doom Orb, Rod of Asclepius, The World Stone, Gem of Focus, Freya''s Tears, Kinetic
    Cuirass, Jade Scepter, Totem of Death, Amanita Charm, Dreamer''s Idol, Typhon’s
    Heart, Shield of the Phoenix.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.49
      win: 0.47
      pick: 0.35
      fit: 0.24
    Nimble Ring:
      total: 0.6
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.68
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.56
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.44
    Spear of the Magus:
      total: 0.47
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.44
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Soul Gem, Genji''s Guard, Death Metal, The Cosmic Horror, Bragi''s Harp,
    Spear of the Magus, Breastplate of Valor, Bancroft''s Talon, Bracer of The Abyss,
    Chronos'' Pendant, Blood-Bound Book, Oni Hunter''s Garb, Helm of Radiance, Doom
    Orb, The World Stone, Rod of Asclepius, Kinetic Cuirass, Freya''s Tears, Amanita
    Charm, Gem of Focus, Jade Scepter, Eye of Providence, Triton''s Conch.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.49
      win: 0.47
      pick: 0.35
      fit: 0.28
    Genji's Guard:
      total: 0.47
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.18
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.18
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.48
    Spear of Desolation:
      total: 0.48
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.45
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  flex_slots:
  - The Cosmic Horror
  - Book of Thoth
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
    god: Soul Gem, Gluttonous Grimoire, Genji''s Guard, The Cosmic Horror, Spear of
    the Magus, Breastplate of Valor, Death Metal, Bragi''s Harp, Chronos'' Pendant,
    Bracer of The Abyss, Freya''s Tears, Blood-Bound Book, Kinetic Cuirass, Shield
    of the Phoenix, Doom Orb, Bancroft''s Talon, Amanita Charm, The World Stone, Gem
    of Focus, Helm of Radiance, Eye of Providence, Rod of Asclepius, Oni Hunter''s
    Garb, Totem of Death, Dreamer''s Idol.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.49
      win: 0.47
      pick: 0.35
      fit: 0.16
    Genji's Guard:
      total: 0.47
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.16
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.44
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.56
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Oni Hunter's Garb
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
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Genji''s Guard, Blood-Bound Book, Bancroft''s
    Talon, Chandra''s Grace, Oni Hunter''s Garb, Freya''s Tears, Breastplate of Valor,
    Lifebinder, Phoenix Feather, The Cosmic Horror, Spectral Armor, Spear of the Magus,
    Erosion, Shifter''s Shield, Eye of Providence, Helm of Radiance, Draconic Scale,
    Leviathan''s Hide, Umbral Link, Bracer of The Abyss.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.19
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.49
    Oni Hunter's Garb:
      total: 0.46
      efficiency: 0.61
      win: 0.45
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.47
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.34
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear of the Magus,
    Genji''s Guard, Doom Orb, Screeching Gargoyle, The World Stone, Bracer of The
    Abyss, Dreamer''s Idol, Breastplate of Valor, Blood-Bound Book, Chronos'' Pendant,
    Bancroft''s Talon, Bragi''s Harp, Stone of Binding, Death Metal, Helm of Radiance,
    Kinetic Cuirass, Void Shield, Amanita Charm, Rod of Asclepius, Freya''s Tears,
    Eye of Providence, Oni Hunter''s Garb.'
  slot_scores:
    Nimble Ring:
      total: 0.58
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.53
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.66
    The Cosmic Horror:
      total: 0.49
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.57
    Spear of the Magus:
      total: 0.49
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.57
    Obsidian Shard:
      total: 0.48
      efficiency: 0.52
      win: 0.43
      pick: 0.3
      fit: 0.57
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
    of the Magus, Bragi''s Harp, Death Metal, Bracer of The Abyss, Breastplate of
    Valor, Blood-Bound Book, Chronos'' Pendant, Bancroft''s Talon, Kinetic Cuirass,
    Amanita Charm, Helm of Radiance, Freya''s Tears, Rod of Asclepius, Eye of Providence,
    Oni Hunter''s Garb, Shield of the Phoenix, Jade Scepter, Gem of Focus, Doom Orb,
    The World Stone, Ethereal Staff.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.51
      win: 0.45
      pick: 0.0
      fit: 0.41
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.49
    Bragi's Harp:
      total: 0.44
      efficiency: 0.42
      win: 0.45
      pick: 0.0
      fit: 0.64
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.47
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.38
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
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
    Grimoire, Breastplate of Valor, Chronos'' Pendant, Freya''s Tears, Shield of the
    Phoenix, The Cosmic Horror, Screeching Gargoyle, Gem of Focus, Chandra''s Grace,
    Spear of the Magus, Totem of Death, Bracer of The Abyss, Death Metal, Bragi''s
    Harp, Kinetic Cuirass, Amanita Charm, Blood-Bound Book, Eye of Providence, Oni
    Hunter''s Garb, Bancroft''s Talon, Gladiator''s Shield, Helm of Radiance, Rod
    of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.49
      win: 0.47
      pick: 0.35
      fit: 0.1
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.59
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.24
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Crusher
  flex_slots:
  - Tyrfing
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
    win/pick). Underrated for this god: The Crusher, Jotunn''s Revenge, Gluttonous
    Grimoire, Soul Gem, Tyrfing, The Reaper, Death Metal, Hydra''s Lament, The Cosmic
    Horror, Spear of the Magus, Genji''s Guard, Lernaean Bow, Bragi''s Harp, Runeforged
    Hammer, Riptalon, Golden Blade, Berserker''s Shield, Tekko-Kagi, Damaru, Breastplate
    of Valor, Blood-Bound Book, Chronos'' Pendant, Heartseeker, Pendulum Blade, Bancroft''s
    Talon, Titan''s Bane, Silverbranch Bow, Dominance, Transcendence, Avenging Blade,
    Triton''s Conch, Bracer of The Abyss, Arondight, Helm of Radiance, Shield Splitter,
    Kinetic Cuirass, Doom Orb, Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.48
      efficiency: 0.46
      win: 0.54
      pick: 0.07
      fit: 0.51
    Death Metal:
      total: 0.47
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.49
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.49
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Soul Gem, The
    Crusher, Jotunn''s Revenge, Tyrfing, Berserker''s Shield, The Cosmic Horror, Riptalon,
    Death Metal, Bragi''s Harp, Spear of the Magus, Lernaean Bow, Hydra''s Lament,
    Genji''s Guard, The Reaper, Golden Blade, Tekko-Kagi, Bracer of The Abyss, Silverbranch
    Bow, Runeforged Hammer, Blood-Bound Book, Chronos'' Pendant, Breastplate of Valor,
    Dominance, Damaru, Bancroft''s Talon, Pharaoh''s Curse, Helm of Radiance, Rod
    of Asclepius, Kinetic Cuirass, Doom Orb, Amanita Charm, Freya''s Tears, The World
    Stone, Heartseeker, Jade Scepter, Eye of Providence, Triton''s Conch.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.49
      win: 0.47
      pick: 0.35
      fit: 0.21
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.47
    Transcendence:
      total: 0.42
      efficiency: 0.52
      win: 0.45
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.58
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.53
    The Crusher:
      total: 0.5
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear
    of the Magus, Bracer of The Abyss, Genji''s Guard, Blood-Bound Book, Chronos''
    Pendant, Bragi''s Harp, Breastplate of Valor, Bancroft''s Talon, Death Metal,
    Helm of Radiance, Doom Orb, Rod of Asclepius, The World Stone, Gem of Focus, Freya''s
    Tears, Kinetic Cuirass, Jade Scepter, Totem of Death, Amanita Charm, Dreamer''s
    Idol, Typhon’s Heart, Shield of the Phoenix.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.51
      win: 0.45
      pick: 0.0
      fit: 0.56
    Nimble Ring:
      total: 0.6
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.68
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.56
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.44
    Spear of the Magus:
      total: 0.47
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Spectral Armor
  flex_slots:
  - Spectral Armor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Genji''s Guard, Rod of
    Asclepius, Spectral Armor, Erosion, Breastplate of Valor, The Cosmic Horror, Kinetic
    Cuirass, Doublet of Binding, Spear of the Magus, Freya''s Tears, Oni Hunter''s
    Garb, Bracer of The Abyss, Void Stone, Shield of the Phoenix, Lifebinder, Chronos''
    Pendant, Void Shield, Triton''s Conch, Blood-Bound Book, Stampede, Screeching
    Gargoyle, Chandra''s Grace.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.49
      win: 0.47
      pick: 0.35
      fit: 0.12
    Genji's Guard:
      total: 0.48
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.5
    Spear of Desolation:
      total: 0.48
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.46
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.29
    Spectral Armor:
      total: 0.46
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.38
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Amanita Charm, Genji''s Guard, Rod of Asclepius, Triton''s
    Conch, Spectral Armor, Death Metal, The Cosmic Horror, Breastplate of Valor, Spear
    of the Magus, Bragi''s Harp, Erosion, Oni Hunter''s Garb, Lifebinder, Kinetic
    Cuirass, Doublet of Binding, Bancroft''s Talon, Chronos'' Pendant, Bracer of The
    Abyss, Blood-Bound Book, Void Shield, Void Stone, Freya''s Tears, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.49
      win: 0.47
      pick: 0.35
      fit: 0.25
    Genji's Guard:
      total: 0.48
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.21
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.16
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.43
    Spear of Desolation:
      total: 0.48
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.4
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.37
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  flex_slots:
  - The Cosmic Horror
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Genji''s Guard, Rod of Asclepius,
    The Cosmic Horror, Spectral Armor, Spear of the Magus, Triton''s Conch, Breastplate
    of Valor, Erosion, Kinetic Cuirass, Death Metal, Doublet of Binding, Freya''s
    Tears, Lifebinder, Chronos'' Pendant, Oni Hunter''s Garb, Bragi''s Harp, Void
    Stone, Void Shield, Shield of the Phoenix, Bracer of The Abyss, Blood-Bound Book,
    Stampede.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.49
      win: 0.47
      pick: 0.35
      fit: 0.14
    Genji's Guard:
      total: 0.47
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.2
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.39
    Spear of Desolation:
      total: 0.49
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.49
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.35
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Doublet of Binding — magical protection
    swap_item: Doublet of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Spectral Armor, Erosion, Lifebinder, Kinetic Cuirass, Genji''s Guard,
    Umbral Link, Chandra''s Grace, Blood-Bound Book, Void Shield, Doublet of Binding,
    Freya''s Tears, Breastplate of Valor, Bancroft''s Talon, Oni Hunter''s Garb, Stampede,
    Void Stone, Phoenix Feather, Mystical Mail, Shifter''s Shield, Eye of Providence,
    The Cosmic Horror, Triton''s Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.49
    Spectral Armor:
      total: 0.49
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.49
      efficiency: 0.52
      win: 0.45
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Void Shield
  - Void Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Void Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Void Stone, Void Shield,
    Genji''s Guard, The Cosmic Horror, Spear of the Magus, Screeching Gargoyle, Rod
    of Asclepius, Spectral Armor, Erosion, Breastplate of Valor, Kinetic Cuirass,
    Doublet of Binding, Stone of Binding, Freya''s Tears, Oni Hunter''s Garb, Lifebinder,
    Shield of the Phoenix, Doom Orb, Chronos'' Pendant, Bracer of The Abyss, The World
    Stone, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.2
    Void Shield:
      total: 0.48
      efficiency: 0.46
      win: 0.45
      pick: 0.0
      fit: 0.77
    Void Stone:
      total: 0.48
      efficiency: 0.43
      win: 0.45
      pick: 0.0
      fit: 0.83
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.57
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.43
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Relativity
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
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Genji''s Guard, Rod of
    Asclepius, Spectral Armor, Erosion, Breastplate of Valor, Kinetic Cuirass, Triton''s
    Conch, Doublet of Binding, The Cosmic Horror, Oni Hunter''s Garb, Freya''s Tears,
    Spear of the Magus, Void Stone, Void Shield, Death Metal, Lifebinder, Bragi''s
    Harp, Bracer of The Abyss, Shield of the Phoenix, Chronos'' Pendant, Stampede,
    Eye of Providence, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.18
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.51
      win: 0.45
      pick: 0.0
      fit: 0.31
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.42
      fit: 0.38
    Bragi's Harp:
      total: 0.43
      efficiency: 0.42
      win: 0.45
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.21
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.8
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Spectral Armor
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Gluttonous
    Grimoire, Amanita Charm, Breastplate of Valor, Freya''s Tears, Rod of Asclepius,
    Spectral Armor, Shield of the Phoenix, Chronos'' Pendant, Erosion, Screeching
    Gargoyle, Kinetic Cuirass, Chandra''s Grace, Doublet of Binding, The Cosmic Horror,
    Triton''s Conch, Oni Hunter''s Garb, Spear of the Magus, Void Stone, Gem of Focus,
    Void Shield, Lifebinder, Totem of Death, Death Metal, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.46
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.36
    Spear of Desolation:
      total: 0.49
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.52
    Spectral Armor:
      total: 0.46
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.36
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.99
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - The Crusher
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, The Crusher,
    Gluttonous Grimoire, Amanita Charm, Tyrfing, Pharaoh''s Curse, Genji''s Guard,
    Hydra''s Lament, Rod of Asclepius, Triton''s Conch, The Reaper, Shogun''s Ofuda,
    Spectral Armor, Runeforged Hammer, Berserker''s Shield, Death Metal, Golden Blade,
    Erosion, Lernaean Bow, The Cosmic Horror, Breastplate of Valor, Kinetic Cuirass,
    Spear of the Magus, Riptalon, Sanguine Lash, Doublet of Binding, Eros'' Bow, Damaru,
    Freya''s Tears, Eye of the Storm, Oni Hunter''s Garb, Tekko-Kagi, Void Stone,
    Avenging Blade, Bragi''s Harp, Void Shield, Lifebinder, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.57
    Tyrfing:
      total: 0.48
      efficiency: 0.46
      win: 0.54
      pick: 0.07
      fit: 0.46
    Spear of Desolation:
      total: 0.48
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.41
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.53
    Pharaoh's Curse:
      total: 0.48
      efficiency: 0.55
      win: 0.45
      pick: 0.0
      fit: 0.54
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.9
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - The Crusher
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, Jotunn''s
    Revenge, The Crusher, Pharaoh''s Curse, Amanita Charm, Tyrfing, Rod of Asclepius,
    Shogun''s Ofuda, Genji''s Guard, Berserker''s Shield, Triton''s Conch, Spectral
    Armor, Hydra''s Lament, The Cosmic Horror, Eros'' Bow, Golden Blade, Death Metal,
    Spear of the Magus, Riptalon, Lernaean Bow, Erosion, Runeforged Hammer, Bragi''s
    Harp, The Reaper, Breastplate of Valor, Kinetic Cuirass, Lifebinder, Doublet of
    Binding, Chronos'' Pendant, Bracer of The Abyss, Silverbranch Bow, Oni Hunter''s
    Garb, Tekko-Kagi, Freya''s Tears, Void Stone, Void Shield, Blood-Bound Book.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.48
      efficiency: 0.46
      win: 0.54
      pick: 0.07
      fit: 0.47
    Spear of Desolation:
      total: 0.48
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.44
    The Crusher:
      total: 0.49
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.42
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.55
      win: 0.45
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.91
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Underrated for this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Genji''s
    Guard, Rod of Asclepius, Spectral Armor, Erosion, Breastplate of Valor, The Cosmic
    Horror, Kinetic Cuirass, Doublet of Binding, Spear of the Magus, Freya''s Tears,
    Oni Hunter''s Garb, Bracer of The Abyss, Void Stone, Shield of the Phoenix, Lifebinder,
    Chronos'' Pendant, Void Shield, Triton''s Conch, Blood-Bound Book, Stampede, Screeching
    Gargoyle, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.25
    Spear of Desolation:
      total: 0.48
      efficiency: 0.52
      win: 0.48
      pick: 0.33
      fit: 0.46
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.77
      win: 0.38
      pick: 0.4
      fit: 0.29
    Spectral Armor:
      total: 0.46
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.38
    Erosion:
      total: 0.45
      efficiency: 0.52
      win: 0.45
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.96
  starter: *id001
  aspect: Aspect of Relativity
---
