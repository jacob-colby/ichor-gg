---
type: smite-build
god: Cernunnos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Strife
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.56
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.83
    win_rate: 0.62
    alternates:
    - name: Tyrfing
      pick_rate: 0.07
      win_rate: 0.5
    - name: Avenging Blade
      pick_rate: 0.02
      win_rate: 1.0
  - name: Dagger of Frenzy
    pick_rate: 0.35
    win_rate: 0.6
    alternates:
    - name: Tyrfing
      pick_rate: 0.14
      win_rate: 0.63
    - name: Vital Amplifier
      pick_rate: 0.12
      win_rate: 0.69
  - name: Riptalon
    pick_rate: 0.2
    win_rate: 0.68
    alternates:
    - name: Dominance
      pick_rate: 0.18
      win_rate: 0.65
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.67
  - name: Dominance
    pick_rate: 0.17
    win_rate: 0.61
    alternates:
    - name: Riptalon
      pick_rate: 0.18
      win_rate: 0.47
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.82
  - name: Silverbranch Bow
    pick_rate: 0.13
    win_rate: 0.62
    alternates:
    - name: Riptalon
      pick_rate: 0.19
      win_rate: 0.63
    - name: The Executioner
      pick_rate: 0.09
      win_rate: 0.44
  - name: Hunter's Bow
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Dominance
      pick_rate: 0.11
      win_rate: 0.89
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.63
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.4
    win_rate: 0.67
  - name: Sharpshooter's Arrow
    pick_rate: 0.22
    win_rate: 0.52
  - name: Leather Cowl
    pick_rate: 0.14
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/cernunnos/
  last_verified: '2026-11-06'
  god_win_rate: 0.6106194690265486
  god_matches_won: 69
  god_matches_played: 113
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Soul Gem, Jotunn''s Revenge, Spear of Desolation,
    Nimble Ring, Gluttonous Grimoire, The Reaper, Bragi''s Harp, Blood-Bound Book,
    Tekko-Kagi, Obsidian Shard, Hydra''s Lament, Spear of the Magus, The Crusher,
    Ancient Signet, Bracer of The Abyss, Lernaean Bow, Heartseeker, Dreamer''s Idol,
    Polynomicon, Chronos'' Pendant, Titan''s Bane, Doom Orb, Arondight, Golden Blade,
    The World Stone, Bancroft''s Talon, Rage, Toxic Blade, Soul Reaver, Gem of Focus,
    Heartwood Charm, Demon Blade, Deathbringer, Qin''s Blade, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.63
      efficiency: 0.42
      win: 1.0
      pick: 0.02
      fit: 0.25
    Berserker's Shield:
      total: 0.57
      efficiency: 0.46
      win: 0.82
      pick: 0.17
      fit: 0.2
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.38
    Death Metal:
      total: 0.58
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.29
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Transcendence
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
    of Tahuti, Death Metal, Jotunn''s Revenge, Soul Gem, Spear of Desolation, Nimble
    Ring, Bragi''s Harp, Hydra''s Lament, Gluttonous Grimoire, The Reaper, Ancient
    Signet, Blood-Bound Book, Polynomicon, Obsidian Shard, Heartseeker, Tekko-Kagi,
    Spear of the Magus, Chronos'' Pendant, The Crusher, Bracer of The Abyss, Lernaean
    Bow, Dreamer''s Idol, Doom Orb, Bancroft''s Talon, Heartwood Charm, Soul Reaver,
    The World Stone, Titan''s Bane, Arondight, Gem of Focus, Golden Blade, Rage, Transcendence,
    Deathbringer, Avatar''s Parashu, Book of Thoth, Demon Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.64
      efficiency: 0.42
      win: 1.0
      pick: 0.02
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.63
      pick: 0.0
      fit: 0.24
    Death Metal:
      total: 0.58
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Avenging Blade
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Avenging Blade
  - Rage
  - Death Metal
  - Deathbringer
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Rage
  - Deathbringer
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
    this god: Rod of Tahuti, Death Metal, Soul Gem, Jotunn''s Revenge, Spear of Desolation,
    Nimble Ring, Gluttonous Grimoire, The Reaper, Bragi''s Harp, Blood-Bound Book,
    Obsidian Shard, Tekko-Kagi, Spear of the Magus, Hydra''s Lament, Ancient Signet,
    Bracer of The Abyss, The Crusher, Dreamer''s Idol, Polynomicon, Chronos'' Pendant,
    Heartseeker, Lernaean Bow, Titan''s Bane, Doom Orb, The World Stone, Bancroft''s
    Talon, Rage, Arondight, Golden Blade, Soul Reaver, Gem of Focus, Heartwood Charm,
    Toxic Blade, Deathbringer, Demon Blade, Qin''s Blade, The Cosmic Horror.'
  slot_scores:
    Avenging Blade:
      total: 0.63
      efficiency: 0.42
      win: 1.0
      pick: 0.02
      fit: 0.22
    Rage:
      total: 0.5
      efficiency: 0.46
      win: 0.63
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.58
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.51
    Deathbringer:
      total: 0.49
      efficiency: 0.44
      win: 0.63
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.29
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Avenging Blade
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Soul Gem, Jotunn''s Revenge, Death Metal, Spear of Desolation,
    Gluttonous Grimoire, The Reaper, Nimble Ring, Obsidian Shard, Hydra''s Lament,
    Tekko-Kagi, Bragi''s Harp, Spear of the Magus, Blood-Bound Book, The Crusher,
    Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Ancient Signet, Titan''s Bane,
    Polynomicon, Bracer of The Abyss, Doom Orb, Lernaean Bow, Arondight, The World
    Stone, Gem of Focus, Heartwood Charm, Toxic Blade, Bancroft''s Talon, Golden Blade,
    Avatar''s Parashu, Soul Reaver, Rage, Pendulum Blade, The Cosmic Horror, Deathbringer.'
  slot_scores:
    Avenging Blade:
      total: 0.63
      efficiency: 0.42
      win: 1.0
      pick: 0.02
      fit: 0.23
    Berserker's Shield:
      total: 0.57
      efficiency: 0.46
      win: 0.82
      pick: 0.17
      fit: 0.17
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.33
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Death Metal
  - Rod of Tahuti
  - Amanita Charm
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, The Reaper, Shield of the Phoenix,
    Blood-Bound Book, Gluttonous Grimoire, Death Metal, Genji''s Guard, Kinetic Cuirass,
    Jotunn''s Revenge, Ethereal Staff, Yogi''s Necklace, Phoenix Feather, Bancroft''s
    Talon, Spear of Desolation, Freya''s Tears, Shield Splitter, Breastplate of Valor,
    Nimble Ring, Chandra''s Grace, Runeforged Hammer, Golden Blade, Oni Hunter''s
    Garb, Bragi''s Harp, Obsidian Shard, Hydra''s Lament, Helm of Radiance, Sphere
    of Negation, Ancient Signet, Bloodforge, Regrowth Striders, Draconic Scale, Spear
    of the Magus, Polynomicon, The Crusher, Tekko-Kagi, Midgardian Mail.'
  slot_scores:
    Avenging Blade:
      total: 0.66
      efficiency: 0.47
      win: 1.0
      pick: 0.02
      fit: 0.32
    Berserker's Shield:
      total: 0.68
      efficiency: 0.72
      win: 0.82
      pick: 0.17
      fit: 0.34
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.21
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, Rod of Tahuti, Jotunn''s Revenge, Soul Gem, Death
    Metal, Spear of Desolation, Gluttonous Grimoire, The Reaper, Obsidian Shard, Tekko-Kagi,
    Spear of the Magus, Nimble Ring, The Crusher, Heartseeker, Dreamer''s Idol, Bragi''s
    Harp, Blood-Bound Book, Titan''s Bane, Hydra''s Lament, Doom Orb, Ancient Signet,
    The World Stone, Polynomicon, Bracer of The Abyss, Lernaean Bow, Chronos'' Pendant,
    Toxic Blade, Avatar''s Parashu, The Cosmic Horror, Arondight, Bancroft''s Talon,
    Golden Blade, Soul Reaver, Pendulum Blade, Rage, Gem of Focus, Heartwood Charm.'
  slot_scores:
    Avenging Blade:
      total: 0.68
      efficiency: 0.42
      win: 1.0
      pick: 0.02
      fit: 0.53
    Berserker's Shield:
      total: 0.57
      efficiency: 0.46
      win: 0.82
      pick: 0.17
      fit: 0.17
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.47
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.39
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Tyrfing
  - Death Metal
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Soul Gem, Jotunn''s Revenge, Spear of Desolation,
    Nimble Ring, Gluttonous Grimoire, Bragi''s Harp, The Reaper, Blood-Bound Book,
    Obsidian Shard, Tekko-Kagi, Ancient Signet, Hydra''s Lament, Spear of the Magus,
    Bracer of The Abyss, Polynomicon, The Crusher, Lernaean Bow, Chronos'' Pendant,
    Dreamer''s Idol, Golden Blade, Heartseeker, Toxic Blade, Qin''s Blade, Titan''s
    Bane, Doom Orb, Bancroft''s Talon, Arondight, The World Stone, Soul Reaver, Gem
    of Focus, Heartwood Charm, Rage, Demon Blade, Deathbringer.'
  slot_scores:
    Avenging Blade:
      total: 0.63
      efficiency: 0.42
      win: 1.0
      pick: 0.02
      fit: 0.21
    Berserker's Shield:
      total: 0.57
      efficiency: 0.46
      win: 0.82
      pick: 0.17
      fit: 0.2
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.54
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.41
    Riptalon:
      total: 0.56
      efficiency: 0.45
      win: 0.68
      pick: 0.31
      fit: 0.52
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.25
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Berserker's Shield
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Jotunn''s
    Revenge, Spear of Desolation, Death Metal, Hydra''s Lament, Chronos'' Pendant,
    Nimble Ring, Gluttonous Grimoire, The Reaper, Arondight, Blood-Bound Book, Obsidian
    Shard, Bragi''s Harp, Gem of Focus, Heartwood Charm, Tekko-Kagi, Ancient Signet,
    Spear of the Magus, The Crusher, Bracer of The Abyss, Polynomicon, Lernaean Bow,
    Heartseeker, Dreamer''s Idol, Damaru, Genji''s Guard, Titan''s Bane, Totem of
    Death, Pendulum Blade, Doom Orb, Toxic Blade, Bancroft''s Talon, The World Stone,
    Golden Blade, Soul Reaver, Qin''s Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.62
      efficiency: 0.42
      win: 1.0
      pick: 0.02
      fit: 0.18
    Berserker's Shield:
      total: 0.57
      efficiency: 0.46
      win: 0.82
      pick: 0.17
      fit: 0.18
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.21
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Nimble Ring
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Death Metal, Soul Gem, Jotunn''s Revenge,
    Spear of Desolation, Nimble Ring, Gluttonous Grimoire, The Reaper, Bragi''s Harp,
    Blood-Bound Book, Tekko-Kagi, Obsidian Shard, Hydra''s Lament, Spear of the Magus,
    The Crusher, Ancient Signet, Bracer of The Abyss, Lernaean Bow, Heartseeker, Dreamer''s
    Idol, Polynomicon, Chronos'' Pendant, Titan''s Bane, Doom Orb, Arondight, Golden
    Blade, The World Stone, Bancroft''s Talon, Rage, Toxic Blade, Soul Reaver, Gem
    of Focus, Heartwood Charm, Demon Blade, Deathbringer, Qin''s Blade, Avatar''s
    Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.38
    Death Metal:
      total: 0.58
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.5
    Nimble Ring:
      total: 0.54
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.29
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Death Metal
  - The Reaper
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - The Reaper
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Avenging Blade, Rod of Tahuti, Soul Gem, Death Metal, The Reaper, Gluttonous
    Grimoire, Jotunn''s Revenge, Blood-Bound Book, Spear of Desolation, Nimble Ring,
    Bancroft''s Talon, Ethereal Staff, Obsidian Shard, Runeforged Hammer, Hydra''s
    Lament, Bragi''s Harp, Yogi''s Necklace, Golden Blade, Spear of the Magus, Ancient
    Signet, The Crusher, Heartseeker, Polynomicon, Tekko-Kagi, Bloodforge, Dreamer''s
    Idol, Chronos'' Pendant, Chandra''s Grace, Titan''s Bane, Jade Scepter, Bracer
    of The Abyss, Toxic Blade, Lernaean Bow, Doom Orb, Arondight, Triton''s Conch,
    The World Stone.'
  slot_scores:
    Avenging Blade:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.02
      fit: 0.33
    Berserker's Shield:
      total: 0.59
      efficiency: 0.52
      win: 0.82
      pick: 0.17
      fit: 0.2
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.47
    The Reaper:
      total: 0.57
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.27
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: mana-stack
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Avenging
    Blade, Rod of Tahuti, Soul Gem, Death Metal, Jotunn''s Revenge, The Reaper, Blood-Bound
    Book, Gluttonous Grimoire, Spear of Desolation, Bancroft''s Talon, Hydra''s Lament,
    Nimble Ring, Ancient Signet, Ethereal Staff, Yogi''s Necklace, Bragi''s Harp,
    Polynomicon, Obsidian Shard, Runeforged Hammer, Heartseeker, Spear of the Magus,
    Chronos'' Pendant, The Crusher, Golden Blade, Chandra''s Grace, Bloodforge, Dreamer''s
    Idol, Doom Orb, Tekko-Kagi, Soul Reaver, Jade Scepter, Heartwood Charm, Titan''s
    Bane, The World Stone, Bracer of The Abyss, Arondight, Lernaean Bow, Triton''s
    Conch.'
  slot_scores:
    Avenging Blade:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.02
      fit: 0.34
    Berserker's Shield:
      total: 0.58
      efficiency: 0.52
      win: 0.82
      pick: 0.17
      fit: 0.17
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.63
      pick: 0.0
      fit: 0.23
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.33
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.75
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: crit
  slot_order:
  - Avenging Blade
  - Rage
  - Berserker's Shield
  - Death Metal
  - Deathbringer
  - Soul Gem
  flex_slots:
  - Rage
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Soul Gem, Death Metal, Gluttonous Grimoire, The Reaper,
    Blood-Bound Book, Jotunn''s Revenge, Spear of Desolation, Nimble Ring, Bancroft''s
    Talon, Ethereal Staff, Bragi''s Harp, Obsidian Shard, Golden Blade, Yogi''s Necklace,
    Runeforged Hammer, Ancient Signet, Hydra''s Lament, Spear of the Magus, Tekko-Kagi,
    Polynomicon, The Crusher, Bracer of The Abyss, Chronos'' Pendant, Dreamer''s Idol,
    Toxic Blade, Heartseeker, Bloodforge, Chandra''s Grace, Lernaean Bow, Jade Scepter,
    Titan''s Bane, Doom Orb, Amanita Charm, The World Stone, Arondight.'
  slot_scores:
    Avenging Blade:
      total: 0.66
      efficiency: 0.47
      win: 1.0
      pick: 0.02
      fit: 0.29
    Rage:
      total: 0.49
      efficiency: 0.46
      win: 0.63
      pick: 0.0
      fit: 0.31
    Berserker's Shield:
      total: 0.6
      efficiency: 0.52
      win: 0.82
      pick: 0.17
      fit: 0.25
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.44
    Deathbringer:
      total: 0.49
      efficiency: 0.44
      win: 0.63
      pick: 0.0
      fit: 0.31
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: burst
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Soul Gem, Jotunn''s Revenge, The Reaper, Gluttonous Grimoire,
    Death Metal, Blood-Bound Book, Spear of Desolation, Obsidian Shard, Bancroft''s
    Talon, Nimble Ring, Hydra''s Lament, Spear of the Magus, Ethereal Staff, The Crusher,
    Yogi''s Necklace, Runeforged Hammer, Heartseeker, Dreamer''s Idol, Chronos'' Pendant,
    Ancient Signet, Bragi''s Harp, Tekko-Kagi, Chandra''s Grace, Titan''s Bane, Polynomicon,
    Golden Blade, Doom Orb, Bloodforge, Toxic Blade, Arondight, The World Stone, Jade
    Scepter, Bracer of The Abyss, Gem of Focus, Lernaean Bow, Heartwood Charm.'
  slot_scores:
    Avenging Blade:
      total: 0.66
      efficiency: 0.47
      win: 1.0
      pick: 0.02
      fit: 0.3
    Berserker's Shield:
      total: 0.59
      efficiency: 0.52
      win: 0.82
      pick: 0.17
      fit: 0.17
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.41
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.31
    Soul Gem:
      total: 0.61
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.84
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Death Metal
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Amanita Charm, Soul Gem, Rod of Tahuti, The Reaper, Blood-Bound Book,
    Shield of the Phoenix, Gluttonous Grimoire, Death Metal, Kinetic Cuirass, Genji''s
    Guard, Jotunn''s Revenge, Ethereal Staff, Bancroft''s Talon, Yogi''s Necklace,
    Phoenix Feather, Spear of Desolation, Freya''s Tears, Shield Splitter, Breastplate
    of Valor, Chandra''s Grace, Nimble Ring, Runeforged Hammer, Oni Hunter''s Garb,
    Bloodforge, Obsidian Shard, Hydra''s Lament, Helm of Radiance, Sphere of Negation,
    Ancient Signet, Regrowth Striders, Golden Blade, Draconic Scale, Spear of the
    Magus, Bragi''s Harp, Polynomicon, The Crusher, Midgardian Mail, Erosion.'
  slot_scores:
    Avenging Blade:
      total: 0.66
      efficiency: 0.47
      win: 1.0
      pick: 0.02
      fit: 0.32
    Berserker's Shield:
      total: 0.67
      efficiency: 0.72
      win: 0.82
      pick: 0.17
      fit: 0.29
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.21
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, Rod of Tahuti, Soul Gem, The Reaper, Gluttonous
    Grimoire, Jotunn''s Revenge, Death Metal, Spear of Desolation, Blood-Bound Book,
    Obsidian Shard, Spear of the Magus, The Crusher, Bancroft''s Talon, Nimble Ring,
    Heartseeker, Dreamer''s Idol, Tekko-Kagi, Ethereal Staff, Titan''s Bane, Runeforged
    Hammer, Yogi''s Necklace, Hydra''s Lament, Doom Orb, Ancient Signet, Toxic Blade,
    Bragi''s Harp, Golden Blade, The World Stone, Polynomicon, Chronos'' Pendant,
    Bloodforge, Chandra''s Grace, Jade Scepter, Avatar''s Parashu, Bracer of The Abyss,
    Lernaean Bow, Arondight.'
  slot_scores:
    Avenging Blade:
      total: 0.71
      efficiency: 0.47
      win: 1.0
      pick: 0.02
      fit: 0.6
    Berserker's Shield:
      total: 0.59
      efficiency: 0.52
      win: 0.82
      pick: 0.17
      fit: 0.18
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.41
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.37
    Soul Gem:
      total: 0.61
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.84
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: attack-speed
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Soul Gem, Death Metal, Gluttonous Grimoire, Jotunn''s
    Revenge, Blood-Bound Book, The Reaper, Spear of Desolation, Nimble Ring, Golden
    Blade, Bragi''s Harp, Ethereal Staff, Bancroft''s Talon, Obsidian Shard, Toxic
    Blade, Yogi''s Necklace, Ancient Signet, Runeforged Hammer, Hydra''s Lament, Tekko-Kagi,
    Spear of the Magus, Bracer of The Abyss, Polynomicon, The Crusher, Chronos'' Pendant,
    Lernaean Bow, Dreamer''s Idol, Chandra''s Grace, Heartseeker, Jade Scepter, Bloodforge,
    Titan''s Bane, Qin''s Blade, Doom Orb, Amanita Charm, Arondight.'
  slot_scores:
    Avenging Blade:
      total: 0.66
      efficiency: 0.47
      win: 1.0
      pick: 0.02
      fit: 0.27
    Berserker's Shield:
      total: 0.6
      efficiency: 0.52
      win: 0.82
      pick: 0.17
      fit: 0.26
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.51
    Riptalon:
      total: 0.58
      efficiency: 0.45
      win: 0.68
      pick: 0.31
      fit: 0.69
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.23
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: cooldown
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Rod of Tahuti, Jotunn''s
    Revenge, Spear of Desolation, The Reaper, Gluttonous Grimoire, Blood-Bound Book,
    Death Metal, Hydra''s Lament, Chandra''s Grace, Chronos'' Pendant, Nimble Ring,
    Bancroft''s Talon, Yogi''s Necklace, Arondight, Ethereal Staff, Obsidian Shard,
    Shield of the Phoenix, Runeforged Hammer, Gem of Focus, Heartwood Charm, Ancient
    Signet, Spear of the Magus, Golden Blade, The Crusher, Polynomicon, Bragi''s Harp,
    Heartseeker, Dreamer''s Idol, Bloodforge, Damaru, Genji''s Guard, Tekko-Kagi,
    Toxic Blade, Eye of Erebus, Titan''s Bane, Amanita Charm, Jade Scepter.'
  slot_scores:
    Avenging Blade:
      total: 0.65
      efficiency: 0.47
      win: 1.0
      pick: 0.02
      fit: 0.26
    Berserker's Shield:
      total: 0.59
      efficiency: 0.52
      win: 0.82
      pick: 0.17
      fit: 0.18
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.2
    Soul Gem:
      total: 0.62
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Avenging Blade
  - Berserker's Shield
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - The Reaper
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Soul Gem, Death Metal, The Reaper, Gluttonous
    Grimoire, Jotunn''s Revenge, Blood-Bound Book, Spear of Desolation, Nimble Ring,
    Bancroft''s Talon, Ethereal Staff, Obsidian Shard, Runeforged Hammer, Hydra''s
    Lament, Bragi''s Harp, Yogi''s Necklace, Golden Blade, Spear of the Magus, Ancient
    Signet, The Crusher, Heartseeker, Polynomicon, Tekko-Kagi, Bloodforge, Dreamer''s
    Idol, Chronos'' Pendant, Chandra''s Grace, Titan''s Bane, Jade Scepter, Bracer
    of The Abyss, Toxic Blade, Lernaean Bow, Doom Orb, Arondight, Avenging Blade,
    Triton''s Conch, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.47
    The Reaper:
      total: 0.57
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.63
      pick: 0.0
      fit: 0.27
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of Strife
---
