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
  - name: Spear of Desolation
    pick_rate: 0.45
    win_rate: 0.55
    alternates:
    - name: Book of Thoth
      pick_rate: 0.36
      win_rate: 0.54
    - name: Doom Orb
      pick_rate: 0.06
      win_rate: 0.44
  - name: Book of Thoth
    pick_rate: 0.24
    win_rate: 0.58
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.31
      win_rate: 0.52
    - name: The World Stone
      pick_rate: 0.11
      win_rate: 0.48
  - name: Soul Gem
    pick_rate: 0.39
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.57
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.55
  - name: Rod of Tahuti
    pick_rate: 0.39
    win_rate: 0.53
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.21
      win_rate: 0.52
    - name: Soul Gem
      pick_rate: 0.11
      win_rate: 0.63
  - name: Obsidian Shard
    pick_rate: 0.32
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.63
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.39
  - name: Evil Eye
    pick_rate: 0.11
    win_rate: 0.45
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.63
    - name: Dreamer's Idol
      pick_rate: 0.08
      win_rate: 0.74
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.48
    win_rate: 0.59
  - name: Conduit Gem
    pick_rate: 0.29
    win_rate: 0.4
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/janus/
  last_verified: '2026-08-21'
  god_win_rate: 0.5256281407035176
  god_matches_won: 523
  god_matches_played: 995
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
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Nimble Ring,
    Chronos'' Pendant, Death Metal, Gem of Focus, Helm of Radiance, Totem of Death,
    Ancient Signet, Ethereal Staff, Rod of Asclepius, Doom Orb, Genji''s Guard, Breastplate
    of Valor, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Bracer of The Abyss,
    Freya''s Tears, Bancroft''s Talon, Alchemist Coat.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.58
      pick: 0.33
      fit: 0.44
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.55
      pick: 0.45
      fit: 1.0
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.53
      pick: 0.65
      fit: 0.78
    Obsidian Shard:
      total: 0.65
      efficiency: 0.54
      win: 0.64
      pick: 0.69
      fit: 0.88
    Dreamer's Idol:
      total: 0.64
      efficiency: 0.51
      win: 0.74
      pick: 0.25
      fit: 0.78
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Genji's Guard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Gluttonous Grimoire, Spear of the Magus, Nimble Ring, Genji''s Guard, Breastplate
    of Valor, Ancient Signet, Bragi''s Harp, Chronos'' Pendant, The Cosmic Horror,
    Helm of Radiance, Wish-Granting Pearl, Ethereal Staff, Rod of Asclepius, Triton''s
    Conch, Gem of Focus, Bancroft''s Talon, Freya''s Tears, Doom Orb, Polynomicon,
    Totem of Death, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.58
      pick: 0.33
      fit: 0.39
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.29
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.53
      pick: 0.65
      fit: 0.57
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.64
      pick: 0.69
      fit: 0.57
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.51
      win: 0.74
      pick: 0.25
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    god: Gluttonous Grimoire, Spear of the Magus, Death Metal, The Cosmic Horror,
    Genji''s Guard, Breastplate of Valor, Nimble Ring, Chronos'' Pendant, Freya''s
    Tears, Gem of Focus, Helm of Radiance, Bragi''s Harp, Totem of Death, Ancient
    Signet, Ethereal Staff, Shield of the Phoenix, Rod of Asclepius, Doom Orb, Amanita
    Charm, Screeching Gargoyle, Kinetic Cuirass, Jade Scepter, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.58
      pick: 0.33
      fit: 0.22
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.22
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.55
      pick: 0.45
      fit: 0.78
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.53
      pick: 0.65
      fit: 0.56
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.64
      pick: 0.69
      fit: 0.66
    Dreamer's Idol:
      total: 0.61
      efficiency: 0.51
      win: 0.74
      pick: 0.25
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire, Ethereal
    Staff, Rod of Asclepius, Kinetic Cuirass, Freya''s Tears, Shifter''s Shield, Genji''s
    Guard, Breastplate of Valor, Lifebinder, Spear of the Magus, Blood-Bound Book,
    Helm of Radiance, Phoenix Feather, Chandra''s Grace, Nimble Ring, Sphere of Negation,
    Erosion, Yogi''s Necklace, Bancroft''s Talon, Eye of Providence, Spectral Armor,
    Mantle Of Discord, Draconic Scale.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.55
      pick: 0.45
      fit: 0.48
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.53
      pick: 0.65
      fit: 0.37
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.64
      pick: 0.69
      fit: 0.47
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.51
      win: 0.74
      pick: 0.25
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.82
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.52
      pick: 0.61
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - The Cosmic Horror
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Doom
    Orb, Nimble Ring, Screeching Gargoyle, Chronos'' Pendant, Death Metal, Helm of
    Radiance, Genji''s Guard, Breastplate of Valor, Stone of Binding, Ancient Signet,
    Ethereal Staff, Rod of Asclepius, Gem of Focus, Freya''s Tears, Totem of Death,
    Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Amanita Charm, Bracer of
    The Abyss.'
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.55
      pick: 0.45
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.53
      pick: 0.65
      fit: 0.85
    Obsidian Shard:
      total: 0.66
      efficiency: 0.54
      win: 0.64
      pick: 0.69
      fit: 0.95
    Dreamer's Idol:
      total: 0.65
      efficiency: 0.51
      win: 0.74
      pick: 0.25
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Nimble Ring, Gluttonous Grimoire, Death Metal, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Genji''s Guard, Breastplate of Valor, Helm of Radiance,
    Chronos'' Pendant, The Cosmic Horror, Amanita Charm, Freya''s Tears, Ancient Signet,
    Kinetic Cuirass, Ethereal Staff, Blood-Bound Book, Rod of Asclepius, Bancroft''s
    Talon, Eye of Providence, Jade Scepter, Gem of Focus, Doom Orb.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.41
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.49
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.64
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.65
      fit: 0.3
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.64
      pick: 0.69
      fit: 0.4
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.51
      win: 0.74
      pick: 0.25
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
  - Genji's Guard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Chronos'' Pendant, Gluttonous Grimoire, Shield of the Phoenix,
    Gem of Focus, Screeching Gargoyle, Totem of Death, Spear of the Magus, Death Metal,
    Nimble Ring, Chandra''s Grace, Eye of Erebus, The Cosmic Horror, Helm of Radiance,
    Prophetic Cloak, Amanita Charm, Gladiator''s Shield, Kinetic Cuirass, Ancient
    Signet, Ethereal Staff, Doom Orb.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.55
      pick: 0.45
      fit: 0.85
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.65
      fit: 0.35
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.64
      pick: 0.69
      fit: 0.45
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.51
      win: 0.74
      pick: 0.25
      fit: 0.35
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.52
      pick: 0.61
      fit: 0.95
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
    Cosmic Horror, Nimble Ring, Chronos'' Pendant, Death Metal, Gem of Focus, Helm
    of Radiance, Totem of Death, Ancient Signet, Ethereal Staff, Rod of Asclepius,
    Genji''s Guard, Breastplate of Valor, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Bracer of The Abyss, Freya''s Tears, Bancroft''s Talon, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.55
      pick: 0.45
      fit: 1.0
    Doom Orb:
      total: 0.5
      efficiency: 0.53
      win: 0.44
      pick: 0.06
      fit: 0.78
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.53
      pick: 0.65
      fit: 0.78
    Obsidian Shard:
      total: 0.65
      efficiency: 0.54
      win: 0.64
      pick: 0.69
      fit: 0.88
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.52
      pick: 0.61
      fit: 1.0
  starter: *id001
---
