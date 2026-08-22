---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.54
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.46
    win_rate: 0.47
    alternates:
    - name: Book of Thoth
      pick_rate: 0.22
      win_rate: 0.55
    - name: Yogi's Necklace
      pick_rate: 0.09
      win_rate: 0.57
  - name: Book of Thoth
    pick_rate: 0.24
    win_rate: 0.46
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.54
    - name: Doom Orb
      pick_rate: 0.08
      win_rate: 0.48
  - name: Polynomicon
    pick_rate: 0.24
    win_rate: 0.49
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.48
    - name: Soul Gem
      pick_rate: 0.13
      win_rate: 0.51
  - name: Rod of Tahuti
    pick_rate: 0.35
    win_rate: 0.49
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.18
      win_rate: 0.47
    - name: Polynomicon
      pick_rate: 0.07
      win_rate: 0.65
  - name: Obsidian Shard
    pick_rate: 0.27
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.59
    - name: Evil Eye
      pick_rate: 0.09
      win_rate: 0.45
  - name: Killing Stone
    pick_rate: 0.08
    win_rate: 0.42
    alternates:
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.5
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
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-08-22'
  god_win_rate: 0.4932182490752158
  god_matches_won: 400
  god_matches_played: 811
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
    Gem of Focus, Ancient Signet, Ethereal Staff, Totem of Death, Rod of Asclepius,
    Genji''s Guard, Breastplate of Valor, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Freya''s Tears, Bracer of The Abyss, Bancroft''s Talon, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.47
      pick: 0.46
      fit: 1.0
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.48
      pick: 0.11
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.49
      pick: 0.58
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.5
      pick: 0.58
      fit: 0.89
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.51
      pick: 0.2
      fit: 1.0
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Gluttonous Grimoire, Spear of the Magus, Doom Orb, Nimble Ring, The World
    Stone, Genji''s Guard, Breastplate of Valor, Ancient Signet, Bragi''s Harp, Chronos''
    Pendant, The Cosmic Horror, Helm of Radiance, Wish-Granting Pearl, Ethereal Staff,
    Rod of Asclepius, Triton''s Conch, Gem of Focus, Bancroft''s Talon, Freya''s Tears,
    Totem of Death, Jade Scepter.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.47
      pick: 0.46
      fit: 0.61
    Doom Orb:
      total: 0.49
      efficiency: 0.53
      win: 0.48
      pick: 0.11
      fit: 0.57
    The World Stone:
      total: 0.49
      efficiency: 0.52
      win: 0.49
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.49
      pick: 0.58
      fit: 0.57
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.5
      pick: 0.58
      fit: 0.57
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.51
      pick: 0.2
      fit: 0.71
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
    Horror, The World Stone, Genji''s Guard, Breastplate of Valor, Nimble Ring, Chronos''
    Pendant, Freya''s Tears, Gem of Focus, Helm of Radiance, Bragi''s Harp, Totem
    of Death, Ancient Signet, Ethereal Staff, Shield of the Phoenix, Rod of Asclepius,
    Amanita Charm, Screeching Gargoyle, Kinetic Cuirass, Jade Scepter, Wish-Granting
    Pearl.'
  slot_scores:
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.49
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.47
      pick: 0.46
      fit: 0.78
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.49
      pick: 0.58
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.5
      pick: 0.58
      fit: 0.66
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.51
      pick: 0.2
      fit: 0.88
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
    Staff, Rod of Asclepius, Kinetic Cuirass, Yogi''s Necklace, Freya''s Tears, Spear
    of the Magus, Shifter''s Shield, Genji''s Guard, Breastplate of Valor, Lifebinder,
    Blood-Bound Book, Helm of Radiance, Phoenix Feather, Chandra''s Grace, Nimble
    Ring, Sphere of Negation, Erosion, Bancroft''s Talon, Eye of Providence, Spectral
    Armor, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.47
      pick: 0.46
      fit: 0.49
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.49
      pick: 0.58
      fit: 0.39
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.58
      fit: 0.49
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.51
      pick: 0.2
      fit: 0.89
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
    for this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The Cosmic Horror,
    The World Stone, Nimble Ring, Screeching Gargoyle, Chronos'' Pendant, Death Metal,
    Helm of Radiance, Genji''s Guard, Breastplate of Valor, Stone of Binding, Ancient
    Signet, Ethereal Staff, Rod of Asclepius, Gem of Focus, Freya''s Tears, Totem
    of Death, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Amanita Charm,
    Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.47
      pick: 0.46
      fit: 1.0
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.48
      pick: 0.11
      fit: 0.85
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.49
      pick: 0.58
      fit: 0.85
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.5
      pick: 0.58
      fit: 0.95
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.51
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
    Harp, Bracer of The Abyss, Genji''s Guard, Breastplate of Valor, Helm of Radiance,
    Doom Orb, The Cosmic Horror, Chronos'' Pendant, Amanita Charm, The World Stone,
    Freya''s Tears, Ancient Signet, Kinetic Cuirass, Ethereal Staff, Blood-Bound Book,
    Rod of Asclepius, Bancroft''s Talon, Eye of Providence, Jade Scepter, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.49
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.49
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.49
      pick: 0.58
      fit: 0.32
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.58
      fit: 0.42
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.51
      pick: 0.2
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Obsidian Shard
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
    Gem of Focus, Spear of the Magus, Screeching Gargoyle, Totem of Death, Death Metal,
    Nimble Ring, Chandra''s Grace, Doom Orb, The Cosmic Horror, Eye of Erebus, The
    World Stone, Helm of Radiance, Amanita Charm, Prophetic Cloak, Kinetic Cuirass,
    Gladiator''s Shield, Ancient Signet, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.47
      pick: 0.46
      fit: 0.86
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.49
      pick: 0.58
      fit: 0.37
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.58
      fit: 0.47
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.51
      pick: 0.2
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
    Cosmic Horror, The World Stone, Nimble Ring, Chronos'' Pendant, Death Metal, Helm
    of Radiance, Gem of Focus, Ancient Signet, Ethereal Staff, Totem of Death, Rod
    of Asclepius, Genji''s Guard, Breastplate of Valor, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Freya''s Tears, Bracer of The Abyss, Bancroft''s Talon,
    Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.47
      pick: 0.46
      fit: 1.0
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.48
      pick: 0.11
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.49
      pick: 0.58
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.5
      pick: 0.58
      fit: 0.89
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.51
      pick: 0.2
      fit: 1.0
  starter: *id001
---
