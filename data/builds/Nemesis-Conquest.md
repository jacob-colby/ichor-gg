---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.35
  aspect_win_rate: 0.45
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.23
    win_rate: 0.86
    alternates:
    - name: Golden Blade
      pick_rate: 0.19
      win_rate: 0.5
    - name: Daybreak Gavel
      pick_rate: 0.19
      win_rate: 0.83
  - name: The Crusher
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 1.0
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.33
  - name: The Reaper
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.1
      win_rate: 0.0
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.5
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.0
    alternates:
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 1.0
  - name: Veve Charm
    pick_rate: 0.09
    win_rate: 0.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Infused Axe
      pick_rate: 0.15
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.26
    win_rate: 0.5
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.6
  - name: Bumba's Cudgel
    pick_rate: 0.13
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-09-10'
  god_win_rate: 0.4838709677419355
  god_matches_won: 15
  god_matches_played: 31
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Hydra's Lament
  - Daybreak Gavel
  - Freya's Tears
  - The Crusher
  - Heartseeker
  flex_slots:
  - The Crusher
  - Daybreak Gavel
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Tyrfing, Tekko-Kagi,
    Silverbranch Bow, Lernaean Bow, Nimble Ring, Bragi''s Harp, Spear of the Magus,
    Riptalon, Spear of Desolation, Titan''s Bane, Dominance, Obsidian Shard, Deathbringer,
    Soul Gem, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence,
    The World Stone, Arondight, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol,
    Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.66
      efficiency: 0.46
      win: 1.0
      pick: 0.14
      fit: 0.25
    Hydra's Lament:
      total: 0.65
      efficiency: 0.54
      win: 0.86
      pick: 0.23
      fit: 0.39
    Daybreak Gavel:
      total: 0.56
      efficiency: 0.51
      win: 0.83
      pick: 0.19
      fit: 0.0
    Freya's Tears:
      total: 0.59
      efficiency: 0.36
      win: 1.0
      pick: 0.19
      fit: 0.04
    The Crusher:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.18
      fit: 0.54
    Heartseeker:
      total: 0.72
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.64
  community_ordered:
  - Berserker's Shield
  - Hydra's Lament
  - Daybreak Gavel
  - Freya's Tears
  - The Crusher
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Berserker's Shield
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Rod of Tahuti
  - The Crusher
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
    of Tahuti, Jotunn''s Revenge, Death Metal, Spear of Desolation, Nimble Ring, Soul
    Gem, Spear of the Magus, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow,
    Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos''
    Pendant, Silverbranch Bow, Dominance, Bracer of The Abyss, Titan''s Bane, Dreamer''s
    Idol, Transcendence, Deathbringer, Arondight, Gem of Focus, Book of Thoth, Polynomicon,
    Pendulum Blade, Riptalon, Runeforged Hammer, Musashi''s Dual Swords, Soul Reaver,
    Avatar''s Parashu, Rod of Asclepius, The Cosmic Horror, Toxic Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.64
      efficiency: 0.46
      win: 1.0
      pick: 0.14
      fit: 0.15
    Hydra's Lament:
      total: 0.66
      efficiency: 0.54
      win: 0.86
      pick: 0.23
      fit: 0.49
    Freya's Tears:
      total: 0.6
      efficiency: 0.36
      win: 1.0
      pick: 0.19
      fit: 0.1
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.18
      fit: 0.44
    Heartseeker:
      total: 0.72
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.62
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Hydra's Lament
  - Daybreak Gavel
  - Freya's Tears
  - The Crusher
  - Heartseeker
  flex_slots:
  - Daybreak Gavel
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Rod of Tahuti, Jotunn''s Revenge,
    Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass, Soul Gem, Death Metal,
    Riptalon, Runeforged Hammer, Gluttonous Grimoire, Breastplate of Valor, Shield
    Splitter, Ethereal Staff, Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse,
    Tyrfing, Lernaean Bow, Phoenix Feather, Erosion, Nimble Ring, Shogun''s Ofuda,
    Toxic Blade, Silverbranch Bow, Eye of Providence, Spear of the Magus, Tekko-Kagi,
    Lifebinder, Draconic Scale, Avenging Blade, Helm of Radiance, Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.76
      efficiency: 0.68
      win: 1.0
      pick: 0.14
      fit: 0.42
    Hydra's Lament:
      total: 0.63
      efficiency: 0.54
      win: 0.86
      pick: 0.23
      fit: 0.28
    Daybreak Gavel:
      total: 0.61
      efficiency: 0.59
      win: 0.83
      pick: 0.19
      fit: 0.15
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.19
      fit: 0.27
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.75
      pick: 0.18
      fit: 0.37
    Heartseeker:
      total: 0.7
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.47
  community_ordered:
  - Berserker's Shield
  - Hydra's Lament
  - Daybreak Gavel
  - Freya's Tears
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  - Heartseeker
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Silverbranch Bow, Tekko-Kagi,
    Spear of the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Titan''s
    Bane, Soul Gem, Riptalon, Gluttonous Grimoire, Tyrfing, Toxic Blade, Lernaean
    Bow, Doom Orb, The World Stone, Nimble Ring, Avatar''s Parashu, Avenging Blade,
    Dreamer''s Idol, Pendulum Blade, Bragi''s Harp, Dominance, Deathbringer, The Cosmic
    Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords,
    Transcendence, The Executioner, Runeforged Hammer, Arondight, Ancient Signet,
    Qin''s Blade, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.65
      efficiency: 0.46
      win: 1.0
      pick: 0.14
      fit: 0.19
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.61
    Hydra's Lament:
      total: 0.64
      efficiency: 0.54
      win: 0.86
      pick: 0.23
      fit: 0.32
    Freya's Tears:
      total: 0.59
      efficiency: 0.36
      win: 1.0
      pick: 0.19
      fit: 0.03
    The Crusher:
      total: 0.61
      efficiency: 0.47
      win: 0.75
      pick: 0.18
      fit: 0.67
    Heartseeker:
      total: 0.74
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.77
  community_ordered:
  - Berserker's Shield
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Hydra's Lament
  - Nimble Ring
  - Freya's Tears
  - Riptalon
  - Heartseeker
  flex_slots:
  - Nimble Ring
  - Riptalon
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Jotunn''s Revenge, Nimble Ring,
    Riptalon, Tyrfing, Silverbranch Bow, Death Metal, Soul Gem, Lernaean Bow, Gluttonous
    Grimoire, Tekko-Kagi, Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian
    Shard, Spear of Desolation, Dominance, Bracer of The Abyss, Qin''s Blade, Titan''s
    Bane, Deathbringer, Demon Blade, Doom Orb, The World Stone, Ancient Signet, Sun
    Beam Bow, Blood-Bound Book, Transcendence, Dreamer''s Idol, Chronos'' Pendant,
    Musashi''s Dual Swords, Runeforged Hammer, Arondight, Avatar''s Parashu, Bancroft''s
    Talon, Pendulum Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.66
      efficiency: 0.46
      win: 1.0
      pick: 0.14
      fit: 0.26
    Hydra's Lament:
      total: 0.63
      efficiency: 0.54
      win: 0.86
      pick: 0.23
      fit: 0.27
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.59
      efficiency: 0.36
      win: 1.0
      pick: 0.19
      fit: 0.03
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.65
    Heartseeker:
      total: 0.7
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.47
  community_ordered:
  - Berserker's Shield
  - Hydra's Lament
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Daybreak Gavel
  - Freya's Tears
  - Heartseeker
  flex_slots:
  - Jotunn's Revenge
  - Daybreak Gavel
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Spear of Desolation, Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear
    of the Magus, Silverbranch Bow, Arondight, Gem of Focus, Obsidian Shard, Tyrfing,
    Lernaean Bow, Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp,
    Bracer of The Abyss, Totem of Death, Doom Orb, Riptalon, The World Stone, Ancient
    Signet, Titan''s Bane, Breastplate of Valor, Dreamer''s Idol, Toxic Blade, Deathbringer,
    Dominance, Qin''s Blade, Transcendence, Musashi''s Dual Swords, Runeforged Hammer,
    Demon Blade, Avatar''s Parashu.'
  slot_scores:
    Berserker's Shield:
      total: 0.64
      efficiency: 0.46
      win: 1.0
      pick: 0.14
      fit: 0.17
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.67
      efficiency: 0.54
      win: 0.86
      pick: 0.23
      fit: 0.55
    Daybreak Gavel:
      total: 0.56
      efficiency: 0.51
      win: 0.83
      pick: 0.19
      fit: 0.0
    Freya's Tears:
      total: 0.64
      efficiency: 0.36
      win: 1.0
      pick: 0.19
      fit: 0.34
    Heartseeker:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.23
      fit: 0.44
  community_ordered:
  - Berserker's Shield
  - Hydra's Lament
  - Daybreak Gavel
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Tekko-Kagi
  - Silverbranch Bow
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
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Tyrfing,
    Tekko-Kagi, Silverbranch Bow, Lernaean Bow, Nimble Ring, Bragi''s Harp, Spear
    of the Magus, Riptalon, Spear of Desolation, Titan''s Bane, Dominance, Obsidian
    Shard, Deathbringer, Soul Gem, Toxic Blade, Demon Blade, Gluttonous Grimoire,
    Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum
    Blade, Transcendence, The World Stone, Arondight, Qin''s Blade, Runeforged Hammer,
    Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade,
    Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.26
  starter: *id001
---
