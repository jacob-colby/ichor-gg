---
type: smite-build
god: Kukulkan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Squall
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.55
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.79
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.46
    - name: Chronos' Pendant
      pick_rate: 0.02
      win_rate: 0.23
  - name: Spear of Desolation
    pick_rate: 0.26
    win_rate: 0.57
    alternates:
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.48
    - name: The Cosmic Horror
      pick_rate: 0.07
      win_rate: 0.48
  - name: The Cosmic Horror
    pick_rate: 0.13
    win_rate: 0.6
    alternates:
    - name: Polynomicon
      pick_rate: 0.11
      win_rate: 0.61
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.58
  - name: Rod of Tahuti
    pick_rate: 0.26
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.44
    - name: Totem of Death
      pick_rate: 0.08
      win_rate: 0.63
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.63
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.64
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.54
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.54
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.53
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.64
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.31
    win_rate: 0.57
  - name: Conduit Gem
    pick_rate: 0.2
    win_rate: 0.39
  - name: Pendulum of the Ages
    pick_rate: 0.2
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/kukulkan/
  last_verified: '2026-08-21'
  god_win_rate: 0.5267558528428093
  god_matches_won: 315
  god_matches_played: 598
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
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - The Cosmic Horror
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
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom Orb, The World
    Stone, Nimble Ring, Dreamer''s Idol, Totem of Death, Death Metal, Helm of Radiance,
    Genji''s Guard, Breastplate of Valor, Gem of Focus, Ancient Signet, Ethereal Staff,
    Rod of Asclepius, Jade Scepter, Freya''s Tears, Wish-Granting Pearl, Blood-Bound
    Book, Bracer of The Abyss, Bancroft''s Talon, Alchemist Coat, Chronos'' Pendant.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.57
      pick: 0.35
      fit: 0.84
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.2
      fit: 0.66
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.66
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.63
      pick: 0.35
      fit: 0.76
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.94
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Death Metal, Gluttonous Grimoire, Spear of the Magus, Nimble Ring, Genji''s
    Guard, Doom Orb, Breastplate of Valor, The World Stone, Ancient Signet, Bragi''s
    Harp, Helm of Radiance, Dreamer''s Idol, Wish-Granting Pearl, Ethereal Staff,
    Rod of Asclepius, Freya''s Tears, Gem of Focus, Triton''s Conch, Bancroft''s Talon,
    Amanita Charm, Jade Scepter, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.55
      pick: 0.79
      fit: 0.35
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.22
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.52
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.63
      pick: 0.35
      fit: 0.53
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Death Metal
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
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Death Metal, Doom Orb,
    Genji''s Guard, Breastplate of Valor, Nimble Ring, The World Stone, Dreamer''s
    Idol, Totem of Death, Freya''s Tears, Helm of Radiance, Gem of Focus, Ancient
    Signet, Bragi''s Harp, Ethereal Staff, Shield of the Phoenix, Amanita Charm, Rod
    of Asclepius, Kinetic Cuirass, Screeching Gargoyle, Jade Scepter, Wish-Granting
    Pearl, Chronos'' Pendant.'
  slot_scores:
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.57
      pick: 0.35
      fit: 0.7
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.5
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.63
      pick: 0.35
      fit: 0.6
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.59
      pick: 0.0
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
  - Obsidian Shard
  - Spear of Desolation
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Ethereal Staff, Rod of Asclepius, Kinetic Cuirass, Freya''s Tears, Genji''s Guard,
    Spear of the Magus, Breastplate of Valor, Shifter''s Shield, Blood-Bound Book,
    Lifebinder, Chandra''s Grace, Phoenix Feather, Helm of Radiance, Nimble Ring,
    Yogi''s Necklace, Sphere of Negation, Bancroft''s Talon, Erosion, Spectral Armor,
    Mantle Of Discord, Stone of Binding, Eye of Providence.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.35
      fit: 0.45
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.36
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.63
      pick: 0.35
      fit: 0.46
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.85
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
  - Spear of the Magus
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom Orb, The
    World Stone, Dreamer''s Idol, Nimble Ring, Screeching Gargoyle, Death Metal, Stone
    of Binding, Totem of Death, Genji''s Guard, Breastplate of Valor, Helm of Radiance,
    Ancient Signet, Ethereal Staff, Rod of Asclepius, Freya''s Tears, Gem of Focus,
    Amanita Charm, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Kinetic Cuirass,
    Chronos'' Pendant.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.57
      pick: 0.35
      fit: 0.88
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.2
      fit: 0.75
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.75
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.63
      pick: 0.35
      fit: 0.85
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.59
      pick: 0.0
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Death
    Metal, Bragi''s Harp, Bracer of The Abyss, Genji''s Guard, Breastplate of Valor,
    Helm of Radiance, Doom Orb, Amanita Charm, The World Stone, Freya''s Tears, Ancient
    Signet, Kinetic Cuirass, Ethereal Staff, Blood-Bound Book, Dreamer''s Idol, Rod
    of Asclepius, Bancroft''s Talon, Eye of Providence, Jade Scepter, Gem of Focus,
    Chronos'' Pendant.'
  slot_scores:
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
      total: 0.63
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.32
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.63
      pick: 0.35
      fit: 0.42
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Breastplate
    of Valor, Freya''s Tears, Totem of Death, Gluttonous Grimoire, Shield of the Phoenix,
    Spear of the Magus, Gem of Focus, Screeching Gargoyle, Death Metal, Nimble Ring,
    Chandra''s Grace, Doom Orb, The World Stone, Eye of Erebus, Amanita Charm, Helm
    of Radiance, Dreamer''s Idol, Kinetic Cuirass, Ancient Signet, Ethereal Staff,
    Prophetic Cloak, Rod of Asclepius, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.55
      pick: 0.79
      fit: 0.13
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.57
      pick: 0.35
      fit: 0.77
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.33
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.87
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
    Underrated for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom
    Orb, The World Stone, Nimble Ring, Dreamer''s Idol, Chronos'' Pendant, Death Metal,
    Helm of Radiance, Genji''s Guard, Breastplate of Valor, Gem of Focus, Ancient
    Signet, Ethereal Staff, Rod of Asclepius, Totem of Death, Jade Scepter, Freya''s
    Tears, Wish-Granting Pearl, Blood-Bound Book, Bracer of The Abyss, Bancroft''s
    Talon, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.57
      pick: 0.35
      fit: 0.84
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.66
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.63
      pick: 0.35
      fit: 0.76
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.94
  starter: *id001
---
