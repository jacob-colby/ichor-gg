---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.44
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.31
    win_rate: 0.52
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.25
      win_rate: 0.56
    - name: Devourer's Gauntlet
      pick_rate: 0.11
      win_rate: 0.57
  - name: Jotunn's Revenge
    pick_rate: 0.11
    win_rate: 0.52
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.25
      win_rate: 0.6
    - name: Arondight
      pick_rate: 0.06
      win_rate: 0.42
  - name: The Crusher
    pick_rate: 0.12
    win_rate: 0.64
    alternates:
    - name: Arondight
      pick_rate: 0.08
      win_rate: 0.73
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.46
  - name: Heartseeker
    pick_rate: 0.31
    win_rate: 0.56
    alternates:
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.58
    - name: The Crusher
      pick_rate: 0.06
      win_rate: 0.8
  - name: Blinking Abyss
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.61
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.5
  - name: Skeggox
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Magi's Cloak
      pick_rate: 0.1
      win_rate: 0.64
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.63
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.27
    win_rate: 0.59
  - name: Hunter's Cowl
    pick_rate: 0.19
    win_rate: 0.67
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.31
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-09-28'
  god_win_rate: 0.5132275132275133
  god_matches_won: 97
  god_matches_played: 189
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-28'
  god_matches_analyzed: 7013
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Arondight
  - The Crusher
  - Heartseeker
  flex_slots:
  - Tyrfing
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Arondight, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch
    Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus,
    Riptalon, Spear of Desolation, The Reaper, Dominance, Obsidian Shard, Deathbringer,
    Soul Gem, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence,
    The World Stone, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage,
    Ancient Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.52
      pick: 0.15
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.51
    Arondight:
      total: 0.55
      efficiency: 0.5
      win: 0.73
      pick: 0.12
      fit: 0.29
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.64
      pick: 0.19
      fit: 0.54
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.56
      pick: 0.52
      fit: 0.64
  community_ordered:
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Arondight
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Transcendence
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Arondight, Death Metal, Spear of Desolation, Nimble Ring, Soul Gem,
    Spear of the Magus, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow, Doom
    Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos''
    Pendant, Silverbranch Bow, Dominance, Bracer of The Abyss, The Reaper, Golden
    Blade, Dreamer''s Idol, Transcendence, Deathbringer, Gem of Focus, Book of Thoth,
    Polynomicon, Pendulum Blade, Riptalon, Runeforged Hammer, Musashi''s Dual Swords,
    Soul Reaver, Avatar''s Parashu, Rod of Asclepius, The Cosmic Horror, Toxic Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.52
      pick: 0.15
      fit: 0.52
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.28
    Arondight:
      total: 0.56
      efficiency: 0.5
      win: 0.73
      pick: 0.12
      fit: 0.31
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.56
      pick: 0.52
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Arondight
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Arondight
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Soul Gem, The Reaper, Golden Blade, Death Metal,
    Riptalon, Runeforged Hammer, Freya''s Tears, Gluttonous Grimoire, Genji''s Guard,
    Shifter''s Shield, Breastplate of Valor, Shield Splitter, Ethereal Staff, Yogi''s
    Necklace, Eye of the Storm, Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix Feather,
    Erosion, Nimble Ring, Shogun''s Ofuda, Toxic Blade, Silverbranch Bow, Eye of Providence,
    Spear of the Magus, Tekko-Kagi, Lifebinder, Draconic Scale, Avenging Blade, Helm
    of Radiance, Chandra''s Grace, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.52
      pick: 0.15
      fit: 0.3
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.6
    Arondight:
      total: 0.54
      efficiency: 0.5
      win: 0.73
      pick: 0.12
      fit: 0.18
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Arondight
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Arondight
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  flex_slots:
  - Tekko-Kagi
  - Arondight
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
    for this god: Rod of Tahuti, Silverbranch Bow, Tekko-Kagi, Arondight, Spear of
    the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Soul Gem, The Reaper,
    Riptalon, Gluttonous Grimoire, Tyrfing, Toxic Blade, Lernaean Bow, Doom Orb, The
    World Stone, Nimble Ring, Avatar''s Parashu, Avenging Blade, Dreamer''s Idol,
    Pendulum Blade, Golden Blade, Bragi''s Harp, Dominance, Deathbringer, The Cosmic
    Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords,
    Transcendence, The Executioner, Runeforged Hammer, Ancient Signet, Qin''s Blade,
    Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.52
      pick: 0.15
      fit: 0.61
    Arondight:
      total: 0.54
      efficiency: 0.5
      win: 0.73
      pick: 0.12
      fit: 0.22
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.68
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.64
      pick: 0.19
      fit: 0.67
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.56
      pick: 0.52
      fit: 0.77
  community_ordered:
  - Jotunn's Revenge
  - Arondight
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Arondight
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
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
    this god: Rod of Tahuti, Nimble Ring, Riptalon, Arondight, Tyrfing, Silverbranch
    Bow, Death Metal, Soul Gem, Lernaean Bow, The Reaper, Gluttonous Grimoire, Tekko-Kagi,
    Golden Blade, Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian Shard,
    Spear of Desolation, Dominance, Bracer of The Abyss, Qin''s Blade, Deathbringer,
    Demon Blade, Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound
    Book, Transcendence, Dreamer''s Idol, Chronos'' Pendant, Musashi''s Dual Swords,
    Runeforged Hammer, Berserker''s Shield, Avatar''s Parashu, Bancroft''s Talon,
    Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.52
      pick: 0.15
      fit: 0.31
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.67
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.39
    Arondight:
      total: 0.54
      efficiency: 0.5
      win: 0.73
      pick: 0.12
      fit: 0.17
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - Arondight
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Arondight
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Arondight, Spear of
    Desolation, Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear of the
    Magus, Silverbranch Bow, Gem of Focus, Obsidian Shard, Tyrfing, Lernaean Bow,
    Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp, Bracer of The
    Abyss, Totem of Death, Doom Orb, Riptalon, Golden Blade, The World Stone, Ancient
    Signet, The Reaper, Breastplate of Valor, Dreamer''s Idol, Toxic Blade, Deathbringer,
    Dominance, Genji''s Guard, Qin''s Blade, Transcendence, Musashi''s Dual Swords,
    Runeforged Hammer, Demon Blade, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.52
      pick: 0.15
      fit: 0.59
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.34
    Arondight:
      total: 0.58
      efficiency: 0.5
      win: 0.73
      pick: 0.12
      fit: 0.45
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Arondight
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
    Underrated for this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch
    Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus,
    Riptalon, Spear of Desolation, Dominance, Obsidian Shard, Deathbringer, Soul Gem,
    The Reaper, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence,
    The World Stone, Arondight, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol,
    Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.52
      pick: 0.15
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
