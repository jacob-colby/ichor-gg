---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.28
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.41
    win_rate: 0.61
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.63
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.74
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.56
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.65
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.62
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.65
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.66
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.55
  - name: Sage's Ring
    pick_rate: 0.09
    win_rate: 0.89
    alternates:
    - name: Veve Charm
      pick_rate: 0.08
      win_rate: 0.61
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.71
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.32
    win_rate: 0.62
  - name: Bumba's Cudgel
    pick_rate: 0.3
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.09
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-11-02'
  god_win_rate: 0.5677749360613811
  god_matches_won: 222
  god_matches_played: 391
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Jotunn''s Revenge, Berserker''s
    Shield, Erosion, Eye of Providence, Hydra''s Lament, Shield of the Phoenix, Stone
    of Binding, Helm of Darkness, Oni Hunter''s Garb, Magi''s Cloak, Midgardian Mail,
    Helm of Radiance, Mantle Of Discord, Avenging Blade, Titan''s Bane, Screeching
    Gargoyle, Wyrmskin Hide, Leviathan''s Hide, Gluttonous Grimoire, Spear of Desolation,
    Arondight, Ancile, Hide of the Nemean Lion, Obsidian Shard, Stampede, Prophetic
    Cloak, Void Stone, Death Metal, Void Shield, Soul Gem, Brawler’s Beat Stick, Xibalban
    Effigy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.67
    Shield Splitter:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.6
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.52
    Shifter's Shield:
      total: 0.59
      efficiency: 0.47
      win: 0.74
      pick: 0.16
      fit: 0.57
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Jotunn''s Revenge,
    Shield Splitter, Berserker''s Shield, Soul Gem, Phoenix Feather, Yogi''s Necklace,
    The Reaper, Ethereal Staff, Erosion, Hydra''s Lament, Eye of Providence, Chandra''s
    Grace, Oni Hunter''s Garb, Avenging Blade, Gluttonous Grimoire, Midgardian Mail,
    Wyrmskin Hide, Glorious Pridwen, Titan''s Bane, Leviathan''s Hide, Regrowth Striders,
    Blood-Bound Book, Stone of Binding, Helm of Radiance, Rod of Asclepius, Helm of
    Darkness, Sphere of Negation, Arondight, Spear of Desolation, Screeching Gargoyle,
    Magi''s Cloak, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.66
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.52
      win: 0.65
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.59
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.46
    Shifter's Shield:
      total: 0.59
      efficiency: 0.47
      win: 0.74
      pick: 0.16
      fit: 0.56
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Shield Splitter, Screeching Gargoyle, Avenging Blade, Berserker''s Shield, Titan''s
    Bane, Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, Void Stone, Soul
    Gem, Void Shield, The Crusher, Heartseeker, Spear of the Magus, The Reaper, Hydra''s
    Lament, Erosion, Eye of Providence, Doom Orb, Helm of Radiance, Oni Hunter''s
    Garb, Tekko-Kagi, The World Stone, Shield of the Phoenix, Helm of Darkness, Midgardian
    Mail, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Dreamer''s Idol, Avatar''s
    Parashu.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.5
      win: 0.65
      pick: 0.0
      fit: 0.7
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.67
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.52
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.38
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Golden Blade, Shield Splitter, Gluttonous Grimoire, Tyrfing, Soul
    Gem, Tekko-Kagi, Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Hydra''s Lament,
    Shogun''s Ofuda, Silverbranch Bow, Helm of Radiance, Erosion, Eros'' Bow, Oni
    Hunter''s Garb, Eye of Providence, Stone of Binding, Midgardian Mail, Shield of
    the Phoenix, Obsidian Shard, Helm of Darkness, Magi''s Cloak, Spear of Desolation,
    Screeching Gargoyle, The Reaper, Riptalon, Titan''s Bane, Mantle Of Discord, Leviathan''s
    Hide, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.65
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.62
      efficiency: 0.75
      win: 0.65
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.47
    Nimble Ring:
      total: 0.56
      efficiency: 0.64
      win: 0.65
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Berserker''s Shield, Spear of Desolation, Shield of the Phoenix,
    Hydra''s Lament, Shield Splitter, Screeching Gargoyle, Soul Gem, Chronos'' Pendant,
    Arondight, Prophetic Cloak, Helm of Radiance, Helm of Darkness, Erosion, Eye of
    Providence, Gluttonous Grimoire, Gladiator''s Shield, Stone of Binding, Oni Hunter''s
    Garb, Gem of Focus, Obsidian Shard, Heartwood Charm, Midgardian Mail, Magi''s
    Cloak, Mantle Of Discord, Chandra''s Grace, Leviathan''s Hide, Eye of Erebus,
    Glorious Pridwen, Regrowth Striders, Titan''s Bane, Jade Scepter, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.64
      win: 0.67
      pick: 0.2
      fit: 0.48
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.61
      pick: 0.23
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.55
    Freya's Tears:
      total: 0.62
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.64
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Tekko-Kagi, Titan''s Bane, Golden Blade,
    Hydra''s Lament, Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, Tyrfing,
    The Crusher, Heartseeker, Lernaean Bow, Erosion, Avenging Blade, Eye of Providence,
    Soul Gem, Helm of Radiance, Oni Hunter''s Garb, Stone of Binding, Arondight, The
    Reaper, Shield of the Phoenix, Helm of Darkness, Midgardian Mail, Magi''s Cloak,
    Pharaoh''s Curse, Screeching Gargoyle, Death Metal, Toxic Blade, Wyrmskin Hide,
    Mantle Of Discord, Spear of the Magus.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.75
      win: 0.65
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.52
    Shield Splitter:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.38
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Shield Splitter, Berserker''s Shield, Gluttonous Grimoire, Spear
    of Desolation, Obsidian Shard, Soul Gem, Helm of Radiance, Helm of Darkness, Titan''s
    Bane, Spear of the Magus, Hydra''s Lament, Death Metal, Erosion, Eye of Providence,
    Doom Orb, The Crusher, Oni Hunter''s Garb, Stone of Binding, Jade Scepter, Heartseeker,
    Shield of the Phoenix, The World Stone, Midgardian Mail, Avenging Blade, Magi''s
    Cloak, Chronos'' Pendant, Screeching Gargoyle, Mantle Of Discord, Arondight, The
    Reaper, Leviathan''s Hide, Dreamer''s Idol.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.67
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.52
    Shield Splitter:
      total: 0.57
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.38
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Jotunn''s
    Revenge, Berserker''s Shield, Erosion, Eye of Providence, Hydra''s Lament, Shield
    of the Phoenix, Stone of Binding, Helm of Darkness, Oni Hunter''s Garb, Magi''s
    Cloak, Midgardian Mail, Helm of Radiance, Mantle Of Discord, Avenging Blade, Titan''s
    Bane, Screeching Gargoyle, Wyrmskin Hide, Leviathan''s Hide, Gluttonous Grimoire,
    Spear of Desolation, Arondight, Ancile, Hide of the Nemean Lion, Obsidian Shard,
    Stampede, Prophetic Cloak, Void Stone, Death Metal, Void Shield, Soul Gem, Brawler’s
    Beat Stick, Xibalban Effigy.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.23
      fit: 0.31
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.67
    Shield Splitter:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
---
