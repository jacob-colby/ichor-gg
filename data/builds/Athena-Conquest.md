---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.62
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.33
    win_rate: 0.57
    alternates:
    - name: Stampede
      pick_rate: 0.18
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.51
  - name: Stampede
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.64
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.48
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.51
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.6
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.55
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.04
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.58
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.55
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.76
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.29
    win_rate: 0.54
  - name: Bumba's Hammer
    pick_rate: 0.26
    win_rate: 0.68
  - name: Selflessness
    pick_rate: 0.19
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-11-02'
  god_win_rate: 0.5695431472081218
  god_matches_won: 561
  god_matches_played: 985
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Rod of Tahuti, Kinetic Cuirass, Berserker''s
    Shield, Shield Splitter, Erosion, Breastplate of Valor, Eye of Providence, Draconic
    Scale, Jotunn''s Revenge, Shield of the Phoenix, Oni Hunter''s Garb, Stone of
    Binding, Helm of Darkness, Magi''s Cloak, Midgardian Mail, Mantle Of Discord,
    Leviathan''s Hide, Gluttonous Grimoire, Screeching Gargoyle, Helm of Radiance,
    Prophetic Cloak, Shifter''s Shield, Ancile, Runeforged Hammer, Hide of the Nemean
    Lion, Void Stone, Spear of Desolation, Void Shield, Xibalban Effigy, Gladiator''s
    Shield, Hussar''s Wings, Obsidian Shard, Soul Gem, Spectral Armor, Brawler’s Beat
    Stick, Phoenix Feather, Hydra''s Lament, Doublet of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.44
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.09
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.51
      pick: 0.28
      fit: 0.62
    Shield Splitter:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  - Erosion
  flex_slots:
  - Berserker's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Genji''s Guard, Rod of Tahuti,
    Kinetic Cuirass, Berserker''s Shield, Soul Gem, Phoenix Feather, Erosion, Jotunn''s
    Revenge, Yogi''s Necklace, Eye of Providence, Draconic Scale, Breastplate of Valor,
    Chandra''s Grace, Ethereal Staff, Shield Splitter, Oni Hunter''s Garb, Gluttonous
    Grimoire, Glorious Pridwen, Midgardian Mail, Leviathan''s Hide, Runeforged Hammer,
    Regrowth Striders, Rod of Asclepius, Helm of Darkness, Stone of Binding, Ancile,
    Hide of the Nemean Lion, Sphere of Negation, Screeching Gargoyle, Magi''s Cloak,
    Void Stone, Void Shield, Spear of Desolation, Helm of Radiance, Shifter''s Shield,
    Mantle Of Discord, Gladiator''s Shield, Blood-Bound Book.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.09
      fit: 0.34
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.9
    Amanita Charm:
      total: 0.61
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.96
    Erosion:
      total: 0.52
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Genji''s Guard, Amanita Charm,
    Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Obsidian
    Shard, Berserker''s Shield, Spear of Desolation, Soul Gem, Void Stone, Void Shield,
    Breastplate of Valor, Titan''s Bane, Spear of the Magus, Shield Splitter, Avenging
    Blade, Erosion, Eye of Providence, Doom Orb, Draconic Scale, Oni Hunter''s Garb,
    The World Stone, Shield of the Phoenix, Heartseeker, The Crusher, Midgardian Mail,
    Helm of Darkness, Magi''s Cloak, Helm of Radiance, Mantle Of Discord, Toxic Blade,
    Leviathan''s Hide, Runeforged Hammer, The Reaper, Dreamer''s Idol, Ancile, Hydra''s
    Lament, Shifter''s Shield.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.53
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.09
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Genji''s Guard, Amanita Charm, Nimble
    Ring, Jotunn''s Revenge, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Shield
    Splitter, Breastplate of Valor, Tyrfing, Soul Gem, Pharaoh''s Curse, Tekko-Kagi,
    Toxic Blade, Runeforged Hammer, Silverbranch Bow, Shogun''s Ofuda, Lernaean Bow,
    Oni Hunter''s Garb, Eros'' Bow, Erosion, Hydra''s Lament, Riptalon, Eye of Providence,
    Stone of Binding, Obsidian Shard, Helm of Radiance, Draconic Scale, Shield of
    the Phoenix, Midgardian Mail, Screeching Gargoyle, Spear of Desolation, Magi''s
    Cloak, Sundering Echo, Helm of Darkness, The Reaper, Titan''s Bane, Leviathan''s
    Hide, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.09
      fit: 0.2
    Berserker's Shield:
      total: 0.56
      efficiency: 0.7
      win: 0.56
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.2
    Nimble Ring:
      total: 0.51
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Jotunn''s
    Revenge, Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix,
    Berserker''s Shield, Spear of Desolation, Screeching Gargoyle, Hydra''s Lament,
    Soul Gem, Shield Splitter, Chronos'' Pendant, Prophetic Cloak, Erosion, Gladiator''s
    Shield, Arondight, Gluttonous Grimoire, Eye of Providence, Helm of Radiance, Helm
    of Darkness, Oni Hunter''s Garb, Draconic Scale, Runeforged Hammer, Obsidian Shard,
    Stone of Binding, Heartwood Charm, Gem of Focus, Chandra''s Grace, Midgardian
    Mail, Magi''s Cloak, Sundering Echo, Glorious Pridwen, Mantle Of Discord, Leviathan''s
    Hide, Regrowth Striders, Eye of Erebus, Ancile, Titan''s Bane, Shifter''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.61
      pick: 0.09
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.51
      pick: 0.28
      fit: 0.64
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Genji''s Guard, Amanita Charm, Shield Splitter, Kinetic Cuirass, Golden
    Blade, Tekko-Kagi, Titan''s Bane, Runeforged Hammer, Breastplate of Valor, Gluttonous
    Grimoire, Hydra''s Lament, Obsidian Shard, Tyrfing, Spear of Desolation, Sundering
    Echo, Erosion, Heartseeker, Toxic Blade, Soul Gem, Oni Hunter''s Garb, The Crusher,
    Eye of Providence, Lernaean Bow, Draconic Scale, Silverbranch Bow, Stone of Binding,
    Shield of the Phoenix, Helm of Radiance, Avenging Blade, Midgardian Mail, Pharaoh''s
    Curse, The Reaper, Magi''s Cloak, Screeching Gargoyle, Helm of Darkness, Wyrmskin
    Hide, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.7
      win: 0.56
      pick: 0.0
      fit: 0.36
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.09
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Helm of Darkness — magical protection
    swap_item: Helm of Darkness
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Berserker''s Shield,
    Shield Splitter, Obsidian Shard, Spear of Desolation, Soul Gem, Sundering Echo,
    Breastplate of Valor, Helm of Radiance, Titan''s Bane, Runeforged Hammer, Helm
    of Darkness, Spear of the Magus, Hydra''s Lament, Erosion, Oni Hunter''s Garb,
    Death Metal, Eye of Providence, Doom Orb, Draconic Scale, Stone of Binding, Shield
    of the Phoenix, The World Stone, Heartseeker, Midgardian Mail, The Crusher, Screeching
    Gargoyle, Magi''s Cloak, Jade Scepter, Chronos'' Pendant, Mantle Of Discord, Leviathan''s
    Hide, Avenging Blade, The Reaper, Triton''s Conch, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.27
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.09
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.51
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Berserker''s
    Shield, Genji''s Guard, Shield Splitter, Erosion, Breastplate of Valor, Eye of
    Providence, Draconic Scale, Jotunn''s Revenge, Shield of the Phoenix, Shifter''s
    Shield, Oni Hunter''s Garb, Stone of Binding, Helm of Darkness, Magi''s Cloak,
    Midgardian Mail, Mantle Of Discord, Leviathan''s Hide, Gluttonous Grimoire, Screeching
    Gargoyle, Helm of Radiance, Prophetic Cloak, Ancile, Runeforged Hammer, Hide of
    the Nemean Lion, Void Stone, Spear of Desolation, Void Shield, Xibalban Effigy,
    Gladiator''s Shield, Hussar''s Wings, Obsidian Shard, Soul Gem, Spectral Armor,
    Brawler’s Beat Stick, Phoenix Feather, Hydra''s Lament, Doublet of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.44
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.09
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.51
      pick: 0.28
      fit: 0.62
    Shield Splitter:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.56
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
