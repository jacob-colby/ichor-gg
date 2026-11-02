---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.31
  aspect_win_rate: 0.6
  slot_order:
  - name: Tyrfing
    pick_rate: 0.41
    win_rate: 0.57
    alternates:
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.49
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.53
  - name: Hastened Fatalis
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.64
    - name: Dagger of Frenzy
      pick_rate: 0.08
      win_rate: 0.48
  - name: Silverbranch Bow
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.63
    - name: Hastened Fatalis
      pick_rate: 0.11
      win_rate: 0.49
  - name: Odysseus' Bow
    pick_rate: 0.13
    win_rate: 0.66
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.68
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.54
  - name: The Executioner
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.09
      win_rate: 0.54
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.5
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.68
    alternates:
    - name: Bow
      pick_rate: 0.07
      win_rate: 0.5
    - name: Manchu Bow
      pick_rate: 0.07
      win_rate: 0.63
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.25
    win_rate: 0.6
  - name: Archmage's Gem
    pick_rate: 0.13
    win_rate: 0.56
  - name: Death's Embrace
    pick_rate: 0.11
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-11-02'
  god_win_rate: 0.5365168539325843
  god_matches_won: 191
  god_matches_played: 356
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
  - Tekko-Kagi
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Titan's Bane
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
    this god: Jotunn''s Revenge, Rod of Tahuti, Tekko-Kagi, Death Metal, Titan''s
    Bane, Lernaean Bow, Obsidian Shard, Nimble Ring, Heartseeker, Golden Blade, Bragi''s
    Harp, Spear of Desolation, Sundering Echo, The Crusher, Hydra''s Lament, Dominance,
    Soul Gem, The Reaper, Toxic Blade, Spear of the Magus, Demon Blade, Deathbringer,
    Musashi''s Dual Swords, Gluttonous Grimoire, Riptalon, Doom Orb, Bracer of The
    Abyss, Arondight, The World Stone, Rage, Pendulum Blade, Transcendence, Eros''
    Bow, Qin''s Blade, Avatar''s Parashu, Runeforged Hammer, Dreamer''s Idol, Berserker''s
    Shield, Chronos'' Pendant, The Cosmic Horror.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.46
      win: 0.57
      pick: 0.41
      fit: 0.68
    Death Metal:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.69
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.5
      win: 0.56
      pick: 0.25
      fit: 0.53
    Titan's Bane:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
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
  - Hydra's Lament
  - Nimble Ring
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
    of Tahuti, Jotunn''s Revenge, Death Metal, Spear of Desolation, Obsidian Shard,
    Sundering Echo, Soul Gem, Tekko-Kagi, Hydra''s Lament, Nimble Ring, Titan''s Bane,
    Bragi''s Harp, Doom Orb, Spear of the Magus, The World Stone, Heartseeker, Lernaean
    Bow, Gluttonous Grimoire, Dominance, Chronos'' Pendant, The Crusher, Heartwood
    Charm, Bracer of The Abyss, Ancient Signet, Polynomicon, Arondight, The Reaper,
    Golden Blade, Dreamer''s Idol, Transcendence, Eros'' Bow, Gem of Focus, Blood-Bound
    Book, Soul Reaver, Deathbringer, Musashi''s Dual Swords, The Cosmic Horror, Pendulum
    Blade, Toxic Blade, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.5
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.36
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.81
      win: 0.5
      pick: 0.13
      fit: 0.42
  community_ordered:
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Death Metal
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Jotunn''s Revenge,
    Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Death Metal, The Reaper, Genji''s
    Guard, Yogi''s Necklace, Shield Splitter, Golden Blade, Phoenix Feather, Tekko-Kagi,
    Runeforged Hammer, Ethereal Staff, Gluttonous Grimoire, Breastplate of Valor,
    Titan''s Bane, Riptalon, Obsidian Shard, Freya''s Tears, Pharaoh''s Curse, Toxic
    Blade, Chandra''s Grace, Oni Hunter''s Garb, Blood-Bound Book, Erosion, Shogun''s
    Ofuda, Lernaean Bow, Eye of Providence, Eros'' Bow, Nimble Ring, Draconic Scale,
    Midgardian Mail, Spear of Desolation, Hydra''s Lament, Sundering Echo, Rod of
    Asclepius.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.7
      win: 0.56
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.6
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Tekko-Kagi
  - Silverbranch Bow
  - Titan's Bane
  - Rod of Tahuti
  flex_slots:
  - Titan's Bane
  - Spear of Desolation
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Tekko-Kagi, Titan''s Bane, Obsidian
    Shard, Spear of Desolation, Death Metal, Heartseeker, The Crusher, Soul Gem, Spear
    of the Magus, The Reaper, Toxic Blade, Gluttonous Grimoire, Doom Orb, The World
    Stone, Lernaean Bow, Riptalon, Nimble Ring, Sundering Echo, Hydra''s Lament, Dreamer''s
    Idol, Avenging Blade, Pendulum Blade, Avatar''s Parashu, Dominance, Bragi''s Harp,
    Golden Blade, The Cosmic Horror, Deathbringer, Musashi''s Dual Swords, Bracer
    of The Abyss, Arondight, Oath-Sworn Spear, Transcendence, Demon Blade, Rage, Eros''
    Bow, Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.47
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.76
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.5
      win: 0.56
      pick: 0.25
      fit: 0.64
    Titan's Bane:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.67
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.81
      win: 0.5
      pick: 0.13
      fit: 0.43
  community_ordered:
  - Silverbranch Bow
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Tekko-Kagi
  - Silverbranch Bow
  - Riptalon
  flex_slots:
  - Tekko-Kagi
  - Riptalon
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
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Tekko-Kagi, Riptalon,
    Death Metal, Soul Gem, Gluttonous Grimoire, Lernaean Bow, Golden Blade, The Reaper,
    Toxic Blade, Obsidian Shard, Titan''s Bane, Spear of Desolation, Dominance, Bragi''s
    Harp, Sundering Echo, Hydra''s Lament, Qin''s Blade, Heartseeker, Spear of the
    Magus, Bracer of The Abyss, The Crusher, Blood-Bound Book, Eros'' Bow, Doom Orb,
    The World Stone, Berserker''s Shield, Demon Blade, Sun Beam Bow, Deathbringer,
    Arondight, Musashi''s Dual Swords, Chronos'' Pendant, Transcendence, Bloodforge,
    Dreamer''s Idol, Bancroft''s Talon, Dagger of Frenzy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.31
    Tyrfing:
      total: 0.54
      efficiency: 0.46
      win: 0.57
      pick: 0.41
      fit: 0.67
    Nimble Ring:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.39
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.5
      win: 0.56
      pick: 0.25
      fit: 0.57
    Riptalon:
      total: 0.51
      efficiency: 0.45
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
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Spear of Desolation, Soul Gem, Hydra''s Lament, Death Metal, Chronos'' Pendant,
    Obsidian Shard, Tekko-Kagi, Arondight, Nimble Ring, Heartwood Charm, Gem of Focus,
    Titan''s Bane, Sundering Echo, Spear of the Magus, Pendulum Blade, Lernaean Bow,
    Gluttonous Grimoire, Bragi''s Harp, Doom Orb, Totem of Death, Genji''s Guard,
    The World Stone, Bracer of The Abyss, Heartseeker, The Crusher, Damaru, Toxic
    Blade, Dominance, Golden Blade, Breastplate of Valor, The Reaper, Eros'' Bow,
    Dreamer''s Idol, Chandra''s Grace, Riptalon, Ancient Signet, Polynomicon, Deathbringer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.55
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.81
      win: 0.5
      pick: 0.13
      fit: 0.24
    Soul Gem:
      total: 0.53
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Tekko-Kagi
  - Titan's Bane
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Titan's Bane
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
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Tekko-Kagi, Death Metal,
    Titan''s Bane, Lernaean Bow, Obsidian Shard, Nimble Ring, Heartseeker, Golden
    Blade, Bragi''s Harp, Spear of Desolation, Sundering Echo, The Crusher, Hydra''s
    Lament, Dominance, Soul Gem, The Reaper, Toxic Blade, Spear of the Magus, Demon
    Blade, Deathbringer, Musashi''s Dual Swords, Gluttonous Grimoire, Riptalon, Doom
    Orb, Bracer of The Abyss, Arondight, The World Stone, Rage, Pendulum Blade, Transcendence,
    Eros'' Bow, Qin''s Blade, Avatar''s Parashu, Runeforged Hammer, Dreamer''s Idol,
    Berserker''s Shield, Chronos'' Pendant, The Cosmic Horror.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.46
      win: 0.57
      pick: 0.41
      fit: 0.68
    Death Metal:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.69
    Titan's Bane:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.81
      win: 0.5
      pick: 0.13
      fit: 0.26
  community_ordered:
  - Tyrfing
  - Rod of Tahuti
  starter: *id001
---
