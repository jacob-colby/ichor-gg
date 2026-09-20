---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.52
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.3
    win_rate: 0.57
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.27
      win_rate: 0.57
    - name: Jotunn's Revenge
      pick_rate: 0.16
      win_rate: 0.52
  - name: Jotunn's Revenge
    pick_rate: 0.12
    win_rate: 0.4
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.19
      win_rate: 0.58
    - name: The Crusher
      pick_rate: 0.07
      win_rate: 0.74
  - name: The Crusher
    pick_rate: 0.1
    win_rate: 0.62
    alternates:
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.59
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.62
  - name: Heartseeker
    pick_rate: 0.3
    win_rate: 0.63
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.38
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.53
  - name: Avatar's Parashu
    pick_rate: 0.08
    win_rate: 0.62
    alternates:
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.64
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.67
  - name: Skeggox
    pick_rate: 0.1
    win_rate: 0.59
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.65
    - name: Axe
      pick_rate: 0.06
      win_rate: 0.83
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.29
    win_rate: 0.57
  - name: Hunter's Cowl
    pick_rate: 0.21
    win_rate: 0.56
  - name: Bumba's Cudgel
    pick_rate: 0.18
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-09-20'
  god_win_rate: 0.5503875968992248
  god_matches_won: 213
  god_matches_played: 387
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-20'
  god_matches_analyzed: 14083
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Heartseeker
  - Titan's Bane
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Tyrfing, Titan''s Bane, Tekko-Kagi, Silverbranch
    Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus,
    Riptalon, Spear of Desolation, Dominance, Obsidian Shard, Deathbringer, Soul Gem,
    Toxic Blade, Demon Blade, The Reaper, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Doom Orb, Pendulum Blade, Transcendence, The World Stone,
    Arondight, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient
    Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.62
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.62
      pick: 0.0
      fit: 0.69
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.63
      pick: 0.5
      fit: 0.64
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.13
      fit: 0.54
  community_ordered:
  - Heartseeker
  - Titan's Bane
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
    of Tahuti, Death Metal, Spear of Desolation, Nimble Ring, Soul Gem, Spear of the
    Magus, Titan''s Bane, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow, Doom
    Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos''
    Pendant, Silverbranch Bow, Dominance, Bracer of The Abyss, Golden Blade, Dreamer''s
    Idol, Transcendence, Deathbringer, Arondight, Gem of Focus, Book of Thoth, The
    Reaper, Polynomicon, Pendulum Blade, Riptalon, Runeforged Hammer, Musashi''s Dual
    Swords, Soul Reaver, Rod of Asclepius, The Cosmic Horror, Toxic Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.28
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.3
      fit: 0.49
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.63
      pick: 0.5
      fit: 0.62
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.62
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
  - Shield of the Phoenix
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Soul Gem, Golden Blade, Death Metal, Shifter''s
    Shield, Riptalon, Runeforged Hammer, Freya''s Tears, Gluttonous Grimoire, The
    Reaper, Genji''s Guard, Breastplate of Valor, Shield Splitter, Ethereal Staff,
    Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix
    Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Toxic Blade, Silverbranch Bow,
    Eye of Providence, Spear of the Magus, Tekko-Kagi, Lifebinder, Draconic Scale,
    Avenging Blade, Helm of Radiance, Chandra''s Grace.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.6
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.5
      fit: 0.47
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Crusher
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Titan''s Bane, Silverbranch Bow, Tekko-Kagi, Spear
    of the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Soul Gem, Riptalon,
    Gluttonous Grimoire, Tyrfing, Toxic Blade, The Reaper, Lernaean Bow, Doom Orb,
    The World Stone, Nimble Ring, Avenging Blade, Dreamer''s Idol, Pendulum Blade,
    Golden Blade, Bragi''s Harp, Dominance, Deathbringer, The Cosmic Horror, Bracer
    of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords, Transcendence,
    The Executioner, Runeforged Hammer, Arondight, Ancient Signet, Qin''s Blade, Chronos''
    Pendant.'
  slot_scores:
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.39
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.68
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.62
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.62
      pick: 0.16
      fit: 0.67
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.63
      pick: 0.5
      fit: 0.77
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.13
      fit: 0.67
  community_ordered:
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Death Metal
  - Riptalon
  - Heartseeker
  - Silverbranch Bow
  flex_slots:
  - Heartseeker
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
    this god: Rod of Tahuti, Nimble Ring, Riptalon, Tyrfing, Silverbranch Bow, Death
    Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Titan''s Bane,
    Golden Blade, The Reaper, Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian
    Shard, Spear of Desolation, Dominance, Bracer of The Abyss, Qin''s Blade, Deathbringer,
    Demon Blade, Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound
    Book, Transcendence, Dreamer''s Idol, Chronos'' Pendant, Musashi''s Dual Swords,
    Runeforged Hammer, Arondight, Berserker''s Shield, Bancroft''s Talon, Pendulum
    Blade.'
  slot_scores:
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.62
      pick: 0.0
      fit: 0.67
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.32
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.65
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.5
      fit: 0.47
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Heartseeker
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
    Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Titan''s
    Bane, Silverbranch Bow, Arondight, Gem of Focus, Obsidian Shard, Tyrfing, Lernaean
    Bow, Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp, Bracer of
    The Abyss, Totem of Death, Doom Orb, Riptalon, Golden Blade, The World Stone,
    Ancient Signet, Breastplate of Valor, Dreamer''s Idol, Toxic Blade, Deathbringer,
    Dominance, Genji''s Guard, The Reaper, Qin''s Blade, Transcendence, Musashi''s
    Dual Swords, Runeforged Hammer, Demon Blade.'
  slot_scores:
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.3
      fit: 0.55
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.59
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.5
      fit: 0.44
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Hydra's Lament
  - Heartseeker
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
    Riptalon, Spear of Desolation, Titan''s Bane, Dominance, Obsidian Shard, Deathbringer,
    Soul Gem, The Reaper, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of
    The Abyss, Musashi''s Dual Swords, Doom Orb, Pendulum Blade, Transcendence, The
    World Stone, Arondight, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol, Damaru,
    Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.4
      pick: 0.16
      fit: 0.49
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.62
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.62
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
