---
type: smite-build
god: Poseidon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Trident
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.49
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.57
    win_rate: 0.56
    alternates:
    - name: Book of Thoth
      pick_rate: 0.13
      win_rate: 0.6
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.48
  - name: The World Stone
    pick_rate: 0.24
    win_rate: 0.55
    alternates:
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.52
  - name: Nimble Ring
    pick_rate: 0.23
    win_rate: 0.53
    alternates:
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.48
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.56
  - name: Rod of Tahuti
    pick_rate: 0.28
    win_rate: 0.51
    alternates:
    - name: Nimble Ring
      pick_rate: 0.17
      win_rate: 0.61
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.52
  - name: Obsidian Shard
    pick_rate: 0.2
    win_rate: 0.59
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.65
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.4
  - name: Evil Eye
    pick_rate: 0.12
    win_rate: 0.54
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.83
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.63
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.29
    win_rate: 0.6
  - name: Sands Of Time
    pick_rate: 0.2
    win_rate: 0.49
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/poseidon/
  last_verified: '2026-08-21'
  god_win_rate: 0.5477239353891337
  god_matches_won: 373
  god_matches_played: 681
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
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
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
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom Orb, The Cosmic
    Horror, Dreamer''s Idol, Death Metal, Helm of Radiance, Genji''s Guard, Breastplate
    of Valor, Ancient Signet, Ethereal Staff, Gem of Focus, Rod of Asclepius, Totem
    of Death, Freya''s Tears, Chronos'' Pendant, Jade Scepter, Wish-Granting Pearl,
    Blood-Bound Book, Bracer of The Abyss, Amanita Charm, Bancroft''s Talon, Alchemist
    Coat.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.58
      pick: 0.2
      fit: 0.32
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.36
      fit: 0.32
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.56
      pick: 0.57
      fit: 0.76
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.51
      pick: 0.47
      fit: 0.6
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.59
      pick: 0.43
      fit: 0.7
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Death Metal, Gluttonous Grimoire, Spear of the Magus, Genji''s Guard, Breastplate
    of Valor, Doom Orb, Ancient Signet, Helm of Radiance, The Cosmic Horror, Bragi''s
    Harp, Wish-Granting Pearl, Dreamer''s Idol, Ethereal Staff, Rod of Asclepius,
    Freya''s Tears, Gem of Focus, Bancroft''s Talon, Amanita Charm, Triton''s Conch,
    Jade Scepter, Kinetic Cuirass, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.58
      pick: 0.2
      fit: 0.33
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.21
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.56
      pick: 0.57
      fit: 0.53
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.33
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.51
      pick: 0.47
      fit: 0.49
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.59
      pick: 0.43
      fit: 0.5
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
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Death Metal, Genji''s
    Guard, Breastplate of Valor, Doom Orb, The Cosmic Horror, Dreamer''s Idol, Freya''s
    Tears, Helm of Radiance, Gem of Focus, Ancient Signet, Amanita Charm, Ethereal
    Staff, Shield of the Phoenix, Bragi''s Harp, Rod of Asclepius, Kinetic Cuirass,
    Totem of Death, Chronos'' Pendant, Screeching Gargoyle, Jade Scepter, Wish-Granting
    Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.36
      fit: 0.19
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.38
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.56
      pick: 0.57
      fit: 0.66
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.51
      pick: 0.47
      fit: 0.47
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.59
      pick: 0.43
      fit: 0.57
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
  - Kinetic Cuirass
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
    Breastplate of Valor, Spear of the Magus, Blood-Bound Book, Shifter''s Shield,
    Lifebinder, Chandra''s Grace, Phoenix Feather, Helm of Radiance, Yogi''s Necklace,
    Bancroft''s Talon, Sphere of Negation, Spectral Armor, Mantle Of Discord, Stone
    of Binding, Erosion, Eye of Providence.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.56
      pick: 0.57
      fit: 0.43
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.51
      pick: 0.47
      fit: 0.34
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.59
      pick: 0.43
      fit: 0.44
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.74
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.83
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
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom Orb, The
    Cosmic Horror, Dreamer''s Idol, Screeching Gargoyle, Death Metal, Stone of Binding,
    Genji''s Guard, Breastplate of Valor, Helm of Radiance, Ancient Signet, Ethereal
    Staff, Rod of Asclepius, Freya''s Tears, Gem of Focus, Amanita Charm, Kinetic
    Cuirass, Jade Scepter, Void Shield, Wish-Granting Pearl, Blood-Bound Book, Chronos''
    Pendant.'
  slot_scores:
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.36
      fit: 0.24
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.56
      pick: 0.57
      fit: 0.82
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.7
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.55
      pick: 0.33
      fit: 0.7
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.51
      pick: 0.47
      fit: 0.7
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.59
      pick: 0.43
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Death Metal, Bragi''s
    Harp, Bracer of The Abyss, Genji''s Guard, Breastplate of Valor, Helm of Radiance,
    Doom Orb, The Cosmic Horror, Amanita Charm, Freya''s Tears, Ancient Signet, Kinetic
    Cuirass, Ethereal Staff, Blood-Bound Book, Dreamer''s Idol, Rod of Asclepius,
    Bancroft''s Talon, Eye of Providence, Jade Scepter, Gem of Focus, Chronos'' Pendant.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.36
      fit: 0.48
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.55
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.57
      fit: 0.4
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.51
      pick: 0.47
      fit: 0.32
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.59
      pick: 0.43
      fit: 0.42
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
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Breastplate
    of Valor, Freya''s Tears, Gluttonous Grimoire, Shield of the Phoenix, Spear of
    the Magus, Gem of Focus, Screeching Gargoyle, Death Metal, Totem of Death, Chronos''
    Pendant, Chandra''s Grace, Doom Orb, The Cosmic Horror, Amanita Charm, Helm of
    Radiance, Kinetic Cuirass, Eye of Erebus, Dreamer''s Idol, Ancient Signet, Ethereal
    Staff, Rod of Asclepius, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.41
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.56
      pick: 0.57
      fit: 0.72
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.51
      pick: 0.47
      fit: 0.31
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.59
      pick: 0.43
      fit: 0.41
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Death Metal,
    The Crusher, Gluttonous Grimoire, Spear of the Magus, Tyrfing, Heartseeker, Golden
    Blade, Hydra''s Lament, The Reaper, Bragi''s Harp, Tekko-Kagi, Berserker''s Shield,
    Runeforged Hammer, Lernaean Bow, Silverbranch Bow, Titan''s Bane, Genji''s Guard,
    Riptalon, Breastplate of Valor, Doom Orb, The Cosmic Horror, Helm of Radiance,
    Dreamer''s Idol, Shield Splitter, Arondight, Pendulum Blade, Ancient Signet, Freya''s
    Tears, Amanita Charm, Ethereal Staff, Dominance, Avenging Blade, Bracer of The
    Abyss, Rod of Asclepius, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.58
      pick: 0.2
      fit: 0.19
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.55
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.27
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.36
      fit: 0.3
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.56
      pick: 0.57
      fit: 0.47
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.51
      pick: 0.47
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Death Metal
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Gluttonous
    Grimoire, Death Metal, The Crusher, Spear of the Magus, Heartseeker, The Reaper,
    Hydra''s Lament, Doom Orb, The Cosmic Horror, Runeforged Hammer, Titan''s Bane,
    Tyrfing, Bragi''s Harp, Dreamer''s Idol, Genji''s Guard, Helm of Radiance, Breastplate
    of Valor, Golden Blade, Tekko-Kagi, Silverbranch Bow, Ancient Signet, Ethereal
    Staff, Berserker''s Shield, Rod of Asclepius, Riptalon, Pendulum Blade, Lernaean
    Bow, Freya''s Tears, Arondight, Triton''s Conch, Gem of Focus, Shield Splitter,
    Amanita Charm, Avatar''s Parashu, Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.58
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.56
      pick: 0.57
      fit: 0.58
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.51
      pick: 0.47
      fit: 0.47
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.59
      pick: 0.43
      fit: 0.57
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.68
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
    Orb, The Cosmic Horror, Dreamer''s Idol, Chronos'' Pendant, Death Metal, Helm
    of Radiance, Genji''s Guard, Breastplate of Valor, Ancient Signet, Ethereal Staff,
    Gem of Focus, Rod of Asclepius, Totem of Death, Freya''s Tears, Jade Scepter,
    Wish-Granting Pearl, Blood-Bound Book, Bracer of The Abyss, Amanita Charm, Bancroft''s
    Talon, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.56
      pick: 0.57
      fit: 0.76
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.6
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.51
      pick: 0.47
      fit: 0.6
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.59
      pick: 0.43
      fit: 0.7
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.86
  starter: *id001
---
