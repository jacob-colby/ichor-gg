---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.46
  aspect_win_rate: 0.63
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.28
    win_rate: 0.59
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.52
    - name: Book of Thoth
      pick_rate: 0.06
      win_rate: 0.4
  - name: Genji's Guard
    pick_rate: 0.11
    win_rate: 0.63
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.62
  - name: Rod of Tahuti
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.57
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.62
  - name: Obsidian Shard
    pick_rate: 0.12
    win_rate: 0.38
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.55
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.64
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.58
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.5
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.67
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.83
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.2
    win_rate: 0.57
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.48
  - name: Bumba's Cudgel
    pick_rate: 0.13
    win_rate: 0.71
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-08-19'
  god_win_rate: 0.5851393188854489
  god_matches_won: 189
  god_matches_played: 323
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus,
    Nimble Ring, Chronos'' Pendant, Doom Orb, The World Stone, Dreamer''s Idol, Gem
    of Focus, Totem of Death, Death Metal, Breastplate of Valor, Helm of Radiance,
    Blood-Bound Book, Rod of Asclepius, Bancroft''s Talon, Jade Scepter, Bracer of
    The Abyss, Ethereal Staff, Book of Thoth, Alchemist Coat.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.15
      fit: 0.23
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.59
      pick: 0.28
      fit: 1.0
    The Cosmic Horror:
      total: 0.6
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.59
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.77
      win: 0.59
      pick: 0.19
      fit: 0.77
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Nimble Ring, Death Metal, The Cosmic Horror, Spear of
    the Magus, Breastplate of Valor, Chronos'' Pendant, Doom Orb, Bragi''s Harp, The
    World Stone, Bancroft''s Talon, Triton''s Conch, Helm of Radiance, Book of Thoth,
    Gem of Focus, Blood-Bound Book, Rod of Asclepius, Totem of Death, Oni Hunter''s
    Garb, Polynomicon, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.49
      win: 0.62
      pick: 0.11
      fit: 0.39
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.15
      fit: 0.24
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.24
    Death Metal:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.59
      pick: 0.19
      fit: 0.57
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Nimble
    Ring, Death Metal, Chronos'' Pendant, Breastplate of Valor, Doom Orb, The World
    Stone, Gem of Focus, Dreamer''s Idol, Totem of Death, Shield of the Phoenix, Bragi''s
    Harp, Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Amanita
    Charm, Screeching Gargoyle, Triton''s Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.15
      fit: 0.22
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.59
      pick: 0.28
      fit: 0.78
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.59
      pick: 0.19
      fit: 0.56
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Chandra''s Grace, Nimble Ring, Blood-Bound
    Book, Oni Hunter''s Garb, Lifebinder, Breastplate of Valor, Bancroft''s Talon,
    The Cosmic Horror, Spear of the Magus, Phoenix Feather, Erosion, Spectral Armor,
    Eye of Providence, Draconic Scale, Helm of Radiance, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.15
      fit: 0.27
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.64
      pick: 0.2
      fit: 0.42
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.59
      pick: 0.19
      fit: 0.38
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Spear of the Magus
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear of the Magus,
    Doom Orb, The World Stone, Nimble Ring, Dreamer''s Idol, Chronos'' Pendant, Screeching
    Gargoyle, Breastplate of Valor, Death Metal, Gem of Focus, Helm of Radiance, Blood-Bound
    Book, Rod of Asclepius, Totem of Death, Bancroft''s Talon, Jade Scepter, Stone
    of Binding, Shield of the Phoenix, Kinetic Cuirass.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.64
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.94
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.59
      pick: 0.28
      fit: 1.0
    The Cosmic Horror:
      total: 0.61
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.84
    Doom Orb:
      total: 0.57
      efficiency: 0.46
      win: 0.62
      pick: 0.0
      fit: 0.84
    Spear of the Magus:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.59
      pick: 0.19
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear
    of the Magus, Death Metal, Bragi''s Harp, Bracer of The Abyss, Breastplate of
    Valor, Chronos'' Pendant, Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass,
    Amanita Charm, Helm of Radiance, Rod of Asclepius, Eye of Providence, Oni Hunter''s
    Garb, Shield of the Phoenix, Gem of Focus, Jade Scepter, Doom Orb.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.63
      pick: 0.15
      fit: 0.09
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.59
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.52
      efficiency: 0.42
      win: 0.62
      pick: 0.0
      fit: 0.62
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.59
      pick: 0.19
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Breastplate of Valor, Gluttonous
    Grimoire, Chronos'' Pendant, Shield of the Phoenix, Gem of Focus, Nimble Ring,
    Totem of Death, The Cosmic Horror, Screeching Gargoyle, Chandra''s Grace, Spear
    of the Magus, Death Metal, Gladiator''s Shield, Kinetic Cuirass, Prophetic Cloak,
    Amanita Charm, Doom Orb, The World Stone, Helm of Radiance, Eye of Providence,
    Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.69
      win: 0.63
      pick: 0.15
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.64
      pick: 0.2
      fit: 0.48
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.59
      pick: 0.28
      fit: 0.86
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.59
      pick: 0.19
      fit: 0.37
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, The Crusher, Soul Gem,
    Gluttonous Grimoire, Nimble Ring, Death Metal, Hydra''s Lament, The Cosmic Horror,
    Spear of the Magus, The Reaper, Bragi''s Harp, Lernaean Bow, Runeforged Hammer,
    Tekko-Kagi, Golden Blade, Berserker''s Shield, Damaru, Chronos'' Pendant, Tyrfing,
    Breastplate of Valor, Pendulum Blade, Heartseeker, Riptalon, Titan''s Bane, Triton''s
    Conch, Silverbranch Bow, Arondight, Dominance, Bracer of The Abyss, Transcendence,
    Avenging Blade, Helm of Radiance, Doom Orb, Shield Splitter, The World Stone,
    Blood-Bound Book, Rod of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.49
      win: 0.62
      pick: 0.11
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.65
    Transcendence:
      total: 0.51
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.32
    The Crusher:
      total: 0.6
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.59
      pick: 0.19
      fit: 0.43
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, The Crusher,
    Gluttonous Grimoire, Death Metal, The Cosmic Horror, Nimble Ring, Spear of the
    Magus, Hydra''s Lament, The Reaper, Chronos'' Pendant, Runeforged Hammer, Bragi''s
    Harp, Pendulum Blade, Breastplate of Valor, Doom Orb, Damaru, The World Stone,
    Triton''s Conch, Heartseeker, Helm of Radiance, Titan''s Bane, Gem of Focus, Tekko-Kagi,
    Blood-Bound Book, Rod of Asclepius, Dreamer''s Idol, Lernaean Bow, Totem of Death,
    Arondight, Bancroft''s Talon, Golden Blade, Jade Scepter, Berserker''s Shield,
    Transcendence, Avenging Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.49
      win: 0.62
      pick: 0.11
      fit: 0.3
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.7
    Transcendence:
      total: 0.51
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.3
    The Crusher:
      total: 0.6
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.59
      pick: 0.19
      fit: 0.55
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Obsidian Shard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, The Cosmic Horror, Spear
    of the Magus, Nimble Ring, Chronos'' Pendant, Doom Orb, The World Stone, Dreamer''s
    Idol, Gem of Focus, Totem of Death, Death Metal, Breastplate of Valor, Helm of
    Radiance, Blood-Bound Book, Rod of Asclepius, Bancroft''s Talon, Jade Scepter,
    Bracer of The Abyss, Ethereal Staff, Alchemist Coat, Book of Thoth.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.63
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.59
      pick: 0.28
      fit: 1.0
    The Cosmic Horror:
      total: 0.6
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.59
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.77
      win: 0.59
      pick: 0.19
      fit: 0.77
    Obsidian Shard:
      total: 0.48
      efficiency: 0.52
      win: 0.38
      pick: 0.2
      fit: 0.77
  starter: *id001
---
