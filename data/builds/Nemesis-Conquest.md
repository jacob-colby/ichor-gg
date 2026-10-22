---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.26
  aspect_win_rate: 0.67
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.36
    win_rate: 0.48
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.28
      win_rate: 0.68
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.44
  - name: Sanguine Lash
    pick_rate: 0.14
    win_rate: 0.73
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.78
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.5
  - name: Berserker's Shield
    pick_rate: 0.13
    win_rate: 0.7
    alternates:
    - name: The Crusher
      pick_rate: 0.11
      win_rate: 0.33
    - name: Sanguine Lash
      pick_rate: 0.08
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Golden Blade
      pick_rate: 0.07
      win_rate: 0.6
    - name: The Crusher
      pick_rate: 0.07
      win_rate: 0.4
  - name: Avatar's Parashu
    pick_rate: 0.09
    win_rate: 0.83
    alternates:
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.6
    - name: Magi's Cloak
      pick_rate: 0.06
      win_rate: 1.0
  - name: Axe
    pick_rate: 0.1
    win_rate: 0.8
    alternates:
    - name: Skeggox
      pick_rate: 0.08
      win_rate: 0.5
    - name: Hunter's Bow
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.25
    win_rate: 0.65
  - name: Hunter's Cowl
    pick_rate: 0.24
    win_rate: 0.63
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-10-22'
  god_win_rate: 0.5625
  god_matches_won: 45
  god_matches_played: 80
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-22'
  god_matches_analyzed: 1760
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Magi's Cloak
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Avatar's Parashu
  flex_slots:
  - Tekko-Kagi
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch Bow, Lernaean
    Bow, Golden Blade, Jotunn''s Revenge, Nimble Ring, Bragi''s Harp, Spear of the
    Magus, Riptalon, Spear of Desolation, Titan''s Bane, Dominance, Obsidian Shard,
    Deathbringer, Soul Gem, The Reaper, Toxic Blade, Demon Blade, Gluttonous Grimoire,
    Bracer of The Abyss, Musashi''s Dual Swords, Doom Orb, Pendulum Blade, Transcendence,
    The World Stone, Arondight, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol,
    Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Magi's Cloak:
      total: 0.55
      efficiency: 0.26
      win: 1.0
      pick: 0.13
      fit: 0.0
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.69
    Avatar's Parashu:
      total: 0.61
      efficiency: 0.45
      win: 0.83
      pick: 0.19
      fit: 0.44
  community_ordered:
  - Magi's Cloak
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Magi's Cloak
  - Death Metal
  - Doom Orb
  - Rod of Tahuti
  - Avatar's Parashu
  flex_slots:
  - Jotunn's Revenge
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Spear of Desolation, Nimble Ring, Soul Gem, Spear of the
    Magus, Jotunn''s Revenge, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow,
    Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos''
    Pendant, Silverbranch Bow, Dominance, Bracer of The Abyss, Golden Blade, Titan''s
    Bane, Dreamer''s Idol, Transcendence, Deathbringer, The Reaper, Arondight, Gem
    of Focus, Book of Thoth, Polynomicon, Pendulum Blade, Riptalon, Runeforged Hammer,
    Musashi''s Dual Swords, Soul Reaver, Rod of Asclepius, The Cosmic Horror, Toxic
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.11
      fit: 0.52
    Magi's Cloak:
      total: 0.55
      efficiency: 0.26
      win: 1.0
      pick: 0.13
      fit: 0.0
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.54
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.45
      win: 0.83
      pick: 0.19
      fit: 0.34
  community_ordered:
  - Jotunn's Revenge
  - Magi's Cloak
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Magi's Cloak
  - Shield of the Phoenix
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Soul Gem, Golden Blade, Death Metal, The Reaper, Riptalon, Runeforged
    Hammer, Freya''s Tears, Gluttonous Grimoire, Genji''s Guard, Shifter''s Shield,
    Breastplate of Valor, Shield Splitter, Ethereal Staff, Yogi''s Necklace, Eye of
    the Storm, Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix Feather, Erosion,
    Nimble Ring, Shogun''s Ofuda, Toxic Blade, Silverbranch Bow, Eye of Providence,
    Spear of the Magus, Tekko-Kagi, Lifebinder, Draconic Scale, Avenging Blade, Helm
    of Radiance, Chandra''s Grace, Daybreak Gavel, Jotunn''s Revenge.'
  slot_scores:
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.7
      pick: 0.2
      fit: 0.42
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.49
    Magi's Cloak:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.13
      fit: 0.24
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.6
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.45
      win: 0.83
      pick: 0.19
      fit: 0.27
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Berserker's Shield
  - Magi's Cloak
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Magi's Cloak
  - Silverbranch Bow
  - Spear of the Magus
  - Tekko-Kagi
  - Rod of Tahuti
  - Avatar's Parashu
  flex_slots:
  - Magi's Cloak
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Silverbranch Bow, Tekko-Kagi, Spear of the Magus,
    Jotunn''s Revenge, Death Metal, Spear of Desolation, Obsidian Shard, Titan''s
    Bane, Soul Gem, Riptalon, The Reaper, Gluttonous Grimoire, Tyrfing, Toxic Blade,
    Lernaean Bow, Doom Orb, The World Stone, Nimble Ring, Avenging Blade, Golden Blade,
    Dreamer''s Idol, Pendulum Blade, Bragi''s Harp, Dominance, Deathbringer, The Cosmic
    Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords,
    Transcendence, The Executioner, Runeforged Hammer, Arondight, Ancient Signet,
    Qin''s Blade, Chronos'' Pendant.'
  slot_scores:
    Magi's Cloak:
      total: 0.55
      efficiency: 0.26
      win: 1.0
      pick: 0.13
      fit: 0.0
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.76
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.43
    Avatar's Parashu:
      total: 0.63
      efficiency: 0.45
      win: 0.83
      pick: 0.19
      fit: 0.57
  community_ordered:
  - Magi's Cloak
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Magi's Cloak
  - Tyrfing
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Riptalon, Tyrfing, Silverbranch Bow, Death
    Metal, Soul Gem, Lernaean Bow, Golden Blade, Gluttonous Grimoire, Tekko-Kagi,
    The Reaper, Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian Shard, Spear
    of Desolation, Dominance, Jotunn''s Revenge, Bracer of The Abyss, Qin''s Blade,
    Titan''s Bane, Deathbringer, Demon Blade, Doom Orb, The World Stone, Ancient Signet,
    Sun Beam Bow, Blood-Bound Book, Transcendence, Dreamer''s Idol, Chronos'' Pendant,
    Musashi''s Dual Swords, Runeforged Hammer, Arondight, Bancroft''s Talon, Pendulum
    Blade.'
  slot_scores:
    Magi's Cloak:
      total: 0.55
      efficiency: 0.26
      win: 1.0
      pick: 0.13
      fit: 0.0
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.67
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.57
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.45
      win: 0.83
      pick: 0.19
      fit: 0.27
  community_ordered:
  - Magi's Cloak
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Magi's Cloak
  - Spear of Desolation
  - Rod of Tahuti
  - Avatar's Parashu
  - Soul Gem
  flex_slots:
  - Magi's Cloak
  - Jotunn's Revenge
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Jotunn''s Revenge, Death Metal, Chronos'' Pendant, Nimble Ring, Spear
    of the Magus, Silverbranch Bow, Arondight, Gem of Focus, Obsidian Shard, Tyrfing,
    Lernaean Bow, Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp,
    Golden Blade, Bracer of The Abyss, Totem of Death, Doom Orb, Riptalon, The World
    Stone, Ancient Signet, Titan''s Bane, Breastplate of Valor, Dreamer''s Idol, Toxic
    Blade, Deathbringer, Dominance, Genji''s Guard, The Reaper, Qin''s Blade, Transcendence,
    Musashi''s Dual Swords, Runeforged Hammer, Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.11
      fit: 0.59
    Magi's Cloak:
      total: 0.55
      efficiency: 0.26
      win: 1.0
      pick: 0.13
      fit: 0.0
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.24
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.45
      win: 0.83
      pick: 0.19
      fit: 0.24
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Magi's Cloak
  - Avatar's Parashu
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
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.11
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
