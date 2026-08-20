---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.56
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.47
    win_rate: 0.47
    alternates:
    - name: Book of Thoth
      pick_rate: 0.22
      win_rate: 0.56
    - name: Yogi's Necklace
      pick_rate: 0.09
      win_rate: 0.6
  - name: Book of Thoth
    pick_rate: 0.24
    win_rate: 0.46
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.25
      win_rate: 0.54
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.49
  - name: Polynomicon
    pick_rate: 0.25
    win_rate: 0.49
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.5
    - name: Soul Gem
      pick_rate: 0.12
      win_rate: 0.53
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.46
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.51
    - name: Polynomicon
      pick_rate: 0.08
      win_rate: 0.68
  - name: Obsidian Shard
    pick_rate: 0.27
    win_rate: 0.48
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.63
    - name: Evil Eye
      pick_rate: 0.09
      win_rate: 0.46
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.46
    alternates:
    - name: Killing Stone
      pick_rate: 0.08
      win_rate: 0.41
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.65
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.43
    win_rate: 0.55
  - name: Conduit Gem
    pick_rate: 0.33
    win_rate: 0.44
  - name: Pendulum of the Ages
    pick_rate: 0.09
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-08-20'
  god_win_rate: 0.49612403100775193
  god_matches_won: 320
  god_matches_played: 645
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-20'
  god_matches_analyzed: 11556
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
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
    this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Nimble Ring,
    Doom Orb, Chronos'' Pendant, The World Stone, Totem of Death, Genji''s Guard,
    Dreamer''s Idol, Gem of Focus, Death Metal, Helm of Radiance, Ethereal Staff,
    Blood-Bound Book, Rod of Asclepius, Breastplate of Valor, Bancroft''s Talon, Jade
    Scepter, Bracer of The Abyss, Alchemist Coat, Freya''s Tears, Soul Reaver.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.47
      pick: 0.47
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.53
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.46
      pick: 0.55
      fit: 0.79
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.48
      pick: 0.58
      fit: 0.89
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.53
      pick: 0.19
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Yogi's Necklace
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Yogi's Necklace
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Nimble Ring, Death Metal, Genji''s Guard, The Cosmic Horror, Spear of
    the Magus, Doom Orb, Breastplate of Valor, Chronos'' Pendant, Bragi''s Harp, The
    World Stone, Totem of Death, Bancroft''s Talon, Triton''s Conch, Helm of Radiance,
    Ethereal Staff, Gem of Focus, Blood-Bound Book, Rod of Asclepius, Oni Hunter''s
    Garb, Jade Scepter, Freya''s Tears, Soul Reaver.'
  slot_scores:
    Yogi's Necklace:
      total: 0.49
      efficiency: 0.57
      win: 0.6
      pick: 0.09
      fit: 0.1
    Book of Thoth:
      total: 0.45
      efficiency: 0.49
      win: 0.46
      pick: 0.33
      fit: 0.39
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.47
      pick: 0.0
      fit: 0.24
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.47
      pick: 0.47
      fit: 0.61
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.46
      pick: 0.55
      fit: 0.57
    Obsidian Shard:
      total: 0.51
      efficiency: 0.52
      win: 0.48
      pick: 0.58
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
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
    god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Genji''s Guard,
    Nimble Ring, Death Metal, Doom Orb, Chronos'' Pendant, Breastplate of Valor, Totem
    of Death, The World Stone, Freya''s Tears, Gem of Focus, Dreamer''s Idol, Shield
    of the Phoenix, Bragi''s Harp, Helm of Radiance, Ethereal Staff, Blood-Bound Book,
    Rod of Asclepius, Kinetic Cuirass, Amanita Charm, Screeching Gargoyle, Triton''s
    Conch, Bancroft''s Talon.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.47
      pick: 0.47
      fit: 0.78
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.5
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.46
      pick: 0.55
      fit: 0.56
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.48
      pick: 0.58
      fit: 0.66
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.53
      pick: 0.19
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Amanita Charm, Yogi''s Necklace, Gluttonous Grimoire, Shield of the
    Phoenix, Ethereal Staff, Kinetic Cuirass, Rod of Asclepius, Genji''s Guard, Chandra''s
    Grace, Nimble Ring, Blood-Bound Book, Freya''s Tears, Oni Hunter''s Garb, Lifebinder,
    The Cosmic Horror, Bancroft''s Talon, Breastplate of Valor, Spear of the Magus,
    Phoenix Feather, Erosion, Shifter''s Shield, Spectral Armor, Eye of Providence,
    Draconic Scale, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.47
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.46
      pick: 0.55
      fit: 0.39
    Obsidian Shard:
      total: 0.5
      efficiency: 0.52
      win: 0.48
      pick: 0.58
      fit: 0.49
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.53
      pick: 0.19
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Doom
    Orb, The World Stone, Nimble Ring, Dreamer''s Idol, Genji''s Guard, Chronos''
    Pendant, Screeching Gargoyle, Totem of Death, Breastplate of Valor, Death Metal,
    Helm of Radiance, Ethereal Staff, Gem of Focus, Blood-Bound Book, Rod of Asclepius,
    Bancroft''s Talon, Jade Scepter, Freya''s Tears, Stone of Binding, Bracer of The
    Abyss, Kinetic Cuirass, Void Shield.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.47
      pick: 0.47
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.54
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.46
      pick: 0.55
      fit: 0.85
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.48
      pick: 0.58
      fit: 0.95
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.53
      pick: 0.19
      fit: 1.0
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Genji''s Guard, The Cosmic Horror,
    Spear of the Magus, Bragi''s Harp, Death Metal, Bracer of The Abyss, Breastplate
    of Valor, Chronos'' Pendant, Blood-Bound Book, Bancroft''s Talon, Doom Orb, Kinetic
    Cuirass, Amanita Charm, Helm of Radiance, Totem of Death, Ethereal Staff, Freya''s
    Tears, Rod of Asclepius, Eye of Providence, Oni Hunter''s Garb, Shield of the
    Phoenix, Jade Scepter, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.45
      efficiency: 0.42
      win: 0.47
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.46
      pick: 0.55
      fit: 0.32
    Obsidian Shard:
      total: 0.49
      efficiency: 0.52
      win: 0.48
      pick: 0.58
      fit: 0.42
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.19
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Gluttonous Grimoire, Chronos'' Pendant, Freya''s Tears, Totem of Death, Shield
    of the Phoenix, Gem of Focus, Nimble Ring, The Cosmic Horror, Screeching Gargoyle,
    Chandra''s Grace, Spear of the Magus, Death Metal, Gladiator''s Shield, Doom Orb,
    Kinetic Cuirass, Prophetic Cloak, Amanita Charm, The World Stone, Helm of Radiance,
    Eye of Providence, Ethereal Staff, Oni Hunter''s Garb, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.47
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.64
      win: 0.47
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.5
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.47
      pick: 0.47
      fit: 0.86
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.46
      pick: 0.55
      fit: 0.37
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.53
      pick: 0.19
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Obsidian Shard
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
    Underrated for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the
    Magus, Nimble Ring, Chronos'' Pendant, Doom Orb, The World Stone, Totem of Death,
    Genji''s Guard, Dreamer''s Idol, Gem of Focus, Death Metal, Helm of Radiance,
    Ethereal Staff, Blood-Bound Book, Rod of Asclepius, Breastplate of Valor, Bancroft''s
    Talon, Jade Scepter, Bracer of The Abyss, Alchemist Coat, Freya''s Tears, Soul
    Reaver.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.47
      pick: 0.47
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.53
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.46
      pick: 0.55
      fit: 0.79
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.48
      pick: 0.58
      fit: 0.89
  starter: *id001
---
