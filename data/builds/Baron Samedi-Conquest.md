---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.81
  aspect_win_rate: 0.38
  slot_order:
  - name: Daybreak Gavel
    pick_rate: 0.16
    win_rate: 0.2
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.4
    - name: Chandra's Grace
      pick_rate: 0.13
      win_rate: 0.75
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.33
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.17
    - name: Gem of Focus
      pick_rate: 0.16
      win_rate: 0.4
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.33
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.75
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.33
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.4
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.75
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.33
  - name: Spear of Desolation
    pick_rate: 0.13
    win_rate: 0.33
    alternates:
    - name: Draconic Scale
      pick_rate: 0.09
      win_rate: 0.5
    - name: Plated Metal
      pick_rate: 0.04
      win_rate: 1.0
  - name: Contagion
    pick_rate: 0.06
    win_rate: 0.0
    alternates:
    - name: Circe's Hexstone
      pick_rate: 0.06
      win_rate: 0.0
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.25
    win_rate: 0.38
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.43
  - name: Archmage's Gem
    pick_rate: 0.13
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-09-23'
  god_win_rate: 0.40625
  god_matches_won: 13
  god_matches_played: 32
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
  - Chandra's Grace
  - Shell of Rebuke
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Spear of the Magus, Helm of Radiance, Shield of the Phoenix, Erosion,
    Rod of Asclepius, Eye of Providence, Stone of Binding, Chronos'' Pendant, Jade
    Scepter, Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness,
    The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Chandra's Grace:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.13
      fit: 0.29
    Shell of Rebuke:
      total: 0.5
      efficiency: 0.28
      win: 0.75
      pick: 0.25
      fit: 0.34
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.4
      pick: 0.32
      fit: 0.48
    Spear of Desolation:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.28
      fit: 0.51
    Draconic Scale:
      total: 0.48
      efficiency: 0.5
      win: 0.5
      pick: 0.19
      fit: 0.49
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.14
      fit: 0.37
  community_ordered:
  - Chandra's Grace
  - Shell of Rebuke
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Breastplate of Valor
  - Shell of Rebuke
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of the Magus,
    Soul Gem, Helm of Radiance, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient
    Signet, The World Stone, Death Metal, Chronos'' Pendant, Shield of the Phoenix,
    Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Triton''s Conch, Screeching
    Gargoyle.'
  slot_scores:
    Chandra's Grace:
      total: 0.53
      efficiency: 0.45
      win: 0.75
      pick: 0.13
      fit: 0.2
    Genji's Guard:
      total: 0.43
      efficiency: 0.66
      win: 0.33
      pick: 0.26
      fit: 0.28
    Breastplate of Valor:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.3
      fit: 0.28
    Shell of Rebuke:
      total: 0.49
      efficiency: 0.28
      win: 0.75
      pick: 0.25
      fit: 0.24
    Draconic Scale:
      total: 0.46
      efficiency: 0.5
      win: 0.5
      pick: 0.19
      fit: 0.35
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.14
      fit: 0.37
  community_ordered:
  - Chandra's Grace
  - Genji's Guard
  - Breastplate of Valor
  - Shell of Rebuke
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chandra's Grace
  - Shell of Rebuke
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Draconic Scale
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass,
    Spear of the Magus, Helm of Radiance, Shield of the Phoenix, Doom Orb, Rod of
    Asclepius, Erosion, Chronos'' Pendant, The World Stone, Screeching Gargoyle, Eye
    of Providence, Stone of Binding, Dreamer''s Idol, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak, Ancient Signet.'
  slot_scores:
    Chandra's Grace:
      total: 0.54
      efficiency: 0.45
      win: 0.75
      pick: 0.13
      fit: 0.25
    Shell of Rebuke:
      total: 0.49
      efficiency: 0.28
      win: 0.75
      pick: 0.25
      fit: 0.25
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.4
      pick: 0.32
      fit: 0.39
    Spear of Desolation:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.28
      fit: 0.49
    Draconic Scale:
      total: 0.46
      efficiency: 0.5
      win: 0.5
      pick: 0.19
      fit: 0.37
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.14
      fit: 0.35
  community_ordered:
  - Chandra's Grace
  - Shell of Rebuke
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chandra's Grace
  - Shell of Rebuke
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Chandra''s Grace, Rod of Tahuti, Amanita Charm, Soul Gem, Shield of
    the Phoenix, Rod of Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Ethereal
    Staff, Spear of the Magus, Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s
    Necklace, Erosion, Eye of Providence, Phoenix Feather, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Glorious Pridwen, Chronos'' Pendant.'
  slot_scores:
    Chandra's Grace:
      total: 0.6
      efficiency: 0.45
      win: 0.75
      pick: 0.13
      fit: 0.63
    Shell of Rebuke:
      total: 0.49
      efficiency: 0.28
      win: 0.75
      pick: 0.25
      fit: 0.3
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.4
      pick: 0.32
      fit: 0.44
    Spear of Desolation:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.28
      fit: 0.51
    Draconic Scale:
      total: 0.48
      efficiency: 0.5
      win: 0.5
      pick: 0.19
      fit: 0.49
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Chandra's Grace
  - Shell of Rebuke
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chandra's Grace
  - Shell of Rebuke
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Amanita Charm, Soul Gem, Spear
    of the Magus, Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Void Shield,
    Void Stone, Doom Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Shield
    of the Phoenix, Rod of Asclepius, Erosion, Eye of Providence, Chronos'' Pendant,
    Jade Scepter, Wish-Granting Pearl, Magi''s Cloak.'
  slot_scores:
    Chandra's Grace:
      total: 0.54
      efficiency: 0.45
      win: 0.75
      pick: 0.13
      fit: 0.24
    Shell of Rebuke:
      total: 0.49
      efficiency: 0.28
      win: 0.75
      pick: 0.25
      fit: 0.28
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.4
      pick: 0.32
      fit: 0.4
    Spear of Desolation:
      total: 0.45
      efficiency: 0.57
      win: 0.33
      pick: 0.28
      fit: 0.59
    Draconic Scale:
      total: 0.47
      efficiency: 0.5
      win: 0.5
      pick: 0.19
      fit: 0.41
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.33
      pick: 0.14
      fit: 0.48
  community_ordered:
  - Chandra's Grace
  - Shell of Rebuke
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chandra's Grace
  - Bracer of The Abyss
  - Nimble Ring
  - Shell of Rebuke
  - Bragi's Harp
  - Draconic Scale
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Spear of the Magus, Helm of Radiance, Rod of Asclepius,
    Bragi''s Harp, Shield of the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion,
    Chronos'' Pendant, Screeching Gargoyle, Eye of Providence, Jade Scepter, Ancient
    Signet, Wish-Granting Pearl, Doom Orb.'
  slot_scores:
    Chandra's Grace:
      total: 0.53
      efficiency: 0.45
      win: 0.75
      pick: 0.13
      fit: 0.17
    Bracer of The Abyss:
      total: 0.37
      efficiency: 0.52
      win: 0.33
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.33
    Shell of Rebuke:
      total: 0.48
      efficiency: 0.28
      win: 0.75
      pick: 0.25
      fit: 0.2
    Bragi's Harp:
      total: 0.37
      efficiency: 0.44
      win: 0.33
      pick: 0.0
      fit: 0.47
    Draconic Scale:
      total: 0.45
      efficiency: 0.5
      win: 0.5
      pick: 0.19
      fit: 0.28
  community_ordered:
  - Chandra's Grace
  - Shell of Rebuke
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Breastplate of Valor
  - Shell of Rebuke
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire, Screeching Gargoyle,
    Chronos'' Pendant, Spear of the Magus, Helm of Radiance, Prophetic Cloak, Erosion,
    Gladiator''s Shield, Eye of Providence, Stone of Binding, Rod of Asclepius, Eye
    of Erebus, Magi''s Cloak, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Chandra's Grace:
      total: 0.57
      efficiency: 0.45
      win: 0.75
      pick: 0.13
      fit: 0.42
    Genji's Guard:
      total: 0.46
      efficiency: 0.66
      win: 0.33
      pick: 0.26
      fit: 0.43
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.65
      win: 0.33
      pick: 0.3
      fit: 0.43
    Shell of Rebuke:
      total: 0.49
      efficiency: 0.28
      win: 0.75
      pick: 0.25
      fit: 0.27
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.4
      pick: 0.32
      fit: 0.56
    Draconic Scale:
      total: 0.47
      efficiency: 0.5
      win: 0.5
      pick: 0.19
      fit: 0.39
  community_ordered:
  - Chandra's Grace
  - Genji's Guard
  - Breastplate of Valor
  - Shell of Rebuke
  - Freya's Tears
  - Draconic Scale
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Soul Gem, Spear of the Magus, Helm of Radiance, Shield of the Phoenix,
    Erosion, Rod of Asclepius, Eye of Providence, Stone of Binding, Chronos'' Pendant,
    Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness,
    The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.33
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.44
      efficiency: 0.66
      win: 0.33
      pick: 0.26
      fit: 0.31
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.4
      pick: 0.32
      fit: 0.48
    Spear of Desolation:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.28
      fit: 0.51
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.14
      fit: 0.37
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
