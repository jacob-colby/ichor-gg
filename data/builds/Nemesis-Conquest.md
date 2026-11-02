---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.59
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.32
    win_rate: 0.55
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.23
      win_rate: 0.58
    - name: Devourer's Gauntlet
      pick_rate: 0.2
      win_rate: 0.6
  - name: Jotunn's Revenge
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.2
      win_rate: 0.62
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.61
  - name: The Crusher
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 0.61
    - name: The Reaper
      pick_rate: 0.05
      win_rate: 0.67
  - name: Heartseeker
    pick_rate: 0.18
    win_rate: 0.51
    alternates:
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.48
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.57
  - name: Magi's Cloak
    pick_rate: 0.06
    win_rate: 0.64
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.56
    - name: Avatar's Parashu
      pick_rate: 0.05
      win_rate: 0.64
  - name: Blinking Abyss
    pick_rate: 0.06
    win_rate: 0.65
    alternates:
    - name: Magi's Cloak
      pick_rate: 0.06
      win_rate: 0.63
    - name: Axe
      pick_rate: 0.05
      win_rate: 0.79
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.27
    win_rate: 0.62
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.64
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.36
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-11-02'
  god_win_rate: 0.5612648221343873
  god_matches_won: 284
  god_matches_played: 506
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - The Reaper
  - Tekko-Kagi
  - Silverbranch Bow
  flex_slots:
  - The Reaper
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Tekko-Kagi, Death Metal, Tyrfing, The Reaper, Silverbranch
    Bow, Lernaean Bow, Titan''s Bane, Obsidian Shard, Golden Blade, Nimble Ring, Spear
    of Desolation, Bragi''s Harp, Sundering Echo, Toxic Blade, Dominance, Soul Gem,
    Spear of the Magus, Riptalon, Avatar''s Parashu, Demon Blade, Deathbringer, Musashi''s
    Dual Swords, Gluttonous Grimoire, Doom Orb, Bracer of The Abyss, Arondight, The
    World Stone, Qin''s Blade, Rage, Berserker''s Shield, Pendulum Blade, Transcendence,
    Eros'' Bow, Runeforged Hammer, Dreamer''s Idol, Chronos'' Pendant, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.25
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.46
      win: 0.6
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.51
    The Reaper:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.08
      fit: 0.44
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.69
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
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
    of Tahuti, Death Metal, Spear of Desolation, Obsidian Shard, Sundering Echo, Soul
    Gem, Tekko-Kagi, The Reaper, Nimble Ring, Bragi''s Harp, Doom Orb, Tyrfing, Spear
    of the Magus, The World Stone, Titan''s Bane, Lernaean Bow, Gluttonous Grimoire,
    Dominance, Silverbranch Bow, Chronos'' Pendant, Heartwood Charm, Bracer of The
    Abyss, Ancient Signet, Polynomicon, Golden Blade, Arondight, Dreamer''s Idol,
    Transcendence, Eros'' Bow, Gem of Focus, Book of Thoth, Blood-Bound Book, Soul
    Reaver, Toxic Blade, Deathbringer, Musashi''s Dual Swords, The Cosmic Horror,
    Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.25
      fit: 0.52
    Hydra's Lament:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.32
      fit: 0.49
    Death Metal:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.52
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.36
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.81
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Death Metal
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, The Reaper, Shield
    of the Phoenix, Soul Gem, Kinetic Cuirass, Death Metal, Genji''s Guard, Golden
    Blade, Yogi''s Necklace, Shield Splitter, Phoenix Feather, Tekko-Kagi, Runeforged
    Hammer, Ethereal Staff, Gluttonous Grimoire, Riptalon, Toxic Blade, Breastplate
    of Valor, Obsidian Shard, Freya''s Tears, Pharaoh''s Curse, Tyrfing, Chandra''s
    Grace, Oni Hunter''s Garb, Blood-Bound Book, Erosion, Silverbranch Bow, Shogun''s
    Ofuda, Lernaean Bow, Eye of Providence, Eros'' Bow, Nimble Ring, Draconic Scale,
    Titan''s Bane, Midgardian Mail, Spear of Desolation, Sundering Echo, Rod of Asclepius.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.7
      win: 0.61
      pick: 0.14
      fit: 0.42
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.25
      fit: 0.3
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.52
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.31
    The Reaper:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.08
      fit: 0.57
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - Silverbranch Bow
  - Obsidian Shard
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - Obsidian Shard
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
    for this god: Rod of Tahuti, Tekko-Kagi, The Reaper, Silverbranch Bow, Obsidian
    Shard, Titan''s Bane, Spear of Desolation, Death Metal, Soul Gem, Toxic Blade,
    Spear of the Magus, Tyrfing, Gluttonous Grimoire, Avatar''s Parashu, Doom Orb,
    Riptalon, The World Stone, Lernaean Bow, Nimble Ring, Sundering Echo, Dreamer''s
    Idol, Avenging Blade, Golden Blade, Pendulum Blade, Dominance, Bragi''s Harp,
    The Cosmic Horror, Deathbringer, Musashi''s Dual Swords, Bracer of The Abyss,
    Arondight, Oath-Sworn Spear, The Executioner, Transcendence, Demon Blade, Qin''s
    Blade, Rage, Eros'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.25
      fit: 0.61
    The Reaper:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.08
      fit: 0.57
    Tekko-Kagi:
      total: 0.57
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.76
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.68
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.81
      win: 0.6
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - The Reaper
  - Tekko-Kagi
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, The Reaper, Tekko-Kagi, Tyrfing, Silverbranch
    Bow, Riptalon, Death Metal, Soul Gem, Gluttonous Grimoire, Lernaean Bow, Golden
    Blade, Toxic Blade, Obsidian Shard, Spear of Desolation, Dominance, Titan''s Bane,
    Bragi''s Harp, Sundering Echo, Qin''s Blade, Spear of the Magus, Bracer of The
    Abyss, Blood-Bound Book, Berserker''s Shield, Eros'' Bow, Doom Orb, The World
    Stone, Demon Blade, Sun Beam Bow, Deathbringer, Arondight, Musashi''s Dual Swords,
    Chronos'' Pendant, Transcendence, Bloodforge, Dreamer''s Idol, Bancroft''s Talon,
    Dagger of Frenzy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.25
      fit: 0.31
    Tyrfing:
      total: 0.53
      efficiency: 0.46
      win: 0.6
      pick: 0.0
      fit: 0.67
    Nimble Ring:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.39
    The Reaper:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.08
      fit: 0.36
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
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
  - Death Metal
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Death Metal, Chronos'' Pendant, Obsidian Shard, Tekko-Kagi, Arondight,
    Nimble Ring, The Reaper, Silverbranch Bow, Heartwood Charm, Gem of Focus, Tyrfing,
    Sundering Echo, Spear of the Magus, Pendulum Blade, Lernaean Bow, Titan''s Bane,
    Gluttonous Grimoire, Bragi''s Harp, Doom Orb, Totem of Death, Genji''s Guard,
    Toxic Blade, The World Stone, Bracer of The Abyss, Golden Blade, Damaru, Dominance,
    Breastplate of Valor, Eros'' Bow, Riptalon, Dreamer''s Idol, Chandra''s Grace,
    Qin''s Blade, Ancient Signet, Polynomicon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.25
      fit: 0.59
    Hydra's Lament:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.32
      fit: 0.55
    Death Metal:
      total: 0.53
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.56
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.81
      win: 0.6
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.55
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Tekko-Kagi
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
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
    Underrated for this god: Rod of Tahuti, Tekko-Kagi, Death Metal, Tyrfing, Silverbranch
    Bow, Titan''s Bane, Lernaean Bow, Obsidian Shard, Golden Blade, Nimble Ring, Spear
    of Desolation, Bragi''s Harp, Sundering Echo, Toxic Blade, Dominance, Soul Gem,
    The Reaper, Spear of the Magus, Riptalon, Demon Blade, Deathbringer, Musashi''s
    Dual Swords, Gluttonous Grimoire, Doom Orb, Bracer of The Abyss, Arondight, The
    World Stone, Qin''s Blade, Rage, Pendulum Blade, Transcendence, Eros'' Bow, Avatar''s
    Parashu, Runeforged Hammer, Dreamer''s Idol, Berserker''s Shield, Chronos'' Pendant,
    Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.25
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.46
      win: 0.6
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.69
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.81
      win: 0.6
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
