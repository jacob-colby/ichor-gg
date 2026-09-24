---
type: smite-build
god: Neith
mode: Conquest
builds:
- source: community
  aspect: Aspect of Wind
  aspect_pick_rate: 0.33
  aspect_win_rate: 0.53
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.27
    win_rate: 0.64
    alternates:
    - name: Tyrfing
      pick_rate: 0.25
      win_rate: 0.46
    - name: Book of Thoth
      pick_rate: 0.2
      win_rate: 0.7
  - name: The World Stone
    pick_rate: 0.18
    win_rate: 0.67
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.18
      win_rate: 0.67
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.16
    win_rate: 0.75
    alternates:
    - name: The World Stone
      pick_rate: 0.12
      win_rate: 0.5
    - name: Silverbranch Bow
      pick_rate: 0.06
      win_rate: 0.33
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.75
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.2
      win_rate: 0.6
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.67
  - name: Chronos' Pendant
    pick_rate: 0.09
    win_rate: 0.75
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.16
      win_rate: 0.71
    - name: Hastened Fatalis
      pick_rate: 0.07
      win_rate: 0.67
  - name: Gem
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Bow
      pick_rate: 0.07
      win_rate: 0.0
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.33
    win_rate: 0.65
  - name: Hunter's Cowl
    pick_rate: 0.18
    win_rate: 0.67
  - name: Conduit Gem
    pick_rate: 0.16
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/neith/
  last_verified: '2026-09-24'
  god_win_rate: 0.6274509803921569
  god_matches_won: 32
  god_matches_played: 51
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Death Metal
  - Soul Gem
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
    this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem, Gluttonous Grimoire,
    Spear of the Magus, Lernaean Bow, The Reaper, Bragi''s Harp, Tekko-Kagi, Hydra''s
    Lament, Bracer of The Abyss, Heartseeker, Doom Orb, Deathbringer, Ancient Signet,
    Blood-Bound Book, Dreamer''s Idol, Golden Blade, Titan''s Bane, Dominance, The
    Crusher, Demon Blade, Bancroft''s Talon, Toxic Blade, Musashi''s Dual Swords,
    Gem of Focus, Arondight, Transcendence, Pendulum Blade, Rod of Asclepius, The
    Cosmic Horror, Runeforged Hammer, Silverbranch Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.49
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.49
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.3
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.75
      pick: 0.27
      fit: 0.4
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Death Metal
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the
    Magus, Hydra''s Lament, Bragi''s Harp, Lernaean Bow, Heartseeker, The Reaper,
    Tekko-Kagi, Doom Orb, Ancient Signet, Bracer of The Abyss, Dominance, Deathbringer,
    Bancroft''s Talon, Titan''s Bane, Blood-Bound Book, The Crusher, Golden Blade,
    Dreamer''s Idol, Transcendence, Arondight, Gem of Focus, Musashi''s Dual Swords,
    Polynomicon, Demon Blade, Runeforged Hammer, Rod of Asclepius, Soul Reaver, Pendulum
    Blade, Silverbranch Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.42
    Death Metal:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.35
    Riptalon:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.38
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.75
      pick: 0.27
      fit: 0.39
  community_ordered:
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Musashi's Dual Swords
  - Riptalon
  - Rod of Tahuti
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Musashi's Dual Swords
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire,
    Spear of the Magus, The Reaper, Lernaean Bow, Bragi''s Harp, Tekko-Kagi, Hydra''s
    Lament, Heartseeker, Bracer of The Abyss, Deathbringer, Doom Orb, Ancient Signet,
    Blood-Bound Book, Dreamer''s Idol, Titan''s Bane, The Crusher, Golden Blade, Dominance,
    Musashi''s Dual Swords, Demon Blade, Bancroft''s Talon, Gem of Focus, Toxic Blade,
    Arondight, Transcendence, Damaru, Rage, Rod of Asclepius, Pendulum Blade, Silverbranch
    Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.35
    Death Metal:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.51
    Musashi's Dual Swords:
      total: 0.52
      efficiency: 0.46
      win: 0.67
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.46
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.3
    Deathbringer:
      total: 0.53
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Riptalon
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Soul Gem, Nimble Ring, Death Metal, Gluttonous Grimoire,
    Spear of the Magus, The Reaper, Tekko-Kagi, Hydra''s Lament, Heartseeker, Lernaean
    Bow, Bragi''s Harp, Doom Orb, Titan''s Bane, The Crusher, Bracer of The Abyss,
    Dreamer''s Idol, Deathbringer, Ancient Signet, Blood-Bound Book, Pendulum Blade,
    Dominance, Golden Blade, Arondight, Gem of Focus, Toxic Blade, Bancroft''s Talon,
    Avatar''s Parashu, Musashi''s Dual Swords, The Cosmic Horror, Demon Blade, Transcendence,
    Runeforged Hammer, Rod of Asclepius, Silverbranch Bow.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.7
      pick: 0.2
      fit: 0.13
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.46
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.13
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.33
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.48
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.75
      pick: 0.27
      fit: 0.43
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Obsidian Shard
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
    Grimoire, Rod of Asclepius, The Reaper, Nimble Ring, Shield of the Phoenix, Death
    Metal, Blood-Bound Book, Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Breastplate
    of Valor, Freya''s Tears, Bancroft''s Talon, Spear of the Magus, Runeforged Hammer,
    Yogi''s Necklace, Golden Blade, Lifebinder, Helm of Radiance, Shifter''s Shield,
    Sphere of Negation, Shield Splitter, Lernaean Bow, Pharaoh''s Curse, Chandra''s
    Grace, Phoenix Feather, Hydra''s Lament, Shogun''s Ofuda, Eye of the Storm, Daybreak
    Gavel, Heartseeker, Erosion, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.26
    Riptalon:
      total: 0.74
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.64
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.21
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.75
      pick: 0.27
      fit: 0.31
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    for this god: Jotunn''s Revenge, Soul Gem, Nimble Ring, Gluttonous Grimoire, Death
    Metal, Spear of the Magus, The Reaper, Tekko-Kagi, Heartseeker, Doom Orb, Lernaean
    Bow, Dreamer''s Idol, Titan''s Bane, The Crusher, Bragi''s Harp, Hydra''s Lament,
    Avenging Blade, Bracer of The Abyss, Toxic Blade, Ancient Signet, Deathbringer,
    Blood-Bound Book, The Cosmic Horror, Pendulum Blade, Avatar''s Parashu, Dominance,
    Golden Blade, Bancroft''s Talon, Gem of Focus, Musashi''s Dual Swords, Arondight,
    Demon Blade, Oath-Sworn Spear, Silverbranch Bow.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.7
      pick: 0.2
      fit: 0.13
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.45
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.11
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.4
    Riptalon:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.56
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.75
      pick: 0.27
      fit: 0.5
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Book of Thoth
  - Jotunn's Revenge
  - Nimble Ring
  - Rod of Tahuti
  - Riptalon
  flex_slots:
  - Lernaean Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem, Gluttonous Grimoire,
    Spear of the Magus, Lernaean Bow, The Reaper, Bragi''s Harp, Tekko-Kagi, Bracer
    of The Abyss, Hydra''s Lament, Golden Blade, Heartseeker, Doom Orb, Toxic Blade,
    Ancient Signet, Deathbringer, Dominance, Blood-Bound Book, Dreamer''s Idol, Titan''s
    Bane, The Crusher, Qin''s Blade, Bancroft''s Talon, Gem of Focus, Demon Blade,
    Musashi''s Dual Swords, Arondight, Transcendence, Rod of Asclepius, Runeforged
    Hammer, Polynomicon, Silverbranch Bow.'
  slot_scores:
    Lernaean Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.4
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.7
      pick: 0.2
      fit: 0.13
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.3
    Nimble Ring:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.39
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.25
    Riptalon:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.52
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Riptalon
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Nimble
    Ring, Death Metal, Hydra''s Lament, Gluttonous Grimoire, Spear of the Magus, Lernaean
    Bow, The Reaper, Tekko-Kagi, Arondight, Gem of Focus, Heartseeker, Bragi''s Harp,
    Bracer of The Abyss, Pendulum Blade, Doom Orb, Deathbringer, Ancient Signet, Titan''s
    Bane, The Crusher, Dominance, Blood-Bound Book, Golden Blade, Dreamer''s Idol,
    Totem of Death, Toxic Blade, Breastplate of Valor, Bancroft''s Talon, Musashi''s
    Dual Swords, Genji''s Guard, Demon Blade, Transcendence, Qin''s Blade, Silverbranch
    Bow.'
  slot_scores:
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.75
      pick: 0.19
      fit: 0.36
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.64
      pick: 0.27
      fit: 0.49
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.21
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.75
      pick: 0.27
      fit: 0.31
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Death Metal
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Death Metal
  - Chronos' Pendant
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
    + win/pick). Underrated for this god: Jotunn''s Revenge, Nimble Ring, Soul Gem,
    Death Metal, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Bracer of
    The Abyss, The Reaper, Lernaean Bow, Hydra''s Lament, Doom Orb, Tekko-Kagi, Ancient
    Signet, Heartseeker, Blood-Bound Book, Dreamer''s Idol, Gem of Focus, Deathbringer,
    Bancroft''s Talon, Titan''s Bane, The Crusher, Dominance, Golden Blade, Arondight,
    Rod of Asclepius, The Cosmic Horror, Toxic Blade, Polynomicon, Musashi''s Dual
    Swords, Typhon’s Heart, Demon Blade, Pendulum Blade, Silverbranch Bow.'
  slot_scores:
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.75
      pick: 0.19
      fit: 0.32
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.35
    Riptalon:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.44
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.75
      pick: 0.27
      fit: 0.45
  community_ordered:
  - Chronos' Pendant
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Death Metal, Nimble
    Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, The Reaper,
    Lernaean Bow, Tekko-Kagi, Hydra''s Lament, Heartseeker, Bracer of The Abyss, Doom
    Orb, Deathbringer, Titan''s Bane, Ancient Signet, The Crusher, Dominance, Golden
    Blade, Dreamer''s Idol, Blood-Bound Book, Musashi''s Dual Swords, Bancroft''s
    Talon, Demon Blade, Arondight, Gem of Focus, Transcendence, Toxic Blade, Runeforged
    Hammer, Pendulum Blade, Avatar''s Parashu, Rod of Asclepius, Silverbranch Bow.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.7
      pick: 0.2
      fit: 0.17
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.39
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.17
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.31
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.45
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.75
      pick: 0.27
      fit: 0.41
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Riptalon
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Death Metal
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Gluttonous Grimoire, Spear of the Magus, Lernaean Bow, The Reaper, Silverbranch
    Bow, Bragi''s Harp, Tekko-Kagi, Hydra''s Lament, Bracer of The Abyss, Heartseeker,
    Doom Orb, Deathbringer, Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Golden
    Blade, Titan''s Bane, Dominance, The Crusher, Demon Blade, Bancroft''s Talon,
    Toxic Blade, Musashi''s Dual Swords, Gem of Focus, Arondight, Transcendence, Pendulum
    Blade, Rod of Asclepius, The Cosmic Horror, Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.64
      pick: 0.27
      fit: 0.38
    Death Metal:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.75
      pick: 0.25
      fit: 0.3
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
