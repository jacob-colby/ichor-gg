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
  - name: Book of Thoth
    pick_rate: 0.4
    win_rate: 0.44
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.25
      win_rate: 0.4
    - name: Blood-Bound Book
      pick_rate: 0.13
      win_rate: 0.8
  - name: Spear of Desolation
    pick_rate: 0.25
    win_rate: 0.4
    alternates:
    - name: The World Stone
      pick_rate: 0.15
      win_rate: 0.17
    - name: Bancroft's Talon
      pick_rate: 0.13
      win_rate: 0.8
  - name: Rod of Tahuti
    pick_rate: 0.2
    win_rate: 0.63
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.2
    - name: Staff of Myrddin
      pick_rate: 0.13
      win_rate: 0.8
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.43
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.36
      win_rate: 0.5
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.5
  - name: Blinking Abyss
    pick_rate: 0.14
    win_rate: 0.4
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.25
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.25
  - name: Evil Eye
    pick_rate: 0.15
    win_rate: 0.25
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.5
    - name: Soul Gem
      pick_rate: 0.07
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.23
    win_rate: 0.33
  - name: Conduit Gem
    pick_rate: 0.18
    win_rate: 0.57
  - name: Pendulum of the Ages
    pick_rate: 0.18
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/zeus/
  last_verified: '2026-10-08'
  god_win_rate: 0.55
  god_matches_won: 22
  god_matches_played: 40
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Blood-Bound Book
  - Spear of Desolation
  - Spear of the Magus
  - Staff of Myrddin
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Blood-Bound Book, Nimble Ring, Gluttonous Grimoire, Spear of the Magus,
    Doom Orb, Bracer of The Abyss, Dreamer''s Idol, Chronos'' Pendant, Ancient Signet,
    Gem of Focus, The Cosmic Horror, Typhon’s Heart, Rod of Asclepius, Polynomicon,
    Totem of Death, Soul Reaver, Jade Scepter, Divine Ruin, Helm of Radiance, Bragi''s
    Harp, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Blood-Bound Book:
      total: 0.61
      efficiency: 0.54
      win: 0.8
      pick: 0.13
      fit: 0.39
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.4
      pick: 0.34
      fit: 0.63
    Spear of the Magus:
      total: 0.48
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.5
    Staff of Myrddin:
      total: 0.55
      efficiency: 0.34
      win: 0.8
      pick: 0.2
      fit: 0.39
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.63
      pick: 0.31
      fit: 0.5
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.43
      pick: 0.3
      fit: 0.6
  community_ordered:
  - Blood-Bound Book
  - Spear of Desolation
  - Staff of Myrddin
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Doom Orb
  - Staff of Myrddin
  flex_slots:
  - Doom Orb
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Blood-Bound
    Book, Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Doom
    Orb, Ancient Signet, Death Metal, Chronos'' Pendant, Bracer of The Abyss, Dreamer''s
    Idol, Gem of Focus, Polynomicon, Soul Reaver, Rod of Asclepius, The Cosmic Horror,
    Typhon’s Heart, Totem of Death, Jade Scepter, Divine Ruin, Triton''s Conch, Wish-Granting
    Pearl.'
  slot_scores:
    Bancroft's Talon:
      total: 0.6
      efficiency: 0.51
      win: 0.8
      pick: 0.18
      fit: 0.38
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.44
      pick: 0.4
      fit: 0.3
    Spear of Desolation:
      total: 0.47
      efficiency: 0.57
      win: 0.4
      pick: 0.34
      fit: 0.47
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.63
      pick: 0.31
      fit: 0.44
    Doom Orb:
      total: 0.45
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.44
    Staff of Myrddin:
      total: 0.54
      efficiency: 0.34
      win: 0.8
      pick: 0.2
      fit: 0.33
  community_ordered:
  - Bancroft's Talon
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Staff of Myrddin
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Blood-Bound Book
  - Spear of Desolation
  - Spear of the Magus
  - Staff of Myrddin
  - Rod of Tahuti
  - Obsidian Shard
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Blood-Bound Book, Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Doom
    Orb, Bragi''s Harp, Chronos'' Pendant, Dreamer''s Idol, Bracer of The Abyss, Death
    Metal, Ancient Signet, Gem of Focus, The Cosmic Horror, Totem of Death, Rod of
    Asclepius, Typhon’s Heart, Polynomicon, Soul Reaver, Jade Scepter, Divine Ruin,
    Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Blood-Bound Book:
      total: 0.59
      efficiency: 0.54
      win: 0.8
      pick: 0.13
      fit: 0.25
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.4
      pick: 0.34
      fit: 0.58
    Spear of the Magus:
      total: 0.47
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.42
    Staff of Myrddin:
      total: 0.54
      efficiency: 0.34
      win: 0.8
      pick: 0.2
      fit: 0.33
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.63
      pick: 0.31
      fit: 0.42
    Obsidian Shard:
      total: 0.48
      efficiency: 0.54
      win: 0.43
      pick: 0.3
      fit: 0.52
  community_ordered:
  - Blood-Bound Book
  - Spear of Desolation
  - Staff of Myrddin
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Blood-Bound Book
  - Bancroft's Talon
  - Book of Thoth
  - Rod of Tahuti
  - Kinetic Cuirass
  - Staff of Myrddin
  flex_slots:
  - Kinetic Cuirass
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Blood-Bound Book, Amanita Charm, Gluttonous Grimoire, Rod of Asclepius,
    Nimble Ring, Shield of the Phoenix, Kinetic Cuirass, Ethereal Staff, Freya''s
    Tears, Genji''s Guard, Breastplate of Valor, Spear of the Magus, Lifebinder, Shifter''s
    Shield, Helm of Radiance, Yogi''s Necklace, Sphere of Negation, Phoenix Feather,
    Chandra''s Grace, Erosion, Eye of Providence, Jade Scepter, Wish-Granting Pearl,
    Draconic Scale.'
  slot_scores:
    Blood-Bound Book:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.13
      fit: 0.54
    Bancroft's Talon:
      total: 0.63
      efficiency: 0.51
      win: 0.8
      pick: 0.18
      fit: 0.54
    Book of Thoth:
      total: 0.42
      efficiency: 0.51
      win: 0.44
      pick: 0.4
      fit: 0.16
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.31
      fit: 0.3
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.49
    Staff of Myrddin:
      total: 0.52
      efficiency: 0.34
      win: 0.8
      pick: 0.2
      fit: 0.24
  community_ordered:
  - Blood-Bound Book
  - Bancroft's Talon
  - Book of Thoth
  - Rod of Tahuti
  - Staff of Myrddin
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Blood-Bound Book
  - Spear of Desolation
  - Spear of the Magus
  - Staff of Myrddin
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Spear of the Magus
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
    for this god: Blood-Bound Book, Gluttonous Grimoire, Nimble Ring, Spear of the
    Magus, Doom Orb, Dreamer''s Idol, The Cosmic Horror, Bracer of The Abyss, Chronos''
    Pendant, Ancient Signet, Gem of Focus, Rod of Asclepius, Typhon’s Heart, Polynomicon,
    Totem of Death, Soul Reaver, Jade Scepter, Divine Ruin, Screeching Gargoyle, Helm
    of Radiance, Ethereal Staff, Bragi''s Harp.'
  slot_scores:
    Blood-Bound Book:
      total: 0.6
      efficiency: 0.54
      win: 0.8
      pick: 0.13
      fit: 0.31
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.4
      pick: 0.34
      fit: 0.71
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.6
    Staff of Myrddin:
      total: 0.54
      efficiency: 0.34
      win: 0.8
      pick: 0.2
      fit: 0.31
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.63
      pick: 0.31
      fit: 0.6
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.43
      pick: 0.3
      fit: 0.7
  community_ordered:
  - Blood-Bound Book
  - Spear of Desolation
  - Staff of Myrddin
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Blood-Bound Book
  - Bracer of The Abyss
  - Nimble Ring
  - Rod of Tahuti
  - Bragi's Harp
  - Staff of Myrddin
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
    this god: Blood-Bound Book, Nimble Ring, Gluttonous Grimoire, Spear of the Magus,
    Bragi''s Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, Ancient Signet,
    Dreamer''s Idol, Death Metal, Gem of Focus, Rod of Asclepius, The Cosmic Horror,
    Typhon’s Heart, Polynomicon, Soul Reaver, Totem of Death, Jade Scepter, Divine
    Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Blood-Bound Book:
      total: 0.59
      efficiency: 0.54
      win: 0.8
      pick: 0.13
      fit: 0.25
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.44
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.63
      pick: 0.31
      fit: 0.32
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.44
      pick: 0.0
      fit: 0.63
    Staff of Myrddin:
      total: 0.53
      efficiency: 0.34
      win: 0.8
      pick: 0.2
      fit: 0.25
  community_ordered:
  - Blood-Bound Book
  - Rod of Tahuti
  - Staff of Myrddin
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Staff of Myrddin
  - Rod of Tahuti
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Blood-Bound Book, Nimble Ring, Gluttonous
    Grimoire, Chronos'' Pendant, Spear of the Magus, Gem of Focus, Bragi''s Harp,
    Doom Orb, Bracer of The Abyss, Totem of Death, Dreamer''s Idol, Ancient Signet,
    Breastplate of Valor, Genji''s Guard, Death Metal, The Cosmic Horror, Rod of Asclepius,
    Typhon’s Heart, Polynomicon, Eye of Erebus, Soul Reaver.'
  slot_scores:
    Chronos' Pendant:
      total: 0.46
      efficiency: 0.55
      win: 0.44
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.4
      pick: 0.34
      fit: 0.63
    Staff of Myrddin:
      total: 0.56
      efficiency: 0.34
      win: 0.8
      pick: 0.2
      fit: 0.46
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.31
      fit: 0.27
    Obsidian Shard:
      total: 0.46
      efficiency: 0.54
      win: 0.43
      pick: 0.3
      fit: 0.37
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.22
      fit: 0.82
  community_ordered:
  - Spear of Desolation
  - Staff of Myrddin
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
      total: 0.52
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.4
      pick: 0.34
      fit: 0.63
    Doom Orb:
      total: 0.46
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.63
      pick: 0.31
      fit: 0.5
    Spear of the Magus:
      total: 0.48
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.5
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.43
      pick: 0.3
      fit: 0.6
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
