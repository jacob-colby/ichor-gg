---
type: smite-build
god: Sol
mode: Conquest
builds:
- source: community
  aspect: Aspect of Conflagration
  aspect_pick_rate: 0.68
  aspect_win_rate: 0.46
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.22
    win_rate: 0.52
    alternates:
    - name: Bragi's Harp
      pick_rate: 0.15
      win_rate: 0.69
    - name: Book of Thoth
      pick_rate: 0.13
      win_rate: 0.38
  - name: Book of Thoth
    pick_rate: 0.16
    win_rate: 0.41
    alternates:
    - name: Riptalon
      pick_rate: 0.12
      win_rate: 0.58
    - name: The World Stone
      pick_rate: 0.08
      win_rate: 0.5
  - name: Soul Gem
    pick_rate: 0.11
    win_rate: 0.73
    alternates:
    - name: Gem of Focus
      pick_rate: 0.1
      win_rate: 0.5
    - name: Chronos' Pendant
      pick_rate: 0.08
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.67
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.4
    - name: Gem of Focus
      pick_rate: 0.07
      win_rate: 0.43
  - name: Obsidian Shard
    pick_rate: 0.11
    win_rate: 0.7
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.17
      win_rate: 0.47
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.29
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.25
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.4
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.23
    win_rate: 0.54
  - name: Conduit Gem
    pick_rate: 0.13
    win_rate: 0.43
  - name: Sands Of Time
    pick_rate: 0.11
    win_rate: 0.18
  source_url: https://smitebrain.com/gods/sol/
  last_verified: '2026-08-14'
  god_win_rate: 0.47115384615384615
  god_matches_won: 49
  god_matches_played: 104
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
  - Bragi's Harp
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Bragi''s Harp, Gluttonous Grimoire, Spear of the Magus, Bracer of The
    Abyss, The Cosmic Horror, Nimble Ring, Genji''s Guard, Blood-Bound Book, Bancroft''s
    Talon, Chronos'' Pendant, Breastplate of Valor, The World Stone, Doom Orb, Helm
    of Radiance, Dreamer''s Idol, Death Metal, Rod of Asclepius, Jade Scepter, Typhon’s
    Heart, Totem of Death, Freya''s Tears, Ancient Signet, Kinetic Cuirass.'
  slot_scores:
    Bragi's Harp:
      total: 0.57
      efficiency: 0.44
      win: 0.69
      pick: 0.15
      fit: 0.64
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.22
      fit: 0.58
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.51
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.44
      win: 0.67
      pick: 0.32
      fit: 0.46
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.7
      pick: 0.24
      fit: 0.46
    Soul Gem:
      total: 0.66
      efficiency: 0.59
      win: 0.73
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
  - Spear of Desolation
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
    god: Bragi''s Harp, Gluttonous Grimoire, Genji''s Guard, Spear of the Magus, The
    Cosmic Horror, Breastplate of Valor, Bracer of The Abyss, Death Metal, Chronos''
    Pendant, Blood-Bound Book, Bancroft''s Talon, Nimble Ring, The World Stone, Doom
    Orb, Freya''s Tears, Dreamer''s Idol, Helm of Radiance, Kinetic Cuirass, Shield
    of the Phoenix, Rod of Asclepius, Amanita Charm, Totem of Death, Oni Hunter''s
    Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.16
    Bragi's Harp:
      total: 0.56
      efficiency: 0.44
      win: 0.69
      pick: 0.15
      fit: 0.62
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.52
      pick: 0.22
      fit: 0.56
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.32
      fit: 0.4
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.7
      pick: 0.24
      fit: 0.4
    Soul Gem:
      total: 0.65
      efficiency: 0.59
      win: 0.73
      pick: 0.17
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Kinetic Cuirass
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass, Genji''s Guard, Chandra''s
    Grace, Breastplate of Valor, Oni Hunter''s Garb, Spear of the Magus, Freya''s
    Tears, Lifebinder, The Cosmic Horror, Bracer of The Abyss, Phoenix Feather, Spectral
    Armor, Helm of Radiance, Shifter''s Shield, Jade Scepter, Erosion, Umbral Link,
    Eye of Providence.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.51
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.54
      efficiency: 0.44
      win: 0.69
      pick: 0.15
      fit: 0.44
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.44
      win: 0.67
      pick: 0.32
      fit: 0.28
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.7
      pick: 0.24
      fit: 0.28
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.73
      pick: 0.17
      fit: 0.83
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Bragi's Harp
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Bragi''s Harp, Spear of the Magus, The Cosmic
    Horror, Genji''s Guard, Bracer of The Abyss, The World Stone, Doom Orb, Dreamer''s
    Idol, Nimble Ring, Screeching Gargoyle, Breastplate of Valor, Blood-Bound Book,
    Bancroft''s Talon, Chronos'' Pendant, Helm of Radiance, Death Metal, Stone of
    Binding, Rod of Asclepius, Jade Scepter, Kinetic Cuirass, Void Shield, Freya''s
    Tears.'
  slot_scores:
    Bragi's Harp:
      total: 0.55
      efficiency: 0.44
      win: 0.69
      pick: 0.15
      fit: 0.53
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.52
      pick: 0.22
      fit: 0.66
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.51
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.44
      win: 0.67
      pick: 0.32
      fit: 0.56
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.7
      pick: 0.24
      fit: 0.56
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.73
      pick: 0.17
      fit: 0.86
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
    this god: Bragi''s Harp, Gluttonous Grimoire, Genji''s Guard, Spear of the Magus,
    Bracer of The Abyss, The Cosmic Horror, Death Metal, Breastplate of Valor, Nimble
    Ring, Blood-Bound Book, Bancroft''s Talon, Chronos'' Pendant, Helm of Radiance,
    Kinetic Cuirass, Rod of Asclepius, Amanita Charm, Oni Hunter''s Garb, Freya''s
    Tears, Jade Scepter, The World Stone, Doom Orb, Dreamer''s Idol, Eye of Providence.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.57
      efficiency: 0.44
      win: 0.69
      pick: 0.15
      fit: 0.63
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.44
      win: 0.67
      pick: 0.32
      fit: 0.31
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.7
      pick: 0.24
      fit: 0.31
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.73
      pick: 0.17
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Bragi's Harp
  - Spear of Desolation
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Bragi''s Harp, Genji''s Guard, Gluttonous
    Grimoire, Breastplate of Valor, Chronos'' Pendant, Freya''s Tears, Spear of the
    Magus, Shield of the Phoenix, Bracer of The Abyss, The Cosmic Horror, Totem of
    Death, Screeching Gargoyle, Chandra''s Grace, Death Metal, Blood-Bound Book, Nimble
    Ring, Bancroft''s Talon, Kinetic Cuirass, Amanita Charm, Oni Hunter''s Garb, Helm
    of Radiance, Eye of Providence, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.55
      efficiency: 0.44
      win: 0.69
      pick: 0.15
      fit: 0.52
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.22
      fit: 0.6
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.7
      pick: 0.24
      fit: 0.26
    Soul Gem:
      total: 0.66
      efficiency: 0.59
      win: 0.73
      pick: 0.17
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Bragi's Harp
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Crusher
  - Rod of Tahuti
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
    win/pick). Underrated for this god: Bragi''s Harp, Gluttonous Grimoire, Jotunn''s
    Revenge, The Crusher, Hydra''s Lament, Death Metal, Spear of the Magus, The Reaper,
    Lernaean Bow, Genji''s Guard, The Cosmic Horror, Berserker''s Shield, Runeforged
    Hammer, Golden Blade, Blood-Bound Book, Damaru, Breastplate of Valor, Bancroft''s
    Talon, Tekko-Kagi, Heartseeker, Bracer of The Abyss, Chronos'' Pendant, Dominance,
    Tyrfing, Pendulum Blade, Nimble Ring, Helm of Radiance, Titan''s Bane, The World
    Stone, Doom Orb, Triton''s Conch, Dreamer''s Idol, Rod of Asclepius, Avenging
    Blade, Arondight, Jade Scepter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.59
    Bragi's Harp:
      total: 0.58
      efficiency: 0.44
      win: 0.69
      pick: 0.15
      fit: 0.71
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.32
      fit: 0.39
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.7
      pick: 0.24
      fit: 0.39
    Soul Gem:
      total: 0.65
      efficiency: 0.59
      win: 0.73
      pick: 0.17
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Bragi's Harp
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - The Crusher
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
    + fit + win/pick). Underrated for this god: Bragi''s Harp, Gluttonous Grimoire,
    Jotunn''s Revenge, The Crusher, Berserker''s Shield, Lernaean Bow, Spear of the
    Magus, Death Metal, The Cosmic Horror, Hydra''s Lament, Bracer of The Abyss, Genji''s
    Guard, Golden Blade, The Reaper, Nimble Ring, Blood-Bound Book, Tekko-Kagi, Bancroft''s
    Talon, Breastplate of Valor, Chronos'' Pendant, Dominance, Tyrfing, Runeforged
    Hammer, Damaru, Pharaoh''s Curse, Helm of Radiance, Rod of Asclepius, The World
    Stone, Heartseeker, Doom Orb, Dreamer''s Idol, Jade Scepter, Kinetic Cuirass,
    Typhon’s Heart, Amanita Charm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.58
      efficiency: 0.44
      win: 0.69
      pick: 0.15
      fit: 0.75
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.32
      fit: 0.38
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.7
      pick: 0.24
      fit: 0.38
    Soul Gem:
      total: 0.64
      efficiency: 0.59
      win: 0.73
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, Bracer of The
    Abyss, The Cosmic Horror, Nimble Ring, Genji''s Guard, Blood-Bound Book, Bancroft''s
    Talon, Chronos'' Pendant, Breastplate of Valor, Bragi''s Harp, The World Stone,
    Doom Orb, Helm of Radiance, Dreamer''s Idol, Death Metal, Rod of Asclepius, Jade
    Scepter, Typhon’s Heart, Totem of Death, Freya''s Tears, Ancient Signet, Kinetic
    Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.12
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.67
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.22
      fit: 0.58
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.59
      win: 0.51
      pick: 0.0
      fit: 0.46
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.51
      pick: 0.0
      fit: 0.46
  starter: *id001
---
