---
type: smite-build
god: Aphrodite
mode: Conquest
builds:
- source: community
  aspect: Aspect of Heartbreak
  aspect_pick_rate: 0.71
  aspect_win_rate: 0.4
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.36
    win_rate: 0.43
    alternates:
    - name: Book of Thoth
      pick_rate: 0.2
      win_rate: 0.41
    - name: Chandra's Grace
      pick_rate: 0.14
      win_rate: 0.58
  - name: Breastplate of Valor
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.23
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.33
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.55
    alternates:
    - name: Totem of Death
      pick_rate: 0.13
      win_rate: 0.55
    - name: Chronos' Pendant
      pick_rate: 0.12
      win_rate: 0.6
  - name: Rod of Tahuti
    pick_rate: 0.3
    win_rate: 0.4
    alternates:
    - name: Rod of Asclepius
      pick_rate: 0.07
      win_rate: 1.0
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.6
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.29
    - name: Spear of the Magus
      pick_rate: 0.08
      win_rate: 0.5
  - name: Killing Stone
    pick_rate: 0.09
    win_rate: 0.0
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.25
    - name: Spear of the Magus
      pick_rate: 0.09
      win_rate: 0.25
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.2
    win_rate: 0.35
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 0.36
  - name: Sands Of Time
    pick_rate: 0.17
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/aphrodite/
  last_verified: '2026-10-22'
  god_win_rate: 0.44047619047619047
  god_matches_won: 37
  god_matches_played: 84
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-22'
  god_matches_analyzed: 1760
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Chronos' Pendant
  - Freya's Tears
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Asclepius, Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous
    Grimoire, Soul Gem, Shifter''s Shield, Helm of Radiance, Obsidian Shard, Shield
    of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Stone of Binding,
    Jade Scepter, Wish-Granting Pearl, Helm of Darkness, Screeching Gargoyle, Doom
    Orb, Magi''s Cloak, The World Stone, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.32
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.15
      fit: 0.32
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.19
      fit: 0.35
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.49
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.36
    Rod of Asclepius:
      total: 0.71
      efficiency: 0.57
      win: 1.0
      pick: 0.12
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Rod of Tahuti
  - Rod of Asclepius
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Chronos' Pendant
  - Freya's Tears
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
    of Asclepius, Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass,
    Soul Gem, Helm of Radiance, Obsidian Shard, Shifter''s Shield, Wish-Granting Pearl,
    Doom Orb, Ancient Signet, The World Stone, Death Metal, Shield of the Phoenix,
    Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Triton''s
    Conch, Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.28
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.15
      fit: 0.28
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.6
      pick: 0.19
      fit: 0.28
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.49
      pick: 0.0
      fit: 0.33
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.37
    Rod of Asclepius:
      total: 0.7
      efficiency: 0.57
      win: 1.0
      pick: 0.12
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Chronos' Pendant
  - Book of Thoth
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Asclepius, Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Soul
    Gem, Kinetic Cuirass, Obsidian Shard, Helm of Radiance, Shifter''s Shield, Shield
    of the Phoenix, Doom Orb, Erosion, The World Stone, Screeching Gargoyle, Eye of
    Providence, Stone of Binding, Draconic Scale, Dreamer''s Idol, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak, Daybreak Gavel, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.51
      win: 0.41
      pick: 0.2
      fit: 0.14
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.27
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.15
      fit: 0.27
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.6
      pick: 0.19
      fit: 0.28
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.35
    Rod of Asclepius:
      total: 0.69
      efficiency: 0.57
      win: 1.0
      pick: 0.12
      fit: 0.25
  community_ordered:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Rod of Tahuti
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Genji's Guard
  - Chronos' Pendant
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
    this god: Rod of Asclepius, Amanita Charm, Soul Gem, Shield of the Phoenix, Chandra''s
    Grace, Gluttonous Grimoire, Kinetic Cuirass, Freya''s Tears, Ethereal Staff, Shifter''s
    Shield, Lifebinder, Helm of Radiance, Obsidian Shard, Sphere of Negation, Yogi''s
    Necklace, Erosion, Eye of Providence, Phoenix Feather, Draconic Scale, Jade Scepter,
    Wish-Granting Pearl, Glorious Pridwen, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.3
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.15
      fit: 0.3
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.19
      fit: 0.35
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.36
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.8
    Rod of Asclepius:
      total: 0.76
      efficiency: 0.57
      win: 1.0
      pick: 0.12
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Chronos' Pendant
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Chronos' Pendant
  - Spear of Desolation
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
    for this god: Rod of Asclepius, Gluttonous Grimoire, Amanita Charm, Soul Gem,
    Stone of Binding, Obsidian Shard, Screeching Gargoyle, Freya''s Tears, Kinetic
    Cuirass, Void Shield, Void Stone, Doom Orb, Helm of Radiance, Shifter''s Shield,
    The World Stone, Dreamer''s Idol, Shield of the Phoenix, Erosion, Eye of Providence,
    Draconic Scale, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.26
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.15
      fit: 0.26
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.43
      pick: 0.36
      fit: 0.59
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.6
      pick: 0.19
      fit: 0.28
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.48
    Rod of Asclepius:
      total: 0.7
      efficiency: 0.57
      win: 1.0
      pick: 0.12
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Chronos' Pendant
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Asclepius, Nimble Ring, Gluttonous Grimoire, Amanita Charm, Soul
    Gem, Freya''s Tears, Kinetic Cuirass, Helm of Radiance, Obsidian Shard, Shifter''s
    Shield, Bragi''s Harp, Shield of the Phoenix, Bracer of The Abyss, Stone of Binding,
    Erosion, Eye of Providence, Daybreak Gavel, Screeching Gargoyle, Jade Scepter,
    Ancient Signet, Wish-Granting Pearl, Draconic Scale, Magi''s Cloak.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.15
      fit: 0.18
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.49
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.49
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.21
    Rod of Asclepius:
      total: 0.69
      efficiency: 0.57
      win: 1.0
      pick: 0.12
      fit: 0.21
  community_ordered:
  - Breastplate of Valor
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Chronos' Pendant
  - Freya's Tears
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
    + fit + win/pick). Underrated for this god: Rod of Asclepius, Freya''s Tears,
    Amanita Charm, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle,
    Gluttonous Grimoire, Shifter''s Shield, Helm of Radiance, Prophetic Cloak, Erosion,
    Obsidian Shard, Gladiator''s Shield, Eye of Providence, Gem of Focus, Draconic
    Scale, Stone of Binding, Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian
    Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.44
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.15
      fit: 0.44
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.19
      fit: 0.39
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.49
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.21
    Rod of Asclepius:
      total: 0.69
      efficiency: 0.57
      win: 1.0
      pick: 0.12
      fit: 0.21
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Chronos' Pendant
  - Jotunn's Revenge
  - Rod of Asclepius
  flex_slots:
  - Chronos' Pendant
  - Berserker's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Asclepius, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire, Runeforged
    Hammer, Shield Splitter, Golden Blade, Soul Gem, Hydra''s Lament, Helm of Radiance,
    Obsidian Shard, Shifter''s Shield, Eye of the Storm, Heartseeker, Nimble Ring,
    Tyrfing, Lernaean Bow, Shield of the Phoenix, Bragi''s Harp, Avenging Blade, Tekko-Kagi,
    Silverbranch Bow, Erosion, Death Metal, Titan''s Bane, Eye of Providence, Stone
    of Binding, The Crusher, Draconic Scale, Jade Scepter, Doom Orb, Screeching Gargoyle,
    Toxic Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.22
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.49
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.15
      fit: 0.22
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.6
      pick: 0.19
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.49
      pick: 0.0
      fit: 0.43
    Rod of Asclepius:
      total: 0.69
      efficiency: 0.57
      win: 1.0
      pick: 0.12
      fit: 0.25
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Asclepius, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass, Soul Gem,
    Shield Splitter, Runeforged Hammer, Helm of Radiance, Obsidian Shard, Shifter''s
    Shield, Hydra''s Lament, Berserker''s Shield, Eye of the Storm, Heartseeker, Shield
    of the Phoenix, Erosion, Eye of Providence, Doom Orb, Jade Scepter, Stone of Binding,
    Draconic Scale, Death Metal, Wish-Granting Pearl, Avenging Blade, The World Stone,
    Screeching Gargoyle, Titan''s Bane, The Crusher, Ancient Signet, Magi''s Cloak,
    Dreamer''s Idol, Triton''s Conch, Helm of Darkness, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.4
      efficiency: 0.51
      win: 0.41
      pick: 0.2
      fit: 0.18
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.15
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.49
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.49
      pick: 0.0
      fit: 0.18
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.33
    Rod of Asclepius:
      total: 0.7
      efficiency: 0.57
      win: 1.0
      pick: 0.12
      fit: 0.3
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Rod of Tahuti
  - Rod of Asclepius
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
    Grimoire, Soul Gem, Shifter''s Shield, Helm of Radiance, Obsidian Shard, Shield
    of the Phoenix, Erosion, Eye of Providence, Rod of Asclepius, Draconic Scale,
    Stone of Binding, Jade Scepter, Wish-Granting Pearl, Helm of Darkness, Screeching
    Gargoyle, Doom Orb, Magi''s Cloak, The World Stone, Midgardian Mail, Mantle Of
    Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.32
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.49
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.43
      pick: 0.36
      fit: 0.5
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.49
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.4
      pick: 0.5
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
