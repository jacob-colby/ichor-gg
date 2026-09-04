---
type: smite-build
god: Janus
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.39
    win_rate: 0.51
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.38
      win_rate: 0.49
    - name: Chronos' Pendant
      pick_rate: 0.09
      win_rate: 0.51
  - name: Spear of Desolation
    pick_rate: 0.33
    win_rate: 0.5
    alternates:
    - name: Book of Thoth
      pick_rate: 0.23
      win_rate: 0.52
    - name: The World Stone
      pick_rate: 0.1
      win_rate: 0.51
  - name: Soul Gem
    pick_rate: 0.37
    win_rate: 0.54
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.17
      win_rate: 0.51
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.41
    win_rate: 0.54
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.2
      win_rate: 0.46
    - name: Soul Gem
      pick_rate: 0.12
      win_rate: 0.46
  - name: Obsidian Shard
    pick_rate: 0.29
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.22
      win_rate: 0.51
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.39
  - name: Dreamer's Idol
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.59
    - name: Evil Eye
      pick_rate: 0.11
      win_rate: 0.35
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.5
    win_rate: 0.57
  - name: Conduit Gem
    pick_rate: 0.28
    win_rate: 0.4
  - name: Pendulum of the Ages
    pick_rate: 0.15
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/janus/
  last_verified: '2026-09-04'
  god_win_rate: 0.5018281535648994
  god_matches_won: 549
  god_matches_played: 1094
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-04'
  god_matches_analyzed: 11911
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Dreamer's Idol
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
    this god: Spear of the Magus, Gluttonous Grimoire, The World Stone, Doom Orb,
    Chronos'' Pendant, Gem of Focus, The Cosmic Horror, Ancient Signet, Totem of Death,
    Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.51
      pick: 0.39
      fit: 0.44
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.5
      pick: 0.45
      fit: 1.0
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.58
      fit: 1.0
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.54
      pick: 0.68
      fit: 0.78
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.53
      pick: 0.63
      fit: 0.88
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.51
      win: 0.6
      pick: 0.37
      fit: 0.78
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, The World Stone, Doom Orb, Death Metal, Gluttonous Grimoire, Chronos''
    Pendant, Ancient Signet, Bragi''s Harp, Gem of Focus, Polynomicon, Soul Reaver,
    The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s
    Conch, Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm
    of Radiance, Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.45
      fit: 0.61
    Doom Orb:
      total: 0.5
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.57
    The World Stone:
      total: 0.5
      efficiency: 0.52
      win: 0.51
      pick: 0.14
      fit: 0.57
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.54
      pick: 0.58
      fit: 0.71
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.54
      pick: 0.68
      fit: 0.57
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.53
      pick: 0.63
      fit: 0.57
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Dreamer's Idol
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
    god: Spear of the Magus, Gluttonous Grimoire, The World Stone, Doom Orb, Chronos''
    Pendant, Death Metal, Gem of Focus, The Cosmic Horror, Ancient Signet, Bragi''s
    Harp, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver,
    Jade Scepter, Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s
    Talon, Genji''s Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.51
      pick: 0.39
      fit: 0.22
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.45
      fit: 0.78
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.54
      pick: 0.58
      fit: 0.88
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.54
      pick: 0.68
      fit: 0.56
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.53
      pick: 0.63
      fit: 0.66
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.37
      fit: 0.56
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Dreamer's Idol
  - Amanita Charm
  - Obsidian Shard
  flex_slots:
  - Dreamer's Idol
  - Spear of Desolation
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Shifter''s Shield, Genji''s Guard,
    Breastplate of Valor, Lifebinder, Spear of the Magus, Helm of Radiance, Sphere
    of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale, Phoenix
    Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound Book,
    Glorious Pridwen, Stone of Binding.'
  slot_scores:
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.45
      fit: 0.48
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.54
      pick: 0.58
      fit: 0.88
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.54
      pick: 0.68
      fit: 0.37
    Dreamer's Idol:
      total: 0.52
      efficiency: 0.51
      win: 0.6
      pick: 0.37
      fit: 0.37
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.82
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.63
      fit: 0.47
  community_ordered:
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Dreamer's Idol
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The World Stone
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Dreamer's Idol
  - The World Stone
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
    for this god: Spear of the Magus, Gluttonous Grimoire, The World Stone, Doom Orb,
    The Cosmic Horror, Chronos'' Pendant, Ancient Signet, Gem of Focus, Rod of Asclepius,
    Totem of Death, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle,
    Wish-Granting Pearl, Typhon’s Heart, Breastplate of Valor, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.5
      pick: 0.45
      fit: 1.0
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.51
      pick: 0.14
      fit: 0.85
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.58
      fit: 1.0
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.54
      pick: 0.68
      fit: 0.85
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.53
      pick: 0.63
      fit: 0.95
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.51
      win: 0.6
      pick: 0.37
      fit: 0.85
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Soul Gem
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
    Bracer of The Abyss, Chronos'' Pendant, The World Stone, Doom Orb, Ancient Signet,
    Blood-Bound Book, Death Metal, Bancroft''s Talon, Gem of Focus, Rod of Asclepius,
    Typhon’s Heart, The Cosmic Horror, Polynomicon, Soul Reaver, Totem of Death, Jade
    Scepter, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.41
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.49
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.51
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.58
      fit: 0.57
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.54
      pick: 0.68
      fit: 0.3
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.53
      pick: 0.63
      fit: 0.4
  community_ordered:
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Chronos' Pendant
  - Dreamer's Idol
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Spear
    of the Magus, Totem of Death, Gluttonous Grimoire, The World Stone, Breastplate
    of Valor, Doom Orb, Genji''s Guard, Death Metal, Ancient Signet, Staff of Myrddin,
    The Cosmic Horror, Eye of Erebus, Screeching Gargoyle, Chandra''s Grace, Bragi''s
    Harp, Freya''s Tears, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver,
    Shield of the Phoenix.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.51
      pick: 0.09
      fit: 0.65
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.45
      fit: 0.85
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.58
      fit: 0.95
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.54
      pick: 0.68
      fit: 0.35
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.63
      fit: 0.45
    Dreamer's Idol:
      total: 0.52
      efficiency: 0.51
      win: 0.6
      pick: 0.37
      fit: 0.35
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Soul Gem
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, The
    World Stone, Chronos'' Pendant, Gem of Focus, The Cosmic Horror, Ancient Signet,
    Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver,
    Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble
    Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.5
      pick: 0.45
      fit: 1.0
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.78
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.51
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.58
      fit: 1.0
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.54
      pick: 0.68
      fit: 0.78
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.53
      pick: 0.63
      fit: 0.88
  community_ordered:
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
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
    + fit + win/pick). Underrated for this god: Spear of the Magus, Gluttonous Grimoire,
    Doom Orb, The World Stone, Chronos'' Pendant, Gem of Focus, The Cosmic Horror,
    Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book,
    Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss,
    Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.5
      pick: 0.45
      fit: 1.0
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.51
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.58
      fit: 1.0
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.54
      pick: 0.68
      fit: 0.78
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.53
      pick: 0.63
      fit: 0.88
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.51
      win: 0.6
      pick: 0.37
      fit: 0.78
  community_ordered:
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  swaps:
  - added: Dreamer's Idol
    removed: Doom Orb
    reason: community 60% win over 131 matches (vs 50% on this god), taking the model's
      weakest slot from Doom Orb
  starter: *id001
---
