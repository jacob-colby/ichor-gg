---
type: smite-build
god: Anubis
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Bancroft's Talon
    pick_rate: 0.57
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.3
    - name: Blood-Bound Book
      pick_rate: 0.08
      win_rate: 0.56
  - name: Typhon’s Heart
    pick_rate: 0.25
    win_rate: 0.57
    alternates:
    - name: Blood-Bound Book
      pick_rate: 0.21
      win_rate: 0.58
    - name: Bancroft's Talon
      pick_rate: 0.12
      win_rate: 0.38
  - name: Rod of Tahuti
    pick_rate: 0.29
    win_rate: 0.63
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.2
      win_rate: 0.5
    - name: Soul Gem
      pick_rate: 0.11
      win_rate: 0.33
  - name: Soul Gem
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.26
      win_rate: 0.36
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Doom Orb
    pick_rate: 0.19
    win_rate: 0.58
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.17
      win_rate: 0.59
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.54
  - name: Dreamer's Idol
    pick_rate: 0.18
    win_rate: 0.64
    alternates:
    - name: Killing Stone
      pick_rate: 0.13
      win_rate: 0.5
    - name: Divine Ruin
      pick_rate: 0.11
      win_rate: 0.43
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.32
    win_rate: 0.61
  - name: Conduit Gem
    pick_rate: 0.25
    win_rate: 0.39
  - name: Pendulum of the Ages
    pick_rate: 0.15
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/anubis/
  last_verified: '2026-09-12'
  god_win_rate: 0.504424778761062
  god_matches_won: 57
  god_matches_played: 113
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-12'
  god_matches_analyzed: 4284
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Doom Orb
  - Spear of the Magus
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
    this god: Spear of the Magus, Gluttonous Grimoire, The World Stone, Chronos''
    Pendant, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod
    of Asclepius, Book of Thoth, Polynomicon, Soul Reaver, Jade Scepter, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Bracer of The Abyss, Nimble
    Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.31
      fit: 1.0
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.79
    Doom Orb:
      total: 0.59
      efficiency: 0.53
      win: 0.58
      pick: 0.41
      fit: 0.79
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.63
      pick: 0.45
      fit: 0.79
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 1.0
    Dreamer's Idol:
      total: 0.61
      efficiency: 0.51
      win: 0.64
      pick: 0.55
      fit: 0.79
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - The World Stone
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - The World Stone
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, The World Stone, Death Metal, Gluttonous Grimoire, Ancient Signet,
    Chronos'' Pendant, Bragi''s Harp, Gem of Focus, Book of Thoth, Polynomicon, Soul
    Reaver, The Cosmic Horror, Rod of Asclepius, Totem of Death, Triton''s Conch,
    Jade Scepter, Wish-Granting Pearl, Helm of Radiance, Breastplate of Valor, Ethereal
    Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.39
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.57
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.41
      fit: 0.57
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.63
      pick: 0.45
      fit: 0.57
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.71
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.51
      win: 0.64
      pick: 0.55
      fit: 0.47
  community_ordered:
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Doom Orb
  - Spear of the Magus
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
    god: Spear of the Magus, Gluttonous Grimoire, The World Stone, Chronos'' Pendant,
    Death Metal, Gem of Focus, The Cosmic Horror, Ancient Signet, Bragi''s Harp, Totem
    of Death, Rod of Asclepius, Book of Thoth, Polynomicon, Soul Reaver, Jade Scepter,
    Triton''s Conch, Breastplate of Valor, Genji''s Guard, Helm of Radiance, Ethereal
    Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.31
      fit: 0.78
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.56
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.41
      fit: 0.56
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.63
      pick: 0.45
      fit: 0.56
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.88
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.51
      win: 0.64
      pick: 0.55
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Soul Gem
  - Amanita Charm
  - Dreamer's Idol
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus, Shifter''s
    Shield, Genji''s Guard, Breastplate of Valor, Lifebinder, Helm of Radiance, Sphere
    of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale, Phoenix
    Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.63
      pick: 0.45
      fit: 0.39
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.89
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.81
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.51
      win: 0.64
      pick: 0.55
      fit: 0.39
  community_ordered:
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Spear of the Magus
  - Spear of Desolation
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
    for this god: Spear of the Magus, Gluttonous Grimoire, The World Stone, The Cosmic
    Horror, Chronos'' Pendant, Ancient Signet, Gem of Focus, Rod of Asclepius, Book
    of Thoth, Totem of Death, Polynomicon, Soul Reaver, Jade Scepter, Helm of Radiance,
    Ethereal Staff, Screeching Gargoyle, Wish-Granting Pearl, Breastplate of Valor,
    Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.31
      fit: 1.0
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.85
    Doom Orb:
      total: 0.59
      efficiency: 0.53
      win: 0.58
      pick: 0.41
      fit: 0.85
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.63
      pick: 0.45
      fit: 0.85
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 1.0
    Dreamer's Idol:
      total: 0.62
      efficiency: 0.51
      win: 0.64
      pick: 0.55
      fit: 0.85
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Chronos'' Pendant, The World Stone, Ancient Signet, Death
    Metal, Gem of Focus, Rod of Asclepius, The Cosmic Horror, Book of Thoth, Polynomicon,
    Soul Reaver, Totem of Death, Jade Scepter, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.63
      pick: 0.45
      fit: 0.32
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.56
      pick: 0.28
      fit: 0.58
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.51
      win: 0.64
      pick: 0.55
      fit: 0.32
  community_ordered:
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Gem of Focus
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Spear
    of the Magus, Gluttonous Grimoire, Totem of Death, The World Stone, Breastplate
    of Valor, Genji''s Guard, Ancient Signet, Death Metal, Staff of Myrddin, The Cosmic
    Horror, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Book
    of Thoth, Chandra''s Grace, Freya''s Tears, Polynomicon, Soul Reaver, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.63
    Gem of Focus:
      total: 0.52
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.31
      fit: 0.86
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.63
      pick: 0.45
      fit: 0.37
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.96
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.51
      win: 0.64
      pick: 0.55
      fit: 0.37
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Doom Orb
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, The World Stone,
    Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death,
    Rod of Asclepius, Book of Thoth, Polynomicon, Soul Reaver, Jade Scepter, Helm
    of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Bracer of
    The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.31
      fit: 1.0
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.79
    Doom Orb:
      total: 0.59
      efficiency: 0.53
      win: 0.58
      pick: 0.41
      fit: 0.79
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.63
      pick: 0.45
      fit: 0.79
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.5
      pick: 0.15
      fit: 0.89
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
---
