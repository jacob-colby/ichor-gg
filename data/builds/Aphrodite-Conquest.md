---
type: smite-build
god: Aphrodite
mode: Conquest
builds:
- source: community
  aspect: Aspect of Heartbreak
  aspect_pick_rate: 0.76
  aspect_win_rate: 0.47
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.38
    win_rate: 0.49
    alternates:
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.45
    - name: Chandra's Grace
      pick_rate: 0.11
      win_rate: 0.53
  - name: The Cosmic Horror
    pick_rate: 0.14
    win_rate: 0.4
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.48
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.4
  - name: Totem of Death
    pick_rate: 0.15
    win_rate: 0.46
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.56
  - name: Rod of Tahuti
    pick_rate: 0.29
    win_rate: 0.53
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.62
    - name: Rod of Asclepius
      pick_rate: 0.06
      win_rate: 0.8
  - name: Spear of the Magus
    pick_rate: 0.11
    win_rate: 0.63
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.43
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.42
  - name: Blinking Abyss
    pick_rate: 0.12
    win_rate: 0.64
    alternates:
    - name: Spear of the Magus
      pick_rate: 0.08
      win_rate: 0.29
    - name: Killing Stone
      pick_rate: 0.07
      win_rate: 0.33
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.47
  - name: Sands Of Time
    pick_rate: 0.18
    win_rate: 0.5
  - name: Pendulum of the Ages
    pick_rate: 0.16
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/aphrodite/
  last_verified: '2026-10-24'
  god_win_rate: 0.4887640449438202
  god_matches_won: 87
  god_matches_played: 178
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-24'
  god_matches_analyzed: 3785
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Asclepius, Genji''s Guard, Amanita Charm, Freya''s Tears, Kinetic
    Cuirass, Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Shifter''s Shield,
    Helm of Radiance, Shield of the Phoenix, Erosion, Eye of Providence, Draconic
    Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter, Wish-Granting Pearl,
    Helm of Darkness, Screeching Gargoyle, Doom Orb, Magi''s Cloak, The World Stone,
    Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.14
      fit: 0.32
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.48
      fit: 0.36
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.24
      fit: 0.36
    Rod of Asclepius:
      total: 0.62
      efficiency: 0.57
      win: 0.8
      pick: 0.1
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  flex_slots:
  - Spear of Desolation
  - Breastplate of Valor
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Asclepius, Genji''s Guard, Amanita Charm, Breastplate of Valor, Gluttonous
    Grimoire, Freya''s Tears, Kinetic Cuirass, Soul Gem, Helm of Radiance, Shifter''s
    Shield, Wish-Granting Pearl, Doom Orb, Ancient Signet, The World Stone, Death
    Metal, Chronos'' Pendant, Shield of the Phoenix, Jade Scepter, Erosion, Eye of
    Providence, Stone of Binding, Draconic Scale, Triton''s Conch, Screeching Gargoyle,
    Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.14
      fit: 0.28
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.28
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.38
      fit: 0.4
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.48
      fit: 0.37
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.24
      fit: 0.31
    Rod of Asclepius:
      total: 0.61
      efficiency: 0.57
      win: 0.8
      pick: 0.1
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Asclepius, Genji''s Guard, Amanita Charm, Gluttonous Grimoire, Freya''s
    Tears, Soul Gem, Breastplate of Valor, Kinetic Cuirass, Helm of Radiance, Shifter''s
    Shield, Shield of the Phoenix, Doom Orb, Erosion, Chronos'' Pendant, The World
    Stone, Screeching Gargoyle, Eye of Providence, Stone of Binding, Draconic Scale,
    Dreamer''s Idol, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel,
    Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.14
      fit: 0.27
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.38
      fit: 0.49
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.53
      pick: 0.48
      fit: 0.35
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.24
      fit: 0.35
    Rod of Asclepius:
      total: 0.6
      efficiency: 0.57
      win: 0.8
      pick: 0.1
      fit: 0.25
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Spear of the Magus
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Rod of Asclepius, Amanita Charm, Soul Gem, Shield of the Phoenix, Genji''s
    Guard, Gluttonous Grimoire, Kinetic Cuirass, Freya''s Tears, Ethereal Staff, Breastplate
    of Valor, Chandra''s Grace, Shifter''s Shield, Lifebinder, Helm of Radiance, Sphere
    of Negation, Yogi''s Necklace, Erosion, Eye of Providence, Phoenix Feather, Draconic
    Scale, Jade Scepter, Wish-Granting Pearl, Glorious Pridwen, Blood-Bound Book,
    Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.14
      fit: 0.3
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.48
      fit: 0.36
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.24
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.8
    Rod of Asclepius:
      total: 0.67
      efficiency: 0.57
      win: 0.8
      pick: 0.1
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  flex_slots:
  - Genji's Guard
  - Stone of Binding
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Asclepius, Genji''s Guard, Gluttonous Grimoire, Amanita Charm,
    Soul Gem, Stone of Binding, Screeching Gargoyle, Freya''s Tears, Kinetic Cuirass,
    Breastplate of Valor, Void Shield, Void Stone, Doom Orb, Helm of Radiance, Shifter''s
    Shield, The World Stone, Dreamer''s Idol, Shield of the Phoenix, Erosion, Eye
    of Providence, Draconic Scale, Chronos'' Pendant, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.68
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.49
      pick: 0.38
      fit: 0.59
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.14
      fit: 0.26
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.53
      pick: 0.48
      fit: 0.48
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.63
      pick: 0.24
      fit: 0.48
    Rod of Asclepius:
      total: 0.61
      efficiency: 0.57
      win: 0.8
      pick: 0.1
      fit: 0.29
  community_ordered:
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Spear of the Magus
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
    this god: Rod of Asclepius, Genji''s Guard, Nimble Ring, Gluttonous Grimoire,
    Amanita Charm, Soul Gem, Freya''s Tears, Breastplate of Valor, Kinetic Cuirass,
    Helm of Radiance, Shifter''s Shield, Bragi''s Harp, Shield of the Phoenix, Bracer
    of The Abyss, Stone of Binding, Erosion, Chronos'' Pendant, Eye of Providence,
    Daybreak Gavel, Screeching Gargoyle, Jade Scepter, Ancient Signet, Wish-Granting
    Pearl, Draconic Scale, Magi''s Cloak.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.51
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.53
      pick: 0.48
      fit: 0.21
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.63
      pick: 0.24
      fit: 0.21
    Rod of Asclepius:
      total: 0.59
      efficiency: 0.57
      win: 0.8
      pick: 0.1
      fit: 0.21
  community_ordered:
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Rod of Asclepius, Genji''s Guard,
    Freya''s Tears, Breastplate of Valor, Amanita Charm, Soul Gem, Kinetic Cuirass,
    Shield of the Phoenix, Screeching Gargoyle, Gluttonous Grimoire, Shifter''s Shield,
    Chronos'' Pendant, Helm of Radiance, Prophetic Cloak, Erosion, Gladiator''s Shield,
    Eye of Providence, Gem of Focus, Draconic Scale, Stone of Binding, Eye of Erebus,
    Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.14
      fit: 0.44
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.53
      pick: 0.48
      fit: 0.21
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.63
      pick: 0.24
      fit: 0.21
    Rod of Asclepius:
      total: 0.6
      efficiency: 0.57
      win: 0.8
      pick: 0.1
      fit: 0.21
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  flex_slots:
  - Genji's Guard
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
    win/pick). Underrated for this god: Rod of Asclepius, Jotunn''s Revenge, Genji''s
    Guard, Berserker''s Shield, Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Runeforged Hammer, Shield Splitter, Golden Blade,
    Soul Gem, Hydra''s Lament, Helm of Radiance, Shifter''s Shield, Eye of the Storm,
    Heartseeker, Nimble Ring, Tyrfing, Lernaean Bow, Shield of the Phoenix, Bragi''s
    Harp, Avenging Blade, Tekko-Kagi, Silverbranch Bow, Erosion, Death Metal, Titan''s
    Bane, Eye of Providence, Stone of Binding, The Crusher, Chronos'' Pendant, Draconic
    Scale, Jade Scepter, Doom Orb, Screeching Gargoyle, Toxic Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.56
      pick: 0.14
      fit: 0.22
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.48
      fit: 0.27
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.24
      fit: 0.27
    Rod of Asclepius:
      total: 0.6
      efficiency: 0.57
      win: 0.8
      pick: 0.1
      fit: 0.25
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Rod of Asclepius
  flex_slots:
  - Genji's Guard
  - Spear of Desolation
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Asclepius, Jotunn''s Revenge,
    Genji''s Guard, Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass,
    Breastplate of Valor, Soul Gem, Shield Splitter, Runeforged Hammer, Helm of Radiance,
    Shifter''s Shield, Hydra''s Lament, Berserker''s Shield, Eye of the Storm, Heartseeker,
    Shield of the Phoenix, Erosion, Eye of Providence, Chronos'' Pendant, Doom Orb,
    Jade Scepter, Stone of Binding, Draconic Scale, Death Metal, Wish-Granting Pearl,
    Avenging Blade, The World Stone, Screeching Gargoyle, Titan''s Bane, The Crusher,
    Ancient Signet, Magi''s Cloak, Dreamer''s Idol, Triton''s Conch, Helm of Darkness,
    Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.14
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.38
      fit: 0.44
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.53
      pick: 0.48
      fit: 0.33
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.24
      fit: 0.33
    Rod of Asclepius:
      total: 0.61
      efficiency: 0.57
      win: 0.8
      pick: 0.1
      fit: 0.3
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
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
    Grimoire, Genji''s Guard, Breastplate of Valor, Soul Gem, Shifter''s Shield, Helm
    of Radiance, Shield of the Phoenix, Erosion, Eye of Providence, Rod of Asclepius,
    Draconic Scale, Stone of Binding, Chronos'' Pendant, Jade Scepter, Wish-Granting
    Pearl, Helm of Darkness, Screeching Gargoyle, Doom Orb, Magi''s Cloak, The World
    Stone, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.14
      fit: 0.32
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.49
      pick: 0.38
      fit: 0.5
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.48
      fit: 0.36
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
