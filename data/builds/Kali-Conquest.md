---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.67
  slot_order:
  - name: Tyrfing
    pick_rate: 0.32
    win_rate: 0.83
    alternates:
    - name: Book of Thoth
      pick_rate: 0.21
      win_rate: 0.5
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.5
  - name: Toxic Blade
    pick_rate: 0.21
    win_rate: 0.5
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.67
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.5
  - name: Polynomicon
    pick_rate: 0.16
    win_rate: 1.0
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.16
      win_rate: 0.67
    - name: The Crusher
      pick_rate: 0.11
      win_rate: 0.5
  - name: Hastened Fatalis
    pick_rate: 0.17
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.17
      win_rate: 0.67
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.67
  - name: Heartseeker
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Qin's Blade
      pick_rate: 0.13
      win_rate: 0.5
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 1.0
  - name: Manchu Bow
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Bow
      pick_rate: 0.08
      win_rate: 1.0
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.21
    win_rate: 0.75
  - name: Hunter's Cowl
    pick_rate: 0.21
    win_rate: 0.75
  - name: Bumba's Spear
    pick_rate: 0.16
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-10-07'
  god_win_rate: 0.631578947368421
  god_matches_won: 12
  god_matches_played: 19
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Transcendence
  - Tyrfing
  - Polynomicon
  - Soul Reaver
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Soul Reaver
  - Transcendence
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
    this god: Death Metal, Tekko-Kagi, Lernaean Bow, Nimble Ring, Bragi''s Harp, Jotunn''s
    Revenge, Golden Blade, Spear of the Magus, Titan''s Bane, Dominance, Obsidian
    Shard, Deathbringer, Soul Gem, The Reaper, Riptalon, Demon Blade, Gluttonous Grimoire,
    Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum
    Blade, Transcendence, The World Stone, Arondight, Runeforged Hammer, Dreamer''s
    Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade, Berserker''s
    Shield.'
  slot_scores:
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.25
    Tyrfing:
      total: 0.66
      efficiency: 0.48
      win: 0.83
      pick: 0.32
      fit: 0.68
    Polynomicon:
      total: 0.65
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.16
    Soul Reaver:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.13
      fit: 0.26
    Heartseeker:
      total: 0.72
      efficiency: 0.47
      win: 1.0
      pick: 0.28
      fit: 0.65
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.67
      pick: 0.28
      fit: 0.26
  community_ordered:
  - Tyrfing
  - Polynomicon
  - Soul Reaver
  - Heartseeker
  - Rod of Tahuti
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Transcendence
  - Tyrfing
  - Polynomicon
  - Soul Reaver
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Reaver, Death Metal, Nimble Ring, Soul Gem, Spear of the Magus, Jotunn''s Revenge,
    Obsidian Shard, Bragi''s Harp, Lernaean Bow, Doom Orb, Tekko-Kagi, Gluttonous
    Grimoire, Ancient Signet, The World Stone, Chronos'' Pendant, Dominance, Bracer
    of The Abyss, Titan''s Bane, Dreamer''s Idol, Transcendence, Deathbringer, Golden
    Blade, The Reaper, Arondight, Gem of Focus, Pendulum Blade, Runeforged Hammer,
    Musashi''s Dual Swords, Riptalon, Avatar''s Parashu, Rod of Asclepius, The Cosmic
    Horror, Demon Blade.'
  slot_scores:
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.28
    Tyrfing:
      total: 0.64
      efficiency: 0.48
      win: 0.83
      pick: 0.32
      fit: 0.51
    Polynomicon:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.38
    Soul Reaver:
      total: 0.67
      efficiency: 0.4
      win: 1.0
      pick: 0.13
      fit: 0.48
    Heartseeker:
      total: 0.72
      efficiency: 0.47
      win: 1.0
      pick: 0.28
      fit: 0.62
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.28
      fit: 0.42
  community_ordered:
  - Tyrfing
  - Polynomicon
  - Soul Reaver
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Polynomicon
  - Soul Reaver
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Berserker's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Soul Gem, Death Metal, The Reaper, Runeforged Hammer, Golden
    Blade, Freya''s Tears, Riptalon, Gluttonous Grimoire, Genji''s Guard, Shifter''s
    Shield, Shield Splitter, Breastplate of Valor, Ethereal Staff, Yogi''s Necklace,
    Eye of the Storm, Pharaoh''s Curse, Lernaean Bow, Phoenix Feather, Erosion, Nimble
    Ring, Shogun''s Ofuda, Eye of Providence, Spear of the Magus, Tekko-Kagi, Draconic
    Scale, Lifebinder, Avenging Blade, Helm of Radiance, Chandra''s Grace, Daybreak
    Gavel, Jotunn''s Revenge.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.42
    Tyrfing:
      total: 0.63
      efficiency: 0.48
      win: 0.83
      pick: 0.32
      fit: 0.45
    Polynomicon:
      total: 0.64
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.14
    Soul Reaver:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.13
      fit: 0.24
    Heartseeker:
      total: 0.7
      efficiency: 0.47
      win: 1.0
      pick: 0.28
      fit: 0.47
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Tyrfing
  - Polynomicon
  - Soul Reaver
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Transcendence
  - Tyrfing
  - Polynomicon
  - Soul Reaver
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Soul Reaver
  - Transcendence
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
    for this god: Tekko-Kagi, Spear of the Magus, Death Metal, Jotunn''s Revenge,
    Obsidian Shard, Titan''s Bane, Soul Gem, The Reaper, Gluttonous Grimoire, Riptalon,
    Lernaean Bow, Doom Orb, The World Stone, Nimble Ring, Avatar''s Parashu, Avenging
    Blade, Dreamer''s Idol, Pendulum Blade, Bragi''s Harp, Golden Blade, Dominance,
    Deathbringer, The Cosmic Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon
    Blade, Musashi''s Dual Swords, Transcendence, The Executioner, Runeforged Hammer,
    Arondight, Ancient Signet, Chronos'' Pendant, Damaru.'
  slot_scores:
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.19
    Tyrfing:
      total: 0.64
      efficiency: 0.48
      win: 0.83
      pick: 0.32
      fit: 0.55
    Polynomicon:
      total: 0.64
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.15
    Soul Reaver:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.13
      fit: 0.25
    Heartseeker:
      total: 0.74
      efficiency: 0.47
      win: 1.0
      pick: 0.28
      fit: 0.77
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.28
      fit: 0.43
  community_ordered:
  - Tyrfing
  - Polynomicon
  - Soul Reaver
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Polynomicon
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Silverbranch Bow
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
    Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Spear of the Magus, Bragi''s Harp,
    Obsidian Shard, Dominance, Bracer of The Abyss, Jotunn''s Revenge, Titan''s Bane,
    Deathbringer, Demon Blade, Doom Orb, The World Stone, Ancient Signet, Sun Beam
    Bow, Blood-Bound Book, Transcendence, Dreamer''s Idol, Musashi''s Dual Swords,
    Chronos'' Pendant, Runeforged Hammer, Arondight, Berserker''s Shield, Avatar''s
    Parashu, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Tyrfing:
      total: 0.66
      efficiency: 0.48
      win: 0.83
      pick: 0.32
      fit: 0.67
    Nimble Ring:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.39
    Polynomicon:
      total: 0.64
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.14
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.25
      fit: 0.57
    Heartseeker:
      total: 0.7
      efficiency: 0.47
      win: 1.0
      pick: 0.28
      fit: 0.47
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.28
      fit: 0.18
  community_ordered:
  - Tyrfing
  - Polynomicon
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Polynomicon
  - Spear of Desolation
  - Rod of Tahuti
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Jotunn's Revenge
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
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Death
    Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Arondight, Gem of Focus,
    Obsidian Shard, Lernaean Bow, Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire,
    Bragi''s Harp, Bracer of The Abyss, Totem of Death, Doom Orb, The World Stone,
    Ancient Signet, Titan''s Bane, Riptalon, Breastplate of Valor, Golden Blade, Dreamer''s
    Idol, Deathbringer, Dominance, Genji''s Guard, The Reaper, Transcendence, Musashi''s
    Dual Swords, Runeforged Hammer, Demon Blade, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.11
      fit: 0.59
    Polynomicon:
      total: 0.65
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.2
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.67
      pick: 0.22
      fit: 0.59
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.67
      pick: 0.28
      fit: 0.24
    Heartseeker:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.28
      fit: 0.44
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Polynomicon
  - Spear of Desolation
  - Rod of Tahuti
  - Heartseeker
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
    Dominance, Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Riptalon, Demon
    Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s
    Parashu, Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight,
    Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant,
    Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.11
      fit: 0.49
    Tyrfing:
      total: 0.66
      efficiency: 0.48
      win: 0.83
      pick: 0.32
      fit: 0.68
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
      total: 0.65
      efficiency: 0.86
      win: 0.67
      pick: 0.28
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Rod of Tahuti
  starter: *id001
---
