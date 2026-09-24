---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.75
  aspect_win_rate: 0.47
  slot_order:
  - name: Chandra's Grace
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Lifebinder
      pick_rate: 0.14
      win_rate: 0.5
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.5
  - name: Shifter's Shield
    pick_rate: 0.15
    win_rate: 0.36
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.33
    - name: Gem of Focus
      pick_rate: 0.08
      win_rate: 0.5
  - name: Breastplate of Valor
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.75
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.55
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.33
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.57
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.5
    - name: Spear of Desolation
      pick_rate: 0.07
      win_rate: 0.25
  - name: Medallion
    pick_rate: 0.05
    win_rate: 1.0
    alternates:
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.0
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.44
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.45
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-09-24'
  god_win_rate: 0.4794520547945205
  god_matches_won: 35
  god_matches_played: 73
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
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
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Spear of the Magus, Helm of Radiance, Shield of the Phoenix, Erosion,
    Rod of Asclepius, Eye of Providence, Draconic Scale, Stone of Binding, Chronos''
    Pendant, Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm
    of Darkness, The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.2
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.31
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.26
      fit: 0.31
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.48
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of the Magus,
    Soul Gem, Helm of Radiance, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient
    Signet, The World Stone, Death Metal, Chronos'' Pendant, Shield of the Phoenix,
    Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Triton''s
    Conch, Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.28
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.26
      fit: 0.28
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.33
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass,
    Spear of the Magus, Helm of Radiance, Shield of the Phoenix, Doom Orb, Rod of
    Asclepius, Erosion, Chronos'' Pendant, The World Stone, Screeching Gargoyle, Eye
    of Providence, Stone of Binding, Draconic Scale, Dreamer''s Idol, Jade Scepter,
    Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.14
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.27
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.26
      fit: 0.27
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.39
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.35
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Soul Gem, Chandra''s Grace, Shield of
    the Phoenix, Rod of Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Ethereal
    Staff, Lifebinder, Spear of the Magus, Helm of Radiance, Sphere of Negation, Yogi''s
    Necklace, Erosion, Eye of Providence, Phoenix Feather, Draconic Scale, Jade Scepter,
    Wish-Granting Pearl, Blood-Bound Book, Glorious Pridwen, Chronos'' Pendant.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.29
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.44
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Spear of the Magus
  - Stone of Binding
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Amanita Charm, Soul Gem, Spear
    of the Magus, Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Void Shield,
    Void Stone, Doom Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Shield
    of the Phoenix, Rod of Asclepius, Erosion, Eye of Providence, Draconic Scale,
    Chronos'' Pendant, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.26
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Genji's Guard
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Rod of Tahuti
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
    this god: Rod of Tahuti, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Spear of the Magus, Helm of Radiance, Rod of Asclepius,
    Bragi''s Harp, Shield of the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion,
    Chronos'' Pendant, Daybreak Gavel, Screeching Gargoyle, Eye of Providence, Jade
    Scepter, Ancient Signet, Wish-Granting Pearl, Doom Orb, Draconic Scale.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.28
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.18
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.28
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.22
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire, Screeching Gargoyle,
    Chronos'' Pendant, Spear of the Magus, Helm of Radiance, Prophetic Cloak, Gem
    of Focus, Erosion, Gladiator''s Shield, Eye of Providence, Stone of Binding, Draconic
    Scale, Rod of Asclepius, Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian
    Mail, Mantle Of Discord.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.43
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.26
      fit: 0.43
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.56
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Soul Gem, Spear of the Magus, Helm of Radiance, Shield of the Phoenix,
    Erosion, Rod of Asclepius, Eye of Providence, Draconic Scale, Stone of Binding,
    Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching Gargoyle,
    Helm of Darkness, The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s
    Idol.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.31
    Spear of Desolation:
      total: 0.4
      efficiency: 0.57
      win: 0.25
      pick: 0.15
      fit: 0.51
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.48
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  starter: *id001
---
