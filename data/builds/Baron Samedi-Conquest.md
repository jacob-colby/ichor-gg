---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.77
  aspect_win_rate: 0.52
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Lifebinder
      pick_rate: 0.13
      win_rate: 0.58
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.63
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.48
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.51
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.49
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.5
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.49
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.54
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.53
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.05
      win_rate: 0.75
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.68
  - name: Shield
    pick_rate: 0.04
    win_rate: 0.38
    alternates:
    - name: Evil Eye
      pick_rate: 0.04
      win_rate: 0.25
    - name: Draconic Scale
      pick_rate: 0.03
      win_rate: 0.71
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.43
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.68
  - name: Archmage's Gem
    pick_rate: 0.11
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-08-06'
  god_win_rate: 0.5204301075268817
  god_matches_won: 242
  god_matches_played: 465
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-06'
  god_matches_analyzed: 12483
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
  - Gluttonous Grimoire
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Ethereal Staff, Draconic Scale, Genji''s Guard, Shifter''s Shield, Gluttonous
    Grimoire, Amanita Charm, Kinetic Cuirass, Soul Gem, Eye of Providence, Freya''s
    Tears, Oni Hunter''s Garb, Breastplate of Valor, Shield of the Phoenix, Spear
    of the Magus, Obsidian Shard, Rod of Asclepius, The Cosmic Horror, Helm of Radiance,
    Erosion, Spectral Armor, Jade Scepter, Yogi''s Necklace, Chronos'' Pendant, Leviathan''s
    Hide, Wish-Granting Pearl, Death Metal.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.12
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.58
      efficiency: 0.53
      win: 0.75
      pick: 0.05
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.63
      pick: 0.11
      fit: 0.49
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.71
      pick: 0.03
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
  - Shifter's Shield
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Genji''s Guard, Draconic Scale, Gluttonous Grimoire, Shifter''s Shield, Soul
    Gem, Amanita Charm, Kinetic Cuirass, Eye of Providence, Breastplate of Valor,
    Oni Hunter''s Garb, Freya''s Tears, Spear of the Magus, Obsidian Shard, Shield
    of the Phoenix, The Cosmic Horror, Death Metal, Rod of Asclepius, Helm of Radiance,
    Spectral Armor, Yogi''s Necklace, Chronos'' Pendant, Erosion, Jade Scepter, Leviathan''s
    Hide, Screeching Gargoyle, Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.12
      fit: 0.27
    Ethereal Staff:
      total: 0.56
      efficiency: 0.53
      win: 0.75
      pick: 0.05
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.63
      pick: 0.11
      fit: 0.37
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.18
      fit: 0.49
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.71
      pick: 0.03
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
    this god: Amanita Charm, Draconic Scale, Soul Gem, Genji''s Guard, Gluttonous
    Grimoire, Shifter''s Shield, Lifebinder, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Eye of Providence, Chandra''s Grace, Oni Hunter''s Garb, Blood-Bound
    Book, Bancroft''s Talon, Breastplate of Valor, Freya''s Tears, Spear of the Magus,
    The Cosmic Horror, Phoenix Feather, Spectral Armor, Jade Scepter, Erosion, Helm
    of Radiance, Yogi''s Necklace, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.12
      fit: 0.29
    Ethereal Staff:
      total: 0.58
      efficiency: 0.53
      win: 0.75
      pick: 0.05
      fit: 0.39
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.63
      pick: 0.11
      fit: 0.49
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.71
      pick: 0.03
      fit: 0.49
    Amanita Charm:
      total: 0.57
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.49
      pick: 0.08
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Ethereal Staff
  - Gluttonous Grimoire
  - Shifter's Shield
  - Spear of Desolation
  - Draconic Scale
  flex_slots:
  - Shifter's Shield
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Genji''s Guard, Shifter''s Shield, Soul Gem,
    Amanita Charm, Kinetic Cuirass, Spear of the Magus, Obsidian Shard, Eye of Providence,
    The Cosmic Horror, Stone of Binding, Screeching Gargoyle, Oni Hunter''s Garb,
    Breastplate of Valor, Freya''s Tears, Void Shield, Shield of the Phoenix, Void
    Stone, Rod of Asclepius, Helm of Radiance, Spectral Armor, Yogi''s Necklace, Erosion,
    Dreamer''s Idol, Jade Scepter, The World Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.12
      fit: 0.26
    Ethereal Staff:
      total: 0.57
      efficiency: 0.53
      win: 0.75
      pick: 0.05
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.63
      pick: 0.11
      fit: 0.41
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.18
      fit: 0.59
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.71
      pick: 0.03
      fit: 0.41
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
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Gluttonous Grimoire, Shifter''s Shield, Amanita Charm,
    Soul Gem, Kinetic Cuirass, Eye of Providence, Oni Hunter''s Garb, Breastplate
    of Valor, Freya''s Tears, Spear of the Magus, Shield of the Phoenix, Death Metal,
    Yogi''s Necklace, Bracer of The Abyss, Rod of Asclepius, The Cosmic Horror, Helm
    of Radiance, Spectral Armor, Jade Scepter, Bragi''s Harp, Blood-Bound Book, Bancroft''s
    Talon, Chronos'' Pendant, Erosion, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.57
      pick: 0.12
      fit: 0.18
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
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
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.47
    Ethereal Staff:
      total: 0.56
      efficiency: 0.53
      win: 0.75
      pick: 0.05
      fit: 0.2
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.71
      pick: 0.03
      fit: 0.28
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Ethereal Staff
  - Shifter's Shield
  - Spear of Desolation
  - Draconic Scale
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Draconic Scale, Shifter''s
    Shield, Soul Gem, Gluttonous Grimoire, Breastplate of Valor, Freya''s Tears, Amanita
    Charm, Kinetic Cuirass, Shield of the Phoenix, Eye of Providence, Oni Hunter''s
    Garb, Chronos'' Pendant, Screeching Gargoyle, Chandra''s Grace, Spectral Armor,
    Spear of the Magus, Yogi''s Necklace, Gladiator''s Shield, Erosion, Rod of Asclepius,
    The Cosmic Horror, Helm of Radiance, Gem of Focus, Death Metal, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.12
      fit: 0.43
    Ethereal Staff:
      total: 0.56
      efficiency: 0.53
      win: 0.75
      pick: 0.05
      fit: 0.21
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.63
      pick: 0.11
      fit: 0.39
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.18
      fit: 0.53
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.71
      pick: 0.03
      fit: 0.39
    Soul Gem:
      total: 0.52
      efficiency: 0.59
      win: 0.49
      pick: 0.08
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
    Soul Gem, Genji''s Guard, Eye of Providence, Freya''s Tears, Oni Hunter''s Garb,
    Breastplate of Valor, Shield of the Phoenix, Spear of the Magus, Shifter''s Shield,
    Rod of Asclepius, The Cosmic Horror, Helm of Radiance, Erosion, Spectral Armor,
    Jade Scepter, Draconic Scale, Yogi''s Necklace, Chronos'' Pendant, Obsidian Shard,
    Leviathan''s Hide, Wish-Granting Pearl, Ethereal Staff, Death Metal.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.12
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Oni Hunter's Garb:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.32
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
  starter: *id001
---
