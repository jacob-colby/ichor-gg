---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.37
  aspect_win_rate: 0.46
  slot_order:
  - name: Lifebinder
    pick_rate: 0.18
    win_rate: 0.48
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.15
      win_rate: 0.58
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.75
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.61
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.12
      win_rate: 0.33
    - name: Soul Reaver
      pick_rate: 0.07
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.61
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.11
      win_rate: 0.5
    - name: Totem of Death
      pick_rate: 0.11
      win_rate: 0.36
  - name: Omen Drum
    pick_rate: 0.2
    win_rate: 0.43
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.45
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.05
      win_rate: 0.6
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.8
  - name: Obsidian Shard
    pick_rate: 0.07
    win_rate: 0.25
    alternates:
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.25
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.4
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.25
    win_rate: 0.56
  - name: Conduit Gem
    pick_rate: 0.11
    win_rate: 0.29
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-09-12'
  god_win_rate: 0.46511627906976744
  god_matches_won: 60
  god_matches_played: 129
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-12'
  god_matches_analyzed: 4284
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Shifter''s Shield, Amanita Charm, Kinetic Cuirass, Freya''s
    Tears, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion,
    Helm of Darkness, Leviathan''s Hide, Void Shield, Stampede, Ancile, Oni Hunter''s
    Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.81
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.61
      pick: 0.3
      fit: 0.39
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.64
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.71
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.8
      pick: 0.11
      fit: 0.15
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Rod of Tahuti
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Shifter's Shield
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Shifter''s Shield, Shield of the Phoenix,
    Kinetic Cuirass, Freya''s Tears, Rod of Asclepius, Ethereal Staff, Soul Gem, Erosion,
    Eye of Providence, Draconic Scale, Gluttonous Grimoire, Phoenix Feather, Yogi''s
    Necklace, Chandra''s Grace, Glorious Pridwen, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede,
    Magi''s Cloak, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.8
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.3
      fit: 0.36
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.92
    Shifter's Shield:
      total: 0.64
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.7
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.8
      pick: 0.11
      fit: 0.16
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Shifter's Shield
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Shifter''s Shield, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Freya''s Tears, Screeching Gargoyle, Spear
    of Desolation, Spear of the Magus, Soul Gem, Void Shield, Void Stone, Erosion,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    The World Stone, Dreamer''s Idol, Magi''s Cloak, Mantle Of Discord, Midgardian
    Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.3
      fit: 0.27
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.19
      fit: 0.27
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.49
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.8
      pick: 0.11
      fit: 0.41
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Shifter's Shield
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Genji's Guard
  - Nimble Ring
  - Bragi's Harp
  - Shifter's Shield
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Rod of Tahuti, Shifter''s Shield, Amanita Charm, Nimble Ring, Kinetic
    Cuirass, Freya''s Tears, Gluttonous Grimoire, Soul Gem, Helm of Radiance, Erosion,
    Stone of Binding, Eye of Providence, Shield of the Phoenix, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the Magus, Spear of Desolation,
    Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of
    The Abyss, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.24
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.3
      fit: 0.2
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.58
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.36
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.8
      pick: 0.11
      fit: 0.08
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Shifter''s Shield,
    Freya''s Tears, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of
    Desolation, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Prophetic Cloak,
    Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of
    Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen,
    Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.19
      fit: 0.48
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.61
      pick: 0.3
      fit: 0.48
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.45
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.8
      pick: 0.11
      fit: 0.13
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Shifter's Shield
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    win/pick). Underrated for this god: Rod of Tahuti, Shifter''s Shield, Jotunn''s
    Revenge, Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Freya''s Tears,
    Shield Splitter, Runeforged Hammer, Golden Blade, Gluttonous Grimoire, Eye of
    the Storm, Hydra''s Lament, Heartseeker, Spear of Desolation, Lernaean Bow, Tyrfing,
    Erosion, Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging Blade, Helm
    of Radiance, Soul Gem, Stone of Binding, Shield of the Phoenix, Draconic Scale,
    Titan''s Bane, The Crusher, Pharaoh''s Curse, Magi''s Cloak, Nimble Ring, Silverbranch
    Bow, The Reaper, Shogun''s Ofuda, Screeching Gargoyle, Toxic Blade, Mantle Of
    Discord, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.05
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.3
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.45
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.22
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.41
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.8
      pick: 0.11
      fit: 0.2
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Shifter''s Shield,
    Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Freya''s
    Tears, Shield Splitter, Spear of Desolation, Spear of the Magus, Runeforged Hammer,
    Helm of Radiance, Soul Gem, Berserker''s Shield, Eye of the Storm, Hydra''s Lament,
    Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Chronos'' Pendant,
    Shield of the Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter,
    Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, The World Stone,
    Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet, Screeching Gargoyle,
    Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.3
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.18
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.42
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.8
      pick: 0.11
      fit: 0.33
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
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
    Tears, Shifter''s Shield, Erosion, Eye of Providence, Draconic Scale, Shield of
    the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide
    of the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Oni Hunter''s Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.19
      fit: 0.39
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.61
      pick: 0.3
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.64
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.71
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
---
