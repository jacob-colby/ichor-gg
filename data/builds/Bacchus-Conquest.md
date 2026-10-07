---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.73
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.39
    win_rate: 0.69
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.17
      win_rate: 0.71
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.71
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.71
    - name: Breastplate of Valor
      pick_rate: 0.15
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.83
    alternates:
    - name: Genji's Guard
      pick_rate: 0.2
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.6
  - name: Shell of Rebuke
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 1.0
  - name: Contagion
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Regrowth Striders
      pick_rate: 0.06
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 1.0
  - name: Kinetic Cuirass
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Sage's Ring
      pick_rate: 0.08
      win_rate: 0.5
    - name: Mana Tome
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.2
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 1.0
  - name: Bluestone Brooch
    pick_rate: 0.1
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-10-07'
  god_win_rate: 0.7560975609756098
  god_matches_won: 31
  god_matches_played: 41
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Rod of Tahuti, Jotunn''s Revenge,
    Erosion, Eye of Providence, Draconic Scale, Berserker''s Shield, Shield Splitter,
    Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of the Storm, Helm
    of Radiance, Mantle Of Discord, Gluttonous Grimoire, Runeforged Hammer, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Prophetic Cloak, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy,
    Void Stone, Spectral Armor, Spear of Desolation, Hussar''s Wings, Gladiator''s
    Shield, Rod of Asclepius, Daybreak Gavel, Doublet of Binding, Hydra''s Lament,
    Soul Gem.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.19
      fit: 0.29
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.71
      pick: 0.23
      fit: 0.37
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.25
    Freya's Tears:
      total: 0.69
      efficiency: 0.61
      win: 0.83
      pick: 0.23
      fit: 0.62
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.68
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Contagion
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Contagion
  - Genji's Guard
  - Regrowth Striders
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Contagion
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Shield of the Phoenix, Rod of Tahuti,
    Rod of Asclepius, Jotunn''s Revenge, Soul Gem, Berserker''s Shield, Erosion, Eye
    of Providence, Draconic Scale, Ethereal Staff, Phoenix Feather, Gluttonous Grimoire,
    Yogi''s Necklace, Shield Splitter, Chandra''s Grace, Runeforged Hammer, Eye of
    the Storm, Glorious Pridwen, Midgardian Mail, Stone of Binding, Lifebinder, Hide
    of the Nemean Lion, Helm of Radiance, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile, Oni Hunter''s Garb, Daybreak Gavel, Screeching Gargoyle, Sphere
    of Negation, Void Stone, Mantle Of Discord, Spectral Armor, Gladiator''s Shield.'
  slot_scores:
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.19
      fit: 0.36
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.71
      pick: 0.23
      fit: 0.34
    Regrowth Striders:
      total: 0.67
      efficiency: 0.35
      win: 1.0
      pick: 0.13
      fit: 0.64
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.83
      pick: 0.23
      fit: 0.54
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.66
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Contagion
  - Genji's Guard
  - Regrowth Striders
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Stone of Binding
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Shifter''s Shield, Rod of Tahuti, Jotunn''s Revenge, Amanita Charm,
    Stone of Binding, Gluttonous Grimoire, Screeching Gargoyle, Spear of Desolation,
    Void Shield, Spear of the Magus, Soul Gem, Void Stone, Obsidian Shard, Avenging
    Blade, Berserker''s Shield, Heartseeker, Erosion, Shield Splitter, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance, Runeforged
    Hammer, The World Stone, Titan''s Bane, Magi''s Cloak, The Crusher, Dreamer''s
    Idol, Eye of the Storm, Mantle Of Discord, Midgardian Mail, The Reaper, Daybreak
    Gavel, Hide of the Nemean Lion, Rod of Asclepius, Leviathan''s Hide, Hydra''s
    Lament.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.19
      fit: 0.24
    Stone of Binding:
      total: 0.61
      efficiency: 0.51
      win: 0.71
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.83
      pick: 0.23
      fit: 0.43
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.48
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Contagion
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Golden Blade
  - Berserker's Shield
  - Nimble Ring
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Rod of Tahuti, Berserker''s Shield, Amanita Charm,
    Jotunn''s Revenge, Nimble Ring, Golden Blade, Gluttonous Grimoire, Tyrfing, Shield
    Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence,
    Stone of Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic
    Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The
    Reaper, Spear of Desolation, Spear of the Magus, Bragi''s Harp, Midgardian Mail,
    Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.19
      fit: 0.2
    Golden Blade:
      total: 0.58
      efficiency: 0.52
      win: 0.71
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.59
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.83
      pick: 0.23
      fit: 0.33
    Shifter's Shield:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.37
  community_ordered:
  - Contagion
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Genji's Guard
  - Jotunn's Revenge
  - Regrowth Striders
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Genji's Guard
  - Contagion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti,
    Jotunn''s Revenge, Amanita Charm, Shield of the Phoenix, Spear of Desolation,
    Hydra''s Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Shield Splitter,
    Berserker''s Shield, Prophetic Cloak, Erosion, Helm of Radiance, Runeforged Hammer,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone
    of Binding, Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius,
    Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel, Chandra''s Grace, Obsidian Shard, Hide of the Nemean Lion,
    Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.19
      fit: 0.23
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.71
      pick: 0.23
      fit: 0.48
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.46
    Regrowth Striders:
      total: 0.65
      efficiency: 0.35
      win: 1.0
      pick: 0.13
      fit: 0.48
    Freya's Tears:
      total: 0.7
      efficiency: 0.61
      win: 0.83
      pick: 0.23
      fit: 0.64
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.45
  community_ordered:
  - Contagion
  - Genji's Guard
  - Regrowth Striders
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Contagion
  - Berserker's Shield
  - Jotunn's Revenge
  - Regrowth Striders
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Regrowth Striders
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti, Jotunn''s
    Revenge, Berserker''s Shield, Amanita Charm, Shield Splitter, Runeforged Hammer,
    Golden Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker,
    Tyrfing, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence,
    Spear of the Magus, Avenging Blade, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Helm of Radiance, Titan''s Bane, Soul Gem, The Crusher, Obsidian Shard,
    Pharaoh''s Curse, Silverbranch Bow, Magi''s Cloak, The Reaper, Nimble Ring, Toxic
    Blade, Shogun''s Ofuda, Screeching Gargoyle, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.19
      fit: 0.22
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.45
    Regrowth Striders:
      total: 0.61
      efficiency: 0.35
      win: 1.0
      pick: 0.13
      fit: 0.23
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.83
      pick: 0.23
      fit: 0.38
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.42
  community_ordered:
  - Contagion
  - Regrowth Striders
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Contagion
  - Genji's Guard
  - Jotunn's Revenge
  - Regrowth Striders
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Regrowth Striders
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti,
    Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Shield Splitter, Spear
    of Desolation, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem,
    Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of
    Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix, Stone
    of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting
    Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant, The World Stone, Helm
    of Darkness, Titan''s Bane, The Crusher, Ancient Signet, Screeching Gargoyle,
    Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.19
      fit: 0.22
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.71
      pick: 0.23
      fit: 0.23
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.41
    Regrowth Striders:
      total: 0.61
      efficiency: 0.35
      win: 1.0
      pick: 0.13
      fit: 0.23
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.83
      pick: 0.23
      fit: 0.38
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.42
  community_ordered:
  - Contagion
  - Genji's Guard
  - Regrowth Striders
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Shifter''s Shield, Jotunn''s
    Revenge, Erosion, Eye of Providence, Draconic Scale, Berserker''s Shield, Shield
    Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of the Storm,
    Helm of Radiance, Mantle Of Discord, Gluttonous Grimoire, Runeforged Hammer, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Prophetic Cloak, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy,
    Void Stone, Spectral Armor, Spear of Desolation, Hussar''s Wings, Gladiator''s
    Shield, Rod of Asclepius, Daybreak Gavel, Doublet of Binding, Hydra''s Lament,
    Soul Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.71
      pick: 0.23
      fit: 0.37
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.25
      fit: 0.78
    Freya's Tears:
      total: 0.69
      efficiency: 0.61
      win: 0.83
      pick: 0.23
      fit: 0.62
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.68
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
