---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.83
  aspect_win_rate: 0.58
  slot_order:
  - name: Damaru
    pick_rate: 0.21
    win_rate: 0.59
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.18
      win_rate: 0.5
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.5
  - name: The Cosmic Horror
    pick_rate: 0.2
    win_rate: 0.6
    alternates:
    - name: Totem of Death
      pick_rate: 0.19
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.71
  - name: Totem of Death
    pick_rate: 0.23
    win_rate: 0.58
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.13
      win_rate: 0.6
    - name: Damaru
      pick_rate: 0.1
      win_rate: 0.57
  - name: Omen Drum
    pick_rate: 0.23
    win_rate: 0.61
    alternates:
    - name: Totem of Death
      pick_rate: 0.13
      win_rate: 0.66
    - name: The Cosmic Horror
      pick_rate: 0.07
      win_rate: 0.8
  - name: Rod of Tahuti
    pick_rate: 0.2
    win_rate: 0.59
    alternates:
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.62
    - name: Omen Drum
      pick_rate: 0.06
      win_rate: 0.82
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.75
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.71
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.29
    win_rate: 0.65
  - name: Bluestone Pendant
    pick_rate: 0.29
    win_rate: 0.52
  - name: Selflessness
    pick_rate: 0.14
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-08-14'
  god_win_rate: 0.576271186440678
  god_matches_won: 136
  god_matches_played: 236
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
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Obsidian Shard
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
    this god: Genji''s Guard, Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Shield of the Phoenix, Erosion, Shifter''s Shield, Eye of Providence,
    Breastplate of Valor, Oni Hunter''s Garb, Draconic Scale, Spectral Armor, Soul
    Gem, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding,
    Nimble Ring, Gladiator''s Shield, Magi''s Cloak, Screeching Gargoyle, Ancile,
    Prophetic Cloak, Helm of Radiance, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.69
      win: 0.71
      pick: 0.1
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.59
      pick: 0.43
      fit: 0.15
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.75
      pick: 0.22
      fit: 0.15
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.7
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
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Rod of Tahuti
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Gluttonous Grimoire, Chandra''s Grace, Freya''s Tears, Rod of Asclepius,
    Oni Hunter''s Garb, Erosion, Shifter''s Shield, Eye of Providence, Breastplate
    of Valor, Draconic Scale, Phoenix Feather, Spectral Armor, Leviathan''s Hide,
    Midgardian Mail, Glorious Pridwen, Lifebinder, Gladiator''s Shield, Nimble Ring,
    Blood-Bound Book, Ancile, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.69
      win: 0.71
      pick: 0.1
      fit: 0.37
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.93
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.59
      pick: 0.43
      fit: 0.16
    Amanita Charm:
      total: 0.63
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.98
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Kinetic Cuirass
  - The Cosmic Horror
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
    for this god: Genji''s Guard, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Stone of Binding, Screeching Gargoyle, Freya''s Tears, Void Shield,
    Breastplate of Valor, Spear of the Magus, Oni Hunter''s Garb, Shield of the Phoenix,
    Spear of Desolation, Void Stone, Erosion, Shifter''s Shield, Eye of Providence,
    Spectral Armor, Nimble Ring, Draconic Scale, Leviathan''s Hide, Midgardian Mail,
    Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.69
      win: 0.71
      pick: 0.1
      fit: 0.28
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.65
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.27
      fit: 0.41
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.59
      pick: 0.43
      fit: 0.41
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.75
      pick: 0.22
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Nimble Ring, Kinetic Cuirass, Amanita Charm, Gluttonous
    Grimoire, Freya''s Tears, Breastplate of Valor, Oni Hunter''s Garb, Soul Gem,
    Shield of the Phoenix, Spectral Armor, Erosion, Shifter''s Shield, Eye of Providence,
    Draconic Scale, Leviathan''s Hide, Midgardian Mail, Helm of Radiance, Mantle Of
    Discord, Stone of Binding, Death Metal, Screeching Gargoyle, Yogi''s Necklace,
    Bracer of The Abyss, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.71
      pick: 0.1
      fit: 0.21
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.48
      efficiency: 0.42
      win: 0.59
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.59
      pick: 0.43
      fit: 0.08
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Freya''s Tears, Breastplate
    of Valor, Kinetic Cuirass, Shield of the Phoenix, Amanita Charm, Soul Gem, Gluttonous
    Grimoire, Screeching Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring,
    Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Shifter''s
    Shield, Spectral Armor, Eye of Providence, Prophetic Cloak, Draconic Scale, Leviathan''s
    Hide, Gem of Focus, Helm of Radiance, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.69
      win: 0.71
      pick: 0.1
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.64
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.59
      pick: 0.43
      fit: 0.13
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Genji''s Guard, The Crusher, Jotunn''s Revenge,
    Kinetic Cuirass, Gluttonous Grimoire, Berserker''s Shield, Amanita Charm, Freya''s
    Tears, Nimble Ring, Breastplate of Valor, Runeforged Hammer, Soul Gem, Hydra''s
    Lament, Shield Splitter, Oni Hunter''s Garb, Shield of the Phoenix, Golden Blade,
    Eye of the Storm, Pharaoh''s Curse, Erosion, Shifter''s Shield, Spectral Armor,
    Eye of Providence, Death Metal, Lernaean Bow, The Reaper, Draconic Scale, Avenging
    Blade, Spear of the Magus, Leviathan''s Hide, Shogun''s Ofuda, Midgardian Mail,
    Spear of Desolation, Mantle Of Discord, Stone of Binding, Helm of Radiance, Tekko-Kagi,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.71
      pick: 0.1
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.59
      pick: 0.43
      fit: 0.2
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.75
      pick: 0.22
      fit: 0.2
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Gluttonous Grimoire,
    The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Soul Gem, Berserker''s
    Shield, Nimble Ring, Freya''s Tears, Breastplate of Valor, Oni Hunter''s Garb,
    Runeforged Hammer, Shield of the Phoenix, Hydra''s Lament, Shield Splitter, Death
    Metal, Spear of the Magus, Spear of Desolation, Erosion, Helm of Radiance, Shifter''s
    Shield, Eye of the Storm, Spectral Armor, Eye of Providence, Draconic Scale, Rod
    of Asclepius, Pharaoh''s Curse, Chronos'' Pendant, The Reaper, Leviathan''s Hide,
    Golden Blade, Jade Scepter, Midgardian Mail, Avenging Blade, Mantle Of Discord,
    Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.71
      pick: 0.1
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.59
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.59
      pick: 0.43
      fit: 0.32
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.75
      pick: 0.22
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Erosion
  flex_slots:
  - Rod of Tahuti
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Genji''s
    Guard, Gluttonous Grimoire, Shield of the Phoenix, Erosion, Shifter''s Shield,
    Eye of Providence, Breastplate of Valor, Oni Hunter''s Garb, Draconic Scale, Spectral
    Armor, Soul Gem, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Stone
    of Binding, Nimble Ring, Gladiator''s Shield, Magi''s Cloak, Screeching Gargoyle,
    Ancile, Prophetic Cloak, Helm of Radiance, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.69
      win: 0.71
      pick: 0.1
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.59
      pick: 0.43
      fit: 0.15
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.7
    Erosion:
      total: 0.55
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.7
  starter: *id001
---
