---
type: smite-build
god: Geb
mode: Conquest
builds:
- source: community
  aspect: Aspect of Calamity
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.29
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.32
    win_rate: 0.59
    alternates:
    - name: Stampede
      pick_rate: 0.2
      win_rate: 0.49
    - name: Yogi's Necklace
      pick_rate: 0.09
      win_rate: 0.66
  - name: Genji's Guard
    pick_rate: 0.25
    win_rate: 0.54
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.61
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.44
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.44
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.17
      win_rate: 0.55
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.59
  - name: Spirit Robe
    pick_rate: 0.08
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.41
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.4
    alternates:
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.85
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.4
  community_starters:
  - name: Selflessness
    pick_rate: 0.39
    win_rate: 0.54
  - name: Heroism
    pick_rate: 0.28
    win_rate: 0.61
  - name: War Banner
    pick_rate: 0.08
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-08-21'
  god_win_rate: 0.525
  god_matches_won: 189
  god_matches_played: 360
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
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Erosion
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Shifter''s Shield, Shield
    of the Phoenix, Erosion, Eye of Providence, Mantle Of Discord, Stone of Binding,
    Draconic Scale, Spectral Armor, Magi''s Cloak, Leviathan''s Hide, Gluttonous Grimoire,
    Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion, Doublet of Binding,
    Prophetic Cloak, Helm of Radiance, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban
    Effigy, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.34
      fit: 0.36
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.59
      pick: 0.2
      fit: 0.6
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.68
    Erosion:
      total: 0.52
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.68
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
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Yogi''s Necklace,
    Rod of Tahuti, Shifter''s Shield, Ethereal Staff, Rod of Asclepius, Phoenix Feather,
    Erosion, Soul Gem, Eye of Providence, Chandra''s Grace, Draconic Scale, Spectral
    Armor, Mantle Of Discord, Stone of Binding, Gluttonous Grimoire, Leviathan''s
    Hide, Glorious Pridwen, Midgardian Mail, Hide of the Nemean Lion, Doublet of Binding,
    Void Shield, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.34
      fit: 0.33
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.88
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.2
      fit: 0.53
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: Rod of Tahuti, Stone of Binding, Amanita Charm, Kinetic Cuirass,
    Gluttonous Grimoire, Screeching Gargoyle, Soul Gem, Void Shield, Void Stone, Spear
    of Desolation, Shifter''s Shield, Spear of the Magus, Shield of the Phoenix, Obsidian
    Shard, Mantle Of Discord, Erosion, Eye of Providence, Spectral Armor, Draconic
    Scale, Leviathan''s Hide, Magi''s Cloak, Doom Orb, The Cosmic Horror, Helm of
    Radiance, The World Stone, Midgardian Mail.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.54
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.34
      fit: 0.24
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.2
      fit: 0.41
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.46
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
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Nimble Ring, Gluttonous
    Grimoire, Shifter''s Shield, Shield of the Phoenix, Mantle Of Discord, Stone of
    Binding, Spectral Armor, Erosion, Eye of Providence, Soul Gem, Draconic Scale,
    Leviathan''s Hide, Death Metal, Helm of Radiance, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, Midgardian Mail, Bragi''s Harp, Hide of the Nemean Lion, Doublet
    of Binding, Void Shield, Ethereal Staff.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.49
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.2
      fit: 0.35
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Screeching Gargoyle
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Soul Gem, Screeching Gargoyle, Spear of Desolation,
    Gluttonous Grimoire, Shifter''s Shield, Mantle Of Discord, Chronos'' Pendant,
    Stone of Binding, Helm of Radiance, Prophetic Cloak, Erosion, Nimble Ring, Spectral
    Armor, Death Metal, Eye of Providence, Draconic Scale, Gladiator''s Shield, Chandra''s
    Grace, Leviathan''s Hide, Gem of Focus, Ethereal Staff, Magi''s Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.5
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.34
      fit: 0.44
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.44
      pick: 0.18
      fit: 0.44
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.51
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.59
      pick: 0.2
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, The Crusher, Shield Splitter, Gluttonous
    Grimoire, Runeforged Hammer, Golden Blade, Shifter''s Shield, Eye of the Storm,
    Shield of the Phoenix, Mantle Of Discord, Hydra''s Lament, Stone of Binding, Heartseeker,
    Death Metal, Tyrfing, Soul Gem, The Reaper, Pharaoh''s Curse, Nimble Ring, Lernaean
    Bow, Spectral Armor, Erosion, Shogun''s Ofuda, Eye of Providence, Avenging Blade,
    Tekko-Kagi, Silverbranch Bow, Draconic Scale, Titan''s Bane, Spear of Desolation,
    Spear of the Magus, Leviathan''s Hide, Helm of Radiance, Riptalon, Toxic Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.34
      fit: 0.21
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.2
      fit: 0.35
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Berserker''s Shield, Soul
    Gem, Death Metal, The Crusher, Shield Splitter, Spear of the Magus, Spear of Desolation,
    Runeforged Hammer, Helm of Radiance, Nimble Ring, Obsidian Shard, Shifter''s Shield,
    Shield of the Phoenix, Mantle Of Discord, Stone of Binding, Eye of the Storm,
    Ethereal Staff, Hydra''s Lament, Rod of Asclepius, Golden Blade, Heartseeker,
    Spectral Armor, The Reaper, Erosion, Eye of Providence, Draconic Scale, Leviathan''s
    Hide, Jade Scepter, Doom Orb, Pharaoh''s Curse, The Cosmic Horror, Wish-Granting
    Pearl, Avenging Blade, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.34
      fit: 0.2
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.2
      fit: 0.33
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.37
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Shifter''s
    Shield, Shield of the Phoenix, Erosion, Eye of Providence, Mantle Of Discord,
    Stone of Binding, Draconic Scale, Spectral Armor, Magi''s Cloak, Leviathan''s
    Hide, Gluttonous Grimoire, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean
    Lion, Doublet of Binding, Prophetic Cloak, Helm of Radiance, Void Shield, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.34
      fit: 0.36
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.44
      pick: 0.18
      fit: 0.36
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.59
      pick: 0.2
      fit: 0.6
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.68
  starter: *id001
---
