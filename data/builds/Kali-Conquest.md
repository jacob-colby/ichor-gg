---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.64
  slot_order:
  - name: Tyrfing
    pick_rate: 0.36
    win_rate: 0.57
    alternates:
    - name: Book of Thoth
      pick_rate: 0.17
      win_rate: 0.48
    - name: Devourer's Gauntlet
      pick_rate: 0.16
      win_rate: 0.57
  - name: Odysseus' Bow
    pick_rate: 0.12
    win_rate: 0.74
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.59
    - name: Dagger of Frenzy
      pick_rate: 0.07
      win_rate: 0.43
  - name: Silverbranch Bow
    pick_rate: 0.14
    win_rate: 0.48
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.86
    - name: Hastened Fatalis
      pick_rate: 0.1
      win_rate: 0.42
  - name: Polynomicon
    pick_rate: 0.07
    win_rate: 0.54
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.14
      win_rate: 0.69
    - name: Odysseus' Bow
      pick_rate: 0.13
      win_rate: 0.5
  - name: The Executioner
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.07
      win_rate: 0.75
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.6
  - name: Bow
    pick_rate: 0.09
    win_rate: 0.55
    alternates:
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.7
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.56
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.25
    win_rate: 0.55
  - name: Archmage's Gem
    pick_rate: 0.14
    win_rate: 0.65
  - name: Death's Embrace
    pick_rate: 0.12
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-10-27'
  god_win_rate: 0.5473684210526316
  god_matches_won: 104
  god_matches_played: 190
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-27'
  god_matches_analyzed: 7385
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Odysseus' Bow
  - Tyrfing
  - Jotunn's Revenge
  - Death Metal
  - Tekko-Kagi
  flex_slots:
  - Lernaean Bow
  - Odysseus' Bow
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
    this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Tekko-Kagi, Lernaean
    Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus,
    Hydra''s Lament, Titan''s Bane, Spear of Desolation, The Crusher, Dominance, Obsidian
    Shard, Deathbringer, Soul Gem, The Reaper, Riptalon, Demon Blade, Toxic Blade,
    Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu,
    Doom Orb, Pendulum Blade, Transcendence, Berserker''s Shield, The World Stone,
    Arondight, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Qin''s Blade, Ancient
    Signet, Chronos'' Pendant, Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.59
    Odysseus' Bow:
      total: 0.51
      efficiency: 0.34
      win: 0.74
      pick: 0.16
      fit: 0.35
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.57
      pick: 0.36
      fit: 0.68
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Odysseus' Bow
  - Tyrfing
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Death Metal, Spear of Desolation, Hydra''s Lament,
    Nimble Ring, Soul Gem, Spear of the Magus, Obsidian Shard, Heartseeker, Bragi''s
    Harp, Lernaean Bow, Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet,
    The World Stone, Chronos'' Pendant, Dominance, Bracer of The Abyss, Titan''s Bane,
    The Crusher, Dreamer''s Idol, Transcendence, Deathbringer, Golden Blade, The Reaper,
    Arondight, Gem of Focus, Polynomicon, Pendulum Blade, Runeforged Hammer, Musashi''s
    Dual Swords, Soul Reaver, Riptalon, Avatar''s Parashu, Rod of Asclepius, The Cosmic
    Horror, Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.57
      pick: 0.36
      fit: 0.51
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Jotunn''s Revenge,
    Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass, Soul Gem, Death Metal,
    The Reaper, Runeforged Hammer, Golden Blade, Freya''s Tears, Riptalon, Gluttonous
    Grimoire, Genji''s Guard, Shifter''s Shield, Shield Splitter, Breastplate of Valor,
    Ethereal Staff, Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse, Lernaean
    Bow, Phoenix Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Eye of Providence,
    Spear of the Magus, Heartseeker, Tekko-Kagi, Draconic Scale, Lifebinder, Toxic
    Blade, Avenging Blade, Helm of Radiance, Hydra''s Lament, Chandra''s Grace, Daybreak
    Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.12
      fit: 0.42
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.57
      pick: 0.36
      fit: 0.45
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Berserker's Shield
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Tekko-Kagi
  - Heartseeker
  - Rod of Tahuti
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Tekko-Kagi, Heartseeker, Spear
    of the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Titan''s Bane,
    Soul Gem, The Crusher, The Reaper, Gluttonous Grimoire, Riptalon, Lernaean Bow,
    Doom Orb, Toxic Blade, The World Stone, Nimble Ring, Avatar''s Parashu, Avenging
    Blade, Dreamer''s Idol, Hydra''s Lament, Pendulum Blade, Bragi''s Harp, Golden
    Blade, Dominance, Deathbringer, The Cosmic Horror, Bracer of The Abyss, Oath-Sworn
    Spear, Demon Blade, Musashi''s Dual Swords, Transcendence, Runeforged Hammer,
    Arondight, Ancient Signet, Chronos'' Pendant, Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.41
      efficiency: 0.51
      win: 0.48
      pick: 0.17
      fit: 0.05
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.61
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.19
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.76
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Book of Thoth
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Odysseus' Bow
  - Tyrfing
  - Nimble Ring
  - Death Metal
  - Riptalon
  flex_slots:
  - Odysseus' Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Riptalon, Death Metal,
    Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper,
    Spear of the Magus, Toxic Blade, Bragi''s Harp, Heartseeker, Obsidian Shard, Spear
    of Desolation, Dominance, Hydra''s Lament, Bracer of The Abyss, Qin''s Blade,
    Berserker''s Shield, Titan''s Bane, The Crusher, Deathbringer, Demon Blade, Doom
    Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound Book, Transcendence,
    Dreamer''s Idol, Musashi''s Dual Swords, Chronos'' Pendant, Runeforged Hammer,
    Arondight, Avatar''s Parashu, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.31
    Odysseus' Bow:
      total: 0.51
      efficiency: 0.34
      win: 0.74
      pick: 0.16
      fit: 0.36
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.57
      pick: 0.36
      fit: 0.67
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.32
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Odysseus' Bow
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Hydra's Lament
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Spear of Desolation, Soul Gem, Hydra''s Lament, Death Metal, Chronos'' Pendant,
    Nimble Ring, Spear of the Magus, Arondight, Gem of Focus, Obsidian Shard, Lernaean
    Bow, Pendulum Blade, Tekko-Kagi, Heartseeker, Gluttonous Grimoire, Bragi''s Harp,
    Bracer of The Abyss, Totem of Death, Doom Orb, The World Stone, Ancient Signet,
    Titan''s Bane, Riptalon, The Crusher, Breastplate of Valor, Golden Blade, Dreamer''s
    Idol, Deathbringer, Dominance, Genji''s Guard, The Reaper, Toxic Blade, Transcendence,
    Musashi''s Dual Swords, Runeforged Hammer, Demon Blade, Qin''s Blade, Avatar''s
    Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.55
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.56
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
    Lernaean Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of
    the Magus, Hydra''s Lament, Titan''s Bane, Spear of Desolation, The Crusher, Dominance,
    Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Riptalon, Demon Blade, Toxic
    Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s
    Parashu, Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight,
    Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Qin''s Blade, Ancient Signet,
    Chronos'' Pendant, Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.57
      pick: 0.36
      fit: 0.68
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Tyrfing
  starter: *id001
---
