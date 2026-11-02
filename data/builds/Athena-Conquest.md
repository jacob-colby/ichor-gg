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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Kinetic Cuirass, Berserker''s
    Shield, Shield Splitter, Erosion, Breastplate of Valor, Eye of Providence, Jotunn''s
    Revenge, Draconic Scale, Shield of the Phoenix, Helm of Darkness, Stone of Binding,
    Oni Hunter''s Garb, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Helm of
    Radiance, Leviathan''s Hide, Screeching Gargoyle, Gluttonous Grimoire, Runeforged
    Hammer, Shifter''s Shield, Prophetic Cloak, Spear of Desolation, Ancile, Hide
    of the Nemean Lion, Void Stone, Brawler’s Beat Stick, Void Shield, Xibalban Effigy,
    Hydra''s Lament, Soul Gem, Obsidian Shard, Gladiator''s Shield, Hussar''s Wings,
    Spectral Armor, Phoenix Feather, Doublet of Binding.'
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Shield of the Phoenix,
    Kinetic Cuirass, Berserker''s Shield, Soul Gem, Phoenix Feather, Jotunn''s Revenge,
    Shield Splitter, Erosion, Eye of Providence, Breastplate of Valor, Draconic Scale,
    Ethereal Staff, Yogi''s Necklace, Chandra''s Grace, Oni Hunter''s Garb, Midgardian
    Mail, Gluttonous Grimoire, Runeforged Hammer, Glorious Pridwen, Leviathan''s Hide,
    Helm of Darkness, Stone of Binding, Rod of Asclepius, Regrowth Striders, Helm
    of Radiance, Sphere of Negation, Magi''s Cloak, Ancile, Hide of the Nemean Lion,
    Screeching Gargoyle, Spear of Desolation, Void Stone, Mantle Of Discord, Blood-Bound
    Book, Shifter''s Shield, Void Shield, The Reaper.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
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
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.76
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
    Stone of Binding, Kinetic Cuirass, Gluttonous Grimoire, Screeching Gargoyle, Berserker''s
    Shield, Spear of Desolation, Obsidian Shard, Soul Gem, Void Stone, Void Shield,
    Shield Splitter, Breastplate of Valor, Titan''s Bane, Avenging Blade, Spear of
    the Magus, Erosion, Eye of Providence, Doom Orb, The Crusher, Draconic Scale,
    The World Stone, Heartseeker, Oni Hunter''s Garb, Helm of Radiance, Shield of
    the Phoenix, Helm of Darkness, Runeforged Hammer, Magi''s Cloak, Midgardian Mail,
    The Reaper, Mantle Of Discord, Dreamer''s Idol, Leviathan''s Hide, Toxic Blade,
    Hydra''s Lament, Ancile, Shifter''s Shield.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.66
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
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.58
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
  - Nimble Ring
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
    this god: Berserker''s Shield, Rod of Tahuti, Genji''s Guard, Amanita Charm, Jotunn''s
    Revenge, Nimble Ring, Kinetic Cuirass, Golden Blade, Shield Splitter, Gluttonous
    Grimoire, Tyrfing, Breastplate of Valor, Soul Gem, Runeforged Hammer, Tekko-Kagi,
    Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Hydra''s Lament, Shogun''s Ofuda,
    Silverbranch Bow, Helm of Radiance, Erosion, Eros'' Bow, Oni Hunter''s Garb, Eye
    of Providence, Stone of Binding, Obsidian Shard, Draconic Scale, Midgardian Mail,
    Shield of the Phoenix, Helm of Darkness, Spear of Desolation, Magi''s Cloak, Screeching
    Gargoyle, The Reaper, Riptalon, Titan''s Bane, Mantle Of Discord, Blood-Bound
    Book, Leviathan''s Hide.'
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
      efficiency: 0.75
      win: 0.56
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.2
    Nimble Ring:
      total: 0.52
      efficiency: 0.64
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
    Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Arondight, Prophetic Cloak,
    Helm of Radiance, Runeforged Hammer, Helm of Darkness, Erosion, Eye of Providence,
    Gluttonous Grimoire, Gladiator''s Shield, Draconic Scale, Stone of Binding, Oni
    Hunter''s Garb, Gem of Focus, Obsidian Shard, Heartwood Charm, Midgardian Mail,
    Magi''s Cloak, Mantle Of Discord, Chandra''s Grace, Leviathan''s Hide, Eye of
    Erebus, Glorious Pridwen, Regrowth Striders, Titan''s Bane, Jade Scepter, Ancile,
    Shifter''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
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
      efficiency: 0.69
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
    Hammer, Golden Blade, Tekko-Kagi, Titan''s Bane, Breastplate of Valor, Hydra''s
    Lament, Tyrfing, Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, The
    Crusher, Heartseeker, Lernaean Bow, Erosion, Soul Gem, Avenging Blade, Eye of
    Providence, Helm of Radiance, Oni Hunter''s Garb, Toxic Blade, Stone of Binding,
    Draconic Scale, Arondight, The Reaper, Shield of the Phoenix, Helm of Darkness,
    Silverbranch Bow, Midgardian Mail, Magi''s Cloak, Death Metal, Screeching Gargoyle,
    Pharaoh''s Curse, Spear of the Magus, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.75
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
      efficiency: 0.69
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Genji''s Guard, Amanita Charm, Shield Splitter, Berserker''s Shield, Kinetic Cuirass,
    Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, Soul Gem, Helm of Radiance,
    Breastplate of Valor, Runeforged Hammer, Helm of Darkness, Titan''s Bane, Spear
    of the Magus, Hydra''s Lament, Death Metal, Erosion, Eye of Providence, Doom Orb,
    The Crusher, Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Jade Scepter,
    Heartseeker, Shield of the Phoenix, The World Stone, Midgardian Mail, Avenging
    Blade, Magi''s Cloak, Chronos'' Pendant, Screeching Gargoyle, Mantle Of Discord,
    Arondight, The Reaper, Leviathan''s Hide, Dreamer''s Idol, Shifter''s Shield.'
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
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.52
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Berserker''s
    Shield, Genji''s Guard, Shield Splitter, Erosion, Breastplate of Valor, Eye of
    Providence, Jotunn''s Revenge, Draconic Scale, Shield of the Phoenix, Shifter''s
    Shield, Helm of Darkness, Stone of Binding, Oni Hunter''s Garb, Magi''s Cloak,
    Midgardian Mail, Mantle Of Discord, Helm of Radiance, Leviathan''s Hide, Screeching
    Gargoyle, Gluttonous Grimoire, Runeforged Hammer, Prophetic Cloak, Spear of Desolation,
    Ancile, Hide of the Nemean Lion, Void Stone, Brawler’s Beat Stick, Void Shield,
    Xibalban Effigy, Hydra''s Lament, Soul Gem, Obsidian Shard, Gladiator''s Shield,
    Hussar''s Wings, Spectral Armor, Phoenix Feather, Doublet of Binding.'
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
