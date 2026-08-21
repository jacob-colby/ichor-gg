---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.57
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.25
    win_rate: 0.58
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.23
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.46
  - name: Genji's Guard
    pick_rate: 0.23
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.15
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.6
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.52
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.48
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.71
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.68
  - name: Sage's Ring
    pick_rate: 0.06
    win_rate: 0.6
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.58
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.44
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.33
    win_rate: 0.49
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.65
  - name: Conduit Gem
    pick_rate: 0.15
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-08-21'
  god_win_rate: 0.5441640378548895
  god_matches_won: 345
  god_matches_played: 634
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
  - Breastplate of Valor
  - Kinetic Cuirass
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Gluttonous Grimoire,
    Draconic Scale, Shield of the Phoenix, Erosion, Oni Hunter''s Garb, Freya''s Tears,
    Eye of Providence, Nimble Ring, Spectral Armor, Soul Gem, Leviathan''s Hide, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Magi''s Cloak, Helm of Radiance, Ancile,
    Screeching Gargoyle, Gladiator''s Shield, Hide of the Nemean Lion, Void Shield,
    Doublet of Binding, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.31
      fit: 0.35
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.57
      pick: 0.15
      fit: 0.35
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.73
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.25
      fit: 0.63
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.58
      pick: 0.13
      fit: 0.63
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.63
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Rod of Tahuti, Ethereal Staff, Rod of Asclepius, Chandra''s Grace, Yogi''s
    Necklace, Oni Hunter''s Garb, Draconic Scale, Erosion, Eye of Providence, Nimble
    Ring, Phoenix Feather, Spectral Armor, Freya''s Tears, Leviathan''s Hide, Lifebinder,
    Midgardian Mail, Blood-Bound Book, Glorious Pridwen, Bancroft''s Talon, Ancile,
    Gladiator''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.57
      pick: 0.15
      fit: 0.31
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.85
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.43
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.25
      fit: 0.61
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Screeching Gargoyle
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Stone of Binding, Screeching Gargoyle, Void Shield, The Cosmic Horror,
    Nimble Ring, Oni Hunter''s Garb, Spear of the Magus, Void Stone, Shield of the
    Phoenix, Obsidian Shard, Spear of Desolation, Draconic Scale, Freya''s Tears,
    Erosion, Spectral Armor, Eye of Providence, Leviathan''s Hide, Midgardian Mail,
    Mantle Of Discord, Helm of Radiance, Ancile.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.53
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.72
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.57
      pick: 0.15
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.57
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Rod of Tahuti, Kinetic Cuirass, Amanita Charm, Gluttonous
    Grimoire, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Draconic Scale,
    Freya''s Tears, Spectral Armor, Erosion, Eye of Providence, Leviathan''s Hide,
    Midgardian Mail, Helm of Radiance, Mantle Of Discord, Stone of Binding, Death
    Metal, Screeching Gargoyle, Ethereal Staff, The Cosmic Horror, Yogi''s Necklace,
    Bracer of The Abyss, Ancile, Rod of Asclepius.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.57
      pick: 0.15
      fit: 0.2
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.47
      efficiency: 0.42
      win: 0.57
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Kinetic Cuirass, Shield
    of the Phoenix, Amanita Charm, Freya''s Tears, Soul Gem, Gluttonous Grimoire,
    Nimble Ring, Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Chandra''s
    Grace, Draconic Scale, Spear of Desolation, Gladiator''s Shield, Erosion, Spectral
    Armor, Eye of Providence, Totem of Death, Prophetic Cloak, Leviathan''s Hide,
    Helm of Radiance, Gem of Focus, Midgardian Mail, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.31
      fit: 0.45
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.15
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.52
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.13
      fit: 0.59
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.25
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, The Crusher, Jotunn''s Revenge,
    Kinetic Cuirass, Gluttonous Grimoire, Berserker''s Shield, Amanita Charm, Nimble
    Ring, Runeforged Hammer, Shield Splitter, Soul Gem, Hydra''s Lament, Oni Hunter''s
    Garb, Golden Blade, Shield of the Phoenix, Eye of the Storm, Draconic Scale, Freya''s
    Tears, Pharaoh''s Curse, Erosion, Spectral Armor, Eye of Providence, Death Metal,
    The Reaper, Lernaean Bow, The Cosmic Horror, Avenging Blade, Damaru, Leviathan''s
    Hide, Spear of the Magus, Shogun''s Ofuda, Heartseeker, Midgardian Mail, Obsidian
    Shard, Dominance, Titan''s Bane, Mantle Of Discord, Spear of Desolation, Stone
    of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.57
      pick: 0.15
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Berserker''s Shield,
    Nimble Ring, Soul Gem, Oni Hunter''s Garb, The Cosmic Horror, Runeforged Hammer,
    Shield of the Phoenix, Hydra''s Lament, Death Metal, Spear of the Magus, Shield
    Splitter, Draconic Scale, Obsidian Shard, Freya''s Tears, Spectral Armor, Helm
    of Radiance, Erosion, Spear of Desolation, Pharaoh''s Curse, Eye of the Storm,
    Golden Blade, Eye of Providence, Ethereal Staff, Rod of Asclepius, The Reaper,
    Leviathan''s Hide, Chronos'' Pendant, Jade Scepter, Lernaean Bow, Midgardian Mail,
    Shogun''s Ofuda, Damaru, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.57
      pick: 0.15
      fit: 0.21
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Shifter's Shield
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Rod of
    Tahuti, Gluttonous Grimoire, Shield of the Phoenix, Erosion, Oni Hunter''s Garb,
    Eye of Providence, Draconic Scale, Nimble Ring, Spectral Armor, Soul Gem, Leviathan''s
    Hide, Midgardian Mail, Mantle Of Discord, Stone of Binding, Magi''s Cloak, Helm
    of Radiance, Ancile, Screeching Gargoyle, Gladiator''s Shield, Hide of the Nemean
    Lion, Void Shield, Doublet of Binding, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.31
      fit: 0.35
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.13
      fit: 0.57
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.25
      fit: 0.63
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.63
  starter: *id001
---
