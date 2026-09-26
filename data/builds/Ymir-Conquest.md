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
  - name: Gauntlet of Thebes
    pick_rate: 0.22
    win_rate: 0.54
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.39
    - name: Runeforged Hammer
      pick_rate: 0.14
      win_rate: 0.55
  - name: Shifter's Shield
    pick_rate: 0.23
    win_rate: 0.58
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.5
  - name: Stampede
    pick_rate: 0.16
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.56
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.75
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.61
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
    - name: Stampede
      pick_rate: 0.04
      win_rate: 0.29
  - name: Veve Charm
    pick_rate: 0.06
    win_rate: 0.71
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Leather Cowl
    pick_rate: 0.21
    win_rate: 0.51
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.68
  - name: Selflessness
    pick_rate: 0.16
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-09-26'
  god_win_rate: 0.5065502183406113
  god_matches_won: 116
  god_matches_played: 229
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-26'
  god_matches_analyzed: 4198
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Genji''s Guard, Erosion,
    Breastplate of Valor, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Prophetic Cloak, Leviathan''s Hide, Void Shield, Helm
    of Darkness, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Hussar''s Wings, Void
    Stone, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.11
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.56
      pick: 0.13
      fit: 0.82
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.52
      win: 0.67
      pick: 0.18
      fit: 0.46
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.58
      pick: 0.31
      fit: 0.72
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.64
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Rod of Tahuti, Erosion, Genji''s Guard, Eye of Providence, Breastplate of Valor,
    Draconic Scale, Ethereal Staff, Phoenix Feather, Yogi''s Necklace, Chandra''s
    Grace, Glorious Pridwen, Soul Gem, Lifebinder, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Leviathan''s Hide, Void Shield, Magi''s Cloak, Ancile, Oni Hunter''s
    Garb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.56
      pick: 0.13
      fit: 0.8
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.92
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.18
      fit: 0.49
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.58
      pick: 0.31
      fit: 0.7
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.57
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Spear of the Magus,
    Void Shield, Genji''s Guard, Soul Gem, Breastplate of Valor, Obsidian Shard, Void
    Stone, Erosion, Eye of Providence, Draconic Scale, Doom Orb, Shield of the Phoenix,
    Helm of Radiance, The World Stone, Magi''s Cloak, Dreamer''s Idol, Mantle Of Discord,
    Midgardian Mail, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.74
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.13
      fit: 0.58
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.18
      fit: 0.31
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.31
      fit: 0.48
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.42
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Genji''s
    Guard, Breastplate of Valor, Erosion, Helm of Radiance, Eye of Providence, Stone
    of Binding, Shield of the Phoenix, Draconic Scale, Magi''s Cloak, Soul Gem, Bragi''s
    Harp, Screeching Gargoyle, Daybreak Gavel, Mantle Of Discord, Midgardian Mail,
    Rod of Asclepius, Gluttonous Grimoire, Bracer of The Abyss, Leviathan''s Hide,
    Void Shield, Ancile.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.45
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.18
      fit: 0.24
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.34
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shield of the Phoenix, Screeching
    Gargoyle, Chronos'' Pendant, Prophetic Cloak, Helm of Radiance, Erosion, Eye of
    Providence, Gladiator''s Shield, Soul Gem, Draconic Scale, Stone of Binding, Gem
    of Focus, Magi''s Cloak, Spear of Desolation, Rod of Asclepius, Eye of Erebus,
    Nimble Ring, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel,
    Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.11
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.13
      fit: 0.55
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.31
      fit: 0.45
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.64
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Genji''s Guard, Runeforged
    Hammer, Breastplate of Valor, Golden Blade, Eye of the Storm, Gluttonous Grimoire,
    Hydra''s Lament, Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation,
    Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging Blade, Helm of Radiance,
    Stone of Binding, Draconic Scale, Shield of the Phoenix, Soul Gem, Titan''s Bane,
    Obsidian Shard, Silverbranch Bow, The Crusher, Pharaoh''s Curse, Magi''s Cloak,
    Toxic Blade, Nimble Ring, The Reaper, Shogun''s Ofuda, Screeching Gargoyle, Mantle
    Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.13
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.18
      fit: 0.27
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Gluttonous Grimoire, Genji''s
    Guard, Shield Splitter, Breastplate of Valor, Spear of Desolation, Spear of the
    Magus, Helm of Radiance, Soul Gem, Runeforged Hammer, Obsidian Shard, Eye of the
    Storm, Golden Blade, Hydra''s Lament, Rod of Asclepius, Heartseeker, Nimble Ring,
    Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Shield of the Phoenix,
    Jade Scepter, Doom Orb, Death Metal, Wish-Granting Pearl, Avenging Blade, Tyrfing,
    Magi''s Cloak, Chronos'' Pendant, The World Stone, Bragi''s Harp, Titan''s Bane,
    Helm of Darkness, Ancient Signet, Lernaean Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.13
      fit: 0.5
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.18
      fit: 0.26
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Genji''s
    Guard, Erosion, Breastplate of Valor, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Leviathan''s Hide, Void
    Shield, Helm of Darkness, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Hussar''s
    Wings, Void Stone, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.11
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.56
      pick: 0.13
      fit: 0.82
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.58
      pick: 0.31
      fit: 0.72
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.64
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
---
