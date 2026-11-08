---
type: smite-build
god: Xbalanque
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Nightstalker
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.55
  slot_order:
  - name: Tyrfing
    pick_rate: 0.52
    win_rate: 0.58
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.28
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.53
  - name: Odysseus' Bow
    pick_rate: 0.27
    win_rate: 0.62
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.65
    - name: Dagger of Frenzy
      pick_rate: 0.16
      win_rate: 0.72
  - name: Silverbranch Bow
    pick_rate: 0.22
    win_rate: 0.65
    alternates:
    - name: Dominance
      pick_rate: 0.19
      win_rate: 0.59
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.58
  - name: The Executioner
    pick_rate: 0.18
    win_rate: 0.57
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.15
      win_rate: 0.58
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.63
  - name: Riptalon
    pick_rate: 0.12
    win_rate: 0.41
    alternates:
    - name: The Executioner
      pick_rate: 0.16
      win_rate: 0.7
    - name: Silverbranch Bow
      pick_rate: 0.15
      win_rate: 0.74
  - name: Manchu Bow
    pick_rate: 0.12
    win_rate: 0.52
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.1
      win_rate: 0.61
    - name: Bow
      pick_rate: 0.09
      win_rate: 0.59
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.6
    win_rate: 0.63
  - name: Death's Toll
    pick_rate: 0.18
    win_rate: 0.52
  - name: Pendulum of the Ages
    pick_rate: 0.06
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/xbalanque/
  last_verified: '2026-11-08'
  god_win_rate: 0.576
  god_matches_won: 144
  god_matches_played: 250
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Dagger of Frenzy
  - Silverbranch Bow
  - Dominance
  flex_slots:
  - Silverbranch Bow
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
    this god: Golden Blade, Lernaean Bow, Demon Blade, Qin''s Blade, Rage, Deathbringer,
    Tekko-Kagi, The Reaper, Hydra''s Lament, Musashi''s Dual Swords, Bloodforge, Barbed
    Carver, Sun Beam Bow, Transcendence, Runeforged Hammer, Toxic Blade, Jotunn''s
    Revenge, The Crusher, Shield Splitter, Eye of the Storm, Avenging Blade, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.45
      win: 0.59
      pick: 0.0
      fit: 0.73
    Tyrfing:
      total: 0.6
      efficiency: 0.53
      win: 0.58
      pick: 0.52
      fit: 0.83
    Lernaean Bow:
      total: 0.53
      efficiency: 0.47
      win: 0.59
      pick: 0.0
      fit: 0.64
    Dagger of Frenzy:
      total: 0.56
      efficiency: 0.42
      win: 0.72
      pick: 0.22
      fit: 0.52
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.4
      win: 0.65
      pick: 0.34
      fit: 0.52
    Dominance:
      total: 0.54
      efficiency: 0.47
      win: 0.59
      pick: 0.3
      fit: 0.64
  community_ordered:
  - Tyrfing
  - Dagger of Frenzy
  - Silverbranch Bow
  - Dominance
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Transcendence
  - Hydra's Lament
  - Silverbranch Bow
  - Dagger of Frenzy
  flex_slots:
  - Hydra's Lament
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
    Revenge, Hydra''s Lament, The Reaper, Heartseeker, Tekko-Kagi, The Crusher, Lernaean
    Bow, Titan''s Bane, Arondight, Golden Blade, Rage, Transcendence, Toxic Blade,
    Deathbringer, Qin''s Blade, Avatar''s Parashu, Demon Blade, Genji''s Guard, Runeforged
    Hammer, Bloodforge, Barbed Carver, Pendulum Blade, Damaru, Shield Splitter, Eye
    of the Storm, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.52
      fit: 0.53
    Transcendence:
      total: 0.48
      efficiency: 0.5
      win: 0.59
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.52
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.49
      win: 0.65
      pick: 0.34
      fit: 0.37
    Dagger of Frenzy:
      total: 0.52
      efficiency: 0.42
      win: 0.72
      pick: 0.22
      fit: 0.26
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Dagger of Frenzy
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Rage
  - Tyrfing
  - Dagger of Frenzy
  - Dominance
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Rage
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Demon Blade, Lernaean Bow, Rage, Deathbringer, Qin''s
    Blade, The Reaper, Musashi''s Dual Swords, Hydra''s Lament, Tekko-Kagi, Bloodforge,
    Barbed Carver, Transcendence, Runeforged Hammer, Sun Beam Bow, Toxic Blade, Jotunn''s
    Revenge, The Crusher, Shield Splitter, Eye of the Storm, Avenging Blade, Heartseeker.'
  slot_scores:
    Rage:
      total: 0.51
      efficiency: 0.46
      win: 0.59
      pick: 0.0
      fit: 0.57
    Tyrfing:
      total: 0.59
      efficiency: 0.53
      win: 0.58
      pick: 0.52
      fit: 0.79
    Dagger of Frenzy:
      total: 0.56
      efficiency: 0.42
      win: 0.72
      pick: 0.22
      fit: 0.49
    Dominance:
      total: 0.54
      efficiency: 0.47
      win: 0.59
      pick: 0.3
      fit: 0.6
    Demon Blade:
      total: 0.52
      efficiency: 0.36
      win: 0.59
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.51
      efficiency: 0.44
      win: 0.59
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Tyrfing
  - Dagger of Frenzy
  - Dominance
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Golden Blade,
    Phoenix Feather, Yogi''s Necklace, Shield Splitter, Oni Hunter''s Garb, Runeforged
    Hammer, Draconic Scale, The Reaper, Shogun''s Ofuda, Pharaoh''s Curse, Erosion,
    Genji''s Guard, Eye of Providence, Bloodforge, Midgardian Mail, Shifter''s Shield,
    Leviathan''s Hide, Lernaean Bow, Hide of the Nemean Lion, Stone of Binding, Ancile,
    Umbral Link, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.63
      efficiency: 0.72
      win: 0.65
      pick: 0.26
      fit: 0.48
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.52
      fit: 0.54
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.5
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Tyrfing
  - Dagger of Frenzy
  - The Reaper
  - Tekko-Kagi
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Dagger of Frenzy
  - The Crusher
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
    for this god: The Reaper, Tekko-Kagi, The Crusher, Heartseeker, Toxic Blade, Titan''s
    Bane, Jotunn''s Revenge, Lernaean Bow, Avatar''s Parashu, Golden Blade, Avenging
    Blade, Qin''s Blade, Rage, Demon Blade, Deathbringer, Hydra''s Lament, Oath-Sworn
    Spear, Transcendence, Bloodforge, Runeforged Hammer, Barbed Carver, Pendulum Blade,
    Musashi''s Dual Swords.'
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.58
      pick: 0.52
      fit: 0.58
    Dagger of Frenzy:
      total: 0.54
      efficiency: 0.42
      win: 0.72
      pick: 0.22
      fit: 0.35
    The Reaper:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.56
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.69
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.49
      win: 0.65
      pick: 0.34
      fit: 0.69
    The Crusher:
      total: 0.53
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Tyrfing
  - Dagger of Frenzy
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Dagger of Frenzy
  - Silverbranch Bow
  - Dominance
  flex_slots:
  - Golden Blade
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
    this god: Golden Blade, Lernaean Bow, Qin''s Blade, Demon Blade, Rage, Deathbringer,
    Hydra''s Lament, Tekko-Kagi, The Reaper, Sun Beam Bow, Bloodforge, Transcendence,
    Barbed Carver, Toxic Blade, Runeforged Hammer, Musashi''s Dual Swords, Jotunn''s
    Revenge, The Crusher, Shield Splitter, Eye of the Storm, Avenging Blade, Heartseeker,
    Vital Amplifier.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.45
      win: 0.59
      pick: 0.0
      fit: 0.65
    Tyrfing:
      total: 0.59
      efficiency: 0.53
      win: 0.58
      pick: 0.52
      fit: 0.75
    Lernaean Bow:
      total: 0.51
      efficiency: 0.47
      win: 0.59
      pick: 0.0
      fit: 0.55
    Dagger of Frenzy:
      total: 0.56
      efficiency: 0.42
      win: 0.72
      pick: 0.22
      fit: 0.49
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.4
      win: 0.65
      pick: 0.34
      fit: 0.49
    Dominance:
      total: 0.53
      efficiency: 0.47
      win: 0.59
      pick: 0.3
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Dagger of Frenzy
  - Silverbranch Bow
  - Dominance
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Dagger of Frenzy
  - Arondight
  - Dominance
  flex_slots:
  - Arondight
  - Dominance
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Arondight, Lernaean Bow, Damaru, Genji''s Guard, Golden Blade, Qin''s Blade, Rage,
    Breastplate of Valor, Demon Blade, Chandra''s Grace, Deathbringer, The Reaper,
    Transcendence, Runeforged Hammer, Bloodforge, Tekko-Kagi, Barbed Carver, Screeching
    Gargoyle, Freya''s Tears, Sun Beam Bow, The Crusher.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.52
      fit: 0.52
    Hydra's Lament:
      total: 0.53
      efficiency: 0.55
      win: 0.59
      pick: 0.0
      fit: 0.51
    Dagger of Frenzy:
      total: 0.53
      efficiency: 0.42
      win: 0.72
      pick: 0.22
      fit: 0.32
    Arondight:
      total: 0.51
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.41
    Dominance:
      total: 0.51
      efficiency: 0.47
      win: 0.59
      pick: 0.3
      fit: 0.4
  community_ordered:
  - Tyrfing
  - Dagger of Frenzy
  - Dominance
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Silverbranch Bow
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
    + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Death Metal, Jotunn''s
    Revenge, Nimble Ring, Gluttonous Grimoire, Spear of Desolation, Blood-Bound Book,
    Bragi''s Harp, Obsidian Shard, Spear of the Magus, The Reaper, Ancient Signet,
    Chronos'' Pendant, Bracer of The Abyss, Polynomicon, Hydra''s Lament, Dreamer''s
    Idol, Tekko-Kagi, Doom Orb, The Crusher, Heartseeker, Gem of Focus, The World
    Stone, Heartwood Charm, Lernaean Bow, Bancroft''s Talon, Soul Reaver, Titan''s
    Bane, Arondight, Golden Blade, Toxic Blade, Qin''s Blade, The Cosmic Horror, Rage,
    Totem of Death, Typhon’s Heart.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.52
      fit: 0.49
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.5
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.49
      win: 0.65
      pick: 0.34
      fit: 0.42
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.59
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Tyrfing
  - Dagger of Frenzy
  - Death Metal
  - Bragi's Harp
  - Silverbranch Bow
  - Gluttonous Grimoire
  flex_slots:
  - Dagger of Frenzy
  - Gluttonous Grimoire
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
    Ring, Bragi''s Harp, Gluttonous Grimoire, Soul Gem, The Reaper, Blood-Bound Book,
    Obsidian Shard, Tekko-Kagi, Spear of the Magus, The Crusher, Ancient Signet, Bracer
    of The Abyss, Heartseeker, Dreamer''s Idol, Lernaean Bow, Polynomicon, Titan''s
    Bane, Golden Blade, Jotunn''s Revenge, Doom Orb, The World Stone, Toxic Blade,
    Bancroft''s Talon, Spear of Desolation, Rage, Soul Reaver, Hydra''s Lament, Demon
    Blade, Qin''s Blade, Deathbringer, Avatar''s Parashu, The Cosmic Horror, Transcendence,
    Runeforged Hammer, Typhon’s Heart.'
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.58
      pick: 0.52
      fit: 0.6
    Dagger of Frenzy:
      total: 0.53
      efficiency: 0.42
      win: 0.72
      pick: 0.22
      fit: 0.31
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.57
    Bragi's Harp:
      total: 0.53
      efficiency: 0.47
      win: 0.59
      pick: 0.0
      fit: 0.67
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.49
      win: 0.65
      pick: 0.34
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.54
      win: 0.59
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Tyrfing
  - Dagger of Frenzy
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Dominance
  - Qin's Blade
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Qin's Blade
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
    Underrated for this god: Golden Blade, Lernaean Bow, Demon Blade, Qin''s Blade,
    Rage, Deathbringer, Tekko-Kagi, The Reaper, Hydra''s Lament, Musashi''s Dual Swords,
    Bloodforge, Barbed Carver, Sun Beam Bow, Transcendence, Runeforged Hammer, Toxic
    Blade, Jotunn''s Revenge, The Crusher, Shield Splitter, Eye of the Storm, Avenging
    Blade, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.45
      win: 0.59
      pick: 0.0
      fit: 0.73
    Tyrfing:
      total: 0.6
      efficiency: 0.53
      win: 0.58
      pick: 0.52
      fit: 0.83
    Lernaean Bow:
      total: 0.53
      efficiency: 0.47
      win: 0.59
      pick: 0.0
      fit: 0.64
    Dominance:
      total: 0.54
      efficiency: 0.47
      win: 0.59
      pick: 0.3
      fit: 0.64
    Qin's Blade:
      total: 0.51
      efficiency: 0.39
      win: 0.59
      pick: 0.0
      fit: 0.72
    Demon Blade:
      total: 0.52
      efficiency: 0.36
      win: 0.59
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Tyrfing
  - Dominance
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-09-24'
  partial_windows:
    ob44: '2026-09-24'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of the Nightstalker
    status: shown
    window: ob46
    window_rule: last closed
    window_start: '2026-10-20'
    window_end: '2026-11-03'
    matches: 71
    wins: 38
    win_share: 0.54
    aggregate:
      aspect_matches: 87
      aspect_win_rate: 0.517
      no_aspect_matches: 505
      no_aspect_win_rate: 0.584
    roles:
    - role: Mid
      matches: 36
      share: 0.51
    - role: Solo
      matches: 22
      share: 0.31
    - role: Carry
      matches: 9
      share: 0.13
    - role: Jungle
      matches: 4
      share: 0.06
    base_role: Carry
    base_role_share: 0.13
    role_shift:
      role: Mid
      share: 0.51
      says: 'most Aspect of the Nightstalker players do not play Carry: Mid 51%, Carry
        13%'
    items:
    - name: Rod of Tahuti
      share: 0.92
    - name: Spear of Desolation
      share: 0.89
    - name: Obsidian Shard
      share: 0.66
    - name: Blinking Abyss
      share: 0.55
    - name: Gem of Focus
      share: 0.49
    - name: Dreamer's Idol
      share: 0.31
    - name: Chronos' Pendant
      share: 0.25
    - name: Book of Thoth
      share: 0.17
    starters:
    - name: Pendulum of the Ages
      share: 0.59
    - name: Archmage's Gem
      share: 0.23
    - name: Bluestone Brooch
      share: 0.07
    relics:
    - name: purification-beads
      share: 0.76
    - name: aegis-of-acceleration
      share: 0.24
    matches_by_window:
      ob47: 25
      ob46: 71
      ob45: 52
      ob44: 62
    unmapped_slugs:
    - aegis-of-acceleration
    - purification-beads
---
