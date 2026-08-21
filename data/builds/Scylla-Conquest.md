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
      win_rate: 0.54
    - name: Yogi's Necklace
      pick_rate: 0.09
      win_rate: 0.6
  - name: Book of Thoth
    pick_rate: 0.24
    win_rate: 0.48
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.27
      win_rate: 0.52
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.49
  - name: Polynomicon
    pick_rate: 0.25
    win_rate: 0.49
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.49
    - name: Soul Gem
      pick_rate: 0.13
      win_rate: 0.52
  - name: Rod of Tahuti
    pick_rate: 0.35
    win_rate: 0.47
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.18
      win_rate: 0.49
    - name: Polynomicon
      pick_rate: 0.07
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.28
    win_rate: 0.48
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.63
    - name: Evil Eye
      pick_rate: 0.09
      win_rate: 0.43
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.48
    alternates:
    - name: Killing Stone
      pick_rate: 0.08
      win_rate: 0.41
    - name: Dreamer's Idol
      pick_rate: 0.06
      win_rate: 0.38
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.44
    win_rate: 0.54
  - name: Conduit Gem
    pick_rate: 0.34
    win_rate: 0.44
  - name: Pendulum of the Ages
    pick_rate: 0.09
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-08-21'
  god_win_rate: 0.4945945945945946
  god_matches_won: 366
  god_matches_played: 740
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The Cosmic Horror,
    The World Stone, Nimble Ring, Chronos'' Pendant, Death Metal, Helm of Radiance,
    Gem of Focus, Genji''s Guard, Ancient Signet, Breastplate of Valor, Ethereal Staff,
    Rod of Asclepius, Totem of Death, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Freya''s Tears, Bracer of The Abyss, Bancroft''s Talon, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.47
      pick: 0.47
      fit: 0.89
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.49
      pick: 0.12
      fit: 0.71
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.71
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.47
      pick: 0.58
      fit: 0.71
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.48
      pick: 0.61
      fit: 0.81
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.52
      pick: 0.2
      fit: 0.99
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Genji's Guard
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Gluttonous Grimoire, Spear of the Magus, Doom Orb, Nimble Ring, Genji''s
    Guard, Breastplate of Valor, The World Stone, Ancient Signet, Chronos'' Pendant,
    Bragi''s Harp, The Cosmic Horror, Helm of Radiance, Wish-Granting Pearl, Ethereal
    Staff, Rod of Asclepius, Gem of Focus, Freya''s Tears, Triton''s Conch, Bancroft''s
    Talon, Jade Scepter, Amanita Charm.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.23
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.47
      pick: 0.47
      fit: 0.58
    Doom Orb:
      total: 0.49
      efficiency: 0.53
      win: 0.49
      pick: 0.12
      fit: 0.54
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.47
      pick: 0.58
      fit: 0.54
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.48
      pick: 0.61
      fit: 0.54
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.52
      pick: 0.2
      fit: 0.68
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
    god: Gluttonous Grimoire, Spear of the Magus, Death Metal, Doom Orb, The Cosmic
    Horror, Genji''s Guard, Breastplate of Valor, The World Stone, Nimble Ring, Chronos''
    Pendant, Freya''s Tears, Helm of Radiance, Gem of Focus, Bragi''s Harp, Ancient
    Signet, Ethereal Staff, Totem of Death, Shield of the Phoenix, Rod of Asclepius,
    Amanita Charm, Kinetic Cuirass, Screeching Gargoyle, Jade Scepter, Wish-Granting
    Pearl.'
  slot_scores:
    Death Metal:
      total: 0.49
      efficiency: 0.61
      win: 0.48
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.47
      pick: 0.47
      fit: 0.73
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.47
      pick: 0.58
      fit: 0.52
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.48
      pick: 0.61
      fit: 0.62
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.52
      pick: 0.2
      fit: 0.83
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
    this god: Amanita Charm, Yogi''s Necklace, Shield of the Phoenix, Gluttonous Grimoire,
    Ethereal Staff, Rod of Asclepius, Kinetic Cuirass, Freya''s Tears, Spear of the
    Magus, Genji''s Guard, Breastplate of Valor, Shifter''s Shield, Lifebinder, Blood-Bound
    Book, Phoenix Feather, Helm of Radiance, Chandra''s Grace, Nimble Ring, Sphere
    of Negation, Bancroft''s Talon, Erosion, Spectral Armor, Mantle Of Discord, Eye
    of Providence, Stone of Binding.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.58
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.47
      pick: 0.47
      fit: 0.47
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.47
      pick: 0.58
      fit: 0.37
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.48
      pick: 0.61
      fit: 0.47
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.52
      pick: 0.2
      fit: 0.87
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
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The Cosmic Horror,
    The World Stone, Nimble Ring, Screeching Gargoyle, Death Metal, Chronos'' Pendant,
    Genji''s Guard, Stone of Binding, Helm of Radiance, Breastplate of Valor, Ancient
    Signet, Ethereal Staff, Rod of Asclepius, Gem of Focus, Freya''s Tears, Jade Scepter,
    Totem of Death, Amanita Charm, Wish-Granting Pearl, Blood-Bound Book, Kinetic
    Cuirass.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.47
      pick: 0.47
      fit: 0.92
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.49
      pick: 0.12
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.47
      pick: 0.58
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.48
      pick: 0.61
      fit: 0.89
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.52
      pick: 0.2
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Death Metal, Bragi''s
    Harp, Bracer of The Abyss, Doom Orb, Genji''s Guard, Breastplate of Valor, Helm
    of Radiance, The Cosmic Horror, Chronos'' Pendant, Amanita Charm, The World Stone,
    Freya''s Tears, Ancient Signet, Kinetic Cuirass, Ethereal Staff, Blood-Bound Book,
    Rod of Asclepius, Bancroft''s Talon, Eye of Providence, Jade Scepter, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.48
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.47
      pick: 0.58
      fit: 0.32
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.48
      pick: 0.61
      fit: 0.42
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.52
      pick: 0.2
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Spear of the Magus, Gem of Focus, Screeching Gargoyle, Totem of Death, Death Metal,
    Nimble Ring, Doom Orb, Chandra''s Grace, The Cosmic Horror, The World Stone, Eye
    of Erebus, Amanita Charm, Helm of Radiance, Kinetic Cuirass, Prophetic Cloak,
    Ancient Signet, Gladiator''s Shield, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.48
      pick: 0.33
      fit: 0.14
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.47
      pick: 0.47
      fit: 0.8
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.47
      pick: 0.58
      fit: 0.35
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.52
      pick: 0.2
      fit: 0.9
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
    Cosmic Horror, The World Stone, Nimble Ring, Chronos'' Pendant, Death Metal, Helm
    of Radiance, Gem of Focus, Genji''s Guard, Ancient Signet, Breastplate of Valor,
    Ethereal Staff, Rod of Asclepius, Totem of Death, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Freya''s Tears, Bracer of The Abyss, Bancroft''s Talon,
    Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.47
      pick: 0.47
      fit: 0.89
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.49
      pick: 0.12
      fit: 0.71
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.71
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.47
      pick: 0.58
      fit: 0.71
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.48
      pick: 0.61
      fit: 0.81
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.52
      pick: 0.2
      fit: 0.99
  starter: *id001
---
