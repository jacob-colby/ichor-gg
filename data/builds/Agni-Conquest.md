---
type: smite-build
god: Agni
mode: Conquest
builds:
- source: community
  aspect: Aspect of Combustion
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.45
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.46
    win_rate: 0.53
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.23
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.55
  - name: The World Stone
    pick_rate: 0.2
    win_rate: 0.54
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.56
    - name: Soul Reaver
      pick_rate: 0.13
      win_rate: 0.5
  - name: Soul Gem
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.5
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.53
  - name: Rod of Tahuti
    pick_rate: 0.3
    win_rate: 0.55
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.24
      win_rate: 0.53
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.55
  - name: Obsidian Shard
    pick_rate: 0.2
    win_rate: 0.55
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.17
      win_rate: 0.59
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.51
  - name: Evil Eye
    pick_rate: 0.13
    win_rate: 0.47
    alternates:
    - name: Soul Reaver
      pick_rate: 0.07
      win_rate: 0.66
    - name: Void Shard
      pick_rate: 0.07
      win_rate: 0.48
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.3
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.47
  - name: Archmage's Gem
    pick_rate: 0.14
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/agni/
  last_verified: '2026-08-11'
  god_win_rate: 0.5321543408360129
  god_matches_won: 993
  god_matches_played: 1866
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - The World Stone
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
    this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Doom Orb,
    Dreamer''s Idol, Genji''s Guard, Gem of Focus, Blood-Bound Book, Bancroft''s Talon,
    Helm of Radiance, Death Metal, Breastplate of Valor, Rod of Asclepius, Bracer
    of The Abyss, Jade Scepter, Ancient Signet, Polynomicon, Ethereal Staff, Wish-Granting
    Pearl, Alchemist Coat, Typhon’s Heart.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.79
    The World Stone:
      total: 0.55
      efficiency: 0.49
      win: 0.54
      pick: 0.27
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.79
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Genji''s Guard,
    Death Metal, Breastplate of Valor, Doom Orb, Dreamer''s Idol, Gem of Focus, Freya''s
    Tears, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Bragi''s Harp, Shield
    of the Phoenix, Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Kinetic Cuirass,
    Triton''s Conch, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.22
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.78
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.56
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Genji''s Guard, Blood-Bound Book, Bancroft''s Talon, Chandra''s
    Grace, Oni Hunter''s Garb, Breastplate of Valor, Spear of the Magus, Freya''s
    Tears, Lifebinder, The Cosmic Horror, Phoenix Feather, Shifter''s Shield, Erosion,
    Helm of Radiance, Spectral Armor, Jade Scepter, Eye of Providence, Draconic Scale,
    Sphere of Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.49
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.39
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - The World Stone
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
    for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Doom
    Orb, Dreamer''s Idol, Genji''s Guard, Screeching Gargoyle, Breastplate of Valor,
    Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death Metal, Gem of Focus,
    Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet, Polynomicon,
    Stone of Binding, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 1.0
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.85
    The World Stone:
      total: 0.56
      efficiency: 0.49
      win: 0.54
      pick: 0.27
      fit: 0.85
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.85
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Genji''s Guard, Spear of the Magus, Bracer of The
    Abyss, The Cosmic Horror, Bragi''s Harp, Death Metal, Breastplate of Valor, Nimble
    Ring, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Rod of Asclepius,
    Kinetic Cuirass, Amanita Charm, Jade Scepter, Oni Hunter''s Garb, Doom Orb, Freya''s
    Tears, Dreamer''s Idol, Eye of Providence, Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.08
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.49
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.55
      pick: 0.0
      fit: 0.63
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.32
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.42
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
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Gluttonous Grimoire, Freya''s Tears, Shield of the Phoenix, Gem of Focus, Spear
    of the Magus, The Cosmic Horror, Screeching Gargoyle, Chandra''s Grace, Death
    Metal, Gladiator''s Shield, Doom Orb, Blood-Bound Book, Dreamer''s Idol, Bancroft''s
    Talon, Helm of Radiance, Kinetic Cuirass, Prophetic Cloak, Amanita Charm, Rod
    of Asclepius, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.56
      win: 0.53
      pick: 0.23
      fit: 0.63
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.86
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - The Crusher
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, The Crusher, Gluttonous
    Grimoire, Death Metal, Hydra''s Lament, Spear of the Magus, Lernaean Bow, The
    Cosmic Horror, Bragi''s Harp, Genji''s Guard, The Reaper, Berserker''s Shield,
    Golden Blade, Tekko-Kagi, Runeforged Hammer, Heartseeker, Damaru, Bracer of The
    Abyss, Breastplate of Valor, Riptalon, Dominance, Tyrfing, Silverbranch Bow, Pendulum
    Blade, Triton''s Conch, Blood-Bound Book, Titan''s Bane, Doom Orb, Bancroft''s
    Talon, Helm of Radiance, Dreamer''s Idol, Rod of Asclepius, Arondight, Avenging
    Blade, Jade Scepter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.65
    Hydra's Lament:
      total: 0.53
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.53
    Death Metal:
      total: 0.53
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.55
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire,
    The Crusher, Spear of the Magus, Death Metal, The Cosmic Horror, Hydra''s Lament,
    Genji''s Guard, The Reaper, Bragi''s Harp, Heartseeker, Doom Orb, Runeforged Hammer,
    Dreamer''s Idol, Breastplate of Valor, Blood-Bound Book, Lernaean Bow, Damaru,
    Bancroft''s Talon, Helm of Radiance, Pendulum Blade, Triton''s Conch, Rod of Asclepius,
    Bracer of The Abyss, Gem of Focus, Titan''s Bane, Tekko-Kagi, Jade Scepter, Berserker''s
    Shield, Ancient Signet, Riptalon, Golden Blade, Arondight, Polynomicon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.69
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.56
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - The World Stone
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Doom Orb, Dreamer''s Idol, Genji''s Guard, Gem of Focus, Blood-Bound Book, Bancroft''s
    Talon, Helm of Radiance, Death Metal, Breastplate of Valor, Rod of Asclepius,
    Bracer of The Abyss, Jade Scepter, Ancient Signet, Polynomicon, Ethereal Staff,
    Wish-Granting Pearl, Alchemist Coat, Typhon’s Heart.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.89
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.79
    The World Stone:
      total: 0.55
      efficiency: 0.49
      win: 0.54
      pick: 0.27
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Soul Reaver
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Soul Reaver
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Genji''s
    Guard, Doom Orb, Bracer of The Abyss, Dreamer''s Idol, Breastplate of Valor, Blood-Bound
    Book, Gem of Focus, Bancroft''s Talon, Helm of Radiance, Death Metal, Rod of Asclepius,
    Jade Scepter, Nimble Ring, Ancient Signet, Bragi''s Harp, Polynomicon, Ethereal
    Staff, Wish-Granting Pearl.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.86
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.68
    Soul Reaver:
      total: 0.53
      efficiency: 0.45
      win: 0.66
      pick: 0.22
      fit: 0.46
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.68
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.96
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Genji''s Guard,
    Death Metal, Breastplate of Valor, Doom Orb, Dreamer''s Idol, Bragi''s Harp, Bracer
    of The Abyss, Gem of Focus, Freya''s Tears, Blood-Bound Book, Bancroft''s Talon,
    Helm of Radiance, Shield of the Phoenix, Rod of Asclepius, Jade Scepter, Kinetic
    Cuirass, Amanita Charm, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.2
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.71
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.51
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.51
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.51
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.81
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Spear of Desolation
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Genji''s Guard, Blood-Bound Book, Bancroft''s Talon, Chandra''s
    Grace, Oni Hunter''s Garb, Breastplate of Valor, Spear of the Magus, Lifebinder,
    Freya''s Tears, The Cosmic Horror, Phoenix Feather, Helm of Radiance, Shifter''s
    Shield, Spectral Armor, Erosion, Jade Scepter, Eye of Providence, Draconic Scale,
    Sphere of Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.46
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.86
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - The World Stone
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
    for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Doom
    Orb, Dreamer''s Idol, Genji''s Guard, Bracer of The Abyss, Screeching Gargoyle,
    Breastplate of Valor, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death
    Metal, Rod of Asclepius, Gem of Focus, Jade Scepter, Ancient Signet, Stone of
    Binding, Freya''s Tears, Polynomicon, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.9
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.77
    The World Stone:
      total: 0.54
      efficiency: 0.49
      win: 0.54
      pick: 0.27
      fit: 0.77
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.77
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 1.0
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Genji''s Guard, Spear of the Magus, Bracer of The
    Abyss, The Cosmic Horror, Bragi''s Harp, Death Metal, Breastplate of Valor, Nimble
    Ring, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Rod of Asclepius,
    Kinetic Cuirass, Amanita Charm, Jade Scepter, Oni Hunter''s Garb, Doom Orb, Freya''s
    Tears, Dreamer''s Idol, Eye of Providence, Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.08
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.49
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.55
      pick: 0.0
      fit: 0.63
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.32
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.58
  starter: *id001
  aspect: Aspect of Combustion
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
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Gluttonous Grimoire, Freya''s Tears, Shield of the Phoenix, Gem of Focus, Spear
    of the Magus, The Cosmic Horror, Screeching Gargoyle, Chandra''s Grace, Death
    Metal, Bracer of The Abyss, Gladiator''s Shield, Blood-Bound Book, Kinetic Cuirass,
    Bancroft''s Talon, Helm of Radiance, Doom Orb, Bragi''s Harp, Amanita Charm, Dreamer''s
    Idol, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.44
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.56
      win: 0.53
      pick: 0.23
      fit: 0.57
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.78
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.88
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - The Crusher
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, The Crusher, Gluttonous
    Grimoire, Death Metal, Hydra''s Lament, Spear of the Magus, Lernaean Bow, The
    Cosmic Horror, Bragi''s Harp, Genji''s Guard, The Reaper, Berserker''s Shield,
    Golden Blade, Tekko-Kagi, Runeforged Hammer, Heartseeker, Damaru, Bracer of The
    Abyss, Breastplate of Valor, Riptalon, Dominance, Tyrfing, Silverbranch Bow, Pendulum
    Blade, Triton''s Conch, Blood-Bound Book, Titan''s Bane, Doom Orb, Bancroft''s
    Talon, Helm of Radiance, Dreamer''s Idol, Rod of Asclepius, Arondight, Avenging
    Blade, Jade Scepter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.65
    Hydra's Lament:
      total: 0.53
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.53
    Death Metal:
      total: 0.53
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.55
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.65
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire,
    The Crusher, Spear of the Magus, Death Metal, The Cosmic Horror, Hydra''s Lament,
    Genji''s Guard, Bragi''s Harp, Lernaean Bow, The Reaper, Berserker''s Shield,
    Bracer of The Abyss, Breastplate of Valor, Runeforged Hammer, Heartseeker, Doom
    Orb, Tekko-Kagi, Blood-Bound Book, Dreamer''s Idol, Riptalon, Golden Blade, Damaru,
    Bancroft''s Talon, Helm of Radiance, Rod of Asclepius, Triton''s Conch, Pendulum
    Blade, Silverbranch Bow, Gem of Focus, Jade Scepter, Titan''s Bane, Dominance,
    Tyrfing, Ancient Signet.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.63
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.61
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.51
    Soul Gem:
      total: 0.59
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.73
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Genji''s Guard, Doom Orb, Bracer of The Abyss, Dreamer''s Idol, Breastplate of
    Valor, Blood-Bound Book, Gem of Focus, Bancroft''s Talon, Helm of Radiance, Death
    Metal, Rod of Asclepius, Jade Scepter, Nimble Ring, Ancient Signet, Bragi''s Harp,
    Polynomicon, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.56
      win: 0.53
      pick: 0.23
      fit: 0.54
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.86
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.68
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.55
      pick: 0.43
      fit: 0.68
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.57
      pick: 0.42
      fit: 0.96
  starter: *id001
  aspect: Aspect of Combustion
---
