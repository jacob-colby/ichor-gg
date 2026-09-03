---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.75
  aspect_win_rate: 0.57
  slot_order:
  - name: The Cosmic Horror
    pick_rate: 0.19
    win_rate: 0.61
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.17
      win_rate: 0.61
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.53
    alternates:
    - name: Totem of Death
      pick_rate: 0.13
      win_rate: 0.55
    - name: The Cosmic Horror
      pick_rate: 0.13
      win_rate: 0.57
  - name: Totem of Death
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.64
    - name: Omen Drum
      pick_rate: 0.1
      win_rate: 0.54
  - name: Omen Drum
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: Totem of Death
      pick_rate: 0.12
      win_rate: 0.62
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.69
  - name: Rod of Tahuti
    pick_rate: 0.06
    win_rate: 0.69
    alternates:
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.56
    - name: Obsidian Shard
      pick_rate: 0.05
      win_rate: 0.73
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.42
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.55
    - name: Void Shard
      pick_rate: 0.05
      win_rate: 0.63
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.3
    win_rate: 0.49
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.63
  - name: Selflessness
    pick_rate: 0.21
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-09-02'
  god_win_rate: 0.553133514986376
  god_matches_won: 203
  god_matches_played: 367
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-01'
  god_matches_analyzed: 8200
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Rod of Tahuti, Freya''s Tears, Amanita Charm, Kinetic Cuirass, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Prophetic Cloak,
    Hide of the Nemean Lion, Leviathan''s Hide, Helm of Darkness, Void Shield, Spear
    of Desolation, Ancile, Oni Hunter''s Garb, Gladiator''s Shield, Xibalban Effigy,
    Stampede.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.69
      pick: 0.13
      fit: 0.65
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.7
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.73
      pick: 0.11
      fit: 0.25
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Freya's Tears
  - Obsidian Shard
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Freya''s Tears, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Shifter''s Shield, Soul Gem, Breastplate of
    Valor, Erosion, Eye of Providence, Draconic Scale, Ethereal Staff, Gluttonous
    Grimoire, Phoenix Feather, Chandra''s Grace, Yogi''s Necklace, Glorious Pridwen,
    Lifebinder, Midgardian Mail, Stone of Binding, Helm of Radiance, Hide of the Nemean
    Lion, Leviathan''s Hide, Void Shield, Magi''s Cloak, Ancile, Stampede.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.93
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.69
      pick: 0.13
      fit: 0.58
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.68
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.73
      pick: 0.11
      fit: 0.26
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.98
  community_ordered:
  - Freya's Tears
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Rod of Tahuti, Obsidian Shard, Freya''s Tears, Amanita Charm, Stone
    of Binding, Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of
    Desolation, Soul Gem, Spear of the Magus, Void Shield, Breastplate of Valor, Void
    Stone, Shifter''s Shield, Erosion, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Doom Orb, Helm of Radiance, The World Stone, Magi''s Cloak, Dreamer''s
    Idol, Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean
    Lion.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.69
      pick: 0.13
      fit: 0.45
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.69
      pick: 0.13
      fit: 0.41
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.73
      pick: 0.11
      fit: 0.51
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Rod of Tahuti
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Freya''s Tears, Amanita Charm, Obsidian Shard, Nimble
    Ring, Kinetic Cuirass, Gluttonous Grimoire, Breastplate of Valor, Shifter''s Shield,
    Soul Gem, Helm of Radiance, Erosion, Shield of the Phoenix, Stone of Binding,
    Eye of Providence, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Spear of
    Desolation, Spear of the Magus, Daybreak Gavel, Bragi''s Harp, Rod of Asclepius,
    Midgardian Mail, Mantle Of Discord, Bracer of The Abyss, Hide of the Nemean Lion,
    Leviathan''s Hide.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.61
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.69
      pick: 0.13
      fit: 0.33
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.69
      pick: 0.13
      fit: 0.08
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Breastplate
    of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Screeching Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic
    Cloak, Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of
    Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen,
    Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.69
      pick: 0.13
      fit: 0.64
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.69
      pick: 0.13
      fit: 0.13
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.73
      pick: 0.11
      fit: 0.23
  community_ordered:
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Freya''s
    Tears, Obsidian Shard, Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield
    Splitter, Golden Blade, Breastplate of Valor, Runeforged Hammer, Shifter''s Shield,
    Gluttonous Grimoire, Eye of the Storm, Tyrfing, Hydra''s Lament, Heartseeker,
    Spear of Desolation, Lernaean Bow, Spear of the Magus, Erosion, Silverbranch Bow,
    Tekko-Kagi, Eye of Providence, Soul Gem, Shield of the Phoenix, Avenging Blade,
    Helm of Radiance, Stone of Binding, Draconic Scale, Toxic Blade, Titan''s Bane,
    The Crusher, Pharaoh''s Curse, Nimble Ring, Magi''s Cloak, The Reaper, Screeching
    Gargoyle, Shogun''s Ofuda, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.69
      pick: 0.13
      fit: 0.38
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.69
      pick: 0.13
      fit: 0.2
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.73
      pick: 0.11
      fit: 0.3
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Obsidian
    Shard, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Breastplate of Valor, Spear of Desolation, Shield Splitter, Spear of the Magus,
    Soul Gem, Runeforged Hammer, Helm of Radiance, Shifter''s Shield, Berserker''s
    Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion,
    Eye of Providence, Shield of the Phoenix, Stone of Binding, Draconic Scale, Doom
    Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Chronos''
    Pendant, Magi''s Cloak, The World Stone, Helm of Darkness, Titan''s Bane, Screeching
    Gargoyle, Ancient Signet, The Crusher, Mantle Of Discord, Dreamer''s Idol, Midgardian
    Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.69
      pick: 0.13
      fit: 0.38
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.69
      pick: 0.13
      fit: 0.32
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.73
      pick: 0.11
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Freya''s
    Tears, Shifter''s Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance,
    Gluttonous Grimoire, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail,
    Prophetic Cloak, Hide of the Nemean Lion, Leviathan''s Hide, Helm of Darkness,
    Void Shield, Stampede, Spear of Desolation, Ancile, Oni Hunter''s Garb, Gladiator''s
    Shield, Xibalban Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.18
      fit: 0.4
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.69
      pick: 0.13
      fit: 0.65
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
