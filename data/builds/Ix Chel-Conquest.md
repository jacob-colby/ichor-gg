---
type: smite-build
god: Ix Chel
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Mother's Light
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.38
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.47
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.18
      win_rate: 0.48
    - name: The World Stone
      pick_rate: 0.07
      win_rate: 0.5
  - name: The World Stone
    pick_rate: 0.36
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.51
  - name: Rod of Tahuti
    pick_rate: 0.22
    win_rate: 0.54
    alternates:
    - name: Soul Gem
      pick_rate: 0.13
      win_rate: 0.55
    - name: The World Stone
      pick_rate: 0.12
      win_rate: 0.47
  - name: Obsidian Shard
    pick_rate: 0.15
    win_rate: 0.54
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.31
      win_rate: 0.55
    - name: Spear of the Magus
      pick_rate: 0.05
      win_rate: 0.63
  - name: Soul Gem
    pick_rate: 0.06
    win_rate: 0.39
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.18
      win_rate: 0.59
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.54
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.54
    alternates:
    - name: Dreamer's Idol
      pick_rate: 0.07
      win_rate: 0.67
    - name: Oracle Staff
      pick_rate: 0.05
      win_rate: 0.56
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.3
    win_rate: 0.62
  - name: Sands Of Time
    pick_rate: 0.22
    win_rate: 0.35
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/ix-chel/
  last_verified: '2026-11-02'
  god_win_rate: 0.4948717948717949
  god_matches_won: 193
  god_matches_played: 390
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
  - Genji's Guard
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Spear of the Magus
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Spear of the Magus, Genji''s Guard, Kinetic Cuirass,
    Gluttonous Grimoire, Freya''s Tears, Breastplate of Valor, Helm of Radiance, Helm
    of Darkness, Erosion, Shield of the Phoenix, Eye of Providence, Draconic Scale,
    Oni Hunter''s Garb, Chronos'' Pendant, Jade Scepter, Screeching Gargoyle, Stone
    of Binding, Midgardian Mail, Doom Orb, Shifter''s Shield, Magi''s Cloak, Mantle
    Of Discord, Leviathan''s Hide, Soul Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.32
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.47
      fit: 0.5
    Spear of the Magus:
      total: 0.54
      efficiency: 0.58
      win: 0.63
      pick: 0.08
      fit: 0.36
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.54
      pick: 0.34
      fit: 0.36
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  flex_slots:
  - Genji's Guard
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, Genji''s Guard, Amanita Charm, Breastplate of Valor, Gluttonous
    Grimoire, Kinetic Cuirass, Helm of Radiance, Freya''s Tears, Death Metal, Helm
    of Darkness, Doom Orb, Oni Hunter''s Garb, Chronos'' Pendant, Jade Scepter, Wish-Granting
    Pearl, Shield of the Phoenix, Ancient Signet, Erosion, Eye of Providence, Screeching
    Gargoyle, Polynomicon, Stone of Binding, Midgardian Mail, Heartwood Charm, Soul
    Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.28
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.47
      fit: 0.4
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.28
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.54
      pick: 0.34
      fit: 0.37
    Spear of the Magus:
      total: 0.54
      efficiency: 0.58
      win: 0.63
      pick: 0.08
      fit: 0.31
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.31
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    god: Spear of the Magus, Amanita Charm, Genji''s Guard, Gluttonous Grimoire, Kinetic
    Cuirass, Breastplate of Valor, Freya''s Tears, Helm of Radiance, Helm of Darkness,
    Doom Orb, Shield of the Phoenix, Screeching Gargoyle, Chronos'' Pendant, Death
    Metal, Erosion, Oni Hunter''s Garb, Eye of Providence, Stone of Binding, Midgardian
    Mail, Jade Scepter, Draconic Scale, Magi''s Cloak, Leviathan''s Hide, Soul Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.47
      fit: 0.49
    Spear of the Magus:
      total: 0.54
      efficiency: 0.58
      win: 0.63
      pick: 0.08
      fit: 0.35
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.54
      pick: 0.34
      fit: 0.35
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.35
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Shield of the Phoenix
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Dreamer's Idol
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Spear of the Magus, Kinetic Cuirass,
    Gluttonous Grimoire, Genji''s Guard, Ethereal Staff, Freya''s Tears, Breastplate
    of Valor, Phoenix Feather, Blood-Bound Book, Helm of Radiance, Yogi''s Necklace,
    Rod of Asclepius, Sphere of Negation, Helm of Darkness, Chandra''s Grace, Soul
    Gem, Erosion, Eye of Providence, Jade Scepter, Oni Hunter''s Garb, Draconic Scale,
    Glorious Pridwen, Chronos'' Pendant, Regrowth Striders.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.79
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.47
      fit: 0.5
    Spear of the Magus:
      total: 0.54
      efficiency: 0.58
      win: 0.63
      pick: 0.08
      fit: 0.36
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.54
      pick: 0.34
      fit: 0.36
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.36
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Spear of Desolation
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  flex_slots:
  - Gluttonous Grimoire
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Spear of the Magus, Gluttonous Grimoire, Amanita Charm, Screeching
    Gargoyle, Stone of Binding, Genji''s Guard, Kinetic Cuirass, Freya''s Tears, Void
    Stone, Breastplate of Valor, Void Shield, Doom Orb, Helm of Radiance, Helm of
    Darkness, Shield of the Phoenix, Erosion, Eye of Providence, Oni Hunter''s Garb,
    Chronos'' Pendant, Draconic Scale, Jade Scepter, Midgardian Mail, The Cosmic Horror,
    Soul Gem.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.54
      pick: 0.47
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.87
      win: 0.54
      pick: 0.34
      fit: 0.48
    Spear of the Magus:
      total: 0.56
      efficiency: 0.58
      win: 0.63
      pick: 0.08
      fit: 0.48
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.48
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
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
    this god: Spear of the Magus, Nimble Ring, Gluttonous Grimoire, Amanita Charm,
    Genji''s Guard, Kinetic Cuirass, Breastplate of Valor, Freya''s Tears, Helm of
    Radiance, Eros'' Bow, Blood-Bound Book, Helm of Darkness, Bragi''s Harp, Oni Hunter''s
    Garb, Bracer of The Abyss, Screeching Gargoyle, Chronos'' Pendant, Shield of the
    Phoenix, Death Metal, Stone of Binding, Jade Scepter, Erosion, Midgardian Mail,
    Eye of Providence, Doom Orb, Soul Gem.'
  slot_scores:
    Nimble Ring:
      total: 0.52
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.47
      efficiency: 0.45
      win: 0.54
      pick: 0.0
      fit: 0.47
    Spear of the Magus:
      total: 0.52
      efficiency: 0.58
      win: 0.63
      pick: 0.08
      fit: 0.21
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.87
      win: 0.54
      pick: 0.34
      fit: 0.21
    Dreamer's Idol:
      total: 0.52
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.21
    Eros' Bow:
      total: 0.48
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Freya''s Tears, Breastplate
    of Valor, Amanita Charm, Spear of the Magus, Kinetic Cuirass, Shield of the Phoenix,
    Screeching Gargoyle, Gluttonous Grimoire, Chronos'' Pendant, Helm of Radiance,
    Prophetic Cloak, Helm of Darkness, Erosion, Gem of Focus, Eye of Providence, Oni
    Hunter''s Garb, Gladiator''s Shield, Heartwood Charm, Stone of Binding, Draconic
    Scale, Midgardian Mail, Magi''s Cloak, Chandra''s Grace, Leviathan''s Hide, Soul
    Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.47
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.87
      win: 0.54
      pick: 0.34
      fit: 0.21
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
  community_ordered:
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
  - Spear of Desolation
  - Freya's Tears
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Genji''s Guard, Kinetic Cuirass, Gluttonous
    Grimoire, Freya''s Tears, Soul Gem, Breastplate of Valor, Helm of Radiance, Helm
    of Darkness, Spear of the Magus, Erosion, Shield of the Phoenix, Eye of Providence,
    Draconic Scale, Oni Hunter''s Garb, Chronos'' Pendant, Jade Scepter, Screeching
    Gargoyle, Stone of Binding, Midgardian Mail, Doom Orb, Shifter''s Shield, Magi''s
    Cloak, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.47
      fit: 0.5
    Freya's Tears:
      total: 0.52
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.54
      pick: 0.34
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
