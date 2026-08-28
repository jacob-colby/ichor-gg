---
type: smite-build
god: The Morrigan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mischief
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.76
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.33
    win_rate: 0.53
    alternates:
    - name: The World Stone
      pick_rate: 0.21
      win_rate: 0.49
    - name: Spear of Desolation
      pick_rate: 0.21
      win_rate: 0.44
  - name: The World Stone
    pick_rate: 0.43
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.45
    - name: Gem of Focus
      pick_rate: 0.07
      win_rate: 0.31
  - name: Polynomicon
    pick_rate: 0.39
    win_rate: 0.5
    alternates:
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.52
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.27
  - name: Rod of Tahuti
    pick_rate: 0.27
    win_rate: 0.49
    alternates:
    - name: Polynomicon
      pick_rate: 0.2
      win_rate: 0.5
    - name: Gem of Focus
      pick_rate: 0.11
      win_rate: 0.56
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.26
      win_rate: 0.54
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.3
  - name: Evil Eye
    pick_rate: 0.15
    win_rate: 0.64
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.16
      win_rate: 0.6
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.35
    win_rate: 0.51
  - name: Conduit Gem
    pick_rate: 0.22
    win_rate: 0.41
  - name: Bumba's Cudgel
    pick_rate: 0.11
    win_rate: 0.37
  source_url: https://smitebrain.com/gods/the-morrigan/
  last_verified: '2026-08-28'
  god_win_rate: 0.5142857142857142
  god_matches_won: 90
  god_matches_played: 175
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-28'
  god_matches_analyzed: 3498
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Book of Thoth
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
    this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, Chronos'' Pendant, The Cosmic Horror, Ancient Signet, Totem of Death, Rod
    of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Wish-Granting Pearl, Staff of Myrddin,
    Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.53
      pick: 0.33
      fit: 0.4
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.8
    The World Stone:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.59
      fit: 0.8
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.49
      pick: 0.45
      fit: 0.8
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.52
      pick: 0.39
      fit: 0.9
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Spear of the Magus, Doom Orb, Death Metal, Gluttonous Grimoire, Ancient Signet,
    Chronos'' Pendant, Dreamer''s Idol, Bragi''s Harp, Soul Reaver, The Cosmic Horror,
    Rod of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s Conch, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate
    of Valor, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.53
      pick: 0.33
      fit: 0.39
    Doom Orb:
      total: 0.51
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.57
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.59
      fit: 0.57
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.49
      pick: 0.45
      fit: 0.57
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.52
      pick: 0.39
      fit: 0.57
    Soul Gem:
      total: 0.52
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    Chronos'' Pendant, Death Metal, The Cosmic Horror, Ancient Signet, Bragi''s Harp,
    Totem of Death, Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s Talon, Genji''s
    Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.53
      pick: 0.33
      fit: 0.22
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.59
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.49
      pick: 0.45
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.52
      pick: 0.39
      fit: 0.66
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Kinetic Cuirass
  - The World Stone
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus,
    Shifter''s Shield, Genji''s Guard, Breastplate of Valor, Lifebinder, Helm of Radiance,
    Sphere of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale,
    Phoenix Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound
    Book, Doom Orb, Stone of Binding.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.53
      pick: 0.33
      fit: 0.2
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.61
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.59
      fit: 0.39
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.49
      pick: 0.45
      fit: 0.39
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
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
    for this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, The Cosmic Horror, Chronos'' Pendant, Ancient Signet, Rod of Asclepius,
    Totem of Death, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle, Wish-Granting Pearl,
    Typhon’s Heart, Breastplate of Valor, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.44
      pick: 0.21
      fit: 1.0
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.86
    The World Stone:
      total: 0.6
      efficiency: 0.52
      win: 0.57
      pick: 0.59
      fit: 0.86
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.49
      pick: 0.45
      fit: 0.86
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.52
      pick: 0.39
      fit: 0.96
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - The World Stone
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
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, Ancient Signet, Dreamer''s
    Idol, Blood-Bound Book, Death Metal, Bancroft''s Talon, The Cosmic Horror, Rod
    of Asclepius, Typhon’s Heart, Soul Reaver, Jade Scepter, Divine Ruin, Totem of
    Death, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.62
    The World Stone:
      total: 0.51
      efficiency: 0.52
      win: 0.57
      pick: 0.59
      fit: 0.32
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.49
      pick: 0.45
      fit: 0.32
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Gem of Focus
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The World Stone
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Spear
    of the Magus, Gluttonous Grimoire, Totem of Death, Doom Orb, Breastplate of Valor,
    Dreamer''s Idol, Genji''s Guard, Ancient Signet, Death Metal, The Cosmic Horror,
    Staff of Myrddin, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius,
    Chandra''s Grace, Freya''s Tears, Blood-Bound Book, Soul Reaver, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.53
      pick: 0.33
      fit: 0.14
    Gem of Focus:
      total: 0.53
      efficiency: 0.5
      win: 0.56
      pick: 0.18
      fit: 0.62
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.44
      pick: 0.21
      fit: 0.86
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.59
      fit: 0.38
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.49
      pick: 0.45
      fit: 0.38
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    Underrated for this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom
    Orb, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Ancient Signet, Totem
    of Death, Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Wish-Granting Pearl,
    Staff of Myrddin, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.44
      pick: 0.21
      fit: 1.0
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.8
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.8
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.49
      pick: 0.45
      fit: 0.8
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.52
      pick: 0.39
      fit: 0.9
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 1.0
  starter: *id001
---
