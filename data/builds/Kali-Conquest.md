---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.58
  slot_order:
  - name: Tyrfing
    pick_rate: 0.4
    win_rate: 0.6
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.39
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.51
  - name: Hastened Fatalis
    pick_rate: 0.2
    win_rate: 0.65
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.15
      win_rate: 0.57
    - name: The Cosmic Horror
      pick_rate: 0.07
      win_rate: 0.49
  - name: Polynomicon
    pick_rate: 0.13
    win_rate: 0.42
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.12
      win_rate: 0.6
    - name: Sun Beam Bow
      pick_rate: 0.12
      win_rate: 0.58
  - name: Odysseus' Bow
    pick_rate: 0.12
    win_rate: 0.55
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.33
    - name: Silverbranch Bow
      pick_rate: 0.09
      win_rate: 0.64
  - name: The Executioner
    pick_rate: 0.14
    win_rate: 0.68
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.41
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.53
  - name: Silverbranch Bow
    pick_rate: 0.13
    win_rate: 0.71
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.1
      win_rate: 0.61
    - name: Manchu Bow
      pick_rate: 0.07
      win_rate: 0.61
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.22
    win_rate: 0.65
  - name: Archmage's Gem
    pick_rate: 0.21
    win_rate: 0.6
  - name: Conduit Gem
    pick_rate: 0.13
    win_rate: 0.3
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-08-23'
  god_win_rate: 0.5392156862745098
  god_matches_won: 275
  god_matches_played: 510
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-23'
  god_matches_analyzed: 15677
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
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
    this god: Jotunn''s Revenge, Death Metal, Tekko-Kagi, Lernaean Bow, Heartseeker,
    Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus, Hydra''s Lament,
    Titan''s Bane, The Crusher, Dominance, Deathbringer, Soul Gem, The Reaper, Riptalon,
    Demon Blade, Toxic Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s
    Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade, Transcendence, The World
    Stone, Arondight, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Qin''s Blade,
    Ancient Signet, Chronos'' Pendant, Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.6
      pick: 0.4
      fit: 0.68
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.71
      pick: 0.4
      fit: 0.53
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.69
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Hydra's Lament
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Death Metal, Hydra''s Lament, Nimble Ring, Soul Gem, Spear of the Magus,
    Heartseeker, Bragi''s Harp, Lernaean Bow, Doom Orb, Tekko-Kagi, Gluttonous Grimoire,
    Ancient Signet, The World Stone, Chronos'' Pendant, Dominance, Bracer of The Abyss,
    Titan''s Bane, The Crusher, Dreamer''s Idol, Transcendence, Deathbringer, Golden
    Blade, The Reaper, Arondight, Gem of Focus, Pendulum Blade, Runeforged Hammer,
    Musashi''s Dual Swords, Soul Reaver, Riptalon, Avatar''s Parashu, Rod of Asclepius,
    Demon Blade, Book of Thoth, The Cosmic Horror.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.6
      pick: 0.4
      fit: 0.51
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.54
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.71
      pick: 0.4
      fit: 0.34
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.17
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Tyrfing
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, Rod of Asclepius, Kinetic Cuirass, Soul Gem, Death Metal, The Reaper,
    Runeforged Hammer, Golden Blade, Freya''s Tears, Riptalon, Gluttonous Grimoire,
    Genji''s Guard, Shifter''s Shield, Shield Splitter, Breastplate of Valor, Ethereal
    Staff, Yogi''s Necklace, Eye of the Storm, Pharaoh''s Curse, Lernaean Bow, Phoenix
    Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Eye of Providence, Spear of the
    Magus, Heartseeker, Tekko-Kagi, Draconic Scale, Lifebinder, Toxic Blade, Avenging
    Blade, Helm of Radiance, Hydra''s Lament, Chandra''s Grace, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.3
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.6
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.6
      pick: 0.4
      fit: 0.45
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.71
      pick: 0.4
      fit: 0.32
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  - Tekko-Kagi
  - Heartseeker
  flex_slots:
  - Heartseeker
  - The Executioner
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
    for this god: Jotunn''s Revenge, Tekko-Kagi, Heartseeker, Spear of the Magus,
    Death Metal, Titan''s Bane, Soul Gem, The Crusher, The Reaper, Gluttonous Grimoire,
    Riptalon, Lernaean Bow, Doom Orb, Toxic Blade, The World Stone, Nimble Ring, Avatar''s
    Parashu, Avenging Blade, Dreamer''s Idol, Hydra''s Lament, Pendulum Blade, Bragi''s
    Harp, Golden Blade, Dominance, Deathbringer, Bracer of The Abyss, Oath-Sworn Spear,
    Demon Blade, Musashi''s Dual Swords, Transcendence, Runeforged Hammer, Arondight,
    Ancient Signet, Chronos'' Pendant, Damaru, The Cosmic Horror.'
  slot_scores:
    The Executioner:
      total: 0.53
      efficiency: 0.35
      win: 0.68
      pick: 0.3
      fit: 0.59
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.61
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.6
      pick: 0.4
      fit: 0.55
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.71
      pick: 0.4
      fit: 0.64
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.76
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.77
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
    this god: Jotunn''s Revenge, Nimble Ring, Riptalon, Death Metal, Soul Gem, Lernaean
    Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Spear of the Magus,
    Toxic Blade, Bragi''s Harp, Heartseeker, Dominance, Hydra''s Lament, Bracer of
    The Abyss, Qin''s Blade, Titan''s Bane, The Crusher, Deathbringer, Demon Blade,
    Doom Orb, The World Stone, Ancient Signet, Blood-Bound Book, Transcendence, Dreamer''s
    Idol, Musashi''s Dual Swords, Chronos'' Pendant, Runeforged Hammer, Arondight,
    Berserker''s Shield, Avatar''s Parashu, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.31
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.6
      pick: 0.4
      fit: 0.67
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.32
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.71
      pick: 0.4
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Tyrfing
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Hydra''s
    Lament, Death Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Arondight,
    Gem of Focus, Lernaean Bow, Pendulum Blade, Tekko-Kagi, Heartseeker, Gluttonous
    Grimoire, Bragi''s Harp, Bracer of The Abyss, Totem of Death, Doom Orb, The World
    Stone, Ancient Signet, Titan''s Bane, Riptalon, The Crusher, Breastplate of Valor,
    Golden Blade, Dreamer''s Idol, Deathbringer, Dominance, Genji''s Guard, The Reaper,
    Toxic Blade, Transcendence, Musashi''s Dual Swords, Runeforged Hammer, Demon Blade,
    Qin''s Blade, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.6
      pick: 0.4
      fit: 0.44
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.55
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.34
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.71
      pick: 0.4
      fit: 0.37
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.69
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
    Underrated for this god: Jotunn''s Revenge, Death Metal, Tekko-Kagi, Lernaean
    Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus,
    Hydra''s Lament, Titan''s Bane, The Crusher, Dominance, Deathbringer, Soul Gem,
    The Reaper, Riptalon, Demon Blade, Toxic Blade, Gluttonous Grimoire, Bracer of
    The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade,
    Transcendence, The World Stone, Arondight, Runeforged Hammer, Dreamer''s Idol,
    Damaru, Rage, Qin''s Blade, Ancient Signet, Chronos'' Pendant, Avenging Blade,
    Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.6
      pick: 0.4
      fit: 0.68
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.41
      pick: 0.17
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Death Metal
  - Hastened Fatalis
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - The Executioner
  - Hastened Fatalis
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Death Metal, Tekko-Kagi,
    Lernaean Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of
    the Magus, Hydra''s Lament, Titan''s Bane, The Crusher, Dominance, Deathbringer,
    Soul Gem, The Reaper, Riptalon, Demon Blade, Toxic Blade, Gluttonous Grimoire,
    Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum
    Blade, Transcendence, The World Stone, Arondight, Runeforged Hammer, Dreamer''s
    Idol, Damaru, Rage, Qin''s Blade, Ancient Signet, Chronos'' Pendant, Avenging
    Blade, Berserker''s Shield.'
  slot_scores:
    The Executioner:
      total: 0.5
      efficiency: 0.35
      win: 0.68
      pick: 0.3
      fit: 0.35
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.51
    Hastened Fatalis:
      total: 0.47
      efficiency: 0.32
      win: 0.65
      pick: 0.27
      fit: 0.34
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.71
      pick: 0.4
      fit: 0.53
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.41
      pick: 0.17
      fit: 0.26
  swaps:
  - added: Silverbranch Bow
    removed: Lernaean Bow
    reason: community 71% win over 66 matches (vs 54% on this god), taking the model's
      weakest slot from Lernaean Bow
  - added: The Executioner
    removed: Tyrfing
    reason: community 68% win over 71 matches (vs 54% on this god), taking the model's
      weakest slot from Tyrfing
  - added: Hastened Fatalis
    removed: Tekko-Kagi
    reason: community 65% win over 102 matches (vs 54% on this god), taking the model's
      weakest slot from Tekko-Kagi
  starter: *id001
---
