---
type: smite-build
god: Hel
mode: Conquest
builds:
- source: community
  aspect: Aspect of Divergence
  aspect_pick_rate: 0.4
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.4
    win_rate: 0.5
    alternates:
    - name: Lotus Sickle
      pick_rate: 0.2
      win_rate: 1.0
    - name: Gauntlet of Thebes
      pick_rate: 0.2
      win_rate: 1.0
  - name: Lotus Sickle
    pick_rate: 0.2
    win_rate: 1.0
    alternates:
    - name: Stampede
      pick_rate: 0.2
      win_rate: 1.0
    - name: The World Stone
      pick_rate: 0.2
      win_rate: 0.0
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 1.0
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.2
      win_rate: 1.0
    - name: The World Stone
      pick_rate: 0.2
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.2
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 1.0
    - name: Rod of Tahuti
      pick_rate: 0.2
      win_rate: 1.0
  - name: Freya's Tears
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.33
      win_rate: 1.0
    - name: Obsidian Shard
      pick_rate: 0.33
      win_rate: 1.0
  - name: Chandra's Grace
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Killing Stone
      pick_rate: 0.5
      win_rate: 1.0
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.6
    win_rate: 1.0
  - name: Archmage's Gem
    pick_rate: 0.2
    win_rate: 0.0
  - name: Sands Of Time
    pick_rate: 0.2
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/hel/
  last_verified: '2026-11-04'
  god_win_rate: 0.6
  god_matches_won: 3
  god_matches_played: 5
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Gluttonous Grimoire
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Kinetic Cuirass, Helm
    of Radiance, Helm of Darkness, Spear of the Magus, Blood-Bound Book, Erosion,
    Shield of the Phoenix, Oni Hunter''s Garb, Eye of Providence, Draconic Scale,
    Ancient Signet, Jade Scepter, Chronos'' Pendant, Doom Orb, Screeching Gargoyle,
    Stone of Binding, Midgardian Mail, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.65
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.75
      efficiency: 0.69
      win: 1.0
      pick: 0.31
      fit: 0.28
    Gluttonous Grimoire:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.66
    Freya's Tears:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.44
    Obsidian Shard:
      total: 0.76
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.44
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 1.0
      pick: 0.33
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Gluttonous Grimoire
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Soul Gem, Amanita Charm, Kinetic Cuirass, Helm of Radiance, Ancient
    Signet, Spear of the Magus, Death Metal, Oni Hunter''s Garb, Helm of Darkness,
    Blood-Bound Book, Doom Orb, Jade Scepter, Chronos'' Pendant, Shield of the Phoenix,
    Erosion, Eye of Providence, Screeching Gargoyle, Midgardian Mail, Wish-Granting
    Pearl, Stone of Binding, Polynomicon.'
  slot_scores:
    Book of Thoth:
      total: 0.66
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.24
    Genji's Guard:
      total: 0.75
      efficiency: 0.69
      win: 1.0
      pick: 0.31
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.31
    Obsidian Shard:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.39
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 1.0
      pick: 0.33
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Gluttonous Grimoire
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Book of Thoth
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Kinetic Cuirass, Spear of the
    Magus, Helm of Radiance, Helm of Darkness, Doom Orb, Blood-Bound Book, Shield
    of the Phoenix, Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Ancient
    Signet, Death Metal, Erosion, Eye of Providence, Midgardian Mail, Jade Scepter,
    Stone of Binding, Dreamer''s Idol, Draconic Scale.'
  slot_scores:
    Book of Thoth:
      total: 0.64
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.13
    Genji's Guard:
      total: 0.74
      efficiency: 0.69
      win: 1.0
      pick: 0.31
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.75
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.37
    Obsidian Shard:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.43
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 1.0
      pick: 0.33
      fit: 0.33
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  - Freya's Tears
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Blood-Bound Book, Kinetic Cuirass, Ethereal Staff, Bancroft''s Talon, Phoenix
    Feather, Yogi''s Necklace, Rod of Asclepius, Helm of Radiance, Sphere of Negation,
    Spear of the Magus, Soul Locket, Helm of Darkness, Oni Hunter''s Garb, Erosion,
    Jade Scepter, Eye of Providence, Regrowth Striders, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.75
      efficiency: 0.69
      win: 1.0
      pick: 0.31
      fit: 0.27
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 1.0
      pick: 0.33
      fit: 0.34
    Obsidian Shard:
      total: 0.76
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.44
    Freya's Tears:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.4
    Amanita Charm:
      total: 0.79
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Gluttonous Grimoire
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Screeching Gargoyle
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
    for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Screeching Gargoyle,
    Stone of Binding, Spear of the Magus, Kinetic Cuirass, Void Stone, Void Shield,
    Doom Orb, Helm of Radiance, Helm of Darkness, Dreamer''s Idol, Blood-Bound Book,
    Oni Hunter''s Garb, Shield of the Phoenix, Ancient Signet, Erosion, Eye of Providence,
    Chronos'' Pendant, Jade Scepter, Draconic Scale.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.64
    Genji's Guard:
      total: 0.74
      efficiency: 0.69
      win: 1.0
      pick: 0.31
      fit: 0.24
    Gluttonous Grimoire:
      total: 0.77
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.37
    Obsidian Shard:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.55
    Rod of Tahuti:
      total: 0.84
      efficiency: 0.86
      win: 1.0
      pick: 0.33
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
  - Eros' Bow
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Kinetic Cuirass,
    Helm of Radiance, Eros'' Bow, Spear of the Magus, Blood-Bound Book, Ancient Signet,
    Helm of Darkness, Oni Hunter''s Garb, Bragi''s Harp, Bracer of The Abyss, Shield
    of the Phoenix, Screeching Gargoyle, Chronos'' Pendant, Jade Scepter, Death Metal,
    Midgardian Mail, Erosion, Stone of Binding, Doom Orb.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.31
      fit: 0.18
    Nimble Ring:
      total: 0.72
      efficiency: 0.63
      win: 1.0
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.33
      fit: 0.22
    Obsidian Shard:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.32
    Eros' Bow:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Rod of Tahuti
  - Freya's Tears
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Soul Gem, Amanita Charm, Gluttonous
    Grimoire, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Chronos''
    Pendant, Helm of Radiance, Oni Hunter''s Garb, Spear of the Magus, Prophetic Cloak,
    Erosion, Helm of Darkness, Eye of Providence, Gem of Focus, Blood-Bound Book,
    Midgardian Mail, Stone of Binding, Heartwood Charm, Draconic Scale, Gladiator''s
    Shield, Magi''s Cloak, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.77
      efficiency: 0.69
      win: 1.0
      pick: 0.31
      fit: 0.4
    Breastplate of Valor:
      total: 0.75
      efficiency: 0.63
      win: 1.0
      pick: 0.31
      fit: 0.4
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.33
      fit: 0.21
    Freya's Tears:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.53
    Obsidian Shard:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.31
    Soul Gem:
      total: 0.75
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Rod of Tahuti
  - Freya's Tears
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Gluttonous Grimoire
  - Obsidian Shard
  - Rod of Tahuti
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
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Kinetic
    Cuirass, Helm of Radiance, Helm of Darkness, Spear of the Magus, Blood-Bound Book,
    Erosion, Shield of the Phoenix, Oni Hunter''s Garb, Eye of Providence, Draconic
    Scale, Ancient Signet, Jade Scepter, Chronos'' Pendant, Doom Orb, Screeching Gargoyle,
    Stone of Binding, Midgardian Mail, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.75
      efficiency: 0.69
      win: 1.0
      pick: 0.31
      fit: 0.28
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.4
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.76
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.44
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 1.0
      pick: 0.33
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
---
