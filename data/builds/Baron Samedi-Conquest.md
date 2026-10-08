---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.55
  aspect_win_rate: 0.31
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.21
    win_rate: 0.33
    alternates:
    - name: Alchemist Coat
      pick_rate: 0.14
      win_rate: 0.5
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 1.0
  - name: Breastplate of Valor
    pick_rate: 0.17
    win_rate: 0.4
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 0.33
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.14
    win_rate: 0.25
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.5
    - name: Rod of Asclepius
      pick_rate: 0.07
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.15
    win_rate: 0.25
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 1.0
  - name: Spear of the Magus
    pick_rate: 0.14
    win_rate: 0.33
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.5
    - name: Hide of the Nemean Lion
      pick_rate: 0.09
      win_rate: 0.5
  - name: Olmec Blue
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.13
      win_rate: 0.5
    - name: Circe's Hexstone
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Sands Of Time
    pick_rate: 0.17
    win_rate: 0.4
  - name: Selflessness
    pick_rate: 0.14
    win_rate: 0.75
  - name: Archmage's Gem
    pick_rate: 0.1
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-10-08'
  god_win_rate: 0.4827586206896552
  god_matches_won: 14
  god_matches_played: 29
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Freya's Tears
  - Circe's Hexstone
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Shifter''s Shield, Helm of Radiance, Rod of Asclepius, Shield of the
    Phoenix, Erosion, Eye of Providence, Draconic Scale, Stone of Binding, Chronos''
    Pendant, Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching Gargoyle, Helm
    of Darkness, The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.31
    Prophetic Cloak:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.14
      fit: 0.48
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.34
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.19
      fit: 0.48
    Circe's Hexstone:
      total: 0.58
      efficiency: 0.23
      win: 1.0
      pick: 0.18
      fit: 0.29
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Freya's Tears
  - Circe's Hexstone
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Circe's Hexstone
  - Rod of Tahuti
  - Wish-Granting Pearl
  flex_slots:
  - Rod of Tahuti
  - Wish-Granting Pearl
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Soul Gem, Helm of
    Radiance, Rod of Asclepius, Shifter''s Shield, Wish-Granting Pearl, Doom Orb,
    Ancient Signet, The World Stone, Death Metal, Chronos'' Pendant, Shield of the
    Phoenix, Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Draconic
    Scale, Triton''s Conch, Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.28
    Prophetic Cloak:
      total: 0.51
      efficiency: 0.44
      win: 0.67
      pick: 0.14
      fit: 0.33
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.24
    Circe's Hexstone:
      total: 0.57
      efficiency: 0.23
      win: 1.0
      pick: 0.18
      fit: 0.2
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.86
      win: 0.25
      pick: 0.22
      fit: 0.37
    Wish-Granting Pearl:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Circe's Hexstone
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Freya's Tears
  - Circe's Hexstone
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
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
    god: Genji''s Guard, Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass,
    Helm of Radiance, Shifter''s Shield, Shield of the Phoenix, Rod of Asclepius,
    Doom Orb, Erosion, Chronos'' Pendant, The World Stone, Screeching Gargoyle, Eye
    of Providence, Stone of Binding, Draconic Scale, Dreamer''s Idol, Jade Scepter,
    Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.27
    Prophetic Cloak:
      total: 0.52
      efficiency: 0.44
      win: 0.67
      pick: 0.14
      fit: 0.39
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.25
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.19
      fit: 0.39
    Circe's Hexstone:
      total: 0.58
      efficiency: 0.23
      win: 1.0
      pick: 0.18
      fit: 0.25
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Freya's Tears
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Circe's Hexstone
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, Soul Gem, Rod of Asclepius, Shield of
    the Phoenix, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, Shifter''s
    Shield, Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s Necklace, Erosion,
    Eye of Providence, Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Glorious Pridwen, Chronos'' Pendant, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.29
    Prophetic Cloak:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.14
      fit: 0.44
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.3
    Circe's Hexstone:
      total: 0.59
      efficiency: 0.23
      win: 1.0
      pick: 0.18
      fit: 0.33
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
  - Prophetic Cloak
  - Shell of Rebuke
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Freya's Tears
  - Gluttonous Grimoire
  - Circe's Hexstone
  flex_slots:
  - Gluttonous Grimoire
  - Freya's Tears
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
    for this god: Genji''s Guard, Gluttonous Grimoire, Amanita Charm, Soul Gem, Stone
    of Binding, Screeching Gargoyle, Kinetic Cuirass, Void Shield, Void Stone, Doom
    Orb, Helm of Radiance, Shifter''s Shield, The World Stone, Dreamer''s Idol, Rod
    of Asclepius, Shield of the Phoenix, Erosion, Eye of Providence, Draconic Scale,
    Chronos'' Pendant, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.26
    Prophetic Cloak:
      total: 0.52
      efficiency: 0.44
      win: 0.67
      pick: 0.14
      fit: 0.4
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.28
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.19
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.7
    Circe's Hexstone:
      total: 0.58
      efficiency: 0.23
      win: 1.0
      pick: 0.18
      fit: 0.24
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Freya's Tears
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Shell of Rebuke
  - Bragi's Harp
  - Circe's Hexstone
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Helm of Radiance, Shifter''s Shield, Rod of Asclepius, Bragi''s
    Harp, Shield of the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion, Chronos''
    Pendant, Daybreak Gavel, Screeching Gargoyle, Eye of Providence, Jade Scepter,
    Ancient Signet, Wish-Granting Pearl, Doom Orb, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.71
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.18
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.2
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.47
    Circe's Hexstone:
      total: 0.57
      efficiency: 0.23
      win: 1.0
      pick: 0.18
      fit: 0.17
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Freya's Tears
  - Circe's Hexstone
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Prophetic Cloak, Amanita
    Charm, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire,
    Screeching Gargoyle, Shifter''s Shield, Chronos'' Pendant, Helm of Radiance, Erosion,
    Gladiator''s Shield, Eye of Providence, Rod of Asclepius, Gem of Focus, Stone
    of Binding, Draconic Scale, Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian
    Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.75
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.43
    Prophetic Cloak:
      total: 0.55
      efficiency: 0.44
      win: 0.67
      pick: 0.14
      fit: 0.56
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.27
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.19
      fit: 0.56
    Circe's Hexstone:
      total: 0.6
      efficiency: 0.23
      win: 1.0
      pick: 0.18
      fit: 0.42
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Shell of Rebuke
  - Freya's Tears
  - Circe's Hexstone
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
    Genji''s Guard, Soul Gem, Shifter''s Shield, Helm of Radiance, Shield of the Phoenix,
    Erosion, Rod of Asclepius, Eye of Providence, Draconic Scale, Stone of Binding,
    Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching Gargoyle,
    Helm of Darkness, The World Stone, Magi''s Cloak, Midgardian Mail, Dreamer''s
    Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.13
      fit: 0.31
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.21
      fit: 0.51
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.19
      fit: 0.48
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.86
      win: 0.25
      pick: 0.22
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
  - Rod of Tahuti
  starter: *id001
---
