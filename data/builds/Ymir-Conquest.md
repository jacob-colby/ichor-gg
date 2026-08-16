---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.66
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.11
      win_rate: 0.67
    - name: Resolute Mantle
      pick_rate: 0.1
      win_rate: 0.64
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.46
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.65
  - name: Stampede
    pick_rate: 0.13
    win_rate: 0.65
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.54
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.67
  - name: Spirit Robe
    pick_rate: 0.07
    win_rate: 0.63
    alternates:
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.56
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.68
    alternates:
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.67
    - name: Spirit Robe
      pick_rate: 0.04
      win_rate: 0.78
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.75
    - name: Medallion
      pick_rate: 0.04
      win_rate: 0.67
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.18
    win_rate: 0.68
  - name: Sundering Axe
    pick_rate: 0.13
    win_rate: 0.69
  - name: Selflessness
    pick_rate: 0.11
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-08-16'
  god_win_rate: 0.5686274509803921
  god_matches_won: 145
  god_matches_played: 255
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Draconic Scale, Breastplate
    of Valor, Erosion, Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb,
    Rod of Tahuti, Gluttonous Grimoire, Spectral Armor, Nimble Ring, Leviathan''s
    Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding, Magi''s Cloak, Ancile,
    Gladiator''s Shield, Soul Gem, Helm of Radiance, Prophetic Cloak, Hide of the
    Nemean Lion, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.64
      win: 0.67
      pick: 0.11
      fit: 0.39
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.59
      efficiency: 0.52
      win: 0.66
      pick: 0.17
      fit: 0.72
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.72
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.66
      pick: 0.0
      fit: 0.72
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
  - Draconic Scale
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Draconic Scale,
    Soul Gem, Chandra''s Grace, Rod of Asclepius, Freya''s Tears, Gluttonous Grimoire,
    Breastplate of Valor, Oni Hunter''s Garb, Erosion, Eye of Providence, Rod of Tahuti,
    Phoenix Feather, Spectral Armor, Leviathan''s Hide, Nimble Ring, Midgardian Mail,
    Lifebinder, Glorious Pridwen, Gladiator''s Shield, Ancile, Blood-Bound Book, Hide
    of the Nemean Lion.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.57
      win: 0.66
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.57
    Shifter's Shield:
      total: 0.59
      efficiency: 0.52
      win: 0.66
      pick: 0.17
      fit: 0.7
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.7
    Amanita Charm:
      total: 0.66
      efficiency: 0.63
      win: 0.66
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Stone of Binding, Breastplate of Valor, Screeching Gargoyle, Freya''s
    Tears, Void Shield, The Cosmic Horror, Oni Hunter''s Garb, Spear of the Magus,
    Draconic Scale, Void Stone, Shield of the Phoenix, Spear of Desolation, Nimble
    Ring, Erosion, Eye of Providence, Spectral Armor, Obsidian Shard, Leviathan''s
    Hide, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.47
      win: 0.66
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.22
      fit: 0.25
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.67
      pick: 0.11
      fit: 0.25
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.63
      win: 0.66
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.66
      pick: 0.0
      fit: 0.4
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Gluttonous
    Grimoire, Breastplate of Valor, Freya''s Tears, Oni Hunter''s Garb, Shield of
    the Phoenix, Draconic Scale, Soul Gem, Spectral Armor, Erosion, Eye of Providence,
    Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Helm of Radiance, Stone
    of Binding, Death Metal, Screeching Gargoyle, Bracer of The Abyss, Ancile, Yogi''s
    Necklace, Rod of Asclepius.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.67
      pick: 0.11
      fit: 0.2
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.48
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.51
      win: 0.66
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.58
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.51
      efficiency: 0.42
      win: 0.66
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.66
      pick: 0.0
      fit: 0.38
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
  - Shield of the Phoenix
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Freya''s Tears,
    Kinetic Cuirass, Shield of the Phoenix, Amanita Charm, Rod of Tahuti, Soul Gem,
    Gluttonous Grimoire, Nimble Ring, Screeching Gargoyle, Oni Hunter''s Garb, Draconic
    Scale, Chronos'' Pendant, Chandra''s Grace, Gladiator''s Shield, Erosion, Spectral
    Armor, Eye of Providence, Spear of Desolation, Prophetic Cloak, Leviathan''s Hide,
    Gem of Focus, Helm of Radiance, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.61
      pick: 0.22
      fit: 0.48
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.64
      win: 0.67
      pick: 0.11
      fit: 0.48
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.66
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.66
      pick: 0.17
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Runeforged Hammer
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, The Crusher, Jotunn''s Revenge,
    Kinetic Cuirass, Gluttonous Grimoire, Amanita Charm, Runeforged Hammer, Breastplate
    of Valor, Freya''s Tears, Nimble Ring, Shield Splitter, Hydra''s Lament, Soul
    Gem, Oni Hunter''s Garb, Golden Blade, Eye of the Storm, Draconic Scale, Shield
    of the Phoenix, Pharaoh''s Curse, Erosion, Spectral Armor, Eye of Providence,
    The Reaper, Lernaean Bow, Death Metal, Avenging Blade, The Cosmic Horror, Damaru,
    Shogun''s Ofuda, Leviathan''s Hide, Spear of the Magus, Midgardian Mail, Mantle
    Of Discord, Stone of Binding, Helm of Radiance, Spear of Desolation, Tekko-Kagi,
    Tyrfing, Berserker''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.67
      pick: 0.11
      fit: 0.22
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.66
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.52
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.66
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.59
      efficiency: 0.64
      win: 0.66
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Breastplate of Valor
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Soul Gem, Nimble
    Ring, Breastplate of Valor, Runeforged Hammer, Freya''s Tears, Oni Hunter''s Garb,
    The Cosmic Horror, Death Metal, Shield Splitter, Draconic Scale, Shield of the
    Phoenix, Spear of the Magus, Hydra''s Lament, Erosion, Helm of Radiance, Spectral
    Armor, Spear of Desolation, Eye of the Storm, Eye of Providence, Pharaoh''s Curse,
    Rod of Asclepius, Golden Blade, The Reaper, Leviathan''s Hide, Obsidian Shard,
    Jade Scepter, Chronos'' Pendant, Midgardian Mail, Avenging Blade, Damaru, Mantle
    Of Discord, Stone of Binding, Berserker''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.22
      fit: 0.22
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.67
      pick: 0.11
      fit: 0.22
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.66
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.63
      win: 0.66
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.66
      pick: 0.0
      fit: 0.42
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
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Erosion,
    Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb, Draconic Scale,
    Rod of Tahuti, Breastplate of Valor, Gluttonous Grimoire, Spectral Armor, Nimble
    Ring, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding,
    Magi''s Cloak, Ancile, Gladiator''s Shield, Soul Gem, Helm of Radiance, Prophetic
    Cloak, Hide of the Nemean Lion, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.22
      fit: 0.39
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.66
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.59
      efficiency: 0.52
      win: 0.66
      pick: 0.17
      fit: 0.72
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.66
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.58
      efficiency: 0.52
      win: 0.66
      pick: 0.0
      fit: 0.72
  starter: *id001
---
