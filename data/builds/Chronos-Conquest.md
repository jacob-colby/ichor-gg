---
type: smite-build
god: Chronos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Relativity
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.51
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.45
    win_rate: 0.51
    alternates:
    - name: Book of Thoth
      pick_rate: 0.29
      win_rate: 0.51
    - name: Polynomicon
      pick_rate: 0.04
      win_rate: 0.47
  - name: Polynomicon
    pick_rate: 0.44
    win_rate: 0.52
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.54
    - name: Book of Thoth
      pick_rate: 0.07
      win_rate: 0.48
  - name: Rod of Tahuti
    pick_rate: 0.37
    win_rate: 0.48
    alternates:
    - name: Nimble Ring
      pick_rate: 0.28
      win_rate: 0.57
    - name: Polynomicon
      pick_rate: 0.1
      win_rate: 0.48
  - name: Nimble Ring
    pick_rate: 0.35
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.25
      win_rate: 0.61
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.31
  - name: Obsidian Shard
    pick_rate: 0.19
    win_rate: 0.57
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.11
      win_rate: 0.61
    - name: Nimble Ring
      pick_rate: 0.09
      win_rate: 0.45
  - name: Blinking Abyss
    pick_rate: 0.14
    win_rate: 0.54
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.71
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.54
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.51
    win_rate: 0.56
  - name: Sands Of Time
    pick_rate: 0.21
    win_rate: 0.38
  - name: War Flag
    pick_rate: 0.09
    win_rate: 0.14
  source_url: https://smitebrain.com/gods/chronos/
  last_verified: '2026-11-02'
  god_win_rate: 0.5074626865671642
  god_matches_won: 374
  god_matches_played: 737
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Bracer of The Abyss
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
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bracer of The Abyss,
    Blood-Bound Book, Eros'' Bow, Doom Orb, The World Stone, Chronos'' Pendant, Dreamer''s
    Idol, Bancroft''s Talon, Heartwood Charm, Gem of Focus, The Cosmic Horror, Ancient
    Signet, Typhon’s Heart, Soul Reaver, Totem of Death, Bragi''s Harp, Divine Ruin,
    Jade Scepter, Helm of Radiance, Ethereal Staff, Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.56
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.44
    Nimble Ring:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.58
      fit: 0.68
    Spear of the Magus:
      total: 0.49
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.44
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.54
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Polynomicon
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Doom Orb
  - Obsidian Shard
  flex_slots:
  - Polynomicon
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Sundering Echo, Bragi''s Harp, Doom Orb, Spear of the
    Magus, The World Stone, Death Metal, Blood-Bound Book, Bracer of The Abyss, Chronos''
    Pendant, Bancroft''s Talon, Heartwood Charm, Ancient Signet, Eros'' Bow, Dreamer''s
    Idol, Gem of Focus, Soul Reaver, The Cosmic Horror, Typhon’s Heart, Totem of Death,
    Divine Ruin, Genji''s Guard, Jade Scepter.'
  slot_scores:
    Polynomicon:
      total: 0.48
      efficiency: 0.47
      win: 0.52
      pick: 0.6
      fit: 0.38
    Spear of Desolation:
      total: 0.51
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.45
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.42
    Nimble Ring:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.58
      fit: 0.48
    Doom Orb:
      total: 0.47
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.42
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.44
  community_ordered:
  - Polynomicon
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Sundering Echo
  - Rod of Tahuti
  - Nimble Ring
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Sundering Echo
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
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Sundering Echo, Doom Orb,
    Bragi''s Harp, The World Stone, Blood-Bound Book, Chronos'' Pendant, Bracer of
    The Abyss, Death Metal, Dreamer''s Idol, Eros'' Bow, Heartwood Charm, Gem of Focus,
    The Cosmic Horror, Bancroft''s Talon, Ancient Signet, Totem of Death, Typhon’s
    Heart, Soul Reaver, Genji''s Guard, Damaru, Divine Ruin.'
  slot_scores:
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.56
    Sundering Echo:
      total: 0.47
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.32
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.4
    Nimble Ring:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.58
      fit: 0.44
    Spear of the Magus:
      total: 0.48
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.4
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
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
  - Spear of Desolation
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Blood-Bound Book, Shield
    of the Phoenix, Kinetic Cuirass, Genji''s Guard, Ethereal Staff, Yogi''s Necklace,
    Bancroft''s Talon, Eros'' Bow, Phoenix Feather, Breastplate of Valor, Freya''s
    Tears, Chandra''s Grace, Rod of Asclepius, Sphere of Negation, Helm of Radiance,
    Oni Hunter''s Garb, Spear of the Magus, Helm of Darkness, Erosion, Eye of Providence,
    Midgardian Mail, Draconic Scale, Regrowth Striders.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.5
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.34
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.27
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.55
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Nimble Ring
  - Spear of the Magus
  - Obsidian Shard
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
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom Orb, The
    World Stone, Dreamer''s Idol, The Cosmic Horror, Blood-Bound Book, Bracer of The
    Abyss, Eros'' Bow, Chronos'' Pendant, Bancroft''s Talon, Heartwood Charm, Gem
    of Focus, Ancient Signet, Typhon’s Heart, Soul Reaver, Totem of Death, Divine
    Ruin, Screeching Gargoyle, Jade Scepter, Bragi''s Harp, Helm of Radiance, Ethereal
    Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.66
    Doom Orb:
      total: 0.49
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.57
    Nimble Ring:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.58
      fit: 0.53
    Spear of the Magus:
      total: 0.51
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.57
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.67
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Bragi's Harp
  - Rod of Tahuti
  - Nimble Ring
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Bragi''s Harp, Sundering Echo, Spear
    of the Magus, Blood-Bound Book, Bracer of The Abyss, Doom Orb, Eros'' Bow, The
    World Stone, Death Metal, Chronos'' Pendant, Bancroft''s Talon, Dreamer''s Idol,
    Ancient Signet, Heartwood Charm, Gem of Focus, The Cosmic Horror, Typhon’s Heart,
    Soul Reaver, Totem of Death, Divine Ruin, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.41
    Bragi's Harp:
      total: 0.47
      efficiency: 0.41
      win: 0.52
      pick: 0.0
      fit: 0.64
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.3
    Nimble Ring:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.58
      fit: 0.49
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.4
    Soul Gem:
      total: 0.51
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, Chronos''
    Pendant, Heartwood Charm, Gem of Focus, Sundering Echo, Spear of the Magus, Blood-Bound
    Book, Bragi''s Harp, Bracer of The Abyss, Doom Orb, Totem of Death, Genji''s Guard,
    The World Stone, Eros'' Bow, Damaru, Death Metal, Breastplate of Valor, Dreamer''s
    Idol, Bancroft''s Talon, Chandra''s Grace, Ancient Signet, The Cosmic Horror,
    Typhon’s Heart.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.48
      win: 0.51
      pick: 0.29
      fit: 0.1
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.59
    Chronos' Pendant:
      total: 0.48
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.24
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.34
    Soul Gem:
      total: 0.54
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Tekko-Kagi
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire,
    The Reaper, Tekko-Kagi, Sundering Echo, Titan''s Bane, Tyrfing, Hydra''s Lament,
    Death Metal, Bragi''s Harp, Heartseeker, Spear of the Magus, Silverbranch Bow,
    The Crusher, Riptalon, Golden Blade, Lernaean Bow, Blood-Bound Book, Doom Orb,
    The World Stone, Arondight, Dominance, Chronos'' Pendant, Toxic Blade, Pendulum
    Blade, Dreamer''s Idol, Bracer of The Abyss, Bloodforge, Transcendence, Bancroft''s
    Talon, The Cosmic Horror, Runeforged Hammer, Avatar''s Parashu, Heartwood Charm,
    Gem of Focus, Ancient Signet.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.49
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.39
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.49
    Soul Gem:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Tekko-Kagi
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Tekko-Kagi,
    Gluttonous Grimoire, Tyrfing, Silverbranch Bow, Sundering Echo, The Reaper, Bragi''s
    Harp, Riptalon, Titan''s Bane, Spear of the Magus, Lernaean Bow, Golden Blade,
    Hydra''s Lament, Blood-Bound Book, Death Metal, Toxic Blade, Doom Orb, Bracer
    of The Abyss, The World Stone, Heartseeker, The Crusher, Dominance, Chronos''
    Pendant, Eros'' Bow, Dreamer''s Idol, Arondight, Bancroft''s Talon, Qin''s Blade,
    Heartwood Charm, The Cosmic Horror, Ancient Signet, Gem of Focus, Pendulum Blade,
    Transcendence, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.47
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.39
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.49
    Soul Gem:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Bracer of The Abyss
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
    Underrated for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bracer
    of The Abyss, Blood-Bound Book, Eros'' Bow, Doom Orb, The World Stone, Chronos''
    Pendant, Dreamer''s Idol, Bancroft''s Talon, Heartwood Charm, Gem of Focus, The
    Cosmic Horror, Ancient Signet, Typhon’s Heart, Soul Reaver, Totem of Death, Bragi''s
    Harp, Divine Ruin, Jade Scepter, Helm of Radiance, Ethereal Staff, Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.56
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.44
    Nimble Ring:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.58
      fit: 0.68
    Spear of the Magus:
      total: 0.49
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.44
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.54
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Eros'' Bow, Gluttonous Grimoire, Genji''s Guard, Amanita Charm,
    Void Stone, Spear of the Magus, Bracer of The Abyss, Blood-Bound Book, Doublet
    of Binding, Chronos'' Pendant, Screeching Gargoyle, Rod of Asclepius, Doom Orb,
    The World Stone, Oni Hunter''s Garb, Heartwood Charm, Gem of Focus, Jade Scepter,
    Dreamer''s Idol, Bancroft''s Talon, Lifebinder, Ethereal Staff, Erosion, Ancient
    Signet, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.25
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.46
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.29
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.39
    Eros' Bow:
      total: 0.52
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.57
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Polynomicon
  - Rod of Tahuti
  - Obsidian Shard
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Polynomicon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Eros'' Bow, Gluttonous Grimoire, Genji''s Guard, Triton''s Conch, Sundering
    Echo, Amanita Charm, Bragi''s Harp, Spear of the Magus, Doom Orb, Blood-Bound
    Book, The World Stone, Death Metal, Void Stone, Rod of Asclepius, Bracer of The
    Abyss, Chronos'' Pendant, Doublet of Binding, Bancroft''s Talon, Heartwood Charm,
    Ancient Signet, Oni Hunter''s Garb, Jade Scepter, Wish-Granting Pearl, Dreamer''s
    Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.21
    Polynomicon:
      total: 0.48
      efficiency: 0.47
      win: 0.52
      pick: 0.6
      fit: 0.35
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.37
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.41
    Eros' Bow:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.71
    Soul Gem:
      total: 0.55
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Polynomicon
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Eros'' Bow, Genji''s Guard, Amanita Charm,
    Spear of the Magus, Triton''s Conch, Sundering Echo, Doom Orb, Void Stone, The
    World Stone, Bragi''s Harp, Blood-Bound Book, Chronos'' Pendant, Rod of Asclepius,
    Doublet of Binding, Bracer of The Abyss, Death Metal, Screeching Gargoyle, Dreamer''s
    Idol, Heartwood Charm, Gem of Focus, Jade Scepter, Oni Hunter''s Garb, The Cosmic
    Horror, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.2
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.49
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.35
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.45
    Eros' Bow:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.57
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: bruiser
  slot_order:
  - Eros' Bow
  - Rod of Tahuti
  - Amanita Charm
  - Obsidian Shard
  - Erosion
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Eros'' Bow, Gluttonous Grimoire, Shield of
    the Phoenix, Rod of Asclepius, Erosion, Genji''s Guard, Blood-Bound Book, Umbral
    Link, Kinetic Cuirass, Void Stone, Stampede, Void Shield, Lifebinder, Yogi''s
    Necklace, Ethereal Staff, Breastplate of Valor, Spectral Armor, Freya''s Tears,
    Phoenix Feather, Chandra''s Grace, Doublet of Binding, Bancroft''s Talon, Oni
    Hunter''s Garb, Regrowth Striders.'
  slot_scores:
    Eros' Bow:
      total: 0.52
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.74
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.21
    Amanita Charm:
      total: 0.6
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.99
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.31
    Erosion:
      total: 0.5
      efficiency: 0.48
      win: 0.52
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.57
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Void Stone
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Void Stone, Eros'' Bow, Screeching
    Gargoyle, Genji''s Guard, Spear of the Magus, Amanita Charm, Doom Orb, The World
    Stone, Dreamer''s Idol, Doublet of Binding, Blood-Bound Book, The Cosmic Horror,
    Rod of Asclepius, Bracer of The Abyss, Chronos'' Pendant, Oni Hunter''s Garb,
    Jade Scepter, Heartwood Charm, Gem of Focus, Bancroft''s Talon, Lifebinder, Ancient
    Signet, Erosion.'
  slot_scores:
    Void Stone:
      total: 0.51
      efficiency: 0.44
      win: 0.52
      pick: 0.0
      fit: 0.83
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.57
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.43
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.53
    Eros' Bow:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.57
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bragi's Harp
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Eros'' Bow, Gluttonous Grimoire, Genji''s Guard, Amanita Charm,
    Void Stone, Triton''s Conch, Sundering Echo, Bragi''s Harp, Doublet of Binding,
    Spear of the Magus, Blood-Bound Book, Bracer of The Abyss, Rod of Asclepius, Screeching
    Gargoyle, Chronos'' Pendant, Doom Orb, The World Stone, Oni Hunter''s Garb, Death
    Metal, Jade Scepter, Heartwood Charm, Gem of Focus, Bancroft''s Talon, Dreamer''s
    Idol, Ancient Signet.'
  slot_scores:
    Bragi's Harp:
      total: 0.45
      efficiency: 0.41
      win: 0.52
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.21
    Nimble Ring:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.58
      fit: 0.38
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.31
    Eros' Bow:
      total: 0.5
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.67
    Soul Gem:
      total: 0.54
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Eros'' Bow,
    Gluttonous Grimoire, Amanita Charm, Screeching Gargoyle, Chronos'' Pendant, Void
    Stone, Heartwood Charm, Gem of Focus, Triton''s Conch, Doublet of Binding, Sundering
    Echo, Spear of the Magus, Blood-Bound Book, Rod of Asclepius, Bragi''s Harp, Chandra''s
    Grace, Bracer of The Abyss, Doom Orb, The World Stone, Oni Hunter''s Garb, Freya''s
    Tears, Totem of Death, Eye of Erebus, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.36
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.52
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.21
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.31
    Eros' Bow:
      total: 0.5
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.57
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.99
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Tekko-Kagi
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Gluttonous Grimoire,
    The Reaper, Tekko-Kagi, Genji''s Guard, Eros'' Bow, Golden Blade, Titan''s Bane,
    Hydra''s Lament, Sanguine Lash, Tyrfing, Triton''s Conch, Pharaoh''s Curse, Amanita
    Charm, Sundering Echo, Runeforged Hammer, Shogun''s Ofuda, Heartseeker, Silverbranch
    Bow, The Crusher, Toxic Blade, Riptalon, Lernaean Bow, Void Stone, Arondight,
    Spear of the Magus, Death Metal, Bragi''s Harp, Doublet of Binding, Blood-Bound
    Book, Pendulum Blade, Avenging Blade, Doom Orb, Dominance, Rod of Asclepius, Shield
    Splitter, Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.51
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.41
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.28
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.38
    Soul Gem:
      total: 0.56
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.9
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Eros''
    Bow, Gluttonous Grimoire, Pharaoh''s Curse, Tekko-Kagi, Genji''s Guard, Golden
    Blade, Shogun''s Ofuda, Tyrfing, Triton''s Conch, Sundering Echo, Amanita Charm,
    Silverbranch Bow, The Reaper, Titan''s Bane, Hydra''s Lament, Toxic Blade, Bragi''s
    Harp, Riptalon, Sanguine Lash, Spear of the Magus, Lernaean Bow, Blood-Bound Book,
    Runeforged Hammer, Void Stone, Death Metal, Rod of Asclepius, Doom Orb, Chronos''
    Pendant, Bracer of The Abyss, The World Stone, Heartseeker, The Crusher, Doublet
    of Binding, Dominance, Berserker''s Shield, Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.51
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.44
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.32
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.42
    Eros' Bow:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.56
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Eros'' Bow, Gluttonous Grimoire, Genji''s Guard,
    Amanita Charm, Void Stone, Spear of the Magus, Bracer of The Abyss, Blood-Bound
    Book, Doublet of Binding, Chronos'' Pendant, Screeching Gargoyle, Rod of Asclepius,
    Doom Orb, The World Stone, Oni Hunter''s Garb, Heartwood Charm, Gem of Focus,
    Jade Scepter, Dreamer''s Idol, Bancroft''s Talon, Lifebinder, Ethereal Staff,
    Erosion, Ancient Signet, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.25
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.51
      pick: 0.45
      fit: 0.46
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.81
      win: 0.48
      pick: 0.58
      fit: 0.29
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.41
      fit: 0.39
    Eros' Bow:
      total: 0.52
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.57
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
---
