---
type: smite-build
god: Aphrodite
mode: Conquest
builds:
- source: community
  aspect: Aspect of Heartbreak
  aspect_pick_rate: 0.65
  aspect_win_rate: 0.46
  slot_order:
  - name: Chandra's Grace
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.2
      win_rate: 0.5
    - name: Book of Thoth
      pick_rate: 0.2
      win_rate: 0.5
  - name: Chronos' Pendant
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.67
    - name: Rod of Asclepius
      pick_rate: 0.1
      win_rate: 0.5
  - name: Spear of the Magus
    pick_rate: 0.2
    win_rate: 0.75
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.33
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 1.0
  - name: Obsidian Shard
    pick_rate: 0.26
    win_rate: 0.2
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.21
      win_rate: 0.75
    - name: Rod of Tahuti
      pick_rate: 0.21
      win_rate: 0.75
  - name: Rod of Tahuti
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Heartwood Charm
      pick_rate: 0.11
      win_rate: 1.0
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 1.0
  - name: Polynomicon
    pick_rate: 0.18
    win_rate: 1.0
    alternates:
    - name: Regrowth Striders
      pick_rate: 0.09
      win_rate: 1.0
    - name: Veve Charm
      pick_rate: 0.09
      win_rate: 0.0
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.35
    win_rate: 0.71
  - name: Sands Of Time
    pick_rate: 0.2
    win_rate: 0.75
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/aphrodite/
  last_verified: '2026-10-08'
  god_win_rate: 0.6
  god_matches_won: 12
  god_matches_played: 20
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
  - Chandra's Grace
  - Freya's Tears
  - Polynomicon
  - Rod of Tahuti
  - Heartwood Charm
  - Spear of the Magus
  flex_slots:
  - Rod of Tahuti
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire,
    Genji''s Guard, Breastplate of Valor, Soul Gem, Shifter''s Shield, Helm of Radiance,
    Shield of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Stone of Binding,
    Jade Scepter, Wish-Granting Pearl, Helm of Darkness, Screeching Gargoyle, Doom
    Orb, Magi''s Cloak, The World Stone, Midgardian Mail, Mantle Of Discord, Rod of
    Asclepius.'
  slot_scores:
    Chandra's Grace:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.25
      fit: 0.3
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.49
    Polynomicon:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.55
      fit: 0.3
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.48
      fit: 0.36
    Heartwood Charm:
      total: 0.63
      efficiency: 0.34
      win: 1.0
      pick: 0.24
      fit: 0.3
    Spear of the Magus:
      total: 0.62
      efficiency: 0.6
      win: 0.75
      pick: 0.31
      fit: 0.36
  community_ordered:
  - Chandra's Grace
  - Polynomicon
  - Rod of Tahuti
  - Heartwood Charm
  - Spear of the Magus
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Rod of Tahuti
  - Heartwood Charm
  - Spear of the Magus
  - Polynomicon
  flex_slots:
  - Rod of Tahuti
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Genji''s Guard, Breastplate of Valor, Gluttonous Grimoire, Freya''s Tears,
    Kinetic Cuirass, Soul Gem, Helm of Radiance, Shifter''s Shield, Wish-Granting
    Pearl, Doom Orb, Ancient Signet, The World Stone, Death Metal, Shield of the Phoenix,
    Jade Scepter, Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Triton''s
    Conch, Screeching Gargoyle, Daybreak Gavel, Rod of Asclepius.'
  slot_scores:
    Chandra's Grace:
      total: 0.65
      efficiency: 0.45
      win: 1.0
      pick: 0.25
      fit: 0.2
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.28
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.48
      fit: 0.37
    Heartwood Charm:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.24
      fit: 0.27
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.75
      pick: 0.31
      fit: 0.31
    Polynomicon:
      total: 0.69
      efficiency: 0.46
      win: 1.0
      pick: 0.55
      fit: 0.35
  community_ordered:
  - Chandra's Grace
  - Rod of Tahuti
  - Heartwood Charm
  - Spear of the Magus
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chandra's Grace
  - Spear of Desolation
  - Heartwood Charm
  - Polynomicon
  - Rod of Tahuti
  - Spear of the Magus
  flex_slots:
  - Rod of Tahuti
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Genji''s Guard, Soul
    Gem, Breastplate of Valor, Kinetic Cuirass, Helm of Radiance, Shifter''s Shield,
    Shield of the Phoenix, Doom Orb, Erosion, The World Stone, Screeching Gargoyle,
    Eye of Providence, Stone of Binding, Draconic Scale, Dreamer''s Idol, Jade Scepter,
    Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel, Ancient Signet, Rod of Asclepius.'
  slot_scores:
    Chandra's Grace:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.25
      fit: 0.25
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.67
      pick: 0.2
      fit: 0.49
    Heartwood Charm:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.24
      fit: 0.25
    Polynomicon:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.55
      fit: 0.24
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.48
      fit: 0.35
    Spear of the Magus:
      total: 0.62
      efficiency: 0.6
      win: 0.75
      pick: 0.31
      fit: 0.35
  community_ordered:
  - Chandra's Grace
  - Spear of Desolation
  - Heartwood Charm
  - Polynomicon
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chandra's Grace
  - Regrowth Striders
  - Polynomicon
  - Rod of Tahuti
  - Heartwood Charm
  - Spear of the Magus
  flex_slots:
  - Spear of the Magus
  - Rod of Tahuti
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Freya''s Tears, Ethereal Staff, Genji''s Guard, Breastplate of
    Valor, Shifter''s Shield, Lifebinder, Helm of Radiance, Sphere of Negation, Yogi''s
    Necklace, Erosion, Eye of Providence, Phoenix Feather, Draconic Scale, Jade Scepter,
    Wish-Granting Pearl, Glorious Pridwen, Blood-Bound Book, Rod of Asclepius.'
  slot_scores:
    Chandra's Grace:
      total: 0.72
      efficiency: 0.45
      win: 1.0
      pick: 0.25
      fit: 0.63
    Regrowth Striders:
      total: 0.67
      efficiency: 0.35
      win: 1.0
      pick: 0.28
      fit: 0.6
    Polynomicon:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.55
      fit: 0.3
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.48
      fit: 0.36
    Heartwood Charm:
      total: 0.63
      efficiency: 0.34
      win: 1.0
      pick: 0.24
      fit: 0.33
    Spear of the Magus:
      total: 0.62
      efficiency: 0.6
      win: 0.75
      pick: 0.31
      fit: 0.36
  community_ordered:
  - Chandra's Grace
  - Regrowth Striders
  - Polynomicon
  - Rod of Tahuti
  - Heartwood Charm
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chandra's Grace
  - Spear of Desolation
  - Heartwood Charm
  - Polynomicon
  - Rod of Tahuti
  - Spear of the Magus
  flex_slots:
  - Heartwood Charm
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Soul Gem, Stone of Binding,
    Screeching Gargoyle, Freya''s Tears, Kinetic Cuirass, Genji''s Guard, Breastplate
    of Valor, Void Shield, Void Stone, Doom Orb, Helm of Radiance, Shifter''s Shield,
    The World Stone, Dreamer''s Idol, Shield of the Phoenix, Erosion, Eye of Providence,
    Draconic Scale, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Rod of Asclepius.'
  slot_scores:
    Chandra's Grace:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.25
      fit: 0.24
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.67
      pick: 0.2
      fit: 0.59
    Heartwood Charm:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.24
      fit: 0.24
    Polynomicon:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.55
      fit: 0.27
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.5
      pick: 0.48
      fit: 0.48
    Spear of the Magus:
      total: 0.64
      efficiency: 0.6
      win: 0.75
      pick: 0.31
      fit: 0.48
  community_ordered:
  - Chandra's Grace
  - Spear of Desolation
  - Heartwood Charm
  - Polynomicon
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chandra's Grace
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Polynomicon
  - Heartwood Charm
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
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Amanita Charm, Soul Gem, Freya''s
    Tears, Genji''s Guard, Breastplate of Valor, Kinetic Cuirass, Helm of Radiance,
    Shifter''s Shield, Bragi''s Harp, Shield of the Phoenix, Bracer of The Abyss,
    Stone of Binding, Erosion, Eye of Providence, Daybreak Gavel, Screeching Gargoyle,
    Jade Scepter, Ancient Signet, Wish-Granting Pearl, Draconic Scale, Magi''s Cloak,
    Rod of Asclepius.'
  slot_scores:
    Chandra's Grace:
      total: 0.65
      efficiency: 0.45
      win: 1.0
      pick: 0.25
      fit: 0.17
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
      fit: 0.34
    Bragi's Harp:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.47
    Polynomicon:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.55
      fit: 0.22
    Heartwood Charm:
      total: 0.61
      efficiency: 0.34
      win: 1.0
      pick: 0.24
      fit: 0.17
  community_ordered:
  - Chandra's Grace
  - Polynomicon
  - Heartwood Charm
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chandra's Grace
  - Genji's Guard
  - Freya's Tears
  - Polynomicon
  - Heartwood Charm
  - Spear of the Magus
  flex_slots:
  - Genji's Guard
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Screeching
    Gargoyle, Gluttonous Grimoire, Shifter''s Shield, Helm of Radiance, Prophetic
    Cloak, Erosion, Gladiator''s Shield, Eye of Providence, Gem of Focus, Draconic
    Scale, Stone of Binding, Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian
    Mail, Mantle Of Discord, Rod of Asclepius.'
  slot_scores:
    Chandra's Grace:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.25
      fit: 0.42
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.58
    Polynomicon:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.55
      fit: 0.19
    Heartwood Charm:
      total: 0.64
      efficiency: 0.34
      win: 1.0
      pick: 0.24
      fit: 0.42
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.75
      pick: 0.31
      fit: 0.21
  community_ordered:
  - Chandra's Grace
  - Polynomicon
  - Heartwood Charm
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Chandra's Grace
  - Jotunn's Revenge
  - Transcendence
  - Heartwood Charm
  - Spear of the Magus
  - Polynomicon
  flex_slots:
  - Spear of the Magus
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita
    Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Shield Splitter, Golden Blade, Soul Gem, Hydra''s
    Lament, Helm of Radiance, Shifter''s Shield, Eye of the Storm, Heartseeker, Nimble
    Ring, Tyrfing, Lernaean Bow, Shield of the Phoenix, Bragi''s Harp, Avenging Blade,
    Tekko-Kagi, Silverbranch Bow, Erosion, Death Metal, Titan''s Bane, Eye of Providence,
    Stone of Binding, The Crusher, Draconic Scale, Jade Scepter, Doom Orb, Screeching
    Gargoyle, Toxic Blade, Rod of Asclepius.'
  slot_scores:
    Chandra's Grace:
      total: 0.65
      efficiency: 0.45
      win: 1.0
      pick: 0.25
      fit: 0.21
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.43
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.2
    Heartwood Charm:
      total: 0.61
      efficiency: 0.34
      win: 1.0
      pick: 0.24
      fit: 0.21
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.75
      pick: 0.31
      fit: 0.27
    Polynomicon:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.55
      fit: 0.24
  community_ordered:
  - Chandra's Grace
  - Heartwood Charm
  - Spear of the Magus
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Chandra's Grace
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartwood Charm
  - Polynomicon
  - Spear of the Magus
  flex_slots:
  - Spear of the Magus
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass, Genji''s Guard, Breastplate
    of Valor, Soul Gem, Shield Splitter, Runeforged Hammer, Helm of Radiance, Shifter''s
    Shield, Hydra''s Lament, Berserker''s Shield, Eye of the Storm, Heartseeker, Shield
    of the Phoenix, Erosion, Eye of Providence, Doom Orb, Jade Scepter, Stone of Binding,
    Draconic Scale, Death Metal, Wish-Granting Pearl, Avenging Blade, The World Stone,
    Screeching Gargoyle, Titan''s Bane, The Crusher, Ancient Signet, Magi''s Cloak,
    Dreamer''s Idol, Triton''s Conch, Helm of Darkness, Daybreak Gavel, Rod of Asclepius.'
  slot_scores:
    Chandra's Grace:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.25
      fit: 0.23
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.67
      pick: 0.2
      fit: 0.44
    Heartwood Charm:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.24
      fit: 0.23
    Polynomicon:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.55
      fit: 0.28
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.75
      pick: 0.31
      fit: 0.33
  community_ordered:
  - Chandra's Grace
  - Spear of Desolation
  - Heartwood Charm
  - Polynomicon
  - Spear of the Magus
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
    Grimoire, Genji''s Guard, Breastplate of Valor, Soul Gem, Shifter''s Shield, Helm
    of Radiance, Shield of the Phoenix, Erosion, Eye of Providence, Rod of Asclepius,
    Draconic Scale, Stone of Binding, Jade Scepter, Wish-Granting Pearl, Helm of Darkness,
    Screeching Gargoyle, Doom Orb, Magi''s Cloak, The World Stone, Midgardian Mail,
    Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.67
      pick: 0.2
      fit: 0.5
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.48
      fit: 0.36
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
