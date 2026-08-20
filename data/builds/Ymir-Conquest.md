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
    pick_rate: 0.18
    win_rate: 0.61
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.5
    - name: Resolute Mantle
      pick_rate: 0.1
      win_rate: 0.63
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.61
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.6
    - name: Spirit Robe
      pick_rate: 0.09
      win_rate: 0.52
  - name: Stampede
    pick_rate: 0.11
    win_rate: 0.66
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.59
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.7
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.62
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.7
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.63
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.62
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.61
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.63
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.64
    - name: Medallion
      pick_rate: 0.04
      win_rate: 0.56
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.18
    win_rate: 0.66
  - name: Sundering Axe
    pick_rate: 0.12
    win_rate: 0.7
  - name: Selflessness
    pick_rate: 0.11
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-08-20'
  god_win_rate: 0.5553145336225597
  god_matches_won: 256
  god_matches_played: 461
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-20'
  god_matches_analyzed: 11556
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
  - Shifter's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Draconic Scale, Erosion,
    Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb, Rod of Tahuti, Breastplate
    of Valor, Gluttonous Grimoire, Spectral Armor, Nimble Ring, Leviathan''s Hide,
    Mantle Of Discord, Midgardian Mail, Stone of Binding, Hide of the Nemean Lion,
    Magi''s Cloak, Ancile, Gladiator''s Shield, Soul Gem, Helm of Radiance, Prophetic
    Cloak, Void Shield, Screeching Gargoyle, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.61
      pick: 0.18
      fit: 0.72
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.62
      pick: 0.13
      fit: 0.72
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.72
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
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
    this god: Amanita Charm, Shield of the Phoenix, Freya''s Tears, Kinetic Cuirass,
    Soul Gem, Ethereal Staff, Chandra''s Grace, Rod of Asclepius, Gluttonous Grimoire,
    Draconic Scale, Oni Hunter''s Garb, Erosion, Yogi''s Necklace, Eye of Providence,
    Rod of Tahuti, Phoenix Feather, Spectral Armor, Breastplate of Valor, Leviathan''s
    Hide, Nimble Ring, Midgardian Mail, Hide of the Nemean Lion, Lifebinder, Glorious
    Pridwen, Gladiator''s Shield, Ancile, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.35
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.57
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.61
      pick: 0.18
      fit: 0.7
    Amanita Charm:
      total: 0.65
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Rod of Tahuti, Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass,
    Amanita Charm, Soul Gem, Stone of Binding, Screeching Gargoyle, Void Shield, The
    Cosmic Horror, Breastplate of Valor, Oni Hunter''s Garb, Spear of the Magus, Void
    Stone, Shield of the Phoenix, Obsidian Shard, Spear of Desolation, Nimble Ring,
    Draconic Scale, Erosion, Eye of Providence, Spectral Armor, Leviathan''s Hide,
    Midgardian Mail, Mantle Of Discord, Helm of Radiance, Ancile.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.25
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.61
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Nimble Ring, Kinetic Cuirass, Amanita Charm, Rod of
    Tahuti, Gluttonous Grimoire, Breastplate of Valor, Oni Hunter''s Garb, Shield
    of the Phoenix, Soul Gem, Draconic Scale, Spectral Armor, Erosion, Eye of Providence,
    Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Helm of Radiance, Stone
    of Binding, Death Metal, Screeching Gargoyle, Ethereal Staff, Bracer of The Abyss,
    Ancile, Yogi''s Necklace, Rod of Asclepius, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.2
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.48
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.42
      win: 0.61
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Kinetic Cuirass, Shield of the Phoenix, Amanita Charm, Rod of Tahuti, Soul Gem,
    Gluttonous Grimoire, Nimble Ring, Screeching Gargoyle, Oni Hunter''s Garb, Chronos''
    Pendant, Chandra''s Grace, Gladiator''s Shield, Draconic Scale, Erosion, Spectral
    Armor, Eye of Providence, Spear of Desolation, Prophetic Cloak, Totem of Death,
    Leviathan''s Hide, Gem of Focus, Helm of Radiance, Midgardian Mail, Mantle Of
    Discord, Stone of Binding.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.58
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Gluttonous Grimoire
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, The Crusher,
    Jotunn''s Revenge, Kinetic Cuirass, Gluttonous Grimoire, Berserker''s Shield,
    Amanita Charm, Nimble Ring, Runeforged Hammer, Shield Splitter, Breastplate of
    Valor, Hydra''s Lament, Soul Gem, Oni Hunter''s Garb, Golden Blade, Eye of the
    Storm, Shield of the Phoenix, Pharaoh''s Curse, Draconic Scale, Erosion, Spectral
    Armor, Eye of Providence, The Reaper, Lernaean Bow, Death Metal, Avenging Blade,
    The Cosmic Horror, Damaru, Shogun''s Ofuda, Leviathan''s Hide, Heartseeker, Spear
    of the Magus, Midgardian Mail, Dominance, Titan''s Bane, Obsidian Shard, Mantle
    Of Discord, Stone of Binding, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Gluttonous
    Grimoire, The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Berserker''s
    Shield, Soul Gem, Nimble Ring, Breastplate of Valor, Oni Hunter''s Garb, The Cosmic
    Horror, Runeforged Hammer, Death Metal, Shield Splitter, Shield of the Phoenix,
    Spear of the Magus, Hydra''s Lament, Obsidian Shard, Draconic Scale, Erosion,
    Helm of Radiance, Spectral Armor, Spear of Desolation, Eye of the Storm, Eye of
    Providence, Ethereal Staff, Pharaoh''s Curse, Rod of Asclepius, Golden Blade,
    The Reaper, Leviathan''s Hide, Jade Scepter, Chronos'' Pendant, Midgardian Mail,
    Avenging Blade, Damaru, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.61
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
    Cloak, Hide of the Nemean Lion, Void Shield, Screeching Gargoyle, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.61
      pick: 0.18
      fit: 0.72
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.57
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.72
  starter: *id001
---
