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
    pick_rate: 0.46
    win_rate: 0.66
    alternates:
    - name: Book of Thoth
      pick_rate: 0.17
      win_rate: 0.62
    - name: Bancroft's Talon
      pick_rate: 0.16
      win_rate: 0.67
  - name: The World Stone
    pick_rate: 0.18
    win_rate: 0.57
    alternates:
    - name: Gem of Focus
      pick_rate: 0.13
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.78
  - name: Rod of Tahuti
    pick_rate: 0.21
    win_rate: 0.75
    alternates:
    - name: Soul Gem
      pick_rate: 0.2
      win_rate: 0.67
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.26
      win_rate: 0.63
    - name: Soul Gem
      pick_rate: 0.12
      win_rate: 1.0
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.4
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.2
      win_rate: 0.75
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.75
  - name: Blinking Abyss
    pick_rate: 0.14
    win_rate: 0.8
    alternates:
    - name: The World Stone
      pick_rate: 0.06
      win_rate: 1.0
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.26
    win_rate: 0.55
  - name: Archmage's Gem
    pick_rate: 0.21
    win_rate: 0.75
  - name: Blood-soaked Shroud
    pick_rate: 0.11
    win_rate: 0.88
  source_url: https://smitebrain.com/gods/zeus/
  last_verified: '2026-08-27'
  god_win_rate: 0.6052631578947368
  god_matches_won: 46
  god_matches_played: 76
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Doom Orb, Bracer
    of The Abyss, Dreamer''s Idol, Chronos'' Pendant, Blood-Bound Book, Ancient Signet,
    The Cosmic Horror, Typhon’s Heart, Rod of Asclepius, Polynomicon, Totem of Death,
    Soul Reaver, Jade Scepter, Divine Ruin, Helm of Radiance, Bragi''s Harp, Ethereal
    Staff, Wish-Granting Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.66
      pick: 0.46
      fit: 0.63
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.5
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.75
      pick: 0.33
      fit: 0.5
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.27
      fit: 0.6
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Nimble Ring
  - Ancient Signet
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Doom Orb
  - Ancient Signet
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Nimble
    Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Doom Orb, Ancient
    Signet, Death Metal, Chronos'' Pendant, Bracer of The Abyss, Blood-Bound Book,
    Dreamer''s Idol, Polynomicon, Soul Reaver, Rod of Asclepius, The Cosmic Horror,
    Typhon’s Heart, Totem of Death, Jade Scepter, Divine Ruin, Triton''s Conch, Wish-Granting
    Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.45
    Ancient Signet:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.66
      pick: 0.46
      fit: 0.47
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.75
      pick: 0.33
      fit: 0.44
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.27
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Doom Orb
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
    god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Doom Orb, Bragi''s
    Harp, Chronos'' Pendant, Dreamer''s Idol, Bracer of The Abyss, Death Metal, Ancient
    Signet, Blood-Bound Book, The Cosmic Horror, Totem of Death, Rod of Asclepius,
    Typhon’s Heart, Polynomicon, Soul Reaver, Jade Scepter, Divine Ruin, Breastplate
    of Valor, Genji''s Guard.'
  slot_scores:
    Nimble Ring:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.66
      pick: 0.46
      fit: 0.58
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.42
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.75
      pick: 0.33
      fit: 0.42
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.67
      pick: 0.27
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shifter's Shield
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Nimble Ring, Shield
    of the Phoenix, Kinetic Cuirass, Ethereal Staff, Blood-Bound Book, Freya''s Tears,
    Genji''s Guard, Breastplate of Valor, Spear of the Magus, Lifebinder, Helm of
    Radiance, Yogi''s Necklace, Sphere of Negation, Phoenix Feather, Chandra''s Grace,
    Erosion, Eye of Providence, Jade Scepter, Wish-Granting Pearl, Draconic Scale.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.49
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.78
      pick: 0.16
      fit: 0.39
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.66
      pick: 0.46
      fit: 0.38
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.75
      pick: 0.33
      fit: 0.3
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.67
      pick: 0.31
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Doom Orb
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
    for this god: Gluttonous Grimoire, Nimble Ring, Spear of the Magus, Doom Orb,
    Dreamer''s Idol, The Cosmic Horror, Bracer of The Abyss, Chronos'' Pendant, Blood-Bound
    Book, Ancient Signet, Rod of Asclepius, Typhon’s Heart, Polynomicon, Totem of
    Death, Soul Reaver, Jade Scepter, Divine Ruin, Screeching Gargoyle, Helm of Radiance,
    Ethereal Staff, Bragi''s Harp.'
  slot_scores:
    Nimble Ring:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.66
      pick: 0.46
      fit: 0.71
    Doom Orb:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.6
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.75
      pick: 0.33
      fit: 0.6
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.67
      pick: 0.27
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Doom Orb, Chronos'' Pendant, Ancient Signet, Blood-Bound
    Book, Dreamer''s Idol, Death Metal, Rod of Asclepius, The Cosmic Horror, Typhon’s
    Heart, Polynomicon, Soul Reaver, Totem of Death, Jade Scepter, Divine Ruin, Helm
    of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.55
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.66
      pick: 0.46
      fit: 0.4
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.75
      pick: 0.33
      fit: 0.32
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.67
      pick: 0.31
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Nimble Ring, Gluttonous Grimoire,
    Chronos'' Pendant, Spear of the Magus, Bragi''s Harp, Doom Orb, Bracer of The
    Abyss, Totem of Death, Dreamer''s Idol, Ancient Signet, Blood-Bound Book, Breastplate
    of Valor, Genji''s Guard, Death Metal, The Cosmic Horror, Rod of Asclepius, Typhon’s
    Heart, Polynomicon, Staff of Myrddin, Eye of Erebus, Soul Reaver.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.66
      pick: 0.46
      fit: 0.63
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.27
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.75
      pick: 0.33
      fit: 0.27
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.27
      fit: 0.37
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.67
      pick: 0.31
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
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
    Book, Ancient Signet, The Cosmic Horror, Typhon’s Heart, Rod of Asclepius, Polynomicon,
    Totem of Death, Soul Reaver, Jade Scepter, Divine Ruin, Helm of Radiance, Bragi''s
    Harp, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.66
      pick: 0.46
      fit: 0.63
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.5
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.75
      pick: 0.33
      fit: 0.5
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.27
      fit: 0.6
  starter: *id001
---
