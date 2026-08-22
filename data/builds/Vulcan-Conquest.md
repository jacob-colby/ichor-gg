---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.55
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.34
    win_rate: 0.55
    alternates:
    - name: Book of Thoth
      pick_rate: 0.34
      win_rate: 0.56
    - name: Doom Orb
      pick_rate: 0.06
      win_rate: 0.57
  - name: The World Stone
    pick_rate: 0.14
    win_rate: 0.58
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.55
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.53
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.58
    alternates:
    - name: Soul Gem
      pick_rate: 0.14
      win_rate: 0.64
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.54
  - name: Obsidian Shard
    pick_rate: 0.28
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.25
      win_rate: 0.64
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.45
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.41
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.64
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.6
  - name: Shrapnel Mod
    pick_rate: 0.15
    win_rate: 0.55
    alternates:
    - name: Thermal Mod
      pick_rate: 0.12
      win_rate: 0.51
    - name: Surplus Mod
      pick_rate: 0.09
      win_rate: 0.53
  - name: Surplus Mod
    pick_rate: 0.26
    win_rate: 0.56
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.33
      win_rate: 0.56
    - name: Thermal Mod
      pick_rate: 0.24
      win_rate: 0.63
  - name: Seismic Mod
    pick_rate: 0.14
    win_rate: 0.56
    alternates:
    - name: Surplus Mod
      pick_rate: 0.69
      win_rate: 0.6
    - name: Thermal Mod
      pick_rate: 0.11
      win_rate: 0.53
  - name: Masterwork Mod
    pick_rate: 0.05
    win_rate: 0.0
    alternates:
    - name: Seismic Mod
      pick_rate: 0.62
      win_rate: 0.43
    - name: Surplus Mod
      pick_rate: 0.32
      win_rate: 0.58
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.31
    win_rate: 0.6
  - name: Sands Of Time
    pick_rate: 0.22
    win_rate: 0.44
  - name: Archmage's Gem
    pick_rate: 0.21
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-08-22'
  god_win_rate: 0.5472703062583223
  god_matches_won: 411
  god_matches_played: 751
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
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
    this god: Gluttonous Grimoire, Spear of the Magus, Nimble Ring, Doom Orb, The
    Cosmic Horror, Dreamer''s Idol, Chronos'' Pendant, Death Metal, Helm of Radiance,
    Bracer of The Abyss, Genji''s Guard, Breastplate of Valor, Gem of Focus, Ancient
    Signet, Ethereal Staff, Rod of Asclepius, Bragi''s Harp, Totem of Death, Jade
    Scepter, Freya''s Tears, Wish-Granting Pearl, Blood-Bound Book, Bancroft''s Talon,
    Alchemist Coat.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.56
      pick: 0.34
      fit: 0.35
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.55
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
      win: 0.58
      pick: 0.3
      fit: 0.66
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.58
      pick: 0.47
      fit: 0.76
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.64
      pick: 0.22
      fit: 0.93
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Doom Orb
  - The World Stone
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Gluttonous Grimoire, Nimble Ring, Spear of the Magus, Doom Orb, Genji''s
    Guard, Bragi''s Harp, Breastplate of Valor, Ancient Signet, Chronos'' Pendant,
    The Cosmic Horror, Helm of Radiance, Dreamer''s Idol, Wish-Granting Pearl, Ethereal
    Staff, Rod of Asclepius, Bracer of The Abyss, Freya''s Tears, Gem of Focus, Triton''s
    Conch, Bancroft''s Talon, Amanita Charm, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.56
      pick: 0.34
      fit: 0.35
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.06
      fit: 0.52
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.19
      fit: 0.52
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.58
      pick: 0.3
      fit: 0.52
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.58
      pick: 0.47
      fit: 0.53
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.64
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
    god: Gluttonous Grimoire, Spear of the Magus, Death Metal, Nimble Ring, Doom Orb,
    Genji''s Guard, The Cosmic Horror, Breastplate of Valor, Dreamer''s Idol, Chronos''
    Pendant, Bragi''s Harp, Freya''s Tears, Helm of Radiance, Gem of Focus, Ancient
    Signet, Ethereal Staff, Shield of the Phoenix, Amanita Charm, Rod of Asclepius,
    Totem of Death, Bracer of The Abyss, Kinetic Cuirass, Screeching Gargoyle, Jade
    Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.56
      pick: 0.34
      fit: 0.2
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.55
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
      win: 0.58
      pick: 0.3
      fit: 0.5
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.58
      pick: 0.47
      fit: 0.6
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.64
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
    this god: Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire, Ethereal
    Staff, Rod of Asclepius, Kinetic Cuirass, Freya''s Tears, Nimble Ring, Genji''s
    Guard, Spear of the Magus, Breastplate of Valor, Shifter''s Shield, Blood-Bound
    Book, Lifebinder, Chandra''s Grace, Phoenix Feather, Helm of Radiance, Yogi''s
    Necklace, Sphere of Negation, Bancroft''s Talon, Spectral Armor, Erosion, Mantle
    Of Discord, Stone of Binding, Eye of Providence.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.34
      fit: 0.45
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.3
      fit: 0.36
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.47
      fit: 0.46
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.64
      pick: 0.22
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - The World Stone
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
    for this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The Cosmic Horror,
    Dreamer''s Idol, Nimble Ring, Screeching Gargoyle, Death Metal, Chronos'' Pendant,
    Stone of Binding, Genji''s Guard, Breastplate of Valor, Helm of Radiance, Ancient
    Signet, Bracer of The Abyss, Ethereal Staff, Rod of Asclepius, Freya''s Tears,
    Gem of Focus, Amanita Charm, Jade Scepter, Bragi''s Harp, Totem of Death, Wish-Granting
    Pearl.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.55
      pick: 0.34
      fit: 0.88
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.75
    The World Stone:
      total: 0.56
      efficiency: 0.52
      win: 0.58
      pick: 0.19
      fit: 0.75
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.58
      pick: 0.3
      fit: 0.75
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.58
      pick: 0.47
      fit: 0.85
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.64
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Death Metal, Bragi''s
    Harp, Bracer of The Abyss, Genji''s Guard, Breastplate of Valor, Doom Orb, Helm
    of Radiance, The Cosmic Horror, Chronos'' Pendant, Amanita Charm, Freya''s Tears,
    Ancient Signet, Kinetic Cuirass, Ethereal Staff, Blood-Bound Book, Dreamer''s
    Idol, Rod of Asclepius, Bancroft''s Talon, Eye of Providence, Jade Scepter, Gem
    of Focus.'
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
      win: 0.58
      pick: 0.3
      fit: 0.32
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.47
      fit: 0.42
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.64
      pick: 0.22
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Chronos'' Pendant, Gluttonous Grimoire, Shield of the Phoenix,
    Nimble Ring, Spear of the Magus, Gem of Focus, Screeching Gargoyle, Death Metal,
    Totem of Death, Doom Orb, Chandra''s Grace, The Cosmic Horror, Eye of Erebus,
    Amanita Charm, Helm of Radiance, Dreamer''s Idol, Kinetic Cuirass, Bragi''s Harp,
    Ancient Signet, Ethereal Staff, Prophetic Cloak.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.56
      pick: 0.34
      fit: 0.13
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.55
      pick: 0.34
      fit: 0.76
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.3
      fit: 0.33
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.64
      pick: 0.22
      fit: 0.86
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, Nimble Ring,
    Doom Orb, The Cosmic Horror, Dreamer''s Idol, Chronos'' Pendant, Death Metal,
    Helm of Radiance, Bracer of The Abyss, Genji''s Guard, Breastplate of Valor, Gem
    of Focus, Ancient Signet, Ethereal Staff, Rod of Asclepius, Bragi''s Harp, Totem
    of Death, Jade Scepter, Freya''s Tears, Wish-Granting Pearl, Blood-Bound Book,
    Bancroft''s Talon, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.55
      pick: 0.34
      fit: 0.83
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.57
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
      win: 0.58
      pick: 0.3
      fit: 0.66
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.58
      pick: 0.47
      fit: 0.76
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.64
      pick: 0.22
      fit: 0.93
  starter: *id001
---
