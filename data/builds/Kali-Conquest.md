---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.4
  aspect_win_rate: 0.68
  slot_order:
  - name: Tyrfing
    pick_rate: 0.49
    win_rate: 0.57
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.12
      win_rate: 0.8
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.33
  - name: Odysseus' Bow
    pick_rate: 0.32
    win_rate: 0.59
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.15
      win_rate: 0.38
    - name: Barbed Carver
      pick_rate: 0.11
      win_rate: 0.78
  - name: Hastened Fatalis
    pick_rate: 0.32
    win_rate: 0.59
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.5
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.83
  - name: Silverbranch Bow
    pick_rate: 0.18
    win_rate: 0.73
    alternates:
    - name: The Executioner
      pick_rate: 0.11
      win_rate: 0.33
    - name: Odysseus' Bow
      pick_rate: 0.1
      win_rate: 0.63
  - name: The Executioner
    pick_rate: 0.18
    win_rate: 0.71
    alternates:
    - name: Manchu Bow
      pick_rate: 0.08
      win_rate: 0.67
    - name: Silverbranch Bow
      pick_rate: 0.07
      win_rate: 0.4
  - name: Toxic Blade
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Manchu Bow
      pick_rate: 0.09
      win_rate: 0.75
    - name: Hunter's Bow
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.68
  - name: Leather Cowl
    pick_rate: 0.21
    win_rate: 0.44
  - name: Bumba's Hammer
    pick_rate: 0.12
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-09-26'
  god_win_rate: 0.5058823529411764
  god_matches_won: 43
  god_matches_played: 85
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-26'
  god_matches_analyzed: 4198
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Hydra's Lament
  - Death Metal
  - The Reaper
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - Tekko-Kagi
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, The Reaper, Hydra''s Lament, Death Metal, Tekko-Kagi,
    Lernaean Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of
    the Magus, Titan''s Bane, Spear of Desolation, The Crusher, Dominance, Obsidian
    Shard, Deathbringer, Soul Gem, Riptalon, Demon Blade, Gluttonous Grimoire, Bracer
    of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade,
    Transcendence, The World Stone, Arondight, Runeforged Hammer, Dreamer''s Idol,
    Damaru, Rage, Qin''s Blade, Ancient Signet, Chronos'' Pendant, Avenging Blade,
    Berserker''s Shield, Jotunn''s Revenge.'
  slot_scores:
    Lernaean Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.69
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.8
      pick: 0.12
      fit: 0.39
    Death Metal:
      total: 0.6
      efficiency: 0.61
      win: 0.69
      pick: 0.0
      fit: 0.51
    The Reaper:
      total: 0.62
      efficiency: 0.5
      win: 0.83
      pick: 0.11
      fit: 0.45
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.73
      pick: 0.3
      fit: 0.53
    Tekko-Kagi:
      total: 0.59
      efficiency: 0.49
      win: 0.69
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Hydra's Lament
  - The Reaper
  - Silverbranch Bow
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
    of Tahuti, Hydra''s Lament, Death Metal, The Reaper, Spear of Desolation, Nimble
    Ring, Soul Gem, Spear of the Magus, Obsidian Shard, Heartseeker, Bragi''s Harp,
    Lernaean Bow, Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet, The World
    Stone, Chronos'' Pendant, Dominance, Bracer of The Abyss, Titan''s Bane, The Crusher,
    Dreamer''s Idol, Transcendence, Deathbringer, Golden Blade, Arondight, Gem of
    Focus, Book of Thoth, Polynomicon, Pendulum Blade, Runeforged Hammer, Musashi''s
    Dual Swords, Soul Reaver, Riptalon, Avatar''s Parashu, Rod of Asclepius, The Cosmic
    Horror, Demon Blade, Jotunn''s Revenge.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.69
      pick: 0.0
      fit: 0.28
    Transcendence:
      total: 0.54
      efficiency: 0.53
      win: 0.69
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.12
      fit: 0.49
    Death Metal:
      total: 0.61
      efficiency: 0.61
      win: 0.69
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.69
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.69
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Hydra's Lament
  - The Reaper
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Silverbranch Bow
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
    this god: Amanita Charm, The Reaper, Rod of Tahuti, Berserker''s Shield, Hydra''s
    Lament, Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass, Soul Gem, Death
    Metal, Runeforged Hammer, Golden Blade, Freya''s Tears, Riptalon, Gluttonous Grimoire,
    Genji''s Guard, Shifter''s Shield, Shield Splitter, Breastplate of Valor, Ethereal
    Staff, Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse, Lernaean Bow, Phoenix
    Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Eye of Providence, Spear of the
    Magus, Heartseeker, Tekko-Kagi, Draconic Scale, Lifebinder, Avenging Blade, Helm
    of Radiance, Chandra''s Grace, Daybreak Gavel, Jotunn''s Revenge.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.69
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.8
      pick: 0.12
      fit: 0.28
    The Reaper:
      total: 0.64
      efficiency: 0.5
      win: 0.83
      pick: 0.11
      fit: 0.57
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.73
      pick: 0.3
      fit: 0.32
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Hydra's Lament
  - The Reaper
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Hydra's Lament
  - The Reaper
  - Silverbranch Bow
  - Spear of the Magus
  - Tekko-Kagi
  - Heartseeker
  flex_slots:
  - Heartseeker
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
    for this god: Rod of Tahuti, The Reaper, Hydra''s Lament, Tekko-Kagi, Heartseeker,
    Spear of the Magus, Death Metal, Spear of Desolation, Obsidian Shard, Titan''s
    Bane, Soul Gem, The Crusher, Gluttonous Grimoire, Riptalon, Lernaean Bow, Doom
    Orb, The World Stone, Nimble Ring, Avatar''s Parashu, Avenging Blade, Dreamer''s
    Idol, Pendulum Blade, Bragi''s Harp, Golden Blade, Dominance, Deathbringer, The
    Cosmic Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s
    Dual Swords, Transcendence, Runeforged Hammer, Arondight, Ancient Signet, Chronos''
    Pendant, Damaru, Jotunn''s Revenge.'
  slot_scores:
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.8
      pick: 0.12
      fit: 0.32
    The Reaper:
      total: 0.64
      efficiency: 0.5
      win: 0.83
      pick: 0.11
      fit: 0.57
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.73
      pick: 0.3
      fit: 0.64
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.69
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.6
      efficiency: 0.49
      win: 0.69
      pick: 0.0
      fit: 0.76
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.69
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Hydra's Lament
  - The Reaper
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Hydra's Lament
  - Nimble Ring
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Riptalon
  - Death Metal
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
    this god: Rod of Tahuti, The Reaper, Hydra''s Lament, Nimble Ring, Riptalon, Death
    Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade,
    Spear of the Magus, Bragi''s Harp, Heartseeker, Obsidian Shard, Spear of Desolation,
    Dominance, Bracer of The Abyss, Qin''s Blade, Titan''s Bane, The Crusher, Deathbringer,
    Demon Blade, Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound
    Book, Transcendence, Dreamer''s Idol, Musashi''s Dual Swords, Chronos'' Pendant,
    Runeforged Hammer, Arondight, Berserker''s Shield, Avatar''s Parashu, Bancroft''s
    Talon, Pendulum Blade, Jotunn''s Revenge.'
  slot_scores:
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.8
      pick: 0.12
      fit: 0.27
    Nimble Ring:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.69
      pick: 0.0
      fit: 0.32
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.69
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.73
      pick: 0.3
      fit: 0.57
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.69
      pick: 0.0
      fit: 0.18
  community_ordered:
  - Hydra's Lament
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Hydra''s Lament, Spear
    of Desolation, Soul Gem, The Reaper, Death Metal, Chronos'' Pendant, Nimble Ring,
    Spear of the Magus, Arondight, Gem of Focus, Obsidian Shard, Lernaean Bow, Pendulum
    Blade, Tekko-Kagi, Heartseeker, Gluttonous Grimoire, Bragi''s Harp, Bracer of
    The Abyss, Totem of Death, Doom Orb, The World Stone, Ancient Signet, Titan''s
    Bane, Riptalon, The Crusher, Breastplate of Valor, Golden Blade, Dreamer''s Idol,
    Deathbringer, Dominance, Genji''s Guard, Transcendence, Musashi''s Dual Swords,
    Runeforged Hammer, Demon Blade, Qin''s Blade, Avatar''s Parashu, Jotunn''s Revenge.'
  slot_scores:
    Hydra's Lament:
      total: 0.64
      efficiency: 0.54
      win: 0.8
      pick: 0.12
      fit: 0.55
    Death Metal:
      total: 0.58
      efficiency: 0.61
      win: 0.69
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.69
      pick: 0.0
      fit: 0.59
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.73
      pick: 0.3
      fit: 0.37
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.69
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.69
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Hydra's Lament
  - Silverbranch Bow
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
    Lernaean Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of
    the Magus, Hydra''s Lament, Titan''s Bane, Spear of Desolation, The Crusher, Dominance,
    Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Riptalon, Demon Blade, Gluttonous
    Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom
    Orb, Pendulum Blade, Transcendence, The World Stone, Arondight, Runeforged Hammer,
    Dreamer''s Idol, Damaru, Rage, Qin''s Blade, Ancient Signet, Chronos'' Pendant,
    Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.69
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.33
      pick: 0.11
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.57
      pick: 0.49
      fit: 0.68
    Death Metal:
      total: 0.6
      efficiency: 0.61
      win: 0.69
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.59
      efficiency: 0.49
      win: 0.69
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.69
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  starter: *id001
---
