---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.68
  aspect_win_rate: 0.56
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.16
    win_rate: 0.42
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.58
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.3
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.42
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.64
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.47
    alternates:
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.33
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.63
  - name: Rod of Tahuti
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.88
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.6
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.25
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.05
      win_rate: 0.33
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.33
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.6
  - name: Sands Of Time
    pick_rate: 0.18
    win_rate: 0.27
  - name: Bluestone Brooch
    pick_rate: 0.16
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-08-29'
  god_win_rate: 0.5126050420168067
  god_matches_won: 61
  god_matches_played: 119
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-29'
  god_matches_analyzed: 4291
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Freya''s Tears, The World Stone, Amanita Charm, Kinetic
    Cuirass, Gluttonous Grimoire, Spear of the Magus, Shifter''s Shield, Helm of Radiance,
    Obsidian Shard, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye of Providence,
    Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, Soul Gem, Magi''s Cloak, Midgardian
    Mail, Dreamer''s Idol.'
  slot_scores:
    Book of Thoth:
      total: 0.35
      efficiency: 0.51
      win: 0.3
      pick: 0.08
      fit: 0.2
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.22
      fit: 0.31
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.47
      pick: 0.18
      fit: 0.31
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.11
      fit: 0.48
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.64
      pick: 0.12
      fit: 0.37
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.13
      fit: 0.37
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - The World Stone
  - Rod of Tahuti
  - Stampede
  flex_slots:
  - Breastplate of Valor
  - Stampede
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Freya''s Tears, The World Stone, Amanita Charm, Gluttonous Grimoire,
    Kinetic Cuirass, Spear of the Magus, Helm of Radiance, Obsidian Shard, Shifter''s
    Shield, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet, Death
    Metal, Chronos'' Pendant, Shield of the Phoenix, Jade Scepter, Erosion, Eye of
    Providence, Stone of Binding, Draconic Scale, Triton''s Conch, Screeching Gargoyle,
    Daybreak Gavel, Soul Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.47
      pick: 0.22
      fit: 0.28
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.47
      pick: 0.18
      fit: 0.28
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.63
      pick: 0.11
      fit: 0.33
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.64
      pick: 0.12
      fit: 0.37
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.13
      fit: 0.37
    Stampede:
      total: 0.48
      efficiency: 0.51
      win: 0.58
      pick: 0.1
      fit: 0.23
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Freya''s Tears, The World Stone, Amanita Charm, Gluttonous
    Grimoire, Kinetic Cuirass, Spear of the Magus, Obsidian Shard, Helm of Radiance,
    Shifter''s Shield, Shield of the Phoenix, Doom Orb, Rod of Asclepius, Soul Gem,
    Erosion, Chronos'' Pendant, Screeching Gargoyle, Eye of Providence, Stone of Binding,
    Draconic Scale, Dreamer''s Idol, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak,
    Daybreak Gavel, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.34
      efficiency: 0.51
      win: 0.3
      pick: 0.08
      fit: 0.14
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.47
      pick: 0.22
      fit: 0.27
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.47
      pick: 0.18
      fit: 0.27
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.11
      fit: 0.39
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.64
      pick: 0.12
      fit: 0.35
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.13
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - The World Stone
  - Rod of Tahuti
  - Amanita Charm
  - Stampede
  flex_slots:
  - Genji's Guard
  - Stampede
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Freya''s Tears, Amanita Charm, Shield of the Phoenix,
    Rod of Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Soul Gem, Ethereal Staff,
    Spear of the Magus, Shifter''s Shield, Lifebinder, Obsidian Shard, Helm of Radiance,
    Sphere of Negation, Yogi''s Necklace, Chandra''s Grace, Erosion, Eye of Providence,
    Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Glorious Pridwen, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.22
      fit: 0.29
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.11
      fit: 0.44
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.64
      pick: 0.12
      fit: 0.37
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.13
      fit: 0.37
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.79
    Stampede:
      total: 0.5
      efficiency: 0.51
      win: 0.58
      pick: 0.1
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Rod of Tahuti, Freya''s Tears, The World Stone, Gluttonous Grimoire,
    Amanita Charm, Spear of the Magus, Stone of Binding, Obsidian Shard, Screeching
    Gargoyle, Kinetic Cuirass, Void Shield, Void Stone, Doom Orb, Helm of Radiance,
    Shifter''s Shield, Soul Gem, Dreamer''s Idol, Shield of the Phoenix, Rod of Asclepius,
    Erosion, Eye of Providence, Draconic Scale, Chronos'' Pendant, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak.'
  slot_scores:
    Book of Thoth:
      total: 0.34
      efficiency: 0.51
      win: 0.3
      pick: 0.08
      fit: 0.17
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.47
      pick: 0.22
      fit: 0.26
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.47
      pick: 0.18
      fit: 0.26
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.11
      fit: 0.4
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.64
      pick: 0.12
      fit: 0.48
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.13
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Freya''s Tears, Gluttonous Grimoire, Nimble Ring, Amanita
    Charm, Kinetic Cuirass, Spear of the Magus, Helm of Radiance, Obsidian Shard,
    Shifter''s Shield, Soul Gem, Rod of Asclepius, Bragi''s Harp, Shield of the Phoenix,
    Bracer of The Abyss, Stone of Binding, Erosion, Chronos'' Pendant, Daybreak Gavel,
    Screeching Gargoyle, Eye of Providence, Jade Scepter, Ancient Signet, Wish-Granting
    Pearl, Doom Orb, Draconic Scale.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.41
      efficiency: 0.52
      win: 0.42
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.47
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.41
      efficiency: 0.44
      win: 0.42
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.63
      pick: 0.11
      fit: 0.28
    The World Stone:
      total: 0.51
      efficiency: 0.52
      win: 0.64
      pick: 0.12
      fit: 0.22
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.13
      fit: 0.22
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - The World Stone
  - Rod of Tahuti
  - Stampede
  flex_slots:
  - The World Stone
  - Stampede
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Amanita
    Charm, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire, Screeching
    Gargoyle, Shifter''s Shield, Chronos'' Pendant, Spear of the Magus, Helm of Radiance,
    Soul Gem, Obsidian Shard, Prophetic Cloak, Erosion, Gladiator''s Shield, Eye of
    Providence, Gem of Focus, Stone of Binding, Draconic Scale, Rod of Asclepius,
    Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.22
      fit: 0.43
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.18
      fit: 0.43
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.11
      fit: 0.56
    The World Stone:
      total: 0.51
      efficiency: 0.52
      win: 0.64
      pick: 0.12
      fit: 0.23
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.13
      fit: 0.23
    Stampede:
      total: 0.48
      efficiency: 0.51
      win: 0.58
      pick: 0.1
      fit: 0.25
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Freya''s Tears, Kinetic
    Cuirass, Gluttonous Grimoire, Soul Gem, Spear of the Magus, Shifter''s Shield,
    Helm of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion, Rod of Asclepius,
    Eye of Providence, Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.22
      fit: 0.31
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.42
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.11
      fit: 0.48
    Spear of Desolation:
      total: 0.47
      efficiency: 0.57
      win: 0.42
      pick: 0.16
      fit: 0.51
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.13
      fit: 0.37
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.49
  starter: *id001
---
