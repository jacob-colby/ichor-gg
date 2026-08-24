---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.52
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.34
    win_rate: 0.56
    alternates:
    - name: Book of Thoth
      pick_rate: 0.33
      win_rate: 0.56
    - name: Doom Orb
      pick_rate: 0.06
      win_rate: 0.56
  - name: The World Stone
    pick_rate: 0.15
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.56
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.56
  - name: Rod of Tahuti
    pick_rate: 0.2
    win_rate: 0.57
    alternates:
    - name: Soul Gem
      pick_rate: 0.14
      win_rate: 0.63
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.54
  - name: Obsidian Shard
    pick_rate: 0.29
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.25
      win_rate: 0.63
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.5
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.43
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.65
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.6
  - name: Shrapnel Mod
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Thermal Mod
      pick_rate: 0.11
      win_rate: 0.52
    - name: Surplus Mod
      pick_rate: 0.09
      win_rate: 0.53
  - name: Surplus Mod
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.33
      win_rate: 0.56
    - name: Thermal Mod
      pick_rate: 0.24
      win_rate: 0.57
  - name: Seismic Mod
    pick_rate: 0.14
    win_rate: 0.52
    alternates:
    - name: Surplus Mod
      pick_rate: 0.7
      win_rate: 0.57
    - name: Thermal Mod
      pick_rate: 0.11
      win_rate: 0.58
  - name: Masterwork Mod
    pick_rate: 0.04
    win_rate: 0.0
    alternates:
    - name: Seismic Mod
      pick_rate: 0.56
      win_rate: 0.46
    - name: Surplus Mod
      pick_rate: 0.4
      win_rate: 0.65
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.3
    win_rate: 0.6
  - name: Archmage's Gem
    pick_rate: 0.22
    win_rate: 0.62
  - name: Sands Of Time
    pick_rate: 0.21
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-08-24'
  god_win_rate: 0.5447839831401475
  god_matches_won: 517
  god_matches_played: 949
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-24'
  god_matches_analyzed: 17273
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble Ring, Dreamer''s
    Idol, Chronos'' Pendant, Bracer of The Abyss, The Cosmic Horror, Gem of Focus,
    Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book,
    Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Wish-Granting Pearl, Soul Reaver, Typhon’s Heart, Bragi''s Harp.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.56
      pick: 0.33
      fit: 0.35
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.56
      pick: 0.34
      fit: 0.83
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.57
      pick: 0.31
      fit: 0.66
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.58
      pick: 0.48
      fit: 0.76
    Soul Gem:
      total: 0.62
      efficiency: 0.52
      win: 0.63
      pick: 0.22
      fit: 0.93
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, Doom Orb, Bragi''s Harp, Nimble Ring, Death Metal, Gluttonous Grimoire,
    Ancient Signet, Chronos'' Pendant, Dreamer''s Idol, Bracer of The Abyss, Gem of
    Focus, Polynomicon, The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem
    of Death, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting
    Pearl, Soul Reaver, Breastplate of Valor.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.56
      pick: 0.34
      fit: 0.56
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.06
      fit: 0.52
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.2
      fit: 0.52
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.57
      pick: 0.31
      fit: 0.52
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.58
      pick: 0.48
      fit: 0.53
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.63
      pick: 0.22
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
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
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble Ring, Dreamer''s
    Idol, Chronos'' Pendant, Bragi''s Harp, Death Metal, Gem of Focus, Ancient Signet,
    The Cosmic Horror, Bracer of The Abyss, Totem of Death, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Breastplate of Valor, Triton''s Conch,
    Bancroft''s Talon, Genji''s Guard, Soul Reaver.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.56
      pick: 0.33
      fit: 0.2
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.56
      pick: 0.34
      fit: 0.7
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.57
      pick: 0.31
      fit: 0.5
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.58
      pick: 0.48
      fit: 0.6
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.63
      pick: 0.22
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
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
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Genji''s Guard, Spear of the
    Magus, Breastplate of Valor, Shifter''s Shield, Lifebinder, Helm of Radiance,
    Yogi''s Necklace, Sphere of Negation, Nimble Ring, Erosion, Eye of Providence,
    Phoenix Feather, Chandra''s Grace, Draconic Scale, Jade Scepter, Blood-Bound Book,
    Wish-Granting Pearl, Doom Orb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.34
      fit: 0.45
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.31
      fit: 0.36
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.48
      fit: 0.46
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.63
      pick: 0.22
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    The Cosmic Horror, Nimble Ring, Chronos'' Pendant, Ancient Signet, Bracer of The
    Abyss, Gem of Focus, Rod of Asclepius, Polynomicon, Totem of Death, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Screeching
    Gargoyle, Ethereal Staff, Wish-Granting Pearl, Soul Reaver, Typhon’s Heart.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.56
      pick: 0.34
      fit: 0.88
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.56
      pick: 0.06
      fit: 0.75
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.57
      pick: 0.31
      fit: 0.75
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.58
      pick: 0.48
      fit: 0.85
    Soul Gem:
      total: 0.62
      efficiency: 0.52
      win: 0.63
      pick: 0.22
      fit: 0.98
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
    Book, Dreamer''s Idol, Death Metal, Bancroft''s Talon, Gem of Focus, Rod of Asclepius,
    The Cosmic Horror, Typhon’s Heart, Polynomicon, Totem of Death, Jade Scepter,
    Divine Ruin, Helm of Radiance, Daybreak Gavel, Soul Reaver.'
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
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.31
      fit: 0.32
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.48
      fit: 0.42
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.63
      pick: 0.22
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
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Spear of the Magus,
    Gem of Focus, Nimble Ring, Gluttonous Grimoire, Totem of Death, Doom Orb, Breastplate
    of Valor, Dreamer''s Idol, Bragi''s Harp, Genji''s Guard, Ancient Signet, Death
    Metal, Bracer of The Abyss, The Cosmic Horror, Staff of Myrddin, Rod of Asclepius,
    Eye of Erebus, Polynomicon, Screeching Gargoyle, Chandra''s Grace, Freya''s Tears,
    Blood-Bound Book.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.56
      pick: 0.34
      fit: 0.76
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.33
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.31
      fit: 0.33
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.48
      fit: 0.43
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.63
      pick: 0.22
      fit: 0.86
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
      total: 0.54
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.56
      pick: 0.34
      fit: 0.83
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.56
      pick: 0.06
      fit: 0.66
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.57
      pick: 0.31
      fit: 0.66
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.58
      pick: 0.48
      fit: 0.76
  starter: *id001
---
