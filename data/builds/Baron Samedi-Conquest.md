---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.63
  aspect_win_rate: 0.42
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.67
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 0.71
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.36
    alternates:
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.67
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.17
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.57
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.17
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.8
    - name: Ethereal Staff
      pick_rate: 0.07
      win_rate: 1.0
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.25
    - name: Spear of the Magus
      pick_rate: 0.05
      win_rate: 0.33
  - name: Mote of Chaos
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: Olmec Blue
      pick_rate: 0.08
      win_rate: 0.67
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.64
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.45
  - name: Sands Of Time
    pick_rate: 0.15
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-10-09'
  god_win_rate: 0.5138888888888888
  god_matches_won: 37
  god_matches_played: 72
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-09'
  god_matches_analyzed: 2961
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Helm of Radiance
  - Ethereal Staff
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Helm of Radiance
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Soul Gem, Shifter''s
    Shield, Helm of Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye
    of Providence, Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm of Darkness, The World
    Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol, Spear of Desolation, Spear
    of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.2
      fit: 0.31
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.59
    Helm of Radiance:
      total: 0.56
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.37
    Ethereal Staff:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.45
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.24
      fit: 0.48
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Ethereal Staff
  - Freya's Tears
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Doom Orb
  - Wish-Granting Pearl
  flex_slots:
  - Wish-Granting Pearl
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Gluttonous Grimoire, Kinetic Cuirass, Soul Gem, Helm of Radiance, Shifter''s
    Shield, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet, The World
    Stone, Death Metal, Chronos'' Pendant, Shield of the Phoenix, Jade Scepter, Erosion,
    Eye of Providence, Stone of Binding, Draconic Scale, Triton''s Conch, Screeching
    Gargoyle, Daybreak Gavel, Spear of Desolation, Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.2
      fit: 0.28
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.45
    Ethereal Staff:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.39
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.24
      fit: 0.33
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.37
    Wish-Granting Pearl:
      total: 0.54
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Ethereal Staff
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Helm of Radiance
  - Ethereal Staff
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Helm of Radiance
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Helm of Radiance,
    Shifter''s Shield, Shield of the Phoenix, Doom Orb, Rod of Asclepius, Erosion,
    Chronos'' Pendant, The World Stone, Screeching Gargoyle, Eye of Providence, Stone
    of Binding, Draconic Scale, Dreamer''s Idol, Jade Scepter, Wish-Granting Pearl,
    Magi''s Cloak, Daybreak Gavel, Ancient Signet, Spear of Desolation, Spear of the
    Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.47
    Helm of Radiance:
      total: 0.55
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.27
    Ethereal Staff:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.35
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.24
      fit: 0.39
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Ethereal Staff
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Ethereal Staff, Amanita Charm, Soul Gem, Shield of the Phoenix, Rod
    of Asclepius, Gluttonous Grimoire, Kinetic Cuirass, Chandra''s Grace, Shifter''s
    Shield, Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s Necklace, Erosion,
    Eye of Providence, Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Glorious Pridwen, Chronos'' Pendant, Spear of Desolation,
    Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.2
      fit: 0.29
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.74
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.79
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.24
      fit: 0.44
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Genji's Guard
  - Ethereal Staff
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  flex_slots:
  - Screeching Gargoyle
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Soul Gem, Stone of Binding,
    Screeching Gargoyle, Kinetic Cuirass, Void Shield, Void Stone, Doom Orb, Helm
    of Radiance, Shifter''s Shield, The World Stone, Dreamer''s Idol, Shield of the
    Phoenix, Rod of Asclepius, Erosion, Eye of Providence, Draconic Scale, Chronos''
    Pendant, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Spear of Desolation,
    Spear of the Magus.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.58
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.58
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.2
      fit: 0.26
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.51
    Ethereal Staff:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.39
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.24
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Ethereal Staff
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Kinetic Cuirass,
    Helm of Radiance, Shifter''s Shield, Rod of Asclepius, Bragi''s Harp, Shield of
    the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion, Chronos'' Pendant,
    Daybreak Gavel, Screeching Gargoyle, Eye of Providence, Jade Scepter, Ancient
    Signet, Wish-Granting Pearl, Doom Orb, Draconic Scale, Spear of Desolation, Spear
    of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.2
      fit: 0.18
    Bracer of The Abyss:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.47
    Ethereal Staff:
      total: 0.66
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.3
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.24
      fit: 0.28
  community_ordered:
  - Genji's Guard
  - Ethereal Staff
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Soul Gem
  flex_slots:
  - Screeching Gargoyle
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
    Shield of the Phoenix, Gluttonous Grimoire, Screeching Gargoyle, Shifter''s Shield,
    Chronos'' Pendant, Helm of Radiance, Prophetic Cloak, Erosion, Gladiator''s Shield,
    Eye of Providence, Gem of Focus, Stone of Binding, Draconic Scale, Rod of Asclepius,
    Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord,
    Spear of Desolation, Spear of the Magus.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.2
      fit: 0.43
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.24
      fit: 0.56
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.39
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Soul Gem, Spear of the Magus, Shifter''s Shield, Helm of
    Radiance, Shield of the Phoenix, Erosion, Rod of Asclepius, Eye of Providence,
    Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting
    Pearl, Screeching Gargoyle, Helm of Darkness, The World Stone, Magi''s Cloak,
    Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.2
      fit: 0.31
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.14
      fit: 0.51
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.24
      fit: 0.48
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.86
      win: 0.25
      pick: 0.15
      fit: 0.37
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
