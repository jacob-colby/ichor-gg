---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.29
  aspect_win_rate: 0.62
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.35
    win_rate: 0.59
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.44
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.69
  - name: Stampede
    pick_rate: 0.14
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.63
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.64
  - name: Shell of Rebuke
    pick_rate: 0.16
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.53
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.62
  - name: Spirit Robe
    pick_rate: 0.05
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.61
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.66
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.64
    alternates:
    - name: Polynomicon
      pick_rate: 0.05
      win_rate: 0.9
    - name: Mote of Chaos
      pick_rate: 0.05
      win_rate: 0.56
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.25
    win_rate: 0.68
  - name: Bumba's Cudgel
    pick_rate: 0.21
    win_rate: 0.46
  - name: Selflessness
    pick_rate: 0.18
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-11-08'
  god_win_rate: 0.5725593667546174
  god_matches_won: 217
  god_matches_played: 379
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Polynomicon
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
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
    this god: Kinetic Cuirass, Amanita Charm, Jotunn''s Revenge, Rod of Tahuti, Berserker''s
    Shield, Draconic Scale, Shield Splitter, Shield of the Phoenix, Gluttonous Grimoire,
    Breastplate of Valor, Erosion, Eye of Providence, Soul Gem, Shifter''s Shield,
    Oni Hunter''s Garb, Stone of Binding, Midgardian Mail, Helm of Darkness, Screeching
    Gargoyle, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Prophetic Cloak,
    Hide of the Nemean Lion, Spear of Desolation, Helm of Radiance, Gladiator''s Shield,
    Lotus Sickle, Ancile, Runeforged Hammer, Blood-Bound Book, Void Stone, Phoenix
    Feather, Void Shield, Spectral Armor, Hydra''s Lament, The Reaper, Doublet of
    Binding, Hussar''s Wings.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.69
      pick: 0.08
      fit: 0.22
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.63
      pick: 0.19
      fit: 0.33
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.61
      win: 0.64
      pick: 0.14
      fit: 0.71
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.25
      fit: 0.55
    Polynomicon:
      total: 0.63
      efficiency: 0.56
      win: 0.9
      pick: 0.15
      fit: 0.16
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Polynomicon
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Polynomicon
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Jotunn''s
    Revenge, Rod of Tahuti, Berserker''s Shield, Phoenix Feather, Gluttonous Grimoire,
    Blood-Bound Book, The Reaper, Draconic Scale, Yogi''s Necklace, Ethereal Staff,
    Oni Hunter''s Garb, Erosion, Chandra''s Grace, Breastplate of Valor, Eye of Providence,
    Shield Splitter, Shifter''s Shield, Midgardian Mail, Bancroft''s Talon, Regrowth
    Striders, Glorious Pridwen, Leviathan''s Hide, Rod of Asclepius, Hide of the Nemean
    Lion, Runeforged Hammer, Soul Locket, Spear of Desolation, Screeching Gargoyle,
    Gladiator''s Shield, Ancile, Stone of Binding, Lotus Sickle, Helm of Darkness,
    Void Stone, Helm of Radiance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.69
      pick: 0.08
      fit: 0.23
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.63
      pick: 0.19
      fit: 0.3
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.61
      win: 0.64
      pick: 0.14
      fit: 0.69
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.83
    Polynomicon:
      total: 0.63
      efficiency: 0.56
      win: 0.9
      pick: 0.15
      fit: 0.17
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.89
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Polynomicon
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm,
    Gluttonous Grimoire, Soul Gem, Screeching Gargoyle, Stone of Binding, Spear of
    Desolation, Berserker''s Shield, Void Stone, Void Shield, The Reaper, Breastplate
    of Valor, Obsidian Shard, Shield Splitter, Shield of the Phoenix, Draconic Scale,
    Avenging Blade, Oni Hunter''s Garb, Spear of the Magus, The Crusher, Erosion,
    Eye of Providence, Dreamer''s Idol, Heartseeker, Shifter''s Shield, Midgardian
    Mail, Titan''s Bane, Helm of Radiance, Lotus Sickle, Doom Orb, Leviathan''s Hide,
    Blood-Bound Book, Magi''s Cloak, Mantle Of Discord, Runeforged Hammer, Helm of
    Darkness, Hide of the Nemean Lion, The World Stone.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.64
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.63
      pick: 0.19
      fit: 0.24
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.69
      pick: 0.08
      fit: 0.44
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.14
      fit: 0.54
    Polynomicon:
      total: 0.63
      efficiency: 0.56
      win: 0.9
      pick: 0.15
      fit: 0.15
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Polynomicon
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Jotunn''s Revenge, Rod of Tahuti,
    Amanita Charm, Tyrfing, Golden Blade, Shield Splitter, Gluttonous Grimoire, Breastplate
    of Valor, Soul Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s Garb, Draconic
    Scale, Runeforged Hammer, Shogun''s Ofuda, Pharaoh''s Curse, Erosion, Hydra''s
    Lament, Eye of Providence, Spear of Desolation, Toxic Blade, Bragi''s Harp, Lotus
    Sickle, Screeching Gargoyle, Shifter''s Shield, Midgardian Mail, Blood-Bound Book,
    The Reaper, Helm of Radiance, Eros'' Bow, Stone of Binding, Lernaean Bow, Dominance,
    Leviathan''s Hide, Silverbranch Bow, Magi''s Cloak, Mantle Of Discord, Hide of
    the Nemean Lion.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.69
      pick: 0.08
      fit: 0.2
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.14
      fit: 0.47
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.53
    Polynomicon:
      total: 0.63
      efficiency: 0.56
      win: 0.9
      pick: 0.15
      fit: 0.14
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Polynomicon
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Kinetic Cuirass,
    Rod of Tahuti, Amanita Charm, Soul Gem, Breastplate of Valor, Shield of the Phoenix,
    Spear of Desolation, Lotus Sickle, Berserker''s Shield, Screeching Gargoyle, Hydra''s
    Lament, Gluttonous Grimoire, Shield Splitter, Chronos'' Pendant, Prophetic Cloak,
    Gladiator''s Shield, Draconic Scale, Oni Hunter''s Garb, Arondight, Erosion, Eye
    of Providence, Helm of Radiance, Runeforged Hammer, Blood-Bound Book, Shifter''s
    Shield, Gem of Focus, Heartwood Charm, Helm of Darkness, Midgardian Mail, Chandra''s
    Grace, Stone of Binding, Leviathan''s Hide, Regrowth Striders, Ancient Signet,
    Magi''s Cloak, Mantle Of Discord, The Reaper, Hide of the Nemean Lion, Eye of
    Erebus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.69
      pick: 0.08
      fit: 0.42
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.63
      pick: 0.19
      fit: 0.45
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.14
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.25
      fit: 0.6
    Polynomicon:
      total: 0.64
      efficiency: 0.56
      win: 0.9
      pick: 0.15
      fit: 0.19
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Polynomicon
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti, Kinetic
    Cuirass, Berserker''s Shield, Amanita Charm, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, The Reaper, Tyrfing, Runeforged Hammer, Breastplate of Valor, Golden
    Blade, Hydra''s Lament, Spear of Desolation, Shield of the Phoenix, The Crusher,
    Oni Hunter''s Garb, Draconic Scale, Heartseeker, Erosion, Eye of Providence, Tekko-Kagi,
    Death Metal, Titan''s Bane, Shifter''s Shield, Midgardian Mail, Screeching Gargoyle,
    Lotus Sickle, Bragi''s Harp, Helm of Radiance, Stone of Binding, Blood-Bound Book,
    Obsidian Shard, Avenging Blade, Leviathan''s Hide, Toxic Blade, Arondight, Nimble
    Ring, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.63
      pick: 0.19
      fit: 0.21
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.69
      pick: 0.08
      fit: 0.42
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.14
      fit: 0.49
    Polynomicon:
      total: 0.63
      efficiency: 0.56
      win: 0.9
      pick: 0.15
      fit: 0.14
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Polynomicon
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire, Soul Gem, Shield Splitter,
    Spear of Desolation, Berserker''s Shield, The Reaper, Breastplate of Valor, Lotus
    Sickle, Helm of Radiance, Blood-Bound Book, Runeforged Hammer, Shield of the Phoenix,
    Obsidian Shard, Death Metal, Oni Hunter''s Garb, Draconic Scale, Helm of Darkness,
    Hydra''s Lament, Spear of the Magus, Ancient Signet, The Crusher, Erosion, Eye
    of Providence, Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Shifter''s Shield,
    Midgardian Mail, Screeching Gargoyle, Tyrfing, Stone of Binding, Jade Scepter,
    Titan''s Bane, Leviathan''s Hide, Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.08
      fit: 0.38
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.63
      pick: 0.19
      fit: 0.21
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.14
      fit: 0.49
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.44
    Polynomicon:
      total: 0.65
      efficiency: 0.56
      win: 0.9
      pick: 0.15
      fit: 0.27
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Berserker''s
    Shield, Draconic Scale, Shield Splitter, Shield of the Phoenix, Gluttonous Grimoire,
    Breastplate of Valor, Erosion, Eye of Providence, Soul Gem, Shifter''s Shield,
    Oni Hunter''s Garb, Jotunn''s Revenge, Stone of Binding, Midgardian Mail, Helm
    of Darkness, Screeching Gargoyle, Magi''s Cloak, Mantle Of Discord, Leviathan''s
    Hide, Hide of the Nemean Lion, Spear of Desolation, Helm of Radiance, Gladiator''s
    Shield, Lotus Sickle, Ancile, Runeforged Hammer, Prophetic Cloak, Blood-Bound
    Book, Void Stone, Phoenix Feather, Void Shield, Spectral Armor, Hydra''s Lament,
    The Reaper, Doublet of Binding, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.63
      pick: 0.19
      fit: 0.33
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.61
      win: 0.64
      pick: 0.14
      fit: 0.71
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.25
      fit: 0.55
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-09-24'
  partial_windows:
    ob44: '2026-09-24'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of War
    status: shown
    window: ob47
    window_rule: newest
    window_start: '2026-11-03'
    window_end: '2026-11-08'
    matches: 101
    wins: 65
    win_share: 0.64
    aggregate:
      aspect_matches: 114
      aspect_win_rate: 0.623
      no_aspect_matches: 288
      no_aspect_win_rate: 0.566
    roles:
    - role: Jungle
      matches: 77
      share: 0.76
    - role: Solo
      matches: 14
      share: 0.14
    - role: Support
      matches: 8
      share: 0.08
    - role: Mid
      matches: 2
      share: 0.02
    base_role: Support
    base_role_share: 0.08
    role_shift:
      role: Jungle
      share: 0.76
      says: 'most Aspect of War players do not play Support: Jungle 76%, Support 8%'
    items:
    - name: Hydra's Lament
      share: 0.53
    - name: Jotunn's Revenge
      share: 0.43
    - name: Transcendence
      share: 0.32
    - name: Book of Thoth
      share: 0.29
    - name: Shifter's Shield
      share: 0.27
    - name: Kinetic Cuirass
      share: 0.25
    - name: Polynomicon
      share: 0.24
    - name: Freya's Tears
      share: 0.21
    starters:
    - name: Bumba's Hammer
      share: 0.6
    - name: Bumba's Cudgel
      share: 0.18
    - name: Sharpshooter's Arrow
      share: 0.08
    relics:
    - name: purification-beads
      share: 0.53
    - name: Blink Rune
      share: 0.16
    - name: aegis-of-acceleration
      share: 0.14
    matches_by_window:
      ob47: 101
      ob46: 208
      ob45: 328
      ob44: 201
    unmapped_slugs:
    - aegis-of-acceleration
    - agility-relic
    - brawlers-ruin
    - phantom-shell
    - purification-beads
    - sundering-arc
---
