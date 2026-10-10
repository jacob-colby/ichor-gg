---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.65
  aspect_win_rate: 0.53
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.15
    win_rate: 0.53
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.15
      win_rate: 0.67
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.69
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.39
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.64
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.5
    - name: Ancile
      pick_rate: 0.06
      win_rate: 0.57
  - name: Stampede
    pick_rate: 0.1
    win_rate: 0.42
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.38
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.63
    alternates:
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.83
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.33
  - name: Mote of Chaos
    pick_rate: 0.06
    win_rate: 0.75
    alternates:
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.14
    win_rate: 0.47
  - name: Conduit Gem
    pick_rate: 0.12
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-10-10'
  god_win_rate: 0.5609756097560976
  god_matches_won: 69
  god_matches_played: 123
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-10'
  god_matches_analyzed: 4063
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shifter''s Shield,
    Soul Gem, Spear of the Magus, Helm of Radiance, Shield of the Phoenix, Erosion,
    Rod of Asclepius, Eye of Providence, Draconic Scale, Stone of Binding, Chronos''
    Pendant, Jade Scepter, Doom Orb, Spear of Desolation, Wish-Granting Pearl, Screeching
    Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s
    Idol, Rod of Tahuti, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.22
      fit: 0.31
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.59
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.15
      fit: 0.34
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.17
      fit: 0.48
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.64
      pick: 0.12
      fit: 0.49
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Doom Orb
  - Wish-Granting Pearl
  - Amanita Charm
  flex_slots:
  - Wish-Granting Pearl
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of the Magus, Soul Gem, Shifter''s
    Shield, Helm of Radiance, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient
    Signet, The World Stone, Death Metal, Chronos'' Pendant, Shield of the Phoenix,
    Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Rod
    of Tahuti, Triton''s Conch, Screeching Gargoyle, Spear of Desolation, Daybreak
    Gavel, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.22
      fit: 0.28
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.15
      fit: 0.24
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.17
      fit: 0.33
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.37
    Wish-Granting Pearl:
      total: 0.53
      efficiency: 0.54
      win: 0.63
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Spear of the Magus
  - Amanita Charm
  flex_slots:
  - Spear of the Magus
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Spear of the
    Magus, Shifter''s Shield, Helm of Radiance, Shield of the Phoenix, Doom Orb, Spear
    of Desolation, Rod of Asclepius, Erosion, Chronos'' Pendant, The World Stone,
    Screeching Gargoyle, Eye of Providence, Stone of Binding, Draconic Scale, Dreamer''s
    Idol, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Rod of
    Tahuti, Ancient Signet, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.22
      fit: 0.27
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.47
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.15
      fit: 0.25
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.17
      fit: 0.39
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.35
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
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
    Grimoire, Kinetic Cuirass, Ethereal Staff, Chandra''s Grace, Shifter''s Shield,
    Spear of the Magus, Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s
    Necklace, Erosion, Eye of Providence, Phoenix Feather, Draconic Scale, Jade Scepter,
    Wish-Granting Pearl, Blood-Bound Book, Glorious Pridwen, Chronos'' Pendant, Spear
    of Desolation, Rod of Tahuti, Obsidian Shard.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.59
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.15
      fit: 0.3
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.17
      fit: 0.44
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.64
      pick: 0.12
      fit: 0.49
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Shell of Rebuke
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of the Magus
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
    Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Shifter''s Shield, Void
    Shield, Void Stone, Doom Orb, Helm of Radiance, The World Stone, Spear of Desolation,
    Dreamer''s Idol, Shield of the Phoenix, Rod of Tahuti, Rod of Asclepius, Erosion,
    Eye of Providence, Draconic Scale, Chronos'' Pendant, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak, Obsidian Shard.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.68
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.15
      fit: 0.28
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.17
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.55
      win: 0.63
      pick: 0.0
      fit: 0.7
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Shell of Rebuke
  - Bragi's Harp
  - Freya's Tears
  - Gluttonous Grimoire
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
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Kinetic Cuirass,
    Shifter''s Shield, Spear of the Magus, Helm of Radiance, Rod of Asclepius, Bragi''s
    Harp, Shield of the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion, Chronos''
    Pendant, Daybreak Gavel, Screeching Gargoyle, Eye of Providence, Jade Scepter,
    Ancient Signet, Wish-Granting Pearl, Doom Orb, Draconic Scale, Spear of Desolation,
    Rod of Tahuti, Obsidian Shard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.33
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.15
      fit: 0.2
    Bragi's Harp:
      total: 0.51
      efficiency: 0.44
      win: 0.63
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.63
      pick: 0.17
      fit: 0.28
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Soul Gem, Kinetic Cuirass,
    Shield of the Phoenix, Shifter''s Shield, Gluttonous Grimoire, Screeching Gargoyle,
    Chronos'' Pendant, Spear of the Magus, Spear of Desolation, Helm of Radiance,
    Prophetic Cloak, Erosion, Gladiator''s Shield, Eye of Providence, Gem of Focus,
    Stone of Binding, Draconic Scale, Rod of Asclepius, Eye of Erebus, Magi''s Cloak,
    Daybreak Gavel, Midgardian Mail, Mantle Of Discord, Rod of Tahuti, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.59
      pick: 0.22
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.49
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.15
      fit: 0.27
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.17
      fit: 0.56
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.64
      pick: 0.12
      fit: 0.39
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Spear of Desolation, Soul Gem, Spear of the Magus, Shifter''s Shield,
    Helm of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion, Rod of Asclepius,
    Eye of Providence, Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.22
      fit: 0.31
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.17
      fit: 0.48
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.15
      fit: 0.51
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.13
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
