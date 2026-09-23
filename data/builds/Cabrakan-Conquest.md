---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.67
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.19
    win_rate: 0.75
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.19
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.67
  - name: Stone of Binding
    pick_rate: 0.19
    win_rate: 1.0
    alternates:
    - name: Polynomicon
      pick_rate: 0.14
      win_rate: 0.33
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.75
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.14
      win_rate: 1.0
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.15
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.5
    - name: Spirit Robe
      pick_rate: 0.1
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.25
    win_rate: 0.75
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 1.0
    - name: Leviathan's Hide
      pick_rate: 0.06
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.22
    win_rate: 1.0
    alternates:
    - name: Spirit Robe
      pick_rate: 0.22
      win_rate: 1.0
    - name: Sage's Ring
      pick_rate: 0.11
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.24
    win_rate: 0.2
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 1.0
  - name: Bumba's Cudgel
    pick_rate: 0.14
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-09-23'
  god_win_rate: 0.5714285714285714
  god_matches_won: 12
  god_matches_played: 21
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Kinetic Cuirass
  - Leviathan's Hide
  - Spirit Robe
  - Shell of Rebuke
  flex_slots:
  - Spirit Robe
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Leviathan''s Hide, Amanita Charm, Rod of Tahuti, Jotunn''s Revenge,
    Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Shifter''s Shield, Magi''s
    Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Void Shield, Stampede, Ancile, Heartseeker,
    Oni Hunter''s Garb, Spear of Desolation, Prophetic Cloak, Daybreak Gavel, Rod
    of Asclepius, Void Stone, Xibalban Effigy, Spectral Armor, Helm of Darkness, Soul
    Gem, Spear of the Magus, Genji''s Guard.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.67
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.41
    Stone of Binding:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.26
      fit: 0.51
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.67
    Leviathan's Hide:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.13
      fit: 0.37
    Spirit Robe:
      total: 0.66
      efficiency: 0.34
      win: 1.0
      pick: 0.68
      fit: 0.41
    Shell of Rebuke:
      total: 0.64
      efficiency: 0.28
      win: 1.0
      pick: 0.68
      fit: 0.41
  community_ordered:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Kinetic Cuirass
  - Leviathan's Hide
  - Spirit Robe
  - Shell of Rebuke
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Kinetic Cuirass
  - Leviathan's Hide
  - Spirit Robe
  - Amanita Charm
  flex_slots:
  - Leviathan's Hide
  - Brawler’s Beat Stick
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Leviathan''s Hide, Rod of Tahuti, Jotunn''s Revenge,
    Shield of the Phoenix, Rod of Asclepius, Shield Splitter, Soul Gem, Eye of the
    Storm, Berserker''s Shield, Erosion, Ethereal Staff, Eye of Providence, The Reaper,
    Draconic Scale, Yogi''s Necklace, Hydra''s Lament, Phoenix Feather, Gluttonous
    Grimoire, Avenging Blade, Chandra''s Grace, Shifter''s Shield, Glorious Pridwen,
    Lifebinder, Midgardian Mail, Helm of Radiance, Daybreak Gavel, Magi''s Cloak,
    Void Shield, Sphere of Negation, Stampede, Ancile, Screeching Gargoyle, Heartseeker,
    Oni Hunter''s Garb, Genji''s Guard.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.66
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.34
    Stone of Binding:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.26
      fit: 0.44
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.66
    Leviathan's Hide:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.13
      fit: 0.38
    Spirit Robe:
      total: 0.7
      efficiency: 0.34
      win: 1.0
      pick: 0.68
      fit: 0.64
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Kinetic Cuirass
  - Leviathan's Hide
  - Spirit Robe
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Leviathan's Hide
  - Spirit Robe
  flex_slots:
  - Brawler’s Beat Stick
  - Spirit Robe
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Avenging Blade, Screeching Gargoyle, Void Shield, Spear of Desolation, Heartseeker,
    Spear of the Magus, Shield Splitter, Void Stone, Soul Gem, Obsidian Shard, Berserker''s
    Shield, Titan''s Bane, The Crusher, Eye of the Storm, Erosion, The Reaper, Hydra''s
    Lament, Eye of Providence, Shield of the Phoenix, Draconic Scale, Helm of Radiance,
    Doom Orb, The World Stone, Magi''s Cloak, Pendulum Blade, Dreamer''s Idol, Shifter''s
    Shield, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail, Daybreak Gavel,
    Rod of Asclepius, Genji''s Guard.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.3
    Stone of Binding:
      total: 0.75
      efficiency: 0.51
      win: 1.0
      pick: 0.26
      fit: 0.7
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.52
    Leviathan's Hide:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.13
      fit: 0.27
    Spirit Robe:
      total: 0.65
      efficiency: 0.34
      win: 1.0
      pick: 0.68
      fit: 0.3
  community_ordered:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Kinetic Cuirass
  - Leviathan's Hide
  - Spirit Robe
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Stone of Binding
  - Berserker's Shield
  - Kinetic Cuirass
  - Leviathan's Hide
  - Nimble Ring
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Golden Blade, Gluttonous Grimoire, Tyrfing, Shield Splitter, Pharaoh''s
    Curse, Soul Gem, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion,
    Helm of Radiance, Eye of Providence, Eye of the Storm, Shield of the Phoenix,
    Hydra''s Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, The Reaper, Midgardian Mail, Mantle Of Discord, Spear of Desolation,
    Bragi''s Harp, Spear of the Magus, Tekko-Kagi, Rod of Asclepius, Avenging Blade,
    Shifter''s Shield, Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.52
      win: 0.75
      pick: 0.0
      fit: 0.54
    Stone of Binding:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.26
      fit: 0.36
    Berserker's Shield:
      total: 0.64
      efficiency: 0.68
      win: 0.75
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.47
    Leviathan's Hide:
      total: 0.67
      efficiency: 0.51
      win: 1.0
      pick: 0.13
      fit: 0.24
    Nimble Ring:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.3
  community_ordered:
  - Stone of Binding
  - Kinetic Cuirass
  - Leviathan's Hide
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Leviathan's Hide
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Leviathan''s Hide, Rod of Tahuti,
    Jotunn''s Revenge, Amanita Charm, Shield of the Phoenix, Spear of Desolation,
    Hydra''s Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Shield Splitter,
    Berserker''s Shield, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous Grimoire,
    Eye of Providence, Gladiator''s Shield, Draconic Scale, Eye of the Storm, Arondight,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Shifter''s Shield, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak
    Gavel, Chandra''s Grace, Obsidian Shard, Jade Scepter, Void Shield, Genji''s Guard.'
  slot_scores:
    Stone of Binding:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.26
      fit: 0.42
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.55
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.53
      win: 0.75
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.75
      pick: 0.3
      fit: 0.64
    Leviathan's Hide:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.13
      fit: 0.29
  community_ordered:
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Leviathan's Hide
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Leviathan's Hide
  - Spirit Robe
  flex_slots:
  - Brawler’s Beat Stick
  - Spirit Robe
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Shield Splitter, Golden Blade, Eye of the Storm, Gluttonous
    Grimoire, Hydra''s Lament, Heartseeker, Lernaean Bow, Erosion, Spear of Desolation,
    Tekko-Kagi, Eye of Providence, Tyrfing, Avenging Blade, Spear of the Magus, Shield
    of the Phoenix, Draconic Scale, Helm of Radiance, Titan''s Bane, Soul Gem, The
    Crusher, Obsidian Shard, Pharaoh''s Curse, Magi''s Cloak, The Reaper, Silverbranch
    Bow, Nimble Ring, Shogun''s Ofuda, Screeching Gargoyle, Shifter''s Shield, Mantle
    Of Discord, Midgardian Mail, Daybreak Gavel, Genji''s Guard.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.3
    Stone of Binding:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.26
      fit: 0.4
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.52
    Leviathan's Hide:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.13
      fit: 0.27
    Spirit Robe:
      total: 0.65
      efficiency: 0.34
      win: 1.0
      pick: 0.68
      fit: 0.3
  community_ordered:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Kinetic Cuirass
  - Leviathan's Hide
  - Spirit Robe
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Leviathan's Hide
  - Spirit Robe
  flex_slots:
  - Jotunn's Revenge
  - Spirit Robe
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Shield Splitter, Spear of Desolation, Spear
    of the Magus, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield,
    Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion, Eye
    of Providence, Shield of the Phoenix, Draconic Scale, Doom Orb, Jade Scepter,
    Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Shifter''s Shield, Mantle Of Discord, Dreamer''s Idol, Midgardian
    Mail, Genji''s Guard.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.22
      fit: 0.3
    Stone of Binding:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.26
      fit: 0.4
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.52
    Leviathan's Hide:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.13
      fit: 0.27
    Spirit Robe:
      total: 0.65
      efficiency: 0.34
      win: 1.0
      pick: 0.68
      fit: 0.3
  community_ordered:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Kinetic Cuirass
  - Leviathan's Hide
  - Spirit Robe
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield
    Splitter, Shifter''s Shield, Genji''s Guard, Eye of the Storm, Berserker''s Shield,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament,
    Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade, Mantle Of
    Discord, Midgardian Mail, Screeching Gargoyle, Leviathan''s Hide, Void Shield,
    Stampede, Ancile, Heartseeker, Oni Hunter''s Garb, Spear of Desolation, Prophetic
    Cloak, Daybreak Gavel, Rod of Asclepius, Void Stone, Xibalban Effigy, Spectral
    Armor, Helm of Darkness, Soul Gem, Spear of the Magus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.76
      efficiency: 0.56
      win: 1.0
      pick: 0.25
      fit: 0.67
    Shield Splitter:
      total: 0.62
      efficiency: 0.55
      win: 0.75
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.75
      pick: 0.3
      fit: 0.52
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.14
      fit: 0.57
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
