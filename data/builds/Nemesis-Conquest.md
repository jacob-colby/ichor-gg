---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.24
  aspect_win_rate: 0.5
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.22
    win_rate: 0.64
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.22
      win_rate: 0.68
    - name: Jotunn's Revenge
      pick_rate: 0.18
      win_rate: 0.22
  - name: Berserker's Shield
    pick_rate: 0.12
    win_rate: 0.75
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.18
      win_rate: 0.5
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.7
  - name: The Reaper
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.78
    - name: Daybreak Gavel
      pick_rate: 0.05
      win_rate: 0.4
  - name: Heartseeker
    pick_rate: 0.2
    win_rate: 0.68
    alternates:
    - name: The Reaper
      pick_rate: 0.06
      win_rate: 0.33
    - name: Dominance
      pick_rate: 0.05
      win_rate: 0.8
  - name: Skeggox
    pick_rate: 0.06
    win_rate: 0.4
    alternates:
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.5
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 0.0
  - name: Infused Axe
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Skeggox
      pick_rate: 0.05
      win_rate: 0.33
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.33
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.42
  - name: Bumba's Cudgel
    pick_rate: 0.18
    win_rate: 0.56
  - name: Hunter's Cowl
    pick_rate: 0.17
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-09-12'
  god_win_rate: 0.5098039215686274
  god_matches_won: 52
  god_matches_played: 102
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-12'
  god_matches_analyzed: 4284
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Transcendence
  - Hydra's Lament
  - Dominance
  - The Crusher
  - Heartseeker
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    this god: Dominance, The Crusher, Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi,
    Silverbranch Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear
    of the Magus, Riptalon, Spear of Desolation, Obsidian Shard, Deathbringer, Soul
    Gem, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s
    Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence, The World
    Stone, Arondight, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage,
    Ancient Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow, Titan''s Bane.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.06
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.25
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.39
    Dominance:
      total: 0.61
      efficiency: 0.45
      win: 0.8
      pick: 0.08
      fit: 0.59
    The Crusher:
      total: 0.6
      efficiency: 0.47
      win: 0.78
      pick: 0.14
      fit: 0.54
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.68
      pick: 0.33
      fit: 0.64
  community_ordered:
  - Hydra's Lament
  - Dominance
  - The Crusher
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Hydra's Lament
  - Death Metal
  - Dominance
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Dominance, The Crusher, Death Metal, Spear of Desolation, Nimble Ring,
    Soul Gem, Spear of the Magus, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean
    Bow, Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone,
    Chronos'' Pendant, Silverbranch Bow, Bracer of The Abyss, Golden Blade, Dreamer''s
    Idol, Transcendence, Deathbringer, Arondight, Gem of Focus, Book of Thoth, Polynomicon,
    Pendulum Blade, Riptalon, Runeforged Hammer, Musashi''s Dual Swords, Soul Reaver,
    Avatar''s Parashu, Rod of Asclepius, The Cosmic Horror, Toxic Blade, Titan''s
    Bane.'
  slot_scores:
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.49
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.54
    Dominance:
      total: 0.6
      efficiency: 0.45
      win: 0.8
      pick: 0.08
      fit: 0.53
    The Crusher:
      total: 0.59
      efficiency: 0.47
      win: 0.78
      pick: 0.14
      fit: 0.44
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.68
      pick: 0.33
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Hydra's Lament
  - Dominance
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Daybreak Gavel
  - Dominance
  - The Crusher
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Daybreak Gavel
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Soul Gem, Golden Blade, Death Metal, Riptalon, Runeforged Hammer,
    Freya''s Tears, Gluttonous Grimoire, Genji''s Guard, Shifter''s Shield, Breastplate
    of Valor, Shield Splitter, Ethereal Staff, Yogi''s Necklace, Eye of the Storm,
    Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix Feather, Erosion, Nimble Ring,
    Shogun''s Ofuda, Toxic Blade, Silverbranch Bow, Eye of Providence, Spear of the
    Magus, Tekko-Kagi, Lifebinder, Draconic Scale, Avenging Blade, Helm of Radiance,
    Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.75
      pick: 0.16
      fit: 0.42
    Daybreak Gavel:
      total: 0.55
      efficiency: 0.59
      win: 0.68
      pick: 0.22
      fit: 0.15
    Dominance:
      total: 0.58
      efficiency: 0.45
      win: 0.8
      pick: 0.08
      fit: 0.4
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.78
      pick: 0.14
      fit: 0.37
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.68
      pick: 0.33
      fit: 0.47
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Berserker's Shield
  - Daybreak Gavel
  - Dominance
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Hydra's Lament
  - Dominance
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  flex_slots:
  - Tekko-Kagi
  - Hydra's Lament
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
    for this god: The Crusher, Rod of Tahuti, Dominance, Silverbranch Bow, Tekko-Kagi,
    Spear of the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Soul Gem,
    Riptalon, Gluttonous Grimoire, Tyrfing, Toxic Blade, Lernaean Bow, Doom Orb, The
    World Stone, Nimble Ring, Avatar''s Parashu, Avenging Blade, Dreamer''s Idol,
    Pendulum Blade, Golden Blade, Bragi''s Harp, Deathbringer, The Cosmic Horror,
    Bracer of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords, Transcendence,
    The Executioner, Runeforged Hammer, Arondight, Ancient Signet, Qin''s Blade, Chronos''
    Pendant, Titan''s Bane.'
  slot_scores:
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.32
    Dominance:
      total: 0.59
      efficiency: 0.45
      win: 0.8
      pick: 0.08
      fit: 0.48
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.68
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.62
      efficiency: 0.47
      win: 0.78
      pick: 0.14
      fit: 0.67
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.68
      pick: 0.33
      fit: 0.77
  community_ordered:
  - Hydra's Lament
  - Dominance
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Nimble Ring
  - Dominance
  - Riptalon
  - The Crusher
  - Heartseeker
  flex_slots:
  - Nimble Ring
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Dominance, Rod of Tahuti, The Crusher, Nimble Ring, Riptalon, Tyrfing,
    Silverbranch Bow, Death Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi,
    Golden Blade, Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian Shard,
    Spear of Desolation, Bracer of The Abyss, Qin''s Blade, Deathbringer, Demon Blade,
    Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound Book, Transcendence,
    Dreamer''s Idol, Chronos'' Pendant, Musashi''s Dual Swords, Runeforged Hammer,
    Arondight, Avatar''s Parashu, Bancroft''s Talon, Pendulum Blade, Titan''s Bane.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.46
      win: 0.75
      pick: 0.16
      fit: 0.26
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.39
    Dominance:
      total: 0.59
      efficiency: 0.45
      win: 0.8
      pick: 0.08
      fit: 0.49
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.78
      pick: 0.14
      fit: 0.37
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.68
      pick: 0.33
      fit: 0.47
  community_ordered:
  - Berserker's Shield
  - Dominance
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Hydra's Lament
  - Dominance
  - Spear of Desolation
  - The Crusher
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Soul Gem
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Dominance, The Crusher,
    Spear of Desolation, Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear
    of the Magus, Silverbranch Bow, Arondight, Gem of Focus, Obsidian Shard, Tyrfing,
    Lernaean Bow, Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp,
    Bracer of The Abyss, Totem of Death, Doom Orb, Riptalon, Golden Blade, The World
    Stone, Ancient Signet, Breastplate of Valor, Dreamer''s Idol, Toxic Blade, Deathbringer,
    Genji''s Guard, Qin''s Blade, Transcendence, Musashi''s Dual Swords, Runeforged
    Hammer, Demon Blade, Avatar''s Parashu, Titan''s Bane.'
  slot_scores:
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.55
    Dominance:
      total: 0.58
      efficiency: 0.45
      win: 0.8
      pick: 0.08
      fit: 0.38
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.78
      pick: 0.14
      fit: 0.34
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.68
      pick: 0.33
      fit: 0.44
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Hydra's Lament
  - Dominance
  - The Crusher
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
    Riptalon, Spear of Desolation, Titan''s Bane, The Crusher, Dominance, Obsidian
    Shard, Deathbringer, Soul Gem, Toxic Blade, Demon Blade, Gluttonous Grimoire,
    Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum
    Blade, Transcendence, The World Stone, Arondight, Qin''s Blade, Runeforged Hammer,
    Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade,
    Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.72
      win: 0.22
      pick: 0.18
      fit: 0.49
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
