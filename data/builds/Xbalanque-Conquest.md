---
type: smite-build
god: Xbalanque
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Nightstalker
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.55
  slot_order:
  - name: Tyrfing
    pick_rate: 0.65
    win_rate: 0.58
    alternates:
    - name: Transcendence
      pick_rate: 0.05
      win_rate: 0.64
    - name: The Cosmic Horror
      pick_rate: 0.05
      win_rate: 0.7
  - name: Odysseus' Bow
    pick_rate: 0.51
    win_rate: 0.58
    alternates:
    - name: Dominance
      pick_rate: 0.07
      win_rate: 0.5
    - name: Hastened Fatalis
      pick_rate: 0.04
      win_rate: 0.53
  - name: Hastened Fatalis
    pick_rate: 0.18
    win_rate: 0.61
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.15
      win_rate: 0.63
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.47
  - name: The Executioner
    pick_rate: 0.2
    win_rate: 0.57
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.18
      win_rate: 0.59
    - name: Riptalon
      pick_rate: 0.17
      win_rate: 0.58
  - name: Silverbranch Bow
    pick_rate: 0.18
    win_rate: 0.71
    alternates:
    - name: The Executioner
      pick_rate: 0.16
      win_rate: 0.56
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.61
  - name: Bow
    pick_rate: 0.09
    win_rate: 0.63
    alternates:
    - name: Manchu Bow
      pick_rate: 0.09
      win_rate: 0.57
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.61
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.54
    win_rate: 0.64
  - name: Death's Toll
    pick_rate: 0.21
    win_rate: 0.46
  - name: Archmage's Gem
    pick_rate: 0.04
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/xbalanque/
  last_verified: '2026-08-23'
  god_win_rate: 0.5807984790874525
  god_matches_won: 611
  god_matches_played: 1052
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-23'
  god_matches_analyzed: 15677
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Deathbringer
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
    this god: Lernaean Bow, Golden Blade, Demon Blade, Deathbringer, Musashi''s Dual
    Swords, Qin''s Blade, Transcendence, Damaru, Rage, Tekko-Kagi, Jotunn''s Revenge,
    Sun Beam Bow, Hydra''s Lament, The Reaper, Berserker''s Shield, Runeforged Hammer,
    Dagger of Frenzy, Dominance, Barbed Carver, Toxic Blade, Avenging Blade, Vital
    Amplifier, Bloodforge, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.73
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.58
      pick: 0.65
      fit: 0.83
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.42
      win: 0.71
      pick: 0.39
      fit: 0.52
    Demon Blade:
      total: 0.54
      efficiency: 0.38
      win: 0.61
      pick: 0.0
      fit: 0.87
    Deathbringer:
      total: 0.53
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Hydra's Lament
  - Silverbranch Bow
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Transcendence,
    Golden Blade, Deathbringer, Titan''s Bane, The Crusher, Arondight, Musashi''s
    Dual Swords, Demon Blade, Toxic Blade, Runeforged Hammer, Pendulum Blade, Avatar''s
    Parashu, Damaru, Qin''s Blade, Rage, Avenging Blade, Barbed Carver, Dominance,
    Berserker''s Shield, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.64
      pick: 0.05
      fit: 0.24
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.58
      pick: 0.65
      fit: 0.53
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.71
      pick: 0.39
      fit: 0.37
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - Musashi's Dual Swords
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Musashi's Dual Swords
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Golden Blade, Demon Blade, Deathbringer, Musashi''s Dual
    Swords, Damaru, Rage, Qin''s Blade, Transcendence, Jotunn''s Revenge, Hydra''s
    Lament, Tekko-Kagi, Sun Beam Bow, The Reaper, Runeforged Hammer, Berserker''s
    Shield, Dagger of Frenzy, Barbed Carver, Dominance, Avenging Blade, Toxic Blade,
    Bloodforge, Vital Amplifier, Heartseeker, Shield Splitter.'
  slot_scores:
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.6
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.58
      pick: 0.65
      fit: 0.79
    Musashi's Dual Swords:
      total: 0.52
      efficiency: 0.46
      win: 0.61
      pick: 0.0
      fit: 0.57
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.42
      win: 0.71
      pick: 0.39
      fit: 0.49
    Demon Blade:
      total: 0.54
      efficiency: 0.38
      win: 0.61
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.54
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Golden Blade, Runeforged
    Hammer, Shield of the Phoenix, Shifter''s Shield, Pharaoh''s Curse, Yogi''s Necklace,
    Shield Splitter, Shogun''s Ofuda, Lernaean Bow, Eye of the Storm, Phoenix Feather,
    Erosion, The Reaper, Eye of Providence, Draconic Scale, Daybreak Gavel, Stone
    of Binding, Avenging Blade, Midgardian Mail, Deathbringer, Umbral Link, Magi''s
    Cloak, Hide of the Nemean Lion, Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.58
      pick: 0.65
      fit: 0.54
    Riptalon:
      total: 0.54
      efficiency: 0.41
      win: 0.61
      pick: 0.3
      fit: 0.69
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker, Toxic Blade,
    Titan''s Bane, The Crusher, Lernaean Bow, Golden Blade, Avenging Blade, Deathbringer,
    Avatar''s Parashu, Transcendence, Demon Blade, Musashi''s Dual Swords, Qin''s
    Blade, Hydra''s Lament, Oath-Sworn Spear, Damaru, Runeforged Hammer, Rage, Pendulum
    Blade, Berserker''s Shield, Sun Beam Bow, Barbed Carver, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.58
      pick: 0.65
      fit: 0.58
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.61
      pick: 0.3
      fit: 0.77
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.71
      pick: 0.39
      fit: 0.69
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.69
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Demon Blade
  flex_slots:
  - Riptalon
  - Demon Blade
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
    this god: Lernaean Bow, Golden Blade, Demon Blade, Deathbringer, Qin''s Blade,
    Musashi''s Dual Swords, Transcendence, Sun Beam Bow, Jotunn''s Revenge, Hydra''s
    Lament, Damaru, Tekko-Kagi, Rage, Berserker''s Shield, Runeforged Hammer, Dagger
    of Frenzy, The Reaper, Toxic Blade, Dominance, Avenging Blade, Barbed Carver,
    Vital Amplifier, Bloodforge, Heartseeker, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.55
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.58
      pick: 0.65
      fit: 0.75
    Riptalon:
      total: 0.52
      efficiency: 0.41
      win: 0.61
      pick: 0.3
      fit: 0.59
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.42
      win: 0.71
      pick: 0.39
      fit: 0.49
    Demon Blade:
      total: 0.51
      efficiency: 0.38
      win: 0.61
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Arondight
  - Silverbranch Bow
  flex_slots:
  - Lernaean Bow
  - Arondight
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Lernaean Bow, Arondight, Golden Blade, Deathbringer, Transcendence, Breastplate
    of Valor, Demon Blade, Qin''s Blade, Musashi''s Dual Swords, Genji''s Guard, Runeforged
    Hammer, Damaru, Rage, Berserker''s Shield, Sun Beam Bow, The Reaper, Tekko-Kagi,
    Avenging Blade, Eye of Erebus, Daybreak Gavel, Barbed Carver, Dagger of Frenzy,
    Vital Amplifier, Screeching Gargoyle, Dominance.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.58
      pick: 0.65
      fit: 0.52
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.51
    Arondight:
      total: 0.51
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.41
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.42
      win: 0.71
      pick: 0.39
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Spear of Desolation
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
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Nimble
    Ring, Soul Gem, Death Metal, Gluttonous Grimoire, Spear of Desolation, Spear of
    the Magus, Obsidian Shard, The Cosmic Horror, Bragi''s Harp, Bracer of The Abyss,
    Chronos'' Pendant, The Reaper, Lernaean Bow, Hydra''s Lament, Doom Orb, Tekko-Kagi,
    The World Stone, Ancient Signet, Heartseeker, Blood-Bound Book, Dreamer''s Idol,
    Gem of Focus, Golden Blade, Bancroft''s Talon, Deathbringer, Titan''s Bane, The
    Crusher, Toxic Blade, Rod of Asclepius, Book of Thoth, Arondight, Polynomicon,
    Musashi''s Dual Swords, Typhon’s Heart, Demon Blade, Qin''s Blade, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.53
      win: 0.71
      pick: 0.39
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Death Metal
  - Silverbranch Bow
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Spear of the Magus
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Nimble
    Ring, Gluttonous Grimoire, Spear of the Magus, Soul Gem, Obsidian Shard, Jotunn''s
    Revenge, Bragi''s Harp, The Reaper, Lernaean Bow, Tekko-Kagi, The Cosmic Horror,
    Heartseeker, Bracer of The Abyss, Golden Blade, Doom Orb, Deathbringer, Spear
    of Desolation, The World Stone, Titan''s Bane, The Crusher, Ancient Signet, Transcendence,
    Dreamer''s Idol, Blood-Bound Book, Toxic Blade, Demon Blade, Musashi''s Dual Swords,
    Bancroft''s Talon, Hydra''s Lament, Avatar''s Parashu, Runeforged Hammer, Qin''s
    Blade, Rod of Asclepius, Damaru, Book of Thoth, Rage, Dominance.'
  slot_scores:
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.58
      pick: 0.65
      fit: 0.6
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.57
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.53
      win: 0.71
      pick: 0.39
      fit: 0.47
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.34
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Dominance
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Dominance
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
    Underrated for this god: Lernaean Bow, Golden Blade, Demon Blade, Deathbringer,
    Dominance, Musashi''s Dual Swords, Qin''s Blade, Damaru, Rage, Tekko-Kagi, Jotunn''s
    Revenge, Sun Beam Bow, Hydra''s Lament, Transcendence, The Reaper, Berserker''s
    Shield, Runeforged Hammer, Dagger of Frenzy, Barbed Carver, Toxic Blade, Avenging
    Blade, Vital Amplifier, Bloodforge, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.73
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.58
      pick: 0.65
      fit: 0.83
    Dominance:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.1
      fit: 0.64
    Demon Blade:
      total: 0.54
      efficiency: 0.38
      win: 0.61
      pick: 0.0
      fit: 0.87
    Deathbringer:
      total: 0.53
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Lernaean Bow, Golden Blade, Demon
    Blade, Deathbringer, Dominance, Musashi''s Dual Swords, Qin''s Blade, Damaru,
    Rage, Tekko-Kagi, Jotunn''s Revenge, Sun Beam Bow, Hydra''s Lament, Transcendence,
    The Reaper, Berserker''s Shield, Runeforged Hammer, Dagger of Frenzy, Barbed Carver,
    Toxic Blade, Avenging Blade, Vital Amplifier, Bloodforge, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.73
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.58
      pick: 0.65
      fit: 0.83
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.42
      win: 0.71
      pick: 0.39
      fit: 0.52
    Demon Blade:
      total: 0.54
      efficiency: 0.38
      win: 0.61
      pick: 0.0
      fit: 0.87
    Deathbringer:
      total: 0.53
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.54
  swaps:
  - added: Silverbranch Bow
    removed: Dominance
    reason: community 71% win over 189 matches (vs 58% on this god), taking the model's
      weakest slot from Dominance
  starter: *id001
---
