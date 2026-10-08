---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.25
  aspect_win_rate: 0.57
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.44
    win_rate: 0.54
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.31
      win_rate: 0.53
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.5
  - name: Sanguine Lash
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.18
      win_rate: 0.5
    - name: Arondight
      pick_rate: 0.13
      win_rate: 0.57
  - name: The Reaper
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.09
      win_rate: 0.4
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.6
  - name: Heartseeker
    pick_rate: 0.21
    win_rate: 0.36
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.75
    - name: Berserker's Shield
      pick_rate: 0.06
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.4
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.0
  - name: Skeggox
    pick_rate: 0.19
    win_rate: 0.4
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.11
      win_rate: 1.0
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.35
    win_rate: 0.53
  - name: Bumba's Cudgel
    pick_rate: 0.25
    win_rate: 0.43
  - name: Bumba's Hammer
    pick_rate: 0.16
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-10-08'
  god_win_rate: 0.5454545454545454
  god_matches_won: 30
  god_matches_played: 55
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Hide of the Nemean Lion
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - Tekko-Kagi
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Tyrfing, Tekko-Kagi,
    Silverbranch Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear
    of the Magus, Riptalon, Spear of Desolation, Titan''s Bane, The Crusher, Dominance,
    Obsidian Shard, Deathbringer, Soul Gem, Toxic Blade, Demon Blade, Gluttonous Grimoire,
    Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum
    Blade, Transcendence, The World Stone, Qin''s Blade, Runeforged Hammer, Dreamer''s
    Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade, Sun Beam
    Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.11
      fit: 0.49
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.54
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.51
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.0
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Hydra's Lament
  - Transcendence
  - Hide of the Nemean Lion
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Death Metal, Spear of Desolation, Nimble Ring, Soul
    Gem, Spear of the Magus, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow,
    Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos''
    Pendant, Silverbranch Bow, Dominance, Bracer of The Abyss, Titan''s Bane, The
    Crusher, Golden Blade, Dreamer''s Idol, Transcendence, Deathbringer, Gem of Focus,
    Book of Thoth, Polynomicon, Pendulum Blade, Riptalon, Runeforged Hammer, Musashi''s
    Dual Swords, Soul Reaver, Avatar''s Parashu, Rod of Asclepius, The Cosmic Horror,
    Toxic Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.11
      fit: 0.52
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.54
      pick: 0.44
      fit: 0.49
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.28
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.0
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.54
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Freya''s Tears, Amanita Charm, Rod of Tahuti, Jotunn''s
    Revenge, Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass, Soul Gem, Golden
    Blade, Death Metal, Riptalon, Runeforged Hammer, Gluttonous Grimoire, Genji''s
    Guard, Shifter''s Shield, Breastplate of Valor, Shield Splitter, Ethereal Staff,
    Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix
    Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Toxic Blade, Silverbranch Bow,
    Eye of Providence, Spear of the Magus, Tekko-Kagi, Lifebinder, Draconic Scale,
    Avenging Blade, Helm of Radiance, Chandra''s Grace, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.1
      fit: 0.42
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.11
      fit: 0.3
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.6
    Hide of the Nemean Lion:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.34
      fit: 0.27
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.75
      pick: 0.13
      fit: 0.27
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Silverbranch Bow
  - Hide of the Nemean Lion
  - Spear of the Magus
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Tekko-Kagi
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Silverbranch Bow, Tekko-Kagi,
    Spear of the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Titan''s
    Bane, Soul Gem, The Crusher, Riptalon, Gluttonous Grimoire, Tyrfing, Toxic Blade,
    Lernaean Bow, Doom Orb, The World Stone, Nimble Ring, Avatar''s Parashu, Avenging
    Blade, Dreamer''s Idol, Pendulum Blade, Golden Blade, Bragi''s Harp, Dominance,
    Deathbringer, The Cosmic Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon
    Blade, Musashi''s Dual Swords, Transcendence, The Executioner, Runeforged Hammer,
    Ancient Signet, Qin''s Blade, Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.11
      fit: 0.61
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.68
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.0
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.76
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.54
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Hide of the Nemean Lion
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Jotunn''s Revenge, Riptalon, Tyrfing, Silverbranch
    Bow, Berserker''s Shield, Death Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire,
    Tekko-Kagi, Golden Blade, Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian
    Shard, Spear of Desolation, Dominance, Bracer of The Abyss, Qin''s Blade, Titan''s
    Bane, The Crusher, Deathbringer, Demon Blade, Doom Orb, The World Stone, Ancient
    Signet, Sun Beam Bow, Blood-Bound Book, Transcendence, Dreamer''s Idol, Chronos''
    Pendant, Musashi''s Dual Swords, Runeforged Hammer, Avatar''s Parashu, Bancroft''s
    Talon, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.11
      fit: 0.31
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.54
      pick: 0.0
      fit: 0.67
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.0
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Hide of the Nemean Lion
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Spear of Desolation, Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear
    of the Magus, Silverbranch Bow, Gem of Focus, Obsidian Shard, Tyrfing, Lernaean
    Bow, Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp, Bracer of
    The Abyss, Totem of Death, Doom Orb, Riptalon, Golden Blade, The World Stone,
    Ancient Signet, Titan''s Bane, The Crusher, Breastplate of Valor, Dreamer''s Idol,
    Toxic Blade, Deathbringer, Dominance, Genji''s Guard, Qin''s Blade, Transcendence,
    Musashi''s Dual Swords, Runeforged Hammer, Demon Blade, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.11
      fit: 0.59
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.54
      pick: 0.44
      fit: 0.55
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.59
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.0
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.54
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
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
    Harp, Spear of the Magus, Riptalon, Spear of Desolation, Titan''s Bane, The Crusher,
    Dominance, Obsidian Shard, Deathbringer, Soul Gem, Toxic Blade, Demon Blade, Gluttonous
    Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom
    Orb, Pendulum Blade, Transcendence, The World Stone, Qin''s Blade, Runeforged
    Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging
    Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.11
      fit: 0.49
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.54
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.54
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
