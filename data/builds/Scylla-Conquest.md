---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.52
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.37
    win_rate: 0.58
    alternates:
    - name: Book of Thoth
      pick_rate: 0.25
      win_rate: 0.6
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.59
  - name: Book of Thoth
    pick_rate: 0.22
    win_rate: 0.62
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.54
    - name: Chronos' Pendant
      pick_rate: 0.08
      win_rate: 0.54
  - name: Rod of Tahuti
    pick_rate: 0.24
    win_rate: 0.58
    alternates:
    - name: Polynomicon
      pick_rate: 0.22
      win_rate: 0.55
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.53
  - name: Obsidian Shard
    pick_rate: 0.22
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.33
      win_rate: 0.59
    - name: Polynomicon
      pick_rate: 0.08
      win_rate: 0.59
  - name: Polynomicon
    pick_rate: 0.06
    win_rate: 0.61
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.26
      win_rate: 0.6
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.71
  - name: Dreamer's Idol
    pick_rate: 0.08
    win_rate: 0.81
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.78
    - name: Killing Stone
      pick_rate: 0.07
      win_rate: 0.64
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.52
    win_rate: 0.6
  - name: Conduit Gem
    pick_rate: 0.32
    win_rate: 0.52
  - name: Warrior's Axe
    pick_rate: 0.08
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-09-29'
  god_win_rate: 0.5638474295190713
  god_matches_won: 340
  god_matches_played: 603
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-29'
  god_matches_analyzed: 8229
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World
    Stone, The Cosmic Horror, Chronos'' Pendant, Gem of Focus, Ancient Signet, Polynomicon,
    Totem of Death, Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin,
    Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.62
      pick: 0.3
      fit: 0.42
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.58
      pick: 0.37
      fit: 1.0
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.58
      pick: 0.37
      fit: 0.79
    Dreamer's Idol:
      total: 0.67
      efficiency: 0.51
      win: 0.81
      pick: 0.25
      fit: 0.79
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Gem, Spear of the Magus, Doom Orb, The World Stone, Death Metal, Gluttonous Grimoire,
    Ancient Signet, Polynomicon, Chronos'' Pendant, Bragi''s Harp, Gem of Focus, Soul
    Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of Death,
    Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl,
    Helm of Radiance, Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.62
      pick: 0.3
      fit: 0.39
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.58
      pick: 0.37
      fit: 0.61
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.58
      pick: 0.37
      fit: 0.57
    Dreamer's Idol:
      total: 0.62
      efficiency: 0.51
      win: 0.81
      pick: 0.25
      fit: 0.47
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone,
    Chronos'' Pendant, Death Metal, Gem of Focus, The Cosmic Horror, Ancient Signet,
    Polynomicon, Bragi''s Harp, Totem of Death, Rod of Asclepius, Blood-Bound Book,
    Soul Reaver, Jade Scepter, Divine Ruin, Triton''s Conch, Breastplate of Valor,
    Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.62
      pick: 0.3
      fit: 0.22
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.58
      pick: 0.37
      fit: 0.78
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.58
      pick: 0.37
      fit: 0.56
    Dreamer's Idol:
      total: 0.64
      efficiency: 0.51
      win: 0.81
      pick: 0.25
      fit: 0.56
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
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
    this god: Amanita Charm, Soul Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus,
    Shifter''s Shield, Breastplate of Valor, Lifebinder, Helm of Radiance, Sphere
    of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Genji''s Guard, Draconic
    Scale, Phoenix Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound
    Book, Doom Orb, Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.37
      fit: 0.49
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.58
      pick: 0.37
      fit: 0.39
    Dreamer's Idol:
      total: 0.61
      efficiency: 0.51
      win: 0.81
      pick: 0.25
      fit: 0.39
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom Orb, The
    World Stone, The Cosmic Horror, Chronos'' Pendant, Ancient Signet, Gem of Focus,
    Polynomicon, Rod of Asclepius, Totem of Death, Blood-Bound Book, Soul Reaver,
    Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Screeching Gargoyle, Wish-Granting Pearl, Typhon’s Heart, Breastplate of Valor,
    Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.58
      pick: 0.37
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.58
      pick: 0.37
      fit: 0.85
    Dreamer's Idol:
      total: 0.68
      efficiency: 0.51
      win: 0.81
      pick: 0.25
      fit: 0.85
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Harp, Bracer of The Abyss, Doom Orb, The World Stone, Ancient Signet, Blood-Bound
    Book, Death Metal, Polynomicon, Chronos'' Pendant, Bancroft''s Talon, Gem of Focus,
    Rod of Asclepius, The Cosmic Horror, Typhon’s Heart, Soul Reaver, Totem of Death,
    Jade Scepter, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.51
      efficiency: 0.44
      win: 0.58
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.37
      fit: 0.32
    Dreamer's Idol:
      total: 0.6
      efficiency: 0.51
      win: 0.81
      pick: 0.25
      fit: 0.32
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - Gem of Focus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
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
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Gem of
    Focus, Spear of the Magus, Gluttonous Grimoire, Totem of Death, Doom Orb, The
    World Stone, Breastplate of Valor, Ancient Signet, Death Metal, Polynomicon, Genji''s
    Guard, Staff of Myrddin, The Cosmic Horror, Eye of Erebus, Screeching Gargoyle,
    Bragi''s Harp, Rod of Asclepius, Chandra''s Grace, Freya''s Tears, Blood-Bound
    Book, Soul Reaver, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.54
      pick: 0.11
      fit: 0.63
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.58
      pick: 0.37
      fit: 0.86
    Gem of Focus:
      total: 0.53
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.37
      fit: 0.37
    Dreamer's Idol:
      total: 0.61
      efficiency: 0.51
      win: 0.81
      pick: 0.25
      fit: 0.37
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
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
    Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom
    Orb, The World Stone, Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Ancient
    Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul
    Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss,
    Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.58
      pick: 0.37
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.58
      pick: 0.37
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.53
      pick: 0.37
      fit: 0.89
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Dreamer's Idol
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous
    Grimoire, Doom Orb, The World Stone, Chronos'' Pendant, The Cosmic Horror, Gem
    of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer
    of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.58
      pick: 0.37
      fit: 1.0
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.58
      pick: 0.37
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.53
      pick: 0.37
      fit: 0.89
    Dreamer's Idol:
      total: 0.67
      efficiency: 0.51
      win: 0.81
      pick: 0.25
      fit: 0.79
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  swaps:
  - added: Dreamer's Idol
    removed: Doom Orb
    reason: community 81% win over 48 matches (vs 56% on this god), taking the model's
      weakest slot from Doom Orb
  starter: *id001
---
