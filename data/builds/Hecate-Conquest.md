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
    The Cosmic Horror, Dreamer''s Idol, Nimble Ring, Death Metal, Gem of Focus, Helm
    of Radiance, Genji''s Guard, Totem of Death, Breastplate of Valor, Ancient Signet,
    Ethereal Staff, Rod of Asclepius, Jade Scepter, Freya''s Tears, Wish-Granting
    Pearl, Blood-Bound Book, Bracer of The Abyss, Bancroft''s Talon, Alchemist Coat.'
  slot_scores:
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 1.0
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.77
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.25
      fit: 0.77
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.77
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.87
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Nimble Ring
  - Death Metal
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Doom Orb
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Gluttonous Grimoire, Spear of the Magus, Chronos'' Pendant, Doom Orb, Nimble
    Ring, Genji''s Guard, Breastplate of Valor, Ancient Signet, Bragi''s Harp, The
    Cosmic Horror, Helm of Radiance, Dreamer''s Idol, Wish-Granting Pearl, Ethereal
    Staff, Rod of Asclepius, Triton''s Conch, Gem of Focus, Bancroft''s Talon, Freya''s
    Tears, Polynomicon, Totem of Death, Jade Scepter.'
  slot_scores:
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.29
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.61
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.57
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.25
      fit: 0.57
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.57
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
    Dreamer''s Idol, Freya''s Tears, Gem of Focus, Helm of Radiance, Bragi''s Harp,
    Totem of Death, Ancient Signet, Ethereal Staff, Shield of the Phoenix, Rod of
    Asclepius, Amanita Charm, Screeching Gargoyle, Kinetic Cuirass, Jade Scepter,
    Wish-Granting Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.22
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.78
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.56
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.66
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
    Staff, Rod of Asclepius, Kinetic Cuirass, Freya''s Tears, Genji''s Guard, Spear
    of the Magus, Breastplate of Valor, Shifter''s Shield, Lifebinder, Chandra''s
    Grace, Blood-Bound Book, Phoenix Feather, Helm of Radiance, Nimble Ring, Sphere
    of Negation, Yogi''s Necklace, Bancroft''s Talon, Erosion, Spectral Armor, Eye
    of Providence, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.76
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.5
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.38
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.48
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.8
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
    Genji''s Guard, Breastplate of Valor, Helm of Radiance, Stone of Binding, Ancient
    Signet, Ethereal Staff, Gem of Focus, Rod of Asclepius, Freya''s Tears, Totem
    of Death, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Amanita Charm,
    Kinetic Cuirass.'
  slot_scores:
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.29
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 1.0
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.84
    The World Stone:
      total: 0.59
      efficiency: 0.52
      win: 0.61
      pick: 0.25
      fit: 0.84
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.84
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.94
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
  - Chronos' Pendant
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Chronos'' Pendant,
    Breastplate of Valor, Freya''s Tears, Gluttonous Grimoire, Shield of the Phoenix,
    Gem of Focus, Spear of the Magus, Screeching Gargoyle, Totem of Death, Death Metal,
    Nimble Ring, Chandra''s Grace, Doom Orb, The Cosmic Horror, Eye of Erebus, Dreamer''s
    Idol, Helm of Radiance, Amanita Charm, Prophetic Cloak, Kinetic Cuirass, Gladiator''s
    Shield, Ancient Signet, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.55
      win: 0.63
      pick: 0.09
      fit: 0.63
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 0.86
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.37
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.52
      pick: 0.36
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The
    Cosmic Horror, Dreamer''s Idol, Nimble Ring, Chronos'' Pendant, Death Metal, Gem
    of Focus, Helm of Radiance, Genji''s Guard, Totem of Death, Breastplate of Valor,
    Ancient Signet, Ethereal Staff, Rod of Asclepius, Jade Scepter, Freya''s Tears,
    Wish-Granting Pearl, Blood-Bound Book, Bracer of The Abyss, Bancroft''s Talon,
    Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.6
      pick: 0.55
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.61
      pick: 0.58
      fit: 0.77
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.61
      pick: 0.41
      fit: 0.87
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.52
      pick: 0.36
      fit: 1.0
  starter: *id001
---
