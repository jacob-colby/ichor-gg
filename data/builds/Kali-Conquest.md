---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.28
  aspect_win_rate: 0.51
  slot_order:
  - name: Tyrfing
    pick_rate: 0.37
    win_rate: 0.57
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.15
      win_rate: 0.47
    - name: Devourer's Gauntlet
      pick_rate: 0.14
      win_rate: 0.53
  - name: Odysseus' Bow
    pick_rate: 0.2
    win_rate: 0.65
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.07
      win_rate: 0.24
    - name: Spear of Desolation
      pick_rate: 0.06
      win_rate: 0.5
  - name: Hastened Fatalis
    pick_rate: 0.14
    win_rate: 0.58
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.12
      win_rate: 0.67
    - name: Odysseus' Bow
      pick_rate: 0.08
      win_rate: 0.28
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 0.41
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.14
      win_rate: 0.56
    - name: Silverbranch Bow
      pick_rate: 0.09
      win_rate: 0.55
  - name: Silverbranch Bow
    pick_rate: 0.09
    win_rate: 0.56
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.69
    - name: The Executioner
      pick_rate: 0.07
      win_rate: 0.57
  - name: Blinking Abyss
    pick_rate: 0.11
    win_rate: 0.71
    alternates:
    - name: Manchu Bow
      pick_rate: 0.07
      win_rate: 0.36
    - name: Bow
      pick_rate: 0.06
      win_rate: 0.56
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.57
  - name: Archmage's Gem
    pick_rate: 0.13
    win_rate: 0.57
  - name: Bumba's Hammer
    pick_rate: 0.12
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-10-13'
  god_win_rate: 0.5169491525423728
  god_matches_won: 122
  god_matches_played: 236
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-13'
  god_matches_analyzed: 7865
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Heartseeker
  flex_slots:
  - Lernaean Bow
  - Heartseeker
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
    this god: Death Metal, Tekko-Kagi, Lernaean Bow, Heartseeker, Nimble Ring, Bragi''s
    Harp, Golden Blade, Spear of the Magus, Titan''s Bane, The Crusher, Dominance,
    Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Riptalon, Demon Blade, Toxic
    Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s
    Parashu, Doom Orb, Spear of Desolation, Pendulum Blade, Transcendence, The World
    Stone, Arondight, Runeforged Hammer, Dreamer''s Idol, Hydra''s Lament, Damaru,
    Rage, Qin''s Blade, Ancient Signet, Chronos'' Pendant, Avenging Blade, Berserker''s
    Shield, Jotunn''s Revenge.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.57
      pick: 0.37
      fit: 0.68
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.19
      fit: 0.53
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.69
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Transcendence
  - Death Metal
  - Doom Orb
  - Heartseeker
  - Rod of Tahuti
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Nimble Ring, Soul Gem, Spear of the Magus, Obsidian Shard, Heartseeker,
    Bragi''s Harp, Lernaean Bow, Doom Orb, Spear of Desolation, Tekko-Kagi, Gluttonous
    Grimoire, Ancient Signet, The World Stone, Chronos'' Pendant, Dominance, Bracer
    of The Abyss, Titan''s Bane, The Crusher, Hydra''s Lament, Dreamer''s Idol, Transcendence,
    Deathbringer, Golden Blade, The Reaper, Arondight, Gem of Focus, Book of Thoth,
    Polynomicon, Pendulum Blade, Runeforged Hammer, Musashi''s Dual Swords, Soul Reaver,
    Riptalon, Avatar''s Parashu, Rod of Asclepius, The Cosmic Horror, Demon Blade,
    Jotunn''s Revenge.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.28
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.28
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.54
    Doom Orb:
      total: 0.5
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.41
      pick: 0.17
      fit: 0.42
  community_ordered:
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Shield of the Phoenix
  - Death Metal
  - Amanita Charm
  flex_slots:
  - Death Metal
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
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Soul Gem, Death Metal, The Reaper, Runeforged Hammer, Golden
    Blade, Freya''s Tears, Riptalon, Gluttonous Grimoire, Genji''s Guard, Shifter''s
    Shield, Shield Splitter, Breastplate of Valor, Ethereal Staff, Yogi''s Necklace,
    Eye of the Storm, Pharaoh''s Curse, Lernaean Bow, Phoenix Feather, Erosion, Nimble
    Ring, Shogun''s Ofuda, Eye of Providence, Spear of the Magus, Heartseeker, Tekko-Kagi,
    Draconic Scale, Lifebinder, Toxic Blade, Avenging Blade, Helm of Radiance, Chandra''s
    Grace, Daybreak Gavel, Hydra''s Lament, Jotunn''s Revenge.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.42
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
      pick: 0.37
      fit: 0.45
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.6
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Tyrfing
  - Spear of the Magus
  - Silverbranch Bow
  - Tekko-Kagi
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Spear of the Magus
  - Tyrfing
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
    for this god: Tekko-Kagi, Heartseeker, Spear of the Magus, Death Metal, Obsidian
    Shard, Titan''s Bane, Soul Gem, The Crusher, The Reaper, Gluttonous Grimoire,
    Riptalon, Lernaean Bow, Doom Orb, Toxic Blade, Spear of Desolation, The World
    Stone, Nimble Ring, Avatar''s Parashu, Avenging Blade, Dreamer''s Idol, Pendulum
    Blade, Bragi''s Harp, Golden Blade, Dominance, Deathbringer, The Cosmic Horror,
    Bracer of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords, Transcendence,
    Runeforged Hammer, Arondight, Ancient Signet, Hydra''s Lament, Chronos'' Pendant,
    Jotunn''s Revenge, Damaru.'
  slot_scores:
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.57
      pick: 0.37
      fit: 0.55
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.43
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.56
      pick: 0.19
      fit: 0.64
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
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.17
      fit: 0.43
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - Nimble Ring
  - Death Metal
  - Silverbranch Bow
  - Riptalon
  flex_slots:
  - Death Metal
  - Lernaean Bow
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
    this god: Nimble Ring, Riptalon, Death Metal, Soul Gem, Lernaean Bow, Gluttonous
    Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Spear of the Magus, Toxic Blade,
    Bragi''s Harp, Heartseeker, Obsidian Shard, Dominance, Bracer of The Abyss, Qin''s
    Blade, Titan''s Bane, The Crusher, Deathbringer, Demon Blade, Doom Orb, Spear
    of Desolation, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound Book,
    Transcendence, Dreamer''s Idol, Musashi''s Dual Swords, Chronos'' Pendant, Runeforged
    Hammer, Arondight, Berserker''s Shield, Avatar''s Parashu, Bancroft''s Talon,
    Hydra''s Lament, Pendulum Blade, Jotunn''s Revenge.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.57
      pick: 0.37
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
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.19
      fit: 0.57
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Tyrfing
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Soul Gem, Spear of Desolation, Death
    Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Arondight, Gem of Focus,
    Obsidian Shard, Hydra''s Lament, Lernaean Bow, Pendulum Blade, Tekko-Kagi, Heartseeker,
    Gluttonous Grimoire, Bragi''s Harp, Bracer of The Abyss, Totem of Death, Doom
    Orb, The World Stone, Ancient Signet, Titan''s Bane, Riptalon, The Crusher, Breastplate
    of Valor, Golden Blade, Dreamer''s Idol, Deathbringer, Dominance, Genji''s Guard,
    The Reaper, Toxic Blade, Transcendence, Jotunn''s Revenge, Musashi''s Dual Swords,
    Runeforged Hammer, Demon Blade, Qin''s Blade, Avatar''s Parashu.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.57
      pick: 0.37
      fit: 0.44
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.08
      fit: 0.59
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.41
      pick: 0.17
      fit: 0.24
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Tyrfing
  - Spear of Desolation
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
    Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus,
    Hydra''s Lament, Titan''s Bane, Spear of Desolation, The Crusher, Dominance, Obsidian
    Shard, Deathbringer, Soul Gem, The Reaper, Riptalon, Demon Blade, Toxic Blade,
    Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu,
    Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight, Runeforged
    Hammer, Dreamer''s Idol, Damaru, Rage, Qin''s Blade, Ancient Signet, Chronos''
    Pendant, Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.72
      win: 0.24
      pick: 0.1
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.57
      pick: 0.37
      fit: 0.68
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.41
      pick: 0.17
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Rod of Tahuti
  starter: *id001
---
