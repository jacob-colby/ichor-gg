---
type: smite-build
god: Danzaburou
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fellowship
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.5
  slot_order:
  - name: Transcendence
    pick_rate: 0.23
    win_rate: 0.33
    alternates:
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.25
    - name: Tyrfing
      pick_rate: 0.13
      win_rate: 0.43
  - name: Odysseus' Bow
    pick_rate: 0.12
    win_rate: 0.17
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.1
      win_rate: 0.4
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.4
  - name: Hydra's Lament
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.09
      win_rate: 0.25
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.0
  - name: Polynomicon
    pick_rate: 0.07
    win_rate: 0.33
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.09
      win_rate: 0.75
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.33
  - name: Rod of Tahuti
    pick_rate: 0.16
    win_rate: 0.29
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.5
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 0.5
  - name: Void Shard
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: Polynomicon
      pick_rate: 0.06
      win_rate: 0.0
    - name: Hunter's Bow
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.15
    win_rate: 0.25
  - name: Archmage's Gem
    pick_rate: 0.13
    win_rate: 0.29
  - name: Hunter's Cowl
    pick_rate: 0.12
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/danzaburou/
  last_verified: '2026-08-27'
  god_win_rate: 0.36538461538461536
  god_matches_won: 19
  god_matches_played: 52
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Tyrfing
  - Jotunn's Revenge
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
    this god: Hydra''s Lament, Tyrfing, Jotunn''s Revenge, Nimble Ring, Death Metal,
    Soul Gem, Lernaean Bow, Tekko-Kagi, The Reaper, Gluttonous Grimoire, Silverbranch
    Bow, Heartseeker, Bragi''s Harp, Spear of the Magus, Deathbringer, Golden Blade,
    Spear of Desolation, Dominance, Demon Blade, Titan''s Bane, The Crusher, Bracer
    of The Abyss, Musashi''s Dual Swords, Toxic Blade, Doom Orb, Damaru, Rage, Blood-Bound
    Book, Ancient Signet, Runeforged Hammer, Arondight, Avatar''s Parashu, Dreamer''s
    Idol, Qin''s Blade, Pendulum Blade, Bancroft''s Talon, Chronos'' Pendant, The
    World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.37
    Tyrfing:
      total: 0.46
      efficiency: 0.48
      win: 0.43
      pick: 0.13
      fit: 0.58
    Hydra's Lament:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.14
      fit: 0.32
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.19
      fit: 0.55
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.86
      win: 0.29
      pick: 0.35
      fit: 0.2
    Obsidian Shard:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.3
      fit: 0.3
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Jotunn''s Revenge, Tyrfing, Death Metal, Nimble Ring, Soul Gem, Gluttonous
    Grimoire, Spear of Desolation, Spear of the Magus, Bragi''s Harp, Lernaean Bow,
    Heartseeker, The Reaper, Tekko-Kagi, Doom Orb, Ancient Signet, Bracer of The Abyss,
    Dominance, Silverbranch Bow, Deathbringer, Bancroft''s Talon, Titan''s Bane, Blood-Bound
    Book, The Crusher, Dreamer''s Idol, Golden Blade, Polynomicon, Arondight, Gem
    of Focus, Musashi''s Dual Swords, Demon Blade, Runeforged Hammer, Rod of Asclepius,
    Soul Reaver, Pendulum Blade, Chronos'' Pendant, Book of Thoth, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.44
      efficiency: 0.48
      win: 0.43
      pick: 0.13
      fit: 0.48
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.14
      fit: 0.42
    Riptalon:
      total: 0.47
      efficiency: 0.51
      win: 0.5
      pick: 0.19
      fit: 0.38
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.86
      win: 0.29
      pick: 0.35
      fit: 0.35
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.3
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Hydra's Lament
  - Death Metal
  - Riptalon
  - Demon Blade
  - Deathbringer
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
    this god: Hydra''s Lament, Tyrfing, Jotunn''s Revenge, Death Metal, Nimble Ring,
    Soul Gem, Gluttonous Grimoire, Lernaean Bow, The Reaper, Tekko-Kagi, Silverbranch
    Bow, Deathbringer, Spear of the Magus, Heartseeker, Spear of Desolation, Bragi''s
    Harp, Demon Blade, Golden Blade, Dominance, Musashi''s Dual Swords, Titan''s Bane,
    The Crusher, Bracer of The Abyss, Toxic Blade, Doom Orb, Damaru, Rage, Blood-Bound
    Book, Ancient Signet, Dreamer''s Idol, Avatar''s Parashu, Runeforged Hammer, Arondight,
    Qin''s Blade, Bancroft''s Talon, Pendulum Blade, Chronos'' Pendant, The World
    Stone.'
  slot_scores:
    Hydra's Lament:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.14
      fit: 0.29
    Death Metal:
      total: 0.44
      efficiency: 0.61
      win: 0.33
      pick: 0.0
      fit: 0.49
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.19
      fit: 0.54
    Demon Blade:
      total: 0.38
      efficiency: 0.38
      win: 0.33
      pick: 0.0
      fit: 0.67
    Deathbringer:
      total: 0.39
      efficiency: 0.51
      win: 0.33
      pick: 0.0
      fit: 0.44
    Obsidian Shard:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.3
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Tyrfing
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, Jotunn''s Revenge, Soul Gem, Tyrfing, Nimble Ring, Death
    Metal, Gluttonous Grimoire, Spear of Desolation, Spear of the Magus, The Reaper,
    Tekko-Kagi, Silverbranch Bow, Heartseeker, Lernaean Bow, Bragi''s Harp, Doom Orb,
    Titan''s Bane, The Crusher, Bracer of The Abyss, Dreamer''s Idol, Deathbringer,
    Ancient Signet, Blood-Bound Book, Pendulum Blade, Dominance, Golden Blade, Arondight,
    Gem of Focus, Toxic Blade, Bancroft''s Talon, Avatar''s Parashu, Musashi''s Dual
    Swords, The Cosmic Horror, Demon Blade, Chronos'' Pendant, Runeforged Hammer,
    Rod of Asclepius, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.44
      efficiency: 0.48
      win: 0.43
      pick: 0.13
      fit: 0.44
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.14
      fit: 0.36
    Death Metal:
      total: 0.43
      efficiency: 0.61
      win: 0.33
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.19
      fit: 0.48
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.3
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Riptalon
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
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
    this god: Amanita Charm, Hydra''s Lament, Berserker''s Shield, Soul Gem, Jotunn''s
    Revenge, Tyrfing, The Reaper, Gluttonous Grimoire, Shield of the Phoenix, Rod
    of Asclepius, Nimble Ring, Death Metal, Kinetic Cuirass, Runeforged Hammer, Golden
    Blade, Freya''s Tears, Genji''s Guard, Blood-Bound Book, Breastplate of Valor,
    Ethereal Staff, Yogi''s Necklace, Shifter''s Shield, Shield Splitter, Bancroft''s
    Talon, Lernaean Bow, Pharaoh''s Curse, Eye of the Storm, Shogun''s Ofuda, Phoenix
    Feather, Spear of the Magus, Lifebinder, Silverbranch Bow, Tekko-Kagi, Erosion,
    Helm of Radiance, Heartseeker, Eye of Providence, Daybreak Gavel, Toxic Blade,
    Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.45
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.25
    Hydra's Lament:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.14
      fit: 0.24
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.19
      fit: 0.67
    Obsidian Shard:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.3
      fit: 0.24
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Hydra's Lament
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
    for this god: Jotunn''s Revenge, Hydra''s Lament, Tyrfing, Soul Gem, Nimble Ring,
    Gluttonous Grimoire, Death Metal, The Reaper, Tekko-Kagi, Silverbranch Bow, Spear
    of the Magus, Heartseeker, Spear of Desolation, Titan''s Bane, Lernaean Bow, The
    Crusher, Doom Orb, Avenging Blade, Toxic Blade, Dreamer''s Idol, Bragi''s Harp,
    Deathbringer, Avatar''s Parashu, Dominance, Golden Blade, Pendulum Blade, Bracer
    of The Abyss, Demon Blade, Musashi''s Dual Swords, The Executioner, The Cosmic
    Horror, Oath-Sworn Spear, Ancient Signet, Blood-Bound Book, Runeforged Hammer,
    Arondight, Chronos'' Pendant, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.37
      efficiency: 0.53
      win: 0.33
      pick: 0.23
      fit: 0.15
    Hydra's Lament:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.14
      fit: 0.28
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.19
      fit: 0.63
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.86
      win: 0.29
      pick: 0.35
      fit: 0.35
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.3
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Hydra's Lament
  - Nimble Ring
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Hydra's Lament
  - Nimble Ring
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
    this god: Tyrfing, Hydra''s Lament, Jotunn''s Revenge, Nimble Ring, Death Metal,
    Silverbranch Bow, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden
    Blade, The Reaper, Spear of the Magus, Bragi''s Harp, Heartseeker, Spear of Desolation,
    Toxic Blade, Deathbringer, Dominance, Bracer of The Abyss, Qin''s Blade, Demon
    Blade, Titan''s Bane, The Crusher, Musashi''s Dual Swords, Doom Orb, Ancient Signet,
    Blood-Bound Book, Dreamer''s Idol, Sun Beam Bow, Runeforged Hammer, Arondight,
    Damaru, Bancroft''s Talon, Rage, Berserker''s Shield, Chronos'' Pendant, The World
    Stone.'
  slot_scores:
    Tyrfing:
      total: 0.46
      efficiency: 0.48
      win: 0.43
      pick: 0.13
      fit: 0.62
    Hydra's Lament:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.14
      fit: 0.25
    Nimble Ring:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.19
      fit: 0.6
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.86
      win: 0.29
      pick: 0.35
      fit: 0.17
    Obsidian Shard:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.3
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Tyrfing
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Jotunn''s Revenge,
    Soul Gem, Tyrfing, Nimble Ring, Spear of Desolation, Death Metal, Gluttonous Grimoire,
    Spear of the Magus, Lernaean Bow, Silverbranch Bow, The Reaper, Arondight, Gem
    of Focus, Tekko-Kagi, Bragi''s Harp, Heartseeker, Bracer of The Abyss, Pendulum
    Blade, Chronos'' Pendant, Deathbringer, Doom Orb, Ancient Signet, Dominance, Blood-Bound
    Book, Golden Blade, Titan''s Bane, Totem of Death, The Crusher, Dreamer''s Idol,
    Breastplate of Valor, Toxic Blade, Bancroft''s Talon, Musashi''s Dual Swords,
    Demon Blade, Genji''s Guard, Qin''s Blade, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.43
      efficiency: 0.48
      win: 0.43
      pick: 0.13
      fit: 0.41
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.14
      fit: 0.47
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.86
      win: 0.29
      pick: 0.35
      fit: 0.2
    Obsidian Shard:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.3
      fit: 0.3
    Soul Gem:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Hydra''s Lament, Jotunn''s Revenge, Nimble
    Ring, Soul Gem, Death Metal, Tyrfing, Gluttonous Grimoire, Spear of Desolation,
    Spear of the Magus, Bragi''s Harp, Lernaean Bow, The Reaper, Bracer of The Abyss,
    Tekko-Kagi, Silverbranch Bow, Doom Orb, Heartseeker, Ancient Signet, Blood-Bound
    Book, Dreamer''s Idol, Deathbringer, Gem of Focus, Titan''s Bane, Bancroft''s
    Talon, The Crusher, Dominance, Golden Blade, Arondight, Polynomicon, Chronos''
    Pendant, Rod of Asclepius, Musashi''s Dual Swords, The Cosmic Horror, Demon Blade,
    Toxic Blade, Pendulum Blade, Typhon’s Heart, Book of Thoth, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.38
    Transcendence:
      total: 0.36
      efficiency: 0.53
      win: 0.33
      pick: 0.23
      fit: 0.13
    Hydra's Lament:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.14
      fit: 0.34
    Riptalon:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.19
      fit: 0.42
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.86
      win: 0.29
      pick: 0.35
      fit: 0.34
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.3
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Tyrfing
  - Death Metal
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Jotunn''s Revenge,
    Tyrfing, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the
    Magus, Spear of Desolation, Bragi''s Harp, The Reaper, Lernaean Bow, Tekko-Kagi,
    Heartseeker, Silverbranch Bow, Bracer of The Abyss, Doom Orb, Deathbringer, Titan''s
    Bane, The Crusher, Ancient Signet, Dominance, Golden Blade, Dreamer''s Idol, Blood-Bound
    Book, Demon Blade, Musashi''s Dual Swords, Bancroft''s Talon, Toxic Blade, Runeforged
    Hammer, Avatar''s Parashu, Arondight, Gem of Focus, The Cosmic Horror, Rod of
    Asclepius, Chronos'' Pendant, Book of Thoth, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.45
      efficiency: 0.48
      win: 0.43
      pick: 0.13
      fit: 0.52
    Hydra's Lament:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.14
      fit: 0.31
    Death Metal:
      total: 0.45
      efficiency: 0.61
      win: 0.33
      pick: 0.0
      fit: 0.55
    Riptalon:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.19
      fit: 0.47
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.3
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
    Underrated for this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Lernaean Bow, Tekko-Kagi, Tyrfing, The Reaper, Gluttonous Grimoire, Silverbranch
    Bow, Heartseeker, Bragi''s Harp, Spear of the Magus, Deathbringer, Hydra''s Lament,
    Golden Blade, Spear of Desolation, Dominance, Demon Blade, Titan''s Bane, The
    Crusher, Bracer of The Abyss, Musashi''s Dual Swords, Toxic Blade, Doom Orb, Damaru,
    Rage, The World Stone, Blood-Bound Book, Ancient Signet, Runeforged Hammer, Arondight,
    Avatar''s Parashu, Dreamer''s Idol, Qin''s Blade, Chronos'' Pendant, Pendulum
    Blade, Bancroft''s Talon.'
  slot_scores:
    Lernaean Bow:
      total: 0.41
      efficiency: 0.52
      win: 0.33
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.37
    Nimble Ring:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.43
      efficiency: 0.61
      win: 0.33
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.86
      win: 0.29
      pick: 0.35
      fit: 0.2
    Soul Gem:
      total: 0.41
      efficiency: 0.57
      win: 0.33
      pick: 0.0
      fit: 0.43
  starter: *id001
---
