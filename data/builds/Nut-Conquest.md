---
type: smite-build
god: Nut
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cosmos
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.61
  slot_order:
  - name: Tyrfing
    pick_rate: 0.49
    win_rate: 0.6
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.22
      win_rate: 0.52
    - name: Devourer's Gauntlet
      pick_rate: 0.13
      win_rate: 0.56
  - name: Bragi's Harp
    pick_rate: 0.45
    win_rate: 0.6
    alternates:
    - name: Tyrfing
      pick_rate: 0.14
      win_rate: 0.56
    - name: Staff of Myrddin
      pick_rate: 0.13
      win_rate: 0.53
  - name: Barbed Carver
    pick_rate: 0.25
    win_rate: 0.59
    alternates:
    - name: Avenging Blade
      pick_rate: 0.15
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.58
  - name: The Executioner
    pick_rate: 0.25
    win_rate: 0.54
    alternates:
    - name: Riptalon
      pick_rate: 0.12
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.57
  - name: Riptalon
    pick_rate: 0.12
    win_rate: 0.58
    alternates:
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.62
    - name: Avenging Blade
      pick_rate: 0.08
      win_rate: 0.57
  - name: Hunter's Bow
    pick_rate: 0.07
    win_rate: 0.59
    alternates:
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.62
    - name: Manchu Bow
      pick_rate: 0.06
      win_rate: 0.61
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.45
    win_rate: 0.59
  - name: Death's Toll
    pick_rate: 0.19
    win_rate: 0.58
  - name: Archmage's Gem
    pick_rate: 0.12
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/nut/
  last_verified: '2026-11-04'
  god_win_rate: 0.5666982024597919
  god_matches_won: 599
  god_matches_played: 1057
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Tyrfing
  - Jotunn's Revenge
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Jotunn''s Revenge, Nimble Ring, Gluttonous Grimoire, The Reaper,
    Tekko-Kagi, Obsidian Shard, Blood-Bound Book, Spear of the Magus, Bracer of The
    Abyss, Death Metal, Silverbranch Bow, Hydra''s Lament, Dreamer''s Idol, The Crusher,
    Ancient Signet, Lernaean Bow, Dominance, Chronos'' Pendant, Heartseeker, Polynomicon,
    Doom Orb, Titan''s Bane, Golden Blade, Toxic Blade, The World Stone, Bancroft''s
    Talon, Arondight, Gem of Focus, Heartwood Charm, Qin''s Blade, Soul Reaver, The
    Cosmic Horror, Avatar''s Parashu, Pendulum Blade, Typhon’s Heart.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.19
    Tyrfing:
      total: 0.57
      efficiency: 0.53
      win: 0.6
      pick: 0.49
      fit: 0.61
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
    Bragi's Harp:
      total: 0.57
      efficiency: 0.47
      win: 0.6
      pick: 0.61
      fit: 0.71
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.18
      fit: 0.38
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Transcendence
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Soul Gem, Nimble Ring, Hydra''s Lament, Gluttonous Grimoire, The Reaper,
    Death Metal, Ancient Signet, Blood-Bound Book, Obsidian Shard, Dominance, Polynomicon,
    Tekko-Kagi, Heartseeker, Spear of the Magus, The Crusher, Chronos'' Pendant, Bracer
    of The Abyss, Lernaean Bow, Doom Orb, Dreamer''s Idol, Bancroft''s Talon, The
    World Stone, Heartwood Charm, Titan''s Bane, Soul Reaver, Arondight, Silverbranch
    Bow, Golden Blade, Gem of Focus, Transcendence, Avatar''s Parashu, Toxic Blade,
    Book of Thoth, The Cosmic Horror, Qin''s Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.57
      efficiency: 0.53
      win: 0.6
      pick: 0.49
      fit: 0.57
    Transcendence:
      total: 0.48
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.57
      efficiency: 0.47
      win: 0.6
      pick: 0.61
      fit: 0.71
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.18
      fit: 0.42
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Jotunn''s Revenge, Gluttonous Grimoire, The Reaper, Nimble Ring,
    Tekko-Kagi, Obsidian Shard, Hydra''s Lament, Spear of the Magus, The Crusher,
    Blood-Bound Book, Heartseeker, Dreamer''s Idol, Silverbranch Bow, Death Metal,
    Chronos'' Pendant, Titan''s Bane, Ancient Signet, Bracer of The Abyss, Doom Orb,
    Lernaean Bow, Dominance, Polynomicon, The World Stone, Arondight, Toxic Blade,
    Gem of Focus, Heartwood Charm, Golden Blade, Pendulum Blade, Avatar''s Parashu,
    Bancroft''s Talon, The Cosmic Horror, Soul Reaver, Qin''s Blade, Totem of Death.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.56
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.49
      fit: 0.54
    Bragi's Harp:
      total: 0.56
      efficiency: 0.47
      win: 0.6
      pick: 0.61
      fit: 0.62
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.52
      pick: 0.22
      fit: 0.56
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.18
      fit: 0.4
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Bragi's Harp
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Amanita Charm, Soul Gem, Berserker''s Shield, Shield of the Phoenix,
    The Reaper, Blood-Bound Book, Gluttonous Grimoire, Kinetic Cuirass, Genji''s Guard,
    Jotunn''s Revenge, Ethereal Staff, Yogi''s Necklace, Phoenix Feather, Bancroft''s
    Talon, Freya''s Tears, Nimble Ring, Shield Splitter, Breastplate of Valor, Golden
    Blade, Chandra''s Grace, Oni Hunter''s Garb, Runeforged Hammer, Obsidian Shard,
    Helm of Radiance, Sphere of Negation, Draconic Scale, Ancient Signet, Toxic Blade,
    Regrowth Striders, Hydra''s Lament, Spear of the Magus, Death Metal, Bloodforge,
    Shogun''s Ofuda, Pharaoh''s Curse, Tekko-Kagi.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.4
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.49
      fit: 0.44
    Bragi's Harp:
      total: 0.54
      efficiency: 0.47
      win: 0.6
      pick: 0.61
      fit: 0.5
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.57
      pick: 0.18
      fit: 0.25
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Spear of Desolation
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
    for this god: Soul Gem, Jotunn''s Revenge, Gluttonous Grimoire, The Reaper, Obsidian
    Shard, Tekko-Kagi, Spear of the Magus, Nimble Ring, Silverbranch Bow, The Crusher,
    Dreamer''s Idol, Heartseeker, Doom Orb, Titan''s Bane, Blood-Bound Book, The World
    Stone, Toxic Blade, Death Metal, Hydra''s Lament, Ancient Signet, Bracer of The
    Abyss, Chronos'' Pendant, Polynomicon, Lernaean Bow, Dominance, The Cosmic Horror,
    Avatar''s Parashu, Golden Blade, Pendulum Blade, Bancroft''s Talon, Arondight,
    Gem of Focus, Heartwood Charm, Soul Reaver, Qin''s Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.55
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.49
      fit: 0.52
    Bragi's Harp:
      total: 0.56
      efficiency: 0.47
      win: 0.6
      pick: 0.61
      fit: 0.61
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.52
      pick: 0.22
      fit: 0.57
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.57
      pick: 0.18
      fit: 0.49
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Nimble Ring
  - Rod of Tahuti
  - Soul Gem
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Jotunn''s Revenge, Nimble Ring, Gluttonous Grimoire, The Reaper,
    Silverbranch Bow, Blood-Bound Book, Tekko-Kagi, Obsidian Shard, Bracer of The
    Abyss, Spear of the Magus, Death Metal, Hydra''s Lament, Ancient Signet, Golden
    Blade, Lernaean Bow, Dominance, Toxic Blade, Dreamer''s Idol, The Crusher, Polynomicon,
    Chronos'' Pendant, Heartseeker, Qin''s Blade, Doom Orb, Titan''s Bane, The World
    Stone, Bancroft''s Talon, Arondight, Gem of Focus, Soul Reaver, Heartwood Charm,
    Dagger of Frenzy, The Cosmic Horror, Avatar''s Parashu, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.49
      fit: 0.63
    Bragi's Harp:
      total: 0.56
      efficiency: 0.47
      win: 0.6
      pick: 0.61
      fit: 0.63
    Nimble Ring:
      total: 0.53
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.57
      pick: 0.18
      fit: 0.31
    Soul Gem:
      total: 0.55
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Bragi's Harp
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Hydra''s
    Lament, Chronos'' Pendant, Nimble Ring, Gluttonous Grimoire, The Reaper, Arondight,
    Gem of Focus, Heartwood Charm, Tekko-Kagi, Blood-Bound Book, Obsidian Shard, Silverbranch
    Bow, Spear of the Magus, The Crusher, Bracer of The Abyss, Ancient Signet, Lernaean
    Bow, Dominance, Damaru, Genji''s Guard, Death Metal, Heartseeker, Dreamer''s Idol,
    Pendulum Blade, Polynomicon, Totem of Death, Titan''s Bane, Toxic Blade, Doom
    Orb, Golden Blade, The World Stone, Qin''s Blade, Bancroft''s Talon, Breastplate
    of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.6
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.49
      fit: 0.5
    Bragi's Harp:
      total: 0.54
      efficiency: 0.47
      win: 0.6
      pick: 0.61
      fit: 0.52
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.52
      pick: 0.22
      fit: 0.6
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.57
      pick: 0.18
      fit: 0.26
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, The Reaper, Gluttonous
    Grimoire, Death Metal, Hydra''s Lament, The Crusher, Heartseeker, Tekko-Kagi,
    Obsidian Shard, Nimble Ring, Blood-Bound Book, Titan''s Bane, Spear of the Magus,
    Dreamer''s Idol, Ancient Signet, Arondight, Lernaean Bow, Dominance, Chronos''
    Pendant, Polynomicon, Doom Orb, Avatar''s Parashu, Golden Blade, The World Stone,
    Silverbranch Bow, Bracer of The Abyss, Bancroft''s Talon, Pendulum Blade, Gem
    of Focus, Heartwood Charm, Bloodforge, Soul Reaver, Transcendence, Runeforged
    Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.57
      efficiency: 0.53
      win: 0.6
      pick: 0.49
      fit: 0.6
    Bragi's Harp:
      total: 0.57
      efficiency: 0.47
      win: 0.6
      pick: 0.61
      fit: 0.7
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.52
      pick: 0.22
      fit: 0.49
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.18
      fit: 0.39
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Tyrfing
  - Jotunn's Revenge
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Nimble
    Ring, Gluttonous Grimoire, The Reaper, Tekko-Kagi, Death Metal, Obsidian Shard,
    Blood-Bound Book, Spear of the Magus, Hydra''s Lament, The Crusher, Bracer of
    The Abyss, Ancient Signet, Lernaean Bow, Dominance, Heartseeker, Dreamer''s Idol,
    Chronos'' Pendant, Silverbranch Bow, Polynomicon, Titan''s Bane, Doom Orb, Golden
    Blade, The World Stone, Arondight, Bancroft''s Talon, Toxic Blade, Gem of Focus,
    Heartwood Charm, Soul Reaver, Avatar''s Parashu, The Cosmic Horror, Qin''s Blade,
    Pendulum Blade, Typhon’s Heart.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.21
    Tyrfing:
      total: 0.57
      efficiency: 0.53
      win: 0.6
      pick: 0.49
      fit: 0.62
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.58
      efficiency: 0.47
      win: 0.6
      pick: 0.61
      fit: 0.75
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.18
      fit: 0.38
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Bragi's Harp
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Jotunn''s Revenge, Nimble Ring, Gluttonous
    Grimoire, The Reaper, Tekko-Kagi, Obsidian Shard, Blood-Bound Book, Spear of the
    Magus, Bracer of The Abyss, Death Metal, Silverbranch Bow, Hydra''s Lament, Dreamer''s
    Idol, The Crusher, Ancient Signet, Lernaean Bow, Dominance, Chronos'' Pendant,
    Heartseeker, Polynomicon, Doom Orb, Titan''s Bane, Golden Blade, Toxic Blade,
    The World Stone, Bancroft''s Talon, Arondight, Gem of Focus, Heartwood Charm,
    Qin''s Blade, Soul Reaver, The Cosmic Horror, Avatar''s Parashu, Pendulum Blade,
    Typhon’s Heart.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.57
      efficiency: 0.53
      win: 0.6
      pick: 0.49
      fit: 0.61
    Bragi's Harp:
      total: 0.57
      efficiency: 0.47
      win: 0.6
      pick: 0.61
      fit: 0.71
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.52
      pick: 0.22
      fit: 0.48
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.18
      fit: 0.38
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
