---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.37
  aspect_win_rate: 0.55
  slot_order:
  - name: Tyrfing
    pick_rate: 0.53
    win_rate: 0.52
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.08
      win_rate: 0.69
    - name: Hydra's Lament
      pick_rate: 0.06
      win_rate: 0.7
  - name: Hastened Fatalis
    pick_rate: 0.32
    win_rate: 0.51
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.18
      win_rate: 0.55
    - name: Hydra's Lament
      pick_rate: 0.05
      win_rate: 0.5
  - name: Odysseus' Bow
    pick_rate: 0.24
    win_rate: 0.53
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.19
      win_rate: 0.51
    - name: Hydra's Lament
      pick_rate: 0.06
      win_rate: 0.61
  - name: The Executioner
    pick_rate: 0.19
    win_rate: 0.53
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.13
      win_rate: 0.55
    - name: Odysseus' Bow
      pick_rate: 0.09
      win_rate: 0.57
  - name: Silverbranch Bow
    pick_rate: 0.2
    win_rate: 0.69
    alternates:
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.57
    - name: The Executioner
      pick_rate: 0.07
      win_rate: 0.62
  - name: Manchu Bow
    pick_rate: 0.1
    win_rate: 0.52
    alternates:
    - name: Qin's Blade
      pick_rate: 0.1
      win_rate: 0.61
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.44
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.26
    win_rate: 0.7
  - name: Leather Cowl
    pick_rate: 0.16
    win_rate: 0.29
  - name: Death's Embrace
    pick_rate: 0.12
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-09-19'
  god_win_rate: 0.5495495495495496
  god_matches_won: 183
  god_matches_played: 333
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-19'
  god_matches_analyzed: 12806
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
  - Tekko-Kagi
  flex_slots:
  - Hydra's Lament
  - Tekko-Kagi
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
    this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Hydra''s Lament, Tekko-Kagi,
    Lernaean Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of
    the Magus, Titan''s Bane, Spear of Desolation, The Crusher, Dominance, Obsidian
    Shard, Deathbringer, Soul Gem, The Reaper, Demon Blade, Toxic Blade, Gluttonous
    Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom
    Orb, Pendulum Blade, Transcendence, The World Stone, Arondight, Runeforged Hammer,
    Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade,
    Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.52
      pick: 0.53
      fit: 0.68
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.61
      pick: 0.09
      fit: 0.39
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.69
      pick: 0.43
      fit: 0.53
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Tyrfing
  - Hydra's Lament
  - Silverbranch Bow
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Silverbranch Bow
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
    of Tahuti, Jotunn''s Revenge, Hydra''s Lament, Death Metal, Spear of Desolation,
    Nimble Ring, Soul Gem, Spear of the Magus, Obsidian Shard, Heartseeker, Bragi''s
    Harp, Lernaean Bow, Doom Orb, Tekko-Kagi, Gluttonous Grimoire, Ancient Signet,
    The World Stone, Chronos'' Pendant, Dominance, Bracer of The Abyss, Titan''s Bane,
    The Crusher, Dreamer''s Idol, Transcendence, Deathbringer, Golden Blade, The Reaper,
    Arondight, Gem of Focus, Book of Thoth, Polynomicon, Pendulum Blade, Runeforged
    Hammer, Musashi''s Dual Swords, Soul Reaver, Avatar''s Parashu, Rod of Asclepius,
    The Cosmic Horror, Demon Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.52
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.61
      pick: 0.09
      fit: 0.49
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.69
      pick: 0.43
      fit: 0.34
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Hydra's Lament
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Daybreak Gavel
  - Riptalon
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Riptalon
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
    this god: Amanita Charm, Rod of Tahuti, Daybreak Gavel, Berserker''s Shield, Jotunn''s
    Revenge, Shield of the Phoenix, Hydra''s Lament, Rod of Asclepius, Kinetic Cuirass,
    Soul Gem, Death Metal, The Reaper, Runeforged Hammer, Golden Blade, Freya''s Tears,
    Gluttonous Grimoire, Genji''s Guard, Shifter''s Shield, Shield Splitter, Breastplate
    of Valor, Ethereal Staff, Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse,
    Lernaean Bow, Phoenix Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Eye of Providence,
    Spear of the Magus, Heartseeker, Tekko-Kagi, Draconic Scale, Lifebinder, Toxic
    Blade, Avenging Blade, Helm of Radiance, Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.3
    Daybreak Gavel:
      total: 0.54
      efficiency: 0.59
      win: 0.69
      pick: 0.08
      fit: 0.15
    Riptalon:
      total: 0.52
      efficiency: 0.46
      win: 0.57
      pick: 0.15
      fit: 0.62
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.43
      fit: 0.32
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Daybreak Gavel
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Tekko-Kagi, Heartseeker, Hydra''s
    Lament, Spear of the Magus, Death Metal, Spear of Desolation, Obsidian Shard,
    Titan''s Bane, Soul Gem, The Crusher, The Reaper, Gluttonous Grimoire, Lernaean
    Bow, Doom Orb, Toxic Blade, The World Stone, Nimble Ring, Avatar''s Parashu, Avenging
    Blade, Dreamer''s Idol, Pendulum Blade, Bragi''s Harp, Golden Blade, Dominance,
    Deathbringer, The Cosmic Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon
    Blade, Musashi''s Dual Swords, Transcendence, Runeforged Hammer, Arondight, Ancient
    Signet, Chronos'' Pendant, Damaru.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.61
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.19
    Riptalon:
      total: 0.52
      efficiency: 0.46
      win: 0.57
      pick: 0.15
      fit: 0.64
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.69
      pick: 0.43
      fit: 0.64
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.76
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Qin's Blade
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Qin's Blade
  - Hydra's Lament
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
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Hydra''s Lament, Death
    Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade,
    The Reaper, Spear of the Magus, Toxic Blade, Bragi''s Harp, Heartseeker, Obsidian
    Shard, Spear of Desolation, Dominance, Bracer of The Abyss, Titan''s Bane, The
    Crusher, Deathbringer, Demon Blade, Doom Orb, The World Stone, Ancient Signet,
    Sun Beam Bow, Blood-Bound Book, Transcendence, Dreamer''s Idol, Musashi''s Dual
    Swords, Chronos'' Pendant, Runeforged Hammer, Arondight, Berserker''s Shield,
    Avatar''s Parashu, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.31
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.52
      pick: 0.53
      fit: 0.67
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.61
      pick: 0.09
      fit: 0.27
    Qin's Blade:
      total: 0.51
      efficiency: 0.37
      win: 0.61
      pick: 0.31
      fit: 0.63
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.57
      pick: 0.15
      fit: 0.65
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.69
      pick: 0.43
      fit: 0.57
  community_ordered:
  - Tyrfing
  - Hydra's Lament
  - Qin's Blade
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Silverbranch Bow
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
    Hydra''s Lament, Spear of Desolation, Soul Gem, Death Metal, Chronos'' Pendant,
    Nimble Ring, Spear of the Magus, Arondight, Gem of Focus, Obsidian Shard, Lernaean
    Bow, Pendulum Blade, Tekko-Kagi, Heartseeker, Gluttonous Grimoire, Bragi''s Harp,
    Bracer of The Abyss, Totem of Death, Doom Orb, The World Stone, Ancient Signet,
    Titan''s Bane, The Crusher, Breastplate of Valor, Golden Blade, Dreamer''s Idol,
    Deathbringer, Dominance, Genji''s Guard, The Reaper, Toxic Blade, Transcendence,
    Musashi''s Dual Swords, Runeforged Hammer, Demon Blade, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.61
      pick: 0.09
      fit: 0.55
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.59
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.69
      pick: 0.43
      fit: 0.37
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.52
      efficiency: 0.52
      win: 0.53
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
  - Tyrfing
  - Jotunn's Revenge
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
    Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Demon Blade, Toxic Blade,
    Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu,
    Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight, Runeforged
    Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging
    Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.52
      pick: 0.53
      fit: 0.68
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Death Metal, Tekko-Kagi, Lernaean Bow, Heartseeker, Nimble Ring, Bragi''s Harp,
    Golden Blade, Spear of the Magus, Hydra''s Lament, Titan''s Bane, Spear of Desolation,
    The Crusher, Dominance, Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Demon
    Blade, Toxic Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual
    Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence, The World
    Stone, Arondight, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet,
    Chronos'' Pendant, Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.52
      pick: 0.53
      fit: 0.68
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.69
      pick: 0.43
      fit: 0.53
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  swaps:
  - added: Silverbranch Bow
    removed: Lernaean Bow
    reason: community 69% win over 67 matches (vs 55% on this god), taking the model's
      weakest slot from Lernaean Bow
  starter: *id001
---
