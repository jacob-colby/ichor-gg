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
  - name: Runeforged Hammer
    pick_rate: 0.16
    win_rate: 0.88
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.38
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.63
    - name: Shogun's Ofuda
      pick_rate: 0.12
      win_rate: 0.67
  - name: Stampede
    pick_rate: 0.12
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.86
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.08
    win_rate: 0.75
    alternates:
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.67
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.5
  - name: Medallion
    pick_rate: 0.12
    win_rate: 0.67
    alternates:
    - name: Contagion
      pick_rate: 0.08
      win_rate: 1.0
    - name: Spectral Armor
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.16
    win_rate: 0.88
  - name: Selflessness
    pick_rate: 0.14
    win_rate: 0.29
  - name: Sundering Axe
    pick_rate: 0.12
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-08-13'
  god_win_rate: 0.5490196078431373
  god_matches_won: 28
  god_matches_played: 51
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Kinetic Cuirass
  - Freya's Tears
  - Dwarven Plate
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
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
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous Grimoire,
    Breastplate of Valor, Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Draconic
    Scale, Eye of Providence, Mantle Of Discord, Leviathan''s Hide, Stone of Binding,
    Midgardian Mail, Helm of Radiance, Soul Gem, Magi''s Cloak, Ancile, Gladiator''s
    Shield, Xibalban Effigy, Prophetic Cloak, Hide of the Nemean Lion, Void Shield,
    Screeching Gargoyle.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.31
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.59
      win: 0.75
      pick: 0.13
      fit: 0.82
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.0
      fit: 0.64
    Dwarven Plate:
      total: 0.66
      efficiency: 0.35
      win: 1.0
      pick: 0.15
      fit: 0.51
    Spectral Armor:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.25
      fit: 0.46
    Amanita Charm:
      total: 0.63
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.72
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Contagion
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Dwarven Plate
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Dwarven Plate
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire,
    Soul Gem, Rod of Asclepius, Oni Hunter''s Garb, Freya''s Tears, Chandra''s Grace,
    Erosion, Draconic Scale, Breastplate of Valor, Eye of Providence, Phoenix Feather,
    Leviathan''s Hide, Blood-Bound Book, Lifebinder, Midgardian Mail, Bancroft''s
    Talon, Glorious Pridwen, Gladiator''s Shield, Ancile, Hide of the Nemean Lion,
    Void Shield.'
  slot_scores:
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.37
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.59
      win: 0.75
      pick: 0.13
      fit: 0.8
    Shield of the Phoenix:
      total: 0.64
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.92
    Dwarven Plate:
      total: 0.65
      efficiency: 0.35
      win: 1.0
      pick: 0.15
      fit: 0.43
    Spectral Armor:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.25
      fit: 0.49
    Amanita Charm:
      total: 0.67
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Stone of Binding
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Dwarven Plate
  - Spectral Armor
  flex_slots:
  - Gluttonous Grimoire
  - Stone of Binding
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Kinetic Cuirass, Gluttonous Grimoire, Soul Gem, Amanita Charm, Stone
    of Binding, Spear of the Magus, Screeching Gargoyle, Breastplate of Valor, Freya''s
    Tears, Void Shield, Oni Hunter''s Garb, The Cosmic Horror, Void Stone, Shield
    of the Phoenix, Spear of Desolation, Erosion, Draconic Scale, Obsidian Shard,
    Eye of Providence, Leviathan''s Hide, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, The World Stone.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.24
    Stone of Binding:
      total: 0.58
      efficiency: 0.48
      win: 0.67
      pick: 0.0
      fit: 0.74
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.59
      win: 0.75
      pick: 0.13
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.63
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.63
    Dwarven Plate:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.15
      fit: 0.34
    Spectral Armor:
      total: 0.71
      efficiency: 0.58
      win: 1.0
      pick: 0.25
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spectral Armor
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Dwarven Plate — magical protection
    swap_item: Dwarven Plate
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Gluttonous Grimoire, Amanita Charm, Breastplate of
    Valor, Freya''s Tears, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Erosion,
    Draconic Scale, Eye of Providence, Bracer of The Abyss, Helm of Radiance, Leviathan''s
    Hide, Death Metal, Midgardian Mail, Mantle Of Discord, Stone of Binding, Yogi''s
    Necklace, Bragi''s Harp, Rod of Asclepius, Blood-Bound Book, Bancroft''s Talon,
    Nimble Ring.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.21
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.75
      pick: 0.13
      fit: 0.48
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.52
      efficiency: 0.49
      win: 0.67
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.45
    Spectral Armor:
      total: 0.7
      efficiency: 0.58
      win: 1.0
      pick: 0.25
      fit: 0.24
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Spectral Armor
  flex_slots:
  - Freya's Tears
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Dwarven Plate — magical protection
    swap_item: Dwarven Plate
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Breastplate of Valor,
    Freya''s Tears, Shield of the Phoenix, Amanita Charm, Soul Gem, Gluttonous Grimoire,
    Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Chandra''s Grace,
    Gladiator''s Shield, Erosion, Draconic Scale, Spear of Desolation, Prophetic Cloak,
    Eye of Providence, Helm of Radiance, Gem of Focus, Totem of Death, Leviathan''s
    Hide, Mantle Of Discord, Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.23
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.59
      win: 0.75
      pick: 0.13
      fit: 0.55
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.0
      fit: 0.64
    Spectral Armor:
      total: 0.71
      efficiency: 0.58
      win: 1.0
      pick: 0.25
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Contagion
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Dwarven Plate
  - Spectral Armor
  flex_slots:
  - Dwarven Plate
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    win/pick). Underrated for this god: Kinetic Cuirass, Jotunn''s Revenge, Gluttonous
    Grimoire, Berserker''s Shield, The Crusher, Amanita Charm, Breastplate of Valor,
    Soul Gem, Hydra''s Lament, Freya''s Tears, Oni Hunter''s Garb, Shield Splitter,
    Pharaoh''s Curse, Golden Blade, Lernaean Bow, Shield of the Phoenix, Eye of the
    Storm, Erosion, Death Metal, Draconic Scale, Spear of the Magus, Eye of Providence,
    Damaru, The Reaper, The Cosmic Horror, Avenging Blade, Helm of Radiance, Riptalon,
    Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Stone of Binding, Heartseeker,
    Silverbranch Bow, Yogi''s Necklace, Tekko-Kagi.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.59
      win: 0.75
      pick: 0.13
      fit: 0.52
    Runeforged Hammer:
      total: 0.66
      efficiency: 0.55
      win: 0.88
      pick: 0.16
      fit: 0.44
    Dwarven Plate:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.15
      fit: 0.3
    Spectral Armor:
      total: 0.71
      efficiency: 0.58
      win: 1.0
      pick: 0.25
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Contagion
  - Kinetic Cuirass
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Dwarven Plate
  - Spectral Armor
  flex_slots:
  - Dwarven Plate
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Gluttonous Grimoire,
    Jotunn''s Revenge, The Crusher, Berserker''s Shield, Amanita Charm, Soul Gem,
    Breastplate of Valor, Freya''s Tears, Spear of the Magus, Oni Hunter''s Garb,
    Hydra''s Lament, Death Metal, The Cosmic Horror, Helm of Radiance, Shield Splitter,
    Shield of the Phoenix, Pharaoh''s Curse, Erosion, Spear of Desolation, Rod of
    Asclepius, Eye of the Storm, Draconic Scale, Eye of Providence, Jade Scepter,
    Obsidian Shard, Golden Blade, Lernaean Bow, Chronos'' Pendant, Leviathan''s Hide,
    Blood-Bound Book, Damaru, Bancroft''s Talon, Bracer of The Abyss, The Reaper,
    Midgardian Mail.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.22
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.59
      win: 0.75
      pick: 0.13
      fit: 0.5
    Runeforged Hammer:
      total: 0.65
      efficiency: 0.55
      win: 0.88
      pick: 0.16
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.53
    Dwarven Plate:
      total: 0.62
      efficiency: 0.35
      win: 1.0
      pick: 0.15
      fit: 0.29
    Spectral Armor:
      total: 0.7
      efficiency: 0.58
      win: 1.0
      pick: 0.25
      fit: 0.26
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
  - Shifter's Shield
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Breastplate of Valor, Erosion, Oni Hunter''s Garb, Shield of the Phoenix,
    Eye of Providence, Draconic Scale, Mantle Of Discord, Leviathan''s Hide, Stone
    of Binding, Midgardian Mail, Helm of Radiance, Soul Gem, Magi''s Cloak, Ancile,
    Gladiator''s Shield, Xibalban Effigy, Prophetic Cloak, Hide of the Nemean Lion,
    Void Shield, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.38
      pick: 0.22
      fit: 0.39
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.59
      win: 0.75
      pick: 0.13
      fit: 0.82
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.58
      efficiency: 0.52
      win: 0.63
      pick: 0.22
      fit: 0.72
    Amanita Charm:
      total: 0.63
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.72
  starter: *id001
---
