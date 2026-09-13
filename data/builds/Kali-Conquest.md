---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.45
  aspect_win_rate: 0.61
  slot_order:
  - name: Tyrfing
    pick_rate: 0.56
    win_rate: 0.58
    alternates:
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.67
    - name: Daybreak Gavel
      pick_rate: 0.05
      win_rate: 0.88
  - name: Hastened Fatalis
    pick_rate: 0.36
    win_rate: 0.61
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.16
      win_rate: 0.54
    - name: Dagger of Frenzy
      pick_rate: 0.04
      win_rate: 0.83
  - name: Odysseus' Bow
    pick_rate: 0.29
    win_rate: 0.63
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.18
      win_rate: 0.5
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.4
  - name: The Executioner
    pick_rate: 0.2
    win_rate: 0.63
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.15
      win_rate: 0.62
    - name: Odysseus' Bow
      pick_rate: 0.1
      win_rate: 0.64
  - name: Silverbranch Bow
    pick_rate: 0.25
    win_rate: 0.72
    alternates:
    - name: The Executioner
      pick_rate: 0.09
      win_rate: 0.67
    - name: Riptalon
      pick_rate: 0.08
      win_rate: 0.73
  - name: Qin's Blade
    pick_rate: 0.14
    win_rate: 0.79
    alternates:
    - name: Manchu Bow
      pick_rate: 0.11
      win_rate: 0.45
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.8
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.31
    win_rate: 0.78
  - name: Death's Embrace
    pick_rate: 0.18
    win_rate: 0.65
  - name: Leather Cowl
    pick_rate: 0.16
    win_rate: 0.22
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-09-13'
  god_win_rate: 0.6013513513513513
  god_matches_won: 89
  god_matches_played: 148
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-13'
  god_matches_analyzed: 5560
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Daybreak Gavel
  - Death Metal
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  flex_slots:
  - Daybreak Gavel
  - Riptalon
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
    Shard, Deathbringer, Soul Gem, The Reaper, Demon Blade, Toxic Blade, Gluttonous
    Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom
    Orb, Pendulum Blade, Transcendence, The World Stone, Arondight, Runeforged Hammer,
    Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade,
    Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.49
    Daybreak Gavel:
      total: 0.58
      efficiency: 0.51
      win: 0.88
      pick: 0.05
      fit: 0.0
    Death Metal:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.51
    Riptalon:
      total: 0.58
      efficiency: 0.46
      win: 0.73
      pick: 0.17
      fit: 0.53
    Qin's Blade:
      total: 0.59
      efficiency: 0.37
      win: 0.79
      pick: 0.43
      fit: 0.54
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.72
      pick: 0.54
      fit: 0.53
  community_ordered:
  - Daybreak Gavel
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Daybreak Gavel
  - Death Metal
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Daybreak Gavel
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Death Metal, Spear of Desolation, Hydra''s Lament,
    Nimble Ring, Soul Gem, Spear of the Magus, Obsidian Shard, Heartseeker, Bragi''s
    Harp, Lernaean Bow, Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet,
    The World Stone, Chronos'' Pendant, Dominance, Bracer of The Abyss, Titan''s Bane,
    The Crusher, Dreamer''s Idol, Transcendence, Deathbringer, Golden Blade, The Reaper,
    Book of Thoth, Arondight, Gem of Focus, Polynomicon, Pendulum Blade, Runeforged
    Hammer, Musashi''s Dual Swords, Soul Reaver, Avatar''s Parashu, Rod of Asclepius,
    The Cosmic Horror, Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.49
    Daybreak Gavel:
      total: 0.58
      efficiency: 0.51
      win: 0.88
      pick: 0.05
      fit: 0.0
    Death Metal:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.54
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.53
      win: 0.72
      pick: 0.54
      fit: 0.34
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Daybreak Gavel
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Daybreak Gavel
  - Riptalon
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Riptalon
  - Silverbranch Bow
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
    this god: Amanita Charm, Daybreak Gavel, Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass, Soul Gem, Death
    Metal, The Reaper, Runeforged Hammer, Golden Blade, Freya''s Tears, Gluttonous
    Grimoire, Genji''s Guard, Shifter''s Shield, Shield Splitter, Breastplate of Valor,
    Ethereal Staff, Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse, Lernaean
    Bow, Phoenix Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Eye of Providence,
    Spear of the Magus, Heartseeker, Tekko-Kagi, Draconic Scale, Lifebinder, Toxic
    Blade, Avenging Blade, Helm of Radiance, Hydra''s Lament, Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.3
    Daybreak Gavel:
      total: 0.63
      efficiency: 0.59
      win: 0.88
      pick: 0.05
      fit: 0.15
    Riptalon:
      total: 0.59
      efficiency: 0.46
      win: 0.73
      pick: 0.17
      fit: 0.62
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.72
      pick: 0.54
      fit: 0.32
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Daybreak Gavel
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Daybreak Gavel
  - Riptalon
  - Tekko-Kagi
  - Silverbranch Bow
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Daybreak Gavel
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
    Soul Gem, The Crusher, The Reaper, Gluttonous Grimoire, Lernaean Bow, Doom Orb,
    Toxic Blade, The World Stone, Nimble Ring, Avatar''s Parashu, Avenging Blade,
    Dreamer''s Idol, Hydra''s Lament, Pendulum Blade, Bragi''s Harp, Golden Blade,
    Dominance, Deathbringer, The Cosmic Horror, Bracer of The Abyss, Oath-Sworn Spear,
    Demon Blade, Musashi''s Dual Swords, Transcendence, Runeforged Hammer, Arondight,
    Ancient Signet, Chronos'' Pendant, Damaru.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.61
    Daybreak Gavel:
      total: 0.58
      efficiency: 0.51
      win: 0.88
      pick: 0.05
      fit: 0.0
    Riptalon:
      total: 0.59
      efficiency: 0.46
      win: 0.73
      pick: 0.17
      fit: 0.64
    Tekko-Kagi:
      total: 0.59
      efficiency: 0.49
      win: 0.67
      pick: 0.0
      fit: 0.76
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.72
      pick: 0.54
      fit: 0.64
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.67
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Daybreak Gavel
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Dagger of Frenzy
  - Daybreak Gavel
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  flex_slots:
  - Daybreak Gavel
  - Dagger of Frenzy
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
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Spear
    of the Magus, Toxic Blade, Bragi''s Harp, Heartseeker, Obsidian Shard, Spear of
    Desolation, Dominance, Hydra''s Lament, Bracer of The Abyss, Titan''s Bane, The
    Crusher, Deathbringer, Demon Blade, Doom Orb, The World Stone, Ancient Signet,
    Sun Beam Bow, Blood-Bound Book, Transcendence, Dreamer''s Idol, Musashi''s Dual
    Swords, Chronos'' Pendant, Runeforged Hammer, Arondight, Berserker''s Shield,
    Avatar''s Parashu, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.31
    Dagger of Frenzy:
      total: 0.57
      efficiency: 0.37
      win: 0.83
      pick: 0.05
      fit: 0.43
    Daybreak Gavel:
      total: 0.58
      efficiency: 0.51
      win: 0.88
      pick: 0.05
      fit: 0.0
    Riptalon:
      total: 0.61
      efficiency: 0.51
      win: 0.73
      pick: 0.17
      fit: 0.65
    Qin's Blade:
      total: 0.6
      efficiency: 0.37
      win: 0.79
      pick: 0.43
      fit: 0.63
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.72
      pick: 0.54
      fit: 0.57
  community_ordered:
  - Dagger of Frenzy
  - Daybreak Gavel
  - Riptalon
  - Qin's Blade
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Daybreak Gavel
  - Spear of Desolation
  - Rod of Tahuti
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Daybreak Gavel
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
    Titan''s Bane, The Crusher, Breastplate of Valor, Golden Blade, Dreamer''s Idol,
    Deathbringer, Dominance, Genji''s Guard, The Reaper, Toxic Blade, Transcendence,
    Musashi''s Dual Swords, Runeforged Hammer, Demon Blade, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.59
    Daybreak Gavel:
      total: 0.58
      efficiency: 0.51
      win: 0.88
      pick: 0.05
      fit: 0.0
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.0
      fit: 0.24
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.53
      win: 0.72
      pick: 0.54
      fit: 0.37
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Daybreak Gavel
  - Silverbranch Bow
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
    Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging
    Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.58
      pick: 0.56
      fit: 0.68
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.58
      efficiency: 0.49
      win: 0.67
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Tyrfing
  starter: *id001
---
