---
type: smite-build
god: Hel
mode: Conquest
builds:
- source: community
  aspect: Aspect of Divergence
  aspect_pick_rate: 0.33
  aspect_win_rate: 0.5
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.5
    win_rate: 0.6
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
    win_rate: 0.58
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.16
      win_rate: 0.62
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
      pick_rate: 0.07
      win_rate: 0.64
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.3
    win_rate: 0.62
  - name: Sands Of Time
    pick_rate: 0.26
    win_rate: 0.58
  - name: Archmage's Gem
    pick_rate: 0.17
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/hel/
  last_verified: '2026-11-02'
  god_win_rate: 0.5903225806451613
  god_matches_won: 732
  god_matches_played: 1240
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Helm of Darkness — magical protection
    swap_item: Helm of Darkness
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Breastplate of Valor, Helm of Radiance, Helm of Darkness, Spear of the
    Magus, Chronos'' Pendant, Erosion, Lotus Sickle, Shield of the Phoenix, Eye of
    Providence, Oni Hunter''s Garb, Draconic Scale, Jade Scepter, Doom Orb, Stone
    of Binding, Screeching Gargoyle, The World Stone, Midgardian Mail, Magi''s Cloak,
    Shifter''s Shield, Freya''s Tears, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.5
      win: 0.6
      pick: 0.5
      fit: 0.2
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.62
      pick: 0.45
      fit: 0.37
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.47
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.49
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
  - Breastplate of Valor
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Breastplate of Valor,
    Soul Gem, Helm of Radiance, Lotus Sickle, Spear of the Magus, Death Metal, Helm
    of Darkness, Chronos'' Pendant, Oni Hunter''s Garb, Doom Orb, The World Stone,
    Jade Scepter, Wish-Granting Pearl, Erosion, Shield of the Phoenix, Eye of Providence,
    Polynomicon, Screeching Gargoyle, Midgardian Mail, Ancient Signet, Triton''s Conch,
    Stone of Binding, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.5
      win: 0.6
      pick: 0.5
      fit: 0.25
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.28
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.28
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.62
      pick: 0.45
      fit: 0.37
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.41
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.35
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
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Genji''s Guard, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass,
    Breastplate of Valor, Spear of the Magus, Helm of Radiance, Chronos'' Pendant,
    Lotus Sickle, Helm of Darkness, Doom Orb, Shield of the Phoenix, The World Stone,
    Oni Hunter''s Garb, Screeching Gargoyle, Death Metal, Erosion, Eye of Providence,
    Dreamer''s Idol, Jade Scepter, Midgardian Mail, Stone of Binding, Draconic Scale,
    Magi''s Cloak, Freya''s Tears, Leviathan''s Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.5
      win: 0.6
      pick: 0.5
      fit: 0.14
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.3
      fit: 0.49
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.62
      pick: 0.45
      fit: 0.35
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.45
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Genji''s Guard, Ethereal Staff, Blood-Bound Book, Phoenix Feather,
    Breastplate of Valor, Yogi''s Necklace, Rod of Asclepius, Helm of Radiance, Chandra''s
    Grace, Sphere of Negation, Spear of the Magus, Helm of Darkness, Oni Hunter''s
    Garb, Erosion, Lotus Sickle, Eye of Providence, Jade Scepter, Draconic Scale,
    Regrowth Striders, Doom Orb, Midgardian Mail, Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.62
      pick: 0.45
      fit: 0.37
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.47
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.6
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.91
  community_ordered:
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
    for this god: Gluttonous Grimoire, Amanita Charm, Soul Gem, Genji''s Guard, Screeching
    Gargoyle, Stone of Binding, Spear of the Magus, Kinetic Cuirass, Void Stone, Void
    Shield, Doom Orb, Breastplate of Valor, The World Stone, Helm of Radiance, Helm
    of Darkness, Dreamer''s Idol, Chronos'' Pendant, Lotus Sickle, Oni Hunter''s Garb,
    Shield of the Phoenix, Erosion, Eye of Providence, Jade Scepter, Draconic Scale,
    Midgardian Mail, The Cosmic Horror, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.5
      win: 0.6
      pick: 0.5
      fit: 0.17
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.26
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.58
      pick: 0.3
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.87
      win: 0.62
      pick: 0.45
      fit: 0.48
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.58
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
    Guard, Kinetic Cuirass, Breastplate of Valor, Helm of Radiance, Eros'' Bow, Spear
    of the Magus, Chronos'' Pendant, Blood-Bound Book, Helm of Darkness, Lotus Sickle,
    Oni Hunter''s Garb, Bragi''s Harp, Bracer of The Abyss, Jade Scepter, Screeching
    Gargoyle, Shield of the Phoenix, Death Metal, Midgardian Mail, Erosion, Stone
    of Binding, Doom Orb, Eye of Providence, Freya''s Tears.'
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
      efficiency: 0.87
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
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Amanita Charm, Breastplate
    of Valor, Soul Gem, Kinetic Cuirass, Shield of the Phoenix, Chronos'' Pendant,
    Screeching Gargoyle, Lotus Sickle, Gluttonous Grimoire, Freya''s Tears, Helm of
    Radiance, Prophetic Cloak, Oni Hunter''s Garb, Spear of the Magus, Helm of Darkness,
    Erosion, Eye of Providence, Gem of Focus, Gladiator''s Shield, Heartwood Charm,
    Draconic Scale, Stone of Binding, Midgardian Mail, Chandra''s Grace, Magi''s Cloak,
    Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.3
      fit: 0.53
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.87
      win: 0.62
      pick: 0.45
      fit: 0.23
    Obsidian Shard:
      total: 0.55
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.33
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Genji''s Guard, Kinetic Cuirass, Gluttonous
    Grimoire, Soul Gem, Freya''s Tears, Breastplate of Valor, Helm of Radiance, Helm
    of Darkness, Spear of the Magus, Erosion, Lotus Sickle, Shield of the Phoenix,
    Eye of Providence, Oni Hunter''s Garb, Draconic Scale, Jade Scepter, Doom Orb,
    Chronos'' Pendant, Stone of Binding, Screeching Gargoyle, The World Stone, Midgardian
    Mail, Magi''s Cloak, Shifter''s Shield, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.3
      fit: 0.51
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.62
      pick: 0.45
      fit: 0.37
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.64
      pick: 0.27
      fit: 0.47
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---
