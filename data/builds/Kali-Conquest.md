---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.64
  slot_order:
  - name: Tyrfing
    pick_rate: 0.45
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.5
    - name: Jotunn's Revenge
      pick_rate: 0.07
      win_rate: 0.5
  - name: Toxic Blade
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.1
      win_rate: 0.33
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.67
  - name: Silverbranch Bow
    pick_rate: 0.17
    win_rate: 0.4
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.14
      win_rate: 0.75
    - name: Odysseus' Bow
      pick_rate: 0.14
      win_rate: 0.25
  - name: Hastened Fatalis
    pick_rate: 0.18
    win_rate: 0.6
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.5
    - name: Odysseus' Bow
      pick_rate: 0.14
      win_rate: 0.5
  - name: Riptalon
    pick_rate: 0.15
    win_rate: 0.75
    alternates:
    - name: Dominance
      pick_rate: 0.12
      win_rate: 0.33
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 1.0
  - name: The Executioner
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Manchu Bow
      pick_rate: 0.1
      win_rate: 0.5
    - name: Bow
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.28
    win_rate: 0.5
  - name: Archmage's Gem
    pick_rate: 0.17
    win_rate: 0.6
  - name: Death's Embrace
    pick_rate: 0.17
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-10-08'
  god_win_rate: 0.5517241379310345
  god_matches_won: 16
  god_matches_played: 29
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Spear of Desolation
  - Riptalon
  - Heartseeker
  flex_slots:
  - Tyrfing
  - Death Metal
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
    this god: Spear of Desolation, Jotunn''s Revenge, Death Metal, Tekko-Kagi, Lernaean
    Bow, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus, Hydra''s Lament,
    Titan''s Bane, The Crusher, Obsidian Shard, Deathbringer, Soul Gem, The Reaper,
    Demon Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords,
    Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight,
    Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Qin''s Blade, Ancient Signet,
    Chronos'' Pendant, Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.07
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.54
      pick: 0.45
      fit: 0.68
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.67
      pick: 0.14
      fit: 0.31
    Riptalon:
      total: 0.59
      efficiency: 0.46
      win: 0.75
      pick: 0.32
      fit: 0.53
    Heartseeker:
      total: 0.72
      efficiency: 0.47
      win: 1.0
      pick: 0.17
      fit: 0.65
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Riptalon
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Riptalon
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Death Metal
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of Desolation, Jotunn''s Revenge, Death Metal, Hydra''s Lament, Nimble Ring, Soul
    Gem, Spear of the Magus, Obsidian Shard, Bragi''s Harp, Lernaean Bow, Doom Orb,
    Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos'' Pendant,
    Bracer of The Abyss, Titan''s Bane, The Crusher, Dreamer''s Idol, Book of Thoth,
    Transcendence, Deathbringer, Golden Blade, The Reaper, Arondight, Gem of Focus,
    Polynomicon, Pendulum Blade, Runeforged Hammer, Musashi''s Dual Swords, Soul Reaver,
    Avatar''s Parashu, Rod of Asclepius, The Cosmic Horror, Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.07
      fit: 0.52
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.67
      pick: 0.14
      fit: 0.45
    Riptalon:
      total: 0.56
      efficiency: 0.46
      win: 0.75
      pick: 0.32
      fit: 0.34
    Heartseeker:
      total: 0.71
      efficiency: 0.47
      win: 1.0
      pick: 0.17
      fit: 0.62
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.23
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Spear of Desolation
  - Riptalon
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Spear of Desolation
  - Riptalon
  - Heartseeker
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
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, Rod of Asclepius, Kinetic Cuirass, Soul Gem, Death Metal, The Reaper,
    Runeforged Hammer, Golden Blade, Freya''s Tears, Gluttonous Grimoire, Genji''s
    Guard, Shifter''s Shield, Shield Splitter, Breastplate of Valor, Ethereal Staff,
    Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse, Lernaean Bow, Phoenix Feather,
    Erosion, Nimble Ring, Shogun''s Ofuda, Eye of Providence, Spear of the Magus,
    Tekko-Kagi, Draconic Scale, Lifebinder, Avenging Blade, Helm of Radiance, Hydra''s
    Lament, Chandra''s Grace, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.07
      fit: 0.3
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.67
      pick: 0.14
      fit: 0.19
    Riptalon:
      total: 0.61
      efficiency: 0.46
      win: 0.75
      pick: 0.32
      fit: 0.62
    Heartseeker:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.17
      fit: 0.47
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Spear of Desolation
  - Riptalon
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Riptalon
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of Desolation, Jotunn''s Revenge, Tekko-Kagi, Spear of the
    Magus, Death Metal, Obsidian Shard, Titan''s Bane, Soul Gem, The Crusher, The
    Reaper, Gluttonous Grimoire, Lernaean Bow, Doom Orb, The World Stone, Nimble Ring,
    Avatar''s Parashu, Avenging Blade, Dreamer''s Idol, Hydra''s Lament, Pendulum
    Blade, Bragi''s Harp, Golden Blade, Deathbringer, The Cosmic Horror, Bracer of
    The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords, Transcendence,
    Runeforged Hammer, Arondight, Ancient Signet, Chronos'' Pendant, Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.51
      win: 0.5
      pick: 0.14
      fit: 0.05
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.07
      fit: 0.61
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.67
      pick: 0.14
      fit: 0.47
    Riptalon:
      total: 0.61
      efficiency: 0.46
      win: 0.75
      pick: 0.32
      fit: 0.64
    Heartseeker:
      total: 0.74
      efficiency: 0.47
      win: 1.0
      pick: 0.17
      fit: 0.77
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.23
      fit: 0.43
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Riptalon
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Spear of Desolation
  - Riptalon
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
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
    this god: Spear of Desolation, Jotunn''s Revenge, Nimble Ring, Death Metal, Soul
    Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper,
    Spear of the Magus, Bragi''s Harp, Obsidian Shard, Hydra''s Lament, Bracer of
    The Abyss, Qin''s Blade, Titan''s Bane, The Crusher, Deathbringer, Demon Blade,
    Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound Book, Transcendence,
    Dreamer''s Idol, Musashi''s Dual Swords, Chronos'' Pendant, Runeforged Hammer,
    Arondight, Berserker''s Shield, Avatar''s Parashu, Bancroft''s Talon, Pendulum
    Blade.'
  slot_scores:
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.54
      pick: 0.45
      fit: 0.67
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.67
      pick: 0.14
      fit: 0.21
    Riptalon:
      total: 0.63
      efficiency: 0.51
      win: 0.75
      pick: 0.32
      fit: 0.65
    Heartseeker:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.17
      fit: 0.47
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.23
      fit: 0.18
  community_ordered:
  - Tyrfing
  - Spear of Desolation
  - Riptalon
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Spear of Desolation, Jotunn''s Revenge,
    Soul Gem, Hydra''s Lament, Death Metal, Chronos'' Pendant, Nimble Ring, Spear
    of the Magus, Arondight, Gem of Focus, Obsidian Shard, Lernaean Bow, Pendulum
    Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp, Bracer of The Abyss, Totem
    of Death, Doom Orb, The World Stone, Ancient Signet, Titan''s Bane, The Crusher,
    Breastplate of Valor, Golden Blade, Dreamer''s Idol, Deathbringer, Genji''s Guard,
    The Reaper, Transcendence, Musashi''s Dual Swords, Runeforged Hammer, Demon Blade,
    Qin''s Blade, Avatar''s Parashu.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.5
      pick: 0.14
      fit: 0.1
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.07
      fit: 0.59
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.67
      pick: 0.14
      fit: 0.59
    Heartseeker:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.17
      fit: 0.44
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.5
      pick: 0.23
      fit: 0.24
    Soul Gem:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
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
    Underrated for this god: Jotunn''s Revenge, Death Metal, Tekko-Kagi, Lernaean
    Bow, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus, Hydra''s Lament,
    Titan''s Bane, Spear of Desolation, The Crusher, Obsidian Shard, Deathbringer,
    Soul Gem, The Reaper, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s
    Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence, The World
    Stone, Arondight, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Qin''s Blade,
    Ancient Signet, Chronos'' Pendant, Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.07
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.54
      pick: 0.45
      fit: 0.68
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.23
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Rod of Tahuti
  starter: *id001
---
