---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.72
  aspect_win_rate: 0.54
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.16
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.57
    - name: Lifebinder
      pick_rate: 0.09
      win_rate: 0.41
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.41
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.53
  - name: Breastplate of Valor
    pick_rate: 0.08
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.45
    - name: The World Stone
      pick_rate: 0.05
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.11
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.61
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.59
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.64
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.64
  - name: Shield
    pick_rate: 0.04
    win_rate: 0.43
    alternates:
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.57
    - name: Soul Reaver
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.42
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.52
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-08-21'
  god_win_rate: 0.5146666666666667
  god_matches_won: 193
  god_matches_played: 375
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass, Shifter''s Shield,
    Soul Gem, Freya''s Tears, Breastplate of Valor, Shield of the Phoenix, Spear of
    the Magus, Helm of Radiance, Obsidian Shard, Nimble Ring, Mantle Of Discord, Stone
    of Binding, Erosion, Ethereal Staff, Rod of Asclepius, Eye of Providence, Spectral
    Armor, Draconic Scale, Death Metal, Chronos'' Pendant, Jade Scepter, Leviathan''s
    Hide, Doom Orb, The Cosmic Horror.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.62
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.14
      fit: 0.49
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.16
      fit: 0.51
    Soul Reaver:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.12
      fit: 0.4
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.51
      pick: 0.18
      fit: 0.37
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Amanita Charm, Kinetic Cuirass, Breastplate of Valor, Soul Gem, Shifter''s
    Shield, Death Metal, Freya''s Tears, Spear of the Magus, Nimble Ring, Helm of
    Radiance, Obsidian Shard, Shield of the Phoenix, Ethereal Staff, Rod of Asclepius,
    Wish-Granting Pearl, Mantle Of Discord, Stone of Binding, Doom Orb, Ancient Signet,
    Spectral Armor, Chronos'' Pendant, Jade Scepter, Erosion, The Cosmic Horror, The
    World Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.12
      fit: 0.28
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.55
      pick: 0.16
      fit: 0.4
    Soul Reaver:
      total: 0.66
      efficiency: 0.4
      win: 1.0
      pick: 0.12
      fit: 0.45
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.51
      pick: 0.18
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Freya''s Tears, Shifter''s Shield, Spear of the Magus, Obsidian Shard,
    Shield of the Phoenix, Death Metal, Nimble Ring, Helm of Radiance, Mantle Of Discord,
    Stone of Binding, Ethereal Staff, Doom Orb, The Cosmic Horror, Spectral Armor,
    Rod of Asclepius, Erosion, Chronos'' Pendant, Screeching Gargoyle, Eye of Providence,
    Draconic Scale, The World Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.12
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.16
      fit: 0.49
    Soul Reaver:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.12
      fit: 0.34
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.51
      pick: 0.18
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Ethereal Staff, Rod of Asclepius, Kinetic Cuirass, Shifter''s Shield, Freya''s
    Tears, Breastplate of Valor, Spear of the Magus, Chandra''s Grace, Blood-Bound
    Book, Obsidian Shard, Phoenix Feather, Helm of Radiance, Nimble Ring, Sphere of
    Negation, Yogi''s Necklace, Bancroft''s Talon, Erosion, Spectral Armor, Eye of
    Providence, Mantle Of Discord, Stone of Binding, Lifebinder.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.16
      fit: 0.51
    Soul Reaver:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.12
      fit: 0.4
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.51
      pick: 0.18
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
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
  - Stone of Binding
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Stone of Binding, Amanita Charm,
    Kinetic Cuirass, Spear of the Magus, Shifter''s Shield, Obsidian Shard, Screeching
    Gargoyle, Freya''s Tears, Breastplate of Valor, Void Shield, Void Stone, Doom
    Orb, Shield of the Phoenix, The Cosmic Horror, Helm of Radiance, Nimble Ring,
    Dreamer''s Idol, Mantle Of Discord, Ethereal Staff, The World Stone, Rod of Asclepius,
    Spectral Armor, Erosion, Death Metal.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.68
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.16
      fit: 0.59
    Soul Reaver:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.12
      fit: 0.37
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.51
      pick: 0.18
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Soul Reaver
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Kinetic Cuirass, Soul
    Gem, Breastplate of Valor, Shifter''s Shield, Freya''s Tears, Death Metal, Spear
    of the Magus, Helm of Radiance, Shield of the Phoenix, Obsidian Shard, Mantle
    Of Discord, Stone of Binding, Ethereal Staff, Rod of Asclepius, Spectral Armor,
    Bragi''s Harp, Bracer of The Abyss, Erosion, Chronos'' Pendant, Leviathan''s Hide,
    Daybreak Gavel, Screeching Gargoyle, Eye of Providence.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.46
    Soul Reaver:
      total: 0.64
      efficiency: 0.4
      win: 1.0
      pick: 0.12
      fit: 0.32
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.51
      pick: 0.18
      fit: 0.22
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Soul Gem, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire,
    Shifter''s Shield, Screeching Gargoyle, Chronos'' Pendant, Spear of the Magus,
    Mantle Of Discord, Stone of Binding, Helm of Radiance, Nimble Ring, Death Metal,
    Obsidian Shard, Prophetic Cloak, Spectral Armor, Erosion, Gladiator''s Shield,
    Eye of Providence, Chandra''s Grace, Gem of Focus, Draconic Scale, Leviathan''s
    Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.12
      fit: 0.43
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.55
      pick: 0.16
      fit: 0.53
    Soul Reaver:
      total: 0.64
      efficiency: 0.4
      win: 1.0
      pick: 0.12
      fit: 0.29
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.51
      pick: 0.18
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
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass,
    Soul Gem, Freya''s Tears, Breastplate of Valor, Shield of the Phoenix, Spear of
    the Magus, Shifter''s Shield, Helm of Radiance, Obsidian Shard, Nimble Ring, Mantle
    Of Discord, Stone of Binding, Erosion, Ethereal Staff, Rod of Asclepius, Eye of
    Providence, Spectral Armor, Draconic Scale, Death Metal, Chronos'' Pendant, Jade
    Scepter, Leviathan''s Hide, Doom Orb, The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.16
      fit: 0.51
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.51
      pick: 0.18
      fit: 0.37
  starter: *id001
---
