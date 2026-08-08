---
type: smite-build
god: Hecate
mode: Conquest
builds:
- source: community
  aspect: Aspect of Ruin
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.48
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.57
    win_rate: 0.63
    alternates:
    - name: Book of Thoth
      pick_rate: 0.19
      win_rate: 0.49
    - name: Doom Orb
      pick_rate: 0.07
      win_rate: 0.54
  - name: Book of Thoth
    pick_rate: 0.22
    win_rate: 0.61
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.2
      win_rate: 0.51
    - name: The World Stone
      pick_rate: 0.16
      win_rate: 0.66
  - name: Soul Gem
    pick_rate: 0.3
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.54
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.57
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.64
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.24
      win_rate: 0.55
    - name: Soul Gem
      pick_rate: 0.06
      win_rate: 0.55
  - name: Obsidian Shard
    pick_rate: 0.26
    win_rate: 0.63
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.72
    - name: Evil Eye
      pick_rate: 0.11
      win_rate: 0.51
  - name: Evil Eye
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.78
    - name: Soul Reaver
      pick_rate: 0.07
      win_rate: 0.76
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.29
    win_rate: 0.62
  - name: Conduit Gem
    pick_rate: 0.23
    win_rate: 0.54
  - name: Pendulum of The Ages
    pick_rate: 0.18
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/hecate/
  last_verified: '2026-08-08'
  god_win_rate: 0.5642458100558659
  god_matches_won: 303
  god_matches_played: 537
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-08'
  god_matches_analyzed: 14443
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - The World Stone
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Reaver
  - Rod of Tahuti
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
    this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Doom Orb,
    Chronos'' Pendant, Dreamer''s Idol, Genji''s Guard, Gem of Focus, Death Metal,
    Rod of Asclepius, Blood-Bound Book, Helm of Radiance, Breastplate of Valor, Bancroft''s
    Talon, Jade Scepter, Bracer of The Abyss, Wish-Granting Pearl, Polynomicon, Ethereal
    Staff, Ancient Signet, Alchemist Coat, Freya''s Tears.'
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.52
      win: 0.63
      pick: 0.57
      fit: 1.0
    The World Stone:
      total: 0.59
      efficiency: 0.49
      win: 0.66
      pick: 0.16
      fit: 0.77
    Soul Reaver:
      total: 0.58
      efficiency: 0.46
      win: 0.76
      pick: 0.07
      fit: 0.51
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.44
      win: 0.64
      pick: 0.33
      fit: 0.77
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.63
      pick: 0.26
      fit: 0.77
    Soul Gem:
      total: 0.66
      efficiency: 0.59
      win: 0.64
      pick: 0.3
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The World Stone
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Reaver
  - Rod of Tahuti
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
    god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Genji''s Guard,
    Death Metal, Doom Orb, Chronos'' Pendant, Breastplate of Valor, Dreamer''s Idol,
    Gem of Focus, Bragi''s Harp, Rod of Asclepius, Freya''s Tears, Blood-Bound Book,
    Helm of Radiance, Bancroft''s Talon, Shield of the Phoenix, Jade Scepter, Amanita
    Charm, Triton''s Conch, Bracer of The Abyss, Oni Hunter''s Garb.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.63
      pick: 0.57
      fit: 0.78
    The World Stone:
      total: 0.56
      efficiency: 0.49
      win: 0.66
      pick: 0.16
      fit: 0.56
    Soul Reaver:
      total: 0.56
      efficiency: 0.46
      win: 0.76
      pick: 0.07
      fit: 0.32
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.44
      win: 0.64
      pick: 0.33
      fit: 0.56
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.63
      pick: 0.26
      fit: 0.56
    Soul Gem:
      total: 0.64
      efficiency: 0.59
      win: 0.64
      pick: 0.3
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - The World Stone
  - Soul Reaver
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Eye of Providence, Genji''s Guard, Oni Hunter''s Garb, Blood-Bound
    Book, Bancroft''s Talon, Chandra''s Grace, Lifebinder, Breastplate of Valor, Freya''s
    Tears, Spear of the Magus, Shifter''s Shield, The Cosmic Horror, Phoenix Feather,
    Spectral Armor, Jade Scepter, Erosion, Helm of Radiance, Yogi''s Necklace, Draconic
    Scale, Wish-Granting Pearl.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.63
      pick: 0.57
      fit: 0.5
    The World Stone:
      total: 0.53
      efficiency: 0.49
      win: 0.66
      pick: 0.16
      fit: 0.38
    Soul Reaver:
      total: 0.55
      efficiency: 0.46
      win: 0.76
      pick: 0.07
      fit: 0.3
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.63
      pick: 0.26
      fit: 0.38
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.64
      efficiency: 0.59
      win: 0.64
      pick: 0.3
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The World Stone
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Soul Reaver
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
    for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Doom
    Orb, Dreamer''s Idol, Genji''s Guard, Chronos'' Pendant, Screeching Gargoyle,
    Breastplate of Valor, Death Metal, Rod of Asclepius, Blood-Bound Book, Helm of
    Radiance, Gem of Focus, Bancroft''s Talon, Jade Scepter, Bracer of The Abyss,
    Wish-Granting Pearl, Amanita Charm, Polynomicon, Ethereal Staff, Freya''s Tears.'
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.52
      win: 0.63
      pick: 0.57
      fit: 1.0
    The World Stone:
      total: 0.6
      efficiency: 0.49
      win: 0.66
      pick: 0.16
      fit: 0.84
    Soul Reaver:
      total: 0.57
      efficiency: 0.46
      win: 0.76
      pick: 0.07
      fit: 0.39
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.44
      win: 0.64
      pick: 0.33
      fit: 0.84
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.63
      pick: 0.26
      fit: 0.84
    Soul Gem:
      total: 0.66
      efficiency: 0.59
      win: 0.64
      pick: 0.3
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Soul Reaver
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
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
    this god: Gluttonous Grimoire, Genji''s Guard, Spear of the Magus, Bracer of The
    Abyss, Bragi''s Harp, Death Metal, The Cosmic Horror, Breastplate of Valor, Nimble
    Ring, Blood-Bound Book, Bancroft''s Talon, Chronos'' Pendant, Rod of Asclepius,
    Amanita Charm, Oni Hunter''s Garb, Helm of Radiance, Yogi''s Necklace, Kinetic
    Cuirass, Jade Scepter, Freya''s Tears, Dreamer''s Idol, Gem of Focus, Eye of Providence.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.63
      pick: 0.57
      fit: 0.41
    Soul Reaver:
      total: 0.55
      efficiency: 0.46
      win: 0.76
      pick: 0.07
      fit: 0.27
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.64
      pick: 0.3
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Soul Reaver
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - The World Stone
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Gluttonous Grimoire,
    Breastplate of Valor, Chronos'' Pendant, Freya''s Tears, Shield of the Phoenix,
    Gem of Focus, Spear of the Magus, The Cosmic Horror, Screeching Gargoyle, Chandra''s
    Grace, Death Metal, Doom Orb, Gladiator''s Shield, Amanita Charm, Rod of Asclepius,
    Oni Hunter''s Garb, Dreamer''s Idol, Yogi''s Necklace, Blood-Bound Book, Kinetic
    Cuirass, Helm of Radiance, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.62
      efficiency: 0.52
      win: 0.63
      pick: 0.57
      fit: 0.86
    The World Stone:
      total: 0.53
      efficiency: 0.49
      win: 0.66
      pick: 0.16
      fit: 0.37
    Soul Reaver:
      total: 0.54
      efficiency: 0.46
      win: 0.76
      pick: 0.07
      fit: 0.24
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.63
      pick: 0.26
      fit: 0.37
    Soul Gem:
      total: 0.65
      efficiency: 0.59
      win: 0.64
      pick: 0.3
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Chronos' Pendant
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Chronos'' Pendant, Dreamer''s Idol, Genji''s Guard, Doom Orb, Gem of Focus, Death
    Metal, Rod of Asclepius, Blood-Bound Book, Helm of Radiance, Breastplate of Valor,
    Bancroft''s Talon, Jade Scepter, Bracer of The Abyss, Wish-Granting Pearl, Polynomicon,
    Ethereal Staff, Ancient Signet, Alchemist Coat, Freya''s Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.65
      efficiency: 0.52
      win: 0.63
      pick: 0.57
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.63
      pick: 0.26
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Rod of Tahuti
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Spear of the
    Magus, The Cosmic Horror, Chronos'' Pendant, Dreamer''s Idol, Genji''s Guard,
    Doom Orb, Gem of Focus, Death Metal, Rod of Asclepius, Blood-Bound Book, Helm
    of Radiance, Breastplate of Valor, Bancroft''s Talon, Jade Scepter, Bracer of
    The Abyss, Wish-Granting Pearl, Polynomicon, Ethereal Staff, Ancient Signet, Alchemist
    Coat, Freya''s Tears.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.65
      efficiency: 0.52
      win: 0.63
      pick: 0.57
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.44
      win: 0.64
      pick: 0.33
      fit: 0.77
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.63
      pick: 0.26
      fit: 0.77
  swaps:
  - added: Rod of Tahuti
    removed: Chronos' Pendant
    reason: community 64% win over 177 matches (vs 56% on this god), taking the model's
      weakest slot from Chronos' Pendant
  starter: *id001
---
