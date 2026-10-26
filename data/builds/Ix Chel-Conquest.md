---
type: smite-build
god: Ix Chel
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Mother's Light
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.33
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.49
    win_rate: 0.59
    alternates:
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.56
    - name: The World Stone
      pick_rate: 0.08
      win_rate: 0.38
  - name: The World Stone
    pick_rate: 0.36
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.27
    win_rate: 0.51
    alternates:
    - name: Soul Gem
      pick_rate: 0.16
      win_rate: 0.54
    - name: The World Stone
      pick_rate: 0.1
      win_rate: 0.63
  - name: Obsidian Shard
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.35
      win_rate: 0.69
    - name: Spear of the Magus
      pick_rate: 0.05
      win_rate: 0.63
  - name: Spear of the Magus
    pick_rate: 0.08
    win_rate: 0.7
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.15
      win_rate: 0.58
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.42
  - name: Dreamer's Idol
    pick_rate: 0.09
    win_rate: 0.71
    alternates:
    - name: Spear of the Magus
      pick_rate: 0.06
      win_rate: 0.8
    - name: Ring of Dispel
      pick_rate: 0.06
      win_rate: 0.4
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.38
    win_rate: 0.66
  - name: Sands Of Time
    pick_rate: 0.2
    win_rate: 0.27
  - name: Archmage's Gem
    pick_rate: 0.16
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/ix-chel/
  last_verified: '2026-10-26'
  god_win_rate: 0.5119047619047619
  god_matches_won: 86
  god_matches_played: 168
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-26'
  god_matches_analyzed: 6194
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire,
    Genji''s Guard, Breastplate of Valor, Shifter''s Shield, Helm of Radiance, Shield
    of the Phoenix, Erosion, Eye of Providence, Rod of Asclepius, Draconic Scale,
    Stone of Binding, Chronos'' Pendant, Jade Scepter, Wish-Granting Pearl, Helm of
    Darkness, Screeching Gargoyle, Doom Orb, Magi''s Cloak, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.59
      pick: 0.49
      fit: 0.5
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.36
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.7
      pick: 0.17
      fit: 0.36
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Genji''s Guard, Breastplate of Valor, Gluttonous Grimoire, Freya''s Tears,
    Kinetic Cuirass, Helm of Radiance, Shifter''s Shield, Rod of Asclepius, Wish-Granting
    Pearl, Doom Orb, Ancient Signet, Death Metal, Chronos'' Pendant, Shield of the
    Phoenix, Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Draconic
    Scale, Triton''s Conch, Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.28
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.49
      fit: 0.4
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.28
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.37
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.7
      pick: 0.17
      fit: 0.31
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.31
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Kinetic Cuirass, Helm of Radiance, Shifter''s Shield, Shield of the
    Phoenix, Doom Orb, Rod of Asclepius, Erosion, Chronos'' Pendant, Screeching Gargoyle,
    Eye of Providence, Stone of Binding, Draconic Scale, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak, Daybreak Gavel, Ancient Signet.'
  slot_scores:
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.49
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.35
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.7
      pick: 0.17
      fit: 0.35
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.35
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Dreamer's Idol
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
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Gluttonous Grimoire,
    Kinetic Cuirass, Freya''s Tears, Ethereal Staff, Genji''s Guard, Breastplate of
    Valor, Shifter''s Shield, Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s
    Necklace, Erosion, Chandra''s Grace, Eye of Providence, Phoenix Feather, Draconic
    Scale, Jade Scepter, Wish-Granting Pearl, Glorious Pridwen, Blood-Bound Book,
    Chronos'' Pendant.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.59
      pick: 0.49
      fit: 0.5
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.7
      pick: 0.17
      fit: 0.36
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.36
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.36
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.54
      pick: 0.25
      fit: 0.9
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Soul Gem
  - Stone of Binding
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Stone of Binding, Screeching
    Gargoyle, Freya''s Tears, Kinetic Cuirass, Genji''s Guard, Breastplate of Valor,
    Void Shield, Void Stone, Doom Orb, Helm of Radiance, Shifter''s Shield, Shield
    of the Phoenix, Rod of Asclepius, Erosion, Eye of Providence, Draconic Scale,
    Chronos'' Pendant, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.68
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.59
      pick: 0.49
      fit: 0.59
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.48
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.7
      pick: 0.17
      fit: 0.48
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.54
      pick: 0.25
      fit: 0.69
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.48
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
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
    this god: Nimble Ring, Gluttonous Grimoire, Amanita Charm, Freya''s Tears, Genji''s
    Guard, Breastplate of Valor, Kinetic Cuirass, Helm of Radiance, Shifter''s Shield,
    Rod of Asclepius, Bragi''s Harp, Shield of the Phoenix, Bracer of The Abyss, Stone
    of Binding, Erosion, Chronos'' Pendant, Eye of Providence, Daybreak Gavel, Screeching
    Gargoyle, Jade Scepter, Ancient Signet, Wish-Granting Pearl, Draconic Scale, Magi''s
    Cloak.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.21
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.7
      pick: 0.17
      fit: 0.21
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.21
  community_ordered:
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  flex_slots:
  - Dreamer's Idol
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle,
    Gluttonous Grimoire, Shifter''s Shield, Chronos'' Pendant, Helm of Radiance, Prophetic
    Cloak, Erosion, Gladiator''s Shield, Eye of Providence, Gem of Focus, Draconic
    Scale, Stone of Binding, Rod of Asclepius, Eye of Erebus, Magi''s Cloak, Daybreak
    Gavel, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.59
      pick: 0.49
      fit: 0.52
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.21
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.7
      pick: 0.17
      fit: 0.21
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.21
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
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
    Grimoire, Genji''s Guard, Breastplate of Valor, Shifter''s Shield, Helm of Radiance,
    Shield of the Phoenix, Erosion, Eye of Providence, Rod of Asclepius, Draconic
    Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter, Wish-Granting Pearl,
    Helm of Darkness, Screeching Gargoyle, Doom Orb, Magi''s Cloak, Midgardian Mail,
    Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.59
      pick: 0.49
      fit: 0.5
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.51
      pick: 0.42
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
