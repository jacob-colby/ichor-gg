---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.29
  aspect_win_rate: 0.63
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.37
    win_rate: 0.57
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.43
    - name: Transcendence
      pick_rate: 0.08
      win_rate: 0.83
  - name: Stampede
    pick_rate: 0.16
    win_rate: 0.49
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.4
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.7
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.71
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.45
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.52
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.56
  - name: Spirit Robe
    pick_rate: 0.06
    win_rate: 0.73
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.73
  - name: Sage's Ring
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Polynomicon
      pick_rate: 0.07
      win_rate: 0.86
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.25
    win_rate: 0.67
  - name: Selflessness
    pick_rate: 0.21
    win_rate: 0.44
  - name: Bumba's Cudgel
    pick_rate: 0.19
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-11-06'
  god_win_rate: 0.5694444444444444
  god_matches_won: 123
  god_matches_played: 216
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Transcendence
  - Polynomicon
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Prophetic Cloak, Rod of Tahuti, Berserker''s
    Shield, Draconic Scale, Shield Splitter, Shield of the Phoenix, Gluttonous Grimoire,
    Breastplate of Valor, Erosion, Eye of Providence, Soul Gem, Shifter''s Shield,
    Oni Hunter''s Garb, Jotunn''s Revenge, Stone of Binding, Midgardian Mail, Helm
    of Darkness, Screeching Gargoyle, Magi''s Cloak, Mantle Of Discord, Leviathan''s
    Hide, Hide of the Nemean Lion, Spear of Desolation, Helm of Radiance, Gladiator''s
    Shield, Lotus Sickle, Ancile, Runeforged Hammer, Blood-Bound Book, Void Stone,
    Phoenix Feather, Void Shield, Spectral Armor, Hydra''s Lament, The Reaper, Doublet
    of Binding, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.33
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.71
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.45
      win: 0.7
      pick: 0.12
      fit: 0.55
    Transcendence:
      total: 0.56
      efficiency: 0.5
      win: 0.83
      pick: 0.08
      fit: 0.05
    Polynomicon:
      total: 0.62
      efficiency: 0.56
      win: 0.86
      pick: 0.22
      fit: 0.16
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Transcendence
  - Polynomicon
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Transcendence
  - Polynomicon
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Rod
    of Tahuti, Berserker''s Shield, Phoenix Feather, Gluttonous Grimoire, Blood-Bound
    Book, The Reaper, Draconic Scale, Yogi''s Necklace, Ethereal Staff, Oni Hunter''s
    Garb, Erosion, Chandra''s Grace, Breastplate of Valor, Eye of Providence, Shield
    Splitter, Shifter''s Shield, Jotunn''s Revenge, Midgardian Mail, Bancroft''s Talon,
    Regrowth Striders, Glorious Pridwen, Leviathan''s Hide, Rod of Asclepius, Hide
    of the Nemean Lion, Runeforged Hammer, Soul Locket, Spear of Desolation, Screeching
    Gargoyle, Gladiator''s Shield, Ancile, Stone of Binding, Lotus Sickle, Helm of
    Darkness, Void Stone, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.3
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.69
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.83
    Transcendence:
      total: 0.56
      efficiency: 0.5
      win: 0.83
      pick: 0.08
      fit: 0.06
    Polynomicon:
      total: 0.62
      efficiency: 0.56
      win: 0.86
      pick: 0.22
      fit: 0.17
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.89
  community_ordered:
  - Genji's Guard
  - Transcendence
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Polynomicon
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Jotunn''s
    Revenge, Kinetic Cuirass, Screeching Gargoyle, Stone of Binding, Spear of Desolation,
    Berserker''s Shield, Void Stone, Void Shield, The Reaper, Breastplate of Valor,
    Obsidian Shard, Shield Splitter, Shield of the Phoenix, Draconic Scale, Avenging
    Blade, Oni Hunter''s Garb, Spear of the Magus, The Crusher, Erosion, Eye of Providence,
    Dreamer''s Idol, Heartseeker, Shifter''s Shield, Midgardian Mail, Titan''s Bane,
    Helm of Radiance, Lotus Sickle, Doom Orb, Leviathan''s Hide, Blood-Bound Book,
    Magi''s Cloak, Mantle Of Discord, Runeforged Hammer, Helm of Darkness, Hide of
    the Nemean Lion, The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.05
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.56
      efficiency: 0.5
      win: 0.83
      pick: 0.08
      fit: 0.04
    Polynomicon:
      total: 0.61
      efficiency: 0.56
      win: 0.86
      pick: 0.22
      fit: 0.15
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.57
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Transcendence
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Transcendence
  - Tyrfing
  - Polynomicon
  - Amanita Charm
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Kinetic Cuirass,
    Tyrfing, Jotunn''s Revenge, Golden Blade, Shield Splitter, Gluttonous Grimoire,
    Breastplate of Valor, Soul Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s
    Garb, Draconic Scale, Runeforged Hammer, Shogun''s Ofuda, Pharaoh''s Curse, Erosion,
    Hydra''s Lament, Eye of Providence, Spear of Desolation, Toxic Blade, Bragi''s
    Harp, Lotus Sickle, Screeching Gargoyle, Shifter''s Shield, Midgardian Mail, Blood-Bound
    Book, The Reaper, Helm of Radiance, Eros'' Bow, Stone of Binding, Lernaean Bow,
    Dominance, Leviathan''s Hide, Silverbranch Bow, Magi''s Cloak, Mantle Of Discord,
    Hide of the Nemean Lion.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.43
    Transcendence:
      total: 0.57
      efficiency: 0.5
      win: 0.83
      pick: 0.08
      fit: 0.1
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.53
    Polynomicon:
      total: 0.61
      efficiency: 0.56
      win: 0.86
      pick: 0.22
      fit: 0.14
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Transcendence
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Prophetic Cloak
  - Transcendence
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Prophetic Cloak, Rod of Tahuti, Amanita
    Charm, Soul Gem, Jotunn''s Revenge, Kinetic Cuirass, Breastplate of Valor, Shield
    of the Phoenix, Spear of Desolation, Lotus Sickle, Berserker''s Shield, Screeching
    Gargoyle, Hydra''s Lament, Gluttonous Grimoire, Shield Splitter, Chronos'' Pendant,
    Gladiator''s Shield, Draconic Scale, Oni Hunter''s Garb, Arondight, Erosion, Eye
    of Providence, Helm of Radiance, Runeforged Hammer, Blood-Bound Book, Shifter''s
    Shield, Gem of Focus, Heartwood Charm, Helm of Darkness, Midgardian Mail, Chandra''s
    Grace, Stone of Binding, Leviathan''s Hide, Regrowth Striders, Ancient Signet,
    Magi''s Cloak, Mantle Of Discord, The Reaper, Hide of the Nemean Lion, Eye of
    Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.45
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.45
      win: 0.7
      pick: 0.12
      fit: 0.6
    Transcendence:
      total: 0.56
      efficiency: 0.5
      win: 0.83
      pick: 0.08
      fit: 0.09
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.23
      fit: 0.6
    Polynomicon:
      total: 0.62
      efficiency: 0.56
      win: 0.86
      pick: 0.22
      fit: 0.19
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Transcendence
  - Freya's Tears
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Polynomicon
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, The Reaper, Tyrfing, Runeforged Hammer, Breastplate of Valor, Golden
    Blade, Hydra''s Lament, Spear of Desolation, Shield of the Phoenix, The Crusher,
    Oni Hunter''s Garb, Draconic Scale, Heartseeker, Erosion, Eye of Providence, Tekko-Kagi,
    Death Metal, Titan''s Bane, Shifter''s Shield, Midgardian Mail, Screeching Gargoyle,
    Lotus Sickle, Bragi''s Harp, Helm of Radiance, Stone of Binding, Blood-Bound Book,
    Obsidian Shard, Avenging Blade, Leviathan''s Hide, Toxic Blade, Arondight, Nimble
    Ring, Magi''s Cloak.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.04
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.58
      efficiency: 0.5
      win: 0.83
      pick: 0.08
      fit: 0.21
    Polynomicon:
      total: 0.61
      efficiency: 0.56
      win: 0.86
      pick: 0.22
      fit: 0.14
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Transcendence
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Transcendence
  - Polynomicon
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Kinetic Cuirass, Soul Gem, Jotunn''s Revenge, Shield Splitter, Spear
    of Desolation, Berserker''s Shield, The Reaper, Breastplate of Valor, Lotus Sickle,
    Helm of Radiance, Blood-Bound Book, Runeforged Hammer, Shield of the Phoenix,
    Obsidian Shard, Death Metal, Oni Hunter''s Garb, Draconic Scale, Helm of Darkness,
    Hydra''s Lament, Spear of the Magus, Ancient Signet, The Crusher, Erosion, Eye
    of Providence, Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Shifter''s Shield,
    Midgardian Mail, Screeching Gargoyle, Tyrfing, Stone of Binding, Jade Scepter,
    Titan''s Bane, Leviathan''s Hide, Magi''s Cloak.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.17
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.21
    Transcendence:
      total: 0.58
      efficiency: 0.5
      win: 0.83
      pick: 0.08
      fit: 0.17
    Polynomicon:
      total: 0.63
      efficiency: 0.56
      win: 0.86
      pick: 0.22
      fit: 0.27
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.57
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Transcendence
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
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.2
      fit: 0.33
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.71
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.23
      fit: 0.55
    Draconic Scale:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
