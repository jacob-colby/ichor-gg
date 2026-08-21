---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.54
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.34
    win_rate: 0.53
    alternates:
    - name: Book of Thoth
      pick_rate: 0.33
      win_rate: 0.55
    - name: The World Stone
      pick_rate: 0.06
      win_rate: 0.49
  - name: The World Stone
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.51
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.54
    alternates:
    - name: Soul Gem
      pick_rate: 0.14
      win_rate: 0.66
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.55
  - name: Obsidian Shard
    pick_rate: 0.29
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.24
      win_rate: 0.62
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.43
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.43
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.64
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.6
  - name: Shrapnel Mod
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Thermal Mod
      pick_rate: 0.11
      win_rate: 0.47
    - name: Surplus Mod
      pick_rate: 0.09
      win_rate: 0.51
  - name: Surplus Mod
    pick_rate: 0.25
    win_rate: 0.52
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.32
      win_rate: 0.55
    - name: Thermal Mod
      pick_rate: 0.24
      win_rate: 0.63
  - name: Seismic Mod
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Surplus Mod
      pick_rate: 0.67
      win_rate: 0.57
    - name: Thermal Mod
      pick_rate: 0.12
      win_rate: 0.53
  - name: Masterwork Mod
    pick_rate: 0.06
    win_rate: 0.0
    alternates:
    - name: Seismic Mod
      pick_rate: 0.62
      win_rate: 0.48
    - name: Surplus Mod
      pick_rate: 0.32
      win_rate: 0.55
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.32
    win_rate: 0.59
  - name: Sands Of Time
    pick_rate: 0.22
    win_rate: 0.44
  - name: Archmage's Gem
    pick_rate: 0.21
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-08-21'
  god_win_rate: 0.5342465753424658
  god_matches_won: 351
  god_matches_played: 657
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
    Genji''s Guard, Bracer of The Abyss, Breastplate of Valor, Ancient Signet, Ethereal
    Staff, Gem of Focus, Rod of Asclepius, Bragi''s Harp, Totem of Death, Freya''s
    Tears, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Amanita Charm, Bancroft''s
    Talon.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.55
      pick: 0.33
      fit: 0.32
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.76
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.54
      pick: 0.3
      fit: 0.6
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.57
      pick: 0.48
      fit: 0.7
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.86
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Gluttonous Grimoire, Nimble Ring, Spear of the Magus, Genji''s Guard, Breastplate
    of Valor, Doom Orb, Bragi''s Harp, Ancient Signet, Chronos'' Pendant, Helm of
    Radiance, The Cosmic Horror, Wish-Granting Pearl, Dreamer''s Idol, Ethereal Staff,
    Rod of Asclepius, Freya''s Tears, Bracer of The Abyss, Gem of Focus, Amanita Charm,
    Bancroft''s Talon, Triton''s Conch, Kinetic Cuirass.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.55
      pick: 0.33
      fit: 0.33
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.21
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.19
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.54
      pick: 0.3
      fit: 0.49
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.48
      fit: 0.5
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.62
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
    god: Gluttonous Grimoire, Spear of the Magus, Death Metal, Nimble Ring, Genji''s
    Guard, Breastplate of Valor, Doom Orb, The Cosmic Horror, Chronos'' Pendant, Dreamer''s
    Idol, Freya''s Tears, Bragi''s Harp, Helm of Radiance, Gem of Focus, Ancient Signet,
    Amanita Charm, Ethereal Staff, Shield of the Phoenix, Rod of Asclepius, Kinetic
    Cuirass, Totem of Death, Bracer of The Abyss, Screeching Gargoyle, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.55
      pick: 0.33
      fit: 0.19
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.66
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.54
      pick: 0.3
      fit: 0.47
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.57
      pick: 0.48
      fit: 0.57
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.76
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
  - Kinetic Cuirass
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
    Guard, Breastplate of Valor, Spear of the Magus, Blood-Bound Book, Shifter''s
    Shield, Lifebinder, Chandra''s Grace, Phoenix Feather, Helm of Radiance, Yogi''s
    Necklace, Bancroft''s Talon, Sphere of Negation, Spectral Armor, Mantle Of Discord,
    Stone of Binding, Erosion, Eye of Providence.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.43
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.54
      pick: 0.3
      fit: 0.34
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.48
      fit: 0.44
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.74
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.83
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
    Dreamer''s Idol, Nimble Ring, Screeching Gargoyle, Death Metal, Stone of Binding,
    Genji''s Guard, Breastplate of Valor, Chronos'' Pendant, Helm of Radiance, Ancient
    Signet, Ethereal Staff, Bracer of The Abyss, Rod of Asclepius, Freya''s Tears,
    Gem of Focus, Amanita Charm, Kinetic Cuirass, Jade Scepter, Void Shield, Wish-Granting
    Pearl.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.81
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.69
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.19
      fit: 0.69
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.54
      pick: 0.3
      fit: 0.69
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.57
      pick: 0.48
      fit: 0.79
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.91
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
    Harp, Bracer of The Abyss, Genji''s Guard, Breastplate of Valor, Helm of Radiance,
    Doom Orb, The Cosmic Horror, Chronos'' Pendant, Amanita Charm, Freya''s Tears,
    Ancient Signet, Kinetic Cuirass, Ethereal Staff, Blood-Bound Book, Dreamer''s
    Idol, Rod of Asclepius, Bancroft''s Talon, Eye of Providence, Jade Scepter, Gem
    of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.54
      pick: 0.3
      fit: 0.32
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.48
      fit: 0.42
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.66
      pick: 0.22
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
  - Genji's Guard
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Gluttonous Grimoire, Chronos'' Pendant, Nimble Ring, Shield of
    the Phoenix, Spear of the Magus, Gem of Focus, Screeching Gargoyle, Death Metal,
    Totem of Death, Chandra''s Grace, Doom Orb, The Cosmic Horror, Amanita Charm,
    Helm of Radiance, Kinetic Cuirass, Eye of Erebus, Dreamer''s Idol, Bragi''s Harp,
    Ancient Signet, Ethereal Staff, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.4
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.71
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.54
      pick: 0.3
      fit: 0.31
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.48
      fit: 0.41
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.81
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
    Helm of Radiance, Genji''s Guard, Bracer of The Abyss, Breastplate of Valor, Ancient
    Signet, Ethereal Staff, Gem of Focus, Rod of Asclepius, Bragi''s Harp, Totem of
    Death, Freya''s Tears, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Amanita
    Charm, Bancroft''s Talon.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.34
      fit: 0.76
    Doom Orb:
      total: 0.51
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.6
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.54
      pick: 0.3
      fit: 0.6
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.57
      pick: 0.48
      fit: 0.7
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.66
      pick: 0.22
      fit: 0.86
  starter: *id001
---
