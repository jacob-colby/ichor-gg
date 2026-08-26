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
    pick_rate: 0.32
    win_rate: 0.57
    alternates:
    - name: Stampede
      pick_rate: 0.32
      win_rate: 0.71
    - name: Yogi's Necklace
      pick_rate: 0.23
      win_rate: 0.4
  - name: Genji's Guard
    pick_rate: 0.36
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.5
  - name: Breastplate of Valor
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.75
    - name: Spirit Robe
      pick_rate: 0.11
      win_rate: 0.0
  - name: Freya's Tears
    pick_rate: 0.33
    win_rate: 0.83
    alternates:
    - name: Captain's Ring
      pick_rate: 0.11
      win_rate: 0.0
    - name: Draconic Scale
      pick_rate: 0.11
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Veve Charm
      pick_rate: 0.13
      win_rate: 1.0
    - name: Captain's Ring
      pick_rate: 0.06
      win_rate: 0.0
  - name: Mote of Chaos
    pick_rate: 0.29
    win_rate: 0.5
    alternates:
    - name: Medallion
      pick_rate: 0.14
      win_rate: 0.0
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.36
    win_rate: 0.63
  - name: Heroism
    pick_rate: 0.27
    win_rate: 0.5
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-08-26'
  god_win_rate: 0.5
  god_matches_won: 11
  god_matches_played: 22
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Erosion, Eye of Providence,
    Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Mantle Of Discord, Prophetic
    Cloak, Midgardian Mail, Hussar''s Wings, Hide of the Nemean Lion, Leviathan''s
    Hide, Screeching Gargoyle, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy,
    Gladiator''s Shield, Void Stone, Spectral Armor, Doublet of Binding, Stygian Anchor.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.25
      fit: 0.45
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.95
    Shell of Rebuke:
      total: 0.65
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.61
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 0.83
      pick: 0.55
      fit: 0.76
    Draconic Scale:
      total: 0.76
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.85
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.85
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Shell of Rebuke
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Stampede
  flex_slots:
  - Breastplate of Valor
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Shifter''s Shield,
    Erosion, Eye of Providence, Phoenix Feather, Glorious Pridwen, Chandra''s Grace,
    Midgardian Mail, Stone of Binding, Hide of the Nemean Lion, Leviathan''s Hide,
    Void Shield, Ancile, Oni Hunter''s Garb, Gladiator''s Shield, Magi''s Cloak, Hussar''s
    Wings, Void Stone, Spectral Armor, Mantle Of Discord, Screeching Gargoyle.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.25
      fit: 0.42
    Shell of Rebuke:
      total: 0.64
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.52
    Freya's Tears:
      total: 0.72
      efficiency: 0.61
      win: 0.83
      pick: 0.55
      fit: 0.68
    Draconic Scale:
      total: 0.76
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.84
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 1.0
    Stampede:
      total: 0.6
      efficiency: 0.51
      win: 0.71
      pick: 0.32
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Shell of Rebuke
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Stampede
  flex_slots:
  - Stampede
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Kinetic Cuirass, Screeching Gargoyle,
    Void Shield, Shifter''s Shield, Void Stone, Erosion, Eye of Providence, Shield
    of the Phoenix, Magi''s Cloak, Mantle Of Discord, Midgardian Mail, Hide of the
    Nemean Lion, Gluttonous Grimoire, Leviathan''s Hide, Ancile, Oni Hunter''s Garb,
    Prophetic Cloak, Spectral Armor, Xibalban Effigy, Doublet of Binding, Gladiator''s
    Shield, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.25
      fit: 0.28
    Shell of Rebuke:
      total: 0.62
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.38
    Freya's Tears:
      total: 0.69
      efficiency: 0.61
      win: 0.83
      pick: 0.55
      fit: 0.47
    Draconic Scale:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.53
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.53
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.71
      pick: 0.32
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Shell of Rebuke
  - Bragi's Harp
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
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
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Erosion, Eye of Providence,
    Nimble Ring, Stone of Binding, Shield of the Phoenix, Magi''s Cloak, Screeching
    Gargoyle, Daybreak Gavel, Mantle Of Discord, Midgardian Mail, Hide of the Nemean
    Lion, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Void Stone,
    Spectral Armor, Xibalban Effigy, Prophetic Cloak, Doublet of Binding, Gladiator''s
    Shield.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.41
      efficiency: 0.35
      win: 0.57
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.49
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.28
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.28
    Bragi's Harp:
      total: 0.45
      efficiency: 0.37
      win: 0.57
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.83
      pick: 0.55
      fit: 0.35
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Shell of Rebuke
  - Freya's Tears
  - Draconic Scale
  - Stampede
  flex_slots:
  - Stampede
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Shield of the Phoenix, Screeching Gargoyle, Shifter''s Shield, Chronos''
    Pendant, Prophetic Cloak, Erosion, Helm of Radiance, Gladiator''s Shield, Eye
    of Providence, Soul Gem, Stone of Binding, Gem of Focus, Spear of Desolation,
    Magi''s Cloak, Eye of Erebus, Rod of Asclepius, Glorious Pridwen, Mantle Of Discord,
    Midgardian Mail, Chandra''s Grace, Daybreak Gavel, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.49
      fit: 0.5
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.25
      fit: 0.5
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.33
    Freya's Tears:
      total: 0.72
      efficiency: 0.61
      win: 0.83
      pick: 0.55
      fit: 0.67
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.47
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.32
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Draconic Scale
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm, Berserker''s
    Shield, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged Hammer, Shifter''s
    Shield, Eye of the Storm, Tyrfing, Heartseeker, Hydra''s Lament, Erosion, Lernaean
    Bow, Tekko-Kagi, Eye of Providence, Avenging Blade, Silverbranch Bow, Stone of
    Binding, Shield of the Phoenix, Titan''s Bane, The Crusher, Toxic Blade, Pharaoh''s
    Curse, Magi''s Cloak, The Reaper, Shogun''s Ofuda, Mantle Of Discord, Screeching
    Gargoyle, Midgardian Mail, Daybreak Gavel, Hide of the Nemean Lion, Arondight,
    Leviathan''s Hide, Void Shield, Dominance, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.25
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.47
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.31
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.83
      pick: 0.55
      fit: 0.39
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.44
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.32
      fit: 0.28
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Draconic Scale
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Spear of
    Desolation, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem,
    Shifter''s Shield, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Rod
    of Asclepius, Hydra''s Lament, Heartseeker, Erosion, Eye of Providence, Stone
    of Binding, Shield of the Phoenix, Doom Orb, Jade Scepter, Death Metal, Wish-Granting
    Pearl, Avenging Blade, Magi''s Cloak, The World Stone, Helm of Darkness, Chronos''
    Pendant, Titan''s Bane, The Crusher, Ancient Signet, Screeching Gargoyle, Mantle
    Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.25
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.4
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.3
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.83
      pick: 0.55
      fit: 0.37
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.42
    Stampede:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.32
      fit: 0.27
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
    Eye of Providence, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Mantle
    Of Discord, Prophetic Cloak, Midgardian Mail, Hussar''s Wings, Hide of the Nemean
    Lion, Leviathan''s Hide, Screeching Gargoyle, Void Shield, Ancile, Oni Hunter''s
    Garb, Xibalban Effigy, Gladiator''s Shield, Void Stone, Spectral Armor, Doublet
    of Binding, Stygian Anchor.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.6
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 0.83
      pick: 0.55
      fit: 0.76
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.85
  starter: *id001
---
