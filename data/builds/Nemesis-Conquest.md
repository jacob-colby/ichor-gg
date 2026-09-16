---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.49
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.32
    win_rate: 0.56
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.23
      win_rate: 0.61
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.35
  - name: Jotunn's Revenge
    pick_rate: 0.09
    win_rate: 0.32
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.17
      win_rate: 0.54
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.73
  - name: The Crusher
    pick_rate: 0.13
    win_rate: 0.61
    alternates:
    - name: The Reaper
      pick_rate: 0.08
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.73
  - name: Heartseeker
    pick_rate: 0.29
    win_rate: 0.61
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.43
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.45
  - name: Avatar's Parashu
    pick_rate: 0.1
    win_rate: 0.65
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.67
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.67
  - name: Skeggox
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.6
    - name: Void Shard
      pick_rate: 0.05
      win_rate: 0.29
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.3
    win_rate: 0.51
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.58
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-09-16'
  god_win_rate: 0.5083333333333333
  god_matches_won: 122
  god_matches_played: 240
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-16'
  god_matches_analyzed: 9166
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Tyrfing
  - Death Metal
  - The Reaper
  - Silverbranch Bow
  - Heartseeker
  - Tekko-Kagi
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
    this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, The Reaper, Silverbranch
    Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus,
    Riptalon, Spear of Desolation, Titan''s Bane, Dominance, Obsidian Shard, Deathbringer,
    Soul Gem, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Doom Orb, Pendulum Blade, Transcendence, The World Stone,
    Arondight, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient
    Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow, Jotunn''s Revenge.'
  slot_scores:
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.61
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.51
    The Reaper:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.12
      fit: 0.44
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.58
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.61
      pick: 0.48
      fit: 0.64
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.69
  community_ordered:
  - The Reaper
  - Heartseeker
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Spear of Desolation, Nimble Ring, Soul Gem, Spear of the
    Magus, The Reaper, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow, Doom
    Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos''
    Pendant, Silverbranch Bow, Dominance, Bracer of The Abyss, Titan''s Bane, Golden
    Blade, Dreamer''s Idol, Transcendence, Deathbringer, Arondight, Gem of Focus,
    Book of Thoth, Polynomicon, Pendulum Blade, Riptalon, Runeforged Hammer, Musashi''s
    Dual Swords, Soul Reaver, Rod of Asclepius, The Cosmic Horror, Toxic Blade, Jotunn''s
    Revenge.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.28
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.32
      fit: 0.49
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.61
      pick: 0.48
      fit: 0.62
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Hydra's Lament
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - The Reaper
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Amanita Charm, Rod of Tahuti, Shifter''s Shield, Berserker''s Shield,
    The Reaper, Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass, Soul Gem,
    Golden Blade, Death Metal, Riptalon, Runeforged Hammer, Freya''s Tears, Gluttonous
    Grimoire, Genji''s Guard, Breastplate of Valor, Shield Splitter, Ethereal Staff,
    Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix
    Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Toxic Blade, Silverbranch Bow,
    Eye of Providence, Spear of the Magus, Tekko-Kagi, Lifebinder, Draconic Scale,
    Avenging Blade, Helm of Radiance, Chandra''s Grace, Jotunn''s Revenge.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.49
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.12
      fit: 0.57
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.73
      pick: 0.09
      fit: 0.39
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.69
  community_ordered:
  - The Reaper
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - The Reaper
  - Silverbranch Bow
  - Spear of the Magus
  - Tekko-Kagi
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Tekko-Kagi
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
    for this god: Rod of Tahuti, The Reaper, Silverbranch Bow, Tekko-Kagi, Spear of
    the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Titan''s Bane, Soul
    Gem, Riptalon, Gluttonous Grimoire, Tyrfing, Toxic Blade, Lernaean Bow, Doom Orb,
    The World Stone, Nimble Ring, Avenging Blade, Dreamer''s Idol, Pendulum Blade,
    Golden Blade, Bragi''s Harp, Dominance, Deathbringer, The Cosmic Horror, Bracer
    of The Abyss, Jotunn''s Revenge, Oath-Sworn Spear, Demon Blade, Musashi''s Dual
    Swords, Transcendence, The Executioner, Runeforged Hammer, Arondight, Ancient
    Signet, Qin''s Blade, Chronos'' Pendant.'
  slot_scores:
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.12
      fit: 0.57
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.76
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.61
      pick: 0.48
      fit: 0.77
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.43
  community_ordered:
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - Death Metal
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
    this god: Rod of Tahuti, Nimble Ring, The Reaper, Riptalon, Tyrfing, Silverbranch
    Bow, Death Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden
    Blade, Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian Shard, Spear of
    Desolation, Dominance, Bracer of The Abyss, Qin''s Blade, Titan''s Bane, Deathbringer,
    Demon Blade, Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound
    Book, Transcendence, Dreamer''s Idol, Chronos'' Pendant, Musashi''s Dual Swords,
    Runeforged Hammer, Arondight, Berserker''s Shield, Bancroft''s Talon, Pendulum
    Blade, Jotunn''s Revenge.'
  slot_scores:
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.61
      pick: 0.0
      fit: 0.67
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.32
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.18
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Silverbranch
    Bow, The Reaper, Arondight, Gem of Focus, Obsidian Shard, Tyrfing, Lernaean Bow,
    Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp, Bracer of The
    Abyss, Totem of Death, Doom Orb, Riptalon, Golden Blade, The World Stone, Ancient
    Signet, Titan''s Bane, Breastplate of Valor, Jotunn''s Revenge, Dreamer''s Idol,
    Toxic Blade, Deathbringer, Dominance, Genji''s Guard, Qin''s Blade, Transcendence,
    Musashi''s Dual Swords, Runeforged Hammer, Demon Blade.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.45
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.56
      pick: 0.32
      fit: 0.55
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Hydra's Lament
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
    Tekko-Kagi, Silverbranch Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s
    Harp, Spear of the Magus, Riptalon, Spear of Desolation, Titan''s Bane, Dominance,
    Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Toxic Blade, Demon Blade,
    Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Doom Orb, Pendulum
    Blade, Transcendence, The World Stone, Arondight, Qin''s Blade, Runeforged Hammer,
    Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade,
    Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.32
      pick: 0.12
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.61
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
