---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.4
  aspect_win_rate: 0.54
  slot_order:
  - name: Chronos' Pendant
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.6
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.65
    alternates:
    - name: Totem of Death
      pick_rate: 0.12
      win_rate: 0.56
    - name: Soul Reaver
      pick_rate: 0.12
      win_rate: 0.42
  - name: Totem of Death
    pick_rate: 0.16
    win_rate: 0.48
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.11
      win_rate: 0.48
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.39
  - name: Omen Drum
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.1
      win_rate: 0.5
    - name: Ethereal Staff
      pick_rate: 0.07
      win_rate: 0.38
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.47
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.77
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.42
  - name: Void Shard
    pick_rate: 0.1
    win_rate: 0.4
    alternates:
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.5
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.75
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.37
    win_rate: 0.42
  - name: Bluestone Brooch
    pick_rate: 0.35
    win_rate: 0.54
  - name: Archmage's Gem
    pick_rate: 0.06
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-08-15'
  god_win_rate: 0.5196078431372549
  god_matches_won: 106
  god_matches_played: 204
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
  - Shifter's Shield
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Erosion, Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb,
    Breastplate of Valor, Draconic Scale, Spectral Armor, Leviathan''s Hide, Mantle
    Of Discord, Midgardian Mail, Soul Gem, Stone of Binding, Nimble Ring, Magi''s
    Cloak, Gladiator''s Shield, Ancile, Helm of Radiance, Prophetic Cloak, Screeching
    Gargoyle, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.65
      pick: 0.18
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.48
      pick: 0.0
      fit: 0.81
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.6
      pick: 0.12
      fit: 0.71
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.75
      pick: 0.25
      fit: 0.15
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.77
      pick: 0.17
      fit: 0.15
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Shield of the Phoenix
  - Shifter's Shield
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Obsidian Shard
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shifter''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Gluttonous Grimoire, Chandra''s Grace, Rod of Asclepius, Freya''s Tears,
    Oni Hunter''s Garb, Erosion, Eye of Providence, Draconic Scale, Phoenix Feather,
    Breastplate of Valor, Spectral Armor, Leviathan''s Hide, Midgardian Mail, Lifebinder,
    Glorious Pridwen, Nimble Ring, Gladiator''s Shield, Ancile, Blood-Bound Book,
    Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.65
      pick: 0.18
      fit: 0.36
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.92
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.6
      pick: 0.12
      fit: 0.7
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.75
      pick: 0.25
      fit: 0.16
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.77
      pick: 0.17
      fit: 0.16
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Shifter''s Shield, Kinetic Cuirass, Amanita
    Charm, Soul Gem, Stone of Binding, Screeching Gargoyle, Freya''s Tears, Void Shield,
    Breastplate of Valor, Spear of the Magus, Oni Hunter''s Garb, Void Stone, Shield
    of the Phoenix, Spear of Desolation, Erosion, Eye of Providence, Spectral Armor,
    Nimble Ring, Draconic Scale, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.65
      pick: 0.18
      fit: 0.27
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.48
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.66
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.12
      fit: 0.49
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.77
      win: 0.75
      pick: 0.25
      fit: 0.41
    Obsidian Shard:
      total: 0.6
      efficiency: 0.52
      win: 0.77
      pick: 0.17
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Nimble Ring, Kinetic Cuirass, Amanita Charm, Gluttonous
    Grimoire, Freya''s Tears, Breastplate of Valor, Oni Hunter''s Garb, Soul Gem,
    Shield of the Phoenix, Spectral Armor, Erosion, Eye of Providence, Draconic Scale,
    Leviathan''s Hide, Midgardian Mail, Helm of Radiance, Mantle Of Discord, Stone
    of Binding, Death Metal, Screeching Gargoyle, Yogi''s Necklace, Bracer of The
    Abyss, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.65
      pick: 0.18
      fit: 0.2
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.51
      win: 0.48
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.5
      efficiency: 0.68
      win: 0.48
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.43
      efficiency: 0.42
      win: 0.48
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.75
      pick: 0.25
      fit: 0.08
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.77
      pick: 0.17
      fit: 0.08
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Freya''s Tears,
    Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix, Amanita Charm, Soul
    Gem, Gluttonous Grimoire, Screeching Gargoyle, Oni Hunter''s Garb, Nimble Ring,
    Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Spectral
    Armor, Eye of Providence, Prophetic Cloak, Draconic Scale, Leviathan''s Hide,
    Gem of Focus, Helm of Radiance, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.69
      win: 0.65
      pick: 0.18
      fit: 0.48
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.48
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.12
      fit: 0.45
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.75
      pick: 0.25
      fit: 0.13
    Obsidian Shard:
      total: 0.56
      efficiency: 0.52
      win: 0.77
      pick: 0.17
      fit: 0.13
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Shifter's Shield
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Shifter''s Shield, The Crusher, Jotunn''s
    Revenge, Kinetic Cuirass, Gluttonous Grimoire, Berserker''s Shield, Amanita Charm,
    Freya''s Tears, Nimble Ring, Runeforged Hammer, Breastplate of Valor, Shield Splitter,
    Soul Gem, Hydra''s Lament, Oni Hunter''s Garb, Golden Blade, Shield of the Phoenix,
    Eye of the Storm, Pharaoh''s Curse, Erosion, Spectral Armor, Eye of Providence,
    Death Metal, The Reaper, Lernaean Bow, Draconic Scale, Avenging Blade, Damaru,
    Leviathan''s Hide, Spear of the Magus, Shogun''s Ofuda, Midgardian Mail, Mantle
    Of Discord, Spear of Desolation, Stone of Binding, Helm of Radiance, Tekko-Kagi,
    Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.65
      pick: 0.18
      fit: 0.23
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.45
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.12
      fit: 0.41
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.77
      win: 0.75
      pick: 0.25
      fit: 0.2
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.77
      pick: 0.17
      fit: 0.2
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Gluttonous Grimoire
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Gluttonous Grimoire,
    The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Soul Gem, Berserker''s
    Shield, Nimble Ring, Freya''s Tears, Breastplate of Valor, Oni Hunter''s Garb,
    Runeforged Hammer, Shield Splitter, Shield of the Phoenix, Death Metal, Spear
    of the Magus, Hydra''s Lament, Erosion, Spear of Desolation, Eye of the Storm,
    Helm of Radiance, Spectral Armor, Eye of Providence, Draconic Scale, Rod of Asclepius,
    Pharaoh''s Curse, The Reaper, Leviathan''s Hide, Golden Blade, Jade Scepter, Midgardian
    Mail, Avenging Blade, Mantle Of Discord, Damaru, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.65
      pick: 0.18
      fit: 0.23
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.12
      fit: 0.42
    The Crusher:
      total: 0.5
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.75
      pick: 0.25
      fit: 0.33
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.77
      pick: 0.17
      fit: 0.33
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Erosion, Shifter''s Shield, Shield of the Phoenix, Eye of Providence,
    Oni Hunter''s Garb, Breastplate of Valor, Draconic Scale, Spectral Armor, Leviathan''s
    Hide, Mantle Of Discord, Midgardian Mail, Soul Gem, Stone of Binding, Nimble Ring,
    Magi''s Cloak, Gladiator''s Shield, Ancile, Helm of Radiance, Prophetic Cloak,
    Screeching Gargoyle, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.65
      pick: 0.18
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.48
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.48
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.6
      pick: 0.12
      fit: 0.71
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.5
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.71
  starter: *id001
---
