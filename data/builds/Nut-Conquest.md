---
type: smite-build
god: Nut
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cosmos
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.14
  slot_order:
  - name: Tyrfing
    pick_rate: 0.42
    win_rate: 0.66
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.56
    - name: Book of Thoth
      pick_rate: 0.06
      win_rate: 0.75
  - name: Bragi's Harp
    pick_rate: 0.36
    win_rate: 0.64
    alternates:
    - name: Staff of Myrddin
      pick_rate: 0.22
      win_rate: 0.53
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.56
  - name: Barbed Carver
    pick_rate: 0.25
    win_rate: 0.71
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.82
    - name: Avenging Blade
      pick_rate: 0.06
      win_rate: 0.75
  - name: The Executioner
    pick_rate: 0.18
    win_rate: 0.75
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.63
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.88
  - name: Avenging Blade
    pick_rate: 0.07
    win_rate: 1.0
    alternates:
    - name: The Executioner
      pick_rate: 0.09
      win_rate: 0.6
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.5
  - name: Bow
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.33
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 1.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.28
    win_rate: 0.79
  - name: Archmage's Gem
    pick_rate: 0.17
    win_rate: 0.75
  - name: Conduit Gem
    pick_rate: 0.13
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/nut/
  last_verified: '2026-09-09'
  god_win_rate: 0.5652173913043478
  god_matches_won: 39
  god_matches_played: 69
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Avenging Blade
  - Book of Thoth
  - Jotunn's Revenge
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear
    of the Magus, Tekko-Kagi, The Reaper, Lernaean Bow, Bracer of The Abyss, Heartseeker,
    Hydra''s Lament, Doom Orb, The World Stone, Chronos'' Pendant, Dreamer''s Idol,
    Dominance, Death Metal, Titan''s Bane, Blood-Bound Book, The Crusher, Ancient
    Signet, Book of Thoth, Bancroft''s Talon, Gem of Focus, Arondight, Pendulum Blade,
    Silverbranch Bow, The Cosmic Horror, Avatar''s Parashu, Transcendence, Rod of
    Asclepius, Typhon’s Heart, Runeforged Hammer, Polynomicon, Berserker''s Shield,
    Totem of Death.'
  slot_scores:
    Avenging Blade:
      total: 0.65
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.26
    Book of Thoth:
      total: 0.55
      efficiency: 0.51
      win: 0.75
      pick: 0.06
      fit: 0.19
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.82
      pick: 0.25
      fit: 0.38
    Riptalon:
      total: 0.69
      efficiency: 0.43
      win: 1.0
      pick: 0.28
      fit: 0.54
    Obsidian Shard:
      total: 0.67
      efficiency: 0.54
      win: 0.88
      pick: 0.2
      fit: 0.48
  community_ordered:
  - Avenging Blade
  - Book of Thoth
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Jotunn's Revenge
  - Hydra's Lament
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire, Hydra''s Lament, Spear of
    the Magus, Heartseeker, Lernaean Bow, The Reaper, Tekko-Kagi, Doom Orb, Ancient
    Signet, The World Stone, Dominance, Bracer of The Abyss, Death Metal, Book of
    Thoth, Chronos'' Pendant, Bancroft''s Talon, Titan''s Bane, The Crusher, Blood-Bound
    Book, Dreamer''s Idol, Transcendence, Arondight, Gem of Focus, Polynomicon, Pendulum
    Blade, Runeforged Hammer, Soul Reaver, Avatar''s Parashu, Rod of Asclepius, The
    Cosmic Horror, Typhon’s Heart, Totem of Death.'
  slot_scores:
    Avenging Blade:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.31
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.71
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.82
      pick: 0.25
      fit: 0.42
    Riptalon:
      total: 0.67
      efficiency: 0.43
      win: 1.0
      pick: 0.28
      fit: 0.4
    Obsidian Shard:
      total: 0.66
      efficiency: 0.54
      win: 0.88
      pick: 0.2
      fit: 0.44
  community_ordered:
  - Avenging Blade
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Avenging Blade
  - Book of Thoth
  - Jotunn's Revenge
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Avenging Blade
  - Book of Thoth
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Soul Gem, Nimble Ring, Gluttonous Grimoire, Spear of the
    Magus, The Reaper, Tekko-Kagi, Heartseeker, Hydra''s Lament, Lernaean Bow, Doom
    Orb, The World Stone, Titan''s Bane, Chronos'' Pendant, The Crusher, Bracer of
    The Abyss, Dreamer''s Idol, Pendulum Blade, Death Metal, Dominance, Ancient Signet,
    Arondight, Blood-Bound Book, Gem of Focus, Book of Thoth, Avatar''s Parashu, The
    Cosmic Horror, Bancroft''s Talon, Silverbranch Bow, Transcendence, Runeforged
    Hammer, Rod of Asclepius, Totem of Death, Typhon’s Heart, Polynomicon.'
  slot_scores:
    Avenging Blade:
      total: 0.65
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.26
    Book of Thoth:
      total: 0.54
      efficiency: 0.51
      win: 0.75
      pick: 0.06
      fit: 0.16
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.82
      pick: 0.25
      fit: 0.4
    Riptalon:
      total: 0.69
      efficiency: 0.43
      win: 1.0
      pick: 0.28
      fit: 0.52
    Obsidian Shard:
      total: 0.67
      efficiency: 0.54
      win: 0.88
      pick: 0.2
      fit: 0.5
  community_ordered:
  - Avenging Blade
  - Book of Thoth
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Berserker''s Shield, Jotunn''s Revenge, Gluttonous
    Grimoire, Rod of Asclepius, Nimble Ring, The Reaper, Shield of the Phoenix, Kinetic
    Cuirass, Blood-Bound Book, Ethereal Staff, Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Bancroft''s Talon, Spear of the Magus, Runeforged Hammer, Yogi''s Necklace,
    Lifebinder, Shifter''s Shield, Helm of Radiance, Pharaoh''s Curse, Shield Splitter,
    Sphere of Negation, Lernaean Bow, Shogun''s Ofuda, Chandra''s Grace, Phoenix Feather,
    Eye of the Storm, Hydra''s Lament, Tekko-Kagi, Erosion, Eye of Providence, Jade
    Scepter, Heartseeker, Bracer of The Abyss.'
  slot_scores:
    Avenging Blade:
      total: 0.68
      efficiency: 0.49
      win: 1.0
      pick: 0.15
      fit: 0.34
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.82
      pick: 0.25
      fit: 0.25
    Riptalon:
      total: 0.71
      efficiency: 0.43
      win: 1.0
      pick: 0.28
      fit: 0.66
    Obsidian Shard:
      total: 0.65
      efficiency: 0.54
      win: 0.88
      pick: 0.2
      fit: 0.35
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Avenging Blade
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Book of Thoth
  - Jotunn's Revenge
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire, Nimble Ring, Spear
    of the Magus, The Reaper, Tekko-Kagi, Heartseeker, Doom Orb, The World Stone,
    Dreamer''s Idol, Titan''s Bane, The Crusher, Lernaean Bow, Bracer of The Abyss,
    Hydra''s Lament, Pendulum Blade, Chronos'' Pendant, The Cosmic Horror, Silverbranch
    Bow, Avatar''s Parashu, Ancient Signet, Blood-Bound Book, Death Metal, Dominance,
    Book of Thoth, Bancroft''s Talon, Gem of Focus, Arondight, Oath-Sworn Spear, Transcendence,
    Rod of Asclepius, Runeforged Hammer, Typhon’s Heart.'
  slot_scores:
    Avenging Blade:
      total: 0.69
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.53
    Book of Thoth:
      total: 0.54
      efficiency: 0.51
      win: 0.75
      pick: 0.06
      fit: 0.16
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.75
      efficiency: 0.86
      win: 0.82
      pick: 0.25
      fit: 0.49
    Riptalon:
      total: 0.71
      efficiency: 0.43
      win: 1.0
      pick: 0.28
      fit: 0.62
    Obsidian Shard:
      total: 0.68
      efficiency: 0.54
      win: 0.88
      pick: 0.2
      fit: 0.59
  community_ordered:
  - Avenging Blade
  - Book of Thoth
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Avenging Blade
  - Nimble Ring
  - Silverbranch Bow
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Silverbranch Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire, Silverbranch
    Bow, Spear of the Magus, Lernaean Bow, Tekko-Kagi, The Reaper, Golden Blade, Bracer
    of The Abyss, Hydra''s Lament, Heartseeker, Toxic Blade, Doom Orb, Chronos'' Pendant,
    The World Stone, Dominance, Ancient Signet, Dreamer''s Idol, Blood-Bound Book,
    Book of Thoth, Death Metal, Titan''s Bane, The Crusher, Qin''s Blade, Bancroft''s
    Talon, Gem of Focus, Arondight, Transcendence, Sun Beam Bow, Pendulum Blade, The
    Cosmic Horror, Rod of Asclepius, Runeforged Hammer, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.65
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.23
    Nimble Ring:
      total: 0.62
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.53
      win: 0.71
      pick: 0.0
      fit: 0.55
    Riptalon:
      total: 0.74
      efficiency: 0.51
      win: 1.0
      pick: 0.28
      fit: 0.63
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.82
      pick: 0.25
      fit: 0.31
    Obsidian Shard:
      total: 0.66
      efficiency: 0.54
      win: 0.88
      pick: 0.2
      fit: 0.41
  community_ordered:
  - Avenging Blade
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Nimble
    Ring, Hydra''s Lament, Gluttonous Grimoire, Chronos'' Pendant, Spear of the Magus,
    Lernaean Bow, The Reaper, Tekko-Kagi, Arondight, Gem of Focus, Pendulum Blade,
    Heartseeker, Bracer of The Abyss, Doom Orb, The World Stone, Totem of Death, Dominance,
    Titan''s Bane, The Crusher, Ancient Signet, Dreamer''s Idol, Blood-Bound Book,
    Book of Thoth, Breastplate of Valor, Death Metal, Genji''s Guard, Bancroft''s
    Talon, Silverbranch Bow, Transcendence, Avatar''s Parashu, Runeforged Hammer,
    The Cosmic Horror, Berserker''s Shield, Rod of Asclepius.'
  slot_scores:
    Avenging Blade:
      total: 0.64
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.2
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.6
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.71
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.82
      pick: 0.25
      fit: 0.26
    Obsidian Shard:
      total: 0.65
      efficiency: 0.54
      win: 0.88
      pick: 0.2
      fit: 0.36
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.71
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Avenging Blade
  - Rod of Tahuti
  - Obsidian Shard
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
      total: 0.64
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.63
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.26
      fit: 0.48
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.71
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.82
      pick: 0.25
      fit: 0.38
    Obsidian Shard:
      total: 0.67
      efficiency: 0.54
      win: 0.88
      pick: 0.2
      fit: 0.48
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
