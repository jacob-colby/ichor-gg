---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.63
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
      win_rate: 0.57
  - name: Deathbringer
    pick_rate: 0.04
    win_rate: 0.66
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
  last_verified: '2026-11-04'
  god_win_rate: 0.5708502024291497
  god_matches_won: 564
  god_matches_played: 988
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
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
    Shield, Shield Splitter, Gluttonous Grimoire, Breastplate of Valor, Erosion, Eye
    of Providence, Jotunn''s Revenge, Soul Gem, Draconic Scale, Oni Hunter''s Garb,
    Shield of the Phoenix, Helm of Darkness, Stone of Binding, Magi''s Cloak, Midgardian
    Mail, Helm of Radiance, Mantle Of Discord, Leviathan''s Hide, Runeforged Hammer,
    Screeching Gargoyle, Spear of Desolation, Lotus Sickle, Ancile, Prophetic Cloak,
    Hide of the Nemean Lion, Obsidian Shard, Void Stone, Hydra''s Lament, Void Shield,
    Shifter''s Shield, Brawler’s Beat Stick, Blood-Bound Book, Xibalban Effigy, Spectral
    Armor, The Reaper, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.33
    Berserker's Shield:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.71
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.51
      pick: 0.28
      fit: 0.55
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  - Soul Gem
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Genji''s Guard, Shield of the
    Phoenix, Kinetic Cuirass, Berserker''s Shield, Gluttonous Grimoire, Blood-Bound
    Book, Phoenix Feather, The Reaper, Shield Splitter, Jotunn''s Revenge, Yogi''s
    Necklace, Ethereal Staff, Erosion, Breastplate of Valor, Eye of Providence, Oni
    Hunter''s Garb, Draconic Scale, Chandra''s Grace, Runeforged Hammer, Midgardian
    Mail, Glorious Pridwen, Leviathan''s Hide, Regrowth Striders, Bancroft''s Talon,
    Rod of Asclepius, Helm of Darkness, Helm of Radiance, Stone of Binding, Sphere
    of Negation, Spear of Desolation, Soul Locket, Lotus Sickle, Magi''s Cloak, Ancile,
    Bloodforge, Screeching Gargoyle, Hide of the Nemean Lion, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.3
    Berserker's Shield:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.69
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.89
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.75
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
  - Gluttonous Grimoire
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge, Genji''s
    Guard, Amanita Charm, Soul Gem, Stone of Binding, Kinetic Cuirass, Screeching
    Gargoyle, Berserker''s Shield, Spear of Desolation, Obsidian Shard, Void Stone,
    Void Shield, The Reaper, Shield Splitter, Avenging Blade, Titan''s Bane, Breastplate
    of Valor, Spear of the Magus, Erosion, Oni Hunter''s Garb, Eye of Providence,
    The Crusher, Doom Orb, Draconic Scale, Helm of Radiance, The World Stone, Shield
    of the Phoenix, Runeforged Hammer, Helm of Darkness, Midgardian Mail, Heartseeker,
    Magi''s Cloak, Lotus Sickle, Mantle Of Discord, Dreamer''s Idol, Leviathan''s
    Hide, Hydra''s Lament, Blood-Bound Book, Shifter''s Shield.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.56
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Genji''s Guard, Amanita Charm, Nimble
    Ring, Kinetic Cuirass, Jotunn''s Revenge, Golden Blade, Shield Splitter, Gluttonous
    Grimoire, Tyrfing, Breastplate of Valor, Soul Gem, Runeforged Hammer, Tekko-Kagi,
    Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Oni Hunter''s Garb, Hydra''s Lament,
    Eros'' Bow, Shogun''s Ofuda, Silverbranch Bow, Helm of Radiance, Erosion, Eye
    of Providence, Lotus Sickle, Stone of Binding, Obsidian Shard, Draconic Scale,
    Midgardian Mail, Spear of Desolation, Shield of the Phoenix, Helm of Darkness,
    The Reaper, Magi''s Cloak, Screeching Gargoyle, Titan''s Bane, Riptalon, Leviathan''s
    Hide, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.2
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.56
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.47
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
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Jotunn''s
    Revenge, Amanita Charm, Soul Gem, Breastplate of Valor, Kinetic Cuirass, Berserker''s
    Shield, Lotus Sickle, Spear of Desolation, Gluttonous Grimoire, Hydra''s Lament,
    Shield of the Phoenix, Shield Splitter, Screeching Gargoyle, Chronos'' Pendant,
    Arondight, Helm of Radiance, Prophetic Cloak, Runeforged Hammer, Oni Hunter''s
    Garb, Erosion, Helm of Darkness, Eye of Providence, Obsidian Shard, Draconic Scale,
    Stone of Binding, Gladiator''s Shield, Gem of Focus, Midgardian Mail, Heartwood
    Charm, Magi''s Cloak, Blood-Bound Book, Mantle Of Discord, Leviathan''s Hide,
    Regrowth Striders, The Reaper, Ancient Signet, Chandra''s Grace, Eye of Erebus,
    Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.51
      pick: 0.28
      fit: 0.6
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.52
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
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
    Revenge, Genji''s Guard, Amanita Charm, Shield Splitter, Gluttonous Grimoire,
    Kinetic Cuirass, Soul Gem, Runeforged Hammer, The Reaper, Tekko-Kagi, Golden Blade,
    Titan''s Bane, Breastplate of Valor, Hydra''s Lament, Nimble Ring, Tyrfing, Obsidian
    Shard, Spear of Desolation, The Crusher, Oni Hunter''s Garb, Lernaean Bow, Erosion,
    Avenging Blade, Helm of Radiance, Eye of Providence, Heartseeker, Toxic Blade,
    Stone of Binding, Draconic Scale, Lotus Sickle, Shield of the Phoenix, Midgardian
    Mail, Arondight, Helm of Darkness, Silverbranch Bow, Magi''s Cloak, Spear of the
    Magus, Death Metal, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.21
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.56
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.49
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Gluttonous
    Grimoire, Jotunn''s Revenge, Amanita Charm, Soul Gem, Shield Splitter, Berserker''s
    Shield, Kinetic Cuirass, Obsidian Shard, Spear of Desolation, Helm of Radiance,
    Runeforged Hammer, Breastplate of Valor, The Reaper, Lotus Sickle, Titan''s Bane,
    Helm of Darkness, Spear of the Magus, Hydra''s Lament, Blood-Bound Book, Death
    Metal, Oni Hunter''s Garb, Ancient Signet, Erosion, Eye of Providence, The Crusher,
    Doom Orb, Jade Scepter, Stone of Binding, Draconic Scale, Shield of the Phoenix,
    Midgardian Mail, Avenging Blade, The World Stone, Magi''s Cloak, Chronos'' Pendant,
    Heartseeker, Screeching Gargoyle, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.17
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.21
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.38
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.17
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
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
    Shield, Genji''s Guard, Shield Splitter, Gluttonous Grimoire, Breastplate of Valor,
    Erosion, Eye of Providence, Jotunn''s Revenge, Soul Gem, Draconic Scale, Oni Hunter''s
    Garb, Shield of the Phoenix, Helm of Darkness, Stone of Binding, Shifter''s Shield,
    Magi''s Cloak, Midgardian Mail, Helm of Radiance, Mantle Of Discord, Leviathan''s
    Hide, Runeforged Hammer, Screeching Gargoyle, Spear of Desolation, Lotus Sickle,
    Ancile, Prophetic Cloak, Hide of the Nemean Lion, Obsidian Shard, Void Stone,
    Hydra''s Lament, Void Shield, Brawler’s Beat Stick, Blood-Bound Book, Xibalban
    Effigy, Spectral Armor, The Reaper, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.6
      pick: 0.14
      fit: 0.33
    Berserker's Shield:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.71
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.51
      pick: 0.28
      fit: 0.55
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
