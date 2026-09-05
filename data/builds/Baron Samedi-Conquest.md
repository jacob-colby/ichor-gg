---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.72
  aspect_win_rate: 0.55
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.2
    win_rate: 0.59
    alternates:
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.64
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.43
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.54
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.43
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.57
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.42
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.42
    - name: Soul Gem
      pick_rate: 0.06
      win_rate: 0.47
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.59
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.54
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.58
  - name: Freya's Tears
    pick_rate: 0.05
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.44
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.5
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.3
    alternates:
    - name: Medallion
      pick_rate: 0.04
      win_rate: 0.71
    - name: Blinking Abyss
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.54
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.53
  - name: Sands Of Time
    pick_rate: 0.14
    win_rate: 0.39
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-09-05'
  god_win_rate: 0.5284090909090909
  god_matches_won: 186
  god_matches_played: 352
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-05'
  god_matches_analyzed: 13197
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of the Magus, Helm of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion,
    Rod of Asclepius, Eye of Providence, Draconic Scale, Stone of Binding, The World
    Stone, Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching
    Gargoyle, Helm of Darkness, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol, Soul
    Gem, Breastplate of Valor, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.2
      fit: 0.31
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.11
      fit: 0.48
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.2
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.59
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Charm, Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass, Spear of the Magus,
    Helm of Radiance, Obsidian Shard, The World Stone, Rod of Asclepius, Wish-Granting
    Pearl, Doom Orb, Ancient Signet, Death Metal, Chronos'' Pendant, Shield of the
    Phoenix, Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Draconic
    Scale, Triton''s Conch, Screeching Gargoyle, Daybreak Gavel, Soul Gem, Breastplate
    of Valor, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.2
      fit: 0.28
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.11
      fit: 0.33
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.59
      pick: 0.2
      fit: 0.4
    The World Stone:
      total: 0.5
      efficiency: 0.52
      win: 0.57
      pick: 0.12
      fit: 0.37
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.59
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass, Spear
    of the Magus, Obsidian Shard, Helm of Radiance, Shield of the Phoenix, The World
    Stone, Doom Orb, Rod of Asclepius, Erosion, Chronos'' Pendant, Screeching Gargoyle,
    Eye of Providence, Stone of Binding, Draconic Scale, Dreamer''s Idol, Soul Gem,
    Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Ancient Signet,
    Breastplate of Valor, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.47
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.2
      fit: 0.27
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.11
      fit: 0.39
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.2
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.59
      pick: 0.22
      fit: 0.35
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Gluttonous Grimoire,
    Freya''s Tears, Kinetic Cuirass, Ethereal Staff, Soul Gem, Spear of the Magus,
    Lifebinder, Obsidian Shard, Helm of Radiance, Sphere of Negation, Yogi''s Necklace,
    Chandra''s Grace, Erosion, Eye of Providence, Phoenix Feather, Draconic Scale,
    Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Glorious Pridwen, Chronos''
    Pendant, Breastplate of Valor, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.59
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.11
      fit: 0.44
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.2
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.59
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Gluttonous Grimoire, Amanita Charm, Spear of the Magus, Stone of
    Binding, Freya''s Tears, Obsidian Shard, Screeching Gargoyle, Kinetic Cuirass,
    Void Shield, Void Stone, The World Stone, Doom Orb, Helm of Radiance, Dreamer''s
    Idol, Soul Gem, Shield of the Phoenix, Rod of Asclepius, Erosion, Eye of Providence,
    Draconic Scale, Chronos'' Pendant, Jade Scepter, Wish-Granting Pearl, Magi''s
    Cloak, Breastplate of Valor, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.68
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.11
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.59
      pick: 0.2
      fit: 0.59
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.59
      pick: 0.22
      fit: 0.48
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Freya''s Tears, Kinetic
    Cuirass, Spear of the Magus, Helm of Radiance, Obsidian Shard, Rod of Asclepius,
    Soul Gem, Bragi''s Harp, Shield of the Phoenix, Bracer of The Abyss, Stone of
    Binding, Erosion, Chronos'' Pendant, Daybreak Gavel, Screeching Gargoyle, Eye
    of Providence, Jade Scepter, Ancient Signet, Wish-Granting Pearl, Doom Orb, Draconic
    Scale, Breastplate of Valor, Shifter''s Shield.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.59
      pick: 0.2
      fit: 0.3
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.59
      pick: 0.22
      fit: 0.22
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Gluttonous Grimoire, Screeching Gargoyle, Chronos''
    Pendant, Spear of the Magus, Helm of Radiance, Obsidian Shard, Prophetic Cloak,
    Erosion, Gladiator''s Shield, Eye of Providence, Soul Gem, Gem of Focus, Stone
    of Binding, Draconic Scale, Breastplate of Valor, Rod of Asclepius, Eye of Erebus,
    Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord, Shifter''s
    Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.2
      fit: 0.43
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.11
      fit: 0.56
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.2
      fit: 0.53
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.59
      pick: 0.22
      fit: 0.23
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
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
    Underrated for this god: Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Spear of the Magus, Shifter''s Shield,
    Helm of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion, Rod of Asclepius,
    Eye of Providence, Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.2
      fit: 0.31
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.11
      fit: 0.48
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.2
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.59
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
