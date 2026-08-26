---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.48
  aspect_win_rate: 0.63
  slot_order:
  - name: Tyrfing
    pick_rate: 0.53
    win_rate: 0.52
    alternates:
    - name: Book of Thoth
      pick_rate: 0.18
      win_rate: 0.57
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.25
  - name: Hastened Fatalis
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.2
      win_rate: 0.63
    - name: Heartwood Charm
      pick_rate: 0.08
      win_rate: 0.67
  - name: Odysseus' Bow
    pick_rate: 0.23
    win_rate: 0.67
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.15
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.67
  - name: Silverbranch Bow
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.16
      win_rate: 0.67
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.33
  - name: The Executioner
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.23
      win_rate: 0.57
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.33
  - name: Blinking Abyss
    pick_rate: 0.15
    win_rate: 0.33
    alternates:
    - name: Manchu Bow
      pick_rate: 0.1
      win_rate: 0.5
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.2
    win_rate: 0.63
  - name: Death's Embrace
    pick_rate: 0.1
    win_rate: 1.0
  - name: Death's Toll
    pick_rate: 0.1
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-08-26'
  god_win_rate: 0.525
  god_matches_won: 21
  god_matches_played: 40
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - The Executioner
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - Tekko-Kagi
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Rod of Tahuti, Death Metal, Tekko-Kagi, Lernaean Bow, Nimble Ring, Bragi''s
    Harp, Golden Blade, Spear of the Magus, Hydra''s Lament, Titan''s Bane, Spear
    of Desolation, Dominance, Obsidian Shard, Deathbringer, Soul Gem, The Reaper,
    Riptalon, Demon Blade, Toxic Blade, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence,
    The World Stone, Arondight, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage,
    Qin''s Blade, Ancient Signet, Chronos'' Pendant, Jotunn''s Revenge, Avenging Blade,
    Berserker''s Shield, The Crusher.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.59
    The Executioner:
      total: 0.64
      efficiency: 0.35
      win: 1.0
      pick: 0.28
      fit: 0.35
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.52
      pick: 0.53
      fit: 0.68
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.23
      fit: 0.53
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.69
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - The Executioner
  - Book of Thoth
  - Genji's Guard
  - Transcendence
  - Hydra's Lament
  - Rod of Tahuti
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Spear of Desolation, Hydra''s Lament, Nimble Ring, Soul
    Gem, Spear of the Magus, Obsidian Shard, Bragi''s Harp, Lernaean Bow, Doom Orb,
    Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos'' Pendant,
    Dominance, Bracer of The Abyss, Titan''s Bane, Dreamer''s Idol, Transcendence,
    Deathbringer, Golden Blade, The Reaper, Arondight, Gem of Focus, Polynomicon,
    Pendulum Blade, Jotunn''s Revenge, Runeforged Hammer, Musashi''s Dual Swords,
    Soul Reaver, Riptalon, Avatar''s Parashu, Rod of Asclepius, The Cosmic Horror,
    Demon Blade, The Crusher.'
  slot_scores:
    The Executioner:
      total: 0.62
      efficiency: 0.35
      win: 1.0
      pick: 0.28
      fit: 0.25
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.57
      pick: 0.18
      fit: 0.28
    Genji's Guard:
      total: 0.49
      efficiency: 0.45
      win: 0.67
      pick: 0.12
      fit: 0.18
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.52
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - The Executioner
  - Genji's Guard
  - Berserker's Shield
  - Shield of the Phoenix
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Silverbranch Bow
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Rod of Tahuti, Berserker''s Shield, Shield
    of the Phoenix, Rod of Asclepius, Kinetic Cuirass, Soul Gem, Death Metal, The
    Reaper, Runeforged Hammer, Golden Blade, Freya''s Tears, Riptalon, Gluttonous
    Grimoire, Shifter''s Shield, Shield Splitter, Breastplate of Valor, Ethereal Staff,
    Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse, Lernaean Bow, Phoenix Feather,
    Erosion, Nimble Ring, Shogun''s Ofuda, Eye of Providence, Spear of the Magus,
    Tekko-Kagi, Draconic Scale, Lifebinder, Toxic Blade, Avenging Blade, Helm of Radiance,
    Hydra''s Lament, Chandra''s Grace, Daybreak Gavel, Jotunn''s Revenge.'
  slot_scores:
    The Executioner:
      total: 0.62
      efficiency: 0.35
      win: 1.0
      pick: 0.28
      fit: 0.25
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.67
      pick: 0.12
      fit: 0.15
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.6
      pick: 0.23
      fit: 0.32
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - The Executioner
  - Tyrfing
  - Silverbranch Bow
  - Spear of the Magus
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Tekko-Kagi, Spear of the Magus, Death Metal, Spear
    of Desolation, Obsidian Shard, Titan''s Bane, Soul Gem, The Reaper, Gluttonous
    Grimoire, Riptalon, Lernaean Bow, Doom Orb, Toxic Blade, The World Stone, Nimble
    Ring, Avatar''s Parashu, Avenging Blade, Dreamer''s Idol, Hydra''s Lament, Pendulum
    Blade, Bragi''s Harp, Golden Blade, Dominance, Deathbringer, Jotunn''s Revenge,
    The Cosmic Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s
    Dual Swords, Transcendence, Runeforged Hammer, Arondight, Ancient Signet, Chronos''
    Pendant, Damaru, The Crusher.'
  slot_scores:
    The Executioner:
      total: 0.68
      efficiency: 0.35
      win: 1.0
      pick: 0.28
      fit: 0.59
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.52
      pick: 0.53
      fit: 0.55
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.23
      fit: 0.64
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.76
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.52
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Odysseus' Bow
  - The Executioner
  - Tyrfing
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Death Metal
  - Odysseus' Bow
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
    this god: Rod of Tahuti, Nimble Ring, Riptalon, Death Metal, Soul Gem, Lernaean
    Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Spear of the Magus,
    Toxic Blade, Bragi''s Harp, Obsidian Shard, Spear of Desolation, Dominance, Hydra''s
    Lament, Bracer of The Abyss, Qin''s Blade, Titan''s Bane, Deathbringer, Demon
    Blade, Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound Book,
    Transcendence, Dreamer''s Idol, Musashi''s Dual Swords, Chronos'' Pendant, Runeforged
    Hammer, Arondight, Berserker''s Shield, Avatar''s Parashu, Bancroft''s Talon,
    Pendulum Blade, Jotunn''s Revenge, The Crusher.'
  slot_scores:
    Odysseus' Bow:
      total: 0.49
      efficiency: 0.34
      win: 0.67
      pick: 0.36
      fit: 0.36
    The Executioner:
      total: 0.64
      efficiency: 0.35
      win: 1.0
      pick: 0.28
      fit: 0.36
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.52
      pick: 0.53
      fit: 0.67
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.32
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.23
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - The Executioner
  - Genji's Guard
  - Spear of Desolation
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Genji''s Guard, Soul Gem, Hydra''s Lament, Death Metal, Chronos'' Pendant, Nimble
    Ring, Spear of the Magus, Arondight, Gem of Focus, Obsidian Shard, Lernaean Bow,
    Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp, Bracer of The
    Abyss, Jotunn''s Revenge, Totem of Death, Doom Orb, The World Stone, Ancient Signet,
    Titan''s Bane, Riptalon, Breastplate of Valor, Golden Blade, Dreamer''s Idol,
    Deathbringer, Dominance, The Reaper, Toxic Blade, Transcendence, Musashi''s Dual
    Swords, Runeforged Hammer, Demon Blade, Qin''s Blade, Avatar''s Parashu, The Crusher.'
  slot_scores:
    The Executioner:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.28
      fit: 0.27
    Genji's Guard:
      total: 0.52
      efficiency: 0.45
      win: 0.67
      pick: 0.12
      fit: 0.34
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.59
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.23
      fit: 0.37
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.52
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.69
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
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Tekko-Kagi,
    Lernaean Bow, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus, Hydra''s
    Lament, Titan''s Bane, Spear of Desolation, The Crusher, Dominance, Obsidian Shard,
    Deathbringer, Soul Gem, The Reaper, Riptalon, Demon Blade, Toxic Blade, Gluttonous
    Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom
    Orb, Pendulum Blade, Transcendence, The World Stone, Arondight, Runeforged Hammer,
    Dreamer''s Idol, Damaru, Rage, Qin''s Blade, Ancient Signet, Chronos'' Pendant,
    Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.72
      win: 0.25
      pick: 0.1
      fit: 0.49
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.52
      pick: 0.53
      fit: 0.68
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.52
      pick: 0.0
      fit: 0.26
  starter: *id001
---
