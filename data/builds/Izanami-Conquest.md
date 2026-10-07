---
type: smite-build
god: Izanami
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.57
    win_rate: 0.56
    alternates:
    - name: Tyrfing
      pick_rate: 0.36
      win_rate: 0.81
    - name: Dagger of Frenzy
      pick_rate: 0.03
      win_rate: 0.5
  - name: Dagger of Frenzy
    pick_rate: 0.28
    win_rate: 0.67
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.25
      win_rate: 0.79
    - name: Tyrfing
      pick_rate: 0.13
      win_rate: 0.5
  - name: Silverbranch Bow
    pick_rate: 0.22
    win_rate: 0.56
    alternates:
    - name: Riptalon
      pick_rate: 0.18
      win_rate: 0.77
    - name: Dominance
      pick_rate: 0.14
      win_rate: 0.6
  - name: Riptalon
    pick_rate: 0.21
    win_rate: 0.67
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.14
      win_rate: 0.7
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.33
  - name: Hastened Fatalis
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.23
      win_rate: 0.88
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.75
  - name: Deathbringer
    pick_rate: 0.17
    win_rate: 1.0
    alternates:
    - name: Manchu Bow
      pick_rate: 0.15
      win_rate: 0.5
    - name: Qin's Blade
      pick_rate: 0.09
      win_rate: 1.0
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.51
    win_rate: 0.74
  - name: Hunter's Cowl
    pick_rate: 0.2
    win_rate: 0.53
  - name: Gilded Arrow
    pick_rate: 0.17
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/izanami/
  last_verified: '2026-10-07'
  god_win_rate: 0.64
  god_matches_won: 48
  god_matches_played: 75
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Riptalon
  - Qin's Blade
  - Deathbringer
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, The Reaper, Spear of Desolation,
    Hydra''s Lament, Spear of the Magus, Heartseeker, Bragi''s Harp, Obsidian Shard,
    Golden Blade, Demon Blade, Titan''s Bane, Bracer of The Abyss, The Crusher, Musashi''s
    Dual Swords, Toxic Blade, Doom Orb, Chronos'' Pendant, Arondight, The World Stone,
    Ancient Signet, Blood-Bound Book, Transcendence, Pendulum Blade, Damaru, Rage,
    Dreamer''s Idol, Runeforged Hammer, Avatar''s Parashu, Bancroft''s Talon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.63
      efficiency: 0.48
      win: 0.81
      pick: 0.36
      fit: 0.55
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.67
      pick: 0.35
      fit: 0.53
    Qin's Blade:
      total: 0.67
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.5
    Deathbringer:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.52
      fit: 0.39
  community_ordered:
  - Tyrfing
  - Riptalon
  - Qin's Blade
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Qin's Blade
  - Deathbringer
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Hydra's Lament
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
    of Tahuti, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire,
    Spear of Desolation, Spear of the Magus, Hydra''s Lament, Obsidian Shard, Bragi''s
    Harp, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Doom Orb, Ancient Signet,
    The World Stone, Bracer of The Abyss, Chronos'' Pendant, Bancroft''s Talon, Titan''s
    Bane, Blood-Bound Book, The Crusher, Golden Blade, Dreamer''s Idol, Transcendence,
    Arondight, Gem of Focus, Book of Thoth, Musashi''s Dual Swords, Polynomicon, Demon
    Blade, Runeforged Hammer, Rod of Asclepius, Soul Reaver, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.81
      pick: 0.36
      fit: 0.48
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.64
      pick: 0.0
      fit: 0.42
    Qin's Blade:
      total: 0.65
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.41
    Deathbringer:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.52
      fit: 0.34
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.64
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Tyrfing
  - Qin's Blade
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Qin's Blade
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Death Metal
  - Demon Blade
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem,
    Gluttonous Grimoire, Lernaean Bow, The Reaper, Tekko-Kagi, Spear of Desolation,
    Hydra''s Lament, Spear of the Magus, Heartseeker, Obsidian Shard, Bragi''s Harp,
    Demon Blade, Golden Blade, Musashi''s Dual Swords, Titan''s Bane, The Crusher,
    Bracer of The Abyss, Toxic Blade, Doom Orb, Chronos'' Pendant, Arondight, Damaru,
    Rage, The World Stone, Ancient Signet, Blood-Bound Book, Transcendence, Dreamer''s
    Idol, Pendulum Blade, Runeforged Hammer, Avatar''s Parashu, Bancroft''s Talon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.63
      efficiency: 0.48
      win: 0.81
      pick: 0.36
      fit: 0.52
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.46
    Qin's Blade:
      total: 0.67
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.48
    Demon Blade:
      total: 0.51
      efficiency: 0.38
      win: 0.64
      pick: 0.0
      fit: 0.63
    Deathbringer:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.52
      fit: 0.41
  community_ordered:
  - Tyrfing
  - Qin's Blade
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - Rod of Tahuti
  - Deathbringer
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Jotunn''s Revenge, Soul Gem, Nimble Ring, Death Metal, Gluttonous
    Grimoire, Spear of Desolation, Spear of the Magus, Obsidian Shard, The Reaper,
    Tekko-Kagi, Hydra''s Lament, Heartseeker, Lernaean Bow, Bragi''s Harp, Doom Orb,
    Chronos'' Pendant, The World Stone, Titan''s Bane, The Crusher, Bracer of The
    Abyss, Dreamer''s Idol, Ancient Signet, Blood-Bound Book, Pendulum Blade, Golden
    Blade, Arondight, Gem of Focus, Toxic Blade, Bancroft''s Talon, Avatar''s Parashu,
    Musashi''s Dual Swords, The Cosmic Horror, Demon Blade, Transcendence, Runeforged
    Hammer, Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.81
      pick: 0.36
      fit: 0.45
    Qin's Blade:
      total: 0.66
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.64
      pick: 0.0
      fit: 0.33
    Deathbringer:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.52
      fit: 0.3
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Tyrfing
  - Qin's Blade
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Deathbringer
  - Amanita Charm
  flex_slots:
  - Riptalon
  - Berserker's Shield
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
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Berserker''s Shield, Jotunn''s
    Revenge, The Reaper, Shield of the Phoenix, Gluttonous Grimoire, Rod of Asclepius,
    Nimble Ring, Kinetic Cuirass, Death Metal, Genji''s Guard, Freya''s Tears, Breastplate
    of Valor, Runeforged Hammer, Blood-Bound Book, Golden Blade, Yogi''s Necklace,
    Ethereal Staff, Shifter''s Shield, Bancroft''s Talon, Shield Splitter, Pharaoh''s
    Curse, Lernaean Bow, Chandra''s Grace, Phoenix Feather, Shogun''s Ofuda, Spear
    of the Magus, Hydra''s Lament, Spear of Desolation, Eye of the Storm, Lifebinder,
    Helm of Radiance, Erosion, Daybreak Gavel, Eye of Providence, Tekko-Kagi, Obsidian
    Shard.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.61
      efficiency: 0.48
      win: 0.81
      pick: 0.36
      fit: 0.41
    Qin's Blade:
      total: 0.65
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.4
    Riptalon:
      total: 0.6
      efficiency: 0.51
      win: 0.67
      pick: 0.35
      fit: 0.66
    Deathbringer:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.52
      fit: 0.26
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Riptalon
  - Qin's Blade
  - Deathbringer
  flex_slots:
  - Riptalon
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Soul Gem, Nimble Ring, Gluttonous
    Grimoire, Death Metal, The Reaper, Tekko-Kagi, Spear of Desolation, Spear of the
    Magus, Heartseeker, Obsidian Shard, Titan''s Bane, Lernaean Bow, The Crusher,
    Hydra''s Lament, Doom Orb, Toxic Blade, Avenging Blade, The World Stone, Dreamer''s
    Idol, Bragi''s Harp, Pendulum Blade, Avatar''s Parashu, Golden Blade, Bracer of
    The Abyss, Demon Blade, Musashi''s Dual Swords, Chronos'' Pendant, Ancient Signet,
    Arondight, The Cosmic Horror, Blood-Bound Book, Oath-Sworn Spear, Transcendence,
    Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.81
      pick: 0.36
      fit: 0.47
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.67
      pick: 0.35
      fit: 0.62
    Qin's Blade:
      total: 0.66
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.44
    Deathbringer:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.52
      fit: 0.32
  community_ordered:
  - Tyrfing
  - Riptalon
  - Qin's Blade
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Riptalon
  - Qin's Blade
  - Deathbringer
  flex_slots:
  - Riptalon
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, The Reaper, Golden Blade, Spear
    of Desolation, Hydra''s Lament, Spear of the Magus, Heartseeker, Obsidian Shard,
    Bragi''s Harp, Toxic Blade, Bracer of The Abyss, Titan''s Bane, The Crusher, Demon
    Blade, Chronos'' Pendant, Musashi''s Dual Swords, Doom Orb, Ancient Signet, Arondight,
    The World Stone, Blood-Bound Book, Transcendence, Dreamer''s Idol, Runeforged
    Hammer, Sun Beam Bow, Bancroft''s Talon, Pendulum Blade, Berserker''s Shield,
    Damaru.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.32
    Tyrfing:
      total: 0.64
      efficiency: 0.48
      win: 0.81
      pick: 0.36
      fit: 0.59
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.35
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.67
      pick: 0.35
      fit: 0.57
    Qin's Blade:
      total: 0.68
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.57
    Deathbringer:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.52
      fit: 0.31
  community_ordered:
  - Tyrfing
  - Riptalon
  - Qin's Blade
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - Spear of Desolation
  - Deathbringer
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Soul Gem, Nimble Ring, Spear of Desolation, Death Metal, Hydra''s Lament, Gluttonous
    Grimoire, Chronos'' Pendant, Spear of the Magus, Lernaean Bow, Obsidian Shard,
    The Reaper, Arondight, Gem of Focus, Tekko-Kagi, Bragi''s Harp, Heartseeker, Bracer
    of The Abyss, Pendulum Blade, Doom Orb, Ancient Signet, Golden Blade, Blood-Bound
    Book, The World Stone, Titan''s Bane, Totem of Death, The Crusher, Dreamer''s
    Idol, Breastplate of Valor, Toxic Blade, Bancroft''s Talon, Musashi''s Dual Swords,
    Demon Blade, Genji''s Guard, Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.61
      efficiency: 0.48
      win: 0.81
      pick: 0.36
      fit: 0.42
    Qin's Blade:
      total: 0.66
      efficiency: 0.37
      win: 1.0
      pick: 0.28
      fit: 0.43
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.48
    Deathbringer:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.52
      fit: 0.27
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Tyrfing
  - Qin's Blade
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Lernaean Bow
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death
    Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, The Reaper, Spear
    of Desolation, Hydra''s Lament, Spear of the Magus, Heartseeker, Bragi''s Harp,
    Obsidian Shard, Golden Blade, Demon Blade, Titan''s Bane, Bracer of The Abyss,
    The Crusher, Musashi''s Dual Swords, Toxic Blade, Doom Orb, Chronos'' Pendant,
    Arondight, The World Stone, Ancient Signet, Blood-Bound Book, Transcendence, Pendulum
    Blade, Damaru, Rage, Dreamer''s Idol, Runeforged Hammer, Avatar''s Parashu, Bancroft''s
    Talon.'
  slot_scores:
    Lernaean Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.39
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.37
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.64
      pick: 0.0
      fit: 0.19
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.48
  starter: *id001
---
