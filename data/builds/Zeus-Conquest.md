---
type: smite-build
god: Zeus
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.4
    win_rate: 0.56
    alternates:
    - name: Bancroft's Talon
      pick_rate: 0.18
      win_rate: 0.71
    - name: Book of Thoth
      pick_rate: 0.18
      win_rate: 0.53
  - name: The World Stone
    pick_rate: 0.14
    win_rate: 0.71
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.64
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.89
  - name: Rod of Tahuti
    pick_rate: 0.2
    win_rate: 0.58
    alternates:
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.56
    - name: Divine Ruin
      pick_rate: 0.05
      win_rate: 0.8
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.37
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 1.0
  - name: Spear of the Magus
    pick_rate: 0.06
    win_rate: 0.6
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.15
      win_rate: 0.58
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.67
  - name: Void Shard
    pick_rate: 0.1
    win_rate: 0.8
    alternates:
    - name: Killing Stone
      pick_rate: 0.1
      win_rate: 0.6
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.23
    win_rate: 0.64
  - name: Conduit Gem
    pick_rate: 0.16
    win_rate: 0.38
  - name: Pendulum of the Ages
    pick_rate: 0.12
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/zeus/
  last_verified: '2026-09-25'
  god_win_rate: 0.5979381443298969
  god_matches_won: 58
  god_matches_played: 97
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-25'
  god_matches_analyzed: 2996
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Divine Ruin, Spear of the Magus, Doom
    Orb, Bracer of The Abyss, Dreamer''s Idol, Chronos'' Pendant, Blood-Bound Book,
    Ancient Signet, Gem of Focus, The Cosmic Horror, Typhon’s Heart, Rod of Asclepius,
    Polynomicon, Totem of Death, Soul Reaver, Jade Scepter, Helm of Radiance, Bragi''s
    Harp, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.53
      pick: 0.18
      fit: 0.26
    Genji's Guard:
      total: 0.63
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.13
    Nimble Ring:
      total: 0.6
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.64
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.71
      pick: 0.19
      fit: 0.5
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.58
      pick: 0.31
      fit: 0.5
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.64
      pick: 0.27
      fit: 0.6
  community_ordered:
  - Book of Thoth
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Divine Ruin
  - Genji's Guard
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Divine Ruin
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Nimble
    Ring, Divine Ruin, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Doom
    Orb, Ancient Signet, Death Metal, Chronos'' Pendant, Bracer of The Abyss, Blood-Bound
    Book, Dreamer''s Idol, Gem of Focus, Polynomicon, Soul Reaver, Rod of Asclepius,
    The Cosmic Horror, Typhon’s Heart, Totem of Death, Jade Scepter, Triton''s Conch,
    Wish-Granting Pearl.'
  slot_scores:
    Divine Ruin:
      total: 0.56
      efficiency: 0.43
      win: 0.8
      pick: 0.08
      fit: 0.32
    Genji's Guard:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.19
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.45
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.71
      pick: 0.19
      fit: 0.44
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.58
      pick: 0.31
      fit: 0.44
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.64
      pick: 0.27
      fit: 0.46
  community_ordered:
  - Divine Ruin
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Genji''s Guard, Nimble Ring, Gluttonous Grimoire, Divine Ruin, Spear of the
    Magus, Doom Orb, Bragi''s Harp, Chronos'' Pendant, Dreamer''s Idol, Bracer of
    The Abyss, Death Metal, Ancient Signet, Gem of Focus, Blood-Bound Book, The Cosmic
    Horror, Totem of Death, Rod of Asclepius, Typhon’s Heart, Polynomicon, Soul Reaver,
    Jade Scepter, Breastplate of Valor.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.53
      pick: 0.18
      fit: 0.17
    Genji's Guard:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.17
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.42
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.71
      pick: 0.19
      fit: 0.42
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.58
      pick: 0.31
      fit: 0.42
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.64
      pick: 0.27
      fit: 0.52
  community_ordered:
  - Book of Thoth
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Bancroft's Talon
  - Book of Thoth
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - The World Stone
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, Gluttonous Grimoire, Rod of Asclepius,
    Nimble Ring, Shield of the Phoenix, Kinetic Cuirass, Ethereal Staff, Blood-Bound
    Book, Freya''s Tears, Breastplate of Valor, Spear of the Magus, Lifebinder, Shifter''s
    Shield, Helm of Radiance, Yogi''s Necklace, Sphere of Negation, Phoenix Feather,
    Chandra''s Grace, Erosion, Eye of Providence, Jade Scepter, Wish-Granting Pearl,
    Draconic Scale.'
  slot_scores:
    Bancroft's Talon:
      total: 0.59
      efficiency: 0.51
      win: 0.71
      pick: 0.18
      fit: 0.54
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.53
      pick: 0.18
      fit: 0.16
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.12
      fit: 0.2
    The World Stone:
      total: 0.56
      efficiency: 0.52
      win: 0.71
      pick: 0.19
      fit: 0.3
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.31
      fit: 0.3
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Bancroft's Talon
  - Book of Thoth
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Nimble Ring, Spear of the Magus, Divine Ruin,
    Doom Orb, Dreamer''s Idol, The Cosmic Horror, Bracer of The Abyss, Chronos'' Pendant,
    Blood-Bound Book, Ancient Signet, Gem of Focus, Rod of Asclepius, Typhon’s Heart,
    Polynomicon, Totem of Death, Soul Reaver, Jade Scepter, Screeching Gargoyle, Helm
    of Radiance, Ethereal Staff, Bragi''s Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.1
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.56
      pick: 0.4
      fit: 0.71
    The World Stone:
      total: 0.6
      efficiency: 0.52
      win: 0.71
      pick: 0.19
      fit: 0.6
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.58
      pick: 0.31
      fit: 0.6
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.64
      pick: 0.27
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Rod of Tahuti
  - Bragi's Harp
  - The World Stone
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Divine Ruin, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, Ancient Signet, Blood-Bound
    Book, Dreamer''s Idol, Death Metal, Gem of Focus, Rod of Asclepius, The Cosmic
    Horror, Typhon’s Heart, Polynomicon, Soul Reaver, Totem of Death, Jade Scepter,
    Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.08
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.31
      fit: 0.32
    Bragi's Harp:
      total: 0.53
      efficiency: 0.44
      win: 0.62
      pick: 0.0
      fit: 0.63
    The World Stone:
      total: 0.56
      efficiency: 0.52
      win: 0.71
      pick: 0.19
      fit: 0.32
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - The World Stone
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Nimble Ring, Gluttonous
    Grimoire, Chronos'' Pendant, Spear of the Magus, Gem of Focus, Bragi''s Harp,
    Doom Orb, Bracer of The Abyss, Totem of Death, Dreamer''s Idol, Ancient Signet,
    Blood-Bound Book, Breastplate of Valor, Death Metal, The Cosmic Horror, Rod of
    Asclepius, Typhon’s Heart, Polynomicon, Staff of Myrddin, Eye of Erebus, Soul
    Reaver.'
  slot_scores:
    Genji's Guard:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.35
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.56
      pick: 0.4
      fit: 0.63
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.19
      fit: 0.27
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.31
      fit: 0.27
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.27
      fit: 0.37
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.56
      pick: 0.16
      fit: 0.82
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Doom Orb
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
    Underrated for this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus,
    Doom Orb, Bracer of The Abyss, Dreamer''s Idol, Chronos'' Pendant, Blood-Bound
    Book, Ancient Signet, Gem of Focus, The Cosmic Horror, Typhon’s Heart, Rod of
    Asclepius, Polynomicon, Totem of Death, Soul Reaver, Jade Scepter, Divine Ruin,
    Helm of Radiance, Bragi''s Harp, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.6
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.56
      pick: 0.4
      fit: 0.63
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.58
      pick: 0.31
      fit: 0.5
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.6
      pick: 0.13
      fit: 0.5
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.64
      pick: 0.27
      fit: 0.6
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: *id001
---
