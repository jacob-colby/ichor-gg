---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.75
  slot_order:
  - name: Tyrfing
    pick_rate: 0.39
    win_rate: 0.71
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.28
      win_rate: 1.0
    - name: Jotunn's Revenge
      pick_rate: 0.06
      win_rate: 0.0
  - name: Odysseus' Bow
    pick_rate: 0.28
    win_rate: 0.6
    alternates:
    - name: The Crusher
      pick_rate: 0.22
      win_rate: 1.0
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.5
  - name: Hydra's Lament
    pick_rate: 0.28
    win_rate: 1.0
    alternates:
    - name: Riptalon
      pick_rate: 0.22
      win_rate: 0.5
    - name: Hastened Fatalis
      pick_rate: 0.11
      win_rate: 1.0
  - name: Avatar's Parashu
    pick_rate: 0.29
    win_rate: 1.0
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.18
      win_rate: 0.33
    - name: Odysseus' Bow
      pick_rate: 0.18
      win_rate: 1.0
  - name: Heartseeker
    pick_rate: 0.19
    win_rate: 1.0
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.19
      win_rate: 0.67
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 1.0
  - name: Qin's Blade
    pick_rate: 0.18
    win_rate: 1.0
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.18
      win_rate: 0.5
    - name: Silverbranch Bow
      pick_rate: 0.18
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.33
    win_rate: 0.83
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.67
  - name: Bluestone Brooch
    pick_rate: 0.11
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-09-09'
  god_win_rate: 0.8333333333333334
  god_matches_won: 15
  god_matches_played: 18
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Transcendence
  - Death Metal
  - Heartseeker
  - Silverbranch Bow
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Death Metal, Tekko-Kagi, Lernaean Bow, Nimble Ring, Bragi''s Harp, Golden
    Blade, Spear of the Magus, Titan''s Bane, Spear of Desolation, Dominance, Obsidian
    Shard, Deathbringer, Soul Gem, The Reaper, Demon Blade, Toxic Blade, Gluttonous
    Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Doom Orb, Pendulum Blade,
    Transcendence, The World Stone, Arondight, Runeforged Hammer, Dreamer''s Idol,
    Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade, Berserker''s
    Shield, Jotunn''s Revenge.'
  slot_scores:
    Book of Thoth:
      total: 0.64
      efficiency: 0.51
      win: 1.0
      pick: 0.0
      fit: 0.06
    Transcendence:
      total: 0.67
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.25
    Death Metal:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.51
    Heartseeker:
      total: 0.73
      efficiency: 0.47
      win: 1.0
      pick: 0.41
      fit: 0.65
    Silverbranch Bow:
      total: 0.74
      efficiency: 0.53
      win: 1.0
      pick: 0.55
      fit: 0.53
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.28
      fit: 0.26
  community_ordered:
  - Heartseeker
  - Silverbranch Bow
  - Rod of Tahuti
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Transcendence
  - Hydra's Lament
  - Death Metal
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Spear of Desolation, Nimble Ring, Soul Gem, Spear of the Magus, Obsidian
    Shard, Bragi''s Harp, Lernaean Bow, Doom Orb, Tekko-Kagi, Gluttonous Grimoire,
    Ancient Signet, The World Stone, Chronos'' Pendant, Dominance, Bracer of The Abyss,
    Titan''s Bane, Dreamer''s Idol, Transcendence, Deathbringer, Golden Blade, The
    Reaper, Arondight, Gem of Focus, Book of Thoth, Polynomicon, Pendulum Blade, Runeforged
    Hammer, Musashi''s Dual Swords, Soul Reaver, Rod of Asclepius, The Cosmic Horror,
    Demon Blade, Jotunn''s Revenge.'
  slot_scores:
    Book of Thoth:
      total: 0.67
      efficiency: 0.51
      win: 1.0
      pick: 0.0
      fit: 0.28
    Transcendence:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.74
      efficiency: 0.54
      win: 1.0
      pick: 0.44
      fit: 0.49
    Death Metal:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.73
      efficiency: 0.47
      win: 1.0
      pick: 0.41
      fit: 0.62
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.28
      fit: 0.42
  community_ordered:
  - Hydra's Lament
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Death Metal
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Silverbranch Bow
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    Blade, Freya''s Tears, Gluttonous Grimoire, Genji''s Guard, Shifter''s Shield,
    Shield Splitter, Breastplate of Valor, Ethereal Staff, Yogi''s Necklace, Eye of
    the Storm, Pharaoh''s Curse, Lernaean Bow, Phoenix Feather, Erosion, Nimble Ring,
    Shogun''s Ofuda, Eye of Providence, Spear of the Magus, Tekko-Kagi, Draconic Scale,
    Lifebinder, Toxic Blade, Avenging Blade, Helm of Radiance, Chandra''s Grace, Jotunn''s
    Revenge.'
  slot_scores:
    Berserker's Shield:
      total: 0.75
      efficiency: 0.68
      win: 1.0
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.72
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.73
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.6
    Death Metal:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.31
    Silverbranch Bow:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.55
      fit: 0.32
    Amanita Charm:
      total: 0.78
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of the Magus
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - The Crusher
  - Spear of the Magus
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
    for this god: Tekko-Kagi, Spear of the Magus, Death Metal, Spear of Desolation,
    Obsidian Shard, Titan''s Bane, Soul Gem, The Reaper, Gluttonous Grimoire, Lernaean
    Bow, Doom Orb, Toxic Blade, The World Stone, Nimble Ring, Avenging Blade, Dreamer''s
    Idol, Pendulum Blade, Bragi''s Harp, Golden Blade, Dominance, Deathbringer, The
    Cosmic Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s
    Dual Swords, Transcendence, The Executioner, Runeforged Hammer, Arondight, Ancient
    Signet, Chronos'' Pendant, Damaru, Jotunn''s Revenge.'
  slot_scores:
    Spear of the Magus:
      total: 0.73
      efficiency: 0.6
      win: 1.0
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.74
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.73
      efficiency: 0.47
      win: 1.0
      pick: 0.3
      fit: 0.67
    Heartseeker:
      total: 0.75
      efficiency: 0.47
      win: 1.0
      pick: 0.41
      fit: 0.77
    Silverbranch Bow:
      total: 0.76
      efficiency: 0.53
      win: 1.0
      pick: 0.55
      fit: 0.64
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.28
      fit: 0.43
  community_ordered:
  - The Crusher
  - Heartseeker
  - Silverbranch Bow
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Silverbranch Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Death Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire,
    Tekko-Kagi, Golden Blade, The Reaper, Spear of the Magus, Toxic Blade, Bragi''s
    Harp, Obsidian Shard, Spear of Desolation, Dominance, Bracer of The Abyss, Titan''s
    Bane, Deathbringer, Demon Blade, Doom Orb, The World Stone, Ancient Signet, Sun
    Beam Bow, Blood-Bound Book, Transcendence, Dreamer''s Idol, Musashi''s Dual Swords,
    Chronos'' Pendant, Runeforged Hammer, Arondight, Berserker''s Shield, Bancroft''s
    Talon, Pendulum Blade, Jotunn''s Revenge.'
  slot_scores:
    Lernaean Bow:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.49
    Nimble Ring:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.32
    Rod of Tahuti:
      total: 0.79
      efficiency: 0.86
      win: 1.0
      pick: 0.28
      fit: 0.18
    Silverbranch Bow:
      total: 0.75
      efficiency: 0.53
      win: 1.0
      pick: 0.55
      fit: 0.57
    Soul Gem:
      total: 0.71
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Rod of Tahuti
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Death Metal
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    + fit + win/pick). Underrated for this god: Spear of Desolation, Soul Gem, Death
    Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Arondight, Gem of Focus,
    Obsidian Shard, Lernaean Bow, Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire,
    Bragi''s Harp, Bracer of The Abyss, Totem of Death, Doom Orb, The World Stone,
    Ancient Signet, Titan''s Bane, Breastplate of Valor, Golden Blade, Dreamer''s
    Idol, Deathbringer, Dominance, Genji''s Guard, The Reaper, Toxic Blade, Transcendence,
    Musashi''s Dual Swords, Runeforged Hammer, Demon Blade, Jotunn''s Revenge.'
  slot_scores:
    Death Metal:
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.34
    Hydra's Lament:
      total: 0.74
      efficiency: 0.54
      win: 1.0
      pick: 0.44
      fit: 0.55
    Spear of Desolation:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.28
      fit: 0.24
    Silverbranch Bow:
      total: 0.72
      efficiency: 0.53
      win: 1.0
      pick: 0.55
      fit: 0.37
    Soul Gem:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Hydra's Lament
  - Rod of Tahuti
  - Silverbranch Bow
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
    Bow, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus, Titan''s Bane,
    Spear of Desolation, Dominance, Obsidian Shard, Deathbringer, Soul Gem, The Reaper,
    Demon Blade, Toxic Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s
    Dual Swords, Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight,
    Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant,
    Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.33
      efficiency: 0.72
      win: 0.0
      pick: 0.06
      fit: 0.49
    Tyrfing:
      total: 0.61
      efficiency: 0.48
      win: 0.71
      pick: 0.39
      fit: 0.68
    Death Metal:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.72
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.28
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Rod of Tahuti
  starter: *id001
---
