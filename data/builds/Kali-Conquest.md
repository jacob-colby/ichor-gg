---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.31
  aspect_win_rate: 0.53
  slot_order:
  - name: Tyrfing
    pick_rate: 0.37
    win_rate: 0.59
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.17
      win_rate: 0.49
    - name: Hydra's Lament
      pick_rate: 0.15
      win_rate: 0.53
  - name: Odysseus' Bow
    pick_rate: 0.19
    win_rate: 0.65
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.07
      win_rate: 0.3
    - name: Dagger of Frenzy
      pick_rate: 0.06
      win_rate: 0.68
  - name: Hastened Fatalis
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.69
    - name: Odysseus' Bow
      pick_rate: 0.1
      win_rate: 0.43
  - name: Silverbranch Bow
    pick_rate: 0.11
    win_rate: 0.64
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.12
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.41
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.52
    - name: The Executioner
      pick_rate: 0.06
      win_rate: 0.5
  - name: Qin's Blade
    pick_rate: 0.06
    win_rate: 0.54
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.12
      win_rate: 0.76
    - name: Manchu Bow
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.21
    win_rate: 0.56
  - name: Archmage's Gem
    pick_rate: 0.14
    win_rate: 0.56
  - name: Bumba's Hammer
    pick_rate: 0.12
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-10-16'
  god_win_rate: 0.528125
  god_matches_won: 169
  god_matches_played: 320
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-16'
  god_matches_analyzed: 10934
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Heartseeker
  flex_slots:
  - Lernaean Bow
  - Heartseeker
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
    this god: Death Metal, Tekko-Kagi, Lernaean Bow, Heartseeker, Nimble Ring, Bragi''s
    Harp, Hydra''s Lament, Golden Blade, Spear of the Magus, Titan''s Bane, Spear
    of Desolation, The Crusher, Dominance, Obsidian Shard, Deathbringer, Soul Gem,
    The Reaper, Riptalon, Demon Blade, Toxic Blade, Gluttonous Grimoire, Bracer of
    The Abyss, Musashi''s Dual Swords, Avatar''s Parashu, Doom Orb, Pendulum Blade,
    Transcendence, Jotunn''s Revenge, The World Stone, Arondight, Runeforged Hammer,
    Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade,
    Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.59
      pick: 0.37
      fit: 0.68
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.64
      pick: 0.18
      fit: 0.53
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.69
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.54
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Spear of Desolation, Hydra''s Lament, Nimble Ring, Soul Gem, Spear of the
    Magus, Obsidian Shard, Heartseeker, Bragi''s Harp, Lernaean Bow, Doom Orb, Tekko-Kagi,
    Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos'' Pendant, Dominance,
    Bracer of The Abyss, Titan''s Bane, The Crusher, Dreamer''s Idol, Transcendence,
    Deathbringer, Jotunn''s Revenge, Golden Blade, The Reaper, Arondight, Gem of Focus,
    Book of Thoth, Polynomicon, Pendulum Blade, Runeforged Hammer, Musashi''s Dual
    Swords, Soul Reaver, Riptalon, Avatar''s Parashu, Rod of Asclepius, The Cosmic
    Horror, Demon Blade.'
  slot_scores:
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.59
      pick: 0.37
      fit: 0.51
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.53
      pick: 0.15
      fit: 0.49
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.54
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.64
      pick: 0.18
      fit: 0.34
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.54
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.41
      pick: 0.15
      fit: 0.42
  community_ordered:
  - Tyrfing
  - Hydra's Lament
  - Silverbranch Bow
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Shield of the Phoenix
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Soul Gem, Death Metal, The Reaper, Runeforged Hammer, Golden
    Blade, Freya''s Tears, Riptalon, Gluttonous Grimoire, Genji''s Guard, Shifter''s
    Shield, Shield Splitter, Breastplate of Valor, Ethereal Staff, Yogi''s Necklace,
    Eye of the Storm, Pharaoh''s Curse, Lernaean Bow, Phoenix Feather, Erosion, Nimble
    Ring, Shogun''s Ofuda, Eye of Providence, Spear of the Magus, Hydra''s Lament,
    Heartseeker, Tekko-Kagi, Draconic Scale, Lifebinder, Toxic Blade, Avenging Blade,
    Helm of Radiance, Chandra''s Grace, Daybreak Gavel, Jotunn''s Revenge.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.59
      pick: 0.37
      fit: 0.45
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.64
      pick: 0.18
      fit: 0.32
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Tyrfing
  - Spear of the Magus
  - Silverbranch Bow
  - Tekko-Kagi
  - Heartseeker
  - Rod of Tahuti
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
    for this god: Tekko-Kagi, Heartseeker, Spear of the Magus, Death Metal, Spear
    of Desolation, Obsidian Shard, Titan''s Bane, Soul Gem, The Crusher, The Reaper,
    Gluttonous Grimoire, Riptalon, Lernaean Bow, Doom Orb, Toxic Blade, The World
    Stone, Nimble Ring, Avatar''s Parashu, Avenging Blade, Hydra''s Lament, Dreamer''s
    Idol, Pendulum Blade, Jotunn''s Revenge, Bragi''s Harp, Golden Blade, Dominance,
    Deathbringer, The Cosmic Horror, Bracer of The Abyss, Oath-Sworn Spear, Demon
    Blade, Musashi''s Dual Swords, Transcendence, Runeforged Hammer, Arondight, Ancient
    Signet, Chronos'' Pendant, The Executioner, Damaru.'
  slot_scores:
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.59
      pick: 0.37
      fit: 0.55
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.43
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.64
      pick: 0.18
      fit: 0.64
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.76
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.54
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.15
      fit: 0.43
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Dagger of Frenzy
  - Nimble Ring
  - Death Metal
  - Silverbranch Bow
  - Riptalon
  flex_slots:
  - Death Metal
  - Dagger of Frenzy
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
    this god: Nimble Ring, Riptalon, Death Metal, Soul Gem, Lernaean Bow, Gluttonous
    Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Spear of the Magus, Toxic Blade,
    Bragi''s Harp, Heartseeker, Hydra''s Lament, Obsidian Shard, Spear of Desolation,
    Dominance, Bracer of The Abyss, Titan''s Bane, The Crusher, Deathbringer, Demon
    Blade, Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound Book,
    Transcendence, Dreamer''s Idol, Musashi''s Dual Swords, Chronos'' Pendant, Runeforged
    Hammer, Arondight, Berserker''s Shield, Avatar''s Parashu, Bancroft''s Talon,
    Pendulum Blade, Jotunn''s Revenge.'
  slot_scores:
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.59
      pick: 0.37
      fit: 0.67
    Dagger of Frenzy:
      total: 0.5
      efficiency: 0.37
      win: 0.68
      pick: 0.08
      fit: 0.43
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.32
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.64
      pick: 0.18
      fit: 0.57
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Tyrfing
  - Dagger of Frenzy
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Silverbranch Bow
  - Soul Gem
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Spear of Desolation, Soul Gem, Hydra''s
    Lament, Death Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Arondight,
    Gem of Focus, Obsidian Shard, Lernaean Bow, Pendulum Blade, Jotunn''s Revenge,
    Tekko-Kagi, Heartseeker, Gluttonous Grimoire, Bragi''s Harp, Bracer of The Abyss,
    Totem of Death, Doom Orb, The World Stone, Ancient Signet, Titan''s Bane, Riptalon,
    The Crusher, Breastplate of Valor, Golden Blade, Dreamer''s Idol, Deathbringer,
    Dominance, Genji''s Guard, The Reaper, Toxic Blade, Transcendence, Musashi''s
    Dual Swords, Runeforged Hammer, Demon Blade, Avatar''s Parashu.'
  slot_scores:
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.59
      pick: 0.37
      fit: 0.44
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.53
      pick: 0.15
      fit: 0.55
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.59
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.64
      pick: 0.18
      fit: 0.37
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Tyrfing
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
    Underrated for this god: Jotunn''s Revenge, Death Metal, Tekko-Kagi, Lernaean
    Bow, Heartseeker, Nimble Ring, Bragi''s Harp, Golden Blade, Spear of the Magus,
    Hydra''s Lament, Titan''s Bane, Spear of Desolation, The Crusher, Dominance, Obsidian
    Shard, Deathbringer, Soul Gem, The Reaper, Riptalon, Demon Blade, Toxic Blade,
    Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s Parashu,
    Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight, Runeforged
    Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging
    Blade, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.72
      win: 0.3
      pick: 0.1
      fit: 0.49
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.59
      pick: 0.37
      fit: 0.68
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.41
      pick: 0.15
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Odysseus' Bow
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Odysseus' Bow
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
    the Magus, Hydra''s Lament, Titan''s Bane, Spear of Desolation, The Crusher, Dominance,
    Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Riptalon, Demon Blade, Toxic
    Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Avatar''s
    Parashu, Doom Orb, Pendulum Blade, Transcendence, The World Stone, Arondight,
    Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant,
    Avenging Blade, Berserker''s Shield.'
  slot_scores:
    Odysseus' Bow:
      total: 0.48
      efficiency: 0.34
      win: 0.65
      pick: 0.26
      fit: 0.35
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.72
      win: 0.3
      pick: 0.1
      fit: 0.49
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.59
      pick: 0.37
      fit: 0.68
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.41
      pick: 0.15
      fit: 0.26
  community_ordered:
  - Odysseus' Bow
  - Jotunn's Revenge
  - Tyrfing
  - Rod of Tahuti
  swaps:
  - added: Odysseus' Bow
    removed: Lernaean Bow
    reason: community 65% win over 61 matches (vs 53% on this god), taking the model's
      weakest slot from Lernaean Bow
  starter: *id001
---
