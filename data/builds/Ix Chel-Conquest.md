---
type: smite-build
god: Ix Chel
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Mother's Light
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.4
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.28
    win_rate: 0.48
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.16
      win_rate: 0.75
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.64
  - name: The World Stone
    pick_rate: 0.26
    win_rate: 0.37
    alternates:
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.4
  - name: Rod of Tahuti
    pick_rate: 0.15
    win_rate: 0.45
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.57
    - name: Chronos' Pendant
      pick_rate: 0.08
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.19
    win_rate: 0.46
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.28
      win_rate: 0.63
    - name: Ethereal Staff
      pick_rate: 0.04
      win_rate: 0.33
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.2
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.2
      win_rate: 0.5
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.57
  - name: Void Shard
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Gem of Focus
      pick_rate: 0.08
      win_rate: 1.0
    - name: Adroit Ring
      pick_rate: 0.06
      win_rate: 0.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.24
    win_rate: 0.56
  - name: Pendulum of the Ages
    pick_rate: 0.23
    win_rate: 0.59
  - name: Conduit Gem
    pick_rate: 0.18
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/ix-chel/
  last_verified: '2026-09-23'
  god_win_rate: 0.527027027027027
  god_matches_won: 39
  god_matches_played: 74
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire,
    Genji''s Guard, Breastplate of Valor, Soul Gem, Shifter''s Shield, Spear of the
    Magus, Helm of Radiance, Shield of the Phoenix, Erosion, Eye of Providence, Rod
    of Asclepius, Draconic Scale, Stone of Binding, Jade Scepter, Wish-Granting Pearl,
    Helm of Darkness, Screeching Gargoyle, Doom Orb, Magi''s Cloak, Midgardian Mail,
    Mantle Of Discord.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.58
      pick: 0.22
      fit: 0.2
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.75
      pick: 0.16
      fit: 0.35
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.48
      pick: 0.28
      fit: 0.5
    Gem of Focus:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.35
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.23
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Gem of Focus
  flex_slots:
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Genji''s Guard, Breastplate of Valor, Gluttonous Grimoire, Freya''s Tears,
    Kinetic Cuirass, Spear of the Magus, Soul Gem, Helm of Radiance, Shifter''s Shield,
    Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet, Death Metal,
    Shield of the Phoenix, Jade Scepter, Erosion, Eye of Providence, Stone of Binding,
    Draconic Scale, Triton''s Conch, Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.58
      pick: 0.22
      fit: 0.25
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.46
      pick: 0.0
      fit: 0.28
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.75
      pick: 0.16
      fit: 0.28
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.48
      pick: 0.28
      fit: 0.4
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.23
      fit: 0.37
    Gem of Focus:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.28
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Gem of Focus
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Book of Thoth
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Genji''s Guard, Soul
    Gem, Breastplate of Valor, Kinetic Cuirass, Spear of the Magus, Helm of Radiance,
    Shifter''s Shield, Shield of the Phoenix, Doom Orb, Rod of Asclepius, Erosion,
    Screeching Gargoyle, Eye of Providence, Stone of Binding, Draconic Scale, Dreamer''s
    Idol, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Ancient
    Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.58
      pick: 0.22
      fit: 0.14
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.75
      pick: 0.16
      fit: 0.28
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.48
      pick: 0.28
      fit: 0.49
    Gem of Focus:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.28
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.23
      fit: 0.35
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Gem of Focus
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Rod of Asclepius, Gluttonous
    Grimoire, Kinetic Cuirass, Freya''s Tears, Genji''s Guard, Breastplate of Valor,
    Shifter''s Shield, Lifebinder, Spear of the Magus, Helm of Radiance, Sphere of
    Negation, Yogi''s Necklace, Erosion, Chandra''s Grace, Eye of Providence, Phoenix
    Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Glorious Pridwen,
    Blood-Bound Book, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.58
      pick: 0.22
      fit: 0.2
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.75
      pick: 0.16
      fit: 0.35
    Gem of Focus:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.35
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.23
      fit: 0.36
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.52
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.9
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Gem of Focus
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Soul Gem, Spear of the Magus,
    Stone of Binding, Screeching Gargoyle, Freya''s Tears, Kinetic Cuirass, Genji''s
    Guard, Breastplate of Valor, Void Shield, Void Stone, Doom Orb, Helm of Radiance,
    Shifter''s Shield, Dreamer''s Idol, Shield of the Phoenix, Rod of Asclepius, Erosion,
    Eye of Providence, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Magi''s
    Cloak.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.58
      pick: 0.22
      fit: 0.17
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.75
      pick: 0.16
      fit: 0.28
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.48
      pick: 0.28
      fit: 0.59
    Gem of Focus:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.28
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.55
      win: 0.46
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.45
      pick: 0.23
      fit: 0.48
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Gem of Focus
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Amanita Charm, Soul Gem, Freya''s
    Tears, Genji''s Guard, Breastplate of Valor, Kinetic Cuirass, Spear of the Magus,
    Helm of Radiance, Shifter''s Shield, Rod of Asclepius, Bragi''s Harp, Shield of
    the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion, Eye of Providence,
    Daybreak Gavel, Screeching Gargoyle, Jade Scepter, Ancient Signet, Wish-Granting
    Pearl, Draconic Scale, Magi''s Cloak.'
  slot_scores:
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.55
      win: 0.75
      pick: 0.16
      fit: 0.2
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.43
      efficiency: 0.44
      win: 0.46
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.45
      pick: 0.23
      fit: 0.21
    Gem of Focus:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.2
  community_ordered:
  - Chronos' Pendant
  - Rod of Tahuti
  - Gem of Focus
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Screeching
    Gargoyle, Gluttonous Grimoire, Shifter''s Shield, Spear of the Magus, Helm of
    Radiance, Prophetic Cloak, Erosion, Gladiator''s Shield, Eye of Providence, Draconic
    Scale, Stone of Binding, Rod of Asclepius, Eye of Erebus, Magi''s Cloak, Daybreak
    Gavel, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.58
      pick: 0.22
      fit: 0.09
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.16
      fit: 0.39
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.48
      pick: 0.28
      fit: 0.52
    Gem of Focus:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.39
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.46
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.45
      pick: 0.23
      fit: 0.21
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
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
  - Genji's Guard
  - Spear of Desolation
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
    Underrated for this god: Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous
    Grimoire, Genji''s Guard, Breastplate of Valor, Soul Gem, Shifter''s Shield, Spear
    of the Magus, Helm of Radiance, Shield of the Phoenix, Erosion, Eye of Providence,
    Rod of Asclepius, Draconic Scale, Stone of Binding, Jade Scepter, Wish-Granting
    Pearl, Helm of Darkness, Screeching Gargoyle, Doom Orb, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.46
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.46
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.48
      pick: 0.28
      fit: 0.5
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.46
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.45
      pick: 0.23
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
