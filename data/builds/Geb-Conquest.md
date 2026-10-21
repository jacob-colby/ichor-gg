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
    pick_rate: 0.44
    win_rate: 0.73
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.16
      win_rate: 0.5
    - name: Amanita Charm
      pick_rate: 0.12
      win_rate: 0.67
  - name: Stampede
    pick_rate: 0.28
    win_rate: 0.71
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.67
    - name: Circe's Hexstone
      pick_rate: 0.08
      win_rate: 1.0
  - name: Freya's Tears
    pick_rate: 0.24
    win_rate: 0.67
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.2
      win_rate: 0.8
    - name: Shell of Rebuke
      pick_rate: 0.16
      win_rate: 0.5
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Olmec Blue
    pick_rate: 0.11
    win_rate: 0.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 1.0
    - name: Medallion
      pick_rate: 0.05
      win_rate: 1.0
  - name: Veve Charm
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Engraved Guard
      pick_rate: 0.17
      win_rate: 0.0
    - name: Contagion
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.56
    win_rate: 0.79
  - name: Heroism
    pick_rate: 0.2
    win_rate: 0.4
  - name: Archmage's Gem
    pick_rate: 0.08
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-10-21'
  god_win_rate: 0.64
  god_matches_won: 16
  god_matches_played: 25
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Erosion, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Mantle
    Of Discord, Prophetic Cloak, Midgardian Mail, Hussar''s Wings, Hide of the Nemean
    Lion, Leviathan''s Hide, Screeching Gargoyle, Void Shield, Ancile, Oni Hunter''s
    Garb, Xibalban Effigy, Gladiator''s Shield, Void Stone, Spectral Armor, Doublet
    of Binding, Stygian Anchor.'
  slot_scores:
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.34
    Breastplate of Valor:
      total: 0.76
      efficiency: 0.65
      win: 1.0
      pick: 0.22
      fit: 0.45
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.67
      pick: 0.37
      fit: 0.76
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.69
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.66
      efficiency: 0.65
      win: 0.67
      pick: 0.12
      fit: 0.85
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Amanita Charm
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Chandra's Grace
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
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
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Shifter''s Shield,
    Erosion, Eye of Providence, Draconic Scale, Phoenix Feather, Glorious Pridwen,
    Yogi''s Necklace, Midgardian Mail, Stone of Binding, Hide of the Nemean Lion,
    Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Gladiator''s Shield,
    Magi''s Cloak, Hussar''s Wings, Void Stone, Spectral Armor, Mantle Of Discord,
    Screeching Gargoyle.'
  slot_scores:
    Chandra's Grace:
      total: 0.65
      efficiency: 0.45
      win: 0.8
      pick: 0.31
      fit: 0.78
    Contagion:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.42
    Breastplate of Valor:
      total: 0.75
      efficiency: 0.65
      win: 1.0
      pick: 0.22
      fit: 0.42
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.67
      pick: 0.37
      fit: 0.68
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.94
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.67
      pick: 0.12
      fit: 1.0
  community_ordered:
  - Chandra's Grace
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Kinetic Cuirass, Screeching Gargoyle,
    Void Shield, Shifter''s Shield, Void Stone, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Magi''s Cloak, Mantle Of Discord, Midgardian Mail,
    Hide of the Nemean Lion, Gluttonous Grimoire, Leviathan''s Hide, Ancile, Oni Hunter''s
    Garb, Prophetic Cloak, Spectral Armor, Xibalban Effigy, Doublet of Binding, Gladiator''s
    Shield, Hussar''s Wings.'
  slot_scores:
    Stone of Binding:
      total: 0.61
      efficiency: 0.51
      win: 0.69
      pick: 0.0
      fit: 0.78
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.25
    Breastplate of Valor:
      total: 0.73
      efficiency: 0.65
      win: 1.0
      pick: 0.22
      fit: 0.28
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.37
      fit: 0.47
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.12
      fit: 0.53
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Erosion, Eye of Providence,
    Nimble Ring, Stone of Binding, Shield of the Phoenix, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, Mantle Of Discord, Midgardian Mail,
    Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Void Stone, Spectral Armor, Xibalban Effigy, Prophetic Cloak, Doublet of
    Binding, Gladiator''s Shield.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.21
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.22
      fit: 0.21
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.35
      win: 0.69
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.55
      efficiency: 0.55
      win: 0.69
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.51
      efficiency: 0.37
      win: 0.69
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.12
      fit: 0.39
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Circe's Hexstone
  - Amanita Charm
  flex_slots:
  - Circe's Hexstone
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Shield of the Phoenix, Screeching Gargoyle, Shifter''s Shield, Chronos''
    Pendant, Prophetic Cloak, Erosion, Helm of Radiance, Gladiator''s Shield, Eye
    of Providence, Soul Gem, Draconic Scale, Stone of Binding, Gem of Focus, Spear
    of Desolation, Magi''s Cloak, Eye of Erebus, Rod of Asclepius, Glorious Pridwen,
    Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Hide of the Nemean Lion.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.23
    Breastplate of Valor:
      total: 0.76
      efficiency: 0.65
      win: 1.0
      pick: 0.22
      fit: 0.5
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.67
      pick: 0.37
      fit: 0.67
    Circe's Hexstone:
      total: 0.61
      efficiency: 0.23
      win: 1.0
      pick: 0.11
      fit: 0.47
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.12
      fit: 0.47
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Circe's Hexstone
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita
    Charm, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged Hammer, Shifter''s
    Shield, Eye of the Storm, Tyrfing, Heartseeker, Hydra''s Lament, Erosion, Lernaean
    Bow, Tekko-Kagi, Eye of Providence, Avenging Blade, Silverbranch Bow, Draconic
    Scale, Stone of Binding, Shield of the Phoenix, Titan''s Bane, The Crusher, Toxic
    Blade, Pharaoh''s Curse, Magi''s Cloak, The Reaper, Shogun''s Ofuda, Mantle Of
    Discord, Screeching Gargoyle, Midgardian Mail, Daybreak Gavel, Hide of the Nemean
    Lion, Arondight, Leviathan''s Hide, Void Shield, Dominance, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.69
      pick: 0.0
      fit: 0.37
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.23
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.22
      fit: 0.23
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.37
      fit: 0.39
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.12
      fit: 0.44
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Contagion
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Spear of
    Desolation, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem,
    Shifter''s Shield, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Rod
    of Asclepius, Hydra''s Lament, Heartseeker, Erosion, Eye of Providence, Stone
    of Binding, Draconic Scale, Shield of the Phoenix, Doom Orb, Jade Scepter, Death
    Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, The World Stone, Helm
    of Darkness, Chronos'' Pendant, Titan''s Bane, The Crusher, Ancient Signet, Screeching
    Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.22
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.22
      fit: 0.22
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.37
      fit: 0.37
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.12
      fit: 0.42
  community_ordered:
  - Contagion
  - Breastplate of Valor
  - Freya's Tears
  - Amanita Charm
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
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Magi''s
    Cloak, Mantle Of Discord, Prophetic Cloak, Midgardian Mail, Hussar''s Wings, Hide
    of the Nemean Lion, Leviathan''s Hide, Screeching Gargoyle, Void Shield, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Gladiator''s Shield, Void Stone, Spectral
    Armor, Doublet of Binding, Stygian Anchor.'
  slot_scores:
    Eye of Providence:
      total: 0.62
      efficiency: 0.61
      win: 0.69
      pick: 0.0
      fit: 0.6
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.67
      pick: 0.37
      fit: 0.76
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.69
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.66
      efficiency: 0.65
      win: 0.67
      pick: 0.12
      fit: 0.85
    Erosion:
      total: 0.62
      efficiency: 0.51
      win: 0.69
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Freya's Tears
  - Amanita Charm
  starter: *id001
---
