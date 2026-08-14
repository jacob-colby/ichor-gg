---
type: smite-build
god: Geb
mode: Conquest
builds:
- source: community
  aspect: Aspect of Calamity
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.0
  slot_order:
  - name: Stampede
    pick_rate: 0.26
    win_rate: 0.45
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.25
      win_rate: 0.57
    - name: Yogi's Necklace
      pick_rate: 0.09
      win_rate: 0.88
  - name: Genji's Guard
    pick_rate: 0.29
    win_rate: 0.64
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.15
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.62
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.46
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.83
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.7
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.67
  - name: Dwarven Plate
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.5
  - name: Shield
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.67
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Selflessness
    pick_rate: 0.44
    win_rate: 0.57
  - name: Heroism
    pick_rate: 0.28
    win_rate: 0.67
  - name: Bluestone Pendant
    pick_rate: 0.07
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-08-14'
  god_win_rate: 0.5647058823529412
  god_matches_won: 48
  god_matches_played: 85
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Kinetic Cuirass, Amanita Charm, Shifter''s Shield, Erosion, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Oni Hunter''s Garb, Spectral Armor, Gluttonous
    Grimoire, Mantle Of Discord, Stone of Binding, Leviathan''s Hide, Midgardian Mail,
    Magi''s Cloak, Gladiator''s Shield, Prophetic Cloak, Hussar''s Wings, Xibalban
    Effigy, Ancile, Void Shield, Hide of the Nemean Lion, Doublet of Binding, Screeching
    Gargoyle.'
  slot_scores:
    Yogi's Necklace:
      total: 0.64
      efficiency: 0.59
      win: 0.88
      pick: 0.09
      fit: 0.24
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.64
      pick: 0.4
      fit: 0.45
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.67
      pick: 0.18
      fit: 0.76
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.85
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
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
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Shifter''s Shield,
    Erosion, Oni Hunter''s Garb, Eye of Providence, Chandra''s Grace, Draconic Scale,
    Gluttonous Grimoire, Phoenix Feather, Rod of Asclepius, Spectral Armor, Soul Gem,
    Leviathan''s Hide, Midgardian Mail, Glorious Pridwen, Gladiator''s Shield, Ancile,
    Void Shield, Hide of the Nemean Lion, Mantle Of Discord, Doublet of Binding, Stone
    of Binding.'
  slot_scores:
    Yogi's Necklace:
      total: 0.66
      efficiency: 0.59
      win: 0.88
      pick: 0.09
      fit: 0.32
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.64
      pick: 0.4
      fit: 0.42
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.94
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 1.0
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.67
      pick: 0.18
      fit: 0.68
    Amanita Charm:
      total: 0.63
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Yogi's Necklace
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Kinetic Cuirass
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Soul Gem, Stone
    of Binding, Screeching Gargoyle, Void Shield, Oni Hunter''s Garb, Spear of the
    Magus, Shield of the Phoenix, Void Stone, Shifter''s Shield, The Cosmic Horror,
    Erosion, Eye of Providence, Spectral Armor, Spear of Desolation, Draconic Scale,
    Obsidian Shard, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Magi''s
    Cloak, Helm of Radiance.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.78
    Yogi's Necklace:
      total: 0.63
      efficiency: 0.59
      win: 0.88
      pick: 0.09
      fit: 0.15
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.64
      pick: 0.4
      fit: 0.28
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.18
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Yogi''s Necklace, Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Oni Hunter''s Garb, Shield of the Phoenix, Soul Gem, Spectral Armor, Shifter''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Leviathan''s Hide, Bracer
    of The Abyss, Midgardian Mail, Mantle Of Discord, Stone of Binding, Helm of Radiance,
    Death Metal, Screeching Gargoyle, Magi''s Cloak, Bragi''s Harp, Ancile, Rod of
    Asclepius.'
  slot_scores:
    Yogi's Necklace:
      total: 0.62
      efficiency: 0.59
      win: 0.88
      pick: 0.09
      fit: 0.11
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.64
      pick: 0.4
      fit: 0.21
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.18
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Amanita Charm, Soul Gem, Gluttonous Grimoire, Oni Hunter''s Garb, Screeching Gargoyle,
    Chronos'' Pendant, Gladiator''s Shield, Chandra''s Grace, Shifter''s Shield, Erosion,
    Prophetic Cloak, Spectral Armor, Eye of Providence, Spear of Desolation, Draconic
    Scale, Helm of Radiance, Gem of Focus, Leviathan''s Hide, Mantle Of Discord, Midgardian
    Mail, Stone of Binding, Rod of Asclepius.'
  slot_scores:
    Yogi's Necklace:
      total: 0.63
      efficiency: 0.59
      win: 0.88
      pick: 0.09
      fit: 0.13
    Genji's Guard:
      total: 0.63
      efficiency: 0.71
      win: 0.64
      pick: 0.4
      fit: 0.5
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.2
      fit: 0.5
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.57
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.67
      pick: 0.18
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Yogi''s Necklace, Jotunn''s Revenge, Berserker''s
    Shield, The Crusher, Kinetic Cuirass, Gluttonous Grimoire, Amanita Charm, Hydra''s
    Lament, Shield Splitter, Oni Hunter''s Garb, Runeforged Hammer, Golden Blade,
    Pharaoh''s Curse, Soul Gem, Eye of the Storm, Lernaean Bow, Shield of the Phoenix,
    Shifter''s Shield, Erosion, Spectral Armor, Eye of Providence, Shogun''s Ofuda,
    Draconic Scale, The Reaper, Damaru, Death Metal, Avenging Blade, Spear of the
    Magus, Riptalon, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Stone
    of Binding, Heartseeker, Tekko-Kagi, The Cosmic Horror, Silverbranch Bow.'
  slot_scores:
    Yogi's Necklace:
      total: 0.63
      efficiency: 0.59
      win: 0.88
      pick: 0.09
      fit: 0.12
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.64
      pick: 0.4
      fit: 0.23
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.18
      fit: 0.39
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    Kinetic Cuirass, The Crusher, Amanita Charm, Soul Gem, Berserker''s Shield, Spear
    of the Magus, Oni Hunter''s Garb, Death Metal, Hydra''s Lament, The Cosmic Horror,
    Runeforged Hammer, Shield Splitter, Helm of Radiance, Shield of the Phoenix, Shifter''s
    Shield, Erosion, Spear of Desolation, Spectral Armor, Eye of the Storm, Rod of
    Asclepius, Eye of Providence, Pharaoh''s Curse, Obsidian Shard, Jade Scepter,
    Draconic Scale, Golden Blade, Chronos'' Pendant, Leviathan''s Hide, Blood-Bound
    Book, Lernaean Bow, The Reaper, Damaru, Bancroft''s Talon, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Yogi's Necklace:
      total: 0.63
      efficiency: 0.59
      win: 0.88
      pick: 0.09
      fit: 0.12
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.64
      pick: 0.4
      fit: 0.22
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.18
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.55
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
  - Shifter's Shield
  - Erosion
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Shifter''s Shield, Erosion,
    Eye of Providence, Shield of the Phoenix, Draconic Scale, Oni Hunter''s Garb,
    Spectral Armor, Gluttonous Grimoire, Mantle Of Discord, Stone of Binding, Leviathan''s
    Hide, Midgardian Mail, Magi''s Cloak, Gladiator''s Shield, Prophetic Cloak, Hussar''s
    Wings, Xibalban Effigy, Ancile, Void Shield, Hide of the Nemean Lion, Doublet
    of Binding, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.64
      pick: 0.4
      fit: 0.45
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.67
      pick: 0.18
      fit: 0.76
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.57
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.85
  starter: *id001
---
