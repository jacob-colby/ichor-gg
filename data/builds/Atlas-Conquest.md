---
type: smite-build
god: Atlas
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unburdened
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.56
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.2
    win_rate: 0.62
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.53
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.79
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.57
    - name: Ethereal Staff
      pick_rate: 0.08
      win_rate: 0.8
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.87
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.56
    - name: The World Stone
      pick_rate: 0.08
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.27
  - name: Ethereal Staff
    pick_rate: 0.05
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.78
    - name: Contagion
      pick_rate: 0.05
      win_rate: 0.43
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.6
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.49
  - name: Bluestone Brooch
    pick_rate: 0.2
    win_rate: 0.62
  - name: Selflessness
    pick_rate: 0.09
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/atlas/
  last_verified: '2026-08-15'
  god_win_rate: 0.6141304347826086
  god_matches_won: 113
  god_matches_played: 184
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
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
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Prophetic Cloak, Rod
    of Tahuti, Gluttonous Grimoire, Erosion, Shield of the Phoenix, Eye of Providence,
    Oni Hunter''s Garb, Draconic Scale, Spectral Armor, Leviathan''s Hide, Mantle
    Of Discord, Midgardian Mail, Soul Gem, Stone of Binding, Nimble Ring, Magi''s
    Cloak, Gladiator''s Shield, Ancile, Helm of Radiance, Screeching Gargoyle, Hide
    of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.81
    Prophetic Cloak:
      total: 0.61
      efficiency: 0.43
      win: 0.79
      pick: 0.1
      fit: 0.64
    Freya's Tears:
      total: 0.7
      efficiency: 0.59
      win: 0.87
      pick: 0.12
      fit: 0.64
    Shifter's Shield:
      total: 0.58
      efficiency: 0.52
      win: 0.62
      pick: 0.2
      fit: 0.71
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Gluttonous Grimoire, Rod of Tahuti, Chandra''s Grace, Rod of Asclepius,
    Oni Hunter''s Garb, Erosion, Eye of Providence, Draconic Scale, Phoenix Feather,
    Spectral Armor, Leviathan''s Hide, Midgardian Mail, Lifebinder, Glorious Pridwen,
    Nimble Ring, Gladiator''s Shield, Ancile, Blood-Bound Book, Hide of the Nemean
    Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.36
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.8
    Prophetic Cloak:
      total: 0.6
      efficiency: 0.43
      win: 0.79
      pick: 0.1
      fit: 0.57
    Shield of the Phoenix:
      total: 0.62
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.69
      efficiency: 0.59
      win: 0.87
      pick: 0.12
      fit: 0.57
    Amanita Charm:
      total: 0.65
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Prophetic Cloak
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: Freya''s Tears, Rod of Tahuti, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, Soul Gem, Stone of Binding, Screeching Gargoyle, Void Shield, The
    Cosmic Horror, Spear of the Magus, Oni Hunter''s Garb, Void Stone, Shield of the
    Phoenix, Spear of Desolation, Erosion, Eye of Providence, Spectral Armor, Nimble
    Ring, Draconic Scale, Obsidian Shard, Leviathan''s Hide, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.59
    Prophetic Cloak:
      total: 0.58
      efficiency: 0.43
      win: 0.79
      pick: 0.1
      fit: 0.44
    Freya's Tears:
      total: 0.67
      efficiency: 0.59
      win: 0.87
      pick: 0.12
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.62
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Nimble Ring, Rod of Tahuti, Kinetic Cuirass, Amanita
    Charm, Gluttonous Grimoire, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix,
    Spectral Armor, Erosion, Eye of Providence, Draconic Scale, Leviathan''s Hide,
    Midgardian Mail, Helm of Radiance, Mantle Of Discord, Stone of Binding, Death
    Metal, Screeching Gargoyle, The Cosmic Horror, Yogi''s Necklace, Bracer of The
    Abyss, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.2
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.42
      win: 0.62
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.87
      pick: 0.12
      fit: 0.33
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.62
      pick: 0.0
      fit: 0.08
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shield of the Phoenix
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Shield of the Phoenix
  - Rod of Tahuti
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Prophetic Cloak, Kinetic
    Cuirass, Shield of the Phoenix, Rod of Tahuti, Amanita Charm, Soul Gem, Gluttonous
    Grimoire, Screeching Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring,
    Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Spectral
    Armor, Eye of Providence, Draconic Scale, Leviathan''s Hide, Gem of Focus, Helm
    of Radiance, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.55
    Prophetic Cloak:
      total: 0.61
      efficiency: 0.43
      win: 0.79
      pick: 0.1
      fit: 0.64
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.7
      efficiency: 0.59
      win: 0.87
      pick: 0.12
      fit: 0.64
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.62
      pick: 0.0
      fit: 0.13
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Erosion
  flex_slots:
  - Rod of Tahuti
  - Erosion
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Rod of
    Tahuti, Gluttonous Grimoire, Erosion, Shield of the Phoenix, Eye of Providence,
    Oni Hunter''s Garb, Draconic Scale, Spectral Armor, Leviathan''s Hide, Mantle
    Of Discord, Midgardian Mail, Soul Gem, Stone of Binding, Nimble Ring, Magi''s
    Cloak, Gladiator''s Shield, Ancile, Helm of Radiance, Prophetic Cloak, Screeching
    Gargoyle, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.7
      efficiency: 0.59
      win: 0.87
      pick: 0.12
      fit: 0.64
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.62
      pick: 0.0
      fit: 0.15
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.57
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.71
  starter: *id001
---
