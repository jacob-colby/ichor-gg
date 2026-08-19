---
type: smite-build
god: Geb
mode: Conquest
builds:
- source: community
  aspect: Aspect of Calamity
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.17
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.29
    win_rate: 0.61
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.47
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.38
  - name: Genji's Guard
    pick_rate: 0.26
    win_rate: 0.54
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.64
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.46
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.22
      win_rate: 0.39
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.52
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.63
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.17
      win_rate: 0.52
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.67
  - name: Spirit Robe
    pick_rate: 0.08
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.39
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.64
  - name: Veve Charm
    pick_rate: 0.08
    win_rate: 0.83
    alternates:
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.36
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.37
    win_rate: 0.52
  - name: Heroism
    pick_rate: 0.28
    win_rate: 0.62
  - name: Hunter's Cowl
    pick_rate: 0.07
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-08-19'
  god_win_rate: 0.5218978102189781
  god_matches_won: 143
  god_matches_played: 274
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Erosion, Shifter''s Shield, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Oni Hunter''s Garb, Spectral Armor, Mantle
    Of Discord, Leviathan''s Hide, Gluttonous Grimoire, Stone of Binding, Midgardian
    Mail, Rod of Tahuti, Magi''s Cloak, Gladiator''s Shield, Hussar''s Wings, Ancile,
    Hide of the Nemean Lion, Void Shield, Doublet of Binding, Screeching Gargoyle,
    Prophetic Cloak.'
  slot_scores:
    Eye of Providence:
      total: 0.58
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.6
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.63
      pick: 0.2
      fit: 0.76
    Shifter's Shield:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.85
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
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Erosion, Shifter''s
    Shield, Eye of Providence, Chandra''s Grace, Oni Hunter''s Garb, Draconic Scale,
    Phoenix Feather, Spectral Armor, Rod of Asclepius, Gluttonous Grimoire, Soul Gem,
    Leviathan''s Hide, Midgardian Mail, Glorious Pridwen, Gladiator''s Shield, Rod
    of Tahuti, Ancile, Hide of the Nemean Lion, Void Shield, Doublet of Binding, Hussar''s
    Wings.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.94
    Shield of the Phoenix:
      total: 0.62
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 1.0
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.63
      pick: 0.2
      fit: 0.68
    Shifter's Shield:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.84
    Amanita Charm:
      total: 0.64
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Void Shield
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Screeching Gargoyle
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Stone of Binding, Screeching Gargoyle, Void Shield, Oni Hunter''s Garb,
    Void Stone, Shield of the Phoenix, Erosion, The Cosmic Horror, Shifter''s Shield,
    Eye of Providence, Spear of the Magus, Spear of Desolation, Spectral Armor, Draconic
    Scale, Leviathan''s Hide, Midgardian Mail, Nimble Ring, Obsidian Shard, Mantle
    Of Discord.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.68
    Stone of Binding:
      total: 0.56
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.78
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.63
    Void Shield:
      total: 0.55
      efficiency: 0.46
      win: 0.61
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.63
      pick: 0.2
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.63
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
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Gluttonous
    Grimoire, Oni Hunter''s Garb, Shield of the Phoenix, Spectral Armor, Erosion,
    Shifter''s Shield, Eye of Providence, Soul Gem, Draconic Scale, Leviathan''s Hide,
    Midgardian Mail, Mantle Of Discord, Stone of Binding, Screeching Gargoyle, Ancile,
    Magi''s Cloak, Yogi''s Necklace, Helm of Radiance, Hide of the Nemean Lion, Void
    Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.49
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.48
      efficiency: 0.42
      win: 0.61
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.63
      pick: 0.2
      fit: 0.35
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Freya's Tears
  flex_slots:
  - Screeching Gargoyle
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Shield of the Phoenix, Kinetic Cuirass,
    Amanita Charm, Rod of Tahuti, Soul Gem, Gluttonous Grimoire, Screeching Gargoyle,
    Oni Hunter''s Garb, Chronos'' Pendant, Chandra''s Grace, Gladiator''s Shield,
    Nimble Ring, Erosion, Shifter''s Shield, Eye of Providence, Spear of Desolation,
    Spectral Armor, Draconic Scale, Gem of Focus, Leviathan''s Hide, Helm of Radiance,
    Midgardian Mail, Mantle Of Discord, Prophetic Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.54
      pick: 0.35
      fit: 0.5
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.57
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.63
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.63
      pick: 0.2
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: The Crusher, Jotunn''s Revenge, Rod of Tahuti,
    Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Gluttonous Grimoire, Runeforged
    Hammer, Shield Splitter, Hydra''s Lament, Oni Hunter''s Garb, Eye of the Storm,
    Golden Blade, Nimble Ring, Shield of the Phoenix, Soul Gem, Pharaoh''s Curse,
    Erosion, Shifter''s Shield, Spectral Armor, Eye of Providence, The Reaper, Lernaean
    Bow, Draconic Scale, Avenging Blade, Damaru, Shogun''s Ofuda, Leviathan''s Hide,
    Death Metal, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Stone of Binding,
    The Cosmic Horror, Tyrfing, Riptalon, Spear of the Magus, Screeching Gargoyle.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.63
      pick: 0.2
      fit: 0.39
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Soul Gem, Berserker''s
    Shield, Nimble Ring, Oni Hunter''s Garb, The Cosmic Horror, Runeforged Hammer,
    Shield Splitter, Death Metal, Shield of the Phoenix, Spear of the Magus, Hydra''s
    Lament, Erosion, Shifter''s Shield, Eye of the Storm, Helm of Radiance, Spear
    of Desolation, Spectral Armor, Eye of Providence, Draconic Scale, Rod of Asclepius,
    Pharaoh''s Curse, The Reaper, Obsidian Shard, Leviathan''s Hide, Golden Blade,
    Jade Scepter, Chronos'' Pendant, Midgardian Mail, Avenging Blade, Mantle Of Discord,
    Damaru, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.63
      pick: 0.2
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.43
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Erosion, Shifter''s Shield,
    Eye of Providence, Shield of the Phoenix, Draconic Scale, Oni Hunter''s Garb,
    Spectral Armor, Mantle Of Discord, Leviathan''s Hide, Gluttonous Grimoire, Stone
    of Binding, Midgardian Mail, Rod of Tahuti, Magi''s Cloak, Gladiator''s Shield,
    Prophetic Cloak, Hussar''s Wings, Ancile, Hide of the Nemean Lion, Void Shield,
    Doublet of Binding, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.54
      pick: 0.35
      fit: 0.45
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.63
      pick: 0.2
      fit: 0.76
    Shifter's Shield:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.58
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.85
  starter: *id001
---
