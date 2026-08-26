---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.5
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.63
    win_rate: 0.73
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.25
      win_rate: 0.67
    - name: Bow
      pick_rate: 0.04
      win_rate: 1.0
  - name: Hydra's Lament
    pick_rate: 0.33
    win_rate: 0.75
    alternates:
    - name: Transcendence
      pick_rate: 0.21
      win_rate: 0.6
    - name: Arondight
      pick_rate: 0.13
      win_rate: 0.67
  - name: The Reaper
    pick_rate: 0.14
    win_rate: 1.0
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.23
      win_rate: 1.0
    - name: Mercury's Talaria
      pick_rate: 0.14
      win_rate: 1.0
  - name: Blinking Abyss
    pick_rate: 0.23
    win_rate: 0.8
    alternates:
    - name: The Reaper
      pick_rate: 0.18
      win_rate: 0.75
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 1.0
  - name: Titan's Bane
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.15
      win_rate: 1.0
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 1.0
  - name: Heartseeker
    pick_rate: 0.19
    win_rate: 0.67
    alternates:
    - name: Magi's Cloak
      pick_rate: 0.13
      win_rate: 1.0
    - name: Axe
      pick_rate: 0.13
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.42
    win_rate: 0.8
  - name: Bumba's Cudgel
    pick_rate: 0.21
    win_rate: 0.4
  - name: Hunter's Cowl
    pick_rate: 0.17
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-08-26'
  god_win_rate: 0.7083333333333334
  god_matches_won: 17
  god_matches_played: 24
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
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
    swap: Magi's Cloak — magical protection
    swap_item: Magi's Cloak
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch Bow, Lernaean
    Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus, Riptalon, Spear
    of Desolation, The Crusher, Dominance, Obsidian Shard, Deathbringer, Soul Gem,
    Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s
    Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, The World Stone, Qin''s
    Blade, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos''
    Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.73
      pick: 0.63
      fit: 0.49
    Tyrfing:
      total: 0.63
      efficiency: 0.48
      win: 0.78
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.64
      efficiency: 0.61
      win: 0.78
      pick: 0.0
      fit: 0.51
    The Reaper:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.22
      fit: 0.44
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.78
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.62
      efficiency: 0.49
      win: 0.78
      pick: 0.0
      fit: 0.69
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - The Reaper
  - Rod of Tahuti
  flex_slots:
  - Hydra's Lament
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Magi's Cloak — magical protection
    swap_item: Magi's Cloak
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Spear of Desolation, Nimble Ring, Soul Gem, Spear of the
    Magus, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow, Doom Orb, Tekko-Kagi,
    Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos'' Pendant, Silverbranch
    Bow, Dominance, Bracer of The Abyss, The Crusher, Golden Blade, Dreamer''s Idol,
    Deathbringer, Gem of Focus, Book of Thoth, Polynomicon, Pendulum Blade, Riptalon,
    Runeforged Hammer, Musashi''s Dual Swords, Soul Reaver, Avatar''s Parashu, Rod
    of Asclepius, The Cosmic Horror, Toxic Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.57
      efficiency: 0.51
      win: 0.78
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.73
      pick: 0.63
      fit: 0.52
    Hydra's Lament:
      total: 0.62
      efficiency: 0.54
      win: 0.75
      pick: 0.45
      fit: 0.49
    Death Metal:
      total: 0.64
      efficiency: 0.61
      win: 0.78
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.22
      fit: 0.34
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.78
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Magi's Cloak
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Rod of Asclepius, Kinetic Cuirass, Soul Gem, Golden Blade, Death Metal, Riptalon,
    Runeforged Hammer, Freya''s Tears, Gluttonous Grimoire, Genji''s Guard, Shifter''s
    Shield, Breastplate of Valor, Shield Splitter, Ethereal Staff, Yogi''s Necklace,
    Eye of the Storm, Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix Feather, Erosion,
    Nimble Ring, Shogun''s Ofuda, Toxic Blade, Silverbranch Bow, Eye of Providence,
    Spear of the Magus, Tekko-Kagi, Lifebinder, Draconic Scale, Avenging Blade, Helm
    of Radiance, Chandra''s Grace, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.78
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.73
      pick: 0.63
      fit: 0.3
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.78
      pick: 0.0
      fit: 0.49
    Magi's Cloak:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.4
      fit: 0.24
    The Reaper:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.22
      fit: 0.57
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.78
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Silverbranch Bow
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
    swap: Magi's Cloak — magical protection
    swap_item: Magi's Cloak
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Silverbranch Bow, Tekko-Kagi, Spear of the Magus,
    Death Metal, Spear of Desolation, Obsidian Shard, Soul Gem, The Crusher, Riptalon,
    Gluttonous Grimoire, Tyrfing, Toxic Blade, Lernaean Bow, Doom Orb, The World Stone,
    Nimble Ring, Avatar''s Parashu, Avenging Blade, Dreamer''s Idol, Pendulum Blade,
    Golden Blade, Bragi''s Harp, Dominance, Deathbringer, The Cosmic Horror, Bracer
    of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords, The Executioner,
    Runeforged Hammer, Ancient Signet, Qin''s Blade, Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.72
      win: 0.73
      pick: 0.63
      fit: 0.61
    The Reaper:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.22
      fit: 0.57
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.78
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.62
      efficiency: 0.6
      win: 0.78
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.63
      efficiency: 0.49
      win: 0.78
      pick: 0.0
      fit: 0.76
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.78
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Rod of Tahuti, Nimble Ring, Riptalon, Tyrfing, Silverbranch Bow, Death
    Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade,
    Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian Shard, Spear of Desolation,
    Dominance, Bracer of The Abyss, Qin''s Blade, The Crusher, Deathbringer, Demon
    Blade, Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound Book,
    Dreamer''s Idol, Chronos'' Pendant, Musashi''s Dual Swords, Runeforged Hammer,
    Berserker''s Shield, Avatar''s Parashu, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.73
      pick: 0.63
      fit: 0.31
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.78
      pick: 0.0
      fit: 0.67
    Nimble Ring:
      total: 0.63
      efficiency: 0.65
      win: 0.78
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.61
      efficiency: 0.61
      win: 0.78
      pick: 0.0
      fit: 0.32
    Riptalon:
      total: 0.62
      efficiency: 0.51
      win: 0.78
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.78
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - The Reaper
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Hydra's Lament
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Magi's Cloak — magical protection
    swap_item: Magi's Cloak
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Silverbranch
    Bow, Gem of Focus, Obsidian Shard, Tyrfing, Lernaean Bow, Pendulum Blade, Tekko-Kagi,
    Gluttonous Grimoire, Bragi''s Harp, Bracer of The Abyss, Totem of Death, Doom
    Orb, Riptalon, Golden Blade, The World Stone, Ancient Signet, The Crusher, Breastplate
    of Valor, Dreamer''s Idol, Toxic Blade, Deathbringer, Dominance, Genji''s Guard,
    Qin''s Blade, Musashi''s Dual Swords, Runeforged Hammer, Demon Blade, Avatar''s
    Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.72
      win: 0.73
      pick: 0.63
      fit: 0.59
    Hydra's Lament:
      total: 0.63
      efficiency: 0.54
      win: 0.75
      pick: 0.45
      fit: 0.55
    Death Metal:
      total: 0.61
      efficiency: 0.61
      win: 0.78
      pick: 0.0
      fit: 0.34
    The Reaper:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.22
      fit: 0.24
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.78
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.78
      pick: 0.0
      fit: 0.24
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
    Riptalon, Spear of Desolation, The Crusher, Dominance, Obsidian Shard, Deathbringer,
    Soul Gem, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, The World
    Stone, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient
    Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.73
      pick: 0.63
      fit: 0.49
    Tyrfing:
      total: 0.63
      efficiency: 0.48
      win: 0.78
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.64
      efficiency: 0.61
      win: 0.78
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.78
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.62
      efficiency: 0.49
      win: 0.78
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.78
      pick: 0.0
      fit: 0.26
  starter: *id001
---
