---
type: smite-build
god: The Morrigan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mischief
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.67
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.28
    win_rate: 0.45
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.27
      win_rate: 0.44
    - name: The World Stone
      pick_rate: 0.12
      win_rate: 0.47
  - name: The World Stone
    pick_rate: 0.46
    win_rate: 0.44
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.47
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.18
  - name: Polynomicon
    pick_rate: 0.34
    win_rate: 0.41
    alternates:
    - name: The World Stone
      pick_rate: 0.19
      win_rate: 0.52
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.3
    alternates:
    - name: Polynomicon
      pick_rate: 0.18
      win_rate: 0.4
    - name: Gem of Focus
      pick_rate: 0.13
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.38
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.28
      win_rate: 0.53
    - name: Evil Eye
      pick_rate: 0.13
      win_rate: 0.47
  - name: Evil Eye
    pick_rate: 0.16
    win_rate: 0.54
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.67
    - name: Gem of Focus
      pick_rate: 0.06
      win_rate: 0.4
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.38
    win_rate: 0.5
  - name: Conduit Gem
    pick_rate: 0.22
    win_rate: 0.34
  - name: Bumba's Hammer
    pick_rate: 0.09
    win_rate: 0.31
  source_url: https://smitebrain.com/gods/the-morrigan/
  last_verified: '2026-08-14'
  god_win_rate: 0.4375
  god_matches_won: 63
  god_matches_played: 144
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
  - Gem of Focus
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  flex_slots:
  - The World Stone
  - Gem of Focus
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
    this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror,
    Doom Orb, Dreamer''s Idol, Chronos'' Pendant, Genji''s Guard, Blood-Bound Book,
    Totem of Death, Bancroft''s Talon, Helm of Radiance, Death Metal, Breastplate
    of Valor, Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet,
    Ethereal Staff, Wish-Granting Pearl, Alchemist Coat.'
  slot_scores:
    Gem of Focus:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.22
      fit: 0.6
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.9
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.44
      pick: 0.27
      fit: 1.0
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.8
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.8
    The World Stone:
      total: 0.52
      efficiency: 0.49
      win: 0.44
      pick: 0.63
      fit: 0.8
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Gem of Focus
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - The World Stone
  - Gem of Focus
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
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Genji''s
    Guard, Death Metal, Breastplate of Valor, Chronos'' Pendant, Doom Orb, Dreamer''s
    Idol, Totem of Death, Freya''s Tears, Blood-Bound Book, Bancroft''s Talon, Helm
    of Radiance, Bragi''s Harp, Shield of the Phoenix, Rod of Asclepius, Bracer of
    The Abyss, Jade Scepter, Kinetic Cuirass, Triton''s Conch.'
  slot_scores:
    Gem of Focus:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.22
      fit: 0.44
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.44
      pick: 0.27
      fit: 0.78
    The Cosmic Horror:
      total: 0.49
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.49
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.48
      efficiency: 0.49
      win: 0.44
      pick: 0.63
      fit: 0.56
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Oni Hunter's Garb
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Genji''s Guard, Blood-Bound Book, Bancroft''s
    Talon, Chandra''s Grace, Oni Hunter''s Garb, Breastplate of Valor, Spear of the
    Magus, Freya''s Tears, Lifebinder, The Cosmic Horror, Phoenix Feather, Shifter''s
    Shield, Erosion, Spectral Armor, Helm of Radiance, Eye of Providence, Jade Scepter,
    Draconic Scale, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.71
      win: 0.44
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.61
    Oni Hunter's Garb:
      total: 0.47
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.47
      efficiency: 0.52
      win: 0.44
      pick: 0.27
      fit: 0.49
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  flex_slots:
  - The World Stone
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror,
    Doom Orb, Dreamer''s Idol, Genji''s Guard, Chronos'' Pendant, Screeching Gargoyle,
    Breastplate of Valor, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Death
    Metal, Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Totem of Death, Ancient
    Signet, Stone of Binding, Freya''s Tears.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.44
      pick: 0.27
      fit: 1.0
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.86
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.86
    The World Stone:
      total: 0.53
      efficiency: 0.49
      win: 0.44
      pick: 0.63
      fit: 0.86
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.38
      pick: 0.28
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Spear of the Magus
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
    this god: Gluttonous Grimoire, Soul Gem, Genji''s Guard, Spear of the Magus, Bracer
    of The Abyss, The Cosmic Horror, Bragi''s Harp, Death Metal, Breastplate of Valor,
    Nimble Ring, Blood-Bound Book, Bancroft''s Talon, Chronos'' Pendant, Helm of Radiance,
    Kinetic Cuirass, Rod of Asclepius, Amanita Charm, Oni Hunter''s Garb, Jade Scepter,
    Doom Orb, Freya''s Tears, Dreamer''s Idol, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.46
      efficiency: 0.71
      win: 0.44
      pick: 0.0
      fit: 0.08
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.44
      efficiency: 0.49
      win: 0.44
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.44
      efficiency: 0.44
      win: 0.44
      pick: 0.0
      fit: 0.62
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.5
    Spear of the Magus:
      total: 0.46
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Gem of Focus
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Gluttonous
    Grimoire, Breastplate of Valor, Chronos'' Pendant, Freya''s Tears, Shield of the
    Phoenix, Spear of the Magus, Totem of Death, The Cosmic Horror, Screeching Gargoyle,
    Chandra''s Grace, Death Metal, Gladiator''s Shield, Doom Orb, Dreamer''s Idol,
    Blood-Bound Book, Bancroft''s Talon, Helm of Radiance, Kinetic Cuirass, Prophetic
    Cloak, Amanita Charm, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.44
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.49
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.62
    Gem of Focus:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.22
      fit: 0.62
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.44
      pick: 0.27
      fit: 0.86
    Soul Gem:
      total: 0.55
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.96
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
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The
    Cosmic Horror, Doom Orb, Dreamer''s Idol, Chronos'' Pendant, Genji''s Guard, Blood-Bound
    Book, Totem of Death, Bancroft''s Talon, Helm of Radiance, Death Metal, Breastplate
    of Valor, Rod of Asclepius, Bracer of The Abyss, Jade Scepter, Ancient Signet,
    Ethereal Staff, Wish-Granting Pearl, Alchemist Coat.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.9
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.44
      pick: 0.27
      fit: 1.0
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.8
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.8
    The World Stone:
      total: 0.52
      efficiency: 0.49
      win: 0.44
      pick: 0.63
      fit: 0.8
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.38
      pick: 0.28
      fit: 0.8
  starter: *id001
---
