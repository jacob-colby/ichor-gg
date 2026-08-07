---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.47
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.16
    win_rate: 0.44
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.53
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.35
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.44
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.43
  - name: The World Stone
    pick_rate: 0.1
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.49
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.42
  - name: Rod of Tahuti
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.38
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.57
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.57
    alternates:
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.52
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.58
  - name: Medal of Defense
    pick_rate: 0.05
    win_rate: 0.57
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.04
      win_rate: 0.54
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.42
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.43
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.37
  - name: Pendulum of The Ages
    pick_rate: 0.08
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-08-07'
  god_win_rate: 0.46048109965635736
  god_matches_won: 268
  god_matches_played: 582
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-07'
  god_matches_analyzed: 13100
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Genji''s Guard, Freya''s
    Tears, Gluttonous Grimoire, Oni Hunter''s Garb, Erosion, Shield of the Phoenix,
    Draconic Scale, Hide of the Nemean Lion, Spectral Armor, Breastplate of Valor,
    Soul Gem, Leviathan''s Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail,
    Yogi''s Necklace, Helm of Radiance, Rod of Asclepius, Magi''s Cloak, Stampede,
    Ancile, Gladiator''s Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.13
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.81
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.05
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Soul Gem, Genji''s Guard, Gluttonous Grimoire, Rod of Asclepius, Freya''s Tears,
    Oni Hunter''s Garb, Chandra''s Grace, Erosion, Draconic Scale, Hide of the Nemean
    Lion, Phoenix Feather, Spectral Armor, Lifebinder, Yogi''s Necklace, Leviathan''s
    Hide, Blood-Bound Book, Midgardian Mail, Bancroft''s Talon, Breastplate of Valor,
    Glorious Pridwen, Jade Scepter, Stampede.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.13
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.05
      fit: 0.57
    Amanita Charm:
      total: 0.61
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Freya's Tears
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass, Genji''s Guard,
    Soul Gem, Eye of Providence, Freya''s Tears, Stone of Binding, Oni Hunter''s Garb,
    Spear of the Magus, Screeching Gargoyle, Void Shield, The Cosmic Horror, Shield
    of the Phoenix, Void Stone, Spear of Desolation, Erosion, Spectral Armor, Draconic
    Scale, Obsidian Shard, Yogi''s Necklace, Breastplate of Valor, Leviathan''s Hide,
    Helm of Radiance, Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Eye of Providence:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.13
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.52
      pick: 0.05
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Eye of Providence, Freya''s Tears, Oni Hunter''s Garb, Soul Gem, Shield of the
    Phoenix, Hide of the Nemean Lion, Spectral Armor, Yogi''s Necklace, Erosion, Breastplate
    of Valor, Bracer of The Abyss, Death Metal, Draconic Scale, Rod of Asclepius,
    Helm of Radiance, Leviathan''s Hide, Bragi''s Harp, Midgardian Mail, Spear of
    the Magus, Jade Scepter, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.13
      fit: 0.2
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Eye of Providence
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Freya''s Tears, Amanita
    Charm, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Gluttonous Grimoire,
    Eye of Providence, Breastplate of Valor, Oni Hunter''s Garb, Chronos'' Pendant,
    Screeching Gargoyle, Chandra''s Grace, Spear of Desolation, Gladiator''s Shield,
    Spectral Armor, Erosion, Yogi''s Necklace, Draconic Scale, Helm of Radiance, Rod
    of Asclepius, Gem of Focus, Death Metal, Leviathan''s Hide, Jade Scepter, Prophetic
    Cloak.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.13
      fit: 0.48
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.44
      pick: 0.1
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.05
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Genji''s
    Guard, Freya''s Tears, Gluttonous Grimoire, Oni Hunter''s Garb, Erosion, Shield
    of the Phoenix, Breastplate of Valor, Draconic Scale, Spectral Armor, Soul Gem,
    Leviathan''s Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail, Yogi''s
    Necklace, Hide of the Nemean Lion, Helm of Radiance, Rod of Asclepius, Magi''s
    Cloak, Stampede, Ancile, Gladiator''s Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.13
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.05
      fit: 0.64
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.44
      pick: 0.16
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
---
