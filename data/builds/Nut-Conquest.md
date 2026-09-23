---
type: smite-build
god: Nut
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cosmos
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.0
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.45
    win_rate: 0.42
    alternates:
    - name: Tyrfing
      pick_rate: 0.3
      win_rate: 0.33
    - name: Bragi's Harp
      pick_rate: 0.06
      win_rate: 0.75
  - name: Bragi's Harp
    pick_rate: 0.26
    win_rate: 0.33
    alternates:
    - name: Staff of Myrddin
      pick_rate: 0.25
      win_rate: 0.24
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.67
  - name: Barbed Carver
    pick_rate: 0.15
    win_rate: 0.2
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.67
    - name: Staff of Myrddin
      pick_rate: 0.1
      win_rate: 0.71
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.45
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.43
    - name: Barbed Carver
      pick_rate: 0.09
      win_rate: 0.33
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.44
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.11
      win_rate: 0.17
    - name: The Executioner
      pick_rate: 0.09
      win_rate: 0.8
  - name: Mote of Chaos
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.67
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.67
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.26
    win_rate: 0.5
  - name: Archmage's Gem
    pick_rate: 0.23
    win_rate: 0.44
  - name: Conduit Gem
    pick_rate: 0.13
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/nut/
  last_verified: '2026-09-23'
  god_win_rate: 0.42028985507246375
  god_matches_won: 29
  god_matches_played: 69
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - The Executioner
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Doom Orb, Jotunn''s Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire,
    Spear of the Magus, Tekko-Kagi, The Reaper, Lernaean Bow, Bracer of The Abyss,
    Heartseeker, Hydra''s Lament, The World Stone, Chronos'' Pendant, Dreamer''s Idol,
    Dominance, Death Metal, Titan''s Bane, Blood-Bound Book, The Crusher, Ancient
    Signet, Riptalon, Bancroft''s Talon, Gem of Focus, Arondight, Pendulum Blade,
    Silverbranch Bow, The Cosmic Horror, Avatar''s Parashu, Transcendence, Rod of
    Asclepius, Book of Thoth, Typhon’s Heart, Runeforged Hammer, Polynomicon, Totem
    of Death.'
  slot_scores:
    The Executioner:
      total: 0.55
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.36
    Berserker's Shield:
      total: 0.51
      efficiency: 0.46
      win: 0.67
      pick: 0.25
      fit: 0.26
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.55
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.12
      fit: 0.38
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.28
      fit: 0.38
  community_ordered:
  - The Executioner
  - Berserker's Shield
  - Doom Orb
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - The Executioner
  - Berserker's Shield
  - Jotunn's Revenge
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Soul Gem
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Doom
    Orb, Jotunn''s Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire, Hydra''s Lament,
    Spear of the Magus, Heartseeker, Lernaean Bow, The Reaper, Tekko-Kagi, Ancient
    Signet, The World Stone, Dominance, Bracer of The Abyss, Death Metal, Chronos''
    Pendant, Bancroft''s Talon, Titan''s Bane, The Crusher, Blood-Bound Book, Dreamer''s
    Idol, Transcendence, Arondight, Gem of Focus, Book of Thoth, Polynomicon, Pendulum
    Blade, Runeforged Hammer, Soul Reaver, Avatar''s Parashu, Rod of Asclepius, Riptalon,
    The Cosmic Horror, Typhon’s Heart, Totem of Death, Avenging Blade.'
  slot_scores:
    The Executioner:
      total: 0.54
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.29
    Berserker's Shield:
      total: 0.5
      efficiency: 0.46
      win: 0.67
      pick: 0.25
      fit: 0.19
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.52
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.67
      pick: 0.12
      fit: 0.42
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.45
      pick: 0.28
      fit: 0.42
    Soul Gem:
      total: 0.48
      efficiency: 0.57
      win: 0.42
      pick: 0.0
      fit: 0.62
  community_ordered:
  - The Executioner
  - Berserker's Shield
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - The Executioner
  - Berserker's Shield
  - Jotunn's Revenge
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Soul Gem
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
    god: Doom Orb, Jotunn''s Revenge, Soul Gem, Nimble Ring, Gluttonous Grimoire,
    Spear of the Magus, The Reaper, Tekko-Kagi, Heartseeker, Hydra''s Lament, Lernaean
    Bow, The World Stone, Titan''s Bane, Chronos'' Pendant, The Crusher, Bracer of
    The Abyss, Dreamer''s Idol, Pendulum Blade, Riptalon, Death Metal, Dominance,
    Ancient Signet, Arondight, Blood-Bound Book, Gem of Focus, Avatar''s Parashu,
    The Cosmic Horror, Bancroft''s Talon, Silverbranch Bow, Transcendence, Runeforged
    Hammer, Rod of Asclepius, Book of Thoth, Totem of Death, Typhon’s Heart, Polynomicon,
    Avenging Blade.'
  slot_scores:
    The Executioner:
      total: 0.54
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.31
    Berserker's Shield:
      total: 0.51
      efficiency: 0.46
      win: 0.67
      pick: 0.25
      fit: 0.21
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.56
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.12
      fit: 0.4
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.45
      pick: 0.28
      fit: 0.4
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.42
      pick: 0.0
      fit: 0.73
  community_ordered:
  - The Executioner
  - Berserker's Shield
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - The Executioner
  - Doom Orb
  - Berserker's Shield
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Amanita Charm
  - Soul Gem
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
    this god: Amanita Charm, Soul Gem, Jotunn''s Revenge, Gluttonous Grimoire, Rod
    of Asclepius, Nimble Ring, The Reaper, Shield of the Phoenix, Kinetic Cuirass,
    Blood-Bound Book, Freya''s Tears, Genji''s Guard, Breastplate of Valor, Bancroft''s
    Talon, Spear of the Magus, Runeforged Hammer, Riptalon, Yogi''s Necklace, Lifebinder,
    Shifter''s Shield, Helm of Radiance, Pharaoh''s Curse, Shield Splitter, Sphere
    of Negation, Lernaean Bow, Shogun''s Ofuda, Chandra''s Grace, Phoenix Feather,
    Eye of the Storm, Hydra''s Lament, Tekko-Kagi, Erosion, Eye of Providence, Jade
    Scepter, Heartseeker, Bracer of The Abyss.'
  slot_scores:
    The Executioner:
      total: 0.53
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.27
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.12
      fit: 0.25
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.25
      fit: 0.4
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.45
      pick: 0.28
      fit: 0.25
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.51
      efficiency: 0.57
      win: 0.42
      pick: 0.0
      fit: 0.79
  community_ordered:
  - The Executioner
  - Doom Orb
  - Berserker's Shield
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - The Executioner
  - Berserker's Shield
  - Jotunn's Revenge
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Soul Gem
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Doom Orb, Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire, Nimble
    Ring, Spear of the Magus, The Reaper, Tekko-Kagi, Heartseeker, The World Stone,
    Dreamer''s Idol, Titan''s Bane, The Crusher, Lernaean Bow, Riptalon, Bracer of
    The Abyss, Hydra''s Lament, Avenging Blade, Pendulum Blade, Chronos'' Pendant,
    The Cosmic Horror, Silverbranch Bow, Avatar''s Parashu, Ancient Signet, Blood-Bound
    Book, Death Metal, Dominance, Bancroft''s Talon, Gem of Focus, Arondight, Oath-Sworn
    Spear, Transcendence, Rod of Asclepius, Book of Thoth, Runeforged Hammer, Typhon’s
    Heart.'
  slot_scores:
    The Executioner:
      total: 0.58
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.61
    Berserker's Shield:
      total: 0.51
      efficiency: 0.46
      win: 0.67
      pick: 0.25
      fit: 0.21
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.55
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.12
      fit: 0.49
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.45
      pick: 0.28
      fit: 0.49
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.42
      pick: 0.0
      fit: 0.76
  community_ordered:
  - The Executioner
  - Berserker's Shield
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - The Executioner
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Nimble Ring
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Doom Orb, Jotunn''s Revenge, Nimble Ring, Soul Gem, Riptalon, Gluttonous
    Grimoire, Silverbranch Bow, Spear of the Magus, Lernaean Bow, Tekko-Kagi, The
    Reaper, Golden Blade, Bracer of The Abyss, Hydra''s Lament, Heartseeker, Toxic
    Blade, Chronos'' Pendant, The World Stone, Dominance, Ancient Signet, Dreamer''s
    Idol, Blood-Bound Book, Death Metal, Titan''s Bane, The Crusher, Qin''s Blade,
    Bancroft''s Talon, Gem of Focus, Arondight, Transcendence, Sun Beam Bow, Pendulum
    Blade, The Cosmic Horror, Rod of Asclepius, Book of Thoth, Runeforged Hammer,
    Avatar''s Parashu.'
  slot_scores:
    The Executioner:
      total: 0.54
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.34
    Berserker's Shield:
      total: 0.51
      efficiency: 0.46
      win: 0.67
      pick: 0.25
      fit: 0.24
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.48
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.12
      fit: 0.31
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.45
      pick: 0.28
      fit: 0.31
  community_ordered:
  - The Executioner
  - Berserker's Shield
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of Desolation
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Doom Orb, Jotunn''s Revenge, Soul
    Gem, Nimble Ring, Hydra''s Lament, Gluttonous Grimoire, Chronos'' Pendant, Spear
    of the Magus, Lernaean Bow, The Reaper, Tekko-Kagi, Arondight, Gem of Focus, Pendulum
    Blade, Heartseeker, Bracer of The Abyss, The World Stone, Totem of Death, Dominance,
    Titan''s Bane, Riptalon, The Crusher, Ancient Signet, Dreamer''s Idol, Blood-Bound
    Book, Breastplate of Valor, Death Metal, Genji''s Guard, Bancroft''s Talon, Silverbranch
    Bow, Transcendence, Avatar''s Parashu, Runeforged Hammer, The Cosmic Horror, Rod
    of Asclepius, Book of Thoth.'
  slot_scores:
    The Executioner:
      total: 0.54
      efficiency: 0.35
      win: 0.8
      pick: 0.19
      fit: 0.32
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.42
      pick: 0.45
      fit: 0.6
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.12
      fit: 0.26
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.45
      pick: 0.28
      fit: 0.26
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.42
      pick: 0.0
      fit: 0.78
  community_ordered:
  - The Executioner
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
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
    The Crusher, Ancient Signet, Riptalon, Bancroft''s Talon, Gem of Focus, Arondight,
    Pendulum Blade, Silverbranch Bow, The Cosmic Horror, Avatar''s Parashu, Transcendence,
    Rod of Asclepius, Book of Thoth, Typhon’s Heart, Runeforged Hammer, Polynomicon,
    Totem of Death.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.42
      pick: 0.45
      fit: 0.48
    Spear of the Magus:
      total: 0.46
      efficiency: 0.6
      win: 0.42
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.28
      fit: 0.38
    Obsidian Shard:
      total: 0.48
      efficiency: 0.54
      win: 0.44
      pick: 0.35
      fit: 0.48
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
