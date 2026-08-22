---
type: smite-build
god: Sol
mode: Conquest
builds:
- source: community
  aspect: Aspect of Conflagration
  aspect_pick_rate: 0.58
  aspect_win_rate: 0.44
  slot_order:
  - name: Tyrfing
    pick_rate: 0.2
    win_rate: 0.48
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.44
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.46
  - name: Book of Thoth
    pick_rate: 0.15
    win_rate: 0.39
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.51
    - name: Gem of Focus
      pick_rate: 0.08
      win_rate: 0.62
  - name: Spear of Desolation
    pick_rate: 0.09
    win_rate: 0.47
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.51
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.58
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.55
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.4
    - name: Soul Gem
      pick_rate: 0.06
      win_rate: 0.44
  - name: Obsidian Shard
    pick_rate: 0.11
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.38
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.52
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.28
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.59
    - name: Manchu Bow
      pick_rate: 0.06
      win_rate: 0.47
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.19
    win_rate: 0.41
  - name: Conduit Gem
    pick_rate: 0.16
    win_rate: 0.42
  - name: Death's Embrace
    pick_rate: 0.1
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/sol/
  last_verified: '2026-08-22'
  god_win_rate: 0.4671201814058957
  god_matches_won: 206
  god_matches_played: 441
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
  - Nimble Ring
  - Gem of Focus
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Spear of the Magus
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Gem of Focus, Spear of Desolation,
    Spear of the Magus, Bracer of The Abyss, Doom Orb, The Cosmic Horror, Bragi''s
    Harp, The World Stone, Death Metal, Genji''s Guard, Breastplate of Valor, Chronos''
    Pendant, Dreamer''s Idol, Helm of Radiance, Blood-Bound Book, Ancient Signet,
    Ethereal Staff, Rod of Asclepius, Freya''s Tears, Bancroft''s Talon, Amanita Charm,
    Kinetic Cuirass, Jade Scepter, Wish-Granting Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.66
    Gem of Focus:
      total: 0.51
      efficiency: 0.5
      win: 0.62
      pick: 0.11
      fit: 0.36
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.47
      pick: 0.14
      fit: 0.58
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.55
      pick: 0.28
      fit: 0.46
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.24
      fit: 0.56
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Gem of Focus
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Nimble Ring, Gluttonous Grimoire, Gem of Focus, Death Metal, Spear of Desolation,
    Spear of the Magus, Bragi''s Harp, Genji''s Guard, Breastplate of Valor, Doom
    Orb, Ancient Signet, The World Stone, Bracer of The Abyss, Helm of Radiance, Chronos''
    Pendant, The Cosmic Horror, Bancroft''s Talon, Ethereal Staff, Freya''s Tears,
    Wish-Granting Pearl, Blood-Bound Book, Rod of Asclepius, Amanita Charm, Dreamer''s
    Idol, Kinetic Cuirass, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.18
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.18
    Gem of Focus:
      total: 0.51
      efficiency: 0.5
      win: 0.62
      pick: 0.11
      fit: 0.31
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.55
      pick: 0.28
      fit: 0.42
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.24
      fit: 0.44
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Gem of Focus
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Spear of the Magus
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
    god: Soul Gem, Gluttonous Grimoire, Nimble Ring, Gem of Focus, Spear of Desolation,
    Spear of the Magus, Death Metal, Genji''s Guard, Breastplate of Valor, Bragi''s
    Harp, Doom Orb, The Cosmic Horror, The World Stone, Chronos'' Pendant, Freya''s
    Tears, Bracer of The Abyss, Dreamer''s Idol, Helm of Radiance, Amanita Charm,
    Kinetic Cuirass, Ancient Signet, Ethereal Staff, Blood-Bound Book, Shield of the
    Phoenix, Rod of Asclepius, Screeching Gargoyle, Totem of Death.'
  slot_scores:
    Gem of Focus:
      total: 0.51
      efficiency: 0.5
      win: 0.62
      pick: 0.11
      fit: 0.32
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.47
      pick: 0.14
      fit: 0.56
    Spear of the Magus:
      total: 0.49
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.55
      pick: 0.28
      fit: 0.4
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.24
      fit: 0.5
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Gem of Focus
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
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix,
    Ethereal Staff, Nimble Ring, Rod of Asclepius, Kinetic Cuirass, Blood-Bound Book,
    Freya''s Tears, Genji''s Guard, Breastplate of Valor, Bancroft''s Talon, Spear
    of the Magus, Spear of Desolation, Chandra''s Grace, Shifter''s Shield, Lifebinder,
    Phoenix Feather, Yogi''s Necklace, Helm of Radiance, Sphere of Negation, Mantle
    Of Discord, Spectral Armor, Stone of Binding, Erosion, Death Metal.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.48
    Gem of Focus:
      total: 0.49
      efficiency: 0.5
      win: 0.62
      pick: 0.11
      fit: 0.22
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.55
      pick: 0.28
      fit: 0.28
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.24
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.83
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gem of Focus
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Gem of Focus
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
    for this god: Soul Gem, Gluttonous Grimoire, Nimble Ring, Spear of Desolation,
    Spear of the Magus, Doom Orb, The Cosmic Horror, The World Stone, Dreamer''s Idol,
    Screeching Gargoyle, Stone of Binding, Bracer of The Abyss, Genji''s Guard, Breastplate
    of Valor, Death Metal, Helm of Radiance, Bragi''s Harp, Chronos'' Pendant, Blood-Bound
    Book, Freya''s Tears, Ancient Signet, Amanita Charm, Ethereal Staff, Rod of Asclepius,
    Kinetic Cuirass, Void Shield, Bancroft''s Talon.'
  slot_scores:
    Gem of Focus:
      total: 0.5
      efficiency: 0.5
      win: 0.62
      pick: 0.11
      fit: 0.29
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.47
      pick: 0.14
      fit: 0.66
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.55
      pick: 0.28
      fit: 0.56
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.57
      pick: 0.24
      fit: 0.66
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.86
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
    this god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Gem of Focus, Spear of the
    Magus, Death Metal, Spear of Desolation, Bragi''s Harp, Bracer of The Abyss, Genji''s
    Guard, Breastplate of Valor, Helm of Radiance, Doom Orb, The Cosmic Horror, Amanita
    Charm, Chronos'' Pendant, The World Stone, Freya''s Tears, Kinetic Cuirass, Ancient
    Signet, Ethereal Staff, Blood-Bound Book, Dreamer''s Idol, Rod of Asclepius, Bancroft''s
    Talon, Eye of Providence, Jade Scepter.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
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
      total: 0.61
      efficiency: 0.86
      win: 0.55
      pick: 0.28
      fit: 0.31
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.24
      fit: 0.41
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Gem of Focus
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Gem of Focus, Nimble Ring,
    Spear of Desolation, Genji''s Guard, Breastplate of Valor, Gluttonous Grimoire,
    Freya''s Tears, Chronos'' Pendant, Spear of the Magus, Shield of the Phoenix,
    Death Metal, Screeching Gargoyle, Totem of Death, Bragi''s Harp, Bracer of The
    Abyss, Amanita Charm, Kinetic Cuirass, Doom Orb, Helm of Radiance, The Cosmic
    Horror, Chandra''s Grace, The World Stone, Ancient Signet, Dreamer''s Idol, Blood-Bound
    Book, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.34
    Gem of Focus:
      total: 0.53
      efficiency: 0.5
      win: 0.62
      pick: 0.11
      fit: 0.44
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.47
      pick: 0.14
      fit: 0.6
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.55
      pick: 0.28
      fit: 0.26
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.24
      fit: 0.36
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Crusher
  - Death Metal
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
    win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Gluttonous Grimoire,
    Nimble Ring, The Crusher, Death Metal, The Reaper, Golden Blade, Spear of Desolation,
    Spear of the Magus, Riptalon, Heartseeker, Hydra''s Lament, Bragi''s Harp, Tekko-Kagi,
    Silverbranch Bow, Lernaean Bow, Runeforged Hammer, Berserker''s Shield, Titan''s
    Bane, Genji''s Guard, Breastplate of Valor, Doom Orb, The Cosmic Horror, The World
    Stone, Toxic Blade, Helm of Radiance, Chronos'' Pendant, Pendulum Blade, Shield
    Splitter, Dreamer''s Idol, Arondight, Dominance, Blood-Bound Book, Avenging Blade,
    Avatar''s Parashu, Ancient Signet, Freya''s Tears, Ethereal Staff.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.0
      fit: 0.59
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.49
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.55
      pick: 0.28
      fit: 0.39
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.24
      fit: 0.49
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Gem of Focus
  - Tyrfing
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Nimble
    Ring, Gluttonous Grimoire, Riptalon, Death Metal, Golden Blade, The Crusher, Berserker''s
    Shield, Silverbranch Bow, Spear of the Magus, Spear of Desolation, Bragi''s Harp,
    Tekko-Kagi, The Reaper, Lernaean Bow, Heartseeker, Hydra''s Lament, Toxic Blade,
    Bracer of The Abyss, Runeforged Hammer, Genji''s Guard, Doom Orb, Breastplate
    of Valor, The Cosmic Horror, Helm of Radiance, The World Stone, Titan''s Bane,
    Chronos'' Pendant, Dominance, Dreamer''s Idol, Ancient Signet, Blood-Bound Book,
    Ethereal Staff, Rod of Asclepius, Amanita Charm, Freya''s Tears, Pharaoh''s Curse,
    Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.49
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.48
      pick: 0.2
      fit: 0.72
    Gem of Focus:
      total: 0.51
      efficiency: 0.5
      win: 0.62
      pick: 0.11
      fit: 0.3
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.55
      pick: 0.28
      fit: 0.38
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.24
      fit: 0.48
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of
    Desolation, Spear of the Magus, Bracer of The Abyss, Doom Orb, The Cosmic Horror,
    Bragi''s Harp, The World Stone, Death Metal, Genji''s Guard, Breastplate of Valor,
    Chronos'' Pendant, Dreamer''s Idol, Helm of Radiance, Blood-Bound Book, Ancient
    Signet, Ethereal Staff, Rod of Asclepius, Freya''s Tears, Bancroft''s Talon, Gem
    of Focus, Amanita Charm, Kinetic Cuirass, Jade Scepter, Wish-Granting Pearl.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.49
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.47
      pick: 0.14
      fit: 0.58
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.55
      pick: 0.28
      fit: 0.46
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.24
      fit: 0.56
  starter: *id001
---
