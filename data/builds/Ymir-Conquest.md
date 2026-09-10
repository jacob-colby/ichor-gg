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
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Circe's Hexstone
      pick_rate: 0.14
      win_rate: 0.8
    - name: Golden Blade
      pick_rate: 0.08
      win_rate: 0.67
  - name: Stampede
    pick_rate: 0.19
    win_rate: 0.29
    alternates:
    - name: Erosion
      pick_rate: 0.16
      win_rate: 0.83
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 1.0
  - name: Stygian Anchor
    pick_rate: 0.19
    win_rate: 0.86
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.4
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.75
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.25
    - name: Spectral Armor
      pick_rate: 0.08
      win_rate: 0.67
  - name: Spirit Robe
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.67
    - name: Hide of the Nemean Lion
      pick_rate: 0.1
      win_rate: 0.33
  - name: Draconic Scale
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Mana Tome
      pick_rate: 0.06
      win_rate: 0.0
    - name: Medal of Disruption
      pick_rate: 0.06
      win_rate: 0.0
  community_starters:
  - name: Heroism
    pick_rate: 0.14
    win_rate: 0.4
  - name: War Banner
    pick_rate: 0.14
    win_rate: 0.8
  - name: War Flag
    pick_rate: 0.14
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-09-10'
  god_win_rate: 0.5405405405405406
  god_matches_won: 20
  god_matches_played: 37
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Spectral Armor, Kinetic Cuirass, Shifter''s Shield, Rod
    of Tahuti, Breastplate of Valor, Eye of Providence, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Mantle Of Discord, Midgardian Mail,
    Screeching Gargoyle, Prophetic Cloak, Leviathan''s Hide, Void Shield, Helm of
    Darkness, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Hussar''s Wings, Void Stone.'
  slot_scores:
    Stygian Anchor:
      total: 0.64
      efficiency: 0.45
      win: 0.86
      pick: 0.3
      fit: 0.51
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.75
      pick: 0.37
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.82
    Spectral Armor:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.46
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.67
      efficiency: 0.51
      win: 0.83
      pick: 0.22
      fit: 0.72
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  - Spectral Armor
  - Erosion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Spirit Robe
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spirit Robe
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Shifter''s Shield,
    Rod of Asclepius, Rod of Tahuti, Eye of Providence, Breastplate of Valor, Ethereal
    Staff, Phoenix Feather, Yogi''s Necklace, Chandra''s Grace, Glorious Pridwen,
    Soul Gem, Lifebinder, Midgardian Mail, Stone of Binding, Helm of Radiance, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Stygian Anchor:
      total: 0.62
      efficiency: 0.45
      win: 0.86
      pick: 0.3
      fit: 0.43
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.75
      pick: 0.37
      fit: 0.35
    Spirit Robe:
      total: 0.58
      efficiency: 0.34
      win: 0.75
      pick: 0.28
      fit: 0.73
    Spectral Armor:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.49
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.67
      efficiency: 0.51
      win: 0.83
      pick: 0.22
      fit: 0.7
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  - Spirit Robe
  - Spectral Armor
  - Erosion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Stygian Anchor
  - Genji's Guard
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Spear of the Magus,
    Void Shield, Soul Gem, Breastplate of Valor, Obsidian Shard, Void Stone, Shifter''s
    Shield, Eye of Providence, Doom Orb, Shield of the Phoenix, Helm of Radiance,
    The World Stone, Magi''s Cloak, Dreamer''s Idol, Mantle Of Discord, Midgardian
    Mail, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.74
    Stygian Anchor:
      total: 0.61
      efficiency: 0.45
      win: 0.86
      pick: 0.3
      fit: 0.34
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.75
      pick: 0.37
      fit: 0.25
    Spectral Armor:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.31
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Erosion:
      total: 0.64
      efficiency: 0.51
      win: 0.83
      pick: 0.22
      fit: 0.48
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  - Spectral Armor
  - Erosion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Erosion
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Breastplate
    of Valor, Shifter''s Shield, Helm of Radiance, Eye of Providence, Stone of Binding,
    Shield of the Phoenix, Magi''s Cloak, Soul Gem, Bragi''s Harp, Screeching Gargoyle,
    Daybreak Gavel, Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Gluttonous
    Grimoire, Bracer of The Abyss, Leviathan''s Hide, Void Shield, Ancile.'
  slot_scores:
    Stygian Anchor:
      total: 0.6
      efficiency: 0.45
      win: 0.86
      pick: 0.3
      fit: 0.27
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.75
      pick: 0.37
      fit: 0.2
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.45
    Erosion:
      total: 0.62
      efficiency: 0.51
      win: 0.83
      pick: 0.22
      fit: 0.38
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  - Erosion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Breastplate of Valor
  - Circe's Hexstone
  - Spectral Armor
  - Erosion
  flex_slots:
  - Spectral Armor
  - Circe's Hexstone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Rod of Tahuti, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Shifter''s
    Shield, Chronos'' Pendant, Prophetic Cloak, Helm of Radiance, Eye of Providence,
    Gladiator''s Shield, Soul Gem, Stone of Binding, Gem of Focus, Magi''s Cloak,
    Spear of Desolation, Rod of Asclepius, Eye of Erebus, Nimble Ring, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace.'
  slot_scores:
    Stygian Anchor:
      total: 0.61
      efficiency: 0.45
      win: 0.86
      pick: 0.3
      fit: 0.32
    Genji's Guard:
      total: 0.66
      efficiency: 0.66
      win: 0.75
      pick: 0.37
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Circe's Hexstone:
      total: 0.51
      efficiency: 0.23
      win: 0.8
      pick: 0.14
      fit: 0.45
    Spectral Armor:
      total: 0.52
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.29
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.83
      pick: 0.22
      fit: 0.45
  community_ordered:
  - Stygian Anchor
  - Genji's Guard
  - Circe's Hexstone
  - Spectral Armor
  - Erosion
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Golden Blade
  - Stygian Anchor
  - Genji's Guard
  - Jotunn's Revenge
  - Spectral Armor
  - Erosion
  flex_slots:
  - Jotunn's Revenge
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
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
    win/pick). Underrated for this god: Golden Blade, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Breastplate of Valor, Shifter''s Shield, Eye of the Storm, Gluttonous
    Grimoire, Hydra''s Lament, Heartseeker, Tyrfing, Lernaean Bow, Spear of Desolation,
    Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging Blade, Helm of Radiance,
    Stone of Binding, Shield of the Phoenix, Soul Gem, Titan''s Bane, Obsidian Shard,
    Silverbranch Bow, The Crusher, Pharaoh''s Curse, Magi''s Cloak, Toxic Blade, Nimble
    Ring, The Reaper, Shogun''s Ofuda, Screeching Gargoyle, Mantle Of Discord, Midgardian
    Mail.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.08
      fit: 0.53
    Stygian Anchor:
      total: 0.6
      efficiency: 0.45
      win: 0.86
      pick: 0.3
      fit: 0.3
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.75
      pick: 0.37
      fit: 0.22
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spectral Armor:
      total: 0.52
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.27
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.83
      pick: 0.22
      fit: 0.42
  community_ordered:
  - Golden Blade
  - Stygian Anchor
  - Genji's Guard
  - Spectral Armor
  - Erosion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Golden Blade
  - Stygian Anchor
  - Genji's Guard
  - Jotunn's Revenge
  - Spectral Armor
  - Erosion
  flex_slots:
  - Jotunn's Revenge
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Circe's Hexstone — CC-immunity / cleanse
    swap_item: Circe's Hexstone
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Golden Blade, Jotunn''s
    Revenge, Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Gluttonous Grimoire,
    Shield Splitter, Breastplate of Valor, Spear of Desolation, Spear of the Magus,
    Runeforged Hammer, Helm of Radiance, Soul Gem, Shifter''s Shield, Obsidian Shard,
    Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Nimble Ring,
    Eye of Providence, Stone of Binding, Shield of the Phoenix, Jade Scepter, Doom
    Orb, Death Metal, Wish-Granting Pearl, Avenging Blade, Tyrfing, Magi''s Cloak,
    Chronos'' Pendant, The World Stone, Bragi''s Harp, Titan''s Bane, Helm of Darkness,
    Ancient Signet, Lernaean Bow.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.67
      pick: 0.08
      fit: 0.42
    Stygian Anchor:
      total: 0.6
      efficiency: 0.45
      win: 0.86
      pick: 0.3
      fit: 0.29
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.75
      pick: 0.37
      fit: 0.22
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Spectral Armor:
      total: 0.52
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.26
    Erosion:
      total: 0.62
      efficiency: 0.51
      win: 0.83
      pick: 0.22
      fit: 0.4
  community_ordered:
  - Golden Blade
  - Stygian Anchor
  - Genji's Guard
  - Spectral Armor
  - Erosion
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Rod
    of Tahuti, Breastplate of Valor, Eye of Providence, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Mantle Of Discord, Midgardian Mail,
    Screeching Gargoyle, Prophetic Cloak, Leviathan''s Hide, Void Shield, Helm of
    Darkness, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Hussar''s Wings, Void Stone,
    Spectral Armor.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.82
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.75
      pick: 0.37
      fit: 0.39
    Freya's Tears:
      total: 0.43
      efficiency: 0.61
      win: 0.25
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.72
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.67
      efficiency: 0.51
      win: 0.83
      pick: 0.22
      fit: 0.72
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Erosion
  starter: *id001
---
