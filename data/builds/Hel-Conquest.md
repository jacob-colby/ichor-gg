---
type: smite-build
god: Hel
mode: Conquest
builds:
- source: community
  aspect: Aspect of Divergence
  aspect_pick_rate: 0.33
  aspect_win_rate: 0.5
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.5
    win_rate: 0.6
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.61
    - name: Chandra's Grace
      pick_rate: 0.07
      win_rate: 0.62
  - name: Spear of Desolation
    pick_rate: 0.22
    win_rate: 0.58
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.63
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.62
  - name: Rod of Tahuti
    pick_rate: 0.29
    win_rate: 0.62
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.07
      win_rate: 0.64
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.53
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.24
      win_rate: 0.62
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.63
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.16
      win_rate: 0.62
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.59
  - name: Killing Stone
    pick_rate: 0.07
    win_rate: 0.7
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.73
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.64
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.3
    win_rate: 0.62
  - name: Sands Of Time
    pick_rate: 0.26
    win_rate: 0.58
  - name: Archmage's Gem
    pick_rate: 0.17
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/hel/
  last_verified: '2026-11-02'
  god_win_rate: 0.5903225806451613
  god_matches_won: 732
  god_matches_played: 1240
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Genji''s Guard,
    Soul Gem, Breastplate of Valor, Spear of the Magus, Shifter''s Shield, Helm of
    Radiance, Shield of the Phoenix, Chronos'' Pendant, Erosion, Lotus Sickle, Rod
    of Asclepius, Eye of Providence, Draconic Scale, Freya''s Tears, Jade Scepter,
    Stone of Binding, Doom Orb, Helm of Darkness, Wish-Granting Pearl, The World Stone,
    Screeching Gargoyle, Magi''s Cloak, Dreamer''s Idol.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.5
      win: 0.6
      pick: 0.5
      fit: 0.2
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.62
      pick: 0.45
      fit: 0.37
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.64
      pick: 0.27
      fit: 0.47
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Genji''s Guard, Gluttonous Grimoire, Breastplate of Valor, Kinetic Cuirass,
    Spear of the Magus, Soul Gem, Helm of Radiance, Lotus Sickle, Chronos'' Pendant,
    Shifter''s Shield, Rod of Asclepius, Doom Orb, Wish-Granting Pearl, The World
    Stone, Jade Scepter, Death Metal, Ancient Signet, Shield of the Phoenix, Erosion,
    Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Triton''s
    Conch, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.5
      win: 0.6
      pick: 0.5
      fit: 0.25
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.28
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.28
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.62
      pick: 0.45
      fit: 0.37
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.64
      pick: 0.27
      fit: 0.41
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Book of Thoth
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Gluttonous Grimoire, Genji''s Guard, Soul Gem, Kinetic Cuirass,
    Breastplate of Valor, Spear of the Magus, Helm of Radiance, Shifter''s Shield,
    Chronos'' Pendant, Lotus Sickle, Shield of the Phoenix, Doom Orb, Rod of Asclepius,
    Freya''s Tears, Erosion, The World Stone, Eye of Providence, Screeching Gargoyle,
    Dreamer''s Idol, Draconic Scale, Jade Scepter, Stone of Binding, Daybreak Gavel,
    Wish-Granting Pearl, Magi''s Cloak.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.5
      win: 0.6
      pick: 0.5
      fit: 0.14
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.3
      fit: 0.49
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.85
      win: 0.62
      pick: 0.45
      fit: 0.35
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.64
      pick: 0.27
      fit: 0.45
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Rod of Asclepius, Gluttonous
    Grimoire, Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Breastplate of Valor,
    Spear of the Magus, Shifter''s Shield, Lifebinder, Helm of Radiance, Chandra''s
    Grace, Yogi''s Necklace, Sphere of Negation, Erosion, Lotus Sickle, Eye of Providence,
    Jade Scepter, Phoenix Feather, Draconic Scale, Blood-Bound Book, Wish-Granting
    Pearl, Glorious Pridwen, Freya''s Tears.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.3
      fit: 0.51
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.62
      pick: 0.45
      fit: 0.37
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.64
      pick: 0.27
      fit: 0.47
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Spear of Desolation
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Soul Gem, Spear of the Magus,
    Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Genji''s Guard, Void Shield,
    Breastplate of Valor, Void Stone, Doom Orb, Helm of Radiance, The World Stone,
    Shifter''s Shield, Dreamer''s Idol, Chronos'' Pendant, Lotus Sickle, Shield of
    the Phoenix, Rod of Asclepius, Erosion, Eye of Providence, Draconic Scale, Freya''s
    Tears, Jade Scepter, Wish-Granting Pearl.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.5
      win: 0.62
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.56
      efficiency: 0.5
      win: 0.62
      pick: 0.0
      fit: 0.68
    Spear of Desolation:
      total: 0.57
      efficiency: 0.58
      win: 0.58
      pick: 0.3
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.85
      win: 0.62
      pick: 0.45
      fit: 0.48
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.64
      pick: 0.27
      fit: 0.58
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Gluttonous Grimoire
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Genji''s
    Guard, Kinetic Cuirass, Breastplate of Valor, Spear of the Magus, Helm of Radiance,
    Shifter''s Shield, Chronos'' Pendant, Lotus Sickle, Rod of Asclepius, Shield of
    the Phoenix, Bragi''s Harp, Bracer of The Abyss, Erosion, Jade Scepter, Stone
    of Binding, Daybreak Gavel, Eye of Providence, Draconic Scale, Screeching Gargoyle,
    Freya''s Tears, Doom Orb, Wish-Granting Pearl.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.62
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.62
      pick: 0.45
      fit: 0.22
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.6
      win: 0.62
      pick: 0.0
      fit: 0.46
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.64
      pick: 0.27
      fit: 0.32
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Freya''s Tears,
    Chronos'' Pendant, Gluttonous Grimoire, Lotus Sickle, Screeching Gargoyle, Shifter''s
    Shield, Spear of the Magus, Helm of Radiance, Erosion, Prophetic Cloak, Eye of
    Providence, Gladiator''s Shield, Draconic Scale, Gem of Focus, Stone of Binding,
    Rod of Asclepius, Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.6
      pick: 0.5
      fit: 0.09
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.56
      efficiency: 0.58
      win: 0.58
      pick: 0.3
      fit: 0.53
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.62
      pick: 0.45
      fit: 0.23
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Freya''s Tears, Genji''s Guard, Soul Gem, Breastplate of Valor, Spear of the Magus,
    Shifter''s Shield, Helm of Radiance, Shield of the Phoenix, Erosion, Lotus Sickle,
    Rod of Asclepius, Eye of Providence, Draconic Scale, Jade Scepter, Stone of Binding,
    Chronos'' Pendant, Doom Orb, Helm of Darkness, Wish-Granting Pearl, The World
    Stone, Screeching Gargoyle, Magi''s Cloak, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.3
      fit: 0.51
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.08
      fit: 0.48
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.62
      pick: 0.45
      fit: 0.37
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
