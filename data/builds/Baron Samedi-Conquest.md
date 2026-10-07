---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.63
  aspect_win_rate: 0.25
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.26
    win_rate: 0.2
    alternates:
    - name: Alchemist Coat
      pick_rate: 0.21
      win_rate: 0.5
    - name: Gauntlet of Thebes
      pick_rate: 0.05
      win_rate: 0.0
  - name: Chandra's Grace
    pick_rate: 0.16
    win_rate: 0.33
    alternates:
    - name: The World Stone
      pick_rate: 0.11
      win_rate: 0.0
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.0
  - name: Rod of Tahuti
    pick_rate: 0.11
    win_rate: 0.0
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.11
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.0
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.12
      win_rate: 1.0
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Erosion
      pick_rate: 0.08
      win_rate: 1.0
    - name: Spectral Armor
      pick_rate: 0.08
      win_rate: 0.0
  - name: Mote of Chaos
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Spectral Armor
      pick_rate: 0.11
      win_rate: 1.0
    - name: Olmec Blue
      pick_rate: 0.11
      win_rate: 0.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.16
    win_rate: 0.0
  - name: Conduit Gem
    pick_rate: 0.16
    win_rate: 0.33
  - name: Sands Of Time
    pick_rate: 0.16
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-10-07'
  god_win_rate: 0.42105263157894735
  god_matches_won: 8
  god_matches_played: 19
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Alchemist Coat
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Spectral Armor
  - Erosion
  flex_slots:
  - Alchemist Coat
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Genji''s Guard,
    Soul Gem, Spear of the Magus, Shifter''s Shield, Helm of Radiance, Shield of the
    Phoenix, Rod of Asclepius, Eye of Providence, Draconic Scale, Stone of Binding,
    Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching Gargoyle,
    Helm of Darkness, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Alchemist Coat:
      total: 0.43
      efficiency: 0.41
      win: 0.5
      pick: 0.21
      fit: 0.35
    Kinetic Cuirass:
      total: 0.4
      efficiency: 0.56
      win: 0.27
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.69
      efficiency: 0.46
      win: 1.0
      pick: 0.2
      fit: 0.45
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.32
      fit: 0.48
    Spectral Armor:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.32
    Erosion:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.49
  community_ordered:
  - Alchemist Coat
  - Ethereal Staff
  - Freya's Tears
  - Spectral Armor
  - Erosion
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Ethereal Staff
  - Rod of Tahuti
  - Wish-Granting Pearl
  - Spectral Armor
  - Erosion
  flex_slots:
  - Rod of Tahuti
  - Wish-Granting Pearl
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Genji''s Guard, Gluttonous Grimoire, Kinetic Cuirass, Spear of the Magus,
    Soul Gem, Helm of Radiance, Shifter''s Shield, Rod of Asclepius, Wish-Granting
    Pearl, Doom Orb, Ancient Signet, Death Metal, Chronos'' Pendant, Shield of the
    Phoenix, Jade Scepter, Eye of Providence, Stone of Binding, Draconic Scale, Triton''s
    Conch, Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.39
      efficiency: 0.66
      win: 0.27
      pick: 0.0
      fit: 0.28
    Ethereal Staff:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.2
      fit: 0.39
    Rod of Tahuti:
      total: 0.36
      efficiency: 0.86
      win: 0.0
      pick: 0.17
      fit: 0.37
    Wish-Granting Pearl:
      total: 0.36
      efficiency: 0.54
      win: 0.27
      pick: 0.0
      fit: 0.36
    Spectral Armor:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.23
    Erosion:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.35
  community_ordered:
  - Ethereal Staff
  - Rod of Tahuti
  - Spectral Armor
  - Erosion
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Alchemist Coat
  - Genji's Guard
  - Ethereal Staff
  - Freya's Tears
  - Spectral Armor
  - Erosion
  flex_slots:
  - Alchemist Coat
  - Genji's Guard
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
    god: Amanita Charm, Gluttonous Grimoire, Genji''s Guard, Soul Gem, Kinetic Cuirass,
    Spear of the Magus, Helm of Radiance, Shifter''s Shield, Shield of the Phoenix,
    Doom Orb, Rod of Asclepius, Chronos'' Pendant, Screeching Gargoyle, Eye of Providence,
    Stone of Binding, Draconic Scale, Dreamer''s Idol, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak, Daybreak Gavel, Ancient Signet.'
  slot_scores:
    Alchemist Coat:
      total: 0.42
      efficiency: 0.41
      win: 0.5
      pick: 0.21
      fit: 0.25
    Genji's Guard:
      total: 0.39
      efficiency: 0.66
      win: 0.27
      pick: 0.0
      fit: 0.27
    Ethereal Staff:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.2
      fit: 0.35
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.32
      fit: 0.39
    Spectral Armor:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.24
    Erosion:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.37
  community_ordered:
  - Alchemist Coat
  - Ethereal Staff
  - Freya's Tears
  - Spectral Armor
  - Erosion
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Alchemist Coat
  - Ethereal Staff
  - Freya's Tears
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Amanita Charm
  - Alchemist Coat
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    Grimoire, Kinetic Cuirass, Genji''s Guard, Spear of the Magus, Shifter''s Shield,
    Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s Necklace, Eye of Providence,
    Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Glorious Pridwen, Chronos'' Pendant.'
  slot_scores:
    Alchemist Coat:
      total: 0.44
      efficiency: 0.41
      win: 0.5
      pick: 0.21
      fit: 0.39
    Ethereal Staff:
      total: 0.74
      efficiency: 0.46
      win: 1.0
      pick: 0.2
      fit: 0.79
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.32
      fit: 0.44
    Spectral Armor:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.34
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.27
      pick: 0.0
      fit: 0.79
    Erosion:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.49
  community_ordered:
  - Alchemist Coat
  - Ethereal Staff
  - Freya's Tears
  - Spectral Armor
  - Erosion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Alchemist Coat
  - Ethereal Staff
  - Freya's Tears
  - Spear of the Magus
  - Spectral Armor
  - Erosion
  flex_slots:
  - Alchemist Coat
  - Spear of the Magus
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
    Stone of Binding, Screeching Gargoyle, Kinetic Cuirass, Genji''s Guard, Void Shield,
    Void Stone, Doom Orb, Helm of Radiance, Shifter''s Shield, Dreamer''s Idol, Shield
    of the Phoenix, Rod of Asclepius, Eye of Providence, Draconic Scale, Chronos''
    Pendant, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak.'
  slot_scores:
    Alchemist Coat:
      total: 0.42
      efficiency: 0.41
      win: 0.5
      pick: 0.21
      fit: 0.29
    Ethereal Staff:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.2
      fit: 0.39
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.32
      fit: 0.4
    Spear of the Magus:
      total: 0.4
      efficiency: 0.6
      win: 0.27
      pick: 0.0
      fit: 0.48
    Spectral Armor:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.27
    Erosion:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.41
  community_ordered:
  - Alchemist Coat
  - Ethereal Staff
  - Freya's Tears
  - Spectral Armor
  - Erosion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
  - Spectral Armor
  - Erosion
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Genji''s
    Guard, Kinetic Cuirass, Spear of the Magus, Helm of Radiance, Shifter''s Shield,
    Rod of Asclepius, Bragi''s Harp, Shield of the Phoenix, Bracer of The Abyss, Stone
    of Binding, Chronos'' Pendant, Daybreak Gavel, Screeching Gargoyle, Eye of Providence,
    Jade Scepter, Ancient Signet, Wish-Granting Pearl, Doom Orb, Draconic Scale.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.34
      efficiency: 0.52
      win: 0.27
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.4
      efficiency: 0.65
      win: 0.27
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.35
      efficiency: 0.44
      win: 0.27
      pick: 0.0
      fit: 0.47
    Ethereal Staff:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.2
      fit: 0.3
    Spectral Armor:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.19
    Erosion:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.28
  community_ordered:
  - Ethereal Staff
  - Spectral Armor
  - Erosion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Alchemist Coat
  - Genji's Guard
  - Freya's Tears
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Alchemist Coat
  - Soul Gem
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire, Screeching Gargoyle,
    Shifter''s Shield, Chronos'' Pendant, Spear of the Magus, Helm of Radiance, Prophetic
    Cloak, Gladiator''s Shield, Eye of Providence, Gem of Focus, Stone of Binding,
    Draconic Scale, Rod of Asclepius, Eye of Erebus, Magi''s Cloak, Daybreak Gavel,
    Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Alchemist Coat:
      total: 0.41
      efficiency: 0.41
      win: 0.5
      pick: 0.21
      fit: 0.21
    Genji's Guard:
      total: 0.41
      efficiency: 0.66
      win: 0.27
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.32
      fit: 0.56
    Spectral Armor:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.34
      fit: 0.25
    Erosion:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.39
    Soul Gem:
      total: 0.39
      efficiency: 0.52
      win: 0.27
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Alchemist Coat
  - Freya's Tears
  - Spectral Armor
  - Erosion
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
    Genji''s Guard, Soul Gem, Spear of the Magus, Shifter''s Shield, Helm of Radiance,
    Shield of the Phoenix, Rod of Asclepius, Eye of Providence, Draconic Scale, Stone
    of Binding, Chronos'' Pendant, Jade Scepter, Doom Orb, Wish-Granting Pearl, Screeching
    Gargoyle, Helm of Darkness, Magi''s Cloak, Midgardian Mail, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.4
      efficiency: 0.66
      win: 0.27
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.4
      efficiency: 0.56
      win: 0.27
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.38
      efficiency: 0.57
      win: 0.2
      pick: 0.26
      fit: 0.51
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.32
      fit: 0.48
    Rod of Tahuti:
      total: 0.36
      efficiency: 0.86
      win: 0.0
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.42
      efficiency: 0.65
      win: 0.27
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
