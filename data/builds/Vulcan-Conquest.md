---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.34
    win_rate: 0.53
    alternates:
    - name: Book of Thoth
      pick_rate: 0.31
      win_rate: 0.62
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.67
  - name: The World Stone
    pick_rate: 0.18
    win_rate: 0.48
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.58
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.5
  - name: Soul Gem
    pick_rate: 0.16
    win_rate: 0.48
    alternates:
    - name: The World Stone
      pick_rate: 0.18
      win_rate: 0.61
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.64
  - name: Rod of Tahuti
    pick_rate: 0.3
    win_rate: 0.64
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.61
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.17
      win_rate: 0.48
    - name: Evil Eye
      pick_rate: 0.12
      win_rate: 0.37
  - name: Shrapnel Mod
    pick_rate: 0.18
    win_rate: 0.75
    alternates:
    - name: Surplus Mod
      pick_rate: 0.11
      win_rate: 0.65
    - name: Thermal Mod
      pick_rate: 0.09
      win_rate: 0.6
  - name: Surplus Mod
    pick_rate: 0.27
    win_rate: 0.67
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.35
      win_rate: 0.63
    - name: Thermal Mod
      pick_rate: 0.23
      win_rate: 0.47
  - name: Seismic Mod
    pick_rate: 0.1
    win_rate: 0.33
    alternates:
    - name: Surplus Mod
      pick_rate: 0.69
      win_rate: 0.59
    - name: Thermal Mod
      pick_rate: 0.1
      win_rate: 0.67
  community_starters:
  - name: Sands Of Time
    pick_rate: 0.28
    win_rate: 0.58
  - name: Archmage's Gem
    pick_rate: 0.24
    win_rate: 0.62
  - name: Pendulum of the Ages
    pick_rate: 0.24
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-09-11'
  god_win_rate: 0.5780346820809249
  god_matches_won: 100
  god_matches_played: 173
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Doom Orb, Spear of the Magus, Gluttonous Grimoire, Nimble Ring, Dreamer''s
    Idol, Chronos'' Pendant, Bracer of The Abyss, The Cosmic Horror, Gem of Focus,
    Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book,
    Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Wish-Granting Pearl, Typhon’s Heart, Bragi''s Harp.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.62
      pick: 0.31
      fit: 0.35
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.83
    Nimble Ring:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.51
    Doom Orb:
      total: 0.59
      efficiency: 0.53
      win: 0.67
      pick: 0.09
      fit: 0.66
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.64
      pick: 0.5
      fit: 0.66
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.58
      pick: 0.32
      fit: 0.76
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Doom Orb
  - Spear of the Magus
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Doom
    Orb, Spear of the Magus, Bragi''s Harp, Nimble Ring, Death Metal, Gluttonous Grimoire,
    Ancient Signet, Chronos'' Pendant, Dreamer''s Idol, Bracer of The Abyss, Gem of
    Focus, Polynomicon, Soul Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s
    Talon, Totem of Death, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine
    Ruin, Wish-Granting Pearl, Breastplate of Valor.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.62
      pick: 0.31
      fit: 0.35
    Nimble Ring:
      total: 0.53
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.35
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.09
      fit: 0.52
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.64
      pick: 0.5
      fit: 0.52
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.58
      pick: 0.32
      fit: 0.53
  community_ordered:
  - Book of Thoth
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Doom Orb, Spear of the Magus, Gluttonous Grimoire, Nimble Ring, Dreamer''s
    Idol, Chronos'' Pendant, Bragi''s Harp, Death Metal, Gem of Focus, Ancient Signet,
    The Cosmic Horror, Bracer of The Abyss, Totem of Death, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Breastplate of Valor,
    Triton''s Conch, Bancroft''s Talon, Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.62
      pick: 0.31
      fit: 0.2
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.7
    Nimble Ring:
      total: 0.52
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.3
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.09
      fit: 0.5
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.64
      pick: 0.5
      fit: 0.5
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.58
      pick: 0.32
      fit: 0.6
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Kinetic Cuirass
  - Doom Orb
  - Rod of Tahuti
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Doom Orb
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Doom Orb, Ethereal Staff, Freya''s Tears, Genji''s Guard, Spear
    of the Magus, Breastplate of Valor, Shifter''s Shield, Lifebinder, Helm of Radiance,
    Yogi''s Necklace, Sphere of Negation, Nimble Ring, Erosion, Eye of Providence,
    Phoenix Feather, Chandra''s Grace, Draconic Scale, Jade Scepter, Blood-Bound Book,
    Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.62
      pick: 0.31
      fit: 0.19
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.56
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.09
      fit: 0.36
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.64
      pick: 0.5
      fit: 0.36
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.76
    Rod of Asclepius:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Book of Thoth
  - Doom Orb
  - Rod of Tahuti
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
  - Spear of Desolation
  - Nimble Ring
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
    for this god: Doom Orb, Spear of the Magus, Gluttonous Grimoire, Dreamer''s Idol,
    The Cosmic Horror, Nimble Ring, Chronos'' Pendant, Ancient Signet, Bracer of The
    Abyss, Gem of Focus, Rod of Asclepius, Polynomicon, Totem of Death, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Screeching Gargoyle, Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart.'
  slot_scores:
    Nimble Ring:
      total: 0.53
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.38
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.88
    Doom Orb:
      total: 0.6
      efficiency: 0.53
      win: 0.67
      pick: 0.09
      fit: 0.75
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.64
      pick: 0.5
      fit: 0.75
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.58
      pick: 0.32
      fit: 0.85
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Doom Orb
  flex_slots:
  - Bracer of The Abyss
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Doom Orb, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Chronos'' Pendant, Ancient Signet, Blood-Bound Book,
    Dreamer''s Idol, Death Metal, Bancroft''s Talon, Gem of Focus, Rod of Asclepius,
    The Cosmic Horror, Typhon’s Heart, Polynomicon, Soul Reaver, Totem of Death, Jade
    Scepter, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.62
      pick: 0.31
      fit: 0.17
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.59
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.64
      pick: 0.5
      fit: 0.32
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.09
      fit: 0.32
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Doom Orb
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Doom Orb
  - Rod of Tahuti
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Doom Orb, Spear
    of the Magus, Gem of Focus, Nimble Ring, Gluttonous Grimoire, Totem of Death,
    Breastplate of Valor, Dreamer''s Idol, Bragi''s Harp, Genji''s Guard, Ancient
    Signet, Death Metal, Bracer of The Abyss, The Cosmic Horror, Staff of Myrddin,
    Rod of Asclepius, Eye of Erebus, Polynomicon, Screeching Gargoyle, Chandra''s
    Grace, Freya''s Tears, Blood-Bound Book.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.62
      pick: 0.31
      fit: 0.13
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.76
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.56
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.09
      fit: 0.33
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.64
      pick: 0.5
      fit: 0.33
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.48
      pick: 0.25
      fit: 0.86
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
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
  - Nimble Ring
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Nimble Ring,
    Doom Orb, Dreamer''s Idol, Chronos'' Pendant, Bracer of The Abyss, The Cosmic
    Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm
    of Radiance, Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Bragi''s Harp.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.83
    Doom Orb:
      total: 0.59
      efficiency: 0.53
      win: 0.67
      pick: 0.09
      fit: 0.66
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.64
      pick: 0.5
      fit: 0.66
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.58
      pick: 0.32
      fit: 0.76
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
