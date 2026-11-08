---
type: smite-build
god: Aladdin
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Genie's Lamp
    pick_rate: 0.73
    win_rate: 0.64
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.61
    - name: Jotunn's Revenge
      pick_rate: 0.06
      win_rate: 0.47
  - name: Spear of Desolation
    pick_rate: 0.3
    win_rate: 0.69
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.16
      win_rate: 0.59
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.59
  - name: Polynomicon
    pick_rate: 0.15
    win_rate: 0.76
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.61
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.52
  - name: Rod of Tahuti
    pick_rate: 0.21
    win_rate: 0.62
    alternates:
    - name: Polynomicon
      pick_rate: 0.13
      win_rate: 0.5
    - name: Soul Gem
      pick_rate: 0.11
      win_rate: 0.79
  - name: Heartseeker
    pick_rate: 0.15
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.33
      win_rate: 0.68
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.69
  - name: Obsidian Shard
    pick_rate: 0.2
    win_rate: 0.72
    alternates:
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.69
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.69
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.55
    win_rate: 0.67
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 0.49
  - name: Bumba's Hammer
    pick_rate: 0.14
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/aladdin/
  last_verified: '2026-11-08'
  god_win_rate: 0.6228813559322034
  god_matches_won: 147
  god_matches_played: 236
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Hydra''s Lament, Titan''s Bane, The Reaper, Arondight,
    Pendulum Blade, Death Metal, Avatar''s Parashu, Tyrfing, Spear of the Magus, Tekko-Kagi,
    Dreamer''s Idol, Gluttonous Grimoire, Chronos'' Pendant, Bragi''s Harp, Doom Orb,
    The World Stone, Ancient Signet, Transcendence, Runeforged Hammer, Gem of Focus,
    Heartwood Charm, Dominance, The Cosmic Horror, Shield Splitter, Eye of the Storm,
    Avenging Blade, Blood-Bound Book, Damaru, Genji''s Guard, Triton''s Conch, Golden
    Blade, Soul Reaver, Lernaean Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.65
      win: 0.59
      pick: 0.22
      fit: 0.9
    Transcendence:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.0
      fit: 0.38
    Spear of Desolation:
      total: 0.64
      efficiency: 0.6
      win: 0.69
      pick: 0.41
      fit: 0.62
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.62
      pick: 0.35
      fit: 0.42
    Obsidian Shard:
      total: 0.62
      efficiency: 0.53
      win: 0.72
      pick: 0.62
      fit: 0.52
    Soul Gem:
      total: 0.66
      efficiency: 0.53
      win: 0.79
      pick: 0.18
      fit: 0.72
  community_ordered:
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Transcendence
  - Spear of Desolation
  - Polynomicon
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Polynomicon
  - Transcendence
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Death Metal, Ancient Signet, Spear of the Magus, Doom Orb, The Crusher,
    Chronos'' Pendant, Dreamer''s Idol, The World Stone, Heartwood Charm, Bragi''s
    Harp, Gluttonous Grimoire, Titan''s Bane, The Reaper, Arondight, Soul Reaver,
    Gem of Focus, Tyrfing, Blood-Bound Book, Transcendence, Avatar''s Parashu, Pendulum
    Blade, The Cosmic Horror, Dominance, Bancroft''s Talon, Totem of Death, Triton''s
    Conch, Tekko-Kagi, Runeforged Hammer, Genji''s Guard, Jade Scepter, Divine Ruin,
    Shield Splitter.'
  slot_scores:
    Transcendence:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.63
      efficiency: 0.6
      win: 0.69
      pick: 0.41
      fit: 0.61
    Polynomicon:
      total: 0.62
      efficiency: 0.56
      win: 0.76
      pick: 0.23
      fit: 0.49
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.82
      win: 0.62
      pick: 0.35
      fit: 0.57
    Obsidian Shard:
      total: 0.63
      efficiency: 0.53
      win: 0.72
      pick: 0.62
      fit: 0.57
    Soul Gem:
      total: 0.66
      efficiency: 0.53
      win: 0.79
      pick: 0.18
      fit: 0.71
  community_ordered:
  - Spear of Desolation
  - Polynomicon
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Polynomicon
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Polynomicon
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Spear of the Magus, The Crusher, Hydra''s Lament, Dreamer''s Idol, Gluttonous
    Grimoire, Titan''s Bane, The Reaper, Death Metal, Chronos'' Pendant, Doom Orb,
    The World Stone, Pendulum Blade, Arondight, Ancient Signet, Gem of Focus, Avatar''s
    Parashu, Heartwood Charm, The Cosmic Horror, Bragi''s Harp, Tyrfing, Tekko-Kagi,
    Blood-Bound Book, Totem of Death, Soul Reaver, Damaru, Genji''s Guard, Transcendence,
    Runeforged Hammer, Triton''s Conch, Dominance, Bancroft''s Talon, Jade Scepter,
    Divine Ruin.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.65
      win: 0.59
      pick: 0.22
      fit: 0.78
    Spear of Desolation:
      total: 0.66
      efficiency: 0.6
      win: 0.69
      pick: 0.41
      fit: 0.78
    Polynomicon:
      total: 0.6
      efficiency: 0.56
      win: 0.76
      pick: 0.23
      fit: 0.32
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.82
      win: 0.62
      pick: 0.35
      fit: 0.56
    Obsidian Shard:
      total: 0.64
      efficiency: 0.53
      win: 0.72
      pick: 0.62
      fit: 0.66
    Soul Gem:
      total: 0.68
      efficiency: 0.53
      win: 0.79
      pick: 0.18
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - Spear of Desolation
  - Polynomicon
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Genji''s Guard,
    Berserker''s Shield, Shield Splitter, The Reaper, Phoenix Feather, Freya''s Tears,
    Yogi''s Necklace, Runeforged Hammer, Ethereal Staff, Draconic Scale, Breastplate
    of Valor, Chandra''s Grace, Oni Hunter''s Garb, Gluttonous Grimoire, Erosion,
    Eye of Providence, Hydra''s Lament, Shifter''s Shield, Blood-Bound Book, Regrowth
    Striders, Midgardian Mail, The Crusher, Leviathan''s Hide, Glorious Pridwen, Hide
    of the Nemean Lion, Screeching Gargoyle, Avenging Blade, Wyrmskin Hide, Stone
    of Binding, Ancile, Helm of Radiance, Titan''s Bane, Sphere of Negation.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.69
      pick: 0.41
      fit: 0.31
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.62
      pick: 0.35
      fit: 0.21
    Amanita Charm:
      total: 0.66
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.8
    Obsidian Shard:
      total: 0.59
      efficiency: 0.53
      win: 0.72
      pick: 0.62
      fit: 0.31
    Soul Gem:
      total: 0.66
      efficiency: 0.53
      win: 0.79
      pick: 0.18
      fit: 0.71
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Heartseeker
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    for this god: The Crusher, Titan''s Bane, The Reaper, Spear of the Magus, Avatar''s
    Parashu, Dreamer''s Idol, Pendulum Blade, Gluttonous Grimoire, Doom Orb, Tekko-Kagi,
    Hydra''s Lament, The World Stone, The Cosmic Horror, Death Metal, Avenging Blade,
    Arondight, Tyrfing, Chronos'' Pendant, Silverbranch Bow, Ancient Signet, Toxic
    Blade, Bragi''s Harp, Oath-Sworn Spear, Transcendence, Runeforged Hammer, Gem
    of Focus, Heartwood Charm, Blood-Bound Book, Riptalon, Dominance, Screeching Gargoyle,
    Soul Reaver, Shield Splitter, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.65
      win: 0.59
      pick: 0.22
      fit: 0.93
    Spear of Desolation:
      total: 0.65
      efficiency: 0.6
      win: 0.69
      pick: 0.41
      fit: 0.74
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.82
      win: 0.62
      pick: 0.35
      fit: 0.6
    Heartseeker:
      total: 0.61
      efficiency: 0.45
      win: 0.64
      pick: 0.32
      fit: 0.99
    Obsidian Shard:
      total: 0.65
      efficiency: 0.53
      win: 0.72
      pick: 0.62
      fit: 0.7
    Soul Gem:
      total: 0.68
      efficiency: 0.53
      win: 0.79
      pick: 0.18
      fit: 0.84
  community_ordered:
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Heartseeker
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Spear of Desolation
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
  - Riptalon
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
    this god: Tyrfing, Silverbranch Bow, Riptalon, Nimble Ring, The Reaper, Tekko-Kagi,
    Bragi''s Harp, Golden Blade, Gluttonous Grimoire, Lernaean Bow, Dominance, Hydra''s
    Lament, Toxic Blade, The Crusher, Qin''s Blade, Blood-Bound Book, Bracer of The
    Abyss, Death Metal, Titan''s Bane, Spear of the Magus, Ancient Signet, Arondight,
    Chronos'' Pendant, Dreamer''s Idol, Dagger of Frenzy, Doom Orb, Avatar''s Parashu,
    Bancroft''s Talon, Berserker''s Shield, The World Stone, Gem of Focus, Heartwood
    Charm, Sun Beam Bow, Soul Reaver.'
  slot_scores:
    Tyrfing:
      total: 0.59
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.71
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.69
      pick: 0.41
      fit: 0.3
    Riptalon:
      total: 0.56
      efficiency: 0.45
      win: 0.67
      pick: 0.0
      fit: 0.7
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.49
      win: 0.67
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.62
      pick: 0.35
      fit: 0.2
    Soul Gem:
      total: 0.64
      efficiency: 0.58
      win: 0.79
      pick: 0.18
      fit: 0.49
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Chronos'' Pendant,
    Arondight, Gem of Focus, Heartwood Charm, Pendulum Blade, Totem of Death, Damaru,
    Genji''s Guard, Spear of the Magus, The Crusher, Death Metal, Dreamer''s Idol,
    Ancient Signet, Gluttonous Grimoire, Titan''s Bane, Breastplate of Valor, The
    Reaper, Doom Orb, Chandra''s Grace, The World Stone, Tyrfing, Blood-Bound Book,
    Staff of Myrddin, Bragi''s Harp, Avatar''s Parashu, Soul Reaver, The Cosmic Horror,
    Screeching Gargoyle, Freya''s Tears, Eye of Erebus, Shield of the Phoenix, Tekko-Kagi,
    Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.65
      win: 0.59
      pick: 0.22
      fit: 0.85
    Hydra's Lament:
      total: 0.6
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.75
    Spear of Desolation:
      total: 0.67
      efficiency: 0.6
      win: 0.69
      pick: 0.41
      fit: 0.85
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.62
      pick: 0.35
      fit: 0.35
    Obsidian Shard:
      total: 0.61
      efficiency: 0.53
      win: 0.72
      pick: 0.62
      fit: 0.45
    Soul Gem:
      total: 0.69
      efficiency: 0.53
      win: 0.79
      pick: 0.18
      fit: 0.95
  community_ordered:
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Tyrfing
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Tyrfing, Tekko-Kagi, The Crusher, Hydra''s
    Lament, Titan''s Bane, The Reaper, Bragi''s Harp, Death Metal, Arondight, Lernaean
    Bow, Dominance, Avatar''s Parashu, Pendulum Blade, Golden Blade, Spear of the
    Magus, Silverbranch Bow, Dreamer''s Idol, Gluttonous Grimoire, Transcendence,
    Runeforged Hammer, Chronos'' Pendant, Doom Orb, Ancient Signet, Toxic Blade, The
    World Stone, Shield Splitter, Eye of the Storm, Avenging Blade, Bracer of The
    Abyss, Nimble Ring, Riptalon, Gem of Focus, Heartwood Charm, The Cosmic Horror.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.65
      win: 0.59
      pick: 0.22
      fit: 0.78
    Tyrfing:
      total: 0.59
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.69
      pick: 0.41
      fit: 0.46
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.62
      pick: 0.35
      fit: 0.33
    Obsidian Shard:
      total: 0.61
      efficiency: 0.53
      win: 0.72
      pick: 0.62
      fit: 0.43
    Soul Gem:
      total: 0.63
      efficiency: 0.53
      win: 0.79
      pick: 0.18
      fit: 0.56
  community_ordered:
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Polynomicon
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Polynomicon
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Death Metal, Spear of the Magus, The
    Crusher, Hydra''s Lament, Dreamer''s Idol, Gluttonous Grimoire, Titan''s Bane,
    The Reaper, Chronos'' Pendant, Doom Orb, Ancient Signet, Bragi''s Harp, The World
    Stone, Arondight, Tyrfing, Avatar''s Parashu, Gem of Focus, Heartwood Charm, Pendulum
    Blade, The Cosmic Horror, Blood-Bound Book, Soul Reaver, Tekko-Kagi, Triton''s
    Conch, Totem of Death, Transcendence, Runeforged Hammer, Dominance, Bancroft''s
    Talon, Jade Scepter, Divine Ruin, Shield Splitter, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.59
      pick: 0.22
      fit: 0.69
    Spear of Desolation:
      total: 0.65
      efficiency: 0.6
      win: 0.69
      pick: 0.41
      fit: 0.69
    Polynomicon:
      total: 0.61
      efficiency: 0.56
      win: 0.76
      pick: 0.23
      fit: 0.41
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.82
      win: 0.62
      pick: 0.35
      fit: 0.56
    Obsidian Shard:
      total: 0.64
      efficiency: 0.53
      win: 0.72
      pick: 0.62
      fit: 0.66
    Soul Gem:
      total: 0.67
      efficiency: 0.53
      win: 0.79
      pick: 0.18
      fit: 0.79
  community_ordered:
  - Jotunn's Revenge
  - Spear of Desolation
  - Polynomicon
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Rod of Tahuti
  - The Crusher
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Hydra''s Lament, Titan''s Bane, The Reaper,
    Arondight, Pendulum Blade, Death Metal, Avatar''s Parashu, Tyrfing, Spear of the
    Magus, Tekko-Kagi, Dreamer''s Idol, Gluttonous Grimoire, Chronos'' Pendant, Bragi''s
    Harp, Doom Orb, The World Stone, Ancient Signet, Transcendence, Runeforged Hammer,
    Gem of Focus, Heartwood Charm, Dominance, The Cosmic Horror, Shield Splitter,
    Eye of the Storm, Avenging Blade, Blood-Bound Book, Damaru, Genji''s Guard, Triton''s
    Conch, Golden Blade, Soul Reaver, Lernaean Bow.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.59
      pick: 0.22
      fit: 0.1
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.65
      win: 0.59
      pick: 0.22
      fit: 0.9
    Spear of Desolation:
      total: 0.64
      efficiency: 0.6
      win: 0.69
      pick: 0.41
      fit: 0.62
    Transcendence:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.62
      pick: 0.35
      fit: 0.42
    The Crusher:
      total: 0.6
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
