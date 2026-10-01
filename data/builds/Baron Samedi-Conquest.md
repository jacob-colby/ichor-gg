---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.65
  aspect_win_rate: 0.49
  slot_order:
  - name: Chronos' Pendant
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Lifebinder
      pick_rate: 0.11
      win_rate: 0.46
    - name: Chandra's Grace
      pick_rate: 0.08
      win_rate: 0.66
  - name: Shifter's Shield
    pick_rate: 0.12
    win_rate: 0.46
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.64
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.46
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.69
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.66
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.64
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.46
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.43
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.61
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.46
  - name: Rod of Tahuti
    pick_rate: 0.05
    win_rate: 0.25
    alternates:
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 0.43
    - name: Sage's Ring
      pick_rate: 0.04
      win_rate: 0.57
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.47
  - name: Archmage's Gem
    pick_rate: 0.13
    win_rate: 0.49
  - name: Conduit Gem
    pick_rate: 0.13
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-10-01'
  god_win_rate: 0.5156695156695157
  god_matches_won: 181
  god_matches_played: 351
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-10-01'
  god_matches_analyzed: 10386
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Soul Gem, Spear of the Magus, Helm of Radiance, Obsidian
    Shard, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye of Providence, Draconic
    Scale, Stone of Binding, Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching
    Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s
    Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.2
      fit: 0.31
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.46
      pick: 0.19
      fit: 0.31
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.34
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.46
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.17
      fit: 0.48
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Rod of Tahuti
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Chronos''
    Pendant, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation,
    Spear of the Magus, Soul Gem, Helm of Radiance, Obsidian Shard, Rod of Asclepius,
    Wish-Granting Pearl, Doom Orb, Ancient Signet, The World Stone, Death Metal, Shield
    of the Phoenix, Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Draconic
    Scale, Triton''s Conch, Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Chandra's Grace:
      total: 0.49
      efficiency: 0.45
      win: 0.66
      pick: 0.08
      fit: 0.2
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.2
      fit: 0.28
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.46
      pick: 0.19
      fit: 0.28
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.28
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.66
      pick: 0.17
      fit: 0.33
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.86
      win: 0.25
      pick: 0.15
      fit: 0.37
  community_ordered:
  - Chandra's Grace
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Spear of Desolation
  flex_slots:
  - Breastplate of Valor
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Chronos'' Pendant, Amanita Charm, Gluttonous Grimoire, Spear of Desolation,
    Soul Gem, Kinetic Cuirass, Spear of the Magus, Obsidian Shard, Helm of Radiance,
    Shield of the Phoenix, Doom Orb, Rod of Asclepius, Erosion, The World Stone, Screeching
    Gargoyle, Eye of Providence, Stone of Binding, Draconic Scale, Dreamer''s Idol,
    Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Ancient Signet.'
  slot_scores:
    Chandra's Grace:
      total: 0.5
      efficiency: 0.45
      win: 0.66
      pick: 0.08
      fit: 0.25
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.2
      fit: 0.27
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.46
      pick: 0.19
      fit: 0.27
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.28
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.17
      fit: 0.39
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.46
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Chandra's Grace
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Chronos' Pendant
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Chronos' Pendant
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Chandra''s Grace, Soul Gem, Chronos'' Pendant, Shield
    of the Phoenix, Rod of Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Ethereal
    Staff, Spear of Desolation, Lifebinder, Spear of the Magus, Obsidian Shard, Helm
    of Radiance, Sphere of Negation, Yogi''s Necklace, Erosion, Eye of Providence,
    Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Glorious Pridwen.'
  slot_scores:
    Chandra's Grace:
      total: 0.55
      efficiency: 0.45
      win: 0.66
      pick: 0.08
      fit: 0.63
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.2
      fit: 0.29
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.34
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.46
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.17
      fit: 0.44
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Chandra's Grace
  - Genji's Guard
  - Chronos' Pendant
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Genji's Guard
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Rod of Tahuti
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
    for this god: Chronos'' Pendant, Gluttonous Grimoire, Amanita Charm, Spear of
    Desolation, Soul Gem, Spear of the Magus, Stone of Binding, Obsidian Shard, Screeching
    Gargoyle, Kinetic Cuirass, Void Shield, Void Stone, Doom Orb, Helm of Radiance,
    The World Stone, Dreamer''s Idol, Shield of the Phoenix, Rod of Asclepius, Erosion,
    Eye of Providence, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Magi''s
    Cloak.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.28
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.2
      fit: 0.26
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.17
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.55
      win: 0.46
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.46
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.25
      pick: 0.15
      fit: 0.48
  community_ordered:
  - Chronos' Pendant
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Gluttonous Grimoire, Nimble Ring, Amanita Charm,
    Soul Gem, Kinetic Cuirass, Spear of Desolation, Spear of the Magus, Helm of Radiance,
    Obsidian Shard, Rod of Asclepius, Bragi''s Harp, Shield of the Phoenix, Bracer
    of The Abyss, Stone of Binding, Erosion, Daybreak Gavel, Screeching Gargoyle,
    Eye of Providence, Jade Scepter, Ancient Signet, Wish-Granting Pearl, Doom Orb,
    Draconic Scale.'
  slot_scores:
    Chronos' Pendant:
      total: 0.5
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.2
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.64
      pick: 0.2
      fit: 0.18
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.43
      efficiency: 0.44
      win: 0.46
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.66
      pick: 0.17
      fit: 0.28
  community_ordered:
  - Chronos' Pendant
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Spear of Desolation
  flex_slots:
  - Breastplate of Valor
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Amanita Charm,
    Spear of Desolation, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous
    Grimoire, Screeching Gargoyle, Spear of the Magus, Helm of Radiance, Obsidian
    Shard, Prophetic Cloak, Erosion, Gladiator''s Shield, Eye of Providence, Gem of
    Focus, Stone of Binding, Draconic Scale, Rod of Asclepius, Eye of Erebus, Magi''s
    Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Chandra's Grace:
      total: 0.52
      efficiency: 0.45
      win: 0.66
      pick: 0.08
      fit: 0.42
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.64
      pick: 0.2
      fit: 0.43
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.46
      pick: 0.19
      fit: 0.43
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.39
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.66
      pick: 0.17
      fit: 0.56
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.46
      pick: 0.0
      fit: 0.53
  community_ordered:
  - Chandra's Grace
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Soul Gem, Spear of the Magus, Helm of Radiance, Obsidian
    Shard, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye of Providence, Draconic
    Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.2
      fit: 0.31
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.46
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.17
      fit: 0.48
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.46
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.86
      win: 0.25
      pick: 0.15
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
