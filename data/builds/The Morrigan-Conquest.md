---
type: smite-build
god: The Morrigan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mischief
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.75
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.3
    win_rate: 0.54
    alternates:
    - name: The World Stone
      pick_rate: 0.26
      win_rate: 0.5
    - name: Spear of Desolation
      pick_rate: 0.19
      win_rate: 0.45
  - name: The World Stone
    pick_rate: 0.41
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.53
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.78
  - name: Polynomicon
    pick_rate: 0.33
    win_rate: 0.47
    alternates:
    - name: The World Stone
      pick_rate: 0.11
      win_rate: 0.62
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.31
  - name: Rod of Tahuti
    pick_rate: 0.25
    win_rate: 0.48
    alternates:
    - name: Polynomicon
      pick_rate: 0.22
      win_rate: 0.54
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.63
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.6
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.23
      win_rate: 0.5
    - name: Chandra's Grace
      pick_rate: 0.06
      win_rate: 0.5
  - name: Evil Eye
    pick_rate: 0.16
    win_rate: 0.8
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.15
      win_rate: 0.44
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.67
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.3
    win_rate: 0.49
  - name: Conduit Gem
    pick_rate: 0.24
    win_rate: 0.43
  - name: Bluestone Brooch
    pick_rate: 0.09
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/the-morrigan/
  last_verified: '2026-08-27'
  god_win_rate: 0.5258620689655172
  god_matches_won: 61
  god_matches_played: 116
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
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Soul Gem
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem
    of Death, Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Wish-Granting Pearl,
    Staff of Myrddin, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.53
      pick: 0.2
      fit: 1.0
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.8
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.56
      fit: 0.8
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.48
      pick: 0.42
      fit: 0.8
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.6
      pick: 0.35
      fit: 0.9
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Breastplate
    of Valor, Soul Gem, Spear of the Magus, Doom Orb, Death Metal, Gluttonous Grimoire,
    Ancient Signet, Chronos'' Pendant, Dreamer''s Idol, Bragi''s Harp, Gem of Focus,
    Soul Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of
    Death, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting
    Pearl, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.54
      pick: 0.3
      fit: 0.39
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.47
      win: 0.78
      pick: 0.11
      fit: 0.24
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.2
      fit: 0.61
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.55
      pick: 0.56
      fit: 0.57
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.48
      pick: 0.42
      fit: 0.57
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.6
      pick: 0.35
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Breastplate of Valor, Spear of the Magus, Gluttonous Grimoire,
    Doom Orb, Dreamer''s Idol, Chronos'' Pendant, Death Metal, Gem of Focus, The Cosmic
    Horror, Ancient Signet, Bragi''s Harp, Totem of Death, Rod of Asclepius, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Triton''s Conch, Bancroft''s Talon,
    Genji''s Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.54
      pick: 0.3
      fit: 0.22
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.47
      win: 0.78
      pick: 0.11
      fit: 0.22
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.2
      fit: 0.78
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.48
      pick: 0.42
      fit: 0.56
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.6
      pick: 0.35
      fit: 0.66
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Freya''s Tears, Soul Gem, Rod of
    Asclepius, Shield of the Phoenix, Gluttonous Grimoire, Kinetic Cuirass, Ethereal
    Staff, Spear of the Magus, Shifter''s Shield, Genji''s Guard, Lifebinder, Helm
    of Radiance, Sphere of Negation, Erosion, Yogi''s Necklace, Eye of Providence,
    Draconic Scale, Phoenix Feather, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Doom Orb, Stone of Binding, Chandra''s Grace.'
  slot_scores:
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.78
      pick: 0.11
      fit: 0.25
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.12
      fit: 0.41
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.48
      pick: 0.42
      fit: 0.39
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.6
      pick: 0.35
      fit: 0.49
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.55
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
  - Spear of the Magus
  - Soul Gem
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, Breastplate of Valor, The Cosmic Horror, Chronos'' Pendant, Ancient Signet,
    Gem of Focus, Rod of Asclepius, Totem of Death, Blood-Bound Book, Soul Reaver,
    Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Screeching Gargoyle, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.53
      pick: 0.2
      fit: 1.0
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.86
    The World Stone:
      total: 0.59
      efficiency: 0.52
      win: 0.55
      pick: 0.56
      fit: 0.86
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.48
      pick: 0.42
      fit: 0.86
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.6
      pick: 0.35
      fit: 0.96
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, Ancient Signet, Dreamer''s
    Idol, Blood-Bound Book, Death Metal, Bancroft''s Talon, Gem of Focus, The Cosmic
    Horror, Rod of Asclepius, Typhon’s Heart, Soul Reaver, Jade Scepter, Divine Ruin,
    Totem of Death, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.47
      win: 0.78
      pick: 0.11
      fit: 0.08
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.55
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.48
      pick: 0.42
      fit: 0.32
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.35
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Soul Gem, Chronos''
    Pendant, Spear of the Magus, Gem of Focus, Gluttonous Grimoire, Totem of Death,
    Doom Orb, Freya''s Tears, Dreamer''s Idol, Genji''s Guard, Ancient Signet, Death
    Metal, The Cosmic Horror, Staff of Myrddin, Eye of Erebus, Screeching Gargoyle,
    Bragi''s Harp, Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Chandra''s Grace.'
  slot_scores:
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.47
      win: 0.78
      pick: 0.11
      fit: 0.48
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.53
      pick: 0.2
      fit: 0.86
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.48
      pick: 0.42
      fit: 0.38
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.6
      pick: 0.35
      fit: 0.48
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.55
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
    Orb, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Ancient
    Signet, Totem of Death, Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade
    Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Wish-Granting
    Pearl, Staff of Myrddin, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.53
      pick: 0.2
      fit: 1.0
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.8
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.8
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.48
      pick: 0.42
      fit: 0.8
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.6
      pick: 0.35
      fit: 0.9
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 1.0
  starter: *id001
---
