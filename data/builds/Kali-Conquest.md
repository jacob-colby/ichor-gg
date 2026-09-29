---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.4
  aspect_win_rate: 0.63
  slot_order:
  - name: Tyrfing
    pick_rate: 0.47
    win_rate: 0.61
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.52
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.86
  - name: Odysseus' Bow
    pick_rate: 0.3
    win_rate: 0.61
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.15
      win_rate: 0.52
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.63
  - name: Hastened Fatalis
    pick_rate: 0.3
    win_rate: 0.65
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.1
      win_rate: 0.67
    - name: Polynomicon
      pick_rate: 0.08
      win_rate: 0.41
  - name: Silverbranch Bow
    pick_rate: 0.17
    win_rate: 0.62
    alternates:
    - name: The Executioner
      pick_rate: 0.11
      win_rate: 0.65
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.68
  - name: The Executioner
    pick_rate: 0.13
    win_rate: 0.54
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.09
      win_rate: 0.56
    - name: Riptalon
      pick_rate: 0.08
      win_rate: 0.67
  - name: Manchu Bow
    pick_rate: 0.08
    win_rate: 0.9
    alternates:
    - name: Toxic Blade
      pick_rate: 0.07
      win_rate: 0.67
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.56
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.55
  - name: Leather Cowl
    pick_rate: 0.15
    win_rate: 0.53
  - name: Bumba's Hammer
    pick_rate: 0.12
    win_rate: 0.73
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-09-29'
  god_win_rate: 0.5687203791469194
  god_matches_won: 120
  god_matches_played: 211
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-29'
  god_matches_analyzed: 8229
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Silverbranch Bow
  - Heartseeker
  flex_slots:
  - Jotunn's Revenge
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
    this god: Hydra''s Lament, Rod of Tahuti, Death Metal, Jotunn''s Revenge, Tekko-Kagi,
    Lernaean Bow, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus, Titan''s
    Bane, Spear of Desolation, The Crusher, Dominance, Obsidian Shard, Deathbringer,
    Soul Gem, The Reaper, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s
    Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence, The World
    Stone, Arondight, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Qin''s Blade,
    Ancient Signet, Chronos'' Pendant, Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.52
      pick: 0.1
      fit: 0.49
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.61
      pick: 0.47
      fit: 0.68
    Hydra's Lament:
      total: 0.64
      efficiency: 0.54
      win: 0.86
      pick: 0.1
      fit: 0.39
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.62
      pick: 0.28
      fit: 0.53
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.68
      pick: 0.15
      fit: 0.65
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Silverbranch Bow
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Rod of Tahuti, Death Metal, Jotunn''s Revenge, Spear of Desolation, Nimble
    Ring, Soul Gem, Spear of the Magus, Obsidian Shard, Bragi''s Harp, Lernaean Bow,
    Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos''
    Pendant, Dominance, Bracer of The Abyss, Titan''s Bane, The Crusher, Dreamer''s
    Idol, Transcendence, Deathbringer, Golden Blade, The Reaper, Arondight, Gem of
    Focus, Book of Thoth, Pendulum Blade, Runeforged Hammer, Musashi''s Dual Swords,
    Soul Reaver, Avatar''s Parashu, Rod of Asclepius, The Cosmic Horror, Demon Blade,
    Polynomicon.'
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
      total: 0.66
      efficiency: 0.54
      win: 0.86
      pick: 0.1
      fit: 0.49
    Death Metal:
      total: 0.58
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.68
      pick: 0.15
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Hydra's Lament
  - Riptalon
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Hydra''s Lament, Amanita Charm, Rod of Tahuti, Berserker''s Shield,
    Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass, Soul Gem, Death Metal,
    The Reaper, Runeforged Hammer, Golden Blade, Freya''s Tears, Gluttonous Grimoire,
    Jotunn''s Revenge, Genji''s Guard, Shifter''s Shield, Shield Splitter, Breastplate
    of Valor, Ethereal Staff, Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse,
    Lernaean Bow, Phoenix Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Eye of Providence,
    Spear of the Magus, Tekko-Kagi, Draconic Scale, Lifebinder, Avenging Blade, Helm
    of Radiance, Chandra''s Grace, Daybreak Gavel.'
  slot_scores:
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
    Hydra's Lament:
      total: 0.62
      efficiency: 0.54
      win: 0.86
      pick: 0.1
      fit: 0.28
    Riptalon:
      total: 0.56
      efficiency: 0.46
      win: 0.67
      pick: 0.17
      fit: 0.62
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.68
      pick: 0.15
      fit: 0.47
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Hydra's Lament
  - Riptalon
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Silverbranch Bow
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Hydra''s Lament, Jotunn''s Revenge, Tekko-Kagi, Spear
    of the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Titan''s Bane,
    Soul Gem, The Crusher, The Reaper, Gluttonous Grimoire, Lernaean Bow, Doom Orb,
    The World Stone, Nimble Ring, Avatar''s Parashu, Avenging Blade, Dreamer''s Idol,
    Pendulum Blade, Bragi''s Harp, Golden Blade, Dominance, Deathbringer, The Cosmic
    Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords,
    Transcendence, Runeforged Hammer, Arondight, Ancient Signet, Chronos'' Pendant,
    Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.05
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.52
      pick: 0.1
      fit: 0.61
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.19
    Hydra's Lament:
      total: 0.63
      efficiency: 0.54
      win: 0.86
      pick: 0.1
      fit: 0.32
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.62
      pick: 0.28
      fit: 0.64
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.68
      pick: 0.15
      fit: 0.77
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Silverbranch Bow
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Toxic Blade
  - Hydra's Lament
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Toxic Blade
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Rod of Tahuti, Nimble Ring, Death Metal, Soul Gem,
    Lernaean Bow, Jotunn''s Revenge, Gluttonous Grimoire, Tekko-Kagi, Golden Blade,
    The Reaper, Spear of the Magus, Bragi''s Harp, Obsidian Shard, Spear of Desolation,
    Dominance, Bracer of The Abyss, Qin''s Blade, Titan''s Bane, The Crusher, Deathbringer,
    Demon Blade, Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound
    Book, Transcendence, Dreamer''s Idol, Musashi''s Dual Swords, Chronos'' Pendant,
    Runeforged Hammer, Arondight, Berserker''s Shield, Avatar''s Parashu, Bancroft''s
    Talon, Pendulum Blade.'
  slot_scores:
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.61
      pick: 0.47
      fit: 0.67
    Toxic Blade:
      total: 0.55
      efficiency: 0.44
      win: 0.67
      pick: 0.22
      fit: 0.57
    Hydra's Lament:
      total: 0.62
      efficiency: 0.54
      win: 0.86
      pick: 0.1
      fit: 0.27
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.67
      pick: 0.17
      fit: 0.65
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.62
      pick: 0.28
      fit: 0.57
  community_ordered:
  - Tyrfing
  - Toxic Blade
  - Hydra's Lament
  - Riptalon
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Rod of Tahuti, Jotunn''s
    Revenge, Spear of Desolation, Soul Gem, Death Metal, Chronos'' Pendant, Nimble
    Ring, Spear of the Magus, Arondight, Gem of Focus, Obsidian Shard, Lernaean Bow,
    Pendulum Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp, Bracer of The
    Abyss, Totem of Death, Doom Orb, The World Stone, Ancient Signet, Titan''s Bane,
    The Crusher, Breastplate of Valor, Golden Blade, Dreamer''s Idol, Deathbringer,
    Dominance, Genji''s Guard, The Reaper, Transcendence, Musashi''s Dual Swords,
    Runeforged Hammer, Demon Blade, Qin''s Blade, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.52
      pick: 0.1
      fit: 0.59
    Hydra's Lament:
      total: 0.66
      efficiency: 0.54
      win: 0.86
      pick: 0.1
      fit: 0.55
    Death Metal:
      total: 0.55
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
    Rod of Tahuti:
      total: 0.62
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
  - Jotunn's Revenge
  - Hydra's Lament
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
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Tekko-Kagi,
    Lernaean Bow, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus, Hydra''s
    Lament, Titan''s Bane, Spear of Desolation, The Crusher, Dominance, Obsidian Shard,
    Deathbringer, Soul Gem, The Reaper, Demon Blade, Gluttonous Grimoire, Bracer of
    The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade,
    Transcendence, The World Stone, Arondight, Runeforged Hammer, Dreamer''s Idol,
    Damaru, Rage, Qin''s Blade, Ancient Signet, Chronos'' Pendant, Avenging Blade,
    Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.52
      pick: 0.1
      fit: 0.49
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.61
      pick: 0.47
      fit: 0.68
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.56
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
  - Tyrfing
  starter: *id001
---
