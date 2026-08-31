---
type: smite-build
god: Danzaburou
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fellowship
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.4
  slot_order:
  - name: Transcendence
    pick_rate: 0.3
    win_rate: 0.56
    alternates:
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.33
    - name: Tyrfing
      pick_rate: 0.14
      win_rate: 0.52
  - name: Jotunn's Revenge
    pick_rate: 0.11
    win_rate: 0.59
    alternates:
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.53
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.33
  - name: Polynomicon
    pick_rate: 0.1
    win_rate: 0.27
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.6
    - name: The Executioner
      pick_rate: 0.06
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.11
    win_rate: 0.65
    alternates:
    - name: Polynomicon
      pick_rate: 0.08
      win_rate: 0.5
    - name: Pendulum Blade
      pick_rate: 0.07
      win_rate: 0.64
  - name: Obsidian Shard
    pick_rate: 0.1
    win_rate: 0.69
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.35
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.5
  - name: Void Shard
    pick_rate: 0.08
    win_rate: 0.38
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.57
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.4
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.19
    win_rate: 0.52
  - name: Conduit Gem
    pick_rate: 0.11
    win_rate: 0.44
  - name: Hunter's Cowl
    pick_rate: 0.11
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/danzaburou/
  last_verified: '2026-08-31'
  god_win_rate: 0.4779874213836478
  god_matches_won: 76
  god_matches_played: 159
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-31'
  god_matches_analyzed: 7103
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Death Metal, Soul Gem, Tyrfing, Riptalon, Pendulum Blade,
    Lernaean Bow, Tekko-Kagi, The Reaper, Gluttonous Grimoire, Silverbranch Bow, Chronos''
    Pendant, Bragi''s Harp, Spear of the Magus, Deathbringer, Heartseeker, Hydra''s
    Lament, Golden Blade, Dominance, Demon Blade, Titan''s Bane, The Crusher, Bracer
    of The Abyss, Musashi''s Dual Swords, Toxic Blade, Doom Orb, Damaru, Rage, The
    World Stone, Blood-Bound Book, Ancient Signet, Runeforged Hammer, Arondight, Avatar''s
    Parashu, Dreamer''s Idol, Qin''s Blade, Bancroft''s Talon, Spear of Desolation.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.53
      pick: 0.15
      fit: 0.05
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.37
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.18
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.39
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.2
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.69
      pick: 0.22
      fit: 0.3
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Nimble Ring, Soul Gem, Chronos'' Pendant, Gluttonous Grimoire, Pendulum
    Blade, Spear of the Magus, Hydra''s Lament, Bragi''s Harp, Lernaean Bow, Tyrfing,
    The Reaper, Heartseeker, Tekko-Kagi, Doom Orb, Ancient Signet, Riptalon, The World
    Stone, Bracer of The Abyss, Dominance, Silverbranch Bow, Deathbringer, Bancroft''s
    Talon, Titan''s Bane, Blood-Bound Book, The Crusher, Dreamer''s Idol, Golden Blade,
    Arondight, Gem of Focus, Musashi''s Dual Swords, Demon Blade, Runeforged Hammer,
    Rod of Asclepius, Soul Reaver, Spear of Desolation.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.53
      pick: 0.15
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.44
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.24
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.35
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.69
      pick: 0.22
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Demon Blade
  - Deathbringer
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Deathbringer
  - Demon Blade
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Death Metal, Nimble Ring, Soul Gem, Riptalon, Pendulum Blade, Gluttonous
    Grimoire, Tyrfing, Lernaean Bow, The Reaper, Tekko-Kagi, Silverbranch Bow, Chronos''
    Pendant, Deathbringer, Spear of the Magus, Bragi''s Harp, Heartseeker, Demon Blade,
    Hydra''s Lament, Golden Blade, Dominance, Musashi''s Dual Swords, Titan''s Bane,
    The Crusher, Bracer of The Abyss, Toxic Blade, Doom Orb, Damaru, Rage, The World
    Stone, Blood-Bound Book, Ancient Signet, Dreamer''s Idol, Avatar''s Parashu, Runeforged
    Hammer, Arondight, Qin''s Blade, Bancroft''s Talon, Spear of Desolation.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.34
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.49
    Demon Blade:
      total: 0.47
      efficiency: 0.38
      win: 0.53
      pick: 0.0
      fit: 0.67
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.2
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.69
      pick: 0.22
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Nimble Ring, Death Metal, Pendulum Blade, Gluttonous Grimoire,
    Chronos'' Pendant, Spear of the Magus, The Reaper, Riptalon, Tekko-Kagi, Silverbranch
    Bow, Hydra''s Lament, Lernaean Bow, Tyrfing, Heartseeker, Bragi''s Harp, Doom
    Orb, The World Stone, Titan''s Bane, The Crusher, Bracer of The Abyss, Dreamer''s
    Idol, Deathbringer, Ancient Signet, Blood-Bound Book, Dominance, Golden Blade,
    Arondight, Gem of Focus, Toxic Blade, Bancroft''s Talon, Avatar''s Parashu, Musashi''s
    Dual Swords, The Cosmic Horror, Demon Blade, Runeforged Hammer, Rod of Asclepius,
    Spear of Desolation.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.53
      pick: 0.15
      fit: 0.13
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.46
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.13
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.33
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.69
      pick: 0.22
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Berserker's Shield
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
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, The Reaper, Riptalon,
    Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius, Nimble Ring, Death
    Metal, Kinetic Cuirass, Runeforged Hammer, Golden Blade, Freya''s Tears, Genji''s
    Guard, Blood-Bound Book, Breastplate of Valor, Ethereal Staff, Yogi''s Necklace,
    Shifter''s Shield, Shield Splitter, Bancroft''s Talon, Lernaean Bow, Pharaoh''s
    Curse, Tyrfing, Eye of the Storm, Shogun''s Ofuda, Phoenix Feather, Spear of the
    Magus, Lifebinder, Silverbranch Bow, Tekko-Kagi, Erosion, Helm of Radiance, Hydra''s
    Lament, Eye of Providence, Daybreak Gavel, Toxic Blade, Chandra''s Grace, Heartseeker.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.25
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.14
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.69
      pick: 0.22
      fit: 0.24
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
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
    for this god: Soul Gem, Pendulum Blade, Nimble Ring, Gluttonous Grimoire, Riptalon,
    Death Metal, The Reaper, Tekko-Kagi, Silverbranch Bow, Spear of the Magus, Heartseeker,
    Titan''s Bane, Tyrfing, Lernaean Bow, The Crusher, Chronos'' Pendant, Doom Orb,
    Avenging Blade, Toxic Blade, The World Stone, Hydra''s Lament, Dreamer''s Idol,
    Bragi''s Harp, Deathbringer, Avatar''s Parashu, Dominance, Golden Blade, Bracer
    of The Abyss, Demon Blade, Musashi''s Dual Swords, The Cosmic Horror, Oath-Sworn
    Spear, Ancient Signet, The Executioner, Blood-Bound Book, Runeforged Hammer, Arondight,
    Spear of Desolation.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.53
      pick: 0.15
      fit: 0.04
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.48
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.15
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.32
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.35
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.69
      pick: 0.22
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Riptalon
  - Tyrfing
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Death Metal, Riptalon, Tyrfing, Silverbranch Bow, Soul
    Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper,
    Chronos'' Pendant, Spear of the Magus, Bragi''s Harp, Toxic Blade, Hydra''s Lament,
    Heartseeker, Deathbringer, Dominance, Bracer of The Abyss, Qin''s Blade, Demon
    Blade, Titan''s Bane, The Crusher, Musashi''s Dual Swords, Doom Orb, Ancient Signet,
    The World Stone, Blood-Bound Book, Dreamer''s Idol, Sun Beam Bow, Runeforged Hammer,
    Arondight, Damaru, Bancroft''s Talon, Rage, Berserker''s Shield, Spear of Desolation.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.28
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.52
      pick: 0.14
      fit: 0.62
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.17
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.69
      pick: 0.22
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Pendulum Blade
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - Pendulum Blade
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
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Nimble
    Ring, Pendulum Blade, Death Metal, Hydra''s Lament, Gluttonous Grimoire, Spear
    of the Magus, Riptalon, Lernaean Bow, Tyrfing, Silverbranch Bow, The Reaper, Arondight,
    Gem of Focus, Tekko-Kagi, Bragi''s Harp, Bracer of The Abyss, Heartseeker, Deathbringer,
    Doom Orb, Ancient Signet, Dominance, Blood-Bound Book, The World Stone, Golden
    Blade, Titan''s Bane, Totem of Death, The Crusher, Dreamer''s Idol, Breastplate
    of Valor, Toxic Blade, Bancroft''s Talon, Musashi''s Dual Swords, Demon Blade,
    Genji''s Guard, Qin''s Blade, Spear of Desolation.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.09
      fit: 0.37
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.48
    Pendulum Blade:
      total: 0.51
      efficiency: 0.42
      win: 0.64
      pick: 0.12
      fit: 0.48
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.2
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.69
      pick: 0.22
      fit: 0.3
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
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
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Nimble Ring, Soul Gem, Death Metal, Chronos''
    Pendant, Gluttonous Grimoire, Spear of the Magus, Pendulum Blade, Bragi''s Harp,
    Lernaean Bow, The Reaper, Riptalon, Tyrfing, Hydra''s Lament, Bracer of The Abyss,
    Tekko-Kagi, Silverbranch Bow, Doom Orb, The World Stone, Ancient Signet, Heartseeker,
    Blood-Bound Book, Dreamer''s Idol, Deathbringer, Gem of Focus, Titan''s Bane,
    Bancroft''s Talon, The Crusher, Dominance, Golden Blade, Arondight, Rod of Asclepius,
    Musashi''s Dual Swords, The Cosmic Horror, Demon Blade, Toxic Blade, Typhon’s
    Heart, Spear of Desolation.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.53
      pick: 0.15
      fit: 0.2
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.38
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.13
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.34
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.69
      pick: 0.22
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Death Metal, Nimble Ring, Soul Gem,
    Gluttonous Grimoire, Chronos'' Pendant, Spear of the Magus, Bragi''s Harp, The
    Reaper, Tyrfing, Lernaean Bow, Tekko-Kagi, Riptalon, Silverbranch Bow, Bracer
    of The Abyss, Heartseeker, Hydra''s Lament, Doom Orb, Deathbringer, The World
    Stone, Titan''s Bane, The Crusher, Ancient Signet, Dominance, Golden Blade, Dreamer''s
    Idol, Blood-Bound Book, Demon Blade, Musashi''s Dual Swords, Bancroft''s Talon,
    Toxic Blade, Runeforged Hammer, Avatar''s Parashu, Arondight, Gem of Focus, The
    Cosmic Horror, Rod of Asclepius, Spear of Desolation.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.53
      pick: 0.15
      fit: 0.18
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.36
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.18
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.33
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.69
      pick: 0.22
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Nimble Ring, Death Metal, Soul Gem, Riptalon, Lernaean
    Bow, Tekko-Kagi, Tyrfing, The Reaper, Gluttonous Grimoire, Silverbranch Bow, Heartseeker,
    Bragi''s Harp, Spear of the Magus, Deathbringer, Hydra''s Lament, Golden Blade,
    Spear of Desolation, Dominance, Demon Blade, Titan''s Bane, The Crusher, Bracer
    of The Abyss, Musashi''s Dual Swords, Toxic Blade, Doom Orb, Damaru, Rage, The
    World Stone, Blood-Bound Book, Ancient Signet, Runeforged Hammer, Arondight, Avatar''s
    Parashu, Dreamer''s Idol, Qin''s Blade, Chronos'' Pendant, Pendulum Blade, Bancroft''s
    Talon.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.15
      fit: 0.37
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.65
      pick: 0.18
      fit: 0.2
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.43
  starter: *id001
---
