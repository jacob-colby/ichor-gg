---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.29
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.42
    win_rate: 0.36
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.63
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.29
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.2
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.25
  - name: Freya's Tears
    pick_rate: 0.24
    win_rate: 0.25
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.2
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.2
  - name: Genji's Guard
    pick_rate: 0.1
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.24
      win_rate: 0.42
    - name: Sundering Echo
      pick_rate: 0.06
      win_rate: 0.33
  - name: Sundering Echo
    pick_rate: 0.07
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.5
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.67
  - name: Medal of Defense
    pick_rate: 0.11
    win_rate: 0.33
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.5
    - name: Spear of the Magus
      pick_rate: 0.07
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.31
    win_rate: 0.44
  - name: Bumba's Cudgel
    pick_rate: 0.23
    win_rate: 0.33
  - name: Bluestone Brooch
    pick_rate: 0.12
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-11-06'
  god_win_rate: 0.38461538461538464
  god_matches_won: 20
  god_matches_played: 52
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
  - Runeforged Hammer
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of the Magus
  - Amanita Charm
  flex_slots:
  - Spear of the Magus
  - Runeforged Hammer
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield Splitter, Berserker''s Shield,
    Jotunn''s Revenge, Gluttonous Grimoire, Shield of the Phoenix, Draconic Scale,
    Soul Gem, Erosion, Oni Hunter''s Garb, Eye of Providence, Hydra''s Lament, The
    Reaper, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s Hide,
    Spear of Desolation, Helm of Darkness, Magi''s Cloak, Mantle Of Discord, Helm
    of Radiance, Lotus Sickle, Blood-Bound Book, Wyrmskin Hide, Death Metal, Ancile,
    Tyrfing, Avenging Blade, Gladiator''s Shield, Void Stone, The Crusher, Arondight,
    Phoenix Feather, Breastplate of Valor.'
  slot_scores:
    Runeforged Hammer:
      total: 0.44
      efficiency: 0.55
      win: 0.36
      pick: 0.42
      fit: 0.44
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.17
      fit: 0.28
    Hide of the Nemean Lion:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.22
      fit: 0.33
    Shifter's Shield:
      total: 0.52
      efficiency: 0.5
      win: 0.56
      pick: 0.23
      fit: 0.52
    Spear of the Magus:
      total: 0.44
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.09
    Amanita Charm:
      total: 0.46
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Runeforged Hammer
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of the Magus
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Shield of the Phoenix
  - Runeforged Hammer
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Runeforged Hammer
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Rod of Tahuti, The Reaper,
    Berserker''s Shield, Jotunn''s Revenge, Blood-Bound Book, Shield Splitter, Phoenix
    Feather, Gluttonous Grimoire, Yogi''s Necklace, Ethereal Staff, Draconic Scale,
    Chandra''s Grace, Oni Hunter''s Garb, Erosion, Hydra''s Lament, Eye of Providence,
    Bloodforge, Bancroft''s Talon, Regrowth Striders, Midgardian Mail, Rod of Asclepius,
    Leviathan''s Hide, Soul Locket, Spear of Desolation, Glorious Pridwen, Avenging
    Blade, Screeching Gargoyle, Wyrmskin Hide, Lotus Sickle, Death Metal, Stone of
    Binding, Ancile, Breastplate of Valor.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.46
      efficiency: 0.57
      win: 0.33
      pick: 0.0
      fit: 0.75
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.55
      win: 0.36
      pick: 0.42
      fit: 0.5
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.17
      fit: 0.26
    Hide of the Nemean Lion:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.22
      fit: 0.35
    Shifter's Shield:
      total: 0.51
      efficiency: 0.5
      win: 0.56
      pick: 0.23
      fit: 0.5
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Runeforged Hammer
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Hide of the Nemean Lion
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, Screeching Gargoyle, Stone of Binding, The Reaper, Spear of Desolation,
    Berserker''s Shield, Shield Splitter, Avenging Blade, Void Stone, Void Shield,
    The Crusher, Heartseeker, Obsidian Shard, Shield of the Phoenix, Titan''s Bane,
    Draconic Scale, Oni Hunter''s Garb, Hydra''s Lament, Erosion, Eye of Providence,
    Dreamer''s Idol, Midgardian Mail, Lotus Sickle, Blood-Bound Book, Helm of Radiance,
    Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Doom Orb, Avatar''s Parashu,
    Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.17
      fit: 0.21
    Hide of the Nemean Lion:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.22
      fit: 0.25
    Shifter's Shield:
      total: 0.5
      efficiency: 0.5
      win: 0.56
      pick: 0.23
      fit: 0.39
    Spear of the Magus:
      total: 0.48
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.31
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.82
      win: 0.33
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Genji's Guard
  - Tyrfing
  - Shifter's Shield
  - Hide of the Nemean Lion
  flex_slots:
  - Tyrfing
  - Golden Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Tyrfing, Jotunn''s
    Revenge, Golden Blade, Shield Splitter, Gluttonous Grimoire, Soul Gem, Shield
    of the Phoenix, Oni Hunter''s Garb, Nimble Ring, Draconic Scale, Shogun''s Ofuda,
    Pharaoh''s Curse, Erosion, Hydra''s Lament, Eye of Providence, Toxic Blade, Spear
    of Desolation, Bragi''s Harp, Screeching Gargoyle, Lotus Sickle, Midgardian Mail,
    The Reaper, Blood-Bound Book, Helm of Radiance, Stone of Binding, Eros'' Bow,
    Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch Bow, Magi''s Cloak, Mantle
    Of Discord, Breastplate of Valor.'
  slot_scores:
    Golden Blade:
      total: 0.41
      efficiency: 0.51
      win: 0.33
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.43
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.17
      fit: 0.2
    Tyrfing:
      total: 0.42
      efficiency: 0.53
      win: 0.33
      pick: 0.0
      fit: 0.53
    Shifter's Shield:
      total: 0.49
      efficiency: 0.5
      win: 0.56
      pick: 0.23
      fit: 0.37
    Hide of the Nemean Lion:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.22
      fit: 0.24
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Soul Gem
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Jotunn''s Revenge, Shield of the Phoenix, Spear of Desolation, Lotus Sickle,
    Berserker''s Shield, Screeching Gargoyle, Hydra''s Lament, Gluttonous Grimoire,
    Shield Splitter, Chronos'' Pendant, Gladiator''s Shield, Draconic Scale, Oni Hunter''s
    Garb, Prophetic Cloak, Arondight, Erosion, Eye of Providence, Blood-Bound Book,
    Helm of Radiance, Breastplate of Valor, Gem of Focus, Heartwood Charm, Helm of
    Darkness, Midgardian Mail, Stone of Binding, Chandra''s Grace, Leviathan''s Hide,
    Regrowth Striders, The Reaper, Ancient Signet, Magi''s Cloak, Mantle Of Discord,
    Eye of Erebus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.42
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.6
      pick: 0.17
      fit: 0.44
    Hide of the Nemean Lion:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.22
      fit: 0.27
    Shifter's Shield:
      total: 0.5
      efficiency: 0.5
      win: 0.56
      pick: 0.23
      fit: 0.41
    Spear of the Magus:
      total: 0.45
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.12
    Soul Gem:
      total: 0.44
      efficiency: 0.58
      win: 0.33
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of the Magus
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Shield Splitter, Gluttonous Grimoire, Soul Gem, The
    Reaper, Tyrfing, Hydra''s Lament, Spear of Desolation, Shield of the Phoenix,
    Golden Blade, The Crusher, Oni Hunter''s Garb, Draconic Scale, Heartseeker, Erosion,
    Eye of Providence, Tekko-Kagi, Titan''s Bane, Death Metal, Midgardian Mail, Screeching
    Gargoyle, Lotus Sickle, Blood-Bound Book, Stone of Binding, Bragi''s Harp, Helm
    of Radiance, Obsidian Shard, Avenging Blade, Leviathan''s Hide, Arondight, Nimble
    Ring, Magi''s Cloak, Mantle Of Discord, Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.45
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.17
      fit: 0.21
    Hide of the Nemean Lion:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.22
      fit: 0.25
    Shifter's Shield:
      total: 0.5
      efficiency: 0.5
      win: 0.56
      pick: 0.23
      fit: 0.39
    Spear of the Magus:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.17
    Amanita Charm:
      total: 0.45
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of the Magus
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Soul Gem, Jotunn''s Revenge, Shield Splitter, Spear of Desolation, Berserker''s
    Shield, The Reaper, Lotus Sickle, Blood-Bound Book, Helm of Radiance, Shield of
    the Phoenix, Obsidian Shard, Death Metal, Oni Hunter''s Garb, Draconic Scale,
    Helm of Darkness, Hydra''s Lament, Ancient Signet, The Crusher, Erosion, Eye of
    Providence, Polynomicon, Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Screeching
    Gargoyle, Midgardian Mail, Stone of Binding, Jade Scepter, Titan''s Bane, Leviathan''s
    Hide, Magi''s Cloak, Mantle Of Discord, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.17
      fit: 0.21
    Hide of the Nemean Lion:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.22
      fit: 0.25
    Shifter's Shield:
      total: 0.5
      efficiency: 0.5
      win: 0.56
      pick: 0.23
      fit: 0.39
    Spear of the Magus:
      total: 0.48
      efficiency: 0.56
      win: 0.5
      pick: 0.22
      fit: 0.3
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.82
      win: 0.33
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.44
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Spear of the Magus
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
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Shield Splitter, Berserker''s
    Shield, Jotunn''s Revenge, Gluttonous Grimoire, Breastplate of Valor, Shield of
    the Phoenix, Draconic Scale, Soul Gem, Erosion, Oni Hunter''s Garb, Eye of Providence,
    Hydra''s Lament, The Reaper, Midgardian Mail, Stone of Binding, Screeching Gargoyle,
    Leviathan''s Hide, Spear of Desolation, Helm of Darkness, Magi''s Cloak, Mantle
    Of Discord, Helm of Radiance, Lotus Sickle, Blood-Bound Book, Wyrmskin Hide, Death
    Metal, Ancile, Tyrfing, Avenging Blade, Gladiator''s Shield, Void Stone, The Crusher,
    Arondight, Phoenix Feather.'
  slot_scores:
    Berserker's Shield:
      total: 0.43
      efficiency: 0.66
      win: 0.33
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.17
      fit: 0.28
    Kinetic Cuirass:
      total: 0.4
      efficiency: 0.61
      win: 0.2
      pick: 0.16
      fit: 0.62
    Freya's Tears:
      total: 0.41
      efficiency: 0.61
      win: 0.25
      pick: 0.37
      fit: 0.47
    Shield Splitter:
      total: 0.44
      efficiency: 0.58
      win: 0.33
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.46
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
