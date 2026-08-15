---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.56
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.34
    win_rate: 0.4
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.2
      win_rate: 0.58
    - name: Chronos' Pendant
      pick_rate: 0.14
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.67
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.5
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.43
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.36
  - name: The Cosmic Horror
    pick_rate: 0.08
    win_rate: 0.64
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.61
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.7
  - name: Staff of Myrddin
    pick_rate: 0.06
    win_rate: 0.57
    alternates:
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.29
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.57
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.75
    - name: Rod of Tahuti
      pick_rate: 0.04
      win_rate: 0.67
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.28
    win_rate: 0.63
  - name: Bumba's Cudgel
    pick_rate: 0.23
    win_rate: 0.42
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.48
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-14'
  god_win_rate: 0.5225806451612903
  god_matches_won: 81
  god_matches_played: 155
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
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Dwarven Plate — magical protection
    swap_item: Dwarven Plate
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Freya''s Tears, The Crusher, Jotunn''s Revenge, Gluttonous Grimoire, Shield Splitter,
    Oni Hunter''s Garb, Shield of the Phoenix, Erosion, Eye of Providence, Eye of
    the Storm, Hydra''s Lament, Spectral Armor, Pharaoh''s Curse, Nimble Ring, Leviathan''s
    Hide, Soul Gem, Midgardian Mail, Mantle Of Discord, Golden Blade, Stone of Binding,
    Avenging Blade, Death Metal, Magi''s Cloak, Ancile, Screeching Gargoyle, Helm
    of Radiance, Shogun''s Ofuda, Damaru, Hide of the Nemean Lion, Gladiator''s Shield,
    Void Shield, Doublet of Binding, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.54
      pick: 0.25
      fit: 0.31
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.67
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.2
      fit: 0.48
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Berserker''s Shield, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Chandra''s Grace, Rod of Asclepius, Freya''s Tears, Oni Hunter''s Garb, The Reaper,
    Eye of the Storm, Erosion, Shield Splitter, Phoenix Feather, Eye of Providence,
    Hydra''s Lament, Spectral Armor, Golden Blade, Pharaoh''s Curse, Avenging Blade,
    Leviathan''s Hide, Nimble Ring, Midgardian Mail, Blood-Bound Book, Lifebinder,
    Glorious Pridwen, Riptalon, Bancroft''s Talon, Death Metal, Ancile, Shogun''s
    Ofuda, Gladiator''s Shield, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.54
      pick: 0.25
      fit: 0.28
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.8
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.2
      fit: 0.54
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Cosmic Horror
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - The Cosmic Horror
  - Kinetic Cuirass
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, Jotunn''s Revenge,
    The Cosmic Horror, Kinetic Cuirass, Amanita Charm, Soul Gem, Stone of Binding,
    Berserker''s Shield, Avenging Blade, Screeching Gargoyle, Freya''s Tears, Void
    Shield, Oni Hunter''s Garb, Void Stone, The Reaper, Spear of the Magus, Shield
    of the Phoenix, Shield Splitter, Hydra''s Lament, Spear of Desolation, Nimble
    Ring, Erosion, Spectral Armor, Eye of Providence, Eye of the Storm, Pharaoh''s
    Curse, Obsidian Shard, Riptalon, Leviathan''s Hide, Midgardian Mail, Heartseeker,
    Golden Blade, Silverbranch Bow, Mantle Of Discord, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.56
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.64
      pick: 0.13
      fit: 0.34
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.67
      pick: 0.12
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Nimble Ring, Kinetic Cuirass, Amanita
    Charm, Gluttonous Grimoire, Golden Blade, The Crusher, Pharaoh''s Curse, Freya''s
    Tears, Jotunn''s Revenge, Riptalon, Oni Hunter''s Garb, Shield of the Phoenix,
    Soul Gem, Shogun''s Ofuda, Tyrfing, Spectral Armor, Erosion, Hydra''s Lament,
    Lernaean Bow, Silverbranch Bow, Shield Splitter, Eye of Providence, Eye of the
    Storm, Leviathan''s Hide, Midgardian Mail, Toxic Blade, Mantle Of Discord, Stone
    of Binding, Helm of Radiance, Death Metal, Screeching Gargoyle, Yogi''s Necklace,
    Damaru, Ancile, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.54
      pick: 0.25
      fit: 0.2
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.47
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Breastplate of Valor
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s
    Revenge, Kinetic Cuirass, Shield of the Phoenix, Amanita Charm, Soul Gem, Gluttonous
    Grimoire, Hydra''s Lament, Berserker''s Shield, The Cosmic Horror, The Crusher,
    Screeching Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring, Chandra''s
    Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Spectral Armor, Eye
    of Providence, Prophetic Cloak, Shield Splitter, Pharaoh''s Curse, Eye of the
    Storm, Leviathan''s Hide, Gem of Focus, Helm of Radiance, Midgardian Mail, Mantle
    Of Discord, Totem of Death, Stone of Binding, Arondight, Death Metal, Rod of Asclepius,
    Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.54
      pick: 0.25
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.23
      fit: 0.48
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, The Crusher, Jotunn''s Revenge,
    Kinetic Cuirass, Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, The
    Cosmic Horror, Freya''s Tears, Nimble Ring, Shield Splitter, Hydra''s Lament,
    Oni Hunter''s Garb, Soul Gem, Golden Blade, Eye of the Storm, Shield of the Phoenix,
    Pharaoh''s Curse, Erosion, Spectral Armor, Eye of Providence, The Reaper, Lernaean
    Bow, Death Metal, Avenging Blade, Damaru, Shogun''s Ofuda, Leviathan''s Hide,
    Midgardian Mail, Spear of the Magus, Mantle Of Discord, Stone of Binding, Tekko-Kagi,
    Spear of Desolation, Tyrfing, Riptalon, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.54
      pick: 0.25
      fit: 0.23
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.52
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Cosmic Horror
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    The Cosmic Horror, The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm,
    Soul Gem, Berserker''s Shield, Nimble Ring, Freya''s Tears, Oni Hunter''s Garb,
    Shield Splitter, Shield of the Phoenix, Death Metal, Spear of the Magus, Hydra''s
    Lament, Erosion, Spear of Desolation, Eye of the Storm, Helm of Radiance, Spectral
    Armor, Eye of Providence, Rod of Asclepius, Chronos'' Pendant, Pharaoh''s Curse,
    The Reaper, Obsidian Shard, Leviathan''s Hide, Golden Blade, Jade Scepter, Midgardian
    Mail, Avenging Blade, Mantle Of Discord, Damaru, Stone of Binding, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.55
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.64
      pick: 0.13
      fit: 0.33
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.67
      pick: 0.12
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Rod of Tahuti, Freya''s Tears, The Crusher, Jotunn''s Revenge, Gluttonous Grimoire,
    Shield Splitter, Oni Hunter''s Garb, Shield of the Phoenix, Erosion, Eye of Providence,
    Eye of the Storm, Draconic Scale, Hydra''s Lament, Spectral Armor, Pharaoh''s
    Curse, Nimble Ring, Leviathan''s Hide, Soul Gem, Midgardian Mail, Mantle Of Discord,
    Golden Blade, Stone of Binding, Avenging Blade, Death Metal, Magi''s Cloak, Ancile,
    Screeching Gargoyle, Helm of Radiance, Shogun''s Ofuda, Damaru, Hide of the Nemean
    Lion, Gladiator''s Shield, Void Shield, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.54
      pick: 0.25
      fit: 0.31
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.52
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.57
  starter: *id001
---
