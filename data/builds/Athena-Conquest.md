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
  god_matches_analyzed: 14484
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
  - Shield Splitter
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Kinetic Cuirass, Berserker''s
    Shield, Shield Splitter, Erosion, Eye of Providence, Breastplate of Valor, Draconic
    Scale, Jotunn''s Revenge, Shield of the Phoenix, Helm of Darkness, Oni Hunter''s
    Garb, Stone of Binding, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Helm
    of Radiance, Leviathan''s Hide, Gluttonous Grimoire, Screeching Gargoyle, Runeforged
    Hammer, Shifter''s Shield, Prophetic Cloak, Spear of Desolation, Ancile, Hide
    of the Nemean Lion, Void Stone, Void Shield, Brawler’s Beat Stick, Xibalban Effigy,
    Hydra''s Lament, Obsidian Shard, Soul Gem, Spectral Armor, Hussar''s Wings, Gladiator''s
    Shield, Phoenix Feather, Doublet of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.44
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.09
      fit: 0.37
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.51
      pick: 0.28
      fit: 0.62
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
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
  - Shield Splitter
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Shield of the Phoenix,
    Kinetic Cuirass, Berserker''s Shield, Soul Gem, Phoenix Feather, Shield Splitter,
    Erosion, Eye of Providence, Jotunn''s Revenge, Ethereal Staff, Draconic Scale,
    Yogi''s Necklace, Breastplate of Valor, Oni Hunter''s Garb, Chandra''s Grace,
    Gluttonous Grimoire, Midgardian Mail, Runeforged Hammer, Glorious Pridwen, Leviathan''s
    Hide, Helm of Darkness, Rod of Asclepius, Regrowth Striders, Stone of Binding,
    Helm of Radiance, Sphere of Negation, Ancile, Magi''s Cloak, Spear of Desolation,
    Hide of the Nemean Lion, Blood-Bound Book, Screeching Gargoyle, Void Stone, Mantle
    Of Discord, Void Shield, Shifter''s Shield, The Reaper.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.09
      fit: 0.34
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.76
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.47
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.9
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Genji''s Guard, Amanita Charm,
    Stone of Binding, Kinetic Cuirass, Gluttonous Grimoire, Spear of Desolation, Berserker''s
    Shield, Screeching Gargoyle, Obsidian Shard, Soul Gem, Void Stone, Void Shield,
    Shield Splitter, Titan''s Bane, Spear of the Magus, Avenging Blade, Breastplate
    of Valor, Erosion, Eye of Providence, Oni Hunter''s Garb, Doom Orb, The Crusher,
    Draconic Scale, The World Stone, Helm of Radiance, Shield of the Phoenix, Helm
    of Darkness, Heartseeker, Runeforged Hammer, Midgardian Mail, Magi''s Cloak, Dreamer''s
    Idol, The Reaper, Mantle Of Discord, Leviathan''s Hide, Toxic Blade, Hydra''s
    Lament, Ancile, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.09
      fit: 0.26
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.58
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
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
    Ring, Jotunn''s Revenge, Kinetic Cuirass, Golden Blade, Shield Splitter, Gluttonous
    Grimoire, Tyrfing, Breastplate of Valor, Soul Gem, Runeforged Hammer, Tekko-Kagi,
    Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Hydra''s Lament, Oni Hunter''s Garb,
    Shogun''s Ofuda, Eros'' Bow, Helm of Radiance, Silverbranch Bow, Erosion, Eye
    of Providence, Stone of Binding, Obsidian Shard, Draconic Scale, Midgardian Mail,
    Spear of Desolation, Helm of Darkness, Shield of the Phoenix, Magi''s Cloak, The
    Reaper, Screeching Gargoyle, Titan''s Bane, Riptalon, Leviathan''s Hide, Blood-Bound
    Book, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.09
      fit: 0.2
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.56
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.2
    Nimble Ring:
      total: 0.52
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Jotunn''s
    Revenge, Amanita Charm, Breastplate of Valor, Kinetic Cuirass, Berserker''s Shield,
    Spear of Desolation, Shield of the Phoenix, Hydra''s Lament, Shield Splitter,
    Screeching Gargoyle, Soul Gem, Lotus Sickle, Chronos'' Pendant, Arondight, Prophetic
    Cloak, Helm of Radiance, Runeforged Hammer, Erosion, Helm of Darkness, Eye of
    Providence, Oni Hunter''s Garb, Gluttonous Grimoire, Gladiator''s Shield, Draconic
    Scale, Gem of Focus, Stone of Binding, Obsidian Shard, Heartwood Charm, Midgardian
    Mail, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Chandra''s Grace, Regrowth
    Striders, Eye of Erebus, Glorious Pridwen, Jade Scepter, Titan''s Bane, Shifter''s
    Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.61
      pick: 0.09
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.51
      pick: 0.28
      fit: 0.64
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
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
    Revenge, Genji''s Guard, Amanita Charm, Shield Splitter, Kinetic Cuirass, Runeforged
    Hammer, Golden Blade, Tekko-Kagi, Titan''s Bane, Hydra''s Lament, Breastplate
    of Valor, Tyrfing, Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, The
    Crusher, Oni Hunter''s Garb, Erosion, Lernaean Bow, Soul Gem, Avenging Blade,
    Eye of Providence, Heartseeker, Helm of Radiance, Toxic Blade, Draconic Scale,
    Stone of Binding, The Reaper, Shield of the Phoenix, Helm of Darkness, Arondight,
    Midgardian Mail, Silverbranch Bow, Magi''s Cloak, Death Metal, Spear of the Magus,
    Pharaoh''s Curse, Screeching Gargoyle, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.74
      win: 0.56
      pick: 0.0
      fit: 0.36
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.09
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
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
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Helm of Darkness — magical protection
    swap_item: Helm of Darkness
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Berserker''s Shield, Kinetic Cuirass,
    Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, Soul Gem, Helm of Radiance,
    Runeforged Hammer, Breastplate of Valor, Helm of Darkness, Titan''s Bane, Spear
    of the Magus, Hydra''s Lament, Death Metal, Oni Hunter''s Garb, Erosion, Eye of
    Providence, Lotus Sickle, The Crusher, Doom Orb, Jade Scepter, Draconic Scale,
    Stone of Binding, Shield of the Phoenix, The World Stone, Midgardian Mail, Avenging
    Blade, Heartseeker, Magi''s Cloak, Chronos'' Pendant, Screeching Gargoyle, Mantle
    Of Discord, Leviathan''s Hide, The Reaper, Dreamer''s Idol, Arondight.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.27
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.09
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
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
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Berserker''s
    Shield, Genji''s Guard, Shield Splitter, Erosion, Eye of Providence, Breastplate
    of Valor, Draconic Scale, Jotunn''s Revenge, Shield of the Phoenix, Helm of Darkness,
    Oni Hunter''s Garb, Shifter''s Shield, Stone of Binding, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Helm of Radiance, Leviathan''s Hide, Gluttonous Grimoire,
    Screeching Gargoyle, Runeforged Hammer, Prophetic Cloak, Spear of Desolation,
    Ancile, Hide of the Nemean Lion, Void Stone, Void Shield, Brawler’s Beat Stick,
    Xibalban Effigy, Hydra''s Lament, Obsidian Shard, Soul Gem, Spectral Armor, Hussar''s
    Wings, Gladiator''s Shield, Phoenix Feather, Doublet of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.44
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.09
      fit: 0.37
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.51
      pick: 0.28
      fit: 0.62
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
