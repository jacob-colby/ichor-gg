---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.0
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.24
    win_rate: 0.67
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.75
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.33
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.67
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.67
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 1.0
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.8
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.33
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.5
  - name: Stampede
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.0
    - name: Oni Hunter's Garb
      pick_rate: 0.1
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.18
    win_rate: 1.0
    alternates:
    - name: Sage's Ring
      pick_rate: 0.18
      win_rate: 0.67
    - name: Mote of Chaos
      pick_rate: 0.12
      win_rate: 0.5
  - name: Captain's Ring
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 1.0
    - name: Spectral Armor
      pick_rate: 0.13
      win_rate: 1.0
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.44
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.25
  - name: Bluestone Brooch
    pick_rate: 0.08
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-10-08'
  god_win_rate: 0.6
  god_matches_won: 15
  god_matches_played: 25
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Oni Hunter's Garb
  - Draconic Scale
  - Stampede
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Shifter''s Shield, Eye of the Storm, Berserker''s Shield,
    Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding, Hydra''s
    Lament, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion,
    Leviathan''s Hide, Void Shield, Ancile, Heartseeker, Spear of Desolation, Prophetic
    Cloak, Daybreak Gavel, Rod of Asclepius, Void Stone, Xibalban Effigy, Helm of
    Darkness, Soul Gem, Spear of the Magus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.8
      pick: 0.0
      fit: 0.37
    Oni Hunter's Garb:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.37
    Draconic Scale:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.57
    Stampede:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.37
    Spectral Armor:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.37
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.8
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Oni Hunter's Garb
  - Draconic Scale
  - Stampede
  - Spectral Armor
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Oni Hunter's Garb
  - Draconic Scale
  - Stampede
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Jotunn's Revenge
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Draconic Scale, Rod of Tahuti, Jotunn''s Revenge, Shield
    of the Phoenix, Kinetic Cuirass, Rod of Asclepius, Shield Splitter, Shifter''s
    Shield, Soul Gem, Eye of the Storm, Berserker''s Shield, Erosion, Ethereal Staff,
    Eye of Providence, The Reaper, Yogi''s Necklace, Hydra''s Lament, Phoenix Feather,
    Gluttonous Grimoire, Avenging Blade, Chandra''s Grace, Glorious Pridwen, Lifebinder,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Daybreak Gavel, Hide of the
    Nemean Lion, Magi''s Cloak, Leviathan''s Hide, Void Shield, Sphere of Negation,
    Ancile, Screeching Gargoyle, Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.8
      pick: 0.0
      fit: 0.39
    Oni Hunter's Garb:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.38
    Draconic Scale:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.56
    Stampede:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.38
    Spectral Armor:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.38
    Amanita Charm:
      total: 0.72
      efficiency: 0.65
      win: 0.8
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Oni Hunter's Garb
  - Draconic Scale
  - Stampede
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Oni Hunter's Garb
  - Draconic Scale
  - Stampede
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Draconic Scale, Jotunn''s Revenge, Amanita Charm,
    Stone of Binding, Kinetic Cuirass, Gluttonous Grimoire, Avenging Blade, Screeching
    Gargoyle, Void Shield, Spear of Desolation, Heartseeker, Spear of the Magus, Shield
    Splitter, Void Stone, Soul Gem, Obsidian Shard, Shifter''s Shield, Berserker''s
    Shield, Titan''s Bane, The Crusher, Eye of the Storm, Erosion, The Reaper, Hydra''s
    Lament, Eye of Providence, Shield of the Phoenix, Helm of Radiance, Doom Orb,
    The World Stone, Magi''s Cloak, Pendulum Blade, Dreamer''s Idol, Avatar''s Parashu,
    Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.8
      pick: 0.0
      fit: 0.54
    Oni Hunter's Garb:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.27
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.42
    Stampede:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.27
    Spectral Armor:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.27
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.8
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Oni Hunter's Garb
  - Draconic Scale
  - Stampede
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Nimble Ring
  - Draconic Scale
  - Stampede
  - Spectral Armor
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Tyrfing,
    Shifter''s Shield, Shield Splitter, Pharaoh''s Curse, Soul Gem, Riptalon, Lernaean
    Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence,
    Stone of Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic
    Blade, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Midgardian
    Mail, Mantle Of Discord, Spear of Desolation, Bragi''s Harp, Spear of the Magus,
    Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.62
      efficiency: 0.52
      win: 0.8
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.66
      efficiency: 0.68
      win: 0.8
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.63
      efficiency: 0.65
      win: 0.8
      pick: 0.0
      fit: 0.3
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.37
    Stampede:
      total: 0.67
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.24
    Spectral Armor:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.24
  community_ordered:
  - Draconic Scale
  - Stampede
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Shield of the Phoenix
  - Draconic Scale
  - Stampede
  - Spectral Armor
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Hydra''s Lament, Screeching Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant,
    Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Helm of Radiance,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Stone of Binding,
    Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye
    of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel, Chandra''s Grace, Obsidian Shard, Hide of the Nemean Lion,
    Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.8
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.68
      efficiency: 0.66
      win: 0.8
      pick: 0.34
      fit: 0.48
    Shield of the Phoenix:
      total: 0.64
      efficiency: 0.53
      win: 0.8
      pick: 0.0
      fit: 0.61
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.45
    Stampede:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.29
    Spectral Armor:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  - Stampede
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Oni Hunter's Garb
  - Draconic Scale
  - Stampede
  - Spectral Armor
  flex_slots:
  - Oni Hunter's Garb
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Shifter''s
    Shield, Golden Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament,
    Heartseeker, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence,
    Tyrfing, Avenging Blade, Spear of the Magus, Shield of the Phoenix, Stone of Binding,
    Helm of Radiance, Titan''s Bane, Soul Gem, The Crusher, Obsidian Shard, Pharaoh''s
    Curse, Magi''s Cloak, The Reaper, Silverbranch Bow, Nimble Ring, Shogun''s Ofuda,
    Screeching Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.65
      efficiency: 0.68
      win: 0.8
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.8
      pick: 0.0
      fit: 0.45
    Oni Hunter's Garb:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.27
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.42
    Stampede:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.27
    Spectral Armor:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.27
  community_ordered:
  - Oni Hunter's Garb
  - Draconic Scale
  - Stampede
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Oni Hunter's Garb
  - Draconic Scale
  - Stampede
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Draconic Scale, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter,
    Spear of Desolation, Spear of the Magus, Helm of Radiance, Soul Gem, Shifter''s
    Shield, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s Lament,
    Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix,
    Stone of Binding, Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging
    Blade, Magi''s Cloak, Chronos'' Pendant, The World Stone, Helm of Darkness, Titan''s
    Bane, The Crusher, Ancient Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s
    Idol, Midgardian Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.8
      pick: 0.0
      fit: 0.41
    Oni Hunter's Garb:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.27
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.11
      fit: 0.42
    Stampede:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.17
      fit: 0.27
    Spectral Armor:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.4
      fit: 0.27
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.8
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Oni Hunter's Garb
  - Draconic Scale
  - Stampede
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Shifter''s Shield, Eye of the Storm, Berserker''s Shield,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding,
    Hydra''s Lament, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean
    Lion, Leviathan''s Hide, Void Shield, Ancile, Heartseeker, Spear of Desolation,
    Prophetic Cloak, Daybreak Gavel, Rod of Asclepius, Void Stone, Xibalban Effigy,
    Helm of Darkness, Soul Gem, Spear of the Magus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.8
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.56
      win: 0.8
      pick: 0.0
      fit: 0.67
    Shield Splitter:
      total: 0.65
      efficiency: 0.55
      win: 0.8
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.16
      fit: 0.52
    Shifter's Shield:
      total: 0.64
      efficiency: 0.55
      win: 0.8
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.8
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Freya's Tears
  starter: *id001
---
