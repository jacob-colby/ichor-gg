---
type: smite-build
god: Nut
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cosmos
  aspect_pick_rate: 0.05
  aspect_win_rate: 1.0
  slot_order:
  - name: Tyrfing
    pick_rate: 0.56
    win_rate: 0.49
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.35
      win_rate: 0.64
    - name: Bragi's Harp
      pick_rate: 0.02
      win_rate: 1.0
  - name: Bragi's Harp
    pick_rate: 0.49
    win_rate: 0.45
    alternates:
    - name: Staff of Myrddin
      pick_rate: 0.24
      win_rate: 0.73
    - name: The World Stone
      pick_rate: 0.06
      win_rate: 0.5
  - name: Barbed Carver
    pick_rate: 0.19
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.3
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 1.0
  - name: The Executioner
    pick_rate: 0.29
    win_rate: 0.47
    alternates:
    - name: Barbed Carver
      pick_rate: 0.1
      win_rate: 0.33
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.67
  - name: Qin's Blade
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.8
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.8
  - name: Riptalon
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Void Shard
      pick_rate: 0.09
      win_rate: 0.33
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.43
    win_rate: 0.52
  - name: Bluestone Brooch
    pick_rate: 0.13
    win_rate: 0.88
  - name: Archmage's Gem
    pick_rate: 0.11
    win_rate: 0.86
  source_url: https://smitebrain.com/gods/nut/
  last_verified: '2026-08-26'
  god_win_rate: 0.5873015873015873
  god_matches_won: 37
  god_matches_played: 63
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Staff of Myrddin
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Staff of Myrddin
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear
    of the Magus, Tekko-Kagi, The Reaper, Lernaean Bow, Bracer of The Abyss, Heartseeker,
    Hydra''s Lament, The World Stone, Doom Orb, Chronos'' Pendant, Dreamer''s Idol,
    Dominance, Death Metal, Titan''s Bane, Blood-Bound Book, The Crusher, Ancient
    Signet, Bancroft''s Talon, Gem of Focus, Arondight, Pendulum Blade, Silverbranch
    Bow, The Cosmic Horror, Avatar''s Parashu, Transcendence, Rod of Asclepius, Book
    of Thoth, Typhon’s Heart, Runeforged Hammer, Polynomicon, Berserker''s Shield,
    Totem of Death.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.48
    Staff of Myrddin:
      total: 0.51
      efficiency: 0.34
      win: 0.73
      pick: 0.33
      fit: 0.3
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 1.0
      pick: 0.17
      fit: 0.38
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.48
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire, Hydra''s Lament, Spear of
    the Magus, Heartseeker, Lernaean Bow, The Reaper, Tekko-Kagi, The World Stone,
    Doom Orb, Ancient Signet, Dominance, Bracer of The Abyss, Death Metal, Chronos''
    Pendant, Bancroft''s Talon, Titan''s Bane, The Crusher, Blood-Bound Book, Dreamer''s
    Idol, Transcendence, Arondight, Gem of Focus, Book of Thoth, Polynomicon, Pendulum
    Blade, Runeforged Hammer, Soul Reaver, Avatar''s Parashu, Rod of Asclepius, The
    Cosmic Horror, Typhon’s Heart, Totem of Death, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.49
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.45
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 1.0
      pick: 0.17
      fit: 0.42
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Staff of Myrddin
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Staff of Myrddin
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Soul Gem, Nimble Ring, Gluttonous Grimoire, Spear of the
    Magus, The Reaper, Tekko-Kagi, Heartseeker, Hydra''s Lament, Lernaean Bow, The
    World Stone, Doom Orb, Titan''s Bane, Chronos'' Pendant, The Crusher, Bracer of
    The Abyss, Dreamer''s Idol, Pendulum Blade, Death Metal, Dominance, Ancient Signet,
    Arondight, Blood-Bound Book, Gem of Focus, Avatar''s Parashu, The Cosmic Horror,
    Bancroft''s Talon, Silverbranch Bow, Transcendence, Runeforged Hammer, Rod of
    Asclepius, Book of Thoth, Totem of Death, Typhon’s Heart, Polynomicon, Avenging
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.56
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.56
    Staff of Myrddin:
      total: 0.51
      efficiency: 0.34
      win: 0.73
      pick: 0.33
      fit: 0.32
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 1.0
      pick: 0.17
      fit: 0.4
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Nimble Ring
  - Shell of Rebuke
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Berserker''s Shield, Jotunn''s Revenge, Gluttonous
    Grimoire, Rod of Asclepius, Nimble Ring, The Reaper, Shield of the Phoenix, Kinetic
    Cuirass, Blood-Bound Book, Ethereal Staff, Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Bancroft''s Talon, Spear of the Magus, Runeforged Hammer, Yogi''s Necklace,
    Lifebinder, Helm of Radiance, Pharaoh''s Curse, Shield Splitter, Sphere of Negation,
    Lernaean Bow, Shogun''s Ofuda, Chandra''s Grace, Phoenix Feather, Eye of the Storm,
    Hydra''s Lament, Tekko-Kagi, Erosion, Eye of Providence, Jade Scepter, Heartseeker,
    Bracer of The Abyss.'
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.18
      fit: 0.21
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.32
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.17
      fit: 0.25
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.35
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire, Nimble Ring, Spear
    of the Magus, The Reaper, Tekko-Kagi, Heartseeker, The World Stone, Doom Orb,
    Dreamer''s Idol, Titan''s Bane, The Crusher, Lernaean Bow, Bracer of The Abyss,
    Hydra''s Lament, Avenging Blade, Pendulum Blade, Chronos'' Pendant, The Cosmic
    Horror, Silverbranch Bow, Avatar''s Parashu, Ancient Signet, Blood-Bound Book,
    Death Metal, Dominance, Bancroft''s Talon, Gem of Focus, Arondight, Oath-Sworn
    Spear, Transcendence, Rod of Asclepius, Book of Thoth, Runeforged Hammer, Typhon’s
    Heart.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.55
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.57
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.17
      fit: 0.49
    Obsidian Shard:
      total: 0.65
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Spear of Desolation
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire, Silverbranch
    Bow, Spear of the Magus, Lernaean Bow, Tekko-Kagi, The Reaper, Golden Blade, Bracer
    of The Abyss, Hydra''s Lament, Heartseeker, Toxic Blade, The World Stone, Doom
    Orb, Chronos'' Pendant, Dominance, Ancient Signet, Dreamer''s Idol, Blood-Bound
    Book, Death Metal, Titan''s Bane, The Crusher, Bancroft''s Talon, Gem of Focus,
    Arondight, Transcendence, Sun Beam Bow, Pendulum Blade, The Cosmic Horror, Rod
    of Asclepius, Book of Thoth, Runeforged Hammer, Avatar''s Parashu.'
  slot_scores:
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.49
      pick: 0.56
      fit: 0.63
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.39
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.43
      fit: 0.63
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.17
      fit: 0.31
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Staff of Myrddin
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Staff of Myrddin
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Nimble
    Ring, Hydra''s Lament, Gluttonous Grimoire, Chronos'' Pendant, Spear of the Magus,
    Lernaean Bow, The Reaper, Tekko-Kagi, Arondight, Gem of Focus, Pendulum Blade,
    Heartseeker, Bracer of The Abyss, The World Stone, Doom Orb, Totem of Death, Dominance,
    Titan''s Bane, The Crusher, Ancient Signet, Dreamer''s Idol, Blood-Bound Book,
    Breastplate of Valor, Death Metal, Genji''s Guard, Bancroft''s Talon, Silverbranch
    Bow, Transcendence, Avatar''s Parashu, Runeforged Hammer, The Cosmic Horror, Berserker''s
    Shield, Rod of Asclepius, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.6
    Staff of Myrddin:
      total: 0.53
      efficiency: 0.34
      win: 0.73
      pick: 0.33
      fit: 0.44
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.17
      fit: 0.26
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.36
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Gluttonous
    Grimoire, Spear of the Magus, Tekko-Kagi, The Reaper, Lernaean Bow, Bracer of
    The Abyss, Heartseeker, Hydra''s Lament, Doom Orb, The World Stone, Chronos''
    Pendant, Dreamer''s Idol, Dominance, Death Metal, Titan''s Bane, Blood-Bound Book,
    The Crusher, Ancient Signet, Bancroft''s Talon, Gem of Focus, Arondight, Pendulum
    Blade, Silverbranch Bow, The Cosmic Horror, Avatar''s Parashu, Transcendence,
    Rod of Asclepius, Book of Thoth, Typhon’s Heart, Runeforged Hammer, Polynomicon,
    Berserker''s Shield, Totem of Death.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.64
      pick: 0.35
      fit: 0.48
    Spear of the Magus:
      total: 0.49
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 1.0
      pick: 0.17
      fit: 0.38
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.48
  starter: *id001
---
