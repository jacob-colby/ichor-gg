---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.39
  aspect_win_rate: 0.47
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.14
      win_rate: 0.43
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.56
  - name: Totem of Death
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.53
    - name: Soul Reaver
      pick_rate: 0.1
      win_rate: 0.46
  - name: The Cosmic Horror
    pick_rate: 0.13
    win_rate: 0.43
    alternates:
    - name: Totem of Death
      pick_rate: 0.14
      win_rate: 0.45
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.47
  - name: Omen Drum
    pick_rate: 0.1
    win_rate: 0.44
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.55
    - name: The Cosmic Horror
      pick_rate: 0.08
      win_rate: 0.49
  - name: Rod of Tahuti
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Omen Drum
      pick_rate: 0.07
      win_rate: 0.45
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.37
  - name: Void Shard
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.67
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.47
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.54
  - name: Bluestone Pendant
    pick_rate: 0.37
    win_rate: 0.4
  - name: Archmage's Gem
    pick_rate: 0.07
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-08-21'
  god_win_rate: 0.48534201954397393
  god_matches_won: 298
  god_matches_played: 614
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Freya''s Tears, Shield
    of the Phoenix, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale,
    Mantle Of Discord, Stone of Binding, Gluttonous Grimoire, Spectral Armor, Magi''s
    Cloak, Leviathan''s Hide, Helm of Radiance, Soul Gem, Midgardian Mail, Screeching
    Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Doublet of Binding, Helm of
    Darkness, Void Shield, Stampede, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.47
      pick: 0.19
      fit: 0.39
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.71
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Shifter''s Shield,
    Soul Gem, Freya''s Tears, Ethereal Staff, Rod of Asclepius, Gluttonous Grimoire,
    Erosion, Phoenix Feather, Eye of Providence, Breastplate of Valor, Draconic Scale,
    Chandra''s Grace, Spectral Armor, Mantle Of Discord, Stone of Binding, Yogi''s
    Necklace, Leviathan''s Hide, Glorious Pridwen, Lifebinder, Midgardian Mail, Helm
    of Radiance, Hide of the Nemean Lion, Doublet of Binding, Spirit Robe.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.19
      fit: 0.36
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.57
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.7
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Shifter's Shield
  - Rod of Tahuti
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
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
    for this god: Gluttonous Grimoire, Amanita Charm, Stone of Binding, Kinetic Cuirass,
    Soul Gem, Shifter''s Shield, Freya''s Tears, Screeching Gargoyle, Spear of Desolation,
    Spear of the Magus, Void Shield, Breastplate of Valor, Obsidian Shard, Void Stone,
    Shield of the Phoenix, Mantle Of Discord, Erosion, Eye of Providence, Draconic
    Scale, Spectral Armor, Doom Orb, Helm of Radiance, The World Stone, Leviathan''s
    Hide, Dreamer''s Idol, Magi''s Cloak.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.54
      win: 0.47
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.66
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.17
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Nimble Ring, Shifter''s Shield, Freya''s
    Tears, Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Shield of the Phoenix,
    Mantle Of Discord, Stone of Binding, Death Metal, Spectral Armor, Helm of Radiance,
    Erosion, Eye of Providence, Draconic Scale, Leviathan''s Hide, Magi''s Cloak,
    Screeching Gargoyle, Daybreak Gavel, Spear of the Magus, Spear of Desolation,
    Ethereal Staff, Bragi''s Harp, Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.43
      efficiency: 0.44
      win: 0.47
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.5
      pick: 0.17
      fit: 0.08
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Shifter''s Shield,
    Spear of Desolation, Screeching Gargoyle, Gluttonous Grimoire, Mantle Of Discord,
    Stone of Binding, Prophetic Cloak, Erosion, Helm of Radiance, Eye of Providence,
    Gladiator''s Shield, Spectral Armor, Chronos'' Pendant, Death Metal, Draconic
    Scale, Nimble Ring, Chandra''s Grace, Gem of Focus, Leviathan''s Hide, Magi''s
    Cloak, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.45
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita
    Charm, Kinetic Cuirass, Shifter''s Shield, Gluttonous Grimoire, Freya''s Tears,
    The Crusher, Shield Splitter, Runeforged Hammer, Breastplate of Valor, Golden
    Blade, Soul Gem, Death Metal, Eye of the Storm, Shield of the Phoenix, Hydra''s
    Lament, Mantle Of Discord, Stone of Binding, Heartseeker, Nimble Ring, The Reaper,
    Pharaoh''s Curse, Spear of Desolation, Lernaean Bow, Tyrfing, Erosion, Spear of
    the Magus, Spectral Armor, Tekko-Kagi, Eye of Providence, Shogun''s Ofuda, Avenging
    Blade, Helm of Radiance, Draconic Scale, Obsidian Shard, Titan''s Bane, Leviathan''s
    Hide, Magi''s Cloak, Silverbranch Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.47
      pick: 0.19
      fit: 0.23
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.51
    Shifter's Shield:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.41
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Gluttonous Grimoire, Kinetic Cuirass, Berserker''s Shield, Shifter''s Shield,
    Soul Gem, Freya''s Tears, Death Metal, The Crusher, Shield Splitter, Breastplate
    of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer, Helm of
    Radiance, Obsidian Shard, Nimble Ring, Shield of the Phoenix, Mantle Of Discord,
    Stone of Binding, Eye of the Storm, Ethereal Staff, Hydra''s Lament, Rod of Asclepius,
    Heartseeker, Erosion, Spectral Armor, The Reaper, Eye of Providence, Golden Blade,
    Draconic Scale, Doom Orb, Jade Scepter, Leviathan''s Hide, Pharaoh''s Curse, Wish-Granting
    Pearl, Avenging Blade, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.47
      pick: 0.19
      fit: 0.23
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.52
    Shifter's Shield:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.42
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.42
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
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Freya''s Tears, Shifter''s
    Shield, Shield of the Phoenix, Breastplate of Valor, Erosion, Eye of Providence,
    Draconic Scale, Mantle Of Discord, Stone of Binding, Gluttonous Grimoire, Spectral
    Armor, Magi''s Cloak, Leviathan''s Hide, Helm of Radiance, Soul Gem, Midgardian
    Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Doublet of
    Binding, Helm of Darkness, Void Shield, Stampede, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.47
      pick: 0.19
      fit: 0.39
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.47
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.14
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.71
  starter: *id001
---
