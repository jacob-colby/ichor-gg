---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.6
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.22
    win_rate: 0.59
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.62
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.64
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.14
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.7
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.72
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.76
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.68
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.87
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.65
  - name: Olmec Blue
    pick_rate: 0.06
    win_rate: 0.83
    alternates:
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.5
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.8
  community_starters:
  - name: Selflessness
    pick_rate: 0.29
    win_rate: 0.55
  - name: Bumba's Hammer
    pick_rate: 0.23
    win_rate: 0.66
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.66
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-09-14'
  god_win_rate: 0.6086956521739131
  god_matches_won: 252
  god_matches_played: 414
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-14'
  god_matches_analyzed: 6946
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Draconic Scale, Shifter''s
    Shield, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Berserker''s
    Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian
    Mail, Runeforged Hammer, Screeching Gargoyle, Leviathan''s Hide, Void Shield,
    Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy, Void Stone, Spear
    of Desolation, Spectral Armor, Hussar''s Wings, Rod of Asclepius, Gladiator''s
    Shield, Daybreak Gavel, Soul Gem, Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.78
    Hide of the Nemean Lion:
      total: 0.61
      efficiency: 0.52
      win: 0.8
      pick: 0.15
      fit: 0.44
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.23
      fit: 0.62
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.64
      pick: 0.09
      fit: 0.68
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.68
      pick: 0.13
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Hide of the Nemean Lion
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Draconic Scale, Shifter''s Shield, Rod of Asclepius, Jotunn''s Revenge, Soul Gem,
    Breastplate of Valor, Berserker''s Shield, Erosion, Eye of Providence, Ethereal
    Staff, Phoenix Feather, Gluttonous Grimoire, Yogi''s Necklace, Shield Splitter,
    Chandra''s Grace, Runeforged Hammer, Glorious Pridwen, Eye of the Storm, Lifebinder,
    Midgardian Mail, Stone of Binding, Helm of Radiance, Leviathan''s Hide, Void Shield,
    Magi''s Cloak, Ancile, Oni Hunter''s Garb, Daybreak Gavel, Sphere of Negation,
    Screeching Gargoyle, Void Stone, Mantle Of Discord, Spectral Armor, Gladiator''s
    Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.9
    Hide of the Nemean Lion:
      total: 0.62
      efficiency: 0.52
      win: 0.8
      pick: 0.15
      fit: 0.46
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.62
      pick: 0.23
      fit: 0.54
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.68
      pick: 0.13
      fit: 0.66
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Draconic Scale, Shifter''s Shield, Screeching
    Gargoyle, Spear of Desolation, Void Shield, Spear of the Magus, Soul Gem, Breastplate
    of Valor, Void Stone, Obsidian Shard, Avenging Blade, Berserker''s Shield, Heartseeker,
    Erosion, Shield Splitter, Eye of Providence, Shield of the Phoenix, Doom Orb,
    Helm of Radiance, Runeforged Hammer, The World Stone, Titan''s Bane, Magi''s Cloak,
    The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of Discord, Midgardian
    Mail, The Reaper, Daybreak Gavel, Rod of Asclepius, Leviathan''s Hide, Hydra''s
    Lament.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.58
    Hide of the Nemean Lion:
      total: 0.59
      efficiency: 0.52
      win: 0.8
      pick: 0.15
      fit: 0.31
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.23
      fit: 0.43
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Draconic Scale, Golden Blade, Shifter''s Shield,
    Gluttonous Grimoire, Breastplate of Valor, Tyrfing, Shield Splitter, Soul Gem,
    Runeforged Hammer, Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda,
    Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence, Stone of Binding,
    Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic Blade, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Spear of Desolation, Spear
    of the Magus, Bragi''s Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod
    of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.2
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.3
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.52
      win: 0.8
      pick: 0.15
      fit: 0.24
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Draconic
    Scale, Shifter''s Shield, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle,
    Soul Gem, Chronos'' Pendant, Shield Splitter, Berserker''s Shield, Erosion, Helm
    of Radiance, Runeforged Hammer, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Stone of Binding, Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak,
    Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious
    Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Obsidian Shard, Leviathan''s
    Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.59
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.46
    Hide of the Nemean Lion:
      total: 0.59
      efficiency: 0.52
      win: 0.8
      pick: 0.15
      fit: 0.29
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.23
      fit: 0.64
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
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
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Draconic Scale, Shield Splitter, Shifter''s
    Shield, Runeforged Hammer, Breastplate of Valor, Golden Blade, Eye of the Storm,
    Gluttonous Grimoire, Hydra''s Lament, Heartseeker, Tyrfing, Lernaean Bow, Erosion,
    Spear of Desolation, Tekko-Kagi, Spear of the Magus, Eye of Providence, Avenging
    Blade, Shield of the Phoenix, Stone of Binding, Helm of Radiance, Soul Gem, Titan''s
    Bane, Silverbranch Bow, The Crusher, Obsidian Shard, Pharaoh''s Curse, Magi''s
    Cloak, Toxic Blade, The Reaper, Nimble Ring, Shogun''s Ofuda, Screeching Gargoyle,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.59
      efficiency: 0.52
      win: 0.8
      pick: 0.15
      fit: 0.27
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.23
      fit: 0.38
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Draconic Scale, Shifter''s
    Shield, Shield Splitter, Breastplate of Valor, Spear of Desolation, Spear of the
    Magus, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s
    Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion,
    Eye of Providence, Shield of the Phoenix, Stone of Binding, Doom Orb, Jade Scepter,
    Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.59
      efficiency: 0.52
      win: 0.8
      pick: 0.15
      fit: 0.27
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.23
      fit: 0.38
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.68
      pick: 0.13
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy,
    Void Stone, Spear of Desolation, Spectral Armor, Hussar''s Wings, Rod of Asclepius,
    Gladiator''s Shield, Daybreak Gavel, Soul Gem, Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.59
      pick: 0.2
      fit: 0.37
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.23
      fit: 0.62
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.64
      pick: 0.09
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
