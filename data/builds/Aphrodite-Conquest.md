---
type: smite-build
god: Aphrodite
mode: Conquest
builds:
- source: community
  aspect: Aspect of Heartbreak
  aspect_pick_rate: 0.8
  aspect_win_rate: 0.47
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.25
    win_rate: 0.5
    alternates:
    - name: Book of Thoth
      pick_rate: 0.22
      win_rate: 0.45
    - name: Chronos' Pendant
      pick_rate: 0.12
      win_rate: 0.27
  - name: Book of Thoth
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.42
    - name: The Cosmic Horror
      pick_rate: 0.09
      win_rate: 0.57
  - name: Rod of Tahuti
    pick_rate: 0.12
    win_rate: 0.46
    alternates:
    - name: The World Stone
      pick_rate: 0.07
      win_rate: 0.35
    - name: Totem of Death
      pick_rate: 0.07
      win_rate: 0.53
  - name: Obsidian Shard
    pick_rate: 0.08
    win_rate: 0.42
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.29
      win_rate: 0.44
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.5
  - name: Blinking Abyss
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.5
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.52
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.3
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.58
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.68
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.25
    win_rate: 0.55
  - name: Sands Of Time
    pick_rate: 0.24
    win_rate: 0.37
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/aphrodite/
  last_verified: '2026-10-14'
  god_win_rate: 0.49079754601226994
  god_matches_won: 240
  god_matches_played: 489
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-14'
  god_matches_analyzed: 8861
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire,
    Genji''s Guard, Breastplate of Valor, Soul Gem, Shifter''s Shield, Spear of the
    Magus, Helm of Radiance, Shield of the Phoenix, Erosion, Eye of Providence, Rod
    of Asclepius, Draconic Scale, Stone of Binding, Jade Scepter, Wish-Granting Pearl,
    Helm of Darkness, Screeching Gargoyle, Obsidian Shard, Doom Orb, Magi''s Cloak,
    Midgardian Mail, Mantle Of Discord, The World Stone, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.48
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.25
      fit: 0.5
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.48
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.46
      pick: 0.19
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Breastplate of Valor
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Genji''s Guard, Breastplate of Valor, Gluttonous Grimoire, Freya''s Tears,
    Kinetic Cuirass, Spear of the Magus, Soul Gem, Helm of Radiance, Shifter''s Shield,
    Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet, Death Metal,
    Shield of the Phoenix, Jade Scepter, Erosion, Obsidian Shard, Eye of Providence,
    Stone of Binding, Draconic Scale, Triton''s Conch, Screeching Gargoyle, Daybreak
    Gavel, The World Stone, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.5
      pick: 0.12
      fit: 0.25
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.28
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.25
      fit: 0.4
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.28
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.46
      pick: 0.19
      fit: 0.37
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Genji''s Guard, Soul
    Gem, Breastplate of Valor, Kinetic Cuirass, Spear of the Magus, Helm of Radiance,
    Shifter''s Shield, Shield of the Phoenix, Obsidian Shard, Doom Orb, Rod of Asclepius,
    Erosion, Screeching Gargoyle, Eye of Providence, Stone of Binding, Draconic Scale,
    Dreamer''s Idol, Jade Scepter, Wish-Granting Pearl, Magi''s Cloak, Daybreak Gavel,
    Ancient Signet, The World Stone, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.5
      pick: 0.12
      fit: 0.14
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.25
      fit: 0.49
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.48
      pick: 0.0
      fit: 0.39
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.46
      pick: 0.19
      fit: 0.35
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Grimoire, Kinetic Cuirass, Freya''s Tears, Ethereal Staff, Genji''s Guard, Breastplate
    of Valor, Shifter''s Shield, Lifebinder, Spear of the Magus, Helm of Radiance,
    Sphere of Negation, Yogi''s Necklace, Erosion, Chandra''s Grace, Eye of Providence,
    Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Glorious Pridwen,
    Blood-Bound Book, Obsidian Shard, Chronos'' Pendant.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.48
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.48
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.25
      fit: 0.5
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.46
      pick: 0.19
      fit: 0.36
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.9
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Spear of Desolation
  - Gluttonous Grimoire
  - Rod of Tahuti
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Soul Gem, Spear of the Magus,
    Stone of Binding, Screeching Gargoyle, Freya''s Tears, Kinetic Cuirass, Genji''s
    Guard, Breastplate of Valor, Void Shield, Void Stone, Obsidian Shard, Doom Orb,
    Helm of Radiance, Shifter''s Shield, Dreamer''s Idol, Shield of the Phoenix, Rod
    of Asclepius, Erosion, Eye of Providence, Draconic Scale, Jade Scepter, Wish-Granting
    Pearl, Magi''s Cloak, The World Stone, Chronos'' Pendant.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.49
      efficiency: 0.51
      win: 0.48
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.5
      efficiency: 0.51
      win: 0.48
      pick: 0.0
      fit: 0.68
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.25
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.55
      win: 0.48
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.46
      pick: 0.19
      fit: 0.48
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Gluttonous Grimoire
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Amanita Charm, Soul Gem, Freya''s
    Tears, Genji''s Guard, Breastplate of Valor, Kinetic Cuirass, Spear of the Magus,
    Helm of Radiance, Shifter''s Shield, Rod of Asclepius, Bragi''s Harp, Shield of
    the Phoenix, Bracer of The Abyss, Stone of Binding, Erosion, Eye of Providence,
    Daybreak Gavel, Screeching Gargoyle, Jade Scepter, Ancient Signet, Wish-Granting
    Pearl, Draconic Scale, Magi''s Cloak, Obsidian Shard, Chronos'' Pendant.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.44
      efficiency: 0.44
      win: 0.48
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.5
      pick: 0.25
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.46
      pick: 0.19
      fit: 0.21
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Screeching
    Gargoyle, Gluttonous Grimoire, Shifter''s Shield, Spear of the Magus, Helm of
    Radiance, Prophetic Cloak, Erosion, Gladiator''s Shield, Eye of Providence, Gem
    of Focus, Draconic Scale, Stone of Binding, Rod of Asclepius, Eye of Erebus, Magi''s
    Cloak, Daybreak Gavel, Midgardian Mail, Mantle Of Discord, Obsidian Shard, Chronos''
    Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.48
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.25
      fit: 0.52
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.48
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita
    Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Shield Splitter, Golden Blade, Spear of the Magus,
    Soul Gem, Hydra''s Lament, Helm of Radiance, Shifter''s Shield, Eye of the Storm,
    Heartseeker, Nimble Ring, Tyrfing, Lernaean Bow, Rod of Asclepius, Shield of the
    Phoenix, Bragi''s Harp, Avenging Blade, Tekko-Kagi, Silverbranch Bow, Erosion,
    Death Metal, Titan''s Bane, Eye of Providence, Stone of Binding, The Crusher,
    Draconic Scale, Obsidian Shard, Jade Scepter, Doom Orb, Screeching Gargoyle, Toxic
    Blade, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.5
      pick: 0.12
      fit: 0.14
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.48
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.48
      pick: 0.0
      fit: 0.43
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.2
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.46
      pick: 0.19
      fit: 0.27
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass, Genji''s Guard, Breastplate
    of Valor, Soul Gem, Spear of the Magus, Shield Splitter, Runeforged Hammer, Helm
    of Radiance, Shifter''s Shield, Hydra''s Lament, Berserker''s Shield, Eye of the
    Storm, Rod of Asclepius, Heartseeker, Shield of the Phoenix, Erosion, Eye of Providence,
    Obsidian Shard, Doom Orb, Jade Scepter, Stone of Binding, Draconic Scale, Death
    Metal, Wish-Granting Pearl, Avenging Blade, Screeching Gargoyle, Titan''s Bane,
    The Crusher, Ancient Signet, Magi''s Cloak, Dreamer''s Idol, Triton''s Conch,
    Helm of Darkness, Daybreak Gavel, The World Stone, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.5
      pick: 0.12
      fit: 0.18
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.48
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.25
      fit: 0.44
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.18
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.46
      pick: 0.19
      fit: 0.33
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
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
    Grimoire, Genji''s Guard, Breastplate of Valor, Soul Gem, Shifter''s Shield, Spear
    of the Magus, Helm of Radiance, Obsidian Shard, Shield of the Phoenix, Erosion,
    Eye of Providence, Rod of Asclepius, Draconic Scale, Stone of Binding, Chronos''
    Pendant, Jade Scepter, Wish-Granting Pearl, Helm of Darkness, Screeching Gargoyle,
    Doom Orb, Magi''s Cloak, The World Stone, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.48
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.25
      fit: 0.5
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.48
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.46
      pick: 0.19
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
