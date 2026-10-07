---
type: smite-build
god: Amaterasu
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Golden Blade
    pick_rate: 0.43
    win_rate: 0.75
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.29
      win_rate: 0.75
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 1.0
  - name: Berserker's Shield
    pick_rate: 0.54
    win_rate: 0.73
    alternates:
    - name: Golden Blade
      pick_rate: 0.11
      win_rate: 1.0
    - name: The World Stone
      pick_rate: 0.07
      win_rate: 1.0
  - name: Kinetic Cuirass
    pick_rate: 0.25
    win_rate: 0.86
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.18
      win_rate: 0.6
    - name: Shogun's Ofuda
      pick_rate: 0.11
      win_rate: 1.0
  - name: Hussar's Wings
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.6
    - name: Kinetic Cuirass
      pick_rate: 0.15
      win_rate: 0.75
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.75
    alternates:
    - name: Contagion
      pick_rate: 0.13
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 1.0
  - name: Medal of Disruption
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.14
      win_rate: 0.5
    - name: Medallion
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.32
    win_rate: 0.89
  - name: Death's Toll
    pick_rate: 0.32
    win_rate: 0.67
  - name: Hunter's Cowl
    pick_rate: 0.14
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/amaterasu/
  last_verified: '2026-10-07'
  god_win_rate: 0.7857142857142857
  god_matches_won: 22
  god_matches_played: 28
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
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - The World Stone
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Shield Splitter, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye
    of the Storm, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Hydra''s Lament, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Avenging Blade, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail,
    Spear of Desolation, Leviathan''s Hide, Void Shield, Stampede, Prophetic Cloak,
    Ancile, Heartseeker, Oni Hunter''s Garb, Daybreak Gavel, Rod of Asclepius, Soul
    Gem, Void Stone, Xibalban Effigy, Spectral Armor, Helm of Darkness, Spear of the
    Magus.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.7
      efficiency: 0.56
      win: 0.86
      pick: 0.39
      fit: 0.67
    Shifter's Shield:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.14
      fit: 0.57
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.37
      fit: 0.53
    The World Stone:
      total: 0.65
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.1
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.57
    Shogun's Ofuda:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.17
      fit: 0.36
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - The World Stone
  - Shogun's Ofuda
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shifter's Shield
  - Kinetic Cuirass
  - The World Stone
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - The World Stone
  - Jotunn's Revenge
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
    this god: Shifter''s Shield, Amanita Charm, Rod of Tahuti, Jotunn''s Revenge,
    Shield of the Phoenix, Rod of Asclepius, Runeforged Hammer, Soul Gem, Shield Splitter,
    Genji''s Guard, Breastplate of Valor, Eye of the Storm, Ethereal Staff, Erosion,
    Eye of Providence, The Reaper, Yogi''s Necklace, Draconic Scale, Hydra''s Lament,
    Phoenix Feather, Gluttonous Grimoire, Chandra''s Grace, Avenging Blade, Glorious
    Pridwen, Lifebinder, Stone of Binding, Midgardian Mail, Helm of Radiance, Daybreak
    Gavel, Screeching Gargoyle, Sphere of Negation, Magi''s Cloak, Leviathan''s Hide,
    Spear of Desolation, Void Shield, Stampede, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.39
    Shifter's Shield:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.14
      fit: 0.55
    Kinetic Cuirass:
      total: 0.7
      efficiency: 0.56
      win: 0.86
      pick: 0.39
      fit: 0.65
    The World Stone:
      total: 0.65
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.11
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.85
    Shogun's Ofuda:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.17
      fit: 0.38
  community_ordered:
  - Shifter's Shield
  - Kinetic Cuirass
  - The World Stone
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Shifter's Shield
  - Kinetic Cuirass
  - The World Stone
  - Rod of Tahuti
  - Shogun's Ofuda
  flex_slots:
  - Jotunn's Revenge
  - Shogun's Ofuda
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Shifter''s Shield, Rod of Tahuti, The World Stone, Jotunn''s Revenge,
    Amanita Charm, Stone of Binding, Gluttonous Grimoire, Screeching Gargoyle, Avenging
    Blade, Genji''s Guard, Spear of Desolation, Void Shield, Breastplate of Valor,
    Spear of the Magus, Heartseeker, Soul Gem, Shield Splitter, Void Stone, Obsidian
    Shard, Runeforged Hammer, Titan''s Bane, The Crusher, Eye of the Storm, Erosion,
    Hydra''s Lament, The Reaper, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Helm of Radiance, Doom Orb, Magi''s Cloak, Pendulum Blade, Dreamer''s Idol,
    Mantle Of Discord, Avatar''s Parashu, Midgardian Mail, Daybreak Gavel, Rod of
    Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.14
      fit: 0.42
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.56
      win: 0.86
      pick: 0.39
      fit: 0.52
    The World Stone:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.34
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.75
      pick: 0.0
      fit: 0.34
    Shogun's Ofuda:
      total: 0.65
      efficiency: 0.44
      win: 1.0
      pick: 0.17
      fit: 0.27
  community_ordered:
  - Shifter's Shield
  - Kinetic Cuirass
  - The World Stone
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - The World Stone
  - Shogun's Ofuda
  flex_slots:
  - The World Stone
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Genji''s Guard, Gluttonous Grimoire, Breastplate of Valor, Tyrfing,
    Shield Splitter, Soul Gem, Runeforged Hammer, Pharaoh''s Curse, Riptalon, Lernaean
    Bow, Silverbranch Bow, Erosion, Helm of Radiance, Hydra''s Lament, Shield of the
    Phoenix, Stone of Binding, Eye of Providence, Eye of the Storm, Toxic Blade, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of Desolation,
    The Reaper, Spear of the Magus, Bragi''s Harp, Midgardian Mail, Mantle Of Discord,
    Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.62
      efficiency: 0.52
      win: 0.75
      pick: 0.43
      fit: 0.53
    Berserker's Shield:
      total: 0.67
      efficiency: 0.68
      win: 0.73
      pick: 0.74
      fit: 0.43
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.56
      win: 0.86
      pick: 0.39
      fit: 0.46
    Shifter's Shield:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.14
      fit: 0.36
    The World Stone:
      total: 0.65
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.07
    Shogun's Ofuda:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.17
      fit: 0.43
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - The World Stone
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - The World Stone
  flex_slots:
  - The World Stone
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti,
    Jotunn''s Revenge, Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield
    of the Phoenix, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul
    Gem, Chronos'' Pendant, Shield Splitter, Prophetic Cloak, Erosion, Helm of Radiance,
    Runeforged Hammer, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Eye of the Storm, Arondight, Gem of Focus, Magi''s
    Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Obsidian
    Shard, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.75
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.69
      efficiency: 0.56
      win: 0.86
      pick: 0.39
      fit: 0.55
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.75
      pick: 0.37
      fit: 0.64
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.14
      fit: 0.45
    The World Stone:
      total: 0.66
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.13
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - The World Stone
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Shifter's Shield
  - Kinetic Cuirass
  - The World Stone
  - Rod of Tahuti
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti, The World
    Stone, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Spear of Desolation,
    Genji''s Guard, Breastplate of Valor, Soul Gem, Spear of the Magus, Helm of Radiance,
    Obsidian Shard, Shield Splitter, Runeforged Hammer, Rod of Asclepius, Hydra''s
    Lament, Shield of the Phoenix, Chronos'' Pendant, Eye of the Storm, Erosion, Jade
    Scepter, Doom Orb, Heartseeker, Eye of Providence, Wish-Granting Pearl, Stone
    of Binding, Draconic Scale, Ancient Signet, Death Metal, Helm of Darkness, Screeching
    Gargoyle, Dreamer''s Idol, Magi''s Cloak, Avenging Blade, Ethereal Staff, Triton''s
    Conch, Daybreak Gavel, Mantle Of Discord.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.4
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.56
      win: 0.86
      pick: 0.39
      fit: 0.49
    The World Stone:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.35
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.75
      pick: 0.0
      fit: 0.35
    Shogun's Ofuda:
      total: 0.65
      efficiency: 0.44
      win: 1.0
      pick: 0.17
      fit: 0.25
  community_ordered:
  - Shifter's Shield
  - Kinetic Cuirass
  - The World Stone
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Shifter's Shield
  - Kinetic Cuirass
  - The World Stone
  - Rod of Tahuti
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Jotunn's Revenge
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti,
    The World Stone, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Genji''s
    Guard, Breastplate of Valor, Spear of Desolation, Shield Splitter, Spear of the
    Magus, Soul Gem, Runeforged Hammer, Helm of Radiance, Obsidian Shard, Eye of the
    Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence,
    Shield of the Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter,
    Death Metal, Wish-Granting Pearl, Avenging Blade, Chronos'' Pendant, Magi''s Cloak,
    Helm of Darkness, Titan''s Bane, Screeching Gargoyle, Ancient Signet, The Crusher,
    Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.41
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.14
      fit: 0.41
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.56
      win: 0.86
      pick: 0.39
      fit: 0.51
    The World Stone:
      total: 0.68
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.32
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.75
      pick: 0.0
      fit: 0.32
    Shogun's Ofuda:
      total: 0.65
      efficiency: 0.44
      win: 1.0
      pick: 0.17
      fit: 0.26
  community_ordered:
  - Shifter's Shield
  - Kinetic Cuirass
  - The World Stone
  - Shogun's Ofuda
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Shield
    Splitter, Genji''s Guard, Shifter''s Shield, Breastplate of Valor, Runeforged
    Hammer, Eye of the Storm, Erosion, Eye of Providence, Draconic Scale, Shield of
    the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s Cloak, Helm of Radiance,
    Gluttonous Grimoire, Avenging Blade, Mantle Of Discord, Screeching Gargoyle, Midgardian
    Mail, Spear of Desolation, Leviathan''s Hide, Void Shield, Stampede, Prophetic
    Cloak, Ancile, Heartseeker, Oni Hunter''s Garb, Daybreak Gavel, Rod of Asclepius,
    Soul Gem, Void Stone, Xibalban Effigy, Spectral Armor, Helm of Darkness, Spear
    of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.75
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.7
      efficiency: 0.56
      win: 0.86
      pick: 0.39
      fit: 0.67
    Shield Splitter:
      total: 0.62
      efficiency: 0.55
      win: 0.75
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.37
      fit: 0.53
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
