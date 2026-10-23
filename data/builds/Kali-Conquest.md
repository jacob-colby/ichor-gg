---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.39
  aspect_win_rate: 0.62
  slot_order:
  - name: Tyrfing
    pick_rate: 0.27
    win_rate: 0.6
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.27
      win_rate: 0.65
    - name: Book of Thoth
      pick_rate: 0.24
      win_rate: 0.56
  - name: Soul Gem
    pick_rate: 0.13
    win_rate: 0.4
    alternates:
    - name: Bragi's Harp
      pick_rate: 0.11
      win_rate: 0.63
    - name: Odysseus' Bow
      pick_rate: 0.08
      win_rate: 0.67
  - name: Odysseus' Bow
    pick_rate: 0.15
    win_rate: 0.91
    alternates:
    - name: Ancient Signet
      pick_rate: 0.12
      win_rate: 0.44
    - name: Silverbranch Bow
      pick_rate: 0.09
      win_rate: 0.43
  - name: Silverbranch Bow
    pick_rate: 0.2
    win_rate: 0.86
    alternates:
    - name: Polynomicon
      pick_rate: 0.13
      win_rate: 0.56
    - name: Odysseus' Bow
      pick_rate: 0.07
      win_rate: 0.6
  - name: The Executioner
    pick_rate: 0.17
    win_rate: 0.55
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.11
      win_rate: 0.71
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.67
  - name: Manchu Bow
    pick_rate: 0.09
    win_rate: 0.75
    alternates:
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 1.0
    - name: Spear of the Magus
      pick_rate: 0.09
      win_rate: 0.5
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.23
    win_rate: 0.59
  - name: Archmage's Gem
    pick_rate: 0.17
    win_rate: 0.62
  - name: Death's Embrace
    pick_rate: 0.13
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-10-23'
  god_win_rate: 0.5733333333333334
  god_matches_won: 43
  god_matches_played: 75
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-23'
  god_matches_analyzed: 2743
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Odysseus' Bow
  - Jotunn's Revenge
  - Death Metal
  - Silverbranch Bow
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Odysseus' Bow
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
    this god: Jotunn''s Revenge, Death Metal, Tekko-Kagi, Lernaean Bow, Heartseeker,
    Nimble Ring, Golden Blade, Hydra''s Lament, Titan''s Bane, Spear of Desolation,
    The Crusher, Dominance, Obsidian Shard, Deathbringer, The Reaper, Demon Blade,
    Toxic Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords,
    Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight,
    Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Qin''s Blade, Chronos'' Pendant,
    Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Odysseus' Bow:
      total: 0.59
      efficiency: 0.34
      win: 0.91
      pick: 0.23
      fit: 0.35
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.67
      efficiency: 0.53
      win: 0.86
      pick: 0.33
      fit: 0.53
    Riptalon:
      total: 0.7
      efficiency: 0.46
      win: 1.0
      pick: 0.28
      fit: 0.53
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.67
      pick: 0.19
      fit: 0.26
  community_ordered:
  - Odysseus' Bow
  - Silverbranch Bow
  - Riptalon
  - Rod of Tahuti
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Silverbranch Bow
  - Riptalon
  - Rod of Tahuti
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Death Metal, Spear of Desolation, Hydra''s Lament, Nimble Ring, Obsidian
    Shard, Heartseeker, Lernaean Bow, Doom Orb, Tekko-Kagi, Gluttonous Grimoire, The
    World Stone, Chronos'' Pendant, Dominance, Bracer of The Abyss, Titan''s Bane,
    The Crusher, Dreamer''s Idol, Transcendence, Deathbringer, Golden Blade, The Reaper,
    Arondight, Gem of Focus, Pendulum Blade, Runeforged Hammer, Musashi''s Dual Swords,
    Soul Reaver, Avatar''s Parashu, Rod of Asclepius, The Cosmic Horror, Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.63
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.54
    Silverbranch Bow:
      total: 0.64
      efficiency: 0.53
      win: 0.86
      pick: 0.33
      fit: 0.34
    Riptalon:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.28
      fit: 0.34
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.19
      fit: 0.42
  community_ordered:
  - Silverbranch Bow
  - Riptalon
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Odysseus' Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Silverbranch Bow
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Odysseus' Bow
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
    Phoenix, Rod of Asclepius, Kinetic Cuirass, Death Metal, The Reaper, Runeforged
    Hammer, Golden Blade, Freya''s Tears, Gluttonous Grimoire, Genji''s Guard, Shifter''s
    Shield, Shield Splitter, Breastplate of Valor, Ethereal Staff, Yogi''s Necklace,
    Eye of the Storm, Pharaoh''s Curse, Lernaean Bow, Phoenix Feather, Erosion, Nimble
    Ring, Shogun''s Ofuda, Eye of Providence, Heartseeker, Tekko-Kagi, Draconic Scale,
    Lifebinder, Toxic Blade, Avenging Blade, Helm of Radiance, Hydra''s Lament, Chandra''s
    Grace, Daybreak Gavel.'
  slot_scores:
    Odysseus' Bow:
      total: 0.58
      efficiency: 0.34
      win: 0.91
      pick: 0.23
      fit: 0.25
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.3
    Silverbranch Bow:
      total: 0.64
      efficiency: 0.53
      win: 0.86
      pick: 0.33
      fit: 0.32
    Riptalon:
      total: 0.72
      efficiency: 0.46
      win: 1.0
      pick: 0.28
      fit: 0.62
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Odysseus' Bow
  - Silverbranch Bow
  - Riptalon
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Odysseus' Bow
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Odysseus' Bow
  - Tekko-Kagi
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
    for this god: Jotunn''s Revenge, Tekko-Kagi, Heartseeker, Death Metal, Spear of
    Desolation, Obsidian Shard, Titan''s Bane, The Crusher, The Reaper, Gluttonous
    Grimoire, Lernaean Bow, Doom Orb, Toxic Blade, The World Stone, Nimble Ring, Avatar''s
    Parashu, Avenging Blade, Dreamer''s Idol, Hydra''s Lament, Pendulum Blade, Golden
    Blade, Dominance, Deathbringer, The Cosmic Horror, Bracer of The Abyss, Oath-Sworn
    Spear, Demon Blade, Musashi''s Dual Swords, Transcendence, Runeforged Hammer,
    Arondight, Chronos'' Pendant, Damaru.'
  slot_scores:
    Odysseus' Bow:
      total: 0.58
      efficiency: 0.34
      win: 0.91
      pick: 0.23
      fit: 0.29
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.61
    Riptalon:
      total: 0.72
      efficiency: 0.46
      win: 1.0
      pick: 0.28
      fit: 0.64
    Silverbranch Bow:
      total: 0.68
      efficiency: 0.53
      win: 0.86
      pick: 0.33
      fit: 0.64
    Tekko-Kagi:
      total: 0.57
      efficiency: 0.49
      win: 0.63
      pick: 0.0
      fit: 0.76
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.19
      fit: 0.43
  community_ordered:
  - Odysseus' Bow
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Odysseus' Bow
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
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
    this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Lernaean Bow, Gluttonous
    Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Toxic Blade, Heartseeker, Obsidian
    Shard, Spear of Desolation, Dominance, Hydra''s Lament, Bracer of The Abyss, Qin''s
    Blade, Titan''s Bane, The Crusher, Deathbringer, Demon Blade, Doom Orb, The World
    Stone, Sun Beam Bow, Blood-Bound Book, Transcendence, Dreamer''s Idol, Musashi''s
    Dual Swords, Chronos'' Pendant, Runeforged Hammer, Arondight, Berserker''s Shield,
    Avatar''s Parashu, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Odysseus' Bow:
      total: 0.59
      efficiency: 0.34
      win: 0.91
      pick: 0.23
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.31
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.27
      fit: 0.67
    Silverbranch Bow:
      total: 0.67
      efficiency: 0.53
      win: 0.86
      pick: 0.33
      fit: 0.57
    Riptalon:
      total: 0.74
      efficiency: 0.51
      win: 1.0
      pick: 0.28
      fit: 0.65
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.19
      fit: 0.18
  community_ordered:
  - Odysseus' Bow
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Odysseus' Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Silverbranch Bow
  - Riptalon
  flex_slots:
  - Spear of Desolation
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Spear of Desolation,
    Hydra''s Lament, Death Metal, Chronos'' Pendant, Nimble Ring, Arondight, Gem of
    Focus, Obsidian Shard, Lernaean Bow, Pendulum Blade, Tekko-Kagi, Heartseeker,
    Gluttonous Grimoire, Bracer of The Abyss, Totem of Death, Doom Orb, The World
    Stone, Titan''s Bane, The Crusher, Breastplate of Valor, Golden Blade, Dreamer''s
    Idol, Deathbringer, Dominance, Genji''s Guard, The Reaper, Toxic Blade, Transcendence,
    Musashi''s Dual Swords, Runeforged Hammer, Demon Blade, Qin''s Blade, Avatar''s
    Parashu.'
  slot_scores:
    Odysseus' Bow:
      total: 0.58
      efficiency: 0.34
      win: 0.91
      pick: 0.23
      fit: 0.27
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.63
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.59
    Silverbranch Bow:
      total: 0.64
      efficiency: 0.53
      win: 0.86
      pick: 0.33
      fit: 0.37
    Riptalon:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.28
      fit: 0.37
  community_ordered:
  - Odysseus' Bow
  - Silverbranch Bow
  - Riptalon
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
    Bow, Heartseeker, Nimble Ring, Golden Blade, Hydra''s Lament, Titan''s Bane, Spear
    of Desolation, The Crusher, Dominance, Obsidian Shard, Deathbringer, The Reaper,
    Demon Blade, Toxic Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s
    Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence, The World
    Stone, Arondight, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Qin''s Blade,
    Chronos'' Pendant, Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.27
      fit: 0.68
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.63
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.67
      pick: 0.19
      fit: 0.26
  community_ordered:
  - Tyrfing
  - Rod of Tahuti
  starter: *id001
---
