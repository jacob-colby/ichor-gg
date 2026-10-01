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
    pick_rate: 0.18
    win_rate: 0.49
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.58
    - name: Runeforged Hammer
      pick_rate: 0.11
      win_rate: 0.56
  - name: Shifter's Shield
    pick_rate: 0.2
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.51
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.61
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.69
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.65
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.71
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.54
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.51
  - name: Draconic Scale
    pick_rate: 0.04
    win_rate: 0.58
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.58
  - name: Medal of Defense
    pick_rate: 0.05
    win_rate: 0.72
    alternates:
    - name: Legionnaire Armor
      pick_rate: 0.04
      win_rate: 0.4
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.71
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.18
    win_rate: 0.65
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.52
  - name: Selflessness
    pick_rate: 0.14
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-10-01'
  god_win_rate: 0.5552099533437014
  god_matches_won: 357
  god_matches_played: 643
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-10-01'
  god_matches_analyzed: 10386
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
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
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Genji''s Guard, Rod of Tahuti, Erosion,
    Draconic Scale, Breastplate of Valor, Eye of Providence, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Leviathan''s
    Hide, Void Shield, Helm of Darkness, Ancile, Oni Hunter''s Garb, Xibalban Effigy,
    Hussar''s Wings, Void Stone, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.12
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.6
      pick: 0.27
      fit: 0.72
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.71
      pick: 0.15
      fit: 0.64
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Genji''s Guard,
    Rod of Asclepius, Rod of Tahuti, Erosion, Draconic Scale, Eye of Providence, Breastplate
    of Valor, Ethereal Staff, Phoenix Feather, Yogi''s Necklace, Chandra''s Grace,
    Glorious Pridwen, Soul Gem, Lifebinder, Midgardian Mail, Stone of Binding, Helm
    of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.12
      fit: 0.35
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.92
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.6
      pick: 0.27
      fit: 0.7
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.71
      pick: 0.15
      fit: 0.57
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
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
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Genji''s Guard,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Spear of the Magus, Void Shield, Soul Gem, Breastplate of Valor, Obsidian Shard,
    Void Stone, Erosion, Draconic Scale, Eye of Providence, Doom Orb, Shield of the
    Phoenix, Helm of Radiance, The World Stone, Magi''s Cloak, Dreamer''s Idol, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.12
      fit: 0.25
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.27
      fit: 0.48
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.71
      pick: 0.15
      fit: 0.42
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Genji''s Guard, Nimble Ring, Kinetic Cuirass,
    Breastplate of Valor, Erosion, Draconic Scale, Helm of Radiance, Eye of Providence,
    Stone of Binding, Shield of the Phoenix, Magi''s Cloak, Soul Gem, Bragi''s Harp,
    Screeching Gargoyle, Daybreak Gavel, Mantle Of Discord, Midgardian Mail, Rod of
    Asclepius, Gluttonous Grimoire, Bracer of The Abyss, Hide of the Nemean Lion,
    Leviathan''s Hide, Void Shield, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.12
      fit: 0.2
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.58
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.71
      pick: 0.15
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
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
  - Shifter's Shield
  - Kinetic Cuirass
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shield of the Phoenix, Screeching
    Gargoyle, Chronos'' Pendant, Prophetic Cloak, Helm of Radiance, Erosion, Draconic
    Scale, Eye of Providence, Gladiator''s Shield, Soul Gem, Stone of Binding, Gem
    of Focus, Magi''s Cloak, Spear of Desolation, Rod of Asclepius, Eye of Erebus,
    Nimble Ring, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel,
    Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.61
      pick: 0.12
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.27
      fit: 0.45
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.71
      pick: 0.15
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Genji''s Guard, Kinetic Cuirass, Shield Splitter, Breastplate
    of Valor, Golden Blade, Runeforged Hammer, Eye of the Storm, Gluttonous Grimoire,
    Hydra''s Lament, Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation,
    Draconic Scale, Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging Blade,
    Helm of Radiance, Stone of Binding, Shield of the Phoenix, Soul Gem, Titan''s
    Bane, Obsidian Shard, Silverbranch Bow, The Crusher, Pharaoh''s Curse, Magi''s
    Cloak, Toxic Blade, Nimble Ring, The Reaper, Shogun''s Ofuda, Screeching Gargoyle,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.12
      fit: 0.22
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.45
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.27
      fit: 0.42
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.71
      pick: 0.15
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Berserker''s Shield, Genji''s Guard, Kinetic Cuirass, Gluttonous
    Grimoire, Shield Splitter, Breastplate of Valor, Spear of Desolation, Spear of
    the Magus, Helm of Radiance, Soul Gem, Obsidian Shard, Runeforged Hammer, Eye
    of the Storm, Golden Blade, Hydra''s Lament, Rod of Asclepius, Heartseeker, Nimble
    Ring, Erosion, Draconic Scale, Eye of Providence, Stone of Binding, Shield of
    the Phoenix, Jade Scepter, Doom Orb, Death Metal, Wish-Granting Pearl, Avenging
    Blade, Tyrfing, Magi''s Cloak, Chronos'' Pendant, The World Stone, Bragi''s Harp,
    Titan''s Bane, Helm of Darkness, Ancient Signet, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.12
      fit: 0.22
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.39
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.27
      fit: 0.4
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.71
      pick: 0.15
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
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
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion,
    Leviathan''s Hide, Void Shield, Helm of Darkness, Ancile, Oni Hunter''s Garb,
    Xibalban Effigy, Hussar''s Wings, Void Stone, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.12
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.6
      pick: 0.27
      fit: 0.72
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.71
      pick: 0.15
      fit: 0.64
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
---
