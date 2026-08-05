---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.75
  aspect_win_rate: 0.54
  slot_order:
  - name: Lifebinder
    pick_rate: 0.14
    win_rate: 0.54
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.74
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.86
  - name: Breastplate of Valor
    pick_rate: 0.17
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.77
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.54
  - name: Ethereal Staff
    pick_rate: 0.11
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.53
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.73
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.5
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.63
  - name: Dwarven Plate
    pick_rate: 0.05
    win_rate: 0.25
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.67
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-08-01'
  god_win_rate: 0.5433526011560693
  god_matches_won: 94
  god_matches_played: 173
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - Shifter's Shield
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Spear of Desolation, Gluttonous Grimoire, Amanita
    Charm, Kinetic Cuirass, Soul Gem, Eye of Providence, Ethereal Staff, Freya''s
    Tears, Oni Hunter''s Garb, Shield of the Phoenix, Spear of the Magus, Rod of Asclepius,
    The Cosmic Horror, Helm of Radiance, Erosion, Spectral Armor, Jade Scepter, Draconic
    Scale, Obsidian Shard, Yogi''s Necklace, Chronos'' Pendant, Leviathan''s Hide,
    Midgardian Mail, Death Metal.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.2
      fit: 0.31
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.54
      win: 0.75
      pick: 0.05
      fit: 0.32
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shifter's Shield:
      total: 0.66
      efficiency: 0.56
      win: 0.86
      pick: 0.12
      fit: 0.49
    Spear of Desolation:
      total: 0.6
      efficiency: 0.54
      win: 0.74
      pick: 0.13
      fit: 0.51
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.45
      win: 0.73
      pick: 0.09
      fit: 0.37
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - Shifter's Shield
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Rod of Tahuti
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Shifter''s Shield, Spear of Desolation, Gluttonous Grimoire, Soul Gem, Amanita
    Charm, Kinetic Cuirass, Eye of Providence, Freya''s Tears, Spear of the Magus,
    Oni Hunter''s Garb, The Cosmic Horror, Shield of the Phoenix, Death Metal, Obsidian
    Shard, Rod of Asclepius, Helm of Radiance, Spectral Armor, Yogi''s Necklace, Erosion,
    Chronos'' Pendant, Jade Scepter, Draconic Scale, Leviathan''s Hide, Screeching
    Gargoyle, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.2
      fit: 0.27
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.54
      win: 0.75
      pick: 0.05
      fit: 0.24
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.64
      efficiency: 0.56
      win: 0.86
      pick: 0.12
      fit: 0.37
    Spear of Desolation:
      total: 0.6
      efficiency: 0.54
      win: 0.74
      pick: 0.13
      fit: 0.49
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.45
      win: 0.73
      pick: 0.09
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Shifter''s Shield, Spear of Desolation, Amanita Charm, Soul Gem, Gluttonous
    Grimoire, Shield of the Phoenix, Rod of Asclepius, Lifebinder, Kinetic Cuirass,
    Eye of Providence, Chandra''s Grace, Blood-Bound Book, Oni Hunter''s Garb, Bancroft''s
    Talon, Freya''s Tears, Spear of the Magus, The Cosmic Horror, Phoenix Feather,
    Spectral Armor, Erosion, Jade Scepter, Helm of Radiance, Yogi''s Necklace, Draconic
    Scale, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.2
      fit: 0.29
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.54
      win: 0.75
      pick: 0.05
      fit: 0.34
    Shifter's Shield:
      total: 0.66
      efficiency: 0.56
      win: 0.86
      pick: 0.12
      fit: 0.49
    Spear of Desolation:
      total: 0.6
      efficiency: 0.54
      win: 0.74
      pick: 0.13
      fit: 0.51
    Amanita Charm:
      total: 0.58
      efficiency: 0.67
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
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - Shifter's Shield
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Rod of Tahuti
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Shifter''s Shield, Spear of Desolation, Gluttonous Grimoire, Soul
    Gem, Amanita Charm, Kinetic Cuirass, Spear of the Magus, Eye of Providence, The
    Cosmic Horror, Screeching Gargoyle, Stone of Binding, Oni Hunter''s Garb, Freya''s
    Tears, Obsidian Shard, Void Shield, Shield of the Phoenix, Void Stone, Rod of
    Asclepius, Helm of Radiance, Spectral Armor, Erosion, The World Stone, Doom Orb,
    Yogi''s Necklace, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.2
      fit: 0.26
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.54
      win: 0.75
      pick: 0.05
      fit: 0.27
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shifter's Shield:
      total: 0.65
      efficiency: 0.56
      win: 0.86
      pick: 0.12
      fit: 0.41
    Spear of Desolation:
      total: 0.62
      efficiency: 0.54
      win: 0.74
      pick: 0.13
      fit: 0.59
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.45
      win: 0.73
      pick: 0.09
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of Desolation
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Shifter''s Shield, Spear of Desolation, Gluttonous Grimoire, Soul Gem,
    Amanita Charm, Kinetic Cuirass, Eye of Providence, Oni Hunter''s Garb, Freya''s
    Tears, Spear of the Magus, Shield of the Phoenix, Bracer of The Abyss, Death Metal,
    Rod of Asclepius, Yogi''s Necklace, The Cosmic Horror, Helm of Radiance, Spectral
    Armor, Bragi''s Harp, Blood-Bound Book, Jade Scepter, Bancroft''s Talon, Erosion,
    Obsidian Shard, Chronos'' Pendant.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.54
      win: 0.75
      pick: 0.05
      fit: 0.19
    Shifter's Shield:
      total: 0.63
      efficiency: 0.56
      win: 0.86
      pick: 0.12
      fit: 0.28
    Spear of Desolation:
      total: 0.57
      efficiency: 0.54
      win: 0.74
      pick: 0.13
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Spear of Desolation,
    Soul Gem, Gluttonous Grimoire, Freya''s Tears, Amanita Charm, Kinetic Cuirass,
    Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb, Chronos'' Pendant,
    Screeching Gargoyle, Chandra''s Grace, Spear of the Magus, Spectral Armor, Gladiator''s
    Shield, Erosion, Yogi''s Necklace, Rod of Asclepius, The Cosmic Horror, Helm of
    Radiance, Gem of Focus, Prophetic Cloak, Death Metal, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.2
      fit: 0.43
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.17
      fit: 0.43
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.54
      win: 0.75
      pick: 0.05
      fit: 0.25
    Shifter's Shield:
      total: 0.65
      efficiency: 0.56
      win: 0.86
      pick: 0.12
      fit: 0.39
    Spear of Desolation:
      total: 0.61
      efficiency: 0.54
      win: 0.74
      pick: 0.13
      fit: 0.53
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Freya's Tears
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass,
    Soul Gem, Eye of Providence, Freya''s Tears, Oni Hunter''s Garb, Shield of the
    Phoenix, Spear of the Magus, Shifter''s Shield, Spear of Desolation, Rod of Asclepius,
    The Cosmic Horror, Helm of Radiance, Erosion, Spectral Armor, Jade Scepter, Draconic
    Scale, Yogi''s Necklace, Chronos'' Pendant, Obsidian Shard, Leviathan''s Hide,
    Ethereal Staff, Midgardian Mail, Death Metal.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.2
      fit: 0.31
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.59
    Oni Hunter's Garb:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.32
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.06
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
---
