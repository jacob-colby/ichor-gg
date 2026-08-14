---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.43
  aspect_win_rate: 0.58
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.39
    win_rate: 0.63
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.5
    - name: Chronos' Pendant
      pick_rate: 0.05
      win_rate: 0.33
  - name: Soul Gem
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.71
    - name: Doom Orb
      pick_rate: 0.1
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.57
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.21
      win_rate: 0.5
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.33
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.71
    alternates:
    - name: Evil Eye
      pick_rate: 0.09
      win_rate: 0.0
    - name: Captain's Ring
      pick_rate: 0.07
      win_rate: 0.67
  - name: Sage's Ring
    pick_rate: 0.18
    win_rate: 1.0
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.09
      win_rate: 0.5
    - name: Ring of Dispel
      pick_rate: 0.09
      win_rate: 1.0
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.25
    win_rate: 0.6
  - name: Archmage's Gem
    pick_rate: 0.21
    win_rate: 0.38
  - name: Bumba's Cudgel
    pick_rate: 0.15
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-08-13'
  god_win_rate: 0.5901639344262295
  god_matches_won: 36
  god_matches_played: 61
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  flex_slots:
  - Doom Orb
  - The World Stone
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
    this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The World Stone,
    Dreamer''s Idol, Gem of Focus, Totem of Death, Breastplate of Valor, Blood-Bound
    Book, Bancroft''s Talon, Helm of Radiance, Death Metal, Rod of Asclepius, Bracer
    of The Abyss, Jade Scepter, Ancient Signet, Polynomicon, Ethereal Staff, Wish-Granting
    Pearl, Chronos'' Pendant.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.65
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.64
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 1.0
    Doom Orb:
      total: 0.59
      efficiency: 0.49
      win: 0.67
      pick: 0.14
      fit: 0.77
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.77
    The World Stone:
      total: 0.57
      efficiency: 0.49
      win: 0.63
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.71
      pick: 0.35
      fit: 0.77
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Gluttonous Grimoire
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Doom Orb
  - Death Metal
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
    god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, Death Metal, Breastplate
    of Valor, The World Stone, Dreamer''s Idol, Gem of Focus, Totem of Death, Blood-Bound
    Book, Bancroft''s Talon, Helm of Radiance, Bragi''s Harp, Shield of the Phoenix,
    Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Kinetic Cuirass, Triton''s
    Conch, Chronos'' Pendant.'
  slot_scores:
    Death Metal:
      total: 0.55
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.78
    Doom Orb:
      total: 0.56
      efficiency: 0.49
      win: 0.67
      pick: 0.14
      fit: 0.56
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.71
      pick: 0.35
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
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
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Blood-Bound Book, Bancroft''s Talon, Chandra''s Grace, Breastplate
    of Valor, Oni Hunter''s Garb, Spear of the Magus, Lifebinder, Phoenix Feather,
    Erosion, Helm of Radiance, Spectral Armor, Jade Scepter, Eye of Providence, Draconic
    Scale, Chronos'' Pendant.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.63
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.67
      pick: 0.18
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.62
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.68
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.5
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.71
      pick: 0.35
      fit: 0.38
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  flex_slots:
  - Doom Orb
  - The World Stone
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The World Stone,
    Dreamer''s Idol, Screeching Gargoyle, Breastplate of Valor, Blood-Bound Book,
    Bancroft''s Talon, Helm of Radiance, Gem of Focus, Death Metal, Rod of Asclepius,
    Totem of Death, Bracer of The Abyss, Jade Scepter, Ancient Signet, Polynomicon,
    Stone of Binding, Chronos'' Pendant.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.66
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.94
    Spear of Desolation:
      total: 0.64
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 1.0
    Doom Orb:
      total: 0.6
      efficiency: 0.49
      win: 0.67
      pick: 0.14
      fit: 0.84
    Spear of the Magus:
      total: 0.62
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.84
    The World Stone:
      total: 0.58
      efficiency: 0.49
      win: 0.63
      pick: 0.0
      fit: 0.84
    Obsidian Shard:
      total: 0.65
      efficiency: 0.54
      win: 0.71
      pick: 0.35
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Spear of Desolation
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
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
    this god: Gluttonous Grimoire, Spear of the Magus, Bracer of The Abyss, Bragi''s
    Harp, Breastplate of Valor, Death Metal, Doom Orb, Nimble Ring, Blood-Bound Book,
    Bancroft''s Talon, Helm of Radiance, Rod of Asclepius, Kinetic Cuirass, Amanita
    Charm, Jade Scepter, Oni Hunter''s Garb, The World Stone, Gem of Focus, Dreamer''s
    Idol, Eye of Providence, Chronos'' Pendant.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.53
      efficiency: 0.49
      win: 0.63
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.53
      efficiency: 0.44
      win: 0.63
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.41
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.71
      pick: 0.35
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Gluttonous Grimoire,
    Gem of Focus, Shield of the Phoenix, Totem of Death, Spear of the Magus, Screeching
    Gargoyle, Chandra''s Grace, Doom Orb, Death Metal, Gladiator''s Shield, The World
    Stone, Blood-Bound Book, Dreamer''s Idol, Bancroft''s Talon, Helm of Radiance,
    Kinetic Cuirass, Prophetic Cloak, Amanita Charm, Rod of Asclepius, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.57
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.18
      fit: 0.48
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.86
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.71
      pick: 0.35
      fit: 0.37
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.57
      pick: 0.16
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, The Crusher, Gluttonous
    Grimoire, Hydra''s Lament, Death Metal, Spear of the Magus, Lernaean Bow, Bragi''s
    Harp, Doom Orb, The Reaper, Berserker''s Shield, Golden Blade, Runeforged Hammer,
    Tekko-Kagi, Damaru, Breastplate of Valor, Heartseeker, Bracer of The Abyss, Riptalon,
    Dominance, Pendulum Blade, Tyrfing, Silverbranch Bow, Blood-Bound Book, Triton''s
    Conch, Titan''s Bane, Bancroft''s Talon, Helm of Radiance, The World Stone, Dreamer''s
    Idol, Arondight, Rod of Asclepius, Gem of Focus, Avenging Blade, Jade Scepter,
    Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.65
    Hydra's Lament:
      total: 0.57
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.56
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.63
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.71
      pick: 0.35
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire,
    The Crusher, Spear of the Magus, Death Metal, Hydra''s Lament, Doom Orb, The Reaper,
    Bragi''s Harp, Breastplate of Valor, Heartseeker, The World Stone, Runeforged
    Hammer, Dreamer''s Idol, Pendulum Blade, Blood-Bound Book, Damaru, Lernaean Bow,
    Bancroft''s Talon, Helm of Radiance, Triton''s Conch, Gem of Focus, Rod of Asclepius,
    Bracer of The Abyss, Totem of Death, Titan''s Bane, Jade Scepter, Berserker''s
    Shield, Tekko-Kagi, Ancient Signet, Riptalon, Arondight, Golden Blade, Polynomicon,
    Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.7
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 0.7
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.65
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.71
      pick: 0.35
      fit: 0.55
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, Chronos'' Pendant,
    The World Stone, Doom Orb, Dreamer''s Idol, Gem of Focus, Totem of Death, Breastplate
    of Valor, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death Metal,
    Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet, Polynomicon,
    Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Chronos' Pendant:
      total: 0.44
      efficiency: 0.56
      win: 0.33
      pick: 0.05
      fit: 0.64
    Gluttonous Grimoire:
      total: 0.65
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.64
      efficiency: 0.52
      win: 0.63
      pick: 0.39
      fit: 1.0
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.28
      fit: 0.77
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.71
      pick: 0.35
      fit: 0.77
  starter: *id001
---
