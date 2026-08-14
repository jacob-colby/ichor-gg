---
type: smite-build
god: Morgan Le Fay
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cursed Crown
  aspect_pick_rate: 0.43
  aspect_win_rate: 0.46
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.25
    win_rate: 0.52
    alternates:
    - name: Lifebinder
      pick_rate: 0.18
      win_rate: 0.47
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.48
  - name: The Cosmic Horror
    pick_rate: 0.11
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.61
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.65
  - name: Totem of Death
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.5
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.71
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.11
      win_rate: 0.67
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.95
  - name: Obsidian Shard
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.55
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.45
  - name: Void Shard
    pick_rate: 0.09
    win_rate: 0.73
    alternates:
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.33
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 0.2
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.45
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.33
    win_rate: 0.43
  - name: Pendulum of the Ages
    pick_rate: 0.08
    win_rate: 0.7
  source_url: https://smitebrain.com/gods/morgan-le-fay/
  last_verified: '2026-08-14'
  god_win_rate: 0.5306122448979592
  god_matches_won: 130
  god_matches_played: 245
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Ethereal Staff
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Chronos'' Pendant,
    The World Stone, Doom Orb, Dreamer''s Idol, Gem of Focus, Blood-Bound Book, Bancroft''s
    Talon, Helm of Radiance, Death Metal, Breastplate of Valor, Rod of Asclepius,
    Bracer of The Abyss, Jade Scepter, Ancient Signet, Polynomicon, Wish-Granting
    Pearl, Alchemist Coat.'
  slot_scores:
    Ethereal Staff:
      total: 0.56
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.42
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.59
      win: 0.52
      pick: 0.15
      fit: 0.79
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.79
    Soul Gem:
      total: 0.68
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Ethereal Staff
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Ethereal Staff
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Death Metal, Breastplate
    of Valor, Chronos'' Pendant, The World Stone, Doom Orb, Freya''s Tears, Dreamer''s
    Idol, Gem of Focus, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Bragi''s
    Harp, Shield of the Phoenix, Rod of Asclepius, Bracer of The Abyss, Jade Scepter,
    Kinetic Cuirass, Triton''s Conch.'
  slot_scores:
    Ethereal Staff:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.22
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.78
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.15
      fit: 0.56
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.56
    Soul Gem:
      total: 0.66
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Freya''s Tears, Blood-Bound Book, Bancroft''s
    Talon, Chandra''s Grace, Oni Hunter''s Garb, Breastplate of Valor, Spear of the
    Magus, Phoenix Feather, Erosion, Helm of Radiance, Spectral Armor, Jade Scepter,
    Eye of Providence, Draconic Scale, Sphere of Negation, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.61
    Ethereal Staff:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.4
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.42
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Rod of Tahuti
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, The World Stone,
    Doom Orb, Dreamer''s Idol, Chronos'' Pendant, Screeching Gargoyle, Breastplate
    of Valor, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death Metal,
    Gem of Focus, Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet,
    Polynomicon, Stone of Binding.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.59
      win: 0.52
      pick: 0.15
      fit: 0.85
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.44
      win: 0.59
      pick: 0.28
      fit: 0.85
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.85
    Soul Gem:
      total: 0.68
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bracer of The Abyss,
    Bragi''s Harp, Death Metal, Breastplate of Valor, Nimble Ring, Blood-Bound Book,
    Bancroft''s Talon, Chronos'' Pendant, Freya''s Tears, Helm of Radiance, Rod of
    Asclepius, Kinetic Cuirass, Amanita Charm, Jade Scepter, Oni Hunter''s Garb, The
    World Stone, Doom Orb, Dreamer''s Idol, Eye of Providence, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.48
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.63
    Ethereal Staff:
      total: 0.52
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.17
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.32
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Totem of Death
  - Soul Gem
  flex_slots:
  - Totem of Death
  - Freya's Tears
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
    Grimoire, Freya''s Tears, Chronos'' Pendant, Gem of Focus, Shield of the Phoenix,
    Spear of the Magus, Screeching Gargoyle, Chandra''s Grace, Death Metal, Gladiator''s
    Shield, The World Stone, Doom Orb, Blood-Bound Book, Dreamer''s Idol, Bancroft''s
    Talon, Helm of Radiance, Kinetic Cuirass, Prophetic Cloak, Amanita Charm, Rod
    of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.16
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.48
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.86
    Totem of Death:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.2
      fit: 0.63
    Soul Gem:
      total: 0.68
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Ethereal Staff
  - Death Metal
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Ethereal Staff
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, The Crusher,
    Gluttonous Grimoire, Death Metal, Hydra''s Lament, Spear of the Magus, Lernaean
    Bow, Bragi''s Harp, The Reaper, Berserker''s Shield, Golden Blade, Runeforged
    Hammer, Tekko-Kagi, Damaru, Heartseeker, Bracer of The Abyss, Breastplate of Valor,
    Riptalon, Chronos'' Pendant, Dominance, Tyrfing, Silverbranch Bow, Pendulum Blade,
    Blood-Bound Book, Triton''s Conch, Titan''s Bane, The World Stone, Doom Orb, Bancroft''s
    Talon, Helm of Radiance, Dreamer''s Idol, Rod of Asclepius, Arondight, Avenging
    Blade, Jade Scepter, Gem of Focus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.65
    Ethereal Staff:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.23
    Death Metal:
      total: 0.52
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.63
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.44
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Ethereal Staff
  - Spear of the Magus
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Ethereal Staff
  - Spear of the Magus
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Gluttonous
    Grimoire, The Crusher, Spear of the Magus, Death Metal, Hydra''s Lament, The Reaper,
    Chronos'' Pendant, Bragi''s Harp, Heartseeker, The World Stone, Doom Orb, Dreamer''s
    Idol, Runeforged Hammer, Breastplate of Valor, Blood-Bound Book, Damaru, Lernaean
    Bow, Bancroft''s Talon, Helm of Radiance, Pendulum Blade, Triton''s Conch, Rod
    of Asclepius, Gem of Focus, Bracer of The Abyss, Titan''s Bane, Jade Scepter,
    Tekko-Kagi, Berserker''s Shield, Ancient Signet, Riptalon, Golden Blade, Arondight,
    Polynomicon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.69
    Ethereal Staff:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.31
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.56
    Soul Gem:
      total: 0.65
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, Chronos''
    Pendant, The World Stone, Doom Orb, Dreamer''s Idol, Gem of Focus, Blood-Bound
    Book, Bancroft''s Talon, Helm of Radiance, Death Metal, Breastplate of Valor,
    Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet, Polynomicon,
    Wish-Granting Pearl, Alchemist Coat.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.59
      win: 0.52
      pick: 0.15
      fit: 0.79
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Spear of the Magus
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Shield
    of the Phoenix, Spear of the Magus, Kinetic Cuirass, Chandra''s Grace, Oni Hunter''s
    Garb, Jade Scepter, Blood-Bound Book, Bancroft''s Talon, Wish-Granting Pearl,
    Freya''s Tears, Breastplate of Valor, Alchemist Coat, Chronos'' Pendant, Yogi''s
    Necklace, Phoenix Feather, Spectral Armor, The World Stone.'
  slot_scores:
    Ethereal Staff:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.62
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.47
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.47
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.92
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Ethereal Staff
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Spear of the Magus
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Shield of the Phoenix, Rod
    of Asclepius, Spear of the Magus, Chandra''s Grace, Blood-Bound Book, Kinetic
    Cuirass, Bancroft''s Talon, Breastplate of Valor, Freya''s Tears, Oni Hunter''s
    Garb, Death Metal, Chronos'' Pendant, Jade Scepter, Wish-Granting Pearl, The World
    Stone, Doom Orb, Yogi''s Necklace, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.16
      fit: 0.24
    Ethereal Staff:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.34
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.59
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.42
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.42
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.89
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Freya''s Tears, Chandra''s Grace, Oni Hunter''s
    Garb, Blood-Bound Book, Breastplate of Valor, Bancroft''s Talon, Spear of the
    Magus, Erosion, Phoenix Feather, Spectral Armor, Eye of Providence, Draconic Scale,
    Helm of Radiance, Jade Scepter, Leviathan''s Hide, Midgardian Mail, Shifter''s
    Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.63
    Ethereal Staff:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.37
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.44
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.36
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.83
    Soul Gem:
      total: 0.66
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.87
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ethereal Staff
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - The Cosmic Horror
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Amanita Charm,
    Rod of Asclepius, Shield of the Phoenix, Kinetic Cuirass, Oni Hunter''s Garb,
    Chandra''s Grace, Screeching Gargoyle, The World Stone, Doom Orb, Blood-Bound
    Book, Bancroft''s Talon, Dreamer''s Idol, Void Stone, Void Shield, Jade Scepter,
    Breastplate of Valor, Wish-Granting Pearl.'
  slot_scores:
    Ethereal Staff:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.38
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.7
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.15
      fit: 0.59
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.59
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.59
    Soul Gem:
      total: 0.68
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 1.0
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Rod of Asclepius, Blood-Bound
    Book, Shield of the Phoenix, Bancroft''s Talon, Kinetic Cuirass, Oni Hunter''s
    Garb, Spear of the Magus, Chandra''s Grace, Bracer of The Abyss, Breastplate of
    Valor, Freya''s Tears, Death Metal, Jade Scepter, Bragi''s Harp, Yogi''s Necklace,
    Nimble Ring, Spectral Armor, Chronos'' Pendant.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.31
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.37
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.51
    Ethereal Staff:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.24
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.23
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.67
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Ethereal Staff
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, Shield
    of the Phoenix, Chandra''s Grace, Amanita Charm, Breastplate of Valor, Freya''s
    Tears, Rod of Asclepius, Chronos'' Pendant, Kinetic Cuirass, Oni Hunter''s Garb,
    Spear of the Magus, Screeching Gargoyle, Blood-Bound Book, Bancroft''s Talon,
    Gem of Focus, Gladiator''s Shield, Jade Scepter, Yogi''s Necklace, Death Metal,
    Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.16
      fit: 0.43
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.36
    Ethereal Staff:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.29
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.43
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.52
      pick: 0.25
      fit: 0.64
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.94
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Ethereal Staff
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Obsidian Shard
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Amanita Charm, Berserker''s Shield, The Reaper, Rod of Asclepius,
    Runeforged Hammer, Hydra''s Lament, Golden Blade, Shield of the Phoenix, Riptalon,
    Death Metal, Kinetic Cuirass, Lernaean Bow, Spear of the Magus, Oni Hunter''s
    Garb, Blood-Bound Book, Bancroft''s Talon, Chandra''s Grace, Pharaoh''s Curse,
    Eye of the Storm, Avenging Blade, Breastplate of Valor, Bragi''s Harp, Damaru,
    Jade Scepter, Triton''s Conch, Heartseeker, Tekko-Kagi, Shogun''s Ofuda, Bracer
    of The Abyss, Yogi''s Necklace, Silverbranch Bow, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.52
    Ethereal Staff:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.31
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.53
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.31
    Soul Gem:
      total: 0.64
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.7
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Ethereal Staff
  - Spear of the Magus
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Spear of the Magus
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, Jotunn''s
    Revenge, The Crusher, Amanita Charm, Rod of Asclepius, Spear of the Magus, The
    Reaper, Shield of the Phoenix, Death Metal, Runeforged Hammer, Blood-Bound Book,
    Berserker''s Shield, Bancroft''s Talon, Hydra''s Lament, Kinetic Cuirass, Oni
    Hunter''s Garb, Chandra''s Grace, Jade Scepter, Riptalon, Triton''s Conch, Golden
    Blade, Eye of the Storm, Breastplate of Valor, Wish-Granting Pearl, Chronos''
    Pendant, Avenging Blade, Alchemist Coat, Pharaoh''s Curse, Damaru, Lernaean Bow,
    Helm of Radiance, Bragi''s Harp, Yogi''s Necklace, Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.51
    Ethereal Staff:
      total: 0.56
      efficiency: 0.53
      win: 0.67
      pick: 0.18
      fit: 0.41
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.51
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.41
    Soul Gem:
      total: 0.65
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.81
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - The Cosmic Horror
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Rod of
    Asclepius, Shield of the Phoenix, Spear of the Magus, Kinetic Cuirass, Chandra''s
    Grace, Oni Hunter''s Garb, Jade Scepter, Blood-Bound Book, Bancroft''s Talon,
    Wish-Granting Pearl, Breastplate of Valor, Alchemist Coat, Chronos'' Pendant,
    Yogi''s Necklace, Phoenix Feather, Freya''s Tears, Spectral Armor, The World Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.16
      fit: 0.25
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.85
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.15
      fit: 0.47
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.67
      efficiency: 0.59
      win: 0.71
      pick: 0.14
      fit: 0.92
  starter: *id001
  aspect: Aspect of the Cursed Crown
---
