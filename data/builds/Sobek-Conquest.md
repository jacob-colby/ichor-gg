---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.36
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.31
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.52
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.51
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.49
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.54
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.5
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.52
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.6
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.58
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.6
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.54
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.59
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.51
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.61
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.37
    win_rate: 0.47
  - name: Bluestone Brooch
    pick_rate: 0.27
    win_rate: 0.58
  - name: Selflessness
    pick_rate: 0.12
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-08-21'
  god_win_rate: 0.5189591078066914
  god_matches_won: 698
  god_matches_played: 1345
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Draconic Scale, Breastplate
    of Valor, Shield of the Phoenix, Erosion, Mantle Of Discord, Stone of Binding,
    Eye of Providence, Gluttonous Grimoire, Spectral Armor, Magi''s Cloak, Leviathan''s
    Hide, Helm of Radiance, Soul Gem, Midgardian Mail, Screeching Gargoyle, Doublet
    of Binding, Prophetic Cloak, Void Shield, Ancile, Nimble Ring, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.26
      fit: 0.35
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.15
      fit: 0.58
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.17
      fit: 0.64
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.56
      pick: 0.13
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.64
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Soul Gem, Ethereal Staff, Draconic Scale, Rod of Asclepius, Gluttonous Grimoire,
    Breastplate of Valor, Phoenix Feather, Erosion, Chandra''s Grace, Eye of Providence,
    Spectral Armor, Mantle Of Discord, Stone of Binding, Yogi''s Necklace, Leviathan''s
    Hide, Glorious Pridwen, Lifebinder, Midgardian Mail, Helm of Radiance, Blood-Bound
    Book, Doublet of Binding.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.86
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.52
      pick: 0.15
      fit: 0.51
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.17
      fit: 0.62
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.56
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Screeching Gargoyle
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Stone of Binding, Amanita Charm,
    Kinetic Cuirass, Soul Gem, Screeching Gargoyle, Spear of Desolation, Spear of
    the Magus, Void Shield, Draconic Scale, Breastplate of Valor, Obsidian Shard,
    Void Stone, Shield of the Phoenix, Mantle Of Discord, Erosion, Eye of Providence,
    Spectral Armor, Doom Orb, The Cosmic Horror, Helm of Radiance, The World Stone,
    Leviathan''s Hide, Nimble Ring, Magi''s Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.53
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.73
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.15
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.52
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Nimble Ring, Gluttonous
    Grimoire, Breastplate of Valor, Draconic Scale, Soul Gem, Shield of the Phoenix,
    Mantle Of Discord, Stone of Binding, Death Metal, Spectral Armor, Helm of Radiance,
    Erosion, Eye of Providence, Leviathan''s Hide, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, Spear of the Magus, Spear of Desolation, Ethereal Staff, Bragi''s
    Harp, Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.52
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.52
      pick: 0.15
      fit: 0.33
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Spear of Desolation,
    Draconic Scale, Gluttonous Grimoire, Screeching Gargoyle, Chronos'' Pendant, Mantle
    Of Discord, Stone of Binding, Prophetic Cloak, Helm of Radiance, Erosion, Spectral
    Armor, Death Metal, Nimble Ring, Eye of Providence, Gladiator''s Shield, Chandra''s
    Grace, Leviathan''s Hide, Gem of Focus, Ethereal Staff, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.49
      pick: 0.26
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.52
      pick: 0.15
      fit: 0.6
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Breastplate
    of Valor, Shield of the Phoenix, Erosion, Mantle Of Discord, Stone of Binding,
    Eye of Providence, Gluttonous Grimoire, Draconic Scale, Spectral Armor, Magi''s
    Cloak, Leviathan''s Hide, Helm of Radiance, Soul Gem, Midgardian Mail, Screeching
    Gargoyle, Doublet of Binding, Prophetic Cloak, Void Shield, Ancile, Nimble Ring,
    Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.26
      fit: 0.35
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.15
      fit: 0.58
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.17
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.64
  starter: *id001
---
