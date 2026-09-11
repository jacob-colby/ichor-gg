---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.37
  aspect_win_rate: 0.57
  slot_order:
  - name: Tyrfing
    pick_rate: 0.55
    win_rate: 0.6
    alternates:
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.71
    - name: Daybreak Gavel
      pick_rate: 0.08
      win_rate: 1.0
  - name: Hastened Fatalis
    pick_rate: 0.29
    win_rate: 0.59
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.14
      win_rate: 0.55
    - name: Toxic Blade
      pick_rate: 0.07
      win_rate: 0.8
  - name: Odysseus' Bow
    pick_rate: 0.23
    win_rate: 0.53
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.2
      win_rate: 0.47
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.5
  - name: Silverbranch Bow
    pick_rate: 0.15
    win_rate: 0.45
    alternates:
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.56
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.75
  - name: The Executioner
    pick_rate: 0.12
    win_rate: 0.75
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.22
      win_rate: 0.73
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.6
  - name: Hunter's Bow
    pick_rate: 0.1
    win_rate: 0.6
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.12
      win_rate: 0.83
    - name: Manchu Bow
      pick_rate: 0.1
      win_rate: 0.4
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.26
    win_rate: 0.8
  - name: Death's Embrace
    pick_rate: 0.22
    win_rate: 0.65
  - name: Leather Cowl
    pick_rate: 0.13
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-09-11'
  god_win_rate: 0.631578947368421
  god_matches_won: 48
  god_matches_played: 76
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Jotunn's Revenge
  - Daybreak Gavel
  - Death Metal
  - Tekko-Kagi
  flex_slots:
  - Death Metal
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Toxic Blade, Jotunn''s Revenge, Death Metal, Tekko-Kagi,
    Lernaean Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of
    the Magus, Hydra''s Lament, Titan''s Bane, Spear of Desolation, The Crusher, Dominance,
    Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Demon Blade, Gluttonous Grimoire,
    Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum
    Blade, Transcendence, The World Stone, Arondight, Runeforged Hammer, Dreamer''s
    Idol, Damaru, Rage, Qin''s Blade, Ancient Signet, Chronos'' Pendant, Avenging
    Blade, Berserker''s Shield.'
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.44
      win: 0.8
      pick: 0.1
      fit: 0.53
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.6
      pick: 0.55
      fit: 0.68
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.49
    Daybreak Gavel:
      total: 0.63
      efficiency: 0.51
      win: 1.0
      pick: 0.08
      fit: 0.0
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Toxic Blade
  - Tyrfing
  - Daybreak Gavel
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Toxic Blade
  - Book of Thoth
  - Jotunn's Revenge
  - Daybreak Gavel
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Death Metal
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Death Metal, Book of Thoth, Spear of Desolation,
    Hydra''s Lament, Nimble Ring, Soul Gem, Spear of the Magus, Obsidian Shard, Heartseeker,
    Bragi''s Harp, Lernaean Bow, Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient
    Signet, The World Stone, Chronos'' Pendant, Dominance, Bracer of The Abyss, Titan''s
    Bane, The Crusher, Dreamer''s Idol, Transcendence, Deathbringer, Golden Blade,
    The Reaper, Arondight, Gem of Focus, Polynomicon, Pendulum Blade, Runeforged Hammer,
    Musashi''s Dual Swords, Soul Reaver, Avatar''s Parashu, Rod of Asclepius, The
    Cosmic Horror, Demon Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.57
      efficiency: 0.44
      win: 0.8
      pick: 0.1
      fit: 0.34
    Book of Thoth:
      total: 0.54
      efficiency: 0.51
      win: 0.71
      pick: 0.09
      fit: 0.28
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.52
    Daybreak Gavel:
      total: 0.63
      efficiency: 0.51
      win: 1.0
      pick: 0.08
      fit: 0.0
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Toxic Blade
  - Book of Thoth
  - Daybreak Gavel
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Daybreak Gavel
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Daybreak Gavel, Amanita Charm, Toxic Blade, Rod of Tahuti, Berserker''s
    Shield, Jotunn''s Revenge, Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass,
    Soul Gem, Death Metal, The Reaper, Runeforged Hammer, Golden Blade, Freya''s Tears,
    Gluttonous Grimoire, Genji''s Guard, Shifter''s Shield, Shield Splitter, Breastplate
    of Valor, Ethereal Staff, Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse,
    Lernaean Bow, Phoenix Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Eye of Providence,
    Spear of the Magus, Heartseeker, Tekko-Kagi, Draconic Scale, Lifebinder, Avenging
    Blade, Helm of Radiance, Hydra''s Lament, Chandra''s Grace.'
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.46
      win: 0.8
      pick: 0.1
      fit: 0.48
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.3
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.6
    Daybreak Gavel:
      total: 0.68
      efficiency: 0.59
      win: 1.0
      pick: 0.08
      fit: 0.15
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Toxic Blade
  - Daybreak Gavel
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - The Executioner
  - Jotunn's Revenge
  - Daybreak Gavel
  - Tekko-Kagi
  - Heartseeker
  flex_slots:
  - Tekko-Kagi
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Toxic Blade, Jotunn''s Revenge, Tekko-Kagi, Heartseeker,
    Spear of the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Titan''s
    Bane, Soul Gem, The Crusher, The Reaper, Gluttonous Grimoire, Lernaean Bow, Doom
    Orb, The World Stone, Nimble Ring, Avatar''s Parashu, Avenging Blade, Dreamer''s
    Idol, Hydra''s Lament, Pendulum Blade, Bragi''s Harp, Golden Blade, Dominance,
    Deathbringer, The Cosmic Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon
    Blade, Musashi''s Dual Swords, Transcendence, Runeforged Hammer, Arondight, Ancient
    Signet, Chronos'' Pendant, Damaru.'
  slot_scores:
    Toxic Blade:
      total: 0.61
      efficiency: 0.44
      win: 0.8
      pick: 0.1
      fit: 0.64
    The Executioner:
      total: 0.56
      efficiency: 0.35
      win: 0.75
      pick: 0.26
      fit: 0.59
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.61
    Daybreak Gavel:
      total: 0.63
      efficiency: 0.51
      win: 1.0
      pick: 0.08
      fit: 0.0
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.76
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Toxic Blade
  - The Executioner
  - Daybreak Gavel
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Book of Thoth
  - Tyrfing
  - Jotunn's Revenge
  - Daybreak Gavel
  - Nimble Ring
  flex_slots:
  - Nimble Ring
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death Metal,
    Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper,
    Spear of the Magus, Bragi''s Harp, Heartseeker, Obsidian Shard, Spear of Desolation,
    Dominance, Hydra''s Lament, Bracer of The Abyss, Qin''s Blade, Titan''s Bane,
    The Crusher, Deathbringer, Demon Blade, Doom Orb, The World Stone, Ancient Signet,
    Sun Beam Bow, Blood-Bound Book, Transcendence, Dreamer''s Idol, Musashi''s Dual
    Swords, Chronos'' Pendant, Runeforged Hammer, Arondight, Berserker''s Shield,
    Avatar''s Parashu, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.44
      win: 0.8
      pick: 0.1
      fit: 0.57
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.71
      pick: 0.09
      fit: 0.04
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.6
      pick: 0.55
      fit: 0.67
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.31
    Daybreak Gavel:
      total: 0.63
      efficiency: 0.51
      win: 1.0
      pick: 0.08
      fit: 0.0
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Toxic Blade
  - Book of Thoth
  - Tyrfing
  - Daybreak Gavel
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Daybreak Gavel
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Toxic Blade, Spear of Desolation, Soul Gem, Hydra''s Lament, Death Metal, Chronos''
    Pendant, Nimble Ring, Spear of the Magus, Arondight, Gem of Focus, Obsidian Shard,
    Lernaean Bow, Pendulum Blade, Tekko-Kagi, Heartseeker, Gluttonous Grimoire, Bragi''s
    Harp, Bracer of The Abyss, Totem of Death, Doom Orb, The World Stone, Ancient
    Signet, Titan''s Bane, The Crusher, Breastplate of Valor, Golden Blade, Dreamer''s
    Idol, Deathbringer, Dominance, Genji''s Guard, The Reaper, Transcendence, Musashi''s
    Dual Swords, Runeforged Hammer, Demon Blade, Qin''s Blade, Avatar''s Parashu.'
  slot_scores:
    Toxic Blade:
      total: 0.57
      efficiency: 0.44
      win: 0.8
      pick: 0.1
      fit: 0.37
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.59
    Daybreak Gavel:
      total: 0.63
      efficiency: 0.51
      win: 1.0
      pick: 0.08
      fit: 0.0
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Toxic Blade
  - Daybreak Gavel
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - Jotunn's Revenge
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
    Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Demon Blade, Toxic Blade,
    Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu,
    Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight, Runeforged
    Hammer, Dreamer''s Idol, Damaru, Rage, Qin''s Blade, Ancient Signet, Chronos''
    Pendant, Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.6
      pick: 0.55
      fit: 0.68
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Tyrfing
  starter: *id001
---
