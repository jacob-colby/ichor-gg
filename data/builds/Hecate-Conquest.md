---
type: smite-build
god: Hecate
mode: Conquest
builds:
- source: community
  aspect: Aspect of Ruin
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.58
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.55
    win_rate: 0.6
    alternates:
    - name: Book of Thoth
      pick_rate: 0.2
      win_rate: 0.55
    - name: Chronos' Pendant
      pick_rate: 0.09
      win_rate: 0.63
  - name: Book of Thoth
    pick_rate: 0.22
    win_rate: 0.51
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.18
      win_rate: 0.52
    - name: The World Stone
      pick_rate: 0.18
      win_rate: 0.61
  - name: Soul Gem
    pick_rate: 0.23
    win_rate: 0.52
    alternates:
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.58
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.51
  - name: Rod of Tahuti
    pick_rate: 0.35
    win_rate: 0.61
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.2
      win_rate: 0.48
    - name: The World Stone
      pick_rate: 0.05
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.19
    win_rate: 0.61
    alternates:
    - name: Evil Eye
      pick_rate: 0.14
      win_rate: 0.51
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.52
  - name: Evil Eye
    pick_rate: 0.12
    win_rate: 0.65
    alternates:
    - name: Void Shard
      pick_rate: 0.1
      win_rate: 0.47
    - name: Oracle Staff
      pick_rate: 0.06
      win_rate: 0.36
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.27
    win_rate: 0.64
  - name: Conduit Gem
    pick_rate: 0.21
    win_rate: 0.67
  - name: Pendulum of the Ages
    pick_rate: 0.19
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/hecate/
  last_verified: '2026-08-21'
  god_win_rate: 0.5771276595744681
  god_matches_won: 217
  god_matches_played: 376
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Nimble Ring
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
    this god: Gluttonous Grimoire, Spear of the Magus, Chronos'' Pendant, Doom Orb,
    The Cosmic Horror, Nimble Ring, Dreamer''s Idol, Death Metal, Helm of Radiance,
    Genji''s Guard, Gem of Focus, Breastplate of Valor, Ancient Signet, Ethereal Staff,
    Totem of Death, Rod of Asclepius, Freya''s Tears, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Bracer of The Abyss, Bancroft''s Talon, Alchemist Coat.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.36
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.88
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.68
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.61
      pick: 0.25
      fit: 0.68
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.68
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.78
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - The World Stone
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Gluttonous Grimoire, Spear of the Magus, Chronos'' Pendant, Nimble Ring,
    Doom Orb, Genji''s Guard, Breastplate of Valor, Ancient Signet, Bragi''s Harp,
    The Cosmic Horror, Helm of Radiance, Dreamer''s Idol, Wish-Granting Pearl, Ethereal
    Staff, Rod of Asclepius, Gem of Focus, Freya''s Tears, Triton''s Conch, Bancroft''s
    Talon, Jade Scepter, Polynomicon, Amanita Charm.'
  slot_scores:
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.57
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.53
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.25
      fit: 0.53
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.53
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Death Metal
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Death Metal
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Spear of the Magus, Death Metal, Chronos'' Pendant,
    Doom Orb, The Cosmic Horror, Genji''s Guard, Breastplate of Valor, Nimble Ring,
    Dreamer''s Idol, Freya''s Tears, Helm of Radiance, Gem of Focus, Bragi''s Harp,
    Ancient Signet, Ethereal Staff, Shield of the Phoenix, Totem of Death, Rod of
    Asclepius, Amanita Charm, Kinetic Cuirass, Screeching Gargoyle, Jade Scepter,
    Wish-Granting Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.21
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.72
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.52
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire, Ethereal
    Staff, Rod of Asclepius, Kinetic Cuirass, Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Spear of the Magus, Shifter''s Shield, Blood-Bound Book, Lifebinder,
    Chandra''s Grace, Phoenix Feather, Helm of Radiance, Nimble Ring, Sphere of Negation,
    Yogi''s Necklace, Bancroft''s Talon, Erosion, Spectral Armor, Mantle Of Discord,
    Stone of Binding, Eye of Providence.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.57
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.73
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.47
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.36
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.46
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Nimble Ring
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
    for this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The Cosmic Horror,
    Dreamer''s Idol, Chronos'' Pendant, Nimble Ring, Screeching Gargoyle, Death Metal,
    Genji''s Guard, Breastplate of Valor, Stone of Binding, Helm of Radiance, Ancient
    Signet, Ethereal Staff, Rod of Asclepius, Gem of Focus, Freya''s Tears, Totem
    of Death, Amanita Charm, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book,
    Kinetic Cuirass.'
  slot_scores:
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.26
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.91
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.76
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.25
      fit: 0.76
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.76
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Death Metal, Bragi''s
    Harp, Chronos'' Pendant, Genji''s Guard, Breastplate of Valor, Bracer of The Abyss,
    Helm of Radiance, Doom Orb, The Cosmic Horror, Amanita Charm, Freya''s Tears,
    Ancient Signet, Kinetic Cuirass, Ethereal Staff, Blood-Bound Book, Dreamer''s
    Idol, Rod of Asclepius, Bancroft''s Talon, Eye of Providence, Gem of Focus, Jade
    Scepter.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.6
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.41
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.31
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
    Chronos'' Pendant, Freya''s Tears, Gluttonous Grimoire, Shield of the Phoenix,
    Spear of the Magus, Gem of Focus, Screeching Gargoyle, Totem of Death, Death Metal,
    Nimble Ring, Chandra''s Grace, Doom Orb, The Cosmic Horror, Eye of Erebus, Amanita
    Charm, Dreamer''s Idol, Helm of Radiance, Kinetic Cuirass, Ancient Signet, Prophetic
    Cloak, Ethereal Staff, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.55
      win: 0.63
      pick: 0.09
      fit: 0.58
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.79
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.34
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.52
      pick: 0.36
      fit: 0.89
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The
    Cosmic Horror, Nimble Ring, Dreamer''s Idol, Chronos'' Pendant, Death Metal, Helm
    of Radiance, Genji''s Guard, Gem of Focus, Breastplate of Valor, Ancient Signet,
    Ethereal Staff, Totem of Death, Rod of Asclepius, Freya''s Tears, Jade Scepter,
    Wish-Granting Pearl, Blood-Bound Book, Bracer of The Abyss, Bancroft''s Talon,
    Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.88
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.68
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.68
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.78
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.52
      pick: 0.36
      fit: 0.98
  starter: *id001
---
