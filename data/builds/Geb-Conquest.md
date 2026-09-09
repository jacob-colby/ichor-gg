---
type: smite-build
god: Geb
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.2
    win_rate: 1.0
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.2
      win_rate: 1.0
    - name: Chandra's Grace
      pick_rate: 0.13
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.27
    win_rate: 0.5
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.2
      win_rate: 1.0
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.2
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.33
    win_rate: 0.75
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 1.0
    - name: Shroud of Vengeance
      pick_rate: 0.08
      win_rate: 0.0
  - name: Circe's Hexstone
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Captain's Ring
      pick_rate: 0.13
      win_rate: 0.0
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 1.0
  - name: Stygian Anchor
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Mana Tome
      pick_rate: 0.25
      win_rate: 0.0
    - name: Medallion
      pick_rate: 0.25
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.4
    win_rate: 0.5
  - name: Heroism
    pick_rate: 0.2
    win_rate: 1.0
  - name: Archmage's Gem
    pick_rate: 0.07
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-09-09'
  god_win_rate: 0.6666666666666666
  god_matches_won: 10
  god_matches_played: 15
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shifter's Shield
  - Stygian Anchor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Erosion, Eye of Providence,
    Draconic Scale, Breastplate of Valor, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Mantle Of Discord, Midgardian Mail, Hussar''s Wings, Hide of the
    Nemean Lion, Leviathan''s Hide, Screeching Gargoyle, Void Shield, Stampede, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Gladiator''s Shield, Void Stone, Spectral
    Armor, Doublet of Binding.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.95
    Prophetic Cloak:
      total: 0.73
      efficiency: 0.44
      win: 1.0
      pick: 0.2
      fit: 0.76
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 0.88
      pick: 0.0
      fit: 0.85
    Stygian Anchor:
      total: 0.74
      efficiency: 0.45
      win: 1.0
      pick: 0.77
      fit: 0.61
    Amanita Charm:
      total: 0.75
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.7
      efficiency: 0.51
      win: 0.88
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Prophetic Cloak
  - Stygian Anchor
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Chandra's Grace
  - Kinetic Cuirass
  - Prophetic Cloak
  - Stygian Anchor
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Shifter's Shield
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Shifter''s Shield,
    Erosion, Eye of Providence, Draconic Scale, Breastplate of Valor, Phoenix Feather,
    Glorious Pridwen, Yogi''s Necklace, Midgardian Mail, Stone of Binding, Hide of
    the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Ancile, Oni Hunter''s
    Garb, Gladiator''s Shield, Magi''s Cloak, Hussar''s Wings, Void Stone, Spectral
    Armor, Mantle Of Discord, Screeching Gargoyle.'
  slot_scores:
    Chandra's Grace:
      total: 0.74
      efficiency: 0.45
      win: 1.0
      pick: 0.27
      fit: 0.78
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.94
    Prophetic Cloak:
      total: 0.72
      efficiency: 0.44
      win: 1.0
      pick: 0.2
      fit: 0.68
    Stygian Anchor:
      total: 0.72
      efficiency: 0.45
      win: 1.0
      pick: 0.77
      fit: 0.52
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 0.88
      pick: 0.0
      fit: 0.84
    Amanita Charm:
      total: 0.77
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Chandra's Grace
  - Prophetic Cloak
  - Stygian Anchor
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Prophetic Cloak
  - Stygian Anchor
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Kinetic Cuirass, Screeching Gargoyle,
    Void Shield, Shifter''s Shield, Breastplate of Valor, Void Stone, Erosion, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak, Mantle Of
    Discord, Midgardian Mail, Hide of the Nemean Lion, Gluttonous Grimoire, Leviathan''s
    Hide, Stampede, Ancile, Oni Hunter''s Garb, Spectral Armor, Xibalban Effigy, Doublet
    of Binding, Gladiator''s Shield, Hussar''s Wings.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.67
      efficiency: 0.51
      win: 0.88
      pick: 0.0
      fit: 0.68
    Stone of Binding:
      total: 0.69
      efficiency: 0.51
      win: 0.88
      pick: 0.0
      fit: 0.78
    Kinetic Cuirass:
      total: 0.69
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.63
    Prophetic Cloak:
      total: 0.69
      efficiency: 0.44
      win: 1.0
      pick: 0.2
      fit: 0.47
    Stygian Anchor:
      total: 0.7
      efficiency: 0.45
      win: 1.0
      pick: 0.77
      fit: 0.38
    Amanita Charm:
      total: 0.7
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.53
  community_ordered:
  - Prophetic Cloak
  - Stygian Anchor
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Prophetic Cloak
  - Bracer of The Abyss
  - Nimble Ring
  - Stygian Anchor
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Breastplate of Valor, Shifter''s Shield,
    Erosion, Eye of Providence, Nimble Ring, Stone of Binding, Shield of the Phoenix,
    Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Mantle Of
    Discord, Midgardian Mail, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield,
    Stampede, Ancile, Oni Hunter''s Garb, Void Stone, Spectral Armor, Xibalban Effigy,
    Doublet of Binding, Gladiator''s Shield.'
  slot_scores:
    Prophetic Cloak:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.2
      fit: 0.35
    Bracer of The Abyss:
      total: 0.55
      efficiency: 0.35
      win: 0.88
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.63
      efficiency: 0.55
      win: 0.88
      pick: 0.0
      fit: 0.28
    Stygian Anchor:
      total: 0.69
      efficiency: 0.45
      win: 1.0
      pick: 0.77
      fit: 0.28
    Bragi's Harp:
      total: 0.59
      efficiency: 0.37
      win: 0.88
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Prophetic Cloak
  - Stygian Anchor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chandra's Grace
  - Breastplate of Valor
  - Freya's Tears
  - Kinetic Cuirass
  - Prophetic Cloak
  - Stygian Anchor
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Rod of Tahuti, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Shifter''s
    Shield, Chronos'' Pendant, Erosion, Helm of Radiance, Gladiator''s Shield, Eye
    of Providence, Soul Gem, Draconic Scale, Stone of Binding, Gem of Focus, Spear
    of Desolation, Magi''s Cloak, Eye of Erebus, Rod of Asclepius, Glorious Pridwen,
    Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Hide of the Nemean Lion.'
  slot_scores:
    Chandra's Grace:
      total: 0.69
      efficiency: 0.45
      win: 1.0
      pick: 0.27
      fit: 0.47
    Breastplate of Valor:
      total: 0.7
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.75
      pick: 0.55
      fit: 0.67
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.57
    Prophetic Cloak:
      total: 0.71
      efficiency: 0.44
      win: 1.0
      pick: 0.2
      fit: 0.67
    Stygian Anchor:
      total: 0.7
      efficiency: 0.45
      win: 1.0
      pick: 0.77
      fit: 0.33
  community_ordered:
  - Chandra's Grace
  - Freya's Tears
  - Prophetic Cloak
  - Stygian Anchor
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Prophetic Cloak
  - Stygian Anchor
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm, Berserker''s
    Shield, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged Hammer, Breastplate
    of Valor, Shifter''s Shield, Eye of the Storm, Tyrfing, Heartseeker, Hydra''s
    Lament, Erosion, Lernaean Bow, Tekko-Kagi, Eye of Providence, Avenging Blade,
    Silverbranch Bow, Draconic Scale, Stone of Binding, Shield of the Phoenix, Titan''s
    Bane, The Crusher, Toxic Blade, Pharaoh''s Curse, Magi''s Cloak, The Reaper, Shogun''s
    Ofuda, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Daybreak Gavel,
    Hide of the Nemean Lion, Arondight, Leviathan''s Hide, Void Shield, Stampede,
    Dominance, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.69
      efficiency: 0.68
      win: 0.88
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.72
      win: 0.88
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.54
    Prophetic Cloak:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.2
      fit: 0.39
    Stygian Anchor:
      total: 0.69
      efficiency: 0.45
      win: 1.0
      pick: 0.77
      fit: 0.31
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Prophetic Cloak
  - Stygian Anchor
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Prophetic Cloak
  - Stygian Anchor
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Breastplate
    of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer, Helm of
    Radiance, Soul Gem, Shifter''s Shield, Obsidian Shard, Berserker''s Shield, Eye
    of the Storm, Rod of Asclepius, Hydra''s Lament, Heartseeker, Erosion, Eye of
    Providence, Stone of Binding, Draconic Scale, Shield of the Phoenix, Doom Orb,
    Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak,
    The World Stone, Helm of Darkness, Chronos'' Pendant, Titan''s Bane, The Crusher,
    Ancient Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian
    Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.72
      win: 0.88
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.52
    Prophetic Cloak:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.2
      fit: 0.37
    Stygian Anchor:
      total: 0.69
      efficiency: 0.45
      win: 1.0
      pick: 0.77
      fit: 0.3
    Shield Splitter:
      total: 0.66
      efficiency: 0.55
      win: 0.88
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Prophetic Cloak
  - Stygian Anchor
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Erosion,
    Eye of Providence, Draconic Scale, Breastplate of Valor, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Mantle Of Discord, Midgardian Mail, Hussar''s
    Wings, Hide of the Nemean Lion, Leviathan''s Hide, Screeching Gargoyle, Void Shield,
    Stampede, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Gladiator''s Shield, Void
    Stone, Spectral Armor, Doublet of Binding.'
  slot_scores:
    Eye of Providence:
      total: 0.7
      efficiency: 0.61
      win: 0.88
      pick: 0.0
      fit: 0.6
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 0.88
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.69
      efficiency: 0.61
      win: 0.75
      pick: 0.55
      fit: 0.76
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 0.88
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.75
      efficiency: 0.65
      win: 0.88
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.7
      efficiency: 0.51
      win: 0.88
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Freya's Tears
  starter: *id001
---
