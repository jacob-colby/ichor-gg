---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.72
  aspect_win_rate: 0.6
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.72
    - name: Daybreak Gavel
      pick_rate: 0.09
      win_rate: 0.53
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.32
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.63
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.39
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.65
    - name: The Cosmic Horror
      pick_rate: 0.06
      win_rate: 0.2
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.4
  - name: Obsidian Shard
    pick_rate: 0.06
    win_rate: 0.78
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.6
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.63
  - name: Shield
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Rune
      pick_rate: 0.04
      win_rate: 0.5
    - name: Captain's Ring
      pick_rate: 0.03
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.43
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-08-16'
  god_win_rate: 0.5508021390374331
  god_matches_won: 103
  god_matches_played: 187
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Obsidian Shard, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Freya''s Tears, Nimble Ring, Shield of the Phoenix, Oni Hunter''s Garb,
    Spear of the Magus, Erosion, Eye of Providence, Spectral Armor, Helm of Radiance,
    Draconic Scale, Shifter''s Shield, Rod of Asclepius, Chronos'' Pendant, Leviathan''s
    Hide, Jade Scepter, Midgardian Mail, Screeching Gargoyle, The Cosmic Horror.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.13
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.18
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.67
      pick: 0.17
      fit: 0.37
    Obsidian Shard:
      total: 0.6
      efficiency: 0.52
      win: 0.78
      pick: 0.13
      fit: 0.37
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Oni Hunter's Garb
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Obsidian
    Shard, Gluttonous Grimoire, Kinetic Cuirass, Soul Gem, Amanita Charm, Nimble Ring,
    Freya''s Tears, Oni Hunter''s Garb, Death Metal, Spear of the Magus, Shield of
    the Phoenix, Helm of Radiance, Spectral Armor, Rod of Asclepius, Erosion, Chronos''
    Pendant, Eye of Providence, Jade Scepter, Draconic Scale, Shifter''s Shield, Yogi''s
    Necklace, Triton''s Conch, The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.69
      win: 0.39
      pick: 0.2
      fit: 0.28
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.45
    Oni Hunter's Garb:
      total: 0.5
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.67
      pick: 0.17
      fit: 0.37
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.78
      pick: 0.13
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Obsidian Shard, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Freya''s
    Tears, Amanita Charm, Nimble Ring, Shield of the Phoenix, Spear of the Magus,
    Oni Hunter''s Garb, Spectral Armor, Death Metal, Erosion, Helm of Radiance, Chronos''
    Pendant, Eye of Providence, Rod of Asclepius, Draconic Scale, Shifter''s Shield,
    Screeching Gargoyle, Leviathan''s Hide, Midgardian Mail, The Cosmic Horror.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.54
      pick: 0.13
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.53
      pick: 0.18
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.67
      pick: 0.17
      fit: 0.35
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.78
      pick: 0.13
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Freya''s Tears, Chandra''s Grace, Nimble Ring,
    Blood-Bound Book, Oni Hunter''s Garb, Lifebinder, Bancroft''s Talon, Spear of
    the Magus, Phoenix Feather, Erosion, Spectral Armor, Eye of Providence, Draconic
    Scale, Shifter''s Shield, Helm of Radiance, Jade Scepter, The Cosmic Horror.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.13
      fit: 0.44
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.67
      pick: 0.17
      fit: 0.37
    Obsidian Shard:
      total: 0.6
      efficiency: 0.52
      win: 0.78
      pick: 0.13
      fit: 0.37
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Obsidian Shard, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass,
    Amanita Charm, Freya''s Tears, Spear of the Magus, Screeching Gargoyle, Stone
    of Binding, Nimble Ring, Void Shield, Shield of the Phoenix, Oni Hunter''s Garb,
    Void Stone, Spectral Armor, Erosion, Helm of Radiance, Eye of Providence, Rod
    of Asclepius, Draconic Scale, Shifter''s Shield, Doom Orb, The Cosmic Horror.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.54
      pick: 0.13
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.53
      pick: 0.18
      fit: 0.59
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.77
      win: 0.67
      pick: 0.17
      fit: 0.48
    Obsidian Shard:
      total: 0.61
      efficiency: 0.52
      win: 0.78
      pick: 0.13
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Soul Gem, Kinetic Cuirass, Amanita
    Charm, Freya''s Tears, Oni Hunter''s Garb, Shield of the Phoenix, Spear of the
    Magus, Spectral Armor, Death Metal, Helm of Radiance, Erosion, Rod of Asclepius,
    Eye of Providence, Chronos'' Pendant, Bracer of The Abyss, Leviathan''s Hide,
    Blood-Bound Book, Draconic Scale, Midgardian Mail, Shifter''s Shield, The Cosmic
    Horror.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.45
      efficiency: 0.42
      win: 0.53
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.67
      pick: 0.17
      fit: 0.22
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.78
      pick: 0.13
      fit: 0.22
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Soul Gem, Gluttonous
    Grimoire, Shield of the Phoenix, Kinetic Cuirass, Amanita Charm, Nimble Ring,
    Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Chandra''s Grace,
    Gladiator''s Shield, Spectral Armor, Erosion, Eye of Providence, Spear of the
    Magus, Prophetic Cloak, Draconic Scale, Shifter''s Shield, Gem of Focus, Leviathan''s
    Hide, Helm of Radiance, The Cosmic Horror.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.13
      fit: 0.56
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.18
      fit: 0.53
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.67
      pick: 0.17
      fit: 0.23
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.78
      pick: 0.13
      fit: 0.23
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Freya''s Tears, Nimble Ring, Shield of the Phoenix, Oni Hunter''s Garb,
    The Cosmic Horror, Spear of the Magus, Erosion, Shifter''s Shield, Eye of Providence,
    Spectral Armor, Helm of Radiance, Draconic Scale, Rod of Asclepius, Chronos''
    Pendant, Leviathan''s Hide, Obsidian Shard, Jade Scepter, Midgardian Mail, Screeching
    Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.69
      win: 0.39
      pick: 0.2
      fit: 0.31
    Breastplate of Valor:
      total: 0.42
      efficiency: 0.64
      win: 0.32
      pick: 0.18
      fit: 0.31
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.13
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.67
      pick: 0.17
      fit: 0.37
  starter: *id001
---
