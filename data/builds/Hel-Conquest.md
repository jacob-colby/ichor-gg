---
type: smite-build
god: Hel
mode: Conquest
builds:
- source: community
  aspect: Aspect of Divergence
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.5
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.5
    win_rate: 0.61
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.61
    - name: Chandra's Grace
      pick_rate: 0.07
      win_rate: 0.62
  - name: Spear of Desolation
    pick_rate: 0.22
    win_rate: 0.58
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.63
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.62
  - name: Rod of Tahuti
    pick_rate: 0.29
    win_rate: 0.62
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.07
      win_rate: 0.64
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.53
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.24
      win_rate: 0.62
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.63
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.16
      win_rate: 0.63
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.59
  - name: Killing Stone
    pick_rate: 0.07
    win_rate: 0.7
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.73
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.64
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.3
    win_rate: 0.63
  - name: Sands Of Time
    pick_rate: 0.26
    win_rate: 0.58
  - name: Archmage's Gem
    pick_rate: 0.17
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/hel/
  last_verified: '2026-11-04'
  god_win_rate: 0.5919678714859438
  god_matches_won: 737
  god_matches_played: 1245
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Gluttonous Grimoire
  - Obsidian Shard
  flex_slots:
  - Kinetic Cuirass
  - Book of Thoth
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
    this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Genji''s Guard, Kinetic
    Cuirass, Breastplate of Valor, Lotus Sickle, Helm of Radiance, Helm of Darkness,
    Spear of the Magus, Chronos'' Pendant, Blood-Bound Book, Erosion, Shield of the
    Phoenix, Oni Hunter''s Garb, Eye of Providence, Draconic Scale, Ancient Signet,
    Jade Scepter, Doom Orb, Screeching Gargoyle, Stone of Binding, Midgardian Mail,
    The World Stone, Magi''s Cloak, Leviathan''s Hide, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.49
      win: 0.61
      pick: 0.5
      fit: 0.18
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.62
      pick: 0.45
      fit: 0.34
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.44
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  - Lotus Sickle
  flex_slots:
  - Lotus Sickle
  - Book of Thoth
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Soul Gem, Genji''s Guard, Amanita Charm, Lotus Sickle, Kinetic Cuirass,
    Breastplate of Valor, Helm of Radiance, Ancient Signet, Spear of the Magus, Death
    Metal, Chronos'' Pendant, Oni Hunter''s Garb, Helm of Darkness, Blood-Bound Book,
    Doom Orb, The World Stone, Jade Scepter, Shield of the Phoenix, Erosion, Eye of
    Providence, Screeching Gargoyle, Midgardian Mail, Wish-Granting Pearl, Stone of
    Binding, Polynomicon, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.49
      win: 0.61
      pick: 0.5
      fit: 0.24
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.62
      pick: 0.45
      fit: 0.35
    Obsidian Shard:
      total: 0.56
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.39
    Lotus Sickle:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Genji''s Guard, Kinetic Cuirass,
    Breastplate of Valor, Lotus Sickle, Spear of the Magus, Helm of Radiance, Chronos''
    Pendant, Helm of Darkness, Doom Orb, Blood-Bound Book, Shield of the Phoenix,
    Oni Hunter''s Garb, The World Stone, Screeching Gargoyle, Ancient Signet, Death
    Metal, Erosion, Eye of Providence, Midgardian Mail, Jade Scepter, Stone of Binding,
    Dreamer''s Idol, Draconic Scale, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.49
      win: 0.61
      pick: 0.5
      fit: 0.13
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.25
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.3
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.62
      pick: 0.45
      fit: 0.33
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.43
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Book of Thoth
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
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix,
    Blood-Bound Book, Genji''s Guard, Kinetic Cuirass, Ethereal Staff, Bancroft''s
    Talon, Lotus Sickle, Phoenix Feather, Yogi''s Necklace, Breastplate of Valor,
    Rod of Asclepius, Helm of Radiance, Chandra''s Grace, Sphere of Negation, Spear
    of the Magus, Soul Locket, Helm of Darkness, Oni Hunter''s Garb, Erosion, Jade
    Scepter, Eye of Providence, Regrowth Striders, Draconic Scale, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.49
      win: 0.61
      pick: 0.5
      fit: 0.18
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.27
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.62
      pick: 0.45
      fit: 0.34
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.44
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Genji's Guard
  - Book of Thoth
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
    for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Genji''s Guard, Screeching
    Gargoyle, Stone of Binding, Spear of the Magus, Kinetic Cuirass, Void Stone, Void
    Shield, Breastplate of Valor, Doom Orb, Lotus Sickle, Helm of Radiance, The World
    Stone, Helm of Darkness, Dreamer''s Idol, Chronos'' Pendant, Blood-Bound Book,
    Oni Hunter''s Garb, Shield of the Phoenix, Ancient Signet, Erosion, Eye of Providence,
    Jade Scepter, Draconic Scale, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.49
      win: 0.61
      pick: 0.5
      fit: 0.15
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.24
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.58
      pick: 0.3
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.73
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.62
      pick: 0.45
      fit: 0.45
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.55
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  - Eros' Bow
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Genji''s
    Guard, Kinetic Cuirass, Breastplate of Valor, Lotus Sickle, Helm of Radiance,
    Eros'' Bow, Spear of the Magus, Chronos'' Pendant, Blood-Bound Book, Ancient Signet,
    Helm of Darkness, Oni Hunter''s Garb, Bragi''s Harp, Bracer of The Abyss, Shield
    of the Phoenix, Screeching Gargoyle, Jade Scepter, Death Metal, Midgardian Mail,
    Erosion, Stone of Binding, Doom Orb, Freya''s Tears.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.51
      efficiency: 0.45
      win: 0.62
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.62
      pick: 0.45
      fit: 0.22
    Obsidian Shard:
      total: 0.55
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.32
    Eros' Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Soul Gem, Amanita
    Charm, Breastplate of Valor, Gluttonous Grimoire, Lotus Sickle, Kinetic Cuirass,
    Shield of the Phoenix, Chronos'' Pendant, Screeching Gargoyle, Freya''s Tears,
    Helm of Radiance, Oni Hunter''s Garb, Spear of the Magus, Prophetic Cloak, Erosion,
    Helm of Darkness, Eye of Providence, Gem of Focus, Blood-Bound Book, Midgardian
    Mail, Stone of Binding, Heartwood Charm, Draconic Scale, Gladiator''s Shield,
    Magi''s Cloak, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.49
      win: 0.61
      pick: 0.5
      fit: 0.08
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.3
      fit: 0.49
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.62
      pick: 0.45
      fit: 0.21
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.66
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
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Kinetic Cuirass
  - Obsidian Shard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Genji''s
    Guard, Kinetic Cuirass, Freya''s Tears, Breastplate of Valor, Lotus Sickle, Helm
    of Radiance, Helm of Darkness, Spear of the Magus, Blood-Bound Book, Erosion,
    Shield of the Phoenix, Oni Hunter''s Garb, Eye of Providence, Draconic Scale,
    Ancient Signet, Jade Scepter, Chronos'' Pendant, Doom Orb, Screeching Gargoyle,
    Stone of Binding, Midgardian Mail, The World Stone, Magi''s Cloak, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.3
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.62
      pick: 0.45
      fit: 0.34
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.44
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
