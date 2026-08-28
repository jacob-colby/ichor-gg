---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.54
  aspect_win_rate: 0.6
  slot_order:
  - name: Tyrfing
    pick_rate: 0.55
    win_rate: 0.6
    alternates:
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.56
    - name: Jotunn's Revenge
      pick_rate: 0.07
      win_rate: 0.44
  - name: Odysseus' Bow
    pick_rate: 0.3
    win_rate: 0.59
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.18
      win_rate: 0.57
    - name: Transcendence
      pick_rate: 0.08
      win_rate: 0.45
  - name: Hastened Fatalis
    pick_rate: 0.24
    win_rate: 0.57
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.18
      win_rate: 0.65
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.5
  - name: Silverbranch Bow
    pick_rate: 0.12
    win_rate: 0.47
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.15
      win_rate: 0.67
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.62
  - name: Riptalon
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.18
      win_rate: 0.7
    - name: Qin's Blade
      pick_rate: 0.08
      win_rate: 0.67
  - name: Manchu Bow
    pick_rate: 0.11
    win_rate: 0.38
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.43
    - name: Agility Greaves
      pick_rate: 0.07
      win_rate: 0.6
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.23
    win_rate: 0.63
  - name: Death's Embrace
    pick_rate: 0.15
    win_rate: 0.74
  - name: Leather Cowl
    pick_rate: 0.1
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-08-28'
  god_win_rate: 0.5461538461538461
  god_matches_won: 71
  god_matches_played: 130
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-28'
  god_matches_analyzed: 3498
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Riptalon
  - Tekko-Kagi
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Tekko-Kagi, Jotunn''s Revenge, Lernaean
    Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus,
    Titan''s Bane, Spear of Desolation, The Crusher, Dominance, Obsidian Shard, Deathbringer,
    Soul Gem, The Reaper, Demon Blade, Toxic Blade, Gluttonous Grimoire, Bracer of
    The Abyss, Musashi''s Dual Swords, Hydra''s Lament, Avatar''s Parashu, Doom Orb,
    Pendulum Blade, The World Stone, Arondight, Runeforged Hammer, Dreamer''s Idol,
    Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade, Berserker''s
    Shield, Transcendence.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.07
      fit: 0.49
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.6
      pick: 0.55
      fit: 0.68
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.51
    Riptalon:
      total: 0.59
      efficiency: 0.46
      win: 0.75
      pick: 0.24
      fit: 0.53
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.69
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Riptalon
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Heartseeker
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
    of Tahuti, Death Metal, Jotunn''s Revenge, Spear of Desolation, Nimble Ring, Soul
    Gem, Spear of the Magus, Obsidian Shard, Heartseeker, Bragi''s Harp, Lernaean
    Bow, Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone,
    Hydra''s Lament, Chronos'' Pendant, Dominance, Bracer of The Abyss, Titan''s Bane,
    The Crusher, Dreamer''s Idol, Deathbringer, Golden Blade, The Reaper, Book of
    Thoth, Arondight, Gem of Focus, Polynomicon, Pendulum Blade, Runeforged Hammer,
    Musashi''s Dual Swords, Soul Reaver, Avatar''s Parashu, Rod of Asclepius, The
    Cosmic Horror, Demon Blade, Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.07
      fit: 0.52
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.6
      pick: 0.55
      fit: 0.51
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.54
    Riptalon:
      total: 0.56
      efficiency: 0.46
      win: 0.75
      pick: 0.24
      fit: 0.34
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Death Metal
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Soul Gem, Death Metal, The Reaper, Runeforged
    Hammer, Golden Blade, Freya''s Tears, Gluttonous Grimoire, Genji''s Guard, Shifter''s
    Shield, Shield Splitter, Breastplate of Valor, Ethereal Staff, Yogi''s Necklace,
    Eye of the Storm, Pharaoh''s Curse, Jotunn''s Revenge, Lernaean Bow, Phoenix Feather,
    Erosion, Nimble Ring, Shogun''s Ofuda, Eye of Providence, Spear of the Magus,
    Heartseeker, Tekko-Kagi, Draconic Scale, Lifebinder, Toxic Blade, Avenging Blade,
    Helm of Radiance, Chandra''s Grace, Daybreak Gavel, Hydra''s Lament.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.6
      pick: 0.55
      fit: 0.45
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.31
    Riptalon:
      total: 0.6
      efficiency: 0.46
      win: 0.75
      pick: 0.24
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Spear of the Magus
  - Tekko-Kagi
  - Heartseeker
  flex_slots:
  - Heartseeker
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Tekko-Kagi, Heartseeker, Spear
    of the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Titan''s Bane,
    Soul Gem, The Crusher, The Reaper, Gluttonous Grimoire, Lernaean Bow, Doom Orb,
    Toxic Blade, The World Stone, Nimble Ring, Avatar''s Parashu, Avenging Blade,
    Dreamer''s Idol, Pendulum Blade, Bragi''s Harp, Golden Blade, Dominance, Deathbringer,
    The Cosmic Horror, Bracer of The Abyss, Hydra''s Lament, Oath-Sworn Spear, Demon
    Blade, Musashi''s Dual Swords, Runeforged Hammer, Arondight, Ancient Signet, Chronos''
    Pendant, Damaru, Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.07
      fit: 0.61
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.55
      fit: 0.55
    Riptalon:
      total: 0.61
      efficiency: 0.46
      win: 0.75
      pick: 0.24
      fit: 0.64
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.43
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
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Death Metal
  - Qin's Blade
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Qin's Blade
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
    this god: Rod of Tahuti, Nimble Ring, Death Metal, Soul Gem, Lernaean Bow, Gluttonous
    Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Jotunn''s Revenge, Spear of the
    Magus, Toxic Blade, Bragi''s Harp, Heartseeker, Obsidian Shard, Spear of Desolation,
    Dominance, Bracer of The Abyss, Titan''s Bane, The Crusher, Deathbringer, Demon
    Blade, Doom Orb, The World Stone, Ancient Signet, Hydra''s Lament, Sun Beam Bow,
    Blood-Bound Book, Dreamer''s Idol, Musashi''s Dual Swords, Chronos'' Pendant,
    Runeforged Hammer, Arondight, Berserker''s Shield, Avatar''s Parashu, Bancroft''s
    Talon, Pendulum Blade, Transcendence.'
  slot_scores:
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.6
      pick: 0.55
      fit: 0.67
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.32
    Qin's Blade:
      total: 0.53
      efficiency: 0.37
      win: 0.67
      pick: 0.17
      fit: 0.63
    Riptalon:
      total: 0.63
      efficiency: 0.51
      win: 0.75
      pick: 0.24
      fit: 0.65
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.18
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Jotunn''s Revenge, Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Hydra''s
    Lament, Spear of the Magus, Arondight, Gem of Focus, Obsidian Shard, Lernaean
    Bow, Pendulum Blade, Tekko-Kagi, Heartseeker, Gluttonous Grimoire, Bragi''s Harp,
    Bracer of The Abyss, Totem of Death, Doom Orb, The World Stone, Ancient Signet,
    Titan''s Bane, The Crusher, Breastplate of Valor, Golden Blade, Dreamer''s Idol,
    Deathbringer, Dominance, Genji''s Guard, The Reaper, Toxic Blade, Musashi''s Dual
    Swords, Runeforged Hammer, Demon Blade, Avatar''s Parashu, Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.07
      fit: 0.59
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.6
      pick: 0.55
      fit: 0.44
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
      total: 0.54
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
    Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Demon Blade, Toxic Blade,
    Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu,
    Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight, Runeforged
    Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging
    Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.07
      fit: 0.49
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.6
      pick: 0.55
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
      total: 0.59
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.26
  starter: *id001
---
