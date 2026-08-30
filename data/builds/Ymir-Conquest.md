---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Stampede
    pick_rate: 0.22
    win_rate: 0.51
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.66
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.52
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.51
    alternates:
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.78
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.56
  - name: Kinetic Cuirass
    pick_rate: 0.08
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.47
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.61
    alternates:
    - name: Spirit Robe
      pick_rate: 0.09
      win_rate: 0.58
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.65
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.8
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.6
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.44
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.75
    alternates:
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 0.4
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.75
  community_starters:
  - name: Selflessness
    pick_rate: 0.17
    win_rate: 0.46
  - name: Warrior's Axe
    pick_rate: 0.16
    win_rate: 0.51
  - name: War Flag
    pick_rate: 0.11
    win_rate: 0.48
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-08-30'
  god_win_rate: 0.5434782608695652
  god_matches_won: 125
  god_matches_played: 230
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-30'
  god_matches_analyzed: 5563
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
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Erosion,
    Breastplate of Valor, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Leviathan''s
    Hide, Void Shield, Helm of Darkness, Ancile, Oni Hunter''s Garb, Xibalban Effigy,
    Hussar''s Wings, Void Stone, Spectral Armor.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.53
      pick: 0.12
      fit: 0.82
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.56
      pick: 0.16
      fit: 0.72
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.72
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
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Rod of Asclepius, Rod of Tahuti, Erosion, Eye of Providence, Breastplate of Valor,
    Draconic Scale, Ethereal Staff, Phoenix Feather, Yogi''s Necklace, Chandra''s
    Grace, Glorious Pridwen, Soul Gem, Lifebinder, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.53
      pick: 0.12
      fit: 0.8
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.57
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.56
      pick: 0.16
      fit: 0.7
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Rod of Tahuti, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Spear of the Magus, Void Shield, Soul Gem, Breastplate of Valor, Obsidian Shard,
    Void Stone, Erosion, Eye of Providence, Draconic Scale, Doom Orb, Shield of the
    Phoenix, Helm of Radiance, The World Stone, Magi''s Cloak, Dreamer''s Idol, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.74
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.53
      pick: 0.12
      fit: 0.58
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.42
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.16
      fit: 0.48
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass,
    Breastplate of Valor, Erosion, Helm of Radiance, Eye of Providence, Stone of Binding,
    Shield of the Phoenix, Draconic Scale, Magi''s Cloak, Soul Gem, Bragi''s Harp,
    Screeching Gargoyle, Daybreak Gavel, Mantle Of Discord, Midgardian Mail, Rod of
    Asclepius, Gluttonous Grimoire, Bracer of The Abyss, Hide of the Nemean Lion,
    Leviathan''s Hide, Void Shield, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.12
      fit: 0.48
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.55
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.34
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.38
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shield of the Phoenix, Screeching
    Gargoyle, Chronos'' Pendant, Prophetic Cloak, Helm of Radiance, Erosion, Eye of
    Providence, Gladiator''s Shield, Soul Gem, Draconic Scale, Stone of Binding, Gem
    of Focus, Magi''s Cloak, Spear of Desolation, Rod of Asclepius, Eye of Erebus,
    Nimble Ring, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel,
    Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.51
      pick: 0.23
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.12
      fit: 0.55
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.16
      fit: 0.45
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Breastplate of Valor, Golden Blade, Eye of the Storm, Gluttonous Grimoire,
    Hydra''s Lament, Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation,
    Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging Blade, Helm of Radiance,
    Stone of Binding, Draconic Scale, Shield of the Phoenix, Soul Gem, Titan''s Bane,
    Obsidian Shard, Silverbranch Bow, The Crusher, Pharaoh''s Curse, Magi''s Cloak,
    Toxic Blade, Nimble Ring, The Reaper, Shogun''s Ofuda, Screeching Gargoyle, Mantle
    Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.12
      fit: 0.52
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.37
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.16
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s
    Revenge, Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Gluttonous Grimoire,
    Shield Splitter, Breastplate of Valor, Spear of Desolation, Spear of the Magus,
    Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Eye of the Storm,
    Golden Blade, Hydra''s Lament, Rod of Asclepius, Heartseeker, Nimble Ring, Erosion,
    Eye of Providence, Stone of Binding, Draconic Scale, Shield of the Phoenix, Jade
    Scepter, Doom Orb, Death Metal, Wish-Granting Pearl, Avenging Blade, Tyrfing,
    Magi''s Cloak, Chronos'' Pendant, The World Stone, Bragi''s Harp, Titan''s Bane,
    Helm of Darkness, Ancient Signet, Lernaean Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.12
      fit: 0.5
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.36
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.16
      fit: 0.4
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.4
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
  - Genji's Guard
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Freya''s Tears, Rod of
    Tahuti, Erosion, Breastplate of Valor, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion,
    Leviathan''s Hide, Void Shield, Helm of Darkness, Ancile, Oni Hunter''s Garb,
    Xibalban Effigy, Hussar''s Wings, Void Stone, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.51
      pick: 0.23
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.53
      pick: 0.12
      fit: 0.82
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.56
      pick: 0.16
      fit: 0.72
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.72
  starter: *id001
---
