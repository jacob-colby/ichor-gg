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
    pick_rate: 0.35
    win_rate: 0.64
    alternates:
    - name: Book of Thoth
      pick_rate: 0.23
      win_rate: 0.5
    - name: Bancroft's Talon
      pick_rate: 0.18
      win_rate: 0.82
  - name: The World Stone
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.56
    - name: Soul Gem
      pick_rate: 0.11
      win_rate: 1.0
  - name: Rod of Tahuti
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.8
    - name: Gluttonous Grimoire
      pick_rate: 0.07
      win_rate: 0.25
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.63
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.38
      win_rate: 0.7
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 1.0
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.25
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.8
  - name: Void Shard
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.67
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.19
    win_rate: 0.33
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.73
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/zeus/
  last_verified: '2026-09-24'
  god_win_rate: 0.6451612903225806
  god_matches_won: 40
  god_matches_played: 62
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
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
    this god: Nimble Ring, Spear of the Magus, Doom Orb, Bracer of The Abyss, Dreamer''s
    Idol, Chronos'' Pendant, Blood-Bound Book, Ancient Signet, Gem of Focus, The Cosmic
    Horror, Typhon’s Heart, Rod of Asclepius, Polynomicon, Totem of Death, Soul Reaver,
    Jade Scepter, Divine Ruin, Helm of Radiance, Bragi''s Harp, Ethereal Staff, Wish-Granting
    Pearl, Gluttonous Grimoire.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.13
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.63
    The World Stone:
      total: 0.6
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.5
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.56
      pick: 0.23
      fit: 0.5
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 1.0
      pick: 0.15
      fit: 0.85
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Spear of Desolation
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Nimble
    Ring, Spear of the Magus, Bragi''s Harp, Doom Orb, Ancient Signet, Death Metal,
    Chronos'' Pendant, Bracer of The Abyss, Blood-Bound Book, Dreamer''s Idol, Gem
    of Focus, Polynomicon, Soul Reaver, Rod of Asclepius, The Cosmic Horror, Typhon’s
    Heart, Totem of Death, Jade Scepter, Divine Ruin, Triton''s Conch, Wish-Granting
    Pearl, Gluttonous Grimoire.'
  slot_scores:
    Bancroft's Talon:
      total: 0.61
      efficiency: 0.51
      win: 0.82
      pick: 0.18
      fit: 0.38
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.47
    Genji's Guard:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.19
    The World Stone:
      total: 0.59
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.44
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.56
      pick: 0.23
      fit: 0.44
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.46
  community_ordered:
  - Bancroft's Talon
  - Spear of Desolation
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  - Obsidian Shard
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Genji''s Guard, Nimble Ring, Spear of the Magus, Doom Orb, Bragi''s Harp,
    Chronos'' Pendant, Dreamer''s Idol, Bracer of The Abyss, Death Metal, Ancient
    Signet, Gem of Focus, Blood-Bound Book, The Cosmic Horror, Totem of Death, Rod
    of Asclepius, Typhon’s Heart, Polynomicon, Soul Reaver, Jade Scepter, Divine Ruin,
    Breastplate of Valor, Gluttonous Grimoire.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.17
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.58
    The World Stone:
      total: 0.59
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.56
      pick: 0.23
      fit: 0.42
    Soul Gem:
      total: 0.77
      efficiency: 0.57
      win: 1.0
      pick: 0.15
      fit: 0.77
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.52
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
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
  - Soul Gem
  flex_slots:
  - The World Stone
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
    this god: Genji''s Guard, Amanita Charm, Rod of Asclepius, Nimble Ring, Shield
    of the Phoenix, Kinetic Cuirass, Ethereal Staff, Blood-Bound Book, Freya''s Tears,
    Breastplate of Valor, Spear of the Magus, Lifebinder, Shifter''s Shield, Helm
    of Radiance, Yogi''s Necklace, Sphere of Negation, Phoenix Feather, Chandra''s
    Grace, Erosion, Eye of Providence, Jade Scepter, Wish-Granting Pearl, Draconic
    Scale, Gluttonous Grimoire.'
  slot_scores:
    Bancroft's Talon:
      total: 0.64
      efficiency: 0.51
      win: 0.82
      pick: 0.18
      fit: 0.54
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.5
      pick: 0.23
      fit: 0.16
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.12
      fit: 0.2
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.3
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.56
      pick: 0.23
      fit: 0.3
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 1.0
      pick: 0.15
      fit: 0.86
  community_ordered:
  - Bancroft's Talon
  - Book of Thoth
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
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
    for this god: Nimble Ring, Spear of the Magus, Doom Orb, Dreamer''s Idol, The
    Cosmic Horror, Bracer of The Abyss, Chronos'' Pendant, Blood-Bound Book, Ancient
    Signet, Gem of Focus, Rod of Asclepius, Typhon’s Heart, Polynomicon, Totem of
    Death, Soul Reaver, Jade Scepter, Divine Ruin, Screeching Gargoyle, Helm of Radiance,
    Ethereal Staff, Bragi''s Harp, Gluttonous Grimoire.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.1
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.71
    The World Stone:
      total: 0.62
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.6
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.56
      pick: 0.23
      fit: 0.6
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 1.0
      pick: 0.15
      fit: 0.9
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
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
  - Soul Gem
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
    this god: Nimble Ring, Spear of the Magus, Bragi''s Harp, Bracer of The Abyss,
    Doom Orb, Chronos'' Pendant, Ancient Signet, Blood-Bound Book, Dreamer''s Idol,
    Death Metal, Gem of Focus, Rod of Asclepius, The Cosmic Horror, Typhon’s Heart,
    Polynomicon, Soul Reaver, Totem of Death, Jade Scepter, Divine Ruin, Helm of Radiance,
    Daybreak Gavel, Gluttonous Grimoire.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.08
    Bracer of The Abyss:
      total: 0.53
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.59
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.56
      pick: 0.23
      fit: 0.32
    Bragi's Harp:
      total: 0.54
      efficiency: 0.44
      win: 0.64
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.15
      fit: 0.58
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Chronos' Pendant
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The World Stone
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Nimble Ring, Chronos''
    Pendant, Spear of the Magus, Gem of Focus, Bragi''s Harp, Doom Orb, Bracer of
    The Abyss, Totem of Death, Dreamer''s Idol, Ancient Signet, Blood-Bound Book,
    Breastplate of Valor, Death Metal, The Cosmic Horror, Rod of Asclepius, Typhon’s
    Heart, Polynomicon, Staff of Myrddin, Eye of Erebus, Soul Reaver, Gluttonous Grimoire.'
  slot_scores:
    Genji's Guard:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.12
      fit: 0.35
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.55
      win: 0.64
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.63
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.27
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.56
      pick: 0.23
      fit: 0.27
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 1.0
      pick: 0.15
      fit: 0.82
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
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
      total: 0.61
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.63
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.56
      pick: 0.23
      fit: 0.5
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.64
      pick: 0.0
      fit: 0.5
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.6
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
