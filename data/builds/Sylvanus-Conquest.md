---
type: smite-build
god: Sylvanus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Grover's Wrath
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.57
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.2
    win_rate: 0.52
    alternates:
    - name: Tyrfing
      pick_rate: 0.1
      win_rate: 0.61
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.55
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.43
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.36
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.53
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.23
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.46
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.68
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.73
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.5
  - name: Veve Charm
    pick_rate: 0.06
    win_rate: 0.57
    alternates:
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.33
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.4
  community_starters:
  - name: Selflessness
    pick_rate: 0.31
    win_rate: 0.52
  - name: Heroism
    pick_rate: 0.13
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.11
    win_rate: 0.35
  source_url: https://smitebrain.com/gods/sylvanus/
  last_verified: '2026-08-15'
  god_win_rate: 0.5174825174825175
  god_matches_won: 148
  god_matches_played: 286
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Rod of Tahuti
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
    this god: Freya''s Tears, Draconic Scale, Kinetic Cuirass, Amanita Charm, Rod
    of Tahuti, Gluttonous Grimoire, Shield of the Phoenix, Erosion, Shifter''s Shield,
    Oni Hunter''s Garb, Eye of Providence, Soul Gem, Spectral Armor, Nimble Ring,
    Leviathan''s Hide, Helm of Radiance, Midgardian Mail, Mantle Of Discord, Stone
    of Binding, Gladiator''s Shield, Screeching Gargoyle, Prophetic Cloak, Magi''s
    Cloak, Rod of Asclepius, Ancile, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.68
      pick: 0.12
      fit: 0.62
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.63
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.77
      win: 0.52
      pick: 0.0
      fit: 0.2
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.63
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Rod of Tahuti
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Freya''s Tears, Amanita Charm, Shield of the Phoenix,
    Soul Gem, Kinetic Cuirass, Gluttonous Grimoire, Rod of Tahuti, Rod of Asclepius,
    Chandra''s Grace, Oni Hunter''s Garb, Erosion, Shifter''s Shield, Eye of Providence,
    Phoenix Feather, Spectral Armor, Lifebinder, Nimble Ring, Blood-Bound Book, Glorious
    Pridwen, Leviathan''s Hide, Bancroft''s Talon, Midgardian Mail, Gladiator''s Shield,
    Helm of Radiance, Breastplate of Valor.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.68
      pick: 0.12
      fit: 0.55
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.62
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.77
      win: 0.52
      pick: 0.0
      fit: 0.21
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Draconic Scale, Rod of Tahuti, Gluttonous Grimoire,
    Soul Gem, Kinetic Cuirass, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    The Cosmic Horror, Spear of Desolation, Void Shield, Spear of the Magus, Shield
    of the Phoenix, Oni Hunter''s Garb, Void Stone, Nimble Ring, Erosion, Shifter''s
    Shield, Spectral Armor, Eye of Providence, Obsidian Shard, Helm of Radiance, Leviathan''s
    Hide, Midgardian Mail, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.28
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.68
      pick: 0.12
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.66
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.45
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.52
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
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
    this god: Freya''s Tears, Draconic Scale, Nimble Ring, Rod of Tahuti, Gluttonous
    Grimoire, Kinetic Cuirass, Amanita Charm, Soul Gem, Oni Hunter''s Garb, Shield
    of the Phoenix, Spectral Armor, Erosion, Shifter''s Shield, Eye of Providence,
    Helm of Radiance, Leviathan''s Hide, Death Metal, Midgardian Mail, The Cosmic
    Horror, Screeching Gargoyle, Mantle Of Discord, Rod of Asclepius, Bracer of The
    Abyss, Stone of Binding, Chronos'' Pendant, Breastplate of Valor.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.45
      efficiency: 0.42
      win: 0.52
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.68
      pick: 0.12
      fit: 0.33
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.34
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.77
      win: 0.52
      pick: 0.0
      fit: 0.11
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Shield of the Phoenix
  - Rod of Tahuti
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Draconic Scale, Kinetic
    Cuirass, Shield of the Phoenix, Rod of Tahuti, Amanita Charm, Soul Gem, Gluttonous
    Grimoire, Screeching Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring,
    Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Shifter''s
    Shield, Spectral Armor, Eye of Providence, Prophetic Cloak, Leviathan''s Hide,
    Gem of Focus, Helm of Radiance, Midgardian Mail, Breastplate of Valor, Mantle
    Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.68
      pick: 0.12
      fit: 0.64
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.45
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.77
      win: 0.52
      pick: 0.0
      fit: 0.13
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - Draconic Scale
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Draconic Scale, Rod of Tahuti,
    The Crusher, Jotunn''s Revenge, Gluttonous Grimoire, Kinetic Cuirass, Berserker''s
    Shield, Amanita Charm, Nimble Ring, Soul Gem, Hydra''s Lament, Runeforged Hammer,
    Oni Hunter''s Garb, Shield Splitter, Shield of the Phoenix, Golden Blade, Eye
    of the Storm, Pharaoh''s Curse, Death Metal, Spectral Armor, Erosion, Shifter''s
    Shield, The Cosmic Horror, Eye of Providence, Lernaean Bow, Spear of the Magus,
    The Reaper, Spear of Desolation, Damaru, Avenging Blade, Helm of Radiance, Leviathan''s
    Hide, Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Screeching Gargoyle,
    Stone of Binding, Rod of Asclepius, Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.68
      pick: 0.12
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.44
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.38
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.52
      pick: 0.0
      fit: 0.23
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - Draconic Scale
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Draconic Scale, Rod
    of Tahuti, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Kinetic Cuirass,
    Amanita Charm, Soul Gem, Berserker''s Shield, Nimble Ring, Oni Hunter''s Garb,
    Shield of the Phoenix, Hydra''s Lament, The Cosmic Horror, Runeforged Hammer,
    Death Metal, Shield Splitter, Spear of the Magus, Spear of Desolation, Erosion,
    Helm of Radiance, Spectral Armor, Shifter''s Shield, Eye of the Storm, Eye of
    Providence, Rod of Asclepius, Chronos'' Pendant, Pharaoh''s Curse, The Reaper,
    Leviathan''s Hide, Obsidian Shard, Golden Blade, Jade Scepter, Midgardian Mail,
    Avenging Blade, Damaru, Mantle Of Discord, Screeching Gargoyle, Breastplate of
    Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.68
      pick: 0.12
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.53
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.4
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.52
      pick: 0.0
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Freya''s
    Tears, Gluttonous Grimoire, Shield of the Phoenix, Breastplate of Valor, Erosion,
    Shifter''s Shield, Oni Hunter''s Garb, Eye of Providence, Draconic Scale, Soul
    Gem, Spectral Armor, Nimble Ring, Leviathan''s Hide, Helm of Radiance, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Gladiator''s Shield, Screeching Gargoyle,
    Prophetic Cloak, Magi''s Cloak, Rod of Asclepius, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.39
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.64
      win: 0.36
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.68
      pick: 0.12
      fit: 0.62
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.77
      win: 0.52
      pick: 0.0
      fit: 0.2
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.63
  starter: *id001
---
