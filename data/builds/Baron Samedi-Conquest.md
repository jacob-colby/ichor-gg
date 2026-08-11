---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.75
  aspect_win_rate: 0.51
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.17
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.58
    - name: Lifebinder
      pick_rate: 0.11
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.55
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.48
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.41
  - name: Rod of Tahuti
    pick_rate: 0.09
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.49
  - name: Obsidian Shard
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.7
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.65
  - name: Engraved Guard
    pick_rate: 0.04
    win_rate: 0.57
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.04
      win_rate: 0.38
    - name: Draconic Scale
      pick_rate: 0.04
      win_rate: 0.82
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.64
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.43
  - name: Pendulum of The Ages
    pick_rate: 0.12
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-08-10'
  god_win_rate: 0.5207373271889401
  god_matches_won: 339
  god_matches_played: 651
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
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Shifter''s Shield,
    Soul Gem, Kinetic Cuirass, Amanita Charm, Freya''s Tears, Breastplate of Valor,
    Shield of the Phoenix, Spear of the Magus, Oni Hunter''s Garb, The Cosmic Horror,
    Helm of Radiance, Erosion, Eye of Providence, Spectral Armor, Rod of Asclepius,
    Jade Scepter, Chronos'' Pendant, Leviathan''s Hide, Midgardian Mail, Wish-Granting
    Pearl, Death Metal.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.55
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.56
      efficiency: 0.52
      win: 0.7
      pick: 0.13
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.14
      fit: 0.49
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.82
      pick: 0.12
      fit: 0.49
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Ethereal Staff
  - Gluttonous Grimoire
  - Shifter's Shield
  - Spear of Desolation
  - Draconic Scale
  flex_slots:
  - Spear of Desolation
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Draconic Scale, Gluttonous Grimoire, Soul Gem, Shifter''s Shield, Kinetic
    Cuirass, Amanita Charm, Freya''s Tears, Breastplate of Valor, Spear of the Magus,
    The Cosmic Horror, Shield of the Phoenix, Oni Hunter''s Garb, Death Metal, Helm
    of Radiance, Spectral Armor, Chronos'' Pendant, Erosion, Rod of Asclepius, Eye
    of Providence, Jade Scepter, Leviathan''s Hide, Screeching Gargoyle, Blood-Bound
    Book, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.55
      pick: 0.19
      fit: 0.27
    Ethereal Staff:
      total: 0.54
      efficiency: 0.52
      win: 0.7
      pick: 0.13
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.5
      efficiency: 0.52
      win: 0.58
      pick: 0.14
      fit: 0.37
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.17
      fit: 0.49
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.82
      pick: 0.12
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Ethereal Staff
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
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
    this god: Draconic Scale, Soul Gem, Amanita Charm, Gluttonous Grimoire, Shield
    of the Phoenix, Lifebinder, Rod of Asclepius, Shifter''s Shield, Kinetic Cuirass,
    Blood-Bound Book, Bancroft''s Talon, Chandra''s Grace, Freya''s Tears, Oni Hunter''s
    Garb, Breastplate of Valor, Spear of the Magus, The Cosmic Horror, Phoenix Feather,
    Helm of Radiance, Erosion, Spectral Armor, Jade Scepter, Eye of Providence, Chronos''
    Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.55
      pick: 0.19
      fit: 0.29
    Ethereal Staff:
      total: 0.56
      efficiency: 0.52
      win: 0.7
      pick: 0.13
      fit: 0.39
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.14
      fit: 0.49
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.82
      pick: 0.12
      fit: 0.49
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of Desolation
  - Draconic Scale
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Shifter''s Shield, Kinetic Cuirass,
    Spear of the Magus, Amanita Charm, The Cosmic Horror, Stone of Binding, Screeching
    Gargoyle, Freya''s Tears, Breastplate of Valor, Void Shield, Oni Hunter''s Garb,
    Shield of the Phoenix, Void Stone, Helm of Radiance, Spectral Armor, Doom Orb,
    The World Stone, Erosion, Rod of Asclepius, Dreamer''s Idol, Eye of Providence,
    Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.55
      pick: 0.19
      fit: 0.26
    Ethereal Staff:
      total: 0.55
      efficiency: 0.52
      win: 0.7
      pick: 0.13
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.17
      fit: 0.59
    Draconic Scale:
      total: 0.61
      efficiency: 0.5
      win: 0.82
      pick: 0.12
      fit: 0.41
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.55
      pick: 0.15
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
  - Draconic Scale
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Shifter''s Shield, Kinetic Cuirass, Amanita
    Charm, Breastplate of Valor, Freya''s Tears, Oni Hunter''s Garb, Spear of the
    Magus, Bracer of The Abyss, Shield of the Phoenix, The Cosmic Horror, Death Metal,
    Helm of Radiance, Spectral Armor, Blood-Bound Book, Rod of Asclepius, Bancroft''s
    Talon, Jade Scepter, Chronos'' Pendant, Bragi''s Harp, Erosion, Eye of Providence,
    Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.19
      fit: 0.18
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.47
    Ethereal Staff:
      total: 0.54
      efficiency: 0.52
      win: 0.7
      pick: 0.13
      fit: 0.2
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.82
      pick: 0.12
      fit: 0.28
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Ethereal Staff
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Soul Gem, Gluttonous
    Grimoire, Freya''s Tears, Breastplate of Valor, Shifter''s Shield, Kinetic Cuirass,
    Shield of the Phoenix, Amanita Charm, Oni Hunter''s Garb, Chronos'' Pendant, Screeching
    Gargoyle, Chandra''s Grace, Spear of the Magus, Spectral Armor, Gladiator''s Shield,
    Erosion, The Cosmic Horror, Eye of Providence, Helm of Radiance, Gem of Focus,
    Prophetic Cloak, Death Metal, Leviathan''s Hide, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.55
      pick: 0.19
      fit: 0.43
    Ethereal Staff:
      total: 0.54
      efficiency: 0.52
      win: 0.7
      pick: 0.13
      fit: 0.21
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.17
      fit: 0.53
    Draconic Scale:
      total: 0.61
      efficiency: 0.5
      win: 0.82
      pick: 0.12
      fit: 0.39
    Soul Gem:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of the Magus
  flex_slots:
  - Freya's Tears
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Amanita
    Charm, Breastplate of Valor, Freya''s Tears, Shield of the Phoenix, Spear of the
    Magus, Oni Hunter''s Garb, The Cosmic Horror, Helm of Radiance, Shifter''s Shield,
    Erosion, Eye of Providence, Spectral Armor, Rod of Asclepius, Draconic Scale,
    Jade Scepter, Chronos'' Pendant, Leviathan''s Hide, Midgardian Mail, Ethereal
    Staff, Wish-Granting Pearl, Death Metal.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.55
      pick: 0.19
      fit: 0.31
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.14
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of the Magus:
      total: 0.49
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.37
  starter: *id001
---
