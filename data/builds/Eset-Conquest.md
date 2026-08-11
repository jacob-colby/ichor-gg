---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.35
  aspect_win_rate: 0.59
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.38
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.61
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.68
  - name: Soul Gem
    pick_rate: 0.1
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.61
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.6
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.61
    alternates:
    - name: Soul Gem
      pick_rate: 0.12
      win_rate: 0.61
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.61
  - name: Obsidian Shard
    pick_rate: 0.12
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.22
      win_rate: 0.58
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.65
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.49
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.15
      win_rate: 0.62
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.6
  - name: Void Shard
    pick_rate: 0.06
    win_rate: 0.62
    alternates:
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.42
    - name: Oracle Staff
      pick_rate: 0.06
      win_rate: 0.4
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.25
    win_rate: 0.54
  - name: Archmage's Gem
    pick_rate: 0.2
    win_rate: 0.6
  - name: Bumba's Hammer
    pick_rate: 0.11
    win_rate: 0.69
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-08-10'
  god_win_rate: 0.5752941176470588
  god_matches_won: 489
  god_matches_played: 850
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Genji''s Guard, Spear of the Magus, The
    Cosmic Horror, Freya''s Tears, Chronos'' Pendant, Doom Orb, The World Stone, Dreamer''s
    Idol, Gem of Focus, Death Metal, Breastplate of Valor, Blood-Bound Book, Helm
    of Radiance, Bancroft''s Talon, Rod of Asclepius, Bracer of The Abyss, Jade Scepter,
    Ancient Signet, Polynomicon, Ethereal Staff, Wish-Granting Pearl, Alchemist Coat.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.61
      pick: 0.11
      fit: 0.23
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.55
      pick: 0.38
      fit: 1.0
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.44
      win: 0.61
      pick: 0.2
      fit: 0.77
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.77
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.57
      pick: 0.14
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Genji''s Guard, Gluttonous Grimoire, Freya''s Tears, Spear of the
    Magus, The Cosmic Horror, Death Metal, Breastplate of Valor, Chronos'' Pendant,
    Doom Orb, The World Stone, Dreamer''s Idol, Gem of Focus, Blood-Bound Book, Helm
    of Radiance, Bragi''s Harp, Bancroft''s Talon, Shield of the Phoenix, Rod of Asclepius,
    Bracer of The Abyss, Jade Scepter, Triton''s Conch, Kinetic Cuirass, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.61
      pick: 0.11
      fit: 0.22
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.65
      pick: 0.08
      fit: 0.22
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.38
      fit: 0.78
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.44
      win: 0.61
      pick: 0.2
      fit: 0.56
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.56
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.57
      pick: 0.14
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Shifter's Shield
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Genji''s Guard, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Shifter''s Shield, Shield of the Phoenix, Rod of Asclepius, Kinetic
    Cuirass, Blood-Bound Book, Bancroft''s Talon, Chandra''s Grace, Breastplate of
    Valor, Oni Hunter''s Garb, Spear of the Magus, Lifebinder, The Cosmic Horror,
    Phoenix Feather, Erosion, Helm of Radiance, Spectral Armor, Jade Scepter, Eye
    of Providence, Draconic Scale, Sphere of Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.61
      pick: 0.11
      fit: 0.27
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.65
      pick: 0.08
      fit: 0.42
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.15
      fit: 0.5
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.38
      fit: 0.5
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.57
      pick: 0.14
      fit: 0.9
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
  - Spear of the Magus
  - The Cosmic Horror
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
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Genji''s Guard, Freya''s Tears, Doom Orb, The World Stone, Dreamer''s Idol, Chronos''
    Pendant, Screeching Gargoyle, Breastplate of Valor, Death Metal, Blood-Bound Book,
    Helm of Radiance, Bancroft''s Talon, Gem of Focus, Rod of Asclepius, Bracer of
    The Abyss, Jade Scepter, Ancient Signet, Polynomicon, Stone of Binding, Ethereal
    Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.55
      pick: 0.38
      fit: 1.0
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.84
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.44
      win: 0.61
      pick: 0.2
      fit: 0.84
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.84
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.57
      pick: 0.14
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Genji''s Guard, Gluttonous Grimoire, Freya''s Tears, Spear
    of the Magus, Bracer of The Abyss, The Cosmic Horror, Death Metal, Bragi''s Harp,
    Breastplate of Valor, Nimble Ring, Blood-Bound Book, Bancroft''s Talon, Chronos''
    Pendant, Helm of Radiance, Kinetic Cuirass, Rod of Asclepius, Amanita Charm, Jade
    Scepter, Oni Hunter''s Garb, Doom Orb, The World Stone, Eye of Providence, Dreamer''s
    Idol, Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.61
      pick: 0.11
      fit: 0.09
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.47
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.65
      pick: 0.08
      fit: 0.09
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.14
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Freya''s
    Tears, Breastplate of Valor, Gluttonous Grimoire, Chronos'' Pendant, Shield of
    the Phoenix, Gem of Focus, Spear of the Magus, The Cosmic Horror, Screeching Gargoyle,
    Chandra''s Grace, Death Metal, Gladiator''s Shield, Doom Orb, The World Stone,
    Blood-Bound Book, Dreamer''s Idol, Helm of Radiance, Bancroft''s Talon, Kinetic
    Cuirass, Prophetic Cloak, Amanita Charm, Rod of Asclepius, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.61
      pick: 0.11
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.65
      pick: 0.08
      fit: 0.48
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.38
      fit: 0.86
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.57
      pick: 0.14
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  - The Crusher
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Genji''s Guard,
    The Crusher, Gluttonous Grimoire, Death Metal, Hydra''s Lament, Spear of the Magus,
    Lernaean Bow, Bragi''s Harp, The Cosmic Horror, The Reaper, Berserker''s Shield,
    Runeforged Hammer, Golden Blade, Tekko-Kagi, Damaru, Heartseeker, Breastplate
    of Valor, Bracer of The Abyss, Chronos'' Pendant, Riptalon, Dominance, Pendulum
    Blade, Tyrfing, Silverbranch Bow, Triton''s Conch, Blood-Bound Book, Titan''s
    Bane, Helm of Radiance, Doom Orb, The World Stone, Bancroft''s Talon, Dreamer''s
    Idol, Arondight, Rod of Asclepius, Avenging Blade, Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.61
      pick: 0.11
      fit: 0.13
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.65
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.65
      pick: 0.08
      fit: 0.13
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.38
      fit: 0.56
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.14
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Spear of Desolation
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Crusher
  - Obsidian Shard
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Gluttonous
    Grimoire, Genji''s Guard, The Crusher, Death Metal, Spear of the Magus, The Cosmic
    Horror, Hydra''s Lament, The Reaper, Chronos'' Pendant, Bragi''s Harp, Heartseeker,
    Doom Orb, The World Stone, Runeforged Hammer, Breastplate of Valor, Dreamer''s
    Idol, Damaru, Lernaean Bow, Pendulum Blade, Blood-Bound Book, Helm of Radiance,
    Bancroft''s Talon, Triton''s Conch, Gem of Focus, Rod of Asclepius, Bracer of
    The Abyss, Titan''s Bane, Tekko-Kagi, Jade Scepter, Berserker''s Shield, Arondight,
    Ancient Signet, Golden Blade, Riptalon, Polynomicon.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.61
      pick: 0.11
      fit: 0.15
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.55
      pick: 0.38
      fit: 0.7
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.65
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.55
    Soul Gem:
      total: 0.59
      efficiency: 0.59
      win: 0.57
      pick: 0.14
      fit: 0.8
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The
    Cosmic Horror, Chronos'' Pendant, Doom Orb, The World Stone, Dreamer''s Idol,
    Genji''s Guard, Gem of Focus, Death Metal, Breastplate of Valor, Blood-Bound Book,
    Helm of Radiance, Bancroft''s Talon, Rod of Asclepius, Bracer of The Abyss, Jade
    Scepter, Ancient Signet, Polynomicon, Ethereal Staff, Wish-Granting Pearl, Freya''s
    Tears, Alchemist Coat.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.55
      pick: 0.38
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.77
  starter: *id001
---
